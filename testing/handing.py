names = []

try:
    name = input('enter your name: ')
    names.append(name)
except KeyboardInterrupt:    # KeyboardInterrupt 键盘中断错误
    print("\nYou used Ctrl C, exting from the program...")

#print(f"hello {name}")
#print(f"hello {names}")