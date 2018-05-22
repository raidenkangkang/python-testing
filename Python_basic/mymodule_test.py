"""
Your module description
"""
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
    def multipyFunct(self, a,b): #类里面的function得加self作为第一个参数
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