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
		},
		towers: {
			width: 100,
			height: 100,
			icons: {
				'castle': '/static/project_static/svg/Castle.svg',
				'lure': '/static/project_static/svg/Lure.svg',
				'oil': '/static/project_static/svg/Oil.svg',
				'turret': '/static/project_static/svg/Turret.svg',
				'watchtower': '/static/project_static/svg/WatchTower.svg',
				'mine': '/static/project_static/svg/Mine.svg'
			}
		}
	};

	this.data = JSON.parse($('#board-json').text());
	this.svg = Snap.select("#board");
	this.board_group = this.svg.group();
	this.svg_elm = $('#board');
	this.game_id = this.data.game_id;
	this.width = this.data.width;
	this.height = this.data.height;
	this.monsters = this.data.monster;
	this.monsters_group = [];
	this.towers = this.data.towers;
	this.tiles = [];

	this.ResizeBoard(window.innerWidth, window.innerHeight);
	this.GenerateBoard();
	this.RenderMonsters();
	this.RenderTowers();
	this.SetupWebSocket();
}

Board.prototype.SetupWebSocket = function() {
	this.websocket = new WebSocket('ws://' + window.location.host + '/ws/game?subscribe-group=game_' + this.game_id);

	this.websocket.onopen = function() {
		console.log("Connected");
	};

	this.websocket.onmessage = function(msg) {
		var data = JSON.parse(msg);
		console.log(data);
	};
};

Board.prototype.ResizeBoard = function(width, height) {
	this.svg_elm.css({
		height: height,
		width: width
	});
};


Board.prototype.RenderTowers = function() {
	var self = this;

	$.each(this.towers, function(i, t) {
		var target = $('[data-x="'+ t.x +'"][data-y="'+ t.y +'"]');
		var x = Number(target.attr('x')),
			y = Number(target.attr('y')),
			icon = self.settings.towers.icons[t['class']];

		var tower = self.board_group.g().image(
			icon,
			x,
			y,
			self.settings.towers.width,
			self.settings.towers.height
		);

		tower.attr({
			xpos: t.x,
			ypos: t.y,
			hp: t.hp,
			max_hp: t.max_hp,
			name: t.name,
			onmouseover: "evt.target.setAttribute('opacity', '0.5');",
			onmouseout: "evt.target.setAttribute('opacity','1)');",
			onclick: "towerMenu(evt.target.attributes.xpos.value, evt.target.attributes.ypos.value, evt.target.attributes.hp.value, evt.target.attributes.max_hp.value, evt.target.attributes.name.value);"
		});
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

		monster.attr({
			xpos: m.x,
			ypos: m.y,
			hp: m.hp,
			name: m.name,
			max_hp: m.max_hp,
			onmouseover: "evt.target.setAttribute('opacity', '0.5');",
			onmouseout: "evt.target.setAttribute('opacity','1)');",
			onclick: "monsterMenu(evt.target.attributes.xpos.value, evt.target.attributes.ypos.value, evt.target.attributes.hp.value, evt.target.attributes.max_hp.value, evt.target.attributes.name.value);"
		});
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
				xpos: x,
				ypos: y,
				onmouseover: "evt.target.setAttribute('opacity', '0.5');",
				onmouseout: "evt.target.setAttribute('opacity','1)');",
				onclick: "tileMenu(evt.target.attributes.xpos.value, evt.target.attributes.ypos.value);"
			});

			this.board_group.add(tile);
			this.tiles.push(tile);
		}
	}

	this.pan_zoom = svgPanZoom('#board');
};
