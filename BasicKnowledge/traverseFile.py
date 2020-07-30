# f = open("traverse_file", "w")
#
# f.write("This is first line. 173 123123123 \n")
#
# f.write("This is second line. 123 76457456874568 \n")
#
# f.write("This is first line. 567 414523455345 \n")
#
# f.write("This is first line. 246 1231241414141 \n")
#
# f.close()

f = open("traverse_file")

for line in f:
    line = line.split()
    # print(line)
    height = int(line[4])
    if height >= 500:
        print(f"This is my selection. {line}")