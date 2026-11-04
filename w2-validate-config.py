def is_valid(s):
    """Return True if every (), [], {} is properly matched and nested."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in s:
        if ch in pairs.values():  # opening: (, [, {
            stack.append(ch)
        elif ch in pairs:  # closing: ), ], }
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            # ignore anything that isn't a grouping symbol (optional)
            continue

    return not stack


if __name__ == "__main__":
    print(is_valid("{[()()]}"))  # True
    print(is_valid("{[(])}"))    # False
    print(is_valid("(("))        # False
