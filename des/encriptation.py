from commons import conversor, strings
from des import des_tables, des_tables_operations

def des_encript(data, key):
    subkeys = subkey_creation(key)


def subkey_creation(key):
    binary_key = conversor.hex_to_binary(key)
    key_first_permutation = des_tables_operations.bit_permutation(binary_key,des_tables.pc_1)
    key_first_permutation_halfs = strings.split_str_into_len(key_first_permutation, 28)
    print(key_first_permutation_halfs)
