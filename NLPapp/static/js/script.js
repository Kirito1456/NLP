// Get the modal
var modal = document.getElementById("myModal");
        
// Button that opens the modal
var btn = document.getElementById("myBtn");

// Get the  element that closes the modal
var span = document.getElementsByClassName("close")[0];

// User clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// Close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// User clicks anywhere outside of the modal, close modal
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}