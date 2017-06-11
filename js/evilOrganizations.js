var nm1 = ["Aero","Anarchy","Aqua","Arachnid","Arcane","Ash","Avalon","Awe","Bane","Barrage","Black Mark","Blackout","Blank","Blaze","Blight","Bolt","Brain","Cerebro","Chaos","Chrome","Chronos","Cinder","Clone","Cloud","Collapse","Comet","Cosmos","Cringe","Curse","Dash","Death","Dire","Dismay","Dread","Dust","Dynamo","Echo","Eclipse","Ecto","Eternity","Fear","Flock","Frost","Frostburn","Funk","Furor","Fury","Gargoyle","Germ","Ghost","Grim","Grime","Hallow","Harm","Hive","Horror","Hydro","Iron","Judgment","Karma","Knockout","Legion","Libra","Lightning","Miasma","Micro","Midnight","Mime","Mirage","Mirror","Mist","Moira","Murk","Myriad","Myth","Nano","Necron","Nemesis","Nether","Nightmare","Nite","Nitro","Null","Obsidian","Onyx","Orion","Parallel","Phantom","Phobia","Poison","Psi","Psych","Pyro","Quake","Quantum","Rise","Ruin","Rust","Scorpio","Scourge","Serpent","Shade","Shadow","Shock","Shroud","Silence","Sliver","Specter","Spike","Spite","Steel","Stigma","Storm","Swarm","Syndicate","Taint","Taunt","Terror","Thunder","Torment","Toxin","Twilight","Twist","Valhalla","Veil","Venom","Virus","Visage","Void","Whisper","Wrath","Zion"];
var nm2 = ["Anarchy","Arcane","Ash","Barrage","Battle","Beast","Behemoth","Blackout","Blaze","Blight","Cataclysm","Chaos","Chrome","Chrono","Cipher","Clone","Cobalt","Cosmos","Crypt","Curse","Cyber","Dead","Death","Demon","Devil","Diablo","Dire","Doom","Dragon","Dread","Echo","Elemental","Enigma","Fear","Fiend","Fire","Frost","Fury","Gargoyle","Ghost","Gloom","Grim","Hallow","Hate","Horror","Imp","Infernal","Inferno","Iron","Judgment","Justice","Karma","Knockout","Liberty","Lightning","Midnight","Millennium","Mutant","Nano","Necro","Necron","Nemesis","Nether","Nightmare","Obsidian","Odium","Onyx","Phantom","Poison","Psi","Psycho","Pyro","Quantum","Salvation","Serpent","Shadow","Shock","Silent","Sinner","Slayer","Specter","Spectral","Spite","Steel","Storm","Terror","Thunder","Torment","Toxin","Twisted","Undead","Universe","Unknown","Unseen","Vengeance","Venom","Verdict","Vile","Virus","Void","War","Warlord","Wicked"];
var nm3 = ["Assembly","Brigade","Brotherhood","Clan","Company","Corps","Council","Crew","Force","Posse","Sisterhood","Squad","Tribe","Order"];
var nm4 = ["Anarchy","Ash","Battle","Blaze","Blight","Chaos","Chrome","Chronos","Ciphers","Clones","Crypts","Curses","Death","Demons","Devilry","Diablo","Dire","Doom","Dragons","Dread","Echos","Elementals","Fear","Fiends","Fire","Frost","Fury","Gargoyles","Ghosts","Gloom","Grim","Hallow","Hate","Hatred","Horror","Imps","Infernos","Iron","Judgment","Justice","Karma","Liberty","Lightning","Midnight","Mutants","Nightmares","Obsidian","Odium","Onyx","Phantoms","Poison","Psychos","Pyro","Pyromaniacs","Salvation","Serpents","Shadow","Shock","Silence","Sin","Sinners","Slayers","Specters","Spite","Steel","Storm","Terror","Thunder","Thunders","Torment","Toxin","Vengeance","Venom","Verdicts","War","Warlords","the Arcane","the Beast","the Behemoth","the Cataclysm","the Cosmos","the Curse","the Dead","the Devil","the Elements","the Enigma","the Infernal","the Inferno","the Mutant","the Necro","the Nether","the Nightmare","the Phantom","the Serpent","the Shade","the Sinner","the Slayer","the Specter","the Twisted","the Undead","the Universe","the Unknown","the Unseen","the Virus","the Void","the Warlord","the Wicked"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 4){
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd];
		}else if(i < 7){
			rnd = Math.floor(Math.random() * nm2.length);
			rnd2 = Math.floor(Math.random() * nm3.length);
			names = nm2[rnd] + " " + nm3[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			names = nm3[rnd] + " of " + nm4[rnd2];
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