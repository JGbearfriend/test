import itertools as its
#生成密码字典
words="0123456789"
r=its.product(words,repeat=6)
dic=open("password_num.txt","a")

#for k in range(num):
for wd in r:
    print(wd)
    dic.write("".join(wd))
    dic.write("".join("\n"))
dic.close()