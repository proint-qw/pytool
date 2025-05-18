
with open('data.txt', 'w') as file:  # w 指定以可写模式打开一个文件 创建文件
    file.write('hello there!\n')     # 将数据写入所创建的文件之中
    file.write("i am loser.....")

with open('data.txt', 'r') as file:  # 读取文件内容
    data = file.read()
    print(data)
   
# 未来大量使用来保存信息