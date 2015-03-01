(function($) {
	board = new Board();

	$(window).resize(function() {
		board.ResizeBoard(window.innerWidth, window.innerHeight);
	});
})(jQuery);