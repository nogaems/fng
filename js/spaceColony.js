var nm1 = ["Aegis","Aeon","Aeris","Babylon","Aeternitas","Aether","Alliance","Alpha","Amazone","Ancestor","Anemone","Angel","Anomaly","Apollo","Arcadia","Arcadis","Arch","Architect","Ark","Artemis","Asphodel","Asteria","Astraeus","Athena","Atlas","Atmos","Aura","Aurora","Awe","Azura","Azure","Baldur","Beacon","Blue Moon","Borealis","Burrow","Caelestis","Canaan","Century","Chrono","Chronos","Crescent","Curator","Curiosity","Data","Dawn","Daydream","Demeter","Dogma","Dream","Dune","Ecstacys","Eir","Elyse","Elysium","Empyrea","Ender","Enigma","Eos","Epiphany","Epitome","Erebus","Escort","Eternis","Eternity","Exposure","Fable","Father","Fauna","Felicity","Flora","Fortuna","Frontier","Gaia","Galaxy","Genesis","Genius","Glory","Guardian","Halo","Heirloom","Helios","Hemera","Hera","Heritage","Hermes","Horus","Hymn","Hyperion","Hypnos","Ignis","Illume","Inception","Infinity","Isis","Janus","Juno","Legacy","Liberty","Lore","Lucent","Lumina","Luminous","Luna","Lunis","Magni","Mammoth","Mani","Marvel","Memento","Minerva","Miracle","Mother","Muse","Mystery","Mythos","Nebula","Nemesis","Nemo","Neo","Nero","Nimbus","Nott","Nova","Novis","Nox","Nyx","Odyssey","Olympus","Omega","Oracle","Orbital","Origin","Orphan","Osiris","Outlander","Parable","Paradox","Paragon","Pedigree","Phantasm","Phantom","Phenomenon","Phoenix","Pilgrim","Pioneer","Prism","Prodigy","Prometheus","Prophecy","Proto","Radiance","Rebus","Relic","Revelation","Reverie","Rogue","Rune","Saga","Sancus","Scout","Selene","Serenity","Settler","Shangris","Shepherd","Shu","Sol","Solas","Spectacle","Specter","Spectrum","Spire","Symbolica","Tartarus","Terminus","Terra","Terran","Terraria","Themis","Tiberius","Titan","Titanus","Torus","Tranquility","Trivia","Utopis","Valhalla","Vanguard","Vanquish","Vesta","Vestige","Victoria","Virtue","Visage","Voyage","Vulcan","Warden","Yggdrasil","Zeus","Zion"];
var nm2 = ["","Colony","Station","Colony","Station","Base","Terminal",""];
var br = "";

function nameGen(type){
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