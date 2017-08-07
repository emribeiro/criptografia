#Attention: All operations is coded in ASCII

import binascii

# Convert ASCII string into HEX string
def ascii_to_hex(ascii_str):
    ascii_data = ascii_str.encode("ascii")
    return binascii.hexlify(ascii_data).decode('ascii')


# Convert HEX String into ASCII string
def hex_to_ascii(hex_str):
    hex_data = hex_str.encode('ascii')
    return binascii.unhexlify(hex_data).decode('ascii')


# Convert a HEX string into binary String
def hex_to_binary(hex_string):
    binary_data = bin(int(hex_string,16))[2:]
    binary_data_len = len(binary_data)
    hex_string_len = len(hex_string)

    complementary_len = (hex_string_len * 4) - binary_data_len
    complement_bin = ""

    for x in range(0, complementary_len):
        complement_bin += "0"

    return complement_bin + binary_data


# Convert a Binary String into a HEX String
def binary_to_hex(binary_string):
    return hex(int(binary_string, 2))[2:]

