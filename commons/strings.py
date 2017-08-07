def split_str_into_len(s, l):
    return [s[i:i+l] for i in range(0, len(s), l)]


def padding_to_multiple_len(str, multiple):
    while True:
        if(len(str) % multiple == 0):
            break
        else:
            str += '0'

    return str

