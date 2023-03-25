import csv

#文件路径（文件要手动创建）
filePath = 'C:/Users/likes/Desktop/test.csv'


# 写入csv文件
def write_csv_test():
    global filePath
    with open(filePath, 'w', newline='') as sheet:  # 打开sheet文件
        writer = csv.writer(sheet)  # 获取写入指针
        writer.writerows([[1,"这是第一行"],[2,"这是第二行"],[3.0,"这是第三行"]])


# 读取csv文件
def read_csv_test():
    global filePath
    with open(filePath, newline='') as sheet:  # 打开sheet文件
        reader = csv.reader(sheet)  # 读取sheet文件
        for row in reader:  # 读取成了二维数组
            print('这一行的内容是：' + str(row))


#修改csv文件
def change_csv_file():
    global filePath
    sheet = [[]]
    #读取文件内容
    with open(filePath, 'r', newline='') as file:
        sheet = csv.reader(file)

        #修改内容（注意这里的缩进不能删除,因为关闭文件之后这个对象的内存就释放了,但是转化成二维数组就还能存在）
        sheet = [row for row in sheet]      #转换为二维数组
        sheet[0][0] = 'by likeszm'

    #修改文件
    with open(filePath, 'w', newline='') as file:
        filePoint = csv.writer(file)
        filePoint.writerows(sheet)


print("开始运行")
#read_csv_test()
#write_csv_test()
#change_csv_file()
#read_csv_test()

