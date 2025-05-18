import threading
import time

def print_number():
    for i in range(1, 6):
        print(f"number: {i}")
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(f"Letters: {letter}")
        time.sleep(1)


print_number()
print_letters()

# thread1 = threading.Thread(target=print_number)   # 让程序同时打印字母和数字
# thread2 = threading.Thread(target=print_letters)   # 创建树形变量

# thread1.start()  # 创建树形结构
# thread2.start()

# thread1.join()   # 保证同时处理
# thread2.join()

# print("Bath threads have finished execution.")  # 同时打印
