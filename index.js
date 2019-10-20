var express = require('express');
var app = express();
var mongoose = require('mongoose');
var ejs = require('ejs');
var request = require('request');

app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));

app.get('/', (req, res) => {
    res.render('textExtract');
});

app.post('/', (req, res) => {
    var img = req.body.voterID;
});

app.get('*', (req, res) => {
    res.redirect('back');
});

app.listen(3005, () => {
    console.log('> Ready to extract text');
});