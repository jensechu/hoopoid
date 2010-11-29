$(function(){
    
    var paper = Raphael("cloud", 400, 400);
    var back = paper.rect(0, 0, 400, 400);
    back.attr({fill: "#000"});

    var hoop_box = paper.rect(0, 0, 400, 400);
    hoop_box.attr({fill: "#000", stroke: "grey", "stroke-width": 10});

    var hoop = paper.circle(195, 200, 150, 150);
    hoop.attr({stroke: "red", "stroke-width": 10});
    
    var tape_path = paper.path("M 40 200 C 75 100 175 100 200 200 S 305 300 350 200");
    var tape = tape_path.attr({stroke: "white", "stroke-width": 3});
    
    function taping(){
	i = 0
	while (i < 360) {	    
	    tape.clone().rotate(i);
	    i += 10;
	}
    }

    taping();

    var tape_path2 = paper.path("M 40 200 C 75 100 175 100 200 200 S 305 300 350 200");
    var grip_tape = tape_path2.attr({stroke: "green", "stroke-width": 1});
    
    function taping2(){
	i = 0
	while (i < 360) {	    
	    grip_tape.clone().rotate(i);
	    i += 10;
	}
    }

    taping2();

    var hoop2 = paper.circle(195, 200, 146, 146);
    hoop2.attr({fill: "black"});
    var hoop3 = paper.circle(195, 200, 156, 156);
    hoop3.attr({stroke: "black", "stroke-width": 5});
 
/*    var tape = paper.path("M200 200L40 400, M200 200L10 400");
    tape.attr({stroke: "lightblue", "stroke-width": 10});
    
*/

    
})