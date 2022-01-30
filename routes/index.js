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





router.post('/uploadAudio', upload.single('soundBlob'), async function (req, res, next) {
  // console.log(req.file); // see what got uploaded

  let uploadLocation = __dirname + '../temp/' + req.audio // where to save the file to. make sure the incoming name has a .wav extension

  var form = new formidable.IncomingForm();
        form.parse(req, function (err, fields, files) {
            // oldpath : temporary folder to which file is saved to
            var oldpath = files.filetoupload.path;
            var newpath = upload_path + files.filetoupload.name;
            // copy the file to a new location
            fs.rename(oldpath, newpath, function (err) {
                if (err) throw err;
                // you may respond with another html page
                res.write('File uploaded and moved!');
                res.end();
            });
        });

  /*
  async function uploadFile(){
    await gc.bucket('audiofsls').upload((__driname + `../temp/${req.audio.originalname}`), {
      destination: "test.mp3",
    });
    console.log(`$File uploaded to Bucket`);
    }
  uploadFile().catch(console.error);
  */
})


module.exports = router;
