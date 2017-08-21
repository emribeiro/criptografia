
def bitwise_xor(value1, value2):
    i = 0
    resultado = ""
    for x in value1:
        a = int(x)
        b = int(value2[i])
        resultado += str(a ^ b)
        i = i + 1

    return resultado


def left_shift(value, shift_times):

    new_value = ['' for x in value]
    end = len(new_value) - 1
    new_value[0] = value[0]
    new_value[len(new_value) - 1] = value[len(value) - 1]

    for y in range(0, shift_times):
        for x in range(1, end):
            pos = x + 1
            if pos > end - 1:
                pos = 1
            new_value[x] = value[pos]

        new_value[0], new_value[len(new_value) - 1] = new_value[len(new_value) - 1], new_value[0]
        value = list(new_value)

        print(new_value)


