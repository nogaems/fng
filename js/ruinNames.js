var nm1 = ["Borough","City","Cove","Farms","Fields","Forest","Harbor","Island","Isle","Labyrinth","Lands","Mountain","Outpost","Reef","River","Shore","Temple","Town","Vault","Village"];
var nm2 = ["Ash","Ashes","Blight","Bones","Chaos","Charcoal","Coal","Collapse","Corrosion","Cracks","Crimson","Crumbles","Darkness","Death","Debris","Decay","Desertion","Desolation","Despair","Dishonor","Doom","Dread","Dreams","Destruction","Dusk","Emptiness","Ends","Exiles","Extinction","Fire","Fog","Fragments","Ghosts","Gloom","Graves","Hauntings","Ice","Illusions","Isolation","Mist","Mold","Molten Rock","Myths","Necrosis","Nightfall","Nightmares","Oblivion","Obsidian","Onyx","Phantoms","Pieces","Plants","Remains","Remnants","Residue","Rot","Rubble","Ruination","Ruins","Rust","Screams","Shadows","Shambles","Shrubs","Silence","Silver","Skeletons","Skulls","Slate","Sleep","Smoke","Solitude","Soot","Spirits","Stone","Twilight","Undoing","Vibrations","Waste","Water","Whispers","Wind","Wreckages","the Abandoned","the Abyss","the Broken","the Curse","the Damned","the Fallen","the Forgotten","the Forsaken","the Infernal","the Inferno","the Lost","the Night","the Perished","the Scourge","the Unknown","the Vanquished","the Void"];
var nm3 = ["Abandoned","Abyss","Agony","Ashen","Bare","Barren","Bleak","Blight","Bone","Broken","Burning","Chaos","Charcoal","Coal","Cobalt","Collapsed","Corroded","Cracking","Crimson","Crumbled","Crumbling","Cursed","Damned","Dark","Dcayed","Dead","Debris","Decaying","Deserted","Desolated","Desolation","Despair","Destroyed","Destruction","Dismissed","Doom","Dread","Emptied","Empty","End","Ender","Erased","Ethereal","Exile","Exiled","Extinct","Fallen","Fire","Foggy","Forgotten","Forsaken","Fragmented","Frozen","Ghost","Gloom","Grave","Haunted","Ice","Illusion","Infernal","Inferno","Isolated","Isolation","Lifeless","Lonely","Lost","Mist","Molded","Molten","Motionless","Murky","Mythic","Nameless","Necrotic","Neglected","Night","Nightmare","Nullified","Obliterated","Oblivion","Obsidian","Onyx","Overgrown","Perished","Petrified","Phantom","Remnant","Residue","Rotting","Rubble","Ruin","Ruined","Rusted","Savage","Scorching","Scourge","Scream","Screaming","Shadow","Shamble","Shrub","Silent","Silver","Skeleton","Skull","Slate","Sleeping","Sleepy","Smoke","Solitude","Soot","Spirit","Stone","Twilight","Uncanny","Undone","Unknown","Vanquished","Vibrating","Void","Waste","Wasted","Weeping","Whisper","Whispering","Windy","Wreckage"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + " of " + nm2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm1.length);
			names = "The " + nm3[rnd] + " " + nm1[rnd2];
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