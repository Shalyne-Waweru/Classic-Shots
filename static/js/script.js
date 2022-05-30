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

