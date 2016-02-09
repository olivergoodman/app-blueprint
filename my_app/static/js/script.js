//script for personal page

$(document).ready(function(){
	console.log("it's working");

	//creating json objext which contains page's title
	var page_title = 
		{
			page_title: $(document).attr('title')
		};

	$.ajax({
		type: 'POST',
		url: '/_get_page_title',
		data: page_title,
		contentType: 'application/json;charset=UTF-8',
		success: function(response) {
        	console.log(response);
        },
        error: function(error) {
        	console.log(error)}
        });		



	$('div.hidden').fadeIn(2000).removeClass("hidden"); //title not fading right now
	//$('div.slideR').animate({right: "-500px"}, 1000);
	$('div.slideL').animate({left: "-500px"}, 1000);
});