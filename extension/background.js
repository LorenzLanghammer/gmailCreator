chrome.webRequest.onBeforeSendHeaders.addListener(
    function(details) {

        for (let header of details.requestHeaders) {
            if (header.name.toLowerCase() == 'user-agent') {
                header.value = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.208 Safari/537.36";
                break;
            }
        }

        return {requestHeaders: details.requestHeaders}
    },
    {urls:["<all_urls>"]},
    ["blocking", "requestHeaders"]
);






