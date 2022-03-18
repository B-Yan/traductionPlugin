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
	if (window.location.href.includes("youtube.com") || window.location.href.includes("dailymotion.com") || window.location.href.includes("vimeo.com")) {
		urlToJson(window.location.href);
	} else {
		var myVideo = document.getElementsByTagName("video");
		if (myVideo.length == 1){
			try {
				var src = extractVideoSource(myVideo);
				urlToJson(src);
			} catch {
				webStore("We encountered a problem getting the video source")
			}
		} else if (myVideo.length > 1){
			webStore("Found more than one video - this feature is not yet implemented");
		} else {
			webStore("Can't find a video on the page");
			setTimeout(searchVid, 2500);
		}
	}
}

/**
 * 
 * 
 * @param myVideo document.getElementsByTagName("video")
 */
function extractVideoSource(myVideo){
	var src = myVideo[0].getAttribute("src");
	if (checkNull(src)){
		src = myVideo[0].getElementsByTagName("source")[0].getAttribute("src");
	}
	if (checkNull(src)){
		throw "can't extract video";
	}
	return src;
}

function checkNull(str){
	return str == null || str == "" || str == "null";
}

function webStore(message){
	console.log("INFO: webStore - "+message);
	var newMessage = "";
	if (message.charAt(0)=="{"){
		newMessage = "{\"" + window.location.href + "\":"+ message+ "}";
	} else {
		newMessage = "{\"" + window.location.href + "\":\""+ message+ "\"}";
	}
	console.log("INFO: webstore - "+newMessage)
	chrome.storage.local.set(JSON.parse(newMessage));
}

/**
 * A tool that receive an url, create an http post query, send it to the back end and save the result in chrome.storage.
 * 
 * @param vid the url of the video
 */
function urlToJson(vid){
	webStore("Extracting your video");
	console.log("INFO: urlToJson - "+vid);
	let myUrl = "http://localhost:5000";
	let xhr = new XMLHttpRequest();
	xhr.open("POST", myUrl);
	xhr.setRequestHeader('Content-Type', 'application/json');

	xhr.onreadystatechange = function () {
	   if (xhr.readyState === 4) {
		webStore(xhr.responseText);
	   }};

	var val = "{\"URL\":\""+vid+"\"}";
	console.log("INFO: urlToJson - "+val);
	xhr.send(val);
}