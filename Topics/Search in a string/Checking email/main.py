def check_email(string):
    if string.find("@.") > -1:
        return False

    if string.find(" ") > -1:
        return False

    start_index = string.find("@")
    if start_index > -1:
        if string.find(".", start_index, len(string) - 1) == -1:
            return False
    else:
        return False

    return True
