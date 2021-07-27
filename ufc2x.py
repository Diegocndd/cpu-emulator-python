from array import array
import memory

MIR = 0
MPC = 0

MAR = 0
MDR = 0
PC  = 0
MBR = 0
X   = 0
Y   = 0
H   = 0
K   = 0

N   = 0
Z   = 1

BUS_A = 0
BUS_B = 0
BUS_C = 0


# INSTRUÇÃO DE 35 BITS:
# 000000000 000    00          000000  000000         000               000          000
# NEXT_ADD  JMPC   DESLOCADOR  ULA     REGISTRADORES  READ/WRITE/FETCH  BARRAMENTO B BARRAMENTO A

firmware = array('Q', [0]) * 512

#main
firmware[0] = 0b000000000100001101010010000001001000 
            #PC <- PC + 1; MBR <- read_byte(PC); GOTO MBR;

#X = X + mem[address]
firmware[2] = 0b000000011000001101010010000001001000 
            #PC <- PC + 1; MBR <- read_byte(PC); GOTO 3
firmware[3] = 0b000000100000000101001000000010010000 
            #MAR <- MBR; read_word; GOTO 4
firmware[4] = 0b000000101000000101000000010000000000 
            #H <- MDR; GOTO 5
firmware[5] = 0b000000000000001111000001000000011000 
            #X <- X + H; GOTO MAIN;

#mem[address] = X
firmware[6] = 0b000000111000001101010010000001001000 
            #PC <- PC + 1; fetch; GOTO 7
firmware[7] = 0b000001000000000101001000000000010000 
            #MAR <- MBR; GOTO 8
firmware[8] = 0b000000000000000101000100000100011000 
            #MDR <- X; write; GOTO MAIN

#goto address
firmware[9]  = 0b000001010000001101010010000001001000 
            #PC <- PC + 1; fetch; GOTO 10
firmware[10] = 0b000000000100000101000010000001010000 
            #PC <- MBR; fetch; GOTO MBR;

#if X = 0 goto address
firmware[11]  = 0b000001100001000101000001000000011000 
            #X <- X; IF ALU = 0 GOTO 268 (100001100) ELSE GOTO 12 (000001100);
firmware[12]  = 0b000000000000001101010010000000001000 
            #PC <- PC + 1; GOTO MAIN;
firmware[268] = 0b100001101000001101010010000001001000 
            #PC <- PC + 1; fetch; GOTO 269
firmware[269] = 0b000000000100000101000010000001010000 
            #PC <- MBR; fetch; GOTO MBR;

# X = X - mem[address]
firmware[13] = 0b000001110000001101010010000001001000 
            # PC <- PC + 1; fetch;
firmware[14] = 0b000001111000000101001000000010010000 
            # MAR <- MBR; read;
firmware[15] = 0b000010000000000101000000010000000000
            # H <- MDR;
firmware[16] = 0b000000000000001111110001000000011000 
            # X <- X - H; GOTO MAIN;

# Y = Y + mem[adress]
firmware[17] = 0b000010010000001101010010000001001000 
            # PC <- PC + 1; MBR <- read_byte(PC); GOTO 18
firmware[18] = 0b000010011000000101001000000010010000 
            # MAR <- MBR; read_word; GOTO 19
firmware[19] = 0b000010100000000101000000010000000000 
            # H <- MDR; GOTO 20
firmware[20] = 0b000000000000001111000000100000100000 
            # Y <- Y + H; GOTO MAIN;

# H = X * Y
firmware[21] =0b000010110000000100000000010000000000
            # H <- 0; GOTO 22
firmware[22]= 0b000010111001000101000000000000011111
            # IF ALU=0 Goto 279 ;ELSE Goto 23
firmware[279]=0b000000000000001101010000000001001000 
            # GOTO MAIN
firmware[23]= 0b000011000001000101000000000000100111
            # IF ALU=0 Goto 280 ;ELSE Goto 24
firmware[280]=0b000000000000001101010000000001001000
            # GOTO MAIN
firmware[24]= 0b000011001000001111000000010000011000
            # H<- H + X; GOTO 23
firmware[25] =0b000011010000001101100000100000100111
            # Y <- Y - 1; GOTO 24
firmware[26] =0b000011000001000101000000000000100111
            # IF ALU = 0 GOTO 278;ELSE GOTO 24
firmware[282]=0b000000000000001101010000000001001000
            # GOTO MAIN

# H = X / Y
firmware[27]= 0b000011100000000100000000010000000000
            # H<-0 
firmware[28]= 0b000011101001000101000000000000100111    
            # IF Y=0 GOTO 285; ELSE GOTO 29  
firmware[285]=0b011111111000001101010000000001001000
            # GOTO HALT
firmware[29]= 0b000011110001000101000000000000011111 
            # IF X=0 GOTO 286; ELSE GOTO 30
firmware[286]=0b000000000000001101010000000001001000
            # GOTO MAIN
firmware[30]= 0b000011111000000100000000001000000111
            # K<-0
firmware[31]= 0b000100000000001110010000001000000011
            # K<-K+1
firmware[32]= 0b000100001001001111110000000000100011
            # IF Y-K=0 GOTO 289;ELSE GOTO 33
firmware[289]=0b000100010000001101010000000000111111
            # GOTO 34
firmware[33]= 0b000011111001001111110000000000011011
            # IF (X-K)=0 GOTO 289 ;ELSE GOTO 31
firmware[287]=0b000000000000001101010000000001001000
            # GOTO MAIN
firmware[34]= 0b000100011000001111110001000000011010
            # X<-X-Y
firmware[35]= 0b000011101000001110010000010000111000
            # H <- H+1

def read_regs(reg_numA, reg_numB):
    global BUS_A, BUS_B, H, MDR, PC, MBR, X, Y,K

    if reg_numA == 0:
        BUS_A = H
    if reg_numA == 1:
        BUS_A  = X
    if reg_numA == 2:
        BUS_A = Y
    if reg_numA==3:
        BUS_A= K
    if reg_numA == 7:
        BUS_A = 0

    if reg_numB == 0:
        BUS_B = MDR
    elif reg_numB == 1:
        BUS_B = PC
    elif reg_numB == 2:
        BUS_B = MBR
    elif reg_numB == 3:
        BUS_B = X
    elif reg_numB == 4:
        BUS_B = Y
    #ADIÇÂO MINHA
    elif reg_numB == 5:
        BUS_B = H
    else:
        BUS_B = 0

def write_regs(reg_bits):
    global MAR, MDR, PC, X, Y, H,K, BUS_C

    if reg_bits & 0b1000000:
        MAR = BUS_C
    if reg_bits & 0b0100000:
        MDR = BUS_C
    if reg_bits & 0b0010000:
        PC = BUS_C
    if reg_bits & 0b0001000:
        X = BUS_C
    if reg_bits & 0b0000100:
        Y = BUS_C
    if reg_bits & 0b0000010:
        H = BUS_C
    if reg_bits & 0b0000001:
        K=BUS_C
    
def alu(control_bits):
    global N, Z, BUS_A, BUS_B, BUS_C

    a = BUS_A
    b = BUS_B
    o = 0

    shift_bits = (0b11000000 & control_bits) >> 6
    control_bits = 0b00111111 & control_bits
        
    if control_bits == 0b011000:
        o = a
    elif control_bits == 0b010100:
        o = b
    elif control_bits == 0b011010:
        o = ~a
    elif control_bits == 0b101100:
        o = ~b
    elif control_bits == 0b111100:
        o = a+b
    elif control_bits == 0b111101:
        o = a+b+1
    elif control_bits == 0b111001:
        o = a+1
    elif control_bits == 0b110101:
        o = b+1
    elif control_bits == 0b111111:
        o = b-a
    elif control_bits == 0b110110:
        o = b-1
    elif control_bits == 0b111011:
        o = -a
    elif control_bits == 0b001100:
        o = a & b
    elif control_bits == 0b011100:
        o = a | b
    elif control_bits == 0b010000:
        o = 0
    elif control_bits == 0b110001:
        o = 1
    elif control_bits == 0b110010:
        o = -1   

    if o == 0:
        N = 0
        Z = 1
    else:
        N = 1
        Z = 0
        
    if shift_bits == 0b01:
        o = o << 1
    elif shift_bits == 0b10:
        o = o >> 1
    elif shift_bits == 0b11:
        o = o << 8
        
    BUS_C = o

def next_instruction(next, jam):
    global MPC, MBR, Z, N

    if jam == 0:
        MPC = next
        return
        
    if jam & 0b001:
        next = next | (Z << 8)

    if jam & 0b010:
        next = next | (N << 8)
        
    if jam & 0b100:
        next = next | MBR
        
    MPC = next

def memory_io(mem_bits):
    global PC, MBR, MDR, MAR

    if mem_bits & 0b001:
        MBR = memory.read_byte(PC)

    if mem_bits & 0b010:
        MDR = memory.read_word(MAR)
        
    if mem_bits & 0b100:
        memory.write_word(MAR, MDR)
        
def step():
    global MIR, MPC

    MIR = firmware[MPC]

    if MIR == 0:
        return False
        
    read_regs((MIR & 0b000000000000000000000000000000000111), ((MIR & 0b000000000000000000000000000000111000) >> 3))   
    alu((MIR & 0b000000000000111111110000000000000000) >> 16)
    write_regs((MIR & 0b000000000000000000001111111000000000) >> 9)
    memory_io((MIR & 0b000000000000000000000000000111000000) >> 6)
    next_instruction((MIR & 0b111111111000000000000000000000000000) >> 27,
                    (MIR & 0b000000000111000000000000000000000000) >> 24)

    return True
