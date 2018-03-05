$(document).ready(function() {  
	dailyrings.behave();

});

var dailyrings = {

	behave: function() {
		$('.disabled').click(function() {
			return false;
		});
	},	
}
