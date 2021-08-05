from array import array

global memory
memory = array('L', [0]) * (1 * 1024*1024//4)   
                        # 1 MByte = 1048576 Bytes = 
                        # 262144 palavras (words)
                        # 1 word = 4 bytes (32 bits)
                        # 18 bits de endereçamento

def read_word(add):
    add = add & 0b111111111111111111
    return memory[add]

def write_word(add, val):
    add = add & 0b111111111111111111
    memory[add] = val

def read_byte(add):
    word = add >> 2       #(endereço / 4)
    byte = add & 0b11     #(resto da divisão por 4)
    byte_sft = byte << 3  #(multiplicação por 8)

    val = read_word(word)
    val = val >> byte_sft
    val = val & 0x000000FF

    return val

def write_byte(add, val):         
    word_address = add >> 2
    word_address = word_address & 0b111111111111111111
    byte = add & 0b11
    byte_sft = byte << 3

    mask = ~(0xFF << byte_sft)        
    valr  = memory[word_address] & mask            
    val   = val << byte_sft        

    memory[word_address] = (val | valr)
