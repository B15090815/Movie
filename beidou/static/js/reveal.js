/*
  * Normalized hide address bar for iOS & Android
  * (c) Scott Jehl, scottjehl.com
  * MIT License
*/
(function( win ){
	var doc = win.document;

	// If there's a hash, or addEventListener is undefined, stop here
	if( !location.hash && win.addEventListener ){

		//scroll to 1
		window.scrollTo( 0, 1 );
		var scrollTop = 1,
			getScrollTop = function(){
				return win.pageYOffset || doc.compatMode === "CSS1Compat" && doc.documentElement.scrollTop || doc.body.scrollTop || 0;
			},

			//reset to 0 on bodyready, if needed
			bodycheck = setInterval(function(){
				if( doc.body ){
					clearInterval( bodycheck );
					scrollTop = getScrollTop();
					win.scrollTo( 0, scrollTop === 1 ? 0 : 1 );
				}	
			}, 15 );

		win.addEventListener( "load", function(){
			setTimeout(function(){
				//at load, if user hasn't scrolled more than 20 or so...
				if( getScrollTop() < 20 ){
					//reset to hide addr bar at onload
					win.scrollTo( 0, scrollTop === 1 ? 0 : 1 );
				}
			}, 0);
		} );
	}
})( this );

$(document).ready(function() {
	
	// Set up
	$("#project-list").find('li:nth-child(3n + 1)').addClass('third');
	$("#project-list").find('li:nth-child(2n + 1)').addClass('second');
	var navHeight = $('#menu-main-menu').height();
	iframeResize();
		
	// Populate Default Field Values
	$('#author').defaultValue("Name");
	$('#email').defaultValue("Email (Not Published)");
	$('#url').defaultValue("Website");
	$('#comment').defaultValue("Your Thoughts");
	
	// Bind some stuff
	$(window).resize(function () {
		iframeResize();
		});
	window.onorientationchange = function() {
		iframeResize();
		}
	$('#menu-toggle').click(function () {
		$('#branding').toggleClass('navOn');
		})
	$('.comments-toggle').click(function(){
		$(this).toggleClass('out')
		if ($(this).hasClass('out')) {
			$(this).html('hide&nbsp;&nbsp;<img src="http://www.strangenative.com/wp-content/themes/strange native 4/images/bubble-ico.png" alt="comments">');	
		} else {
			$(this).html('show&nbsp;&nbsp;<img src="http://www.strangenative.com/wp-content/themes/strange native 4/images/bubble-ico.png" alt="comments">');
		}
		$(this).next().slideToggle("slow");
	});

	// Functions
	function iframeResize() {
		$('iframe').each(function () {
			var ratio = $(this).attr('height') / $(this).attr('width');
			var contentWidth = $(this).parent().width();
			$(this).attr('width', contentWidth).attr('height', contentWidth * ratio);
			});
		}
});

