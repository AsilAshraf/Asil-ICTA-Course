const express=require('express');
const exphbs=require('express-handlebars')  //for setting template engine ie handlebars

var app=express();

app.engine('handlebars',exphbs({defaultLayout:'mainpage'}));   //code for template engine setting  //default layout setting also
app.set('view engine','handlebars');  //viewing of template engine

app.use(express.static('views/static'));  //image path assigning views folder and its sub folder static
app.use(express.urlencoded());  // data fetching from form
app.get('/', (req,res)=>{
    res.render('index')  //rendering and calling of the rout page
});
app.get('/home', (req,res)=>{
    res.send("welcome to my home")
});
app.get('/contact', (req,res)=>{
    res.render('contact')
});
app.get('/about',(req,res)=>{
    res.render('about')

});
app.get('/gallery',(req,res)=>{
    res.render('gallery')
});

app.post('/getdata',(req,res)=>{  //transfer contents after button clicking into getdata
   var name=req.body.getname;  //data fetched from getname and its add into variable name
   var address=req.body.getaddr;
   var place=req.body.getplace;
   var email=req.body.getemail;
   var mobile=req.body.getmob;

   console.log(name,address,place,email,mobile);
    //res.send(name)
});
app.listen(2500);