var names1 = ["Adonis","Alcazar","Alibi","All Star","Altitude","Apex","Apollo","Aqua","Arcane","Archangel","Arctic","Aspect","Attitude","Aura","Aurora","Azure","Balthazar","Barbarian","Barrage","Bazaar","Blaze","Bliss","Bloom","Blossom","Borealis","Bounce","Boundary","Bullet","Bullseye","Burlesque","Cacao","Cameo","Cargo","Cat's Eye","Century","Chaos","Cinnamon","Cipher","Circus","Climax","Cloud","Cobalt","Cocoa","Code","Colosseum","Comedy","Compass","Cosmos","Creed","Crimson","Crystal","Cube","Debut","Delight","Delirium","Destiny","Detective","Deviant","Diamond","Diva","Drama","Duo","Echo","Eclipse","Ecstasy","Electric","Elegance","Element","Elysium","Embargo","Embassy","Ember","Emperor","Empire","Enchant","Enigma","Entity","Envy","Escape","Essence","Etcetera","Eternity","Euphoria","Fabric","Fantasia","Fantasy","Fate","Felicity","Fever","Fiber","Fiction","Fire","Flower","Fortune","Forum","Frenzy","Frontier","Galaxy","Gallery","Glacier","Glee","Grace","H20","Harmony","Heaven","Horizon","Hysteria","Icecube","Illusion","Indigo","Inferno","Infinity","Insanity","Irony","Ivory","Ivy","Jade","Justice","Karma","Knockout","Lavender","Lily","Lime","Liquid","Loop","Loophole","Lost","Lucifer","Luck","Luna","Magenta","Magic","Mahogany","Majesty","Matter","Meltdown","Memo","Metropolis","Mint","Miracle","Mirage","Mirth","Monarch","Myriad","Mystery","Mystic","Myth","Nebula","Nemesis","Nightingale","Nightshade","Nine Lives","Nirvana","Nova","Obelisk","Obsidian","Ocean","Opal","Oracle","Orchid","Oxygen","Palace","Paradise","Paragon","Parallel","Paramount","Particle","Passion","Penthuose","Petal","Phantom","Phobia","Phoenix","Pinnacle","Priority","Prodigy","Profile","Prophecy","Pulse","Pyre","Quicksilver","Ragdoll","Rapture","Realm","Record","Reflex","Reincarnation","Reply","Republic","Resilience","Revolution","Riddle","Rogue","Rose","Rouge","Royale","Ruby","Sanction","Sanguine","Sanity","Sapphire","Sarcasm","Satire","Scarlet","Scent","Secret","Sepia","Serenity","Shadow","Silver","Sin","Sketch","Snowflake","Solo","Sphinx","Spice","Spirit","Storm","Studio","Summit","Supernova","Syndrome","Telepathy","Tempest","Temple","Temptation","Thunder","Tranquility","Trinity","Trinket","Triumph","Troy","Twilight","Typhoon","Universe","Utopia","Vampire","Vanish","Vapor","Veil","Venue","Venus","Vertex","Vigor","Vision","Volts","Vortex","Werewolf","Whisper","Zion"];
var names2 = ["Adventure","Agenda","Album","Angel","Answer","Aquarium","Arrow","Attitude","Aura","Aurora","Avenue","Barbarian","Beach","Blossom","Bolt","Brew","Bridge","Bullet","Cameo","Capital","Castle","Century","Champion","Cherry","Circus","Coach","Code","Codename","Core","Court","Crobar","Crown","Crypt","Demon","Den","Deviant","Devil","Dove","Dream","Eclipse","Element","Emperor","Empire","Escape","Essence","Finale","Fire","Floor","Flux","Focus","Fortress","Forum","Foundation","Fragment","Galaxy","Gallery","Garage","Garden","Garrison","Gate","Grind","Groove","Harp","Heart","Heat","Hour","Hub","Hunt","Illusion","Incubus","Inferno","Ivy","Jive","Jungle","King","Lagoon","Legacy","Lily","Lion","Lodge","Loop","Loophole","Manor","Match","Millenium","Ministry","Mist","Monarch","Moon","Myth","Needle","Nest","Night","Nomad","Origin","Original","Parlour","Pavilion","Petal","Phantom","Place","Plan","Pride","Prince","Profile","Project","Propaganda","Punch","Punchline","Qube","Queen","Question","Raffle","Release","Resistance","Rhythm","Rogue","Rule","Shadow","Ship","Shore","Shout","Silver Spoon","Sin","Sketch","Sliver","Solstice","Spy","Station","Storm","Studio","Succubus","Summit","Sun","Supernova","Swan","Temptation","Theatre","Thirst","Thorn","Thunder","Titan","Tomb","Trinity","Tunnel","Underground","Underworld","Union","Universe","Vault","Veil","Venue","Vibe","View","Vine","Vision","Vortex","Whisper"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 3){
			rnd = Math.floor(Math.random() * names1.length);
			names = names1[rnd];
		}else if(i < 5){
			rnd = Math.floor(Math.random() * names1.length);
			names = "Club " + names1[rnd];
		}else{
			rnd = Math.floor(Math.random() * names2.length);
			names = "The " + names2[rnd];
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