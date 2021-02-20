var navigation = document.getElementById("navigation");
var topHeader = document.getElementById("topHeader");


window.onscroll = function(){
    if(document.body.scrollTop > 70 || document.documentElement.scrollTop > 70){
        navigation.classList.remove("pleaseStay");
        navigation.classList.add("scrollWithMe");
    } else{
        navigation.classList.add("pleaseStay");
        navigation.classList.remove("scrollWithMe");
    }
}