l = ["Xiaoqian", "xiaoyuan", "xiaoling"]
d = {"name": "Nick", "age": 23, "hobbies": "girls"}
l1 = [1, 2, 3, 4]


# 对于字典列表而言， 他们本身是一个地址，里面的数据占用另外的地址， 所以字典等本身不能被更改
# 但是里面的数据可以改变
def change_data(info, girls):
    info["hobbies"] = "study"
    girls.append("Xiaolu")
    l1[0] = [1, 4, 5]


change_data(d, l)
print(d, l, l1)