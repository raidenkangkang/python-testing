"""
import 功能测试
"""

import time as t #import time 模块, 默认可以使用time下的所有功能
from time import localtime, time #从time模块导入localtime和time两个功能
from time import * #星号导入所有time下面的功能
from mymodule_test import Calculator #导入自己的类库

print(localtime())
print(time())
print(t.timezone)


#测试自己的类模块
myClass = Calculator("kk", "learn") #初始化类
print(myClass.calName)
print(myClass.calPrice)
print(myClass.who)
print(myClass.purpose)
#类功能调用
print(myClass.divideFunct(99,9))
print(myClass.addFunct(111,222))

