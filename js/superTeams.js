function nameGen(){
	var nm1 = ["Aberration","Alpha","Amendment","Angel","Anomaly","Apex","Arachnid","Arcane","Assault","Augmented","Aura","Aurora","Banshee","Barrage","Behemoth","Blitz","Blood","Cardinal","Carnage","Castaway","Challenger","Chaperon","Chief","Cobra","Cosmos","Covert","Crimson","Crisis","Crux","Curator","Custodian","Daemon","Defiance","Demon","Destiny","Devil","Divine","Eerie","Enigma","Epitome","Eternity","Ethereal","Exile","Extreme","Feral","Figment","Flux","Freak","Fugitive","Future","Galaxy","Global","Golden","Grim","Guardian","Hazard","Illusion","Impact","Infernal","Inferno","Infinity","Inhuman","Insurgence","Invasion","Ironclad","Jackal","Justice","Juvenile","Light","Maestro","Maraud","Maroon","Memento","Miracle","Mirage","Monster","Mutant","Myriad","Mystery","Mythic","Nebula","Nemesis","New","New Law","New Vision","Nightmare","Nova","Omega","Oracle","Parable","Paradox","Paragon","Paramount","Phantom","Phenomenon","Phoenix","Pinnacle","Power","Primal","Prime","Prodigy","Prototype","Quantum","Rascal","Reformation","Remedy","Revelation","Revenent","Riot","Rogue","Ruthless","Sanction","Sanguine","Savage","Sentence","Sentinel","Seraph","Shadow","Shepherd","Silent","Silver","Singular","Singularity","Skirmish","Sovereign","Spectral","Storm","Super","Supreme","Terra","Thunder","Time","Transcendent","Triad","Trinity","Universe","Vagrant","Vertex","Vigilante","Viper","Visionary","Vitality","Void","Watchdog","Whisper","Wonder","Zealot"];
	var nm2 = ["Alliance","Allies","Battalion","Brawlers","Centurions","Champions","Clan","Crew","Crusaders","Custodians","Defenders","Fighters","Flight","Force","Guardians","Guards","Heroes","Knights","League","Legion","Marvels","Masters","Oracles","Outcasts","Pack","Patrol","Rangers","Rebels","Sentinels","Soldiers","Squad","Squadron","Syndicate","Titans","Troopers","Unit","Warriors","Watch","Wings"];
	var nm3 = ["Aberrations","Allies","Ancestors","Angels","Animals","Anomalies","Arachnids","Archetypes","Auras","Banshees","Battalion","Behemoths","Berserkers","Bionics","Brawlers","Cardinals","Castaways","Centurions","Champions","Chosen","Cobras","Colossals","Coverts","Crackerjacks","Crazed","Crusaders","Curators","Cursed","Custodians","Daemons","Defenders","Demons","Deranged","Designs","Deviations","Devils","Divine","Divines","Elite","Enigmas","Epitomes","Eternals","Ethereals","Exclusives","Exiles","Fanatics","Ferals","Fiends","Figments","Flight","Freaks","Freaks of Nature","Fruitcakes","Fugitives","Gimmicks","Gizos","Golems","Goliaths","Guardians","Heralds","Hounds","Hunters","Illusionists","Illusions","Immortals","Imps","Infernals","Infinities","Inventions","Ironclad","Jackals","Juveniles","Keepers","Legion","Lunatics","Mad Dogs","Maestros","Malevolents","Maniacs","Marauders","Maroons","Marvels","Masters","Miracles","Mirages","Miscreants","Monsters","Myriad","Nebulas","Nemeses","Nightmares","Novae","Novas","Omegas","Omens","Oracles","Originals","Outcasts","Parable","Paradoxes","Paragons","Paramounts","Phoenixes","Pioneers","Predator","Primals","Primitives","Primordials","Pristines","Prophecies","Prototypes","Quirks","Rangers","Raptors","Rascals","Renegades","Sanguines","Savages","Selected","Sentinels","Seraphs","Silent Ones","Singularities","Spectrals","Superiors","Thunders","Titans","Tricksters","Trinities","Undying","Untamed","Vagabonds","Vagrants","Vigilantes","Vindicators","Vipers","Visionaries","Watchdogs","Whispers","Wildlings","Wings","Wonders","Wretched"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * nm3.length);
			names = "The " + nm3[rnd];
			nm3.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = "The " + nm1[rnd] + " " + nm2[rnd2];
			nm1.splice(rnd, 1);
			nm2.splice(rnd2, 1);
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