# coding: utf-8

# 打开文件，传入文件名和标识符，r代表读
f = open('\\Users\ZC\Desktop\zc.txt', 'r')
# 调用read方法一次性读取文件的全部内容，存入内存，用str对象表示
print(f.read())
f.close()

# 使用with无论程序是否对错都会最后默认关闭文件。
with open('\\Users\ZC\Desktop\zc.txt', 'r') as f:
    print(f.read())

# 使用read()会一次性读取文件的所有内容，如果文件过大，内存会爆掉。可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
f = open('\\Users\ZC\Desktop\zc.txt', 'r')
for line in f.readlines():
    print(line.strip())

# 图片、视频等二进制文件，用rb模式打开
f = open('\\Users\ZC\Pictures\Camera Roll\8.jpg', 'rb')
print(f.read())

# 读取非UTF-8编码的文本文件，需要在open()函数中传入encoding参数,errors参数表示遇到编码错误如何处理。
f = open('\\Users\ZC\Desktop\gbk.txt', 'r', encoding='gbk', errors='ignore')
print(f.read())

# 调用open()函数传入标识符，w代表写入（wb写入二进制文件），如果文件不存在会自动创建。
f = open('\\Users\ZC\Desktop\zc.txt', 'w')
f.write('遇事不决，可问春风 \n')
f.close()
f = open('\\Users\ZC\Desktop\zc.txt', 'r')
print(f.read())

# w模式写入文件，会直接覆盖(即相当于删除后重建)，如果想追加，可使用a(append)模式。
f = open('\\Users\ZC\Desktop\zc.txt', 'a')


# 创建文件，写入内容
def text_create(name, msg):
    desktop_path = 'C://Users/ZC/Desktop/'
    full_path = desktop_path + name + '.txt'
    new_file = open(full_path, 'w')
    new_file.write(msg)
    new_file.close()


# 敏感词为SB，替换成***
def text_filter(word, censored_word='SB', changed_word='***'):
    return word.replace(censored_word, changed_word)


# msg经过text_filter过滤之后存入到clean_msg，然后调用text_create写入。
def text_censored_create(name, msg):
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)
text_censored_create('test', '你是个SB')
