from pynput.keyboard import Key, Controller, Listener
import pyperclip

# Create a controller object
controller = Controller()

def on_release(key):
    if key == Key.esc:
        # Stop the listener if esc key is pressed
        return False
    
    elif key == Key.caps_lock:
        # Control + C to copy
        with controller.pressed(Key.ctrl_l):
            controller.press('c')
            controller.release('c')
            
        # Take what was copied and swap the case
        clipboard = pyperclip.paste().swapcase()
        
        # Copy the "swap cased" text to the clipboard
        pyperclip.copy(clipboard)
        
        # Control + V to paste
        with controller.pressed(Key.ctrl_l):
            controller.press('v')
            controller.release('v')

# Collect events until esc is pressed
with Listener(
        on_release=on_release) as listener:
    listener.join()