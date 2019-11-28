var express = require('express');
var app = express();
var mongoose = require('mongoose');
var ejs = require('ejs');
var bodyParser = require('body-parser'); 
var request = require('request');
var Tesseract = require('tesseract.js');

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + '/public'));

mongoose.connect('mongodb://localhost/capstone1', { useNewUrlParser: true, useUnifiedTopology: true });

var voterSchema = new mongoose.Schema({
    name: String,
    fatherName: String,
    gender: String,
    dob: String,
    vid: String
});

var Voter = mongoose.model("Voter", voterSchema);

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

app.get('*', (req, res) => {
    res.redirect('back');
});

app.listen(3005, () => {
    console.log('> Server started');
});
