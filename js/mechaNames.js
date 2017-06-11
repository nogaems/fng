var nm2 = ["Angel","Armor","Armor Suit","Battler","Buster","Colossus","Combatant","Command Suit","Command Unit","Decimator","Leviathan","Dreadnought","Drone","Engine","Fighter","Fortress","Gear","Guardian","Gun System","Jaeger","Juggernaut","Machine","Master","Master Suit","Mech","Panzer","Runner","Scouter","Sentinel","Stalker","Strider","Suit","Transport","Trooper","Unit","Valkyrie","Walker","Warmech"];

function nameGen(type){
	var nm1 = ["Action","Advanced","Aerial","All Terrain","Amplified","Anarchy","Apex","Aquatic","Arachnid","Arctic","Armageddon","Armed","Armored","Artillery","Assault","Assembly","Augmented","Avatar","Avian","Ballistic","Barrage","Battle","Battleground","Beast","Bio","Bio-Armored","Bionic","Blitz","Broad","Buccaneer","Cardinal","Cataclysm","Cavalry","Central Command","Champion","Chaos","Charge","Chrome","Chrono","Cloud","Cobra","Combat","Compact","Core","Cosmic","Covert","Cruel","Crusader","Cryo","Cyclone","Daemon","Dark","Death","Defensive","Deployment","Destruction","Dimensional","Divine","Domination","Doom","Dragon","Dragoon","Dread","Drill","Dynamic","Elemental","Elite","First Assault","Flock","Flood","Frenzy","Front Line","Fury","Galactic","God","Goddess","Golem","Goliath","Grand","Grave","Great","Grim","Hallowed","Havoc","Hazard","Heavy","Hercules","Hero","High Agility","High Terrain","Horde","Hulking","Hurricane","Hysteria","Immortal","Imperial","Infernal","Infinity","Intervention","Intrusion","Invasion","Iron","Judgment","Jumbo","Jungle","Legion","Light","Mammoth","Maneuver","Martial","Master","Mayhem","Mega","Metal","Miracle","Mist","Mobile","Multi","Myriad","Naval","Nexus","Night","Nuclear","Offensive","Ominous","Orbital","Panzer","Paragon","Peril","Phantom","Phoenix","Pioneer","Plane","Planet","Portable","Power","Powered","Preparation","Primary","Prime","Proto","Psychic","Psycho","Pygmy","Pyro","Raid","Ravage","Regal","Rescue","Revered","Roaming","Robust","Round","Royal","Salvage","Savage","Science","Scorpion","Service","Shade","Shadow","Shock","Silent","Silver","Sinister","Skirmish","Solid","Sonic","Spider","Spirit","Stalker","Storm","Storming","Strategic","Strike","Swarm","Tactical","Tactical Raid","Tactile","Tempest","Thunder","Titan","Titanic","Transforming","Trauma","Typhoon","Unarmed","Urban","Vanguard","Variable","Versatile","Viking","Vile","Viper","Vital","Vitality","Void","Wandering","War","Warfare","Wicked","Wolverine","Wrath"];
	var nm3 = ["Achilles","Actium","Agememnon","Albatross","Anarchy","Andromeda","Antioch","Apollo","Aquila","Archangel","Archmage","Argo","Aries","Arizone","Armada","Armageddon","Artemis","Arthas","Athens","Atlas","Aura","Aurora","Avalanche","Avalaon","Babylon","Badger","Bandit","Basilisk","Bastion","Bear","Behemoth","Berserker","Big Boy","Big Daddy","Big Girl","Big Momma","Black Widow","Blade","Blitz","Blossom","Boa","Boar","Buccaneer","Buzzard","Caelestis","Calamity","Calypso","Carnage","Carthage","Centipede","Centurion","Challenger","Chimera","Chronos","Claymore","Cobra","Colossus","Comet","Condor","Conquistador","Corsair","Covenant","Coyote","Crow","Curator","Cyclops","Dagger","Death","Destiny","Diplomat","Discovery","Divine Intervention","Dragon","Dreadnought","Elysium","Emperor","Empress","Endeavor","Enigma","Eternity","Euphoria","Exarch","Executioner","Fade","Faith","Falcon","Fate","Fortuna","Freedom","Frontier","Galactica","Gauntlet","Genesis","Gladiator","Glory","Goblin","Golem","Gremlin","Grim","Grim Reaper","Grim Reaver","Guardian","Halo","Hammer","Hammerhead","Hannibal","Harlequin","Harmony","Harpy","Hawk","Hercules","Hog","Hummingbird","Hunter","Huntress","Hurricane","Icarus","Impulse","Independence","Inferno","Infinity","Innuendo","Invictus","Invincible","Jaeger","Javelin","Judgment","Juggernaut","Karma","Khan","Kingfisher","Kraken","Legacy","Legionnaire","Leviathan","Liberty","Loki","Lupus","Lust","Mace","Manticore","Matador","Minotaur","Myrmidon","Nebechadnezzar","Nemesis","Nemo","Neptune","Nero","Nexus","Nightingale","Nightmare","Nirvana","Nomad","Nostradamus","Nova","Oberon","Oblivion","Oracle","Orion","Pandora","Pathfinder","Patience","Peacock","Pegasus","Pelican","Phantom","Phoenix","Pilgrim","Polaris","Poseidon","Prometheus","Promise","Proximo","Rascal","Ravager","Raven","Reaper","Reaver","Retribution","Revenant","Rhino","Ripper","Saber","Sage","Samurai","Scavenger","Scimitar","Scorpio","Scythe","Serenity","Shade","Siren","Slayer","Sparrow","Spartacus","Spectator","Storm","Super Nova","Templar","Termite","Thanos","Thor","Thunder","Thunderbolt","Thunderstorm","Tomahawk","Torment","Tortoise","Tranquility","Trident","Triumph","Unicorn","Unity","Vagabond","Valhalla","Valiant","Valkyrie","Vanguard","Vengeance","Vice","Viper","Voyager","Vulture","Warlock","Warrior","Watcher","Widow Maker","Wisdom","Wolf","Wolverine","Woodpecker","Wrath","Wyvern","Zephyr","Zero","Zeus","Zion"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm2.length);
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd] + " " + nm2[rnd2];
			nm1.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			names = nm3[rnd];
			nm3.splice(rnd, 1);
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