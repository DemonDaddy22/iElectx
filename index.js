var express = require('express');
var app = express();
var mongoose = require('mongoose');
var ejs = require('ejs');
var bodyParser = require('body-parser'); 
var request = require('request');

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/public'));

mongoose.connect('mongodb://localhost/capstone2', { useNewUrlParser: true, useUnifiedTopology: true });

var userSchema = new mongoose.Schema({
    firstName: String,
    middleName: String,
    lastName: String,
    fatherName: String,
    motherName: String,
    gender: String,
    date: Number,
    month: Number,
    year: Number,
    contact: String,
    address: String,
    city: String,
    state: String,
    zip: String,
    voterId: String,
    email: {type: String, unique: true, required: true},
    resetPasswordToken: String,
    resetPasswordExpires: Date,
    isAdmin: {type: Boolean, default: false}
});

var User = mongoose.model("Voter", userSchema);

app.get('/', (req, res) => {
    res.render('landing');
});

app.post('/', (req, res) => {
    console.log(req.body);
    res.redirect('/');
});

app.get('/register', (req, res) => {
    res.render('register');
});

app.get('/login', (req, res) => {
    res.render('login');
});

app.get('/about', (req, res) => {
    res.render('about');
});

app.get('*', (req, res) => {
    res.redirect('back');
});

app.listen(3005, () => {
    console.log('> Server started');
});
