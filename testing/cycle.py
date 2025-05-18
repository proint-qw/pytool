fruits = ['apple', 'banana', 'mongo']
print(fruits)

#for fruits in fruits:
    #print("sweet: " + fruits)

#for fruits in fruits:
    #print(f"sweet: {fruits}")

#for index,fruits in enumerate(fruits):          # 索引从0开始 
    #print(f"{index}: {fruits}")

#for index,fruits in enumerate(fruits, start=1):  # 索引从1开始 start 确定索引开始的位置
    #print(f"{index}: {fruits}")

# 让用户输入自己的名字，不要输入其他的
#name = input("enter your name: ")

#if name == '':
    #name = input("enter your name: ")
#else:
    #print(f"hello {name}") 
# 程序有bug，用户按两次enter键后，程序就无法正常执行，绕过安全机制
# 解决措施，while循环（无限循环）

name = input("enter your name: ")

while name == '':
    name = input("enter your name: ")

print(f"hello {name}!")

