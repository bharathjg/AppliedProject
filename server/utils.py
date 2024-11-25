#######

def separate_text_string(text):
    """
    Separates text into main content and errors section using string methods.
    
    Args:
        text (str): Input text containing main content and errors
        
    Returns:
        tuple: (main_content, errors_section)
    """
    if 'Errors:' in text:
        parts = text.split('Errors:', 1)
        return parts[0].strip(), parts[1].strip()
    return text, ''