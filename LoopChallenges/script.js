var number = 1

for(var i = 0; i <= 20; i++){
    number = i
    if(number%2 !== 0){
    console.log(number)
    }
}

//--------------------------------------//

var number = 0

for(var i = 100; i>=0; i--){
    number = i;
    if(number%3 === 0){
        console.log(number)
    }
}

//--------------------------------------//

var arr = [4, 2.5, 1, -0.5, -2, -3.5]
var number = 0

for(var i = 0; i< arr.length; i++){
    number = arr[i];
    console.log(number)
    
}
//--------------------------------------//

var sum = 0

for(var i = 0; i<=100; i++){
    sum += i;
}
console.log(sum)

//--------------------------------------//

var factorial = 1

for(var i = 1; i<=12; i++){
    factorial *= i
}
console.log(factorial)

