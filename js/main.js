var notas_id = ["nota_1","nota_2","nota_3","nota_4"];
var nota_actual = "nota_1";

var scroll_move_nota = 1000;
var scroll_play = true;
// Key Configuration

var nota_move_prev = 37;
var nota_move_next = 39;

var nota_move_prev_targus = 175;
var nota_move_next_targus = 174;

var nota_move_first = 38;
var nota_move_last = 40;

var pause_scroll = 13;
// var nota_move_prev = 38;
// var nota_move_next = 40;
// var nota_move_first = 37;
// var nota_move_last = 39;




//Jquery 1.8.3
//var $elems = $("html, body");
var $elems = $("body");
var delta = 0;

$(document).ready(function(){
	// enterFullscreen();
	console.log("Prompter");
    $("#foo").hide();
});

$(document).on("mousemove", function(e) {
    var h = $(window).height();
    var y = e.clientY - h / 2;
    delta = y * 0.07;

    //cursor
    $mouseY = e.clientY;


});

$(window).on("blur mouseleave", function() {
    delta = 0;
});


/*
(function f() {
    if(delta) {
		$("#cursor").css({top:$mouseY +'px'});

        $elems.scrollTop(function(i, v) {
        	$("#foo").text(v+delta);
            return v + delta;
        });

    }

    //cursor
    //$yp += (($mouseY - $yp)/12);
    //
    //webkitRequestAnimationFrame(f);
    requestAnimationFrame(f);
})();*/

function f() {
    if(delta) {
        

		$("#cursor").css({top:$mouseY +'px'});

        $elems.scrollTop(function(i, v) {
        	$("#foo").text(v+delta);
            return v + delta;
        });

        
    }



    //cursor
    //$yp += (($mouseY - $yp)/12);
    //
    //webkitRequestAnimationFrame(f);
    requestAnimationFrame(f);
}



////////////////  DRAW //////////////////
var fps = 30;
(function draw() {
	setTimeout(function() {
		requestAnimationFrame(draw);
		// Drawing code goes here
		if(delta) {
            if(scroll_play){
                $("#cursor").css({top:$mouseY +'px'});

                $elems.scrollTop(function(i, v) {
                    $("#foo").text(v+delta+"  --  "+delta);
                    return v + delta;
                });
            }else{

            }
			

		}

        var hits = $("#cursor").collision(".nota");
        // console.log( typeof hits[0]);
        if(typeof hits[0] == "undefined")
        {

        }else if(typeof hits[0] == "object"){
            
            nota_actual = hits[0].id;
            console.log(nota_actual)
        }

	}, 1000 / fps);
})();





///////////////////////////// Keyboard Functions //////////////

// var notas_id = ["nota_1","nota_2"];
// var nota_actual = 0;

$("body").keydown(function( event ){
       
        if(event.which == nota_move_first) 
        {
            // direction = "Arriba";

            $('html, body').animate({
                    scrollTop: $("#"+notas_id[0]).offset().top
                }, scroll_move_nota);

            
        }else if(event.which == nota_move_last) 
        {
            // direction = "Abajo";

            $('html, body').animate({
                    scrollTop: $("#"+notas_id[notas_id.length - 1]).offset().top
                }, scroll_move_nota);
            
        }else if((event.which == nota_move_prev) || (event.which == nota_move_prev_targus))
        {
            // direction = "Izquierda";
            // console.log("Nota Anterior");
            var actual_id = notas_id.indexOf(nota_actual);
            if(actual_id > 0)
            {
                console.log("Anterior: "+notas_id[actual_id-1]);
                $('html, body').animate({
                    scrollTop: $("#"+notas_id[actual_id-1]).offset().top
                }, scroll_move_nota);
            }
            
            
        }else if((event.which == nota_move_next) || (event.which == nota_move_next_targus))
        {
            // direction = "Derecha";
            console.log("Nota Siguiente");
            var actual_id = notas_id.indexOf(nota_actual);
            console.log("Actual: "+ actual_id+ " Len: " + notas_id.length.toString());
            if(actual_id < (notas_id.length -1)){
                console.log("Siguiente: "+notas_id[actual_id+1]);
                $('html, body').animate({
                    scrollTop: $("#"+notas_id[actual_id+1]).offset().top
                }, scroll_move_nota);
            }
        }else if(event.which == pause_scroll)
        {
            if(scroll_play){
                scroll_play = false;
            }else{
                scroll_play = true;
            }
        }
        
       
    });

$("body").click(function(){
    if(scroll_play)
    {
        scroll_play = false;
    }else{
        scroll_play = true;
    }
});


////////////// Mouse Full Control Targus /////////////////


    function returnFalse(e) {        
        return false;
    }

    $("body").bind("contextmenu", returnFalse);
    
    
   /* 
    
    // how many milliseconds is a long press?
    var longpress = 500;
    // holds the start time
    var start;

    $( "body" ).on( 'mousedown', function( e ) {
        start = new Date().getTime();
    } );

    $( "body" ).on( 'mouseleave', function( e ) {
        start = 0;
    } );

    $( "body" ).on( 'mouseup', function( e ) {
        
        
        switch (e.which) {
          case 1:
              // $("#ki").html('Left mouse button pressed');
              
              
              if ( new Date().getTime() >= ( start + longpress )  ) {
                 // $("#ki").html('long press!');
                    if(scroll_play)
                    {
                        scroll_play = false;
                    }else{
                        scroll_play = true;
                    }   
              } else {
                 // $("#ki").html('short press!'); 
                    var actual_id = notas_id.indexOf(nota_actual);
                    if(actual_id > 0)
                    {
                        console.log("Anterior: "+notas_id[actual_id-1]);
                        $('html, body').animate({
                            scrollTop: $("#"+notas_id[actual_id-1]).offset().top
                        }, scroll_move_nota);
                    }

              }
              
              break;
              
          case 2:
              // $("#ki").html('Middle mouse button pressed');
              break;
          case 3:
              // $("#ki").html('Right mouse button pressed');
                console.log("Nota Siguiente");
                var actual_id = notas_id.indexOf(nota_actual);
                console.log("Actual: "+ actual_id+ " Len: " + notas_id.length.toString());
                if(actual_id < (notas_id.length -1)){
                    console.log("Siguiente: "+notas_id[actual_id+1]);
                    $('html, body').animate({
                        scrollTop: $("#"+notas_id[actual_id+1]).offset().top
                    }, scroll_move_nota);
                }
              break;
          default:
              // $("#ki").html('You have a strange mouse');
      }
        
    } );*/