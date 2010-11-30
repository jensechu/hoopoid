$(function(){

    var paper = Raphael(document.getElementById("container"), 550, 550);    
 
    //Base hoop
    var hoop = paper.circle(300, 300, 200);
    hoop.attr({stroke: "#ff6699", "stroke-width": 20});

    //Path for all tapes
    var tape_path = paper.path("M200, 100 c-100,200 300,200 200,400");

    //Tape generator
    function tape_generator(set){
	i = 0
	while (i < 180) {
	    set.push(
		tape_path.clone().rotate(i)
	    );
	    i += 10;
	}
	return set;
    }

    //Secondary tape generator
    var secondary_set = tape_generator(paper.set()).attr({stroke: "white", "stroke-width": 15});
    
    //Grip tape generator
    var grip_set = tape_generator(paper.set()).attr({stroke: "green", "stroke-width": 6});
     
    //Smooth out the tape edges    
    var inside_hoop = paper.circle(300, 300, 190);
    inside_hoop.attr({fill: "#141414"});
    var outside_hoop = paper.circle(300, 300, 225);
    outside_hoop.attr({stroke: "#141414", "stroke-width": 40});

//Base colors
    $(".base.pink").click(function() {
	hoop.attr({stroke: "#ff6699"});
    });

    $(".base.light_blue").click(function() {
	hoop.attr({stroke: "#1B70E0"});
    });

    $(".base.green").click(function() {
	hoop.attr({stroke: "green"});
    });

    $(".base.white").click(function() {
	hoop.attr({stroke: "white"});
    });

    $(".base.black").click(function() {
	hoop.attr({stroke: "black"});
    });

    //Secondary colors
    $(".secondary.yellow").click(function() {
	secondary_set.attr({stroke: "yellow"});
    });

    $(".secondary.blue").click(function() {
	secondary_set.attr({stroke: "blue"});
    });

    $(".secondary.green").click(function() {
	secondary_set.attr({stroke: "green"});
    });
    
    $(".secondary.white").click(function() {
	secondary_set.attr({stroke: "white"});
    });

    $(".secondary.black").click(function() {
	secondary_set.attr({stroke: "black"});
    });

    //Grip colors
    $(".grip.neon_pink").click(function() {
	grip_set.attr({stroke: "#FF0066"});
    });

    $(".grip.neon_yellow").click(function() {
	grip_set.attr({stroke: "#D1ff03"});
    });

    $(".grip.neon_green").click(function() {
	grip_set.attr({stroke: "#0DE032"});
    });

    $(".grip.neon_orange").click(function() {
	grip_set.attr({stroke: "#ff1918"});
    });
	
    $(".grip.gray").click(function() {
	grip_set.attr({stroke: "gray"});
    });

})