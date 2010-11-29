$(function(){
    
    var paper = Raphael(document.getElementById("hoop"), 400, 400);
    
    var hoop_box = paper.rect(0, 0, 400, 400);
    hoop_box.attr({fill: "black"});

    //Create hoop and base tape color
    var hooper = paper.circle(195, 200, 150, 150);
    var hoop = hooper;
    hoop.attr({stroke: "#ff6699", "stroke-width": 10});
    
    //Path for all tapes
    var tape_path = paper.path("M 40 200 C 75 100 175 100 200 200 S 305 300 350 200").hide();

    //Tape generator
    function tape_generator(set){
	i = 0
	while (i < 360) {
	    set.push(
		tape_path.clone().rotate(i)
	    );
	    i += 10;
	}
	return set;
    }

    //Secondary tape generator
    var secondary_set = tape_generator(paper.set()).attr({stroke: "white", "stroke-width": 4});
    
    //Grip tape generator
    var grip_set = tape_generator(paper.set()).attr({stroke: "green", "stroke-width": 2});
     
    //Smooth out the tape edges    
    var inside_hoop = paper.circle(195, 200, 146, 146);
    inside_hoop.attr({fill: "#000"});
    var outside_hoop = paper.circle(195, 200, 156, 156);
    outside_hoop.attr({stroke: "#000", "stroke-width": 5});

    //Base colors
    $(".base.pink").click(function() {
	hoop.attr({stroke: "#ff6699"});
    });

    $(".base.blue").click(function() {
	hoop.attr({stroke: "#1B70E0"});
    });

    $(".base.green").click(function() {
	hoop.attr({stroke: "green"});
    });

    $(".base.white").click(function() {
	base_set.attr({stroke: "white"});
    });

    //Secondary colors
    $(".secondary.pink").click(function() {
	secondary_set.attr({stroke: "#ff6699"});
    });

    $(".secondary.blue").click(function() {
	secondary_set.attr({stroke: "#1B70E0"});
    });

    $(".secondary.green").click(function() {
	secondary_set.attr({stroke: "green"});
    });
    
    $(".secondary.white").click(function() {
	secondary_set.attr({stroke: "white"});
    });

    //Grip colors
    $(".grip.pink").click(function() {
	grip_set.attr({stroke: "#ff6699"});
    });

    $(".grip.blue").click(function() {
	grip_set.attr({stroke: "#1B70E0"});
    });

    $(".grip.green").click(function() {
	grip_set.attr({stroke: "green"});
    });
	
    $(".grip.white").click(function() {
	grip_set.attr({stroke: "white"});
    });
	
//Spin the hoop!
    
    $("#hoop_spin").click(function() {
	hoop.animate({rotation: 360}, 4000);
	secondary_set.animateWith(hoop, {rotation: 360}, 4000);
	grip_set.animateWith(hoop, {rotation: 360}, 4000);
    });
	
})