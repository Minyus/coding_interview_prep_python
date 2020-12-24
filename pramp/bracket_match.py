def bracket_match(text):

    n = len(text)
    unexpected = 0
    count = 0

    for i in range(n):
        if text[i] == "(":
            count += 1
        elif count > 0:
            count -= 1
        else:
            unexpected += 1

    return count + unexpected
