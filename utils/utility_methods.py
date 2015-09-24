def is_palindrome(alphanumeric):
    is_palindrome_boolean = True
    alphanumeric_string = str(alphanumeric)
    alphanumeric_string_length = alphanumeric_string.__len__()
    for start_position in range(0, alphanumeric_string_length):
        end_position = alphanumeric_string_length - 1 - start_position  # string is zero indexed but string length is one indexed
        if end_position < start_position:
            return is_palindrome_boolean
        else:
            if alphanumeric_string[start_position] != alphanumeric_string[end_position]:
                return False
