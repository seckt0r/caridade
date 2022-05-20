

	function tm_animate_text(){
	
		"use strict";
		
		var animateSpan			= jQuery('.animation_text_word');
		
			animateSpan.typed({
				strings: ["Donate to changing the world. Be part of the good campaign...", "Donate to changing the world. Be part of the good campaign...", "Donate to changing the world. Be part of the good campaign..."],
				loop: true,
				startDelay: 1e3,
				backDelay: 3e3
			});
	}

	jQuery(document).on('ready', function () {
		(function ($) {
			tm_animate_text();
		})(jQuery);
	});