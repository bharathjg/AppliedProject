// DOM Elements
const chatMessages = document.querySelector('.chat-messages');
const messageInput = document.querySelector('.chat-input input');
const sendButton = document.querySelector('.chat-input button');

function addMessage(message, isSent, isHidden = false) {
    // Main message container
    const messageContainer = document.createElement('div');
    messageContainer.classList.add('message-container');
    // Alignment class based on message type
    messageContainer.classList.add(isSent ? 'sent-container' : 'received-container');

    // message element
    const messageElement = document.createElement('div');
    messageElement.classList.add('message');
    messageElement.classList.add(isSent ? 'sent' : 'received');
    messageElement.textContent = message;

    // styling for hidden message
    if (isHidden) {
        messageElement.style.display = 'none';

        // Create reveal button
        const revealButton = document.createElement('button');
        revealButton.classList.add('reveal-button');
        revealButton.textContent = 'Show Message';

        // click handler to reveal button
        revealButton.addEventListener('click', function () {
            messageElement.style.display = 'block';
            revealButton.style.display = 'none';

            // Scroll to the bottom after revealing
            chatMessages.scrollTop = chatMessages.scrollHeight;
        });

        // Add button to container
        messageContainer.appendChild(revealButton);
    }

    // Add message element to container
    messageContainer.appendChild(messageElement);

    // Add container to chat window
    chatMessages.appendChild(messageContainer);

    // Scroll to the bottom of chat
    chatMessages.scrollTop = chatMessages.scrollHeight;

    return messageElement;
}

function streamTextIntoElement(element, text) {
    return new Promise((resolve) => {
        let index = 0;
        function addNextChar() {
            if (index < text.length) {
                element.textContent += text[index];
                index++;
                setTimeout(addNextChar, 10);

                chatMessages.scrollTop = chatMessages.scrollHeight;
            } else {
                resolve();
            }
        }
        addNextChar();
    });
}


async function sendMessageToAPI(message, messageElement) {
    const response = await fetch('/send_message',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                "user_prompt": message,
                "exercise": 1
            })
        }
    )

    const reader = response.body.getReader();
    const decoder = new TextDecoder('utf-8');
    let buffer = '';
    flag = true
    error_content = '';

    while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop();

        for (const line of lines) {
            const trimmedLine = line
            if (trimmedLine.startsWith('data: ')) {
                const data = trimmedLine.slice(6);
                if (data == 'Errors') {
                    flag = false
                }
                if (data === '[DONE]') {
                    return;
                }
                //console.log(data)
                try {
                    const content = data;
                    //console.log(content)
                    if (content && flag) {
                        await streamTextIntoElement(messageElement, content);
                    }
                    else {
                        error_content += content
                    }
                } catch (error) {
                    console.error('Error parsing JSON:', error);
                }
            }
        }
    }
    error_to_display = processErrorText(error_content)
    const listElement = document.createElement("ul");
    error_to_display.forEach(line => {
        const listItem = document.createElement('li');
        listItem.textContent = line;
        listElement.appendChild(listItem);
    })

    addMessage('', false, true).appendChild(listElement);
}

function isNumeric(char) {
    return !isNaN(char);
}
function processErrorText(text) {
    const errorPattern = /\d+\.\s*(.*?)(?=\d+\.|$)/g; // Regex to match "1. ...", stopping at "2." or the end
    const errors = [];
    let match;

    while ((match = errorPattern.exec(text)) !== null) {
        errors.push(match[1].trim());
    }

    return errors;
}

// Function to handle sending a message
async function handleSendMessage() {
    const message = messageInput.value.trim();

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
            await sendMessageToAPI(message, aiMessageElement);

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
        handleSendMessage();
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
    // Hide welcome screen
    document.getElementById('welcomeScreen').style.display = 'none';

    // Show chat window
    document.getElementById('chatWindow').classList.add('active');

    console.log('Start clicked');
}

function handleRestart() {
    // Get all messages in the chat window
    const messages = chatMessages.getElementsByClassName('message');

    // Remove all messages except the first one
    while (messages.length > 1) {
        messages[1].remove();  // Always remove the second message, keeping the first one intact
    }

    // Hide chat window and show welcome screen
    document.getElementById('chatWindow').classList.remove('active');
    document.getElementById('welcomeScreen').style.display = 'flex';

    console.log('Restart clicked');
}
async function fetchSuggestions() {
    try {
        const response = await fetch('/api/suggestions_ex1');
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
            document.getElementById('chatInput').value = "Generate a biography for " + word;
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
// Initialize suggestions when page loads
document.addEventListener('DOMContentLoaded', fetchSuggestions);
