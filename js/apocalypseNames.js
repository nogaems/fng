var nm1 = ["Armageddon","Bane of Mankind","The Catastrophic Experiment","The Cleansing Rains","Corruption of Mankind","Dawn of Destruction","Dawn of the Others","Dawn of the Walkers","Day of the Dead","Death of the Moon","Death of the Sun","Decimation of Mankind","Dusk of Mankind","End of the Living","Eternal Darkness","Fatal Impact","Final Hour","Final Impact","Frozen Hell","Garbage Day","Global Freezing","Global Warming","Judgement Day","Last Steps","Man's Greed","Mankind's Arrogance","Mankind's Betrayal","Mankind's Disgrace","Mankind's Expiration","Mankind's Ignorance","Nature's Vengeance","Our Expiration Date","Our Mutual Destruction","Our Wrong Choice","Rains of Death","Self-Assisted Damnation","Technological Destruction","Technological Expiration","Terminal Velocity","Terminus","The Annihilation","The Backfire","The Beginning","The Burning Rain","The Burning Skies","The Burning Winds","The Cataclysm","The Cleansing","The Collapse","The Collapse of Mankind","The Collision","The Combustion","The Conclusion","The Decimation","The Decimation of Mankind","The Departure","The Desolation of Mankind","The Detonation","The Disaster","The Drought","The Dry Rains","The End of Resources","The Erupting Earth","The Eternal Day","The Eternal Night","The Eternal Rains","The Eternal Storm","The Experiment","The Final Encounter","The First Encounter","The Flood","The Food Chain Collapse","The Immolation","The Invasion","The Killing Days","The Manifestation","The Meteor","The Nuclear Event","The Ozone Event","The Permafrost","The Phenomenon","The Purge","The Purification","The Putrefaction","The Rapture","The Revelation","The Rupture","The Sacrifice","The Severance","The Showdown","The Sterilization","The Sundering","The Tipping Point","The Visitors","The Wipe Out","Total Annihilation","Toxic Rain","Winds of Death","World War Final","Our Execution","Nature's Judgement","The Omega Event","The Cosmic Annihilation"];
	
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