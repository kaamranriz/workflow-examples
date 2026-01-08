"""
String utility functions for testing the Test Generator workflow.
Contains various string manipulation functions.
"""

import re
from typing import List, Optional


def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome (ignoring case and spaces)."""
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]


def count_words(text: str) -> int:
    """Count the number of words in a text."""
    if not text.strip():
        return 0
    return len(text.split())


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """Truncate text to max_length, adding suffix if truncated."""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def find_all_occurrences(text: str, pattern: str) -> List[int]:
    """Find all starting indices of pattern in text."""
    indices = []
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            break
        indices.append(index)
        start = index + 1
    return indices


def extract_emails(text: str) -> List[str]:
    """Extract all email addresses from text."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug."""
    # Convert to lowercase
    slug = text.lower()
    # Replace spaces and special chars with hyphens
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    return slug


def remove_duplicates(text: str) -> str:
    """Remove duplicate words from text while preserving order."""
    seen = set()
    words = []
    for word in text.split():
        if word.lower() not in seen:
            seen.add(word.lower())
            words.append(word)
    return ' '.join(words)


class TextAnalyzer:
    """Analyze text for various statistics."""

    def __init__(self, text: str):
        self.text = text

    def char_count(self, include_spaces: bool = True) -> int:
        """Count characters in text."""
        if include_spaces:
            return len(self.text)
        return len(self.text.replace(' ', ''))

    def word_frequency(self) -> dict:
        """Return frequency of each word."""
        freq = {}
        for word in self.text.lower().split():
            word = re.sub(r'[^a-z0-9]', '', word)
            if word:
                freq[word] = freq.get(word, 0) + 1
        return freq

    def most_common_word(self) -> Optional[str]:
        """Return the most common word."""
        freq = self.word_frequency()
        if not freq:
            return None
        return max(freq, key=freq.get)

    def sentence_count(self) -> int:
        """Count sentences (ending with . ! or ?)."""
        return len(re.findall(r'[.!?]+', self.text))


