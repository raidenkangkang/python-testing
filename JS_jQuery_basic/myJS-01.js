/*
this is my first
JS external file
*/

//It's a good programming practice to declare all variables at the beginning of a script.
var x, y, z;
x = "10"; //If you put a number in quotes, the rest of the numbers will be treated as strings, and concatenated.
y = 20;
z = x + y;

function myAnotherFunc(){
    document.getElementById("demo").innerHTML = z;
}

function myObject(){
    var myStuff = {
        "name": "raiden",
        "sso": "302015572"
    }
    var my_undefined;
    var my_null;
    my_null = null; // Now value is null, but type is still an object
    document.getElementById("demo").innerHTML = myStuff.name + ", type is: " + typeof(myStuff.name) + ', myundeined item type is: ' + typeof(my_undefined) + ", myNull item type is: " + typeof(my_null)
}
