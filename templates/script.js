var navigation = document.getElementById("navigation");
var topHeader = document.getElementById("topHeader");
var uploadedImage = document.getElementById("uploadedImage");
var submitRoom = document.getElementById("submitRoom");


window.onscroll = function(){
    if(document.body.scrollTop > topHeader.clientHeight || document.documentElement.scrollTop > topHeader.clientHeight){
        navigation.classList.remove("pleaseStay");
        navigation.classList.add("scrollWithMe");
    } else{
        navigation.classList.add("pleaseStay");
        navigation.classList.remove("scrollWithMe");
    }
}


var formData;

function collectThisImage() {
    let thisImage = this.files[0];
    formData = new FormData();
    formData.append('file', thisImage);
}

function sendImage() {
    if (formData != undefined) {
       let xhr = new XMLHttpRequest();
        xhr.open('POST', "http://localhost:8080/upload", true);
        xhr.send(formData);
    } else {
        alert("no image selected")
    }
}

uploadedImage.addEventListener("change", collectThisImage, false);
submitRoom.addEventListener("click", sendImage)
