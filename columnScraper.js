/*
 * @Author: Paul McDowell
 * @License: MIT
 * @Description: The following script can be used to scrape orderly text from
 * tables displayed on websites for the purpose of generating word lists. 
 * Modify the columnName as needed to specify the name of the desired column after
 * inspecting the page source. this works great when dumped into the browser 
 * console for harvesting word lists from wikipedia tables. 
 * 
 * Important Note: Don't forget to donate to wikipedia! Without them, this script
 * wouldn't be nearly as useful.
*/
// make all the storage variables and target the appropriate
// table class used to store the named column TDs
var columnName = "summary";

var rawList = document.getElementsByClassName(columnName);
var combinedStr = '';
var namesList = [];

// grab each item's innerText field and remove the " quotes around it
for(let i = 0; i < rawList.length; i++) { 
	let tmpData = rawList[i].innerText;
	let unquoted = tmpData.substring(1,tmpData.length-1)
	namesList.push(unquoted); 
}
// dump the text to a one-per-line string format easily
// copied and pasted into a txt file
namesList.forEach(x => combinedStr = combinedStr + x + '\n');