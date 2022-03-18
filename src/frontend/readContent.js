/**
 * The javascript called by the popup, it checks for change on chrome.storage.
 * It then automatically update the content of the pop up to display the message or the search bar.
 * 
 * @author Yannick Bellerose
 * @version 1.0.0
 */
var theForm;
var theText;
var theVal;

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
    chrome.tabs.query({active:true, currentWindow: true},function(tab){
        console.log("INFO: getUrl - "+tab[0].url);
        var pageUrl = tab[0].url;
        chrome.storage.local.get(pageUrl, function(result){  
            console.log("INFO: getUrl - " + result[pageUrl])       
            var str = result[pageUrl];
            if (typeof str === 'string' || str instanceof String) {
                searchDisplay(str);
            } else {
                displayAnswerLoaded();
            }   
        
        });
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
    chrome.tabs.query({active:true, currentWindow: true},function(tab){
        var pageUrl = tab[0].url;
        chrome.storage.local.get(pageUrl, function(result){         
            var myJson = result[pageUrl];
            if (typeof myJson === 'string' || myJson instanceof String) {
                console.log("ERROR: The transcription had a problem in the frontend");
                searchDisplay("ERROR: The transcription had a problem in the frontend");
            } else {
                displayResults(analyzeJson(myJson, theVal.value), theVal.value); 
            }   
        
        });
    });
}

function analyzeJson(json, word){
    var results = [];
    for (var i = 0; i<json.list.length; i++){
        if (json.list[i].includes(word)){
            results.push(i*json.step);
            console.log("INFO: analyzeJson - " + i*json.step);
        }
    }
    return results;
}

function displayResults(results, word){
    if (results.length == 0){
        searchDisplay("This word " + word + " doesn't appear in the video");
    } else {
        searchDisplay("The word " + word + " appears at time: " + results.join(" - ") + " seconds");
    }
}

function searchDisplay(text){
    theText.style.display = "block";
    theText.textContent = text;
    console.log("INFO: searchDisplay - "+text);
}

function displayAnswerLoaded(){
    theForm.style.display="block";
    theText.style.display = "none";
    console.log("INFO: displayAnswerLoaded");
}