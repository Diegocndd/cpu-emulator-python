import memory as mem
import ufc2x as cpu
import clock as clk
import disk

disk.read('prog0.bin')

# mem.write_word(200, 100)
# mem.write_word(201, 5)

# ### MULTIPLICAÇÃO ####
# # armazena X
# mem.write_byte(1, 2)
# mem.write_byte(2, 200)

# # armazena Y
# mem.write_byte(3, 17)
# mem.write_byte(4, 201)

# # H = X + Y
# mem.write_byte(5, 21)
# mem.write_byte(6, 255)

# #### DIVISÃO ####
# # armazena X
# mem.write_byte(1, 2)
# mem.write_byte(2, 200)

# # armazena Y
# mem.write_byte(3, 17)
# mem.write_byte(4, 201)

# mem.write_byte(5, 27)
# mem.write_byte(6, 255)

print(f"Antes: X = {cpu.X}, Y = {cpu.Y}, H = {cpu.H}")

clk.start([cpu])

print(f"Depois: X = {cpu.X}, Y = {cpu.Y}, H = {cpu.H}")