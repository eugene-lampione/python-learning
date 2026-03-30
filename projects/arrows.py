from pynput import keyboard
import os

# clear screen
os.system("clear")

def on_press(key):
    try:
        # check for q
        if key.char == 'q':
            print("Exiting Program....")
            return False # stop listener
    except AttributeError:
        pass

    # check for arrow keys
    if key == keyboard.Key.up:
        print('UP ^')
    elif key == keyboard.Key.down:
        print('DOWN v')
    elif key == keyboard.Key.left:
        print('<-- LEFT')
    elif key == keyboard.Key.right:
        print('RIGHT -->')


# prompt the user
print("Press arrow keys! Press 'q' to Exit.")



# create and start a keyboard listener
with keyboard.Listener(on_press=on_press) as listener:#create listener object that listens for keyboard events
    # start the listener and wait for it to finish
    listener.join()