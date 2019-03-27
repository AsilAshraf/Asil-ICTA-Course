function plus(){


        
    var a=parseInt(document.getElementById("num1").value);
    var b=parseInt(document.getElementById("num2").value);
    var c=document.getElementById("oper").value;
var x=0;
    
    if(c=="addition"){
        x=a+b;
        
    }
    else if(c=="substraction"){
        x=a-b;
    }
        else if(c=="multiplication"){
            x=a*b;
        }
    console.log(x);
    document.getElementById("res").innerHTML=x;
        }