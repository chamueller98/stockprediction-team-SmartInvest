function updateFollowers() {
  console.log("hi from updateFollowers");
  let personal_name = prompt("What's your name?");
  let result = "Your name is: " + personal_name;
  console.log(result);
  let name = document.getElementById("followers");
  window.open("/3?name="+personal_name, "_top");
}

window.updateFollowers = updateFollowers;

// ask user for amount of followers --> prompt
// get element to update
// update textContenet of element with what the user entered
