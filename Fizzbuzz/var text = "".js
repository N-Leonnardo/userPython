var text = ""
for(var i = 1; i <= 100; i++){
    text = i
        
    if(text%3 === 0 && text%5 === 0){
    text = "FizzBuzz"
    }
    if(text%3 === 0){
        text = "Fizz"
    }
    if(text%5 === 0){
    text = "Buzz"
    }

    
    console.log(text)
}
