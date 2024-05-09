#!/usr/bin/python3
"""UTF-8 validation module."""

def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints."""
    skip = 0
    for i, val in enumerate(data):
        if skip:
            skip -= 1
            continue
        if not isinstance(val, int) or val < 0 or val > 0x10FFFF:
            return False
        elif val <= 0x7F:
            continue
        elif val & 0xF8 == 0xF0:
            # 4-byte utf-8 character encoding
            span = 4
        elif val & 0xF0 == 0xE0:
            # 3-byte utf-8 character encoding
            span = 3
        elif val & 0xE0 == 0xC0:
            # 2-byte utf-8 character encoding
            span = 2
        else:
            return False

        if len(data) - i < span:
            return False

        for j in range(i + 1, i + span):
            if not (data[j] & 0xC0 == 0x80):
                return False
        skip = span - 1

    return True

