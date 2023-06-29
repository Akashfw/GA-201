const express = require("express");
const mongoose = require("mongoose");
const bcrypt = require("bcrypt");
const jwt= require("jsonwebtoken");
const app= express();

const connection = mongoose.connect(mongourl);

const userSchema = mongoose.Schema({
    name:String,
    email:String,
    pass:String
});

const Usermodel = mongoose.model("user", userSchema);


app.post("/signup", async (req,res)=>{
    const {name,email,pass}= req.body;
    try {
         bcrypt.hash(pass, 6, (hash, err)=>{
             
         })
    } catch (err) {
        
    }
})




app.listen(8000, async ()=>{
    try {
        await connection;
        console.log("connected to DB")
    } catch (err) {
        console.log(err);
        console.log("unable to connect to DB")
    }
    console.log("server is running on port 8000")
})