$(function() {   

    $("#navigation a").addClass("nav");


    function toggle_on() {
	if ($(this).hasClass("selected")) {
	    return;
	}
	else {
	    $(this).addClass($(this).attr("title"));
	}
    }

    function toggle_off() {
	if ($(this).hasClass("selected")) {
	    return;
	}
	else {
	    $(this).removeClass($(this).attr("title"));
	}
    }

    $("#navigation a").hover(toggle_on, toggle_off);


})

    
