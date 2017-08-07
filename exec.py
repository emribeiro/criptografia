from commons import conversor, bitwise_operations,strings
from des import des_tables_operations, des_tables



def main():
    #data = "Testes"
    #hex_data = conversor.ascii_to_hex(data)
    #binary_data = conversor.hex_to_binary(hex_data)
    #hex_data_rev = conversor.binary_to_hex(binary_data)
    #print("Data: {}".format(data))
    #print("Hex Data: {}".format(hex_data))
    #print("Binary Data: {}".format(binary_data))
    #print("Hex Data Rev: {}".format(hex_data_rev))

    #print(bitwise_operations.bitwise_XOR("1111", "0101"))

    #print(des_tables_operations.bit_permutation("0011", [3,4,1,2]))

    #print(des_tables_operations.six_bits_to_four_bits("111011", des_tables.s1))

    #print(strings.split_str_into_len("teste", 2))

    print(strings.padding_to_multiple_len('00', 9))
if __name__ == "__main__":
    main()

