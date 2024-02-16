
//import all packages necessary
const express = require('express');
const path = require('path');
const fileupload = require('express-fileupload');

//store the public folder path inside a variable
let initial_path = path.join(__dirname,"public");

//create expressJS server, set public folder path to static path. Use app.use(fileupload()) to enable file uploads
const app = express();
app.use(express.static(initial_path));
app.use(fileupload);

// Make a home route and in response send a home.html file. Run server on port 3000
app.get('/', (req, res) => {
    res.sendFile(path.join(initial_path, "home.html"));
})

app.listen("3000", () => {
    console.log('listening.......');
})

app.get('/editor', (req,res) => {
    res.sendFile(path.join(initial_path, "editor.html"));
})

//make upload route
app.post('/upload',(req,res) => {
    let file = req.files.image;
    let date = new Date();
    //image name
    let imagename = date.getDate() + date.getTime() + file.name;
    //image upload path
    let path = 'public/uploads/' + imagename;

    //create upload
    file.mv(path, (err, result) => {
        if(err){
            throw err;
        }else{
            // our image upload path
            res.json('uploads/${imagename}')
        }
    })
})