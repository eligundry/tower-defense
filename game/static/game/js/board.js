function Board() {
	this.settings = {
		tile: {
			width: 100,
			height: 100
		},
		monsters: {
			width: 100,
			height: 100,
			icons: {
				'archer': '/static/project_static/svg/Archer.svg',
				'warrior': '/static/project_static/svg/Warrior.svg',
				'brute': '/static/project_static/svg/Brute.svg'
			}
		}
	};

	this.data = JSON.parse($('#board-json').text());
	this.svg = Snap.select("#board");
	this.board_group = this.svg.group();
	this.svg_elm = $('#board');
	this.width = this.data.width;
	this.height = this.data.height;
	this.monsters = this.data.monster;
	this.monsters_group = [];
	this.towers = this.data.towers;
	this.tiles = [];

	this.ResizeBoard(window.innerWidth, window.innerHeight);
	this.GenerateBoard();
	this.RenderMonsters(this.enemies);
}

Board.prototype.ResizeBoard = function(width, height) {
	this.svg_elm.css({
		height: height,
		width: width
	});
};


Board.prototype.RenderTowers = function() {
	$.each(this.towers, function(i, e) {
	});
};

Board.prototype.RenderMonsters = function() {
	var self = this;

	$.each(this.monsters, function(i, m) {
		// this.group.image(image, position_x, position_y, size_x, size_y);
		var target = $('[data-x="'+ m.x +'"][data-y="'+ m.y +'"]');
		var x = Number(target.attr('x')),
			y = Number(target.attr('y')),
			icon = self.settings.monsters.icons[m['class']];

		var monster = self.board_group.g().image(
			icon,
			x,
			y,
			self.settings.monsters.width,
			self.settings.monsters.height
		);
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
				'data-x': x,
				'data-y': y,
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
