var namesFemale = ["Absent","Adamance ","Aide","Angel","Anomaly","Ash","Ashes","Aurora","Beak","Bling","Blinkey","Blossom","Bones","Books","Bookworm","Box","Boxey","Bubblegum","Bucks","Bugs","Butterfly","Cascade","Chance","Cinders","Clarity","Cloak","Cloud","Clumsy","Dancer","Darling","Daydream","Desire","Doc","Doctor","Dot","Dragonfly","Dust","Elsewhere","Ember","Enigma","Exo","Facade","Face","Faith","Feather","Feathers","Fiddles","Fix","Flower","Fluque","Fortune","Foxy","Freak","Freakshow","Freckles","Gadget","Gentle","Ghost","Gloom","Grace","Heat","Hive","Hog","Honey","Hope","Huntress","Hybrid","Hydra","Imp","Ion","Jams","Jester","Joy","Longshot","Lotus","Magma","Magpie","Mask","Mendy","Minx","Misty","Moon","Mopes","Muse","Naughty","Needle","Nemo","Nightmare","Nightowl","Nocturne","Oddity","Patch","Patches","Penance","Pepper","Petal","Pickle","Piggy","Pixy","Plasma","Prodigy","Puzzle","Puzzles","Pygmy","Raine","Random","Rascal","Riddle","Risque","Rogue","Rubble","Saber","Serpente","Silence","Silver","Siren","Skins","Skit","Skitters","Sky","Slime","Slimey","Sly","Smokes","Snail","Snout","Snow","Soot","Specter","Spikes","Spirit","Spot","Spots","Sprite","Starlight","Sunshine","Tadpole","Tags","Tattoo","Tinder","Tinkle","Tooths","Toothsey","Toots","Tootsey","Trace","Twinkle","Utopia","Vex","Vipra","Vyolet","Weeds","Whisper","Wicked","Wings","Wink","Wish","Witch","Wither","Woe","Zero"];
var namesMale = ["Absent","Adamance ","Aide","Angel","Anomaly","Ash","Atlas","Beak","Beast","Bishop","Bling","Blinkey","Blob","Blood","Bolt","Bones","Books","Bookworm","Box","Bravo","Bucks","Buffalo","Bugs","Bullet","Bulletproof","Cable","Captain","Chance","Chaos","Cinders","Cloak","Cloud","Clumsy","Cobalt","Cyclops","Dagger","Dancer","Daydream","Doc","Doctor","Dragonfly","Dust","Elsewhere","Exo","Facade","Face","Fallen","Feather","Feathers","Fiddles","Fix","Flood","Fluke","Freak","Freakshow","Frenzy","Gadget","Gentle","Ghost","Glob","Gloom","Gremlin","Grub","Hawk","Heat","Hermit","Hijack","Hive","Hog","Hunter","Husk","Hybrid","Hydro","Imp","Inn","Ion","Jams","Jester","Jet","Lance","Leech","Longshot","Maggot","Magma","Marsh","Mask","Mercury","Mime","Mist","Moon","Moose","Mopes","Muzzle","Naughty","Needle","Nemo","Newman","Nightmare","Nightowl","Nocturne","Oaf","Oak","Omega","Ooze","Patch","Patches","Penance","Phantom","Pickle","Piggy","Plasma","Prodigy","Puzzle","Puzzles","Pygmy","Pyro","Rain","Random","Rascal","Rat","Riddle","Rig","Rigs","Risk","Roach","Rogue","Rubble","Saber","Scooter","Serpent","Silence","Silver","Skeleton","Sketch","Skins","Skit","Skitters","Sky","Slime","Sly","Smokes","Snail","Snout","Snow","Soot","Specter","Spike","Spikes","Spirit","Spot","Spots","Sprite","Stonewall","Striker","Tadpole","Tags","Tattoo","Thorn","Thunder","Tinder","Toad","Tooth","Triclops","Viper","Weeds","Whisper","Wicked","Wings","Wink","Wither","Worm","Zero"];
var namesNeutral = ["Absent","Adamance ","Aide","Angel","Anomaly","Ash","Beak","Bling","Blinkey","Blob","Bones","Books","Bookworm","Box","Bucks","Bugs","Chance","Cinders","Cloak","Cloud","Clumsy","Cyclops","Dancer","Daydream","Desire","Doc","Doctor","Dragonfly","Dust","Elsewhere","Exo","Facade","Face","Feather","Feathers","Fiddles","Fix","Fluke","Freak","Freakshow","Frenzy","Gadget","Gentle","Ghost","Gloom","Heat","Hive","Hog","Hybrid","Imp","Ion","Jams","Jester","Leech","Longshot","Maggot","Magma","Mask","Mime","Moon","Moonshine","Moose","Mopes","Naughty","Needle","Nemo","Nightmare","Nightowl","Nocturne","Patch","Penance","Pickle","Piggy","Plasma","Prodigy","Puzzle","Puzzles","Pygmy","Random","Rascal","Riddle","Risk","Rogue","Rubble","Saber","Silence","Silver","Skins","Skit","Skitters","Sky","Slime","Sly","Smokes","Smokey","Snail","Snout","Snow","Soot","Specter","Spikes","Spirit","Spot","Spots","Sprite","Tadpole","Tags","Tattoo","Tinder","Tooth","Triclops","Weeds","Whisper","Wicked","Wings","Wink","Wither","Zero"];
var br = "";

function nameGen(type){
	var tp = type;
	if(tp === 1){
		var names1 = namesFemale;
	}else if(tp === 2){
		var names1 = namesNeutral;
	}else{
		var names1 = namesMale;
	}
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		names = names1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}