def remove_consecutive_duplicates(s):
    if not s:
        return s
    result = s[0]
    for ch in s[1:]:
        if ch != result[-1]:
            result += ch
    return result
input_str = input("Enter a word: ")
print(remove_consecutive_duplicates(input_str))