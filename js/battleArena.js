var nm1 = ["Aberration","Abyss","Acid","Afterlife","Amnesia","Anarchy","Angel of death","Annihilation","Anthrax","Archdemon","Armada","Armageddon","Armagedome","Ash and Dust","Assassination","Ataxia","Autopsy","Babylon","Battleborn","Behemoth","Berzerker","Birdfeed","Black Angel","Black Bird","Black Blade","Black Rainbow","Blackheart","Blacksoul","Blacksun","Blade Fury","Bladefist","Blitz","Blood and Gore","Bloodbath","Bloodblitz","Bloodlake","Bloodlust","Bloodstain","Broken Hell","Bullettooth","Burning Wing","Cadaver","Cannibal","Carcass","Carnage","Carnival","Cataclysm","Cemetery","Chaos","Claymore","Crimson","Daggertip","Dark Ages","Dead Horse","Death's","Deathbound","Delirium","Demigod","Demise","Demondome","Desecration","Diablo","Dismember","Dominion","Doomhammer","Double Trouble","Dragontooth","Dread","Dynomite","Eclipse","Elysium","Eradication","Eternity","Euthanasia","Exodus","Exposition","Extinction","Extravaganza","Fallen Saint","Fatality","Fear Factory","Femme Fatale","Fireworks","Forsaken","Four Hoursemen","Fracas","Freakville","Free For All","Freefall","Frenzy","Funeral","Fury","Garotte","Gladiator","Gore","Gorefest","Grim","Grim Reaper","Haemorrhage","Hallowed","Havoc","Hazard","Hell Incarnate","Hell's Gate","Hellbound","Hellion","Hellraised","Hellraiser","Heresy","Hibernation","Hollow","Holy Grail","Horror","Hurricane","Hysteria","Icarus","Immolation","Inferno","Infinity","Insomnia","Iron Maiden","Ironbound","Ironwing","Judgment","Jungle","Karma","King Cobra","Kriskras","Labyrinth","Lawbreaker","Limbo","Lost Soul","Lunacy","Macabre","Madness","Malevolence","Maneater","Mania","Manslayer","Martyr","Massacre","Mayhem","Menimals","Misery","Mistress of Pain","Molotov","Napalm","Necro","Necrodome","Necrosis","Nefarious","Nephilim","Nemo","Nero","Nether","Netherdome","Netherworld","Nightfall","Nirvana","Noxidome","Noxious","Obituary","Obliteration","Oblivion","Overkill","Painkiller","Paradise","Paradox","Paranoia","Phantom","Phenomenon","Phobia","Psycho","Puppetmaster","Reaper","Red Lamb","Revolution","Riot","Sabertooth","Salvation","Sanctuary","Sandman","Sandstorm","Sanguine","Scimitar","Scourge","Scythe","Search and Destoy","Septic","Shadow","Shadowfall","Sharktank","Sinister","Skeleton","Slaughter and Laughter","Slice and Dice","Solstice","Spectacle","Starfall","Stormfury","Suffocation","Suicide","Sundown","Surgery","Switchblade","Symphony","Symptomium","Termination","Terminus","Terror","Terrordome","Thorne","Thunder","Tyranny","Titan","Torture Squad","Tragedy","Tranquility","Transcendence","Twilight","Underdome","Underworld","Vermin","Void","Warpath","White Witch","Wrath","Xenomorph","Zero"];
var nm2 = ["Arena","Stadium","Coliseum","Amphitheater","Arena"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = "The " + nm1[rnd] + " " + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}