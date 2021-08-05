import cpu as cpu
import sys
import memory as mem
import clock as clk 
import disk

disk.read(str(sys.argv[1]))

print("Antes: ", mem.read_word(1))
print(f"X: {cpu.X}", f"Y: {cpu.Y}", f"K: {cpu.K}", f"H: {cpu.H}")

clk.start([cpu])

print("Depois: ", mem.read_word(1))
print(f"X: {cpu.X}", f"Y: {cpu.Y}", f"K: {cpu.K}", f"H: {cpu.H}")
