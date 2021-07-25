url = getActiveTab();
getUrl();

chrome.storage.onChanged.addListener((changes, namespace) => {
    getUrl();
});

function getUrl(){
    chrome.storage.local.get(url, function(result){
        document.getElementById("theUrl").innerHTML = result.url;
    });
}

function getActiveTab(){
    chrome.tabs.query({active:true},function(tab){
        return tab[0].url;
    });
}