var namesMale = ["Bane","Barrage","Beast","Birdman","Bizarre","Blade","Blitz","Blueprint","Bombardment","Boomboom","Boulderfist","Boycott","Brawn","Bullet","Buster","Canine","Carnage","Ceasar","Chaos","Classified","Clobber","Crazy Eyes","Cyclone","Daemon","Deluge","Diablo","Diesel","Digger","Domino","Drake","Dread","Dynamite","Earthquake","Extinction","Fatal Fury","Fear","Gargoyle","Genie","Ghost","Ghost Kicker","Grand Master","Grimace","Grimes","Guts","Havoc","Hazard","Heckler","Hellfire","Hellhound","Hercules","Hunter","Ironman","Jekyll","Jericho","Jester","Jitters","Karma","King","Knock Out","Kong","Macho Monster","Magician","Mayhem","Mercury","Mirage","Morpheus","Mr. Indestructible","Mutiny","Nightmare","Onyx","Paragon","Payne","Pegasus","Perfection","Pincher","Pitbull","Predator","Price","Prince","Puppeteer","Quicksilver","Raptor","Ravager","Raze","Razor","Retribution","Rhino","Riot","Rocket","Rogue","Rowdy","Sandman","Scarface","Sergeant","Slayer","Smash","Smiley","Smite","Snake","Sphinx","Striker","Suave","Swagger","Swine","Taboo","Tank","The Ambassador","The Anaconda","The Archetype","The Badger","The Barbarian","The Bodyguard","The Boulder","The Brute","The Bull","The Bulldozer","The Butcher","The Cataclysm","The Clam","The Clown","The Creature","The Crippler","The Crow","The Demolisher","The Destroyer","The Devourer","The Duke","The Edge","The Fiend","The Flash","The Flea","The Fluke","The Gambler","The Goon","The Gorilla","The Governor","The Guns","The Hallowed","The Hippo","The Hood","The Hound","The Hurricane","The Hyena","The Immortal","The Innovator","The Jackal","The King","The Legend","The Maestro","The Man","The Marauder","The Martyr","The Messenger","The Mongrel","The Mountain","The Oak","The Ogre","The Punisher","The Punk","The Pursuer","The Quake","The Savage","The Scout","The Sorceror","The Stalker","The Storm","The Strangler","The Surgeon","The Terror","The Thunder","The Tormentor","The Torrent","The Typhoon","The Unforgiving","The Viper","The Void","The Volcano","The Wrath","Thruster","Thump","Thunderbolt","Thundercrack","Tremor","Twister","Undertaker","Ursus","Whiz","Wicked","Wolf","Wrath-hog"];
var namesFemale = ["Anemone","Angel","Aries","Aura","Black Widow","Blitz","Blue Rose","Camille","Caramel","Celeste","Chance","Charity","Coral","Curtains","Desire","Destiny","Diamond","Divine","Drama","Elastic","Electric","Enigma","Essence","Eternity","Feline","Fortuna","Fortune","Gale","Gem","Gemini","Ginger","Gloria","Harpy","Hope","Iconiq","Ivory","Ivy","Jade","Jasmine","Jewel","Karma","Katana","Kayo","Key","Knock Out","Libra","Lights","Lioness","Luna","Maneater","Mantis","Mantra","Melody","Miss Fortune","Missy","Mistral","Moxie","Mystique","Nourisha","Obsession","Onyxia","Onyxis","Phobia","Promise","Raven","Remedy","Rogue","Rose","Ruby","Saffron","Sanguine","Sapphire","Scarlet","Serenity","Succubus","Tazz","Tempest","The Amazon","The Cat","The Oracle","The Smile","The Witch","Tigress","Twinkle","Vanity","Velvet","Venus","Violette","Virus","Wildflower","Willow"];
var br = "";

function nameGen(nameFirst){
	names1 = nameFirst;
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