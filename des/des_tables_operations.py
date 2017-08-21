def bit_permutation(bit_string, permutation_table):
    permuted_string = ""

    for position in permutation_table:
        permuted_string += bit_string[position - 1]

    return permuted_string


def six_bits_to_four_bits(six_bits_string, convertion_matrix):
    line = int(six_bits_string[0] + six_bits_string[5], 2)
    column = int(six_bits_string[1:5], 2)

    four_bits_string = convertion_matrix[line][column]

    return '{0:04b}'.format(four_bits_string)