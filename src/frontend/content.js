/**
 * Search for a video on the page.
 * Take it's url and send it to the python backend.
 * Store the answer from the backend in chrome.storage.
 * 
 * @author Yannick Bellerose
 * @version 1.0.0
 */

window.onload = function(){
	searchVid();
}

/**
 * Search for a video in the web page. It's the main logique run on oppening a new window.
 */
function searchVid(){
	var myVideo = document.getElementsByTagName("video");
	if (myVideo.length == 1) {
		webStore("Extracting your video");
		var src = myVideo[0].getAttribute("src");
		if (checkNull(src)){
			src = myVideo[0].getElementsByTagName("source")[0].getAttribute("src");
		}
		if (!checkNull(src)){
			urlToJson(src);
		} else {
			webStore("Problem getting video source");
		}
	} else if (myVideo.length > 1){
		webStore("Found more than one video - this feature is not yet implemented");
	} else {
		webStore("Can't find a video on the page");
		setTimeout(searchVid, 2500);
	}
}

function checkNull(str){
	return str == null || str == "" || str == "null";
}

function webStore(message){
	console.log("INFO: "+message);
	chrome.storage.local.set({url: message});
}

/**
 * A tool that receive am url, create an http post query, send it to the back end and save the result in chrome.storage.
 * 
 * @param vid the url of the video
 */
function urlToJson(vid){
	console.log("INFO: "+vid);
	let myUrl = "http://localhost:5000";
	let xhr = new XMLHttpRequest();
	xhr.open("POST", myUrl);
	xhr.setRequestHeader('Content-Type', 'application/json');

	xhr.onreadystatechange = function () {
	   if (xhr.readyState === 4) {
		webStore(xhr.responseText);
	   }};

	var val = "{\"URL\":\""+vid+"\"}";
	console.log("INFO: "+val);
	xhr.send(val);
}