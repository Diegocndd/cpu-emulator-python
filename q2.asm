    goto main
    wb 0

r   ww 6
a   ww 1
b   ww 1
c   ww 2
d   ww 0
e   ww 1
f   ww 2

main set x, r
     set y, e
     sub x, e
     jz  x, n11
     sub x, e
     jz  x, n11
     set x, r
     sub x, f
     set y, d
     goto fibo

fibo add y, a
     add y, b
     mov y, a
     sub x, e
     jz  x, fim
     set y, d
     add y, a
     add y, b
     mov y, b
     sub x, e
     jz  x, fim
     set y, d
     goto fibo
     halt

n11  mov y, r
     halt

fim mov y, r
    halt