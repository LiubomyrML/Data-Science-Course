def concat_all_strings(*strings):
    result = ""
    for str in strings:
        result += str + " "
    return result