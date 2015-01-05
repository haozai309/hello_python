import operator

def update_dic(content, cha_dic, cha_lis):
    for char in content:
        if char in cha_dic.keys():
            cha_dic[char] += 1
        else:
            cha_dic[char] = 1
            cha_lis.append(char)

my_file = open("input3.txt", "r")

cha_dic = {}
cha_lis = []

for line in my_file.read().split('\n'):
    update_dic(line, cha_dic, cha_lis)

my_file.close()

# print cha_dic
# print cha_lis

# orted_x = sorted(cha_dic.items(), key=operator.itemgetter(1))
# print orted_x

for char in cha_lis:
    if cha_dic[char] < 2:
        print char,