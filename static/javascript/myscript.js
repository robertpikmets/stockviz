var inputs = document.getElementById('tickerList');
var all_inputs = []

function save_input() {
  var new_input = document.getElementById('userInput').value;
  all_inputs.push(new_input);
  document.getElementById('current').innerHTML = new_input;

  var entry = document.createElement('li');
  entry.className = 'list-group-item';
  //entry.style.cssText = 'background-color: red; color: white; display:inline-block; display:inline-block;';
  entry.appendChild(document.createTextNode(new_input));
  inputs.appendChild(entry);
  $("#userInput").val("")
}
