const express=require('express');

var app=express();
app.get('/', (req,res)=>{
    res.send("welcome")
});
app.get('/home', (req,res)=>{
    res.send("welcome to my home")
});
app.get('/contact', (req,res)=>{
    res.send("contact us")
});

app.listen(2500);