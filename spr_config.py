import time
import pip
import subprocess
import sys
import os
import keyboard
try:
        from colorama import init
        from colorama import Fore, Back, Style
        init()
except ImportError as e:
        install("colorama")
        time.sleep(0.5)
        from colorama import init
        from colorama import Fore, Back, Style
        init()
def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])
try:
        import keyboard
except ImportError as e:
        install("keyboard")
        time.sleep(0.5)
        import keyboard
        pass
line = []
line2 = ""
que = input("Sprites_name> ")
while True:
    words = ""
    type = ""
    if keyboard.is_pressed("1"):
        line.append("r")
    if keyboard.is_pressed("2"):
        line.append("g")
    if keyboard.is_pressed("3"):
        line.append("b")
    if keyboard.is_pressed("Enter"):
        line.append("1")
    if keyboard.is_pressed("Backspace"):
     if len(line)-1 != -1:
        line.remove(line[len(line)-1])
    if not os.path.exists(".\\Sprites\\" + que + "\\"):
       os.makedirs(".\\Sprites\\" + que + "\\")
    file = open(".\\Sprites\\" + que + "\\" + que + ".sprite", "w")
    file.write(str(line))
    file.close()
    file = open(".\\Sprites\\" + que + "\\" + que + ".sprite", "r")
    words = file.read()
    for w in range(len(words)-1):
      if w<len(words)-1:
        if words[w] == "[" or words[w] == "]" or words[w] == "," or words[w] == " ":
            pass
        else:
            if words[w] == "r":
                type += Back.RED + " "
            if words[w] == "g":
                type += Back.GREEN + " "
            if words[w] == "b":
                type += Back.BLUE + " "
            if words[w]=="1":
                type += Back.BLACK + "\n"
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(Back.BLACK + type + Back.BLACK)
    time.sleep(0.1)
