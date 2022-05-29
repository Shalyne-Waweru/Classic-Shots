$(document).ready(function(){

  $(".tooltiptext").hide();

  // Share Button Hover Effect
  $(".shareBtn").hover(function(){
    $(".tooltiptext").toggle();
  });

  $(".shareBtn").click(function(){
    $(".tooltiptext").html("Copied to Clipboard!");
    $(".tooltiptext").css("background-color","#0979A5");

  });

});

// Get the modal
var modal = document.getElementById('my-Modal');

// Get the image and insert it inside the modal
var img = document.getElementsByClassName('gallery-img');
// var captionText = document.getElementById("caption").textContent;
// alert(captionText);

for(var i=0; i<img.length; i++){

  var modalImg = document.getElementById("img01");
  var modalCaption = document.getElementById("modal-caption");
  
  img[i].addEventListener('click',function(){
      modal.style.display = "block";
      modalImg.src = this.src;
      // modalCaption.innerHTML = captionText;
      
      // alert(captionText.textContent);
  })
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

