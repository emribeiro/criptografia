
def bitwise_xor(value1, value2):
    i = 0
    resultado = ""
    for x in value1:
        a = int(x)
        b = int(value2[i])
        resultado += str(a ^ b)
        i = i + 1

    return resultado


def bitwise_left_shift(value, shift_times):
    pass



