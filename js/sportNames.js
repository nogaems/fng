function nameGen(){
	var nm1 = ["Acro","Adven","Aero","Air","Alpha","Ama","Anar","Ani","Aqua","Asteroi","Auto","Azu","Bad","Bala","Bea","Bia","Biath","Blitz","Brawl","Bungee","Chaos","Chrono","Clash","Comb","Comet","Corner","Crash","Cri","Cross","Cryo","Cy","Cyclo","Death","Deca","Demo","Demoli","Dino","Diplo","Dirt","Dis","Disc","Dog","Domi","Domina","Draft","Drag","Drago","Dri","Drift","Dril","Dual","Duo","Electri","Endu","Equi","Fien","Fluke","Fore","Free","Frost","Fur","Fury","Fuse","Geo","Giga","Gli","Glue","Grav","Grim","Gut","Gutter","Hi","Hollow","Hover","Hy","Hybri","Hypo","Ice","Immu","Indi","Infini","Inter","Kil","Laser","Lim","Lo","Mara","Mash","Matri","Maze","Mer","Meta","Mind","Mini","Mix","Mod","Mono","Mud","Neo","Nether","Nova","Omega","Orient","Pandemo","Para","Persi","Pitch","Pod","Prime","Pro","Psy","Pyra","Pyre","Pyro","Quad","Quadri","Quantum","Race","Rando","Resi","Reso","Rever","Ring","Ro","Roa","Rock","Rum","Sam","Scu","Scuf","Seg","Siege","Skele","Skir","Soar","Speed","Sti","Storm","Strate","Strato","Sub","Sur","Swor","Sym","Sys","Tag","Tele","Terri","Terror","Thunder","Tira","Tiro","Titan","Trampo","Tria","Triad","Trini","Tug","Tum","Ulti","Ultra","Uni","Venti","Vertex","Verti","Virti","Vitali","Void","Wall","War","Wel","Wheel","Wish","Wub","Zephy"];
	var nm2 = ["ball","base","bat","batics","boarding","chase","course","cross","crosse","cycling","derby","dive","diving","draft","game","glide","go","goal","hoop","line","ling","mix","net","play","pool","race","raid","rally","relay","sail","slam","style","surf","surfing","tag","ton","tour","trial","vault","volley"];
	var nm3 = ["Adventure","Aero","Aqua","Astral","Auto","Balance","Barrel","Battle","Beast","Big","Blind","Blitz","Bone","Bumper","Bungee","Capture","Chrono","Comet","Command","Corner","Crazy","Cross","Crush","Cryo","Cushion","Death","Decoy","Demolition","Dimension","Domination","Doom","Double","Dragon","Drone","Drop","Drum","Duel","Dynamic","Ember","Endurance","Escape","Eternity","Extreme","Field","Final","Floor","Fluster","Free","Freefall","Freestyle","Fury","Galaxy","Gate","Geo","Glider","Glove","Grand","Gravity","Grim","Hammer","High","Hound","Hurdle","Hurricane","Hyper","Ice","Illusion","Immortal","Infinity","Invasion","Iron","Jump","Laser","Leopard","Light","Low","Lunar","Maneuver","Martial","Maze","Mini","Mountain","Mud","Mystery","Nemo","Neo","Neuro","Night","Nimble","Nova","Obstacle","Oracle","Over","Paragon","Parallel","Pitch","Platform","Pod","Power","Primal","Prime","Pyre","Pyro","Quantum","Rally","Realm","Resolution","Retro","River","Roller","Row","Scrub","Serial","Shuffle","Silent","Sky","Smash","Snag","Snail","Snare","Snow","Soft","Solar","Sonic","Speed","Sprint","Stamina","Star","Stasis","Stealth","Stick","Sticky","Still","Storm","Strike","Stunt","Super","Swamp","Sync","Tag","Target","Terra","Tetra","Thunder","Time","Torpedo","Touch","Trial","Trick","Trigger","Tumble","Twister","Typhoon","Ultra","Universe","Vertex","Vertigo","Vision","Vortex","Wall","War","Water","Whack","Wheel","Zero-G","Zigzag"];
	var nm4 = ["Acrobatics","Attack","Ball","Base","Boarding","Chase","Combined","Course","Cross","Cycling","Derby","Dive","Diving","Draft","Game","Gliding","Goal","Hurl","Mix","Pitch","Play","Race","Raid","Rally","Relay","Ring","Rings","Rules","Sailing","Slam","Smash","Style","Surfing","Tag","Tour","Trial","Volley","War"];
	var br = "";
	
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + nm2[rnd2];
			nm1.splice(rnd, 1);
			nm2.splice(rnd2, 1);
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			names = nm3[rnd] + " " + nm4[rnd2];
			nm3.splice(rnd, 1);
			nm4.splice(rnd2, 1);
		}
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}