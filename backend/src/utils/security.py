"""
Security utilities for sanitizing sensitive data in logs and error messages.
"""
import re


def sanitize_api_key(text: str, key_value: str = None) -> str:
    """
    Sanitizes API keys from text by replacing them with masked versions.
    
    Args:
        text: The text that might contain API keys
        key_value: Optional specific key value to sanitize
        
    Returns:
        Text with API keys masked
    """
    if not text:
        return text
    
    # If a specific key value is provided, mask it
    if key_value and len(key_value) > 8:
        # Show first 4 and last 4 characters, mask the rest
        masked = f"{key_value[:4]}...{key_value[-4:]}"
        text = text.replace(key_value, masked)
    
    # Pattern-based sanitization for common API key formats
    # OpenAI keys: sk-... or sk-proj-...
    text = re.sub(r'sk-[a-zA-Z0-9\-]{20,}', 'sk-****REDACTED****', text)
    
    # Generic long alphanumeric strings that look like keys (20+ chars)
    # Be conservative to avoid false positives
    text = re.sub(r'\b[a-zA-Z0-9_\-]{32,}\b', '****REDACTED****', text)
    
    return text


def sanitize_error_message(error: Exception, sensitive_values: list = None) -> str:
    """
    Creates a sanitized error message safe for logging.
    
    Args:
        error: The exception to sanitize
        sensitive_values: List of sensitive values (like API keys) to redact
        
    Returns:
        Sanitized error message
    """
    message = str(error)
    
    # Sanitize any provided sensitive values
    if sensitive_values:
        for value in sensitive_values:
            if value and len(value) > 8:
                masked = f"{value[:4]}...{value[-4:]}"
                message = message.replace(value, masked)
    
    # Apply pattern-based sanitization
    message = sanitize_api_key(message)
    
    return message
