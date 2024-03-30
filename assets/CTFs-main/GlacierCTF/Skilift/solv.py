# Given final tmp4 value
tmp4_final = 0x5443474D489DFDD3

# Stage 4 reverse: Adding 12345678 to tmp4_final
tmp3_reversed = tmp4_final + 12345678

# Stage 3 reverse: XOR tmp3_reversed with "HACKERS!"
tmp2_reversed = tmp3_reversed ^ int.from_bytes(b'HACKERS!', byteorder='big')

# Stage 2 reverse: Right shift tmp2_reversed by 5
tmp1_reversed = tmp2_reversed >> 5

# Stage 1 reverse: Finding key by bitwise AND with 64'hF0F0F0F0F0F0F0F0
key_reversed = tmp1_reversed & 0xF0F0F0F0F0F0F0F0

# Print the key in hexadecimal format
print(hex(key_reversed))
