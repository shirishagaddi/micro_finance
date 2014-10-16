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
	$(function() {
    $( "#datepicker" ).datepicker();
  });
  //branch 
	 $(".query-style").focus(function(e) {
        $(this).css("background-color","#ddd")
    });
	$(".query-style").blur(function(e) {
        $(this).css("background-color","#fff")
    });
	$(".submit-btn").mouseenter(function(e) {
        $(this).css("background-color","#172257")
    });
	$(".submit-btn").mouseleave(function(e) {
        $(this).css("background-color","#394ba0")
    });
	$(".cancel-btn").mouseenter(function(e) {
        $(this).css("background-color","#fe1800")
    });
	$(".cancel-btn").mouseleave(function(e) {
        $(this).css("background-color","#f63600")
    });
  //branch
//main ends here
});