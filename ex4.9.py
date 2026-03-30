def caesar_cipher(filename, shift_positions, direction):
    if direction.lower() == 'left':
        shift_positions = -shift_positions
    elif direction.lower() != 'right':
        print("must be 'left' or 'right'")
        return
    output_filename = "cipher_" + filename
    with open(filename, 'r', encoding='utf-8') as f_in, open(output_filename, 'w', encoding='utf-8') as f_out:
        text = f_in.read()
        result = []
        for char in text:
            if char.isupper():
                x = ord(char) - 65
                y = (x + shift_positions) % 26 + 65
                result.append(chr(y))
            elif char.islower():
                x = ord(char) - 97
                y = (x + shift_positions) % 26 + 97
                result.append(chr(y))
            elif not char.isdigit():
                result.append(char)

        f_out.write("".join(result))

    print(f"file saved: {output_filename}")