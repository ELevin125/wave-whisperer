def bits_to_string(bit_list):
    string = ""
    for i in range(0, len(bit_list), 8):
        # Extract 8 bits at a time and convert them to a number
        bits = bit_list[i: i + 8]
        bit_string = "".join(map(str, bits))
        
        # Remove any non-binary characters
        bit_string = "".join(c for c in bit_string if c in "01")
        
        # Check if the filtered string is empty
        if not bit_string:
            break
        
        # Convert the number value to a character and append to the string
        num_value = int(bit_string, 2)
        character = chr(num_value)
        string += character
    return string

def string_to_bits(string):
    bit_list = []
    for character in string:
        ascii_value = ord(character)
        binary_val = bin(ascii_value).lstrip("0b").rjust(8, "0")
        bit_list.append(binary_val)

    bits = map(int, "".join(bit_list))
    return list(bits)