/**
 * The javascript called by the popup, it checks for change on chrome.storage.
 * It then automatically update the content of the pop up to display the message or the search bar.
 * 
 * @author Yannick Bellerose
 * @version 1.0.0
 */
var url = chrome.tabs.query({active:true},function(tab){return tab[0].url;});
var myJson;
var theForm;
var theText;

window.onload = function(){
    theForm = document.getElementById("theForm");
    theText = document.getElementById("theText");
    theVal = document.getElementById("word");
	getUrl();
    chrome.storage.onChanged.addListener((changes, namespace) => {
        getUrl();
    });
    theForm.onsubmit = searchIt;
}



/**
 * Gets called when chrome.storage change. 
 * If it's a json it means we have received a valid response from the server. We then call createHtml.
 * Otherwise we simplys display the content of chrome.storage
 */
function getUrl(){
    chrome.storage.local.get(url, function(result){
        str = result.url;
        try {
            myJson = JSON.parse(str);
            theForm.style.display="block";
            theText.display = "none";
        } catch (e) {
            theText.textContent = str;
        }   
    });
}

/**
 * A function that take the value extracted in getUrl and the value in the form.
 * It then search in the JSON for the value and calculate where it is in the file.
 * Afterwards it display it
 *  
 * @param event the submit event that triggered the search, to stop the normal submit
 */
function searchIt(event){
    event.preventDefault();
    theText.display = "block";
    var results = [];
    for (var i = 0; i<myJson.list.length; i++){
        if (myJson.list[i].includes(theVal.value)){
            results.push(i*myJson.step);
        }
    }
    if (results.length == 0){
        theText.textContent = "This word " + theVal.value + " doesn't appear in the video";
    } else {
        theText.textContent = "The word " + theVal.value + " appears at time: " + results.toString() + " seconds";
    }
}
