from pynput.keyboard import Key, Controller, Listener
import pyperclip

controller = Controller()

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False
    
    elif key == Key.caps_lock:
        with controller.pressed(Key.ctrl_l):
            controller.press('c')
            controller.release('c')
            
        clipboard = pyperclip.paste().swapcase()
        pyperclip.copy(clipboard)
        
        with controller.pressed(Key.ctrl_l):
            controller.press('v')
            controller.release('v')

# Collect events until released
with Listener(
        on_release=on_release) as listener:
    listener.join()