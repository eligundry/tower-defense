(function($) {
	board = new Board();

	$(window).resize(function() {
		board.ResizeBoard(window.innerWidth, window.innerHeight);
	});

})(jQuery);

function tileMenu(x, y) {
	var menuHTML = "<span class='pure-menu-heading'>X" + x + ", Y" + y + "</span>";
	menuHTML += "<ul class='pure-menu-list'>";
	menuHTML += "<li class='pure-menu-item'><a onclick='spawnTurret("+x+", "+y+")' class='pure-menu-link'>Turret ($15)</a></li>";
	menuHTML += "<li class='pure-menu-item'><a onclick='spawnLure("+x+", "+y+")' class='pure-menu-link'>Lure ($5)</a></li>";
	menuHTML += "</ul>";

   $( "#menu-on-click" ).html(menuHTML);
}
function towerMenu(x, y, hp, max_hp, name) {
   	var menuHTML = "<span class='pure-menu-heading'>X" + x + ", Y" + y + "</span>";
   	menuHTML += "<span class='pure-menu-heading'>"+name+"</span>";
   	menuHTML += "<ul class='pure-menu-list'>";
   	menuHTML += "<li class='pure-menu-item'><span class='pure-menu-heading'>"+hp+"/"+max_hp+"</span></li>";
   	menuHTML += "<li class='pure-menu-item'><a onclick='destroy("+x+", "+y+")' class='pure-menu-link'>Destroy</a></li>";
   	menuHTML += "</ul>";

    $( "#menu-on-click" ).html(menuHTML);
}
function monsterMenu(x, y, hp, max_hp, name) {
	//doesn't handle multiple enemies per tile, only highest in the dom...
   	var menuHTML = "<span class='pure-menu-heading'>X" + x + ", Y" + y + "</span>";
   	menuHTML += "<span class='pure-menu-heading'>"+name+"</span>";
   	menuHTML += "<ul class='pure-menu-list'>";
   	menuHTML += "<li class='pure-menu-item'><span class='pure-menu-heading'>"+hp+"/"+max_hp+" HP</span></li>";
   	menuHTML += "</ul>";

    $( "#menu-on-click" ).html(menuHTML);
}

function spawnTurret(x, y) {
	console.log("spawn a turret at " + x + ", " + y);
}

function spawnLure(x, y) {
	console.log("spawn a lure at " + x + ", " + y);
}

function destroy(x, y) {
	console.log("destroy the tower at " + x + ", " + y);
}