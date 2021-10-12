var mess = "Can't find a video on the page";
var url = String(window.location.href);
webStore(mess);

window.onload = function(){
	searchVid();
}

function searchVid(){
	var myVideo = document.getElementsByTagName("video");
	if (myVideo.length == 1) {
		mess = myVideo[0].getAttribute("src");
	} else if (myVideo.length > 1){
		mess = "Found more than one video - this feature is not yet implemented";
	} else {
		setTimeout(searchVid, 2500);
	}
	webStore(mess);
	console.log(mess);
}

function webStore(message){
	chrome.storage.local.set({url: message});
	//alert(url);
}