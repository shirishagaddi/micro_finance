// JavaScript Document

$(document).ready(function(e) {
	
	//text-b0x focus
    $(".text-style").focus(function(e) {
        $(this).css("background-color","#ddd")
    });
	$(".text-style").blur(function(e) {
        $(this).css("background-color","#fff")
    });//text-box focus ends
	
	//btns
	$(".login-btn").mouseenter(function(e) {
        $(this).css("background-color","#2b4756")
    });
	$(".login-btn").mouseleave(function(e) {
        $(this).css("background-color","#019090")
    });
	
	//btns
	//slide bar
	$(".slide-bar").mouseenter(function(e) {
         $(this).animate({left:'90px'});
    });
	$(".slide-bar").mouseleave(function(e) {
         $(this).animate({left:'-10px'});
    });
	
	//main ends here
});