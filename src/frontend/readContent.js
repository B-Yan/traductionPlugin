
chrome.storage.local.get(["AudioVideoUrl"], function(result){
    document.getElementById("theUrl").innerHTML = result.AudioVideoUrl;
});