var express = require('express');
var body = require('body-parser')
var app = express();
var path = require('path')
var fs = require("fs");

app.use(body.urlencoded({extended: true}));
app.use(body.json());

app.use(express.static('./'))

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
})

app.get('/foods', function (req, res) {
   fs.readFile( __dirname + "/" + "data.json", 'utf8', function (err, data) {
       console.log("GET /foods");
       res.send(JSON.parse(data).map(function(ele)  {
           return {id: ele.id, name: ele.name}
       }));
   });
})

app.get('/foods/:id', function(req, res) {
    fs.readFile( __dirname + "/" + "data.json", 'utf8', function (err, data) {
        let lists = JSON.parse(data);
        let list = lists.filter(a => [req.params.id].includes(a.id.toString()));
        console.log("GET /foods/" + req.params.id);
        if (list != null) {
            res.send(list[0]);
        } else {
            res.status(404).send("Not found");
        }
    });
})

const port = process.env.PORT || 8899;
var server = app.listen(port, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("Serving data on localhost: " + port + "...")

})