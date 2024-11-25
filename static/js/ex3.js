// DOM Elements
const chatMessages = document.querySelector('.chat-messages');
const messageInput = document.querySelector('.chat-input input');
const sendButton = document.querySelector('.chat-input button');
sendButton.style.backgroundColor = "grey"
const alertMessageElement = document.getElementById("alertMessage");
alertMessageElement.style.display = "none";

const wordLimit = 100;
const textEditor = document.getElementById("messageEditor");
const wordCountDisplay = document.getElementById("wordCount");
const editorButton = document.getElementById("editorSend");
editorButton.style.backgroundColor = "grey"

const overlay = document.getElementById("overlay");
overlay.style.display = "block"

let messageHistory = [];

// Function to add a new message to the chat window
function addMessage(message, isSent) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.classList.add(isSent ? 'sent' : 'received');
    chatMessages.appendChild(messageElement);

    // Scroll to the bottom of chat
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // If it's a sent message, add the text content immediately
    if (isSent) {
        messageElement.textContent = message;
        messageHistory.push({
            "role": "user",
            "content": message
        })
    }

    console.log(messageHistory)
    return messageElement;
}

function streamTextIntoElement(element, text) {
    return new Promise((resolve) => {
        let index = 0;
        function addNextChar() {
            if (index < text.length) {
                element.textContent += text[index];
                index++;
                // Control stream speed
                setTimeout(addNextChar, 10);

                // Scroll to the bottom as new content is added
                chatMessages.scrollTop = chatMessages.scrollHeight;
            } else {
                resolve();
            }
        }
        addNextChar();
    });
}

async function sendMessageToAPI(message, messageElement, flag) {
    let response = null;
    if (flag) {
        response = await fetch('/send_message',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "user_prompt": message,
                    "exercise": 3
                }),
                history: JSON.stringify(messageHistory)
            }
        )
    }
    else {
        response = await fetch('/send_message',
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    "user_prompt": message,
                    "exercise": 3
                }),
                history: null
            }
        )
    }

    const reader = response.body.getReader();
    const decoder = new TextDecoder('utf-8');
    let buffer = '';

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
            const trimmedLine = line;
            if (trimmedLine.startsWith('data: ')) {
                const data = trimmedLine.slice(6);
                if (data === '[DONE]') {
                    return;
                }
                //console.log(data)
                try {
                    const content = data;
                    //console.log(content)
                    if (content) {
                        await streamTextIntoElement(messageElement, content);
                    }
                } catch (error) {
                    console.error('Error parsing JSON:', error);
                }
            }
        }
    }
    messageHistory.push({
        "role": "assistant",
        "content": messageElement.textContent
    })
    console.log(messageHistory)
}

function showMessage() {
    alertMessageElement.style.display = "flex"
    alertMessageElement.style.color = "red"
    //alert("This button is disabled.");
}

// Function to handle sending a message
async function handleSendMessage(flag) {
    const message = messageInput.value.trim();

    // if (!flag) {
    //     overlay.style.display = "none";
    // }

    if (message) {
        try {
            // Clear input immediately
            messageInput.value = '';

            // Add user's message to chat
            addMessage(message, true);

            // Disable input and button while waiting for response
            messageInput.disabled = true;
            sendButton.disabled = true;

            // Create an empty message element for the llm response
            const aiMessageElement = addMessage('', false);

            // Send message to API and stream the response
            if (flag) {
                await sendMessageToAPI(message, aiMessageElement, true)
            }
            else {
                await sendMessageToAPI(message, aiMessageElement, false);
            }

        } catch (error) {
            console.error('Error:', error);
            // Handle error - add error message to chat
            addMessage('Sorry, there was an error sending your message. Please try again.', false);
        } finally {
            // Re-enable input and button
            messageInput.disabled = false;
            sendButton.disabled = false;
            messageInput.focus();
        }
    }
}

// Event Listeners
sendButton.addEventListener('click', handleSendMessage);

// Handle Enter key
messageInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault(); // Prevent default to avoid new line
        handleSendMessage(false);
    }
});

// loading state
function setLoadingState(isLoading) {
    if (isLoading) {
        sendButton.innerHTML = '<span>Sending...</span>';
        sendButton.disabled = true;
    } else {
        sendButton.innerHTML = 'Send';
        sendButton.disabled = false;
    }
}

function showTypingIndicator() {
    const typingElement = document.createElement('div');
    typingElement.classList.add('message', 'received', 'typing');
    typingElement.innerHTML = 'Bot is typing...';
    chatMessages.appendChild(typingElement);
    chatMessages.scrollTop = chatMessages.scrollHeight;
    return typingElement;
}

window.addEventListener('online', () => {
    addMessage('Connection restored', false);
});

window.addEventListener('offline', () => {
    addMessage('Connection lost. Please check your internet connection.', false);
});
function handleStart() {
    document.getElementById('welcomeScreen').style.display = 'none';
    document.getElementById('splitScreen').classList.add('active');
}

function handleRestart() {
    const messages = document.querySelector('.chat-messages');
    while (messages.children.length > 1) {
        messages.children[1].remove();
    }
    document.getElementById('splitScreen').classList.remove('active');
    document.getElementById('welcomeScreen').style.display = 'flex';
    document.getElementById('messageEditor').value = '';
}

function clearEditor() {
    document.getElementById('messageEditor').value = '';
}

function sendFromEditor() {
    const editorContent = document.getElementById('messageEditor').value.trim();
    if (editorContent) {
        document.getElementById('chatInput').value = editorContent;
        handleSendMessage(true);
        clearEditor();
        editorButton.disabled = true
        sendButton.disabled = true
        wordCountDisplay.textContent = `Word count: ${0}`;
        wordCountDisplay.style.color = "red"; // Under the limit
        alertMessageElement.style.display = "none";

        editorButton.style.backgroundColor = "grey"
        sendButton.style.backgroundColor = "grey"
        overlay.style.display = "block"
    }
}

async function fetchSuggestions() {
    try {
        const response = await fetch('/api/suggestions_ex3');
        const words = await response.json();
        populateSuggestions(words);
    } catch (error) {
        console.error('Error fetching suggestions:', error);
        // Fallback sample data
        populateSuggestions(['Hello', 'How are you', 'What is this', 'Tell me more', 'Help']);
    }
}

function populateSuggestions(words) {
    const container = document.getElementById('suggestionContainer');
    words.forEach(word => {
        const button = document.createElement('button');
        button.className = 'suggestion-button';
        button.textContent = word;
        button.onclick = () => {
            document.getElementById('chatInput').value = "Write a short essay about " + word;
        };
        container.appendChild(button);
    });
}

function cycleButtons(direction) {
    const container = document.getElementById('suggestionContainer');
    const scrollAmount = direction === 'left' ? -200 : 200;
    container.scrollBy({
        left: scrollAmount,
        behavior: 'smooth'
    });
}


textEditor.addEventListener("input", () => {
    const text = textEditor.value.trim();
    const words = text.split(/\s+/).filter(word => word.length > 0);
    const wordCount = words.length;

    // Update word count display
    wordCountDisplay.textContent = `Word count: ${wordCount}`;

    // Change word count text color based on limit
    if (wordCount <= wordLimit) {
        editorButton.disabled = true
        sendButton.disabled = true
        wordCountDisplay.style.color = "red"; // Under the limit
        alertMessageElement.style.display = "none";

        editorButton.style.backgroundColor = "grey"
        sendButton.style.backgroundColor = "grey"
        overlay.style.display = "block"
    } else {
        editorButton.disabled = false
        sendButton.disabled = false
        wordCountDisplay.style.color = "black"; // Over the limit

        editorButton.style.backgroundColor = "#007bff"
        sendButton.style.backgroundColor = "#007bff"
        overlay.style.display = "none";
    }
});

// Initialize suggestions when page loads
document.addEventListener('DOMContentLoaded', fetchSuggestions);
