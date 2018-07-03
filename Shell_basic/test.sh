#!/bin/bash
MY_NAME="Raiden Yu"  #assign variable
echo $MY_NAME + "HELLO"  #call variable
echo "I'm: " + ${MY_NAME} #this is optional

readonly MY_READ_ONLY="KK"
echo "This is read only variable: " + ${MY_READ_ONLY}

unset MY_NAME  #this will delete the variable, so values in MY_NAME is cleared
echo "After unset, the variable is: " + ${MY_NAME}

MY_STRING="My String Test"
echo "Length of the string is: " + ${#MY_STRING} #show the length of this string