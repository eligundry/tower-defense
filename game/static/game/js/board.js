function Board() {
	this.settings = {
		tile: {
			width: 100,
			height: 100
		}
	};

	this.data = JSON.parse($('#board-json').text());
	this.svg = Snap.select("#board");
	this.board_group = this.svg.group();
	this.svg_elm = $('#board');
	this.width = this.data.width;
	this.height = this.data.height;
	this.tiles = [];

	this.ResizeBoard(window.innerWidth, window.innerHeight);
	this.GenerateBoard();
}

Board.prototype.ResizeBoard = function(width, height) {
	this.svg_elm.css({
		height: height,
		width: width
	});
};

Board.prototype.GenerateBoard = function() {
	for (var y = 0; y < this.height; y++) {
		for (var x = 0; x < this.height; x++) {
			var tile = this.svg.rect(
				x * this.settings.tile.width,
				y * this.settings.tile.height,
				this.settings.tile.width,
				this.settings.tile.height
			);

			tile.attr({
				fill: "#bada55",
				stroke: "#000",
				strokeWidth: 5,
				id: x + ", " + y,
				class: "tileClass " + x + " " + y,
				locationx: x,
				locationy: y,
				onmouseover: "evt.target.setAttribute('opacity', '0.5');",
				onmouseout: "evt.target.setAttribute('opacity','1)');",
				onclick: "tileMenu(this);"
			});

			this.board_group.add(tile);
			this.tiles.push(tile);
		}
	}

	this.pan_zoom = svgPanZoom('#board');
};
