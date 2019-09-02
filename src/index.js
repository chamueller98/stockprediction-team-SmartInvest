function updateFollowers() {
  console.log("hi from updateFollowers");
  let personal_name = prompt("What's your name?");
  let result = "Your name is: " + personal_name;
  console.log(result);
  let name = document.getElementById("followers");
  followers.textContent = number_followers;
}

function updateName() {
  console.log("hi from updateFollowers");
  let each_name = prompt("What is your name?");
  let result = "Hi, nice to meet you " + each_name;
  console.log(result);
  let name = document.getElementById("name");
  name.textContent = each_name;
}

window.updateFollowers = updateFollowers;

// ask user for amount of followers --> prompt
// get element to update
// update textContenet of element with what the user entered
