#!/bin/bash
# this is a test.sh script file


MY_NAME="Raiden Yu"  #assign variable
echo $MY_NAME + "HELLO"  #call variable
echo "I'm: " + ${MY_NAME} #this is optional

readonly MY_READ_ONLY="KK"
echo "This is read only variable: " + ${MY_READ_ONLY}

unset MY_NAME  #this will delete the variable, so values in MY_NAME is cleared
echo "After unset, the variable is: " + ${MY_NAME}

MY_STRING="My String Test"
echo "Length of the string is: " + ${#MY_STRING} # show the length of this string
echo "Position is: " + ${MY_STRING:3:10} # show the position from 3 to 10

MY_ARRAY=(12 33 22 99) # define the array, 没有逗号!!!
MY_ARRAY[3]=66
echo "My array[0] is: " + ${MY_ARRAY[0]}
echo "My array[2] is: " + ${MY_ARRAY[2]}
echo "After change, the array[3] is:" ${MY_ARRAY[3]}
echo ${MY_ARRAY[@]} # get all values in the array
echo ${#MY_ARRAY[@]} # get the length of the array, which is 4

# parameters to be passed when running the .sh
echo "first parameter is: " + $1
echo "second parameter is:" + $2

MY_VAL=`expr 2 + 4` #需要加空格2 + 4而不是2+4, `键在Esc下面
echo ${MY_VAL} #return 2+4
MY_VAL=`expr 2 - 3`
echo ${MY_VAL}
MY_VAL=`expr 3 \* 5` #乘号(*)前边必须加反斜杠(\)才能实现乘法运算；
echo ${MY_VAL}


# -eq	检测两个数是否相等，相等返回 true。	[ $a -eq $b ] 返回 false。
# -ne	检测两个数是否不相等，不相等返回 true。	[ $a -ne $b ] 返回 true。
# -gt	检测左边的数是否大于右边的，如果是，则返回 true。	[ $a -gt $b ] 返回 false。
# -lt	检测左边的数是否小于右边的，如果是，则返回 true。	[ $a -lt $b ] 返回 true。
# -ge	检测左边的数是否大于等于右边的，如果是，则返回 true。	[ $a -ge $b ] 返回 false。
# -le	检测左边的数是否小于等于右边的，如果是，则返回 true。	[ $a -le $b ] 返回 true。
if [ 3 -lt 4 ]
then
    echo "yes"
else
    echo "no"
fi

# !	非运算，表达式为 true 则返回 false，否则返回 true。	[ ! false ] 返回 true。
# -o 或运算，有一个表达式为 true 则返回 true。	[ $a -lt 20 -o $b -gt 100 ] 返回 true。
# -a 与运算，两个表达式都为 true 才返回 true。	[ $a -lt 20 -a $b -gt 100 ] 返回 false。
if [ 3 -eq 4 -o 2 -lt 4 ]
then
    echo "yeap"
else
    echo "nope"
fi

# &&	逻辑的 AND	[[ $a -lt 100 && $b -gt 100 ]] 返回 false
# ||	逻辑的 OR	[[ $a -lt 100 || $b -gt 100 ]] 返回 true
if [[ 3 -eq 3 && 4 -eq 4 ]] #需要两个括号
then
    echo "ok"
else
    echo "not ok"
fi

# =	检测两个字符串是否相等，相等返回 true。	[ $a = $b ] 返回 false。
# !=	检测两个字符串是否相等，不相等返回 true。	[ $a != $b ] 返回 true。
# -z	检测字符串长度是否为0，为0返回 true。	[ -z $a ] 返回 false。
# -n	检测字符串长度是否为0，不为0返回 true。	[ -n "$a" ] 返回 true。
# str	检测字符串是否为空，不为空返回 true。	[ $a ] 返回 true。


# -b file	检测文件是否是块设备文件，如果是，则返回 true。	[ -b $file ] 返回 false。
# -c file	检测文件是否是字符设备文件，如果是，则返回 true。	[ -c $file ] 返回 false。
# -d file	检测文件是否是目录，如果是，则返回 true。	[ -d $file ] 返回 false。
# -f file	检测文件是否是普通文件（既不是目录，也不是设备文件），如果是，则返回 true。	[ -f $file ] 返回 true。
# -g file	检测文件是否设置了 SGID 位，如果是，则返回 true。	[ -g $file ] 返回 false。
# -k file	检测文件是否设置了粘着位(Sticky Bit)，如果是，则返回 true。	[ -k $file ] 返回 false。
# -p file	检测文件是否是有名管道，如果是，则返回 true。	[ -p $file ] 返回 false。
# -u file	检测文件是否设置了 SUID 位，如果是，则返回 true。	[ -u $file ] 返回 false。
# -r file	检测文件是否可读，如果是，则返回 true。	[ -r $file ] 返回 true。
# -w file	检测文件是否可写，如果是，则返回 true。	[ -w $file ] 返回 true。
# -x file	检测文件是否可执行，如果是，则返回 true。	[ -x $file ] 返回 true。
# -s file	检测文件是否为空（文件大小是否大于0），不为空返回 true。	[ -s $file ] 返回 true。
# -e file	检测文件（包括目录）是否存在，如果是，则返回 true。	[ -e $file ] 返回 true。

echo `date`

printf "hello printer ! \n"
# %d %s %c %f 格式替代符详解:
# d: Decimal 十进制整数 -- 对应位置参数必须是十进制整数，否则报错！
# s: String 字符串 -- 对应位置参数必须是字符串或者字符型，否则报错！
# c: Char 字符 -- 对应位置参数必须是字符串或者字符型，否则报错！
# f: Float 浮点 -- 对应位置参数必须是数字型，否则报错！
printf "%d %s %c\n" 1 "abe" "def" # 如：其中最后一个参数是 "def"，%c 自动截取字符串的第一个字符作为结果输出。

read firstStr secondStr # this will ask user input from the console
echo "input something here: ${firstStr} and ${secondStr}"