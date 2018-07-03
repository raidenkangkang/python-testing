#!bin/bash

#function test

demoFunc(){
    echo "this is a function call"
    return `expr 3 + 4`
}

#call the function
demoFunc
echo $? # 函数返回值在调用该函数后通过 $? 来获得。