from array import array
global memory

memory = array('L', [0]) * (1 * 1024*1024//4)
            # 1 MByte = 1048576 Bytes => / 4 = 262144 palavras (words)
            # 1 word = 4 bytes (32 bits) 
            # 18 bits de endereçamento

def read_word(add):
    add = add & 0b111111111111111111 # pega somente 18 bits do add
    return memory[add]

def write_word(add, val):
    add = add & 0b111111111111111111
    memory[add] = val

def read_byte(add):
    word = add >> 2     # endereço / 4
    byte = add & 0b11   # endereco % 4
    byte_sft = byte << 3    # multiplicação por 8 (1 byte)

    word = word & 0b111111111111111111 
    val = memory[word]
    val = val >> byte_sft
    val = val & 0xFF

    return val

def write_byte(add, val):           # val = 10001011
    word_address = add >> 2
    byte = add & 0b11
    byte_sft = byte << 3

    valr = read_word(word_address)  # 11111010100010111000001110101011
    mask = 0xFF                     # 00000000000000000000000011111111
    mask = mask << byte_sft         # 00000000111111110000000000000000
    mask = ~mask                    # 11111111000000001111111111111111
    valr = valr & mask              # 11111010000000001000001110101011
    val = val << byte_sft           # 00000000100010110000000000000000
    valr = val | valr               # 11111010100010111000001110101011

    write_word(word_address, valr)
