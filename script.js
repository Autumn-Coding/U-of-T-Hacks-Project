var navigation = document.getElementById("navigation");
var topHeader = document.getElementById("topHeader");
var uploadedImage = document.getElementById("uploadedImage");


window.onscroll = function(){
    if(document.body.scrollTop > 70 || document.documentElement.scrollTop > 70){
        navigation.classList.remove("pleaseStay");
        navigation.classList.add("scrollWithMe");
    } else{
        navigation.classList.add("pleaseStay");
        navigation.classList.remove("scrollWithMe");
    }
}


function handleFileSelect(element) {
    const thisImage = this.files[0];
}


uploadedImage.addEventListener("change", handleFileSelect, false);