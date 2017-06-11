var nm1 = ["Adventure","Aeon","Affinity","Alchemy","Alliance","Alloy","Ambience","Amigo","Anomaly","Apex","Aptitude","Arcane","Arch","Architect","Artisan","Aspect","Atom","Aura","Aurora","Banshee","Beacon","Beast","Behemoth","Bionics","Bonfire","Buddy","Builder","Bullet","Canvas","Capture","Champion","Chaos","Chief","Chivalry","Cinder","Clairvoyant","Climax","Clone","Companion","Composer","Construction","Core","Courage","Creative","Creature","Crescent","Crow","Crux","Crystal","Curio","Cyborg","Daemon","Dawn","Daydream","Deity","Destiny","Device","Diamond","Divine","Domain","Dominion","Dream","Dungeon","Dwarf","Dynamo","Ebony","Ecstasy","Effigy","Ego","Elysium","Ember","Emblem","Empire","Enigma","Enterprise","Eos","Epitome","Epoch","Era","Essence","Eternity","Executive","Fable","Fairy","Fantasy","Farseer","Fay","Ferocity","Figment","Firework","Flair","Flare","Flexile","Flow","Fluid","Flux","Forged","Forger","Formula","Fortune","Frame","Framework","Fury","Fusion","Galaxy","Gargoyle","Generation","Genesis","Genie","Genius","Globe","Gold","Gorgon","Hallow","Harmony","Havoc","Hazard","Heirloom","Heist","Hex","Hieroglyph","Hymn","Hysteria","Identity","Idol","Illusion","Imagination","Imagine","Immortal","Inception","Infinity","Innovation","Insight","Inspire","Invention","Ivory","Jaeger","Javelin","Journey","Joy","Karma","Kindred","Kinetics","Kobold","Legacy","Legend","Legion","Leviathan","Liberty","Lich","Lighthouse","Locomotion","Lore","Lucid","Luminous","Magma","Mania","Maniac","Martial","Mason","Mayhem","Medusa","Memento","Mercenary","Merry","Mobius","Muse","Myriad","Mystery","Mystic","Myth","Nebula","Nephilim","Nimble","Nimbus","Oasis","Obelisk","Obsidian","Odyssey","Omega","Oracle","Origin","Parable","Paradox","Paragon","Particle","Pegasus","Peril","Phantom","Phoenix","Physique","Pinnacle","Pixel","Pixie","Platinum","Playful","Primal","Prime","Prodigy","Prophecy","Prospect","Prosperity","Protocol","Psyche","Psychic","Pursuit","Quest","Queue","Quickfire","Rage","Rainbow","Rapture","Raze","Rebel","Relic","Renaissance","Revolution","Ritual","Root","Rune","Saga","Sanctuary","Sanctum","Savage","Scope","Scythe","Searchlight","Serenity","Shade","Shadow","Shapeshifter","Shrine","Sidekick","Siege","Silence","Singularity","Siren","Sonic","Source","Sparkle","Specter","Sphinx","Spiral","Spirit","Sprite","Stage","Steel","Storm","Supremacy","Synthesis","Temper","Tempest","Terminus","Terra","Thauma","Tranquillity","Transcendence","Turbulence","Twist","Unity","Universe","Valiance","Vault","Venture","Vertex","Vigor","Virtuality","Virtue","Virtuoso","Vision","Void","Vortex","Voyage","Whiz","World","Zenith","Zion","Zodiac"];
var nm2 = ["Creative Engine","Creator","Engine","Frameworks","Game Engine","Physics Engine","Studio","Tools","Toolset","Engine","Engine"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + " " + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}