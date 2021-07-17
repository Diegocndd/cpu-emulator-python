     goto main
     wb  0
 
res  ww  0
A    ww  0
B    ww  0
c1   ww  1

main add x, A 
     add x, B
     jz  x, jmp
     mov x, res
para halt
jmp  add x, c1
     mov x, res 
     goto para
