def is_valid(config):
    """Return True if every (), [], {} is properly matched and nested."""
    matching_opener = {")": "(", "]": "[", "}": "{"}
    unmatched_openers = []

    for symbol in config:
        if symbol in matching_opener.values():  # opening: (, [, {
            unmatched_openers.append(symbol)
        elif symbol in matching_opener:  # closing: ), ], }
            if not unmatched_openers or unmatched_openers[-1] != matching_opener[symbol]:
                return False
            unmatched_openers.pop()
        else:
            # ignore anything that isn't a grouping symbol (optional)
            continue

    return not unmatched_openers


if __name__ == "__main__":
    print(is_valid("{[()()]}"))  # True
    print(is_valid("{[(])}"))    # False
    print(is_valid("(("))        # False
