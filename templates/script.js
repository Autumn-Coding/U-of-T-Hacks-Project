var navigation = document.getElementById("navigation");
var topHeader = document.getElementById("topHeader");
var uploadedImage = document.getElementById("uploadedImage");
var submitRoom = document.getElementById("submitRoom");
var customFileUpload = document.getElementById("custom-file-upload");
var checkedRoomType = document.querySelector('input[name="roomType"]:checked')

window.onscroll = function(){
    if(document.body.scrollTop > topHeader.clientHeight || document.documentElement.scrollTop > topHeader.clientHeight){
        navigation.classList.remove("pleaseStay");
        navigation.classList.add("scrollWithMe");
    } else{
        navigation.classList.add("pleaseStay");
        navigation.classList.remove("scrollWithMe");
    }
}


var formData = new FormData();

function collectImage() {
    customFileUpload.innerHTML = "Image uploaded";
    customFileUpload.classList.add('fileAddedDisplay');
    let thisImage = this.files[0];
    formData.append('file', thisImage);
}

function sendParameters() {
    if (checkedRoomType != undefined) {
        formData.set('roomtype', document.querySelector('input[name="roomType"]:checked').value);
    }

    if (formData.get('file') != undefined && formData.get('roomtype') != undefined) {
       let xhr = new XMLHttpRequest();
        xhr.open('POST', "http://localhost:8080/upload", true);
        xhr.send(formData);
    } else if (formData.get('file') != undefined) {
        alert("no room type selected");
    } else if (formData.get('roomtype') != undefined) {
        alert("no image selected");
    } else {
        alert("no image or room type selected");
    }
}

uploadedImage.addEventListener("change", collectImage, false);
submitRoom.addEventListener("click", sendParameters)
