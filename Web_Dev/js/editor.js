const blogTitleField = document.querySelector('.title');
const articleField = document.querySelector('.article');

//banner
const bannerImage = document.querySelector('#banner-upload');
const banner = document.querySelector('.banner');
let bannerPath;

const publishBtn = document.querySelector('.publish-btn');
const uploadInput = document.querySelector('#image-upload');

// Add change event to upload inputs and process the upload
bannerImage.addEventListener('change', () => {
    uploadImage(bannerImage, "banner");
})

uploadInput.addEventListener('change', () => {
    uploadImage(uploadInput, "image");
})

// Create uploadImage function
const uploadImage = (uploadFile, uploadType) => {
    const [file] = uploadFile.files;
    if(file && file.type.includes("image")){
        const formdata = new FormData();
        formdata.append('image', file);

        fetch('/upload', {
            method: 'post',
            body: formdata
        }).then(data => {
            if(uploadType == "image"){
                addImage(data, file.name);
            }else{
                bannerPath = '${location.origin}/${data}';
                banner.style.backgroundImage = 'url("${bannerPath}")';
            }
        })
    }else{
        alert("upload Image only");
    }
}

// Create addUpload function
const addImage = (imagepath, alt) => {
    let curPos = articleField.selectionStart;
    let textToInsert = '\r![${alt}](${imagepath})\r';
    articleField.value = articleField.value.slice(0,curPos) + textToInsert + articleField.value.slice(curPos);
}

//make the publish button functional
let months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

publishBtn.addEventListener('click', () => {
    //generating ID
    let letters = 'abcdefghijklmnopqrstuvwxyz';
    let blogTitle = blogTitleField.valu.split(" ").join("-");
    let id = '';
    for(let i = 0; i<4; i++){
        id += letters[Math.floor(Math.random() * letters.length)];
    }

    //setting up the docname
    let docName = '${blogTitle}-${id}';
    let date = new Date(); // for published at info

    // access firestore with db variable;
    db.collection("blogs").doc(docName).set({
        title: blogTitleField.value,
        article: articleField.value,
        bannerImage: bannerPath,
        publishedAt: '${date.getDate()} ${months[date.getMonth()]} ${date.getFullYear()}'
    })
    .then(() => {
        location.href = '/${docName}';
    })
    .catch((err)=>{
        console.error(err);
    })
})