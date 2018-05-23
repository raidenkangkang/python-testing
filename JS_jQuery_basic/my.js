// var carInfo = {
//     maker: "BWM and Benz",
//     year: "2018",
//     owner: "Raiden",
//     //object function
//     carAlert: function(){
//         alert("Alert here !")
//     },
//     getLength: function(){
//         return this.maker.length
//     }
// };
//
// for (k in carInfo) {
//     console.log(k)
//     console.log(carInfo[k])
// }
//
// //carInfo.carAlert()
// //alert(carInfo.getLength())
//
// //query selector
// alert($("h1").text())

var x = $("h1")
x.click(function(){
    alert("hello")
    $(this).css("color", "red")
    $(this).text("new text here !")
})

$("#id1").mouseover(function(){
    //alert("mouse over !")
})


$("#id2").on("dblclick", function(){
    alert("double clicked !")
})