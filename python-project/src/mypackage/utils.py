"""
Utility functions for the package.
"""

from datetime import datetime
from typing import Optional


def format_greeting(name: str, title: Optional[str] = None) -> str:
    """
    Format a greeting message.

    Args:
        name: The name to greet
        title: Optional title (e.g., "Mr.", "Ms.", "Dr.")

    Returns:
        A formatted greeting string
    """
    if title:
        return f"Hello, {title} {name}!"
    return f"Hello, {name}!"


def get_timestamp() -> str:
    """
    Get the current timestamp as an ISO formatted string.

    Returns:
        ISO formatted timestamp string
    """
    return datetime.now().isoformat()


def is_even(number: int) -> bool:
    """
    Check if a number is even.

    Args:
        number: The number to check

    Returns:
        True if the number is even, False otherwise
    """
    return number % 2 == 0


def reverse_string(text: str) -> str:
    """
    Reverse a string.

    Args:
        text: The string to reverse

    Returns:
        The reversed string
    """
    return text[::-1]


if __name__ == "__main__":
    # Example usage
    print(format_greeting("Alice"))
    print(format_greeting("Bob", "Dr."))
    print(f"Current timestamp: {get_timestamp()}")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Is 5 even? {is_even(5)}")
    print(f"Reverse 'hello': {reverse_string('hello')}")
