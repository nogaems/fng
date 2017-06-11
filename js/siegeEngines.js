function nameGen(type){
	var nm1 = ["Aberration","Aegis","Allegiance","Anarchy","Angel Wing","Arachnid","Armageddon","Asteroid","Banshee","Barrage","Basilisk","Battlewolf","Behemoth","Black Talon","Blizzard","Blood Moon","Bloodlord","Bloodspiller","Bone Warden","Brimstone","Buzzard","Caretaker","Cascade","Catastrophe","Cerberus","Chimera","Cobra","Comet","Constrictor","Cosmos","Cauldron","Curator","Curtain's Fall","Cyclops","Degenerate","Demon Horns","Demon Owl","Demon Quake","Devil's Grimace","Devil's Punch","Divine Favor","Divine Vow","Dragon Spine","Dragon Visage","Dragonbreath","Dragonfire","Dragonsoul","Dragoon","Dreadnaught","Ebon Herald","Ebon Shadow","Echo","Eclipse","Electric Guardian","Emerald Flame","Enigma","Eruption","Eulogy","Eventide","Face of Death","Feral Beast","Fiend","Fire Rain","Flame Wall","Frankenstein","Freak Show","Freak of Nature","Gargantuan","Giant's Fist","Grace's Grace","Grave Digger","Grease Monkey","Grim Reaper","Hades","Harbinger","Harvester","Hell Bringer","Hellbird","Hellbrand","Hellion","Hellish Scream","Hercules","Hippogriff","Homage","Hornet","Horseman","Hydra","Icicle","Inferno","Intimidator","Iron Golem","Iron Warden","Ivory Sentinel","Ivory Stinger","Jaeger","Javelin","Juggernaut","King's Legacy","Knockout","Leech","Lion's Roar","Lockjaw","Lone Rider","Mammoth","Man Hunter","Maneater","Medusa","Messenger","Minotaur","Mongrel","Mosquito","Necro","Nether Fiend","Night Terror","Night Watcher","Nightfall","Nightmare","Oathbreaker","Oathkeeper","Oblivion","Obsidian Blitz","Obsidian Grip","Obsidian Maw","Oddysey","Omega","Omen","Onyx Grasp","Onyx Javelin","Oracle","Overture","Pandemonium","Perforator","Phantom","Phoenix","Pilgrim","Plague Bringer","Rabid Dog","Rain of Terror","Rampage","Raptor","Rattlesnake","Reaper","Requiem","Rhinoceros","Rigor Mortis","Sabertooth","Sasquatch","Savage","Scorpio","Seism","Serpent","Serpent Sling","Shepherd","Shooting Star","Silence","Siren","Skeletal Horse","Souleater","Specter","Sphinx","Stalker","Stardust","Steel Knuckles","Steelskin","Storm Cloud","Sunset","Super Nova","Supremacy","Swan Dive","Swan Song","Tempest","Tenderizer","Thunder","Thunder Herald","Thunderstorm","Tidal Wave","Tigress","Titan's Wrath","Toboggan","Tortoise","Tremor","Tribute","Trinity","Trojan","Tsunami","Twister","Typhoon","Tyrant","Valkyrie","Vampire","Void","Volcano","Wall of Death","Warbear","Warden","Warmonger","Whirlwind","Wicker Man","Widow Maker","Wyvern"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = "The " + nm1[rnd];
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