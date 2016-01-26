//script for personal page

$(document).ready(function(){
	console.log("it's working");

	/*
	//get current page title and send to backend
	$(function(){
		var current_title = $(document).attr('title');
		return current_title
	}) */

	$('div.hidden').fadeIn(2000).removeClass("hidden"); //title not fading right now
	//$('div.slideR').animate({right: "-500px"}, 1000);
	$('div.slideL').animate({left: "-500px"}, 1000);
});