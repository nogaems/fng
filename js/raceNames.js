var nm1 = ["Ace","Airjack","Apex","Babe","Baby Face","Backpain","Bandit","Baron/Baroness","Big Beat","Blackjack","Blade","Blizzard","Blondey","Blower","Blowover","Blue Devil","Bolt","Bomber","Breakout","Breeze","Brute","Brute Force","Buddy","Bullet","Bunny","Burnout","Buster","Butch","Cannonball","Carnage","Carwash","Chase","Chaser","Chopper","Clutch","Colonel","Comeback Kid","Comet","Crimson","Delta","Diesel","Digger","Dodge","Dodger","Doughnut","Drift","Drifter","Duster","Dynamite","Dynasty","Earthquake","Echelon","Enigma","Evasive","Fatality","Fearless","Fence","Fireball","Flash","Flopper","Formula Zero","Forza","Foxy","Freebird","Freestyle","Friction","Frosty","Frozenheart","Fury","General","Glacier","Gogo","Golden Kid","Goose","Gravels","Grenade","Gridline","Groovey","Hairpin","Hammer","Handsome","Happy","Havoc","Headway","Helmet Hair","Holeshot","Honker","Hotflash","Hunter/Huntress","Hurricane","Hybrid","Iceheart","Indy","Jolt","Jumper","Junior","Kamikaze","Kid","Kit","Knight","Leadfoot","Lightning","Lightning Bolt","Lightspeed","Lionheart","Little Lightning","Little Stint","Lollipop","Lucky","Mad Max","Magic Feet","Matrix","Maverick","Meatball","Momento","Mongoose","Mouse","Mr/Miss Menace","Muscles","Nemo","Newbie","Nitro","Oracle","Outlaw","Pitstop","Pocket Rocket","Prestige","Prodigy","Proto","Prototype","Quickshift","Railer","Rapido","Red","Red Devil","Redlight","Redline","Reflex","Road Runner","Rocketeer","Rodeo","Rubber","Rubberburn","Rumble","Rush","Rustle","Rusty","Salty","Sandbag","Savage","Scooter","Scorch","Scrub","Shade","Shadow","Shakey","Shortshift","Showtime","Skip","Skipper","Slingshot","Slugs","Smiley","Smokey","Smooth Ride","Snake","Spark","Speedstar","Spirit","Sprint","Spunk","Starflal","Straightline","Swifty","Swirl","T-Bone","Tandem","Tank","Tasmanian Devil","The Comeback","Thriller","Throttle","Turbo","Twitch","Typhoon","Velocity","Viper","Wheelie","Wheelspin","White Smoke","Wild Thing","Wings","Wolf","Wonderkid","Xelarate","Zero","Zero Light","Zigzag","Zoomer","Zoomzoom"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}