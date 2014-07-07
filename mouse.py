from Xlib import X, display
import time
d = display.Display()
s = d.screen()
root = s.root
for i in range(100):
    root.warp_pointer(300+i,300+i)
    d.sync()
    time.sleep(0.01)
