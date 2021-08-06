    goto main
    wb 0

r   ww 15
a   ww 0
b   ww 0
c   ww 1

main set x, r
     goto sum

sum  mov x, a
     add y, a
     sub x, c
     jz  x, zero
     goto sum

zero mov y, r 
     halt