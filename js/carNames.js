var nm1 = ["Blast","Hollo","Wolf","Fang","Eagle","Blade","Adventure","Aeon","Alabaster","Albatross","Apex","Astral","Augury","Aura","Aurora","Avalanche","Baron","Barrage","Basilisk","Behemoth","Blaze","Blend","Bliss","Blitz","Blizzard","Bolt","Buffalo","Bullet","Capital","Catalyst","Celestial","Centaur","Centurion","Charm","Chase","Climax","Cobra","Conqueror","Corsair","Cosmos","Crest","Crown","Crusader","Crux","Curiosity","Dawn","Daydream","Deputy","Desire","Dominion","Dragon","Dusk","Dynamics","Dynamo","Elysium","Eminance","Empire","Empyrean","Encounter","Enigma","Eon","Eos","Epiphany","Epitome","Escape","Essence","Eternity","Ethereal","Evolution","Excursion","Expedition","Falcon","Ferocity","Fire","Flow","Flux","Formula","Fragment","Freedom","Gallop","Grit","Guardian","Guerilla","Harmony","Heirloom","Hero","Hydra","Icon","Inception","Inferno","Inquiry","Instinct","Intro","Ivory","Jazz","Legacy","Legend","Liberty","Lightning","Lioness","Magic","Majesty","Mammoth","Marvel","Mastery","Meridian","Method","Might","Millenium","Mirage","Momentum","Moonlight","Morale","Motion","Motive","Mystery","Mythic","Nebula","Nimbus","Obsidian","Olympian","Onyx","Oracle","Orbit","Origin","Paladin","Paradox","Paragon","Parallel","Passion","Patron","Phantom","Phenomenom","Pinnacle","Portrait","Presence","Prestige","Prime","Prodigy","Prophecy","Prospect","Pulse","Purity","Pyre","Quest","Quicksilver","Radiance","Ranger","Raven","Reach","Realm","Reflect","Renegade","Resolve","Revelation","Roamer","Rune","Sanctuary","Scorpion","Scout","Serpent","Shadow","Silver","Sliver","Specter","Spire","Spirit","Spotlight","Sprite","Stardust","Starlight","Storm","Striker","Supremacy","Surge","Symbol","Tarragon","Temper","Temperament","Tempest","Thriller","Thunder","Tigress","Titan","Tracer","Tradition","Trailblazer","Treasure","Triumph","Twister","Umbra","Union","Universe","Utopia","Vagabond","Vanish","Vertex","Vigor","Vindicator","Viper","Virtue","Vision","Vortex","Voyage","Vulture","Warrior","Whim","Whirlpool","Wish","Zeal"];
function nameGen(){
	var br = "";
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