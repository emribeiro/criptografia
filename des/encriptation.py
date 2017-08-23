from commons import conversor, strings, bitwise_operations
from des import des_tables, des_tables_operations

def des_encript(data, key):
    subkeys = subkey_creation(key)


def subkey_creation(key):
    binary_key = conversor.hex_to_binary(key)
    key_first_permutation = des_tables_operations.bit_permutation(binary_key,des_tables.pc_1)
    key_first_permutation_halfs = strings.split_str_into_len(key_first_permutation, 28)
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    pos = 1

    subkeys = []
    subkeys.append(key_first_permutation_halfs)
    for shift in shifts:
        print()
        subkeys.append([bitwise_operations.left_shift(subkeys[pos-1][0], shift)
                       , bitwise_operations.left_shift(subkeys[pos-1][1], shift)])
        pos += 1

    print(subkeys)
    return subkeys
