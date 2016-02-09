//script for personal page

$(document).ready(function(){
	console.log("Page loaded.");

	//creating json objext which contains page's title
	var page_title = $(document).attr('title')

	// getting 500 error
	$.ajax({
		type: 'POST',
		url: '/_get_page_title',
		data: {'page_title' : page_title},
		contentType: 'application/json;charset=UTF-8',
		dataType : "json",
		success: function(response) {
        	console.log(response);
        	console.log("Successfully passed data to server");
        },
        error: function(error) {
        	console.log(error);
        	console.log("Error in passing data to server");
        }
    });		



	$('div.hidden').fadeIn(2000).removeClass("hidden"); //title not fading right now
	//$('div.slideR').animate({right: "-500px"}, 1000);
	$('div.slideL').animate({left: "-500px"}, 1000);
});