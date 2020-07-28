stu_list = [['唐僧', 23],
            ['八戒', 71],
            ['孙悟空', 82],
            ['沙僧', 93],
            ['方旋', 45],
            ['叶子青', 56],
            ['李玥涵', 69],
            ['曹溪岭', 12],
            ['开心心', 34]
            ]
new_stu_list = [
    [],   #less than 30
    [],   #less than 60
    []    #others
]

for i in stu_list:
    if i[1] < 30:
        new_stu_list[0].append(i)
    elif i[1] < 60:
        new_stu_list[1].append(i)
    else:
        new_stu_list[2].append(i)

print(new_stu_list[0])

print(new_stu_list[1])

print(new_stu_list[2])