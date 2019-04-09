const express=require('express');
const exphbs=require('express-handlebars')  //for setting template engine ie handlebars

var app=express();

app.engine('handlebars',exphbs({defaultLayout:'mainpage'}));   //code for template engine setting  //default layout setting also
app.set('view engine','handlebars');  //viewing of template engine


app.get('/', (req,res)=>{
    res.render('index')  //rendering and calling of the rout page
});
app.get('/home', (req,res)=>{
    res.send("welcome to my home")
});
app.get('/contact', (req,res)=>{
    res.send('[{"name":"ram","gender":"male"},{"name":"raju","age":24}]')
});
app.get('/about',(req,res)=>{
    res.render('about')

});

app.listen(2500);