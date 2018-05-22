"""
file IO testing
"""


# \n 换行操作
myText = "my File IO testing...\n这样一来，AMD 2018年的显卡矩阵又回到了年初路线图给定的三个方向，一是Vega，二是移动显卡，三是7nm的加速卡。不过，最新的爆料显示，在挖矿热潮逐渐冷却之后，AMD的Vega产品线终于“喘过气来”准备出新了，剑指RX Vega Nano。Next line is something...\n外媒回忆，早在2017年8月，AMD全球产品营销高级主管Chris Hook就拿出了一张被认为是Vega Nano的原型产品，然而，也许因为后来挖矿造成Vega 56/64供不应求，导致新“小钢炮”无奈搁置。."


"""
#w=write
#r=read, 不可编写
myFile = open("file_io_test.txt", "w")
myFile.write(myText) #写入
myFile.close() #写完后腰关闭
"""


"""
appendText = "\n追加的文字内容 \n 追加的第二行"
#a = append,文件内容追加
myNewFile = open("file_io_test.txt", "a")
myNewFile.write(appendText)
myNewFile.close()
"""

"""
#文件有内容时候用w方法会覆盖,若要追加，得用a (append)方法
myReWriteFile = open("file_io_test.txt","w")
myReWriteFile.write("new content")
myReWriteFile.close()
"""

"""
#r=read
myReadFile = open("file_io_test.txt","r") #整个文件copy到了变量中，这个时候还没有读取文件内容
myContent = myReadFile.read() #读取文件内容
print(myContent)
"""


#myReadFile = open("file_io_test.txt","r") #整个文件copy到了变量中，这个时候还没有读取文件内容

#readline and readlines 返回的是list类型
#myLineContent = myReadFile.readline() #默认读取第一行,再执行一遍就是读取第二行
#print(myLineContent)
"""
#readlines是读取所有行(返回是个list)
myLinesContent = []
i = 0
for lines in myReadFile.readlines():
    myLinesContent.append(lines)
    print(myLinesContent[i])
    i = i+1
"""


myExcel = open("io_excel_test.xlsx","r")
myExcelContent = []
i = 0
for lines in myExcel.readlines():
    myExcelContent.append(lines)
    print(myExcelContent[i])
    i = i+1

myExcel.close()

