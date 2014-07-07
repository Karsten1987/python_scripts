import Xlib.X as X
import Xlib.display as display
import Xlib.ext.xtest as xtest
import time


disp = display.Display()
root = disp.screen().root

key = disp.keysym_to_keycode(ord(' '))
print type(key)
xtest.fake_input(root, X.KeyPress, key)
xtest.fake_input(root, X.KeyRelease, key)

time.sleep(10)
disp.flush()


