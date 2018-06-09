// 1. An event occurs in a web page (the page is loaded, a button is clicked)
// 2. An XMLHttpRequest object is created by JavaScript
// 3. The XMLHttpRequest object sends a request to a web server
// 4. The server processes the request
// 5. The server sends a response back to the web page
// 6. The response is read by JavaScript
// 7. Proper action (like page update) is performed by JavaScript


function loadDoc() {
  var xmlhttp = new XMLHttpRequest()
  xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
      document.getElementById("demo").innerHTML = xmlhttp.responseText;
    }
  }
  xmlhttp.open("GET", "demo_get2.asp?fname=Henry&lname=Ford", true);
  xmlhttp.send();
}


// Method	Description
// new XMLHttpRequest()	Creates a new XMLHttpRequest object
// abort()	Cancels the current request
// getAllResponseHeaders()	Returns header information
// getResponseHeader()	Returns specific header information
// open(method, url, async, user, psw)	Specifies the request

// method: the request type GET or POST
// url: the file location
// async: true (asynchronous) or false (synchronous)
// user: optional user name
// psw: optional password
// send()	Sends the request to the server
// Used for GET requests
// send(string)	Sends the request to the server.
// Used for POST requests
// setRequestHeader()	Adds a label/value pair to the header to be sent


// Property	Description
// onreadystatechange	Defines a function to be called when the readyState property changes
// readyState	Holds the status of the XMLHttpRequest.
// 0: request not initialized 
// 1: server connection established
// 2: request received 
// 3: processing request 
// 4: request finished and response is ready
// responseText	Returns the response data as a string
// responseXML	Returns the response data as XML data
// status	Returns the status-number of a request
// 200: "OK"
// 403: "Forbidden"
// 404: "Not Found"
// For a complete list go to the Http Messages Reference
// statusText	Returns the status-text (e.g. "OK" or "Not Found")
