from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip

controller = Controller()

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    
    elif key == keyboard.Key.caps_lock:
    
        with controller.pressed(Key.ctrl_l):
            controller.press('c')
            controller.release('c')
            
        clipboard = pyperclip.paste().swapcase()
        pyperclip.copy(clipboard)
        with controller.pressed(Key.ctrl_l):
            controller.press('v')
            controller.release('v')

            

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

"""# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()"""