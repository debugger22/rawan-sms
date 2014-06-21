$( document ).ready(function (){
	$(".head").onepage_scroll({
	   sectionContainer: "section", // sectionContainer accepts any kind of selector in case you don't want to use section
	   easing: "ease", // Easing options accepts the CSS3 easing animation such "ease", "linear", "ease-in", "ease-out", "ease-in-out", or even cubic bezier value such as "cubic-bezier(0.175, 0.885, 0.420, 1.310)"
	   animationTime: 400, // AnimationTime let you define how long each section takes to animate
	   pagination: true, // You can either show or hide the pagination. Toggle true for show, false for hide.
	   updateURL: false, // Toggle this true if you want the URL to be updated automatically when the user scroll to each page.
	   beforeMove: function(index) {}, // This option accepts a callback function. The function will be called before the page moves.
	   afterMove: function(index) {}, // This option accepts a callback function. The function will be called after the page moves.
	   loop: false // You can have the page loop back to the top/bottom when the user navigates at up/down on the first/last page.
	});
	

	$('.bold-line1').bind('inview', function(event, isInView, visiblePartX, visiblePartY) {
	  if (isInView) {
	    // element is now visible in the viewport
	    if (visiblePartY == 'top') {
	      // top part of element is visible
	    } else if (visiblePartY == 'bottom') {
	      // bottom part of element is visible
	    } else {
	      setTimeout(function () {$('.bold-line1').addClass('animated fadeInLeft');
	      							setTimeout(function (){$('.thin-line1').addClass('animated fadeInRight');},500);
	  								},500);
	      setTimeout(function () {$('#trend_image').addClass('animated fadeInRight');},500);
	    }
	  } else {
	    $('.bold-line1').animate({opacity:'0'});
	  	$('.bold-line1').removeClass('animated fadeInLeft');
	  	$('.thin-line1').removeClass('animated fadeInRight');
	  	$('#trend_image').removeClass('animated fadeInRight');
	  	$('#trend_image').animate({opacity:'0'});
	  }
	});

	$('.bold-line2').bind('inview', function(event, isInView, visiblePartX, visiblePartY) {
	  if (isInView) {
	    // element is now visible in the viewport
	    if (visiblePartY == 'top') {
	      // top part of element is visible
	    } else if (visiblePartY == 'bottom') {
	      // bottom part of element is visible
	    } else {
	      setTimeout(function () {$('.bold-line2').addClass('animated fadeInRight');},500);
	      setTimeout(function () {$('#broadcast_image').addClass('animated fadeInLeft');},500);
	    }
	  } else {
	    $('.bold-line2').animate({opacity:'0'},500);
	  	$('.bold-line2').removeClass('animated fadeInRight');
	  	$('#broadcast_image').removeClass('animated fadeInLeft');
	  	$('#broadcast_image').animate({opacity:'0'});
	  }
	});

	$('.bold-line3').bind('inview', function(event, isInView, visiblePartX, visiblePartY) {
	  if (isInView) {
	    // element is now visible in the viewport
	    if (visiblePartY == 'top') {
	      // top part of element is visible
	    } else if (visiblePartY == 'bottom') {
	      // bottom part of element is visible
	    } else {
	      setTimeout(function () {$('.bold-line3').addClass('animated fadeInLeft');},500);
	      setTimeout(function () {$('#notification_image').addClass('animated fadeInRight');},500);
	    }
	  } else {
	    $('.bold-line3').animate({opacity:'0'},500);
	  	$('.bold-line3').removeClass('animated fadeInLeft');
	  	$('#notification_image').removeClass('animated fadeInRight');
	  	$('#notification_image').animate({opacity:'0'});
	  }
	});

	$('.bold-line4').bind('inview', function(event, isInView, visiblePartX, visiblePartY) {
	  if (isInView) {
	    // element is now visible in the viewport
	    if (visiblePartY == 'top') {
	      // top part of element is visible
	    } else if (visiblePartY == 'bottom') {
	      // bottom part of element is visible
	    } else {
	      setTimeout(function () {$('.bold-line4').addClass('animated fadeInRight');},500);
	      setTimeout(function () {$('#minions_image').addClass('animated fadeInLeft');},500);
	    }
	  } else {
	    $('.bold-line4').animate({opacity:'0'},500);
	  	$('.bold-line4').removeClass('animated fadeInRight');
	  	$('#minions_image').removeClass('animated fadeInLeft');
	  	$('#minions_image').animate({opacity:'0'});
	  }
	});

});