     goto main 
     wb 0        
    
r     ww 5
a     ww 0      
b     ww 0   
d     ww 1   

main set x, r
     set y, r
     jz  x, zero
     sub x, d
     mov y, a
     mov x, b
     goto mul
mul  mult r, a, b
     set x, b
     sub x, d
     jz x, hlt
     goto mtn
mtn  mov x, b
     set y, r
     mov y, a
     goto mul
zero add x, d
     mov x, r
     halt

hlt halt