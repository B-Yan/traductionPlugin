/**
 * The javascript called by the popup, it checks for change on chrome.storage.
 * It then automatically update the content of the pop up to display the message or the search bar.
 * 
 * @author Yannick Bellerose
 * @version 1.0.0
 */
var url = chrome.tabs.query({active:true},function(tab){return tab[0].url;});
var myJson;

window.onload = function(){
	getUrl();
}

chrome.storage.onChanged.addListener((changes, namespace) => {
    getUrl();
});

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
            document.getElementById("theUrl").style="display:none";
            document.getElementById("theForm").style="display:block";
        } catch (e) {
            document.getElementById("theUrl").innerHTML = str;
        }   
    });
}

//SearchIt doesn't work and I have no clues why... Is it this tab business?
function searchIt(){
    console.log("test");
    //extract word
    //listOfTime
    //for (var i...)
    //if contains word listOfTime.append(i)
    //theUrl.display + content = list
}
