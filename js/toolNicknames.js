var nm1 = ["Angel Wing","Angler","Arm Buster","Automaton","Backscratcher","Band Aid","Bear Claw","Bear Paw","Bell","Belly","Big Beak","Big Blue","Big Buddy","Big Nose","Bigwig","Biter","Bodangle","Boomer","Braces","Breaker","Breather","Bridesmaid","Brute","Brute Force","Bubble","Bullet","Bullseye","Bumblebee","Burner","Buster","Butterfly","Button Hook","Buzz","Buzzer","Cage","Carrot","Cat Head","Cat Paw","Cheater","Cheese Grater","Chicken Beak","Chicken Catcher","Chipper","Choppers","Chucker","Clicker","Commander","Crusher","Cube","Dirty Bomb","Dislocator","Dismounter","Do-Goodie","Drag","Drag Bag","Dual Wing","Duck Foot","Duster","Eagle Eye","Feather","Firecrackers","Fish","Fish Head","Fixer","Fixeraller","Flasher","Flat Nose","Fluffer","Four Eyes","Friendly One","Frog","Fury","Fuse Gate","Ghost Catcher","Goat Head","Gobbler","Godzilla","Good-for-nothing","Goof","Goofy Hook","Grasshopper","Grater","Grinder","Ground Crusher","Guardian","Guts","Guzzler","Hand Press","Hand Shoe","Handler","Handy Dandy","Hard Head","Hog","Hole Digger","Hole Puncher","Hookclaw","Horn Head","Horseshoe","Icicle","Interogator","Jawbreaker","Jaybird","Jelly","Jiggle","Kicker","Killer","Knocker","Knockout","Knuckle Knocker","Leverager","Little Buddy","Little Green","Little Head","Locator","Looper","Loosener","Lumpy","Measurer","Meat Hook","Mega Laser","Mohawk","Monkey Face","Monkey Suit","Naga","Nail Clipper","Nail Uzi","Nutcracker","Old Yeller","Onion Skin","Parrot","Pawpaw","Pencil Neck","Persuader","Phaser","Picker","Pickle","Pie Knife","Pig Tails","Pignose","Pitcher","Plumber","Plumbstick","Pokey","Power Shower","Powpow","Prickle","Puffer","Pully","Puncher","Punisher","Puppy Eyes","Questioner","Rabbit Ears","Ram","Ram Head","Rambler","Rat Skin","Ratchet","Rattle","Rattle Gun","Remover","Ridge","Rocky","Rum Raddle","Saber","Sabertooth","Salsa","Scalpel","Scratcher","Screecher","Screw Loose","Scythe","Sea Shell","Seahorse","Shackles","Sharpner","Shoe String","Shover","Single Wing","Skater","Skiller","Slack Strap","Slacker","Slapper","Slipper","Sludge","Slug","Small Beak","Smasher","Smiter","Snackbox","Snake","Snapper","Snipsnap","Soft Head","Sparkler","Sparrow","Spiderleg","Spiker","Spine","Spoon","Sprocket","Spuds","Squeezer","Starfish","Stitcher","Stretcher","Stud","Stunner","Sweat Cap","Switcher","Talon","Tater","Tatertot","Terminator","Termite","Thief","Thingymabob","Tingler","Toothpick","Tracker","Trapper","Tumb Crusher","Tumb Wrench","Turner","Tweaker","Twister","Wacker","Watchamacallit","Wazoo","Wedger","Wedgies","Weeper","Weeping Bell","Wheel of Death","Whiskers","Whiskey Stick","Wiggle Stick","Wiggler","Winger","Wippersnapper","Wishywashy","Wizzer","Wonker","Woodhandle","Woodpecker","Wrapper","Zapper","Zigzag","Zipzap"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = "The " + nm1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}