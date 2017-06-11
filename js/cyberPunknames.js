
function nameGen(type){
	var nm1 = ["Acid","Aero","Agile","Alco","Alter","Answer","Ant","Arch","Art","Aspect","Audience","Aura","Aurora","Awe","Badge","Bait","Bandage","Bank","Banks","Bargain","Barrage","Basis","Bat","Beam","Beast","Beauty","Bee","Beetle","Bell","Bells","Bird","Blade","Blank","Block","Blunder","Bold","Bolt","Bomb","Bone","Bones","Bonus","Books","Boost","Boot","Boots","Brash","Brass","Brave","Bribe","Brick","Bright","Brush","Cable","Canine","Canvas","Cash","Catch","Cause","Cell","Cent","Chain","Chalk","Chance","Change","Chaos","Charge","Chart","Cheat","Checkmate","Click","Clock","Clocks","Cloud","Coarse","Coil","Collar","Complex","Console","Crash","Craven","Cross","Crumbs","Cycle","Dapper","Dare","Data","Deal","Design","Detail","Dish","Disk","Double","Dynamic","Dynamo","Edge","Ego","Elite","Eternity","Fearless","Feature","Feedback","Fickle","Fix","Flaky","Fluke","Friction","Frost","Gain","Game","Gear","Gene","Ghost","Gift","Glove","Grave","Grim","Habit","Hack","Hacks","Heat","Hide","Hollow","Hook","Ice","Impulse","Ink","Iron","Jumbo","Junior","Law","Light","Link","Lock","Luck","Mammoth","Math","Maths","Mellow","Memory","Mirror","Mouse","Nemo","Night","Nightowl","Nimble","Noise","Note","Nova","Number","Omen","Owl","Panther","Parcel","Path","Pathfinder","Patriot","Phase","Piece","Pitch","Poison","Prime","Print","Prompt","Push","Quote","Range","Rebel","Requiem","Riddle","Risk","Route","Sable","Scene","Score","Session","Shade","Shallow","Shift","Shiny","Signal","Silver","Slice","Slide","Spark","Spring","Status","Stitch","Stranger","Stretch","Survey","Switch","Thrill","Trick","Tune","Unit","Venom","Virus","Ward","Wicked","Wish","Zen","Zero","Zigzag","Zone"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		names = nm1[rnd];
		nm1.splice(rnd, 1);	
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}