# f = open("stock_data", "w")
# f.close()

f = open("stock_data", "r+")

# 1.加载数据到内存
data = f.read()
new_data = data.replace("NIO", "BA")
print(new_data)

# 2.清空文件
f.seek(0)
f.truncate()  # 截断文件 也就是清空光标所处位置后的所有数据

# 3.把新的内容重新写回硬盘
f.write(new_data)

f.close()
# 这个办法的弊病，文本太大的情况下加载很慢占用过多内存
