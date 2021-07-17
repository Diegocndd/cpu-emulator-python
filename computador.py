import memory as mem
import ufc2x as cpu
import clock as clk

mem.write_word(200, 10)
mem.write_word(201, 14)

# ### MULTIPLICAÇÃO ####
# # armazena X
# mem.write_byte(1, 2)
# mem.write_byte(2, 200)

# # armazena Y
# mem.write_byte(3, 17)
# mem.write_byte(4, 201)

# # H = X * Y
# mem.write_byte(5, 21)
# mem.write_byte(6, 255)


#### SUBTRAÇÃO ####
# # armazena X
# mem.write_byte(1, 2)
# mem.write_byte(2, 200)

# # armazena Y
# mem.write_byte(3, 17)
# mem.write_byte(4, 201)

# # H = X - Y
# mem.write_byte(5, 25)
# mem.write_byte(6, 255)


#### SOMA ####
# # armazena X
# mem.write_byte(1, 2)
# mem.write_byte(2, 200)

# # armazena Y
# mem.write_byte(3, 17)
# mem.write_byte(4, 201)

# # H = X + Y
# mem.write_byte(5, 27)
# mem.write_byte(6, 255)


print(f"Antes: X = {cpu.X}, Y = {cpu.Y}, H = {cpu.H}")

clk.start([cpu])

print(f"Depois: X = {cpu.X}, Y = {cpu.Y}, H = {cpu.H}")