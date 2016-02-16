//script for personal page

$(document).ready(function(){
	console.log("Page loaded.");

	//creating json objext which contains page's title
	var page_title = $(document).attr('title');
	var data = {"page_title" : page_title};

	$.ajax({
		type: 'POST',
		url: '/_get_page_title',
		data: JSON.stringify(data, null, '\t'), //http://stackoverflow.com/questions/14908864/how-can-i-use-data-posted-from-ajax-in-flask
		contentType: 'application/json;charset=UTF-8',
		dataType : "json",
		success: function(response) {
        	console.log(response);
        	console.log("Successfully passed data to server");
        },
        error: function(error) {
        	console.log(error["statusText"] + ": could not pass data to server");
        }
    });		



	// $('div.hidden').fadeIn(2000).removeClass("hidden"); //title not fading right now
	// //$('div.slideR').animate({right: "-500px"}, 1000);
	// $('div.slideL').animate({left: "-500px"}, 1000);
});