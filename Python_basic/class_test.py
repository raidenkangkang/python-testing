"""
class test
"""
#class 通常都是首字母大写
class Calculator:
    #类的静态默认属性
    calName = "Raiden Calculator: "
    calPrice = 15.65
    
    #类的初始化过程中的属性赋值
    def __init__(self, who, purpose="test"): #默认属性，如果没有赋值就是此属性值
        self.who = who
        self.purpose = purpose
    
    
    #类的功能
    #add function
    def addFunct(self, a,b): #类里面的function得加self作为第一个参数
        if type(a)==type(b)==type(10):
            return self.calName + "result-add:" + str(a+b)
        elif type(a)==type(b)==type(10.98):
            return self.calName + "result-add:" + str(a+b)
        else:
            return "wrong argu type !"
            
    #multipy function
    def multipy(self, a,b): #类里面的function得加self作为第一个参数
        if type(a)==type(b)==type(10):
            return self.calName + "result-multipy:" + str(a*b)
        elif type(a)==type(b)==type(10.98):
            return self.calName + "result-multipy:" + str(a*b)
        else:
            return "wrong argu type !"
            
    #minues function
    def minuesFunct(self, a,b): #类里面的function得加self作为第一个参数
        if type(a)==type(b)==type(10):
            return self.calName + "result-minues:" + str(a-b)
        elif type(a)==type(b)==type(10.98):
            return self.calName + "result-minues:" + str(a-b)
        else:
            return "wrong argu type !"
            
    #divide function
    def divideFunct(self, a,b): #类里面的function得加self作为第一个参数
        if type(a)==type(b)==type(10):
            return self.calName + "result-divide:" + str(a/b)
        elif type(a)==type(b)==type(10.98):
            return self.calName + "result-divide:" + str(a/b)
        else:
            return "wrong argu type !"

#input需要用户终端输入
whoInput = input("who's the user: ") #用来给类的初始化值赋值
purposeInput = input("purpose of using the calculator: ") #用来给类的初始化值赋值

myCal = Calculator(whoInput, purposeInput) #初始化的时候赋值,若有缺省值则可以不必输入
print(myCal.calName) #属性打印，无需括号
print(myCal.calPrice) #属性打印，无需括号
print(myCal.who) #属性打印，无需括号
print(myCal.purpose) #属性打印，无需括号

print(myCal.addFunct(100,200)) #类的功能调用
print(myCal.divideFunct(50,20)) #类的功能调用
print(myCal.minuesFunct(99,12)) #类的功能调用
print(myCal.multipy(12.22,8.21)) #类的功能调用


class Cal2:
    def __init__(self, name):
        """
        init function
        """
        self.name = name
        self.num = (1,2,3,4,5,6,6,6,7)
        
    def totalNum(self):
        """
        do some sum job
        """
        return sum(self.num)
        
newCal = Cal2("raiden")
print(newCal.name)
print(newCal.num)
print(newCal.totalNum())

#another testing...
class Student:
    """
    student class
    """
    
    mark = []
    
    def __init__(self, name, school):
        """
        initial of class
        """
        self.name = name
        self.school = school
        
    def avgMark(self):
        """
        do some average of marks
        """
        return sum(self.mark) / len(self.mark)
        
    #类的静态方法，和创建的对象属性无关
    @staticmethod
    def goSchool(): #无需pass self参数
        print("i'm going to school")
        
raiden = Student("raiden","Shanghai U")
kk = Student("kk","DALian U")
raiden.mark.append(100)
raiden.mark.append(200)
raiden.mark.append(300)
print(raiden.avgMark())
Student.goSchool() #静态方法调用，直接通过类调用
raiden.goSchool() #静态方法调用，也可以通过对象调用
