var express = require('express');
var fs = require('fs');
var router = express.Router();
const { paths } = require('../app');
const path = require('path')
const multer  = require('multer') //use multer to upload blob data
const upload = multer(); // set multer to be the upload variable (just like express, see above ( include it, then use it/set it up))

const {Storage} = require('@google-cloud/storage');

const gc = new Storage({
  keyFilename: path.join(__dirname, '../speach-339718-f1b9b69dce93.json'),
  projectId: 'speach-339718'
})



/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('home');
});


router.get('/home', function(req, res, next){
  res.render('home');
});

router.post('/youtubeUpload', function(req, res, next){
  var youtubeLink = req.
})

module.exports = router;
