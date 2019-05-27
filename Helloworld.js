function greet(){
    console.log("Hello World!");          
            }

function logGreeting(fn){
    fn();    
}

var GreetMe = function(){
    console.log("Name assignment for function");
}

logGreeting(greet);

logGreeting(function(){
    console.log("inline function");
    
});

greet();

require('/greet.js')
