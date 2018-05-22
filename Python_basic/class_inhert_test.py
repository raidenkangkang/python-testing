"""
类的继承
"""

class Student:
    def __init__(self, stdName, stdSchool):
        self.stdName = stdName
        self.stdSchool = stdSchool
        self.stdMark = []
        
    def avgMark(self):
        return sum(self.stdMark/len(self.stdMark))
    
    @classmethod  #类方法传入参数是类，而不是self
    def friendWho(cls, friend_name, original_school, teacherName):
        #返回同一个学校里面的其他学生
        return cls(friend_name, original_school, teacherName) #返回一个新的当前的类，同一个学校，但是名字不一样
        
#类的继承
class NewStudent(Student):
    #重载父类方法
    def __init__(self, stdName, stdSchool, stdTeacher):
        #调用父类初始化方法
        super().__init__(stdName, stdSchool)
        self.stdTeacher = stdTeacher
    
    """
    def friendWho(self, friend_name):
        return Student(friend_name, self.stdSchool, self.stdTeacher)
    """ 
        
raiden = NewStudent("raiden", "BJ", "mr Big")
kk = raiden.friendWho("kk", raiden.stdSchool, raiden.stdTeacher)
print(raiden.stdTeacher)
#print(kk.stdTeacher)  这个会报错，因为Student没有teacher属性，所以要改成friendWho为class method