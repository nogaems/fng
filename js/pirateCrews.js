var names1 = ["Albatross","Berserker","Black Bandana","Black Crow","Black Parrot","Black Rose","Black Skull","Black Snake","Black Tooth","Black Tooth Grin","Blackbeard","Bloodsail","Blue Whale","Bone Dry","Brass Knuckle","Broken Heart","Bullseye","Catamaran","Chaos","Crazy Eyed","Crossbone","Cutlass","Cyclone","Daydream","Dead","Defiant","Dread","Drifting","Driftwood","East Sea","Filibuster","Filthy Frigate","Forsaken","Full Sail","Giant Turtle","Golden Grin","Golden Tooth","Goldtooth","Hydra","Jolly","Keel Haul","Kraken","Land Shark","Lost","Lost Rum","Mad Man","Maelstrom","Maroon","Masked","Mermaid","Merpeople","Mirage","Neptune","Nightmare","North Sea","Octo","Octopus","One Eyed","One Legged","Painted","Pegleg","Phantom","Poseidon","Rat Grin","Rattail","Red Bandana","Red Hair","Red Rose","Rickety","River","Rusty","Sanguine","Scarlet","Sea Lurker","Sea Serpent","Sea Siren","Seagull","Seashell","Serpent","Seven Sails","Seven Seas","Shadow","Sharkfin","Sharktooth","Silent Whisper","Silver Crow","Smiling","South Sea","Specter","Talking Parrot","Tankard","Tooth Grin","Undead","Vortex","West Sea","Whirlpool","White Shark","Whitebeard","Black Squid","White Squid","Silver Hydra","Laviathan","Silver Wave","Golden Cannon","Silver Cannon","Hollow","Gilded"];
var names2 = ["Pirates","Raiders","Buccaneers","Corsairs","Rovers","Pillagers","Plunderers","Pirates","Bandits","Buccaneers"];
var names3 = ["Black Diamond","Black Fog","Black Hydra","Black Lagoon","Black Sea","Black Skull","Black Squid","Black Turtle","Bloodied Flag","Blue Lagoon","Blue Moon","Blue Whale","Broken Harbor","Broken Islands","Coin","Crossbones","Curse","Cursed Doubloon","Dark Waters","Dead Sea","Depths","East","East Coast","Eternal Raid","Flintlock","Fog","Forsaken Captain","Frozen North","Frozen Ocean","Frozen Sea","Gilded Cannon","Golden Banner","Golden Cannonball","Golden Cutlass","Golden Mermaid","Great Lake","Hidden Cove","Hidden Monster","High Seas","Hollow","Horizon","Infernal Depths","Inner Sea","Leviathan","Lost Kraken","Lost Mermaid","Lost Ocean","Lost Shores","Lost Treasure","Lurker in the Depths","Maelstrom","Monster Shark","Nether","New Horizon","New World","North","North Sea","Open Seas","Plague","Plank","Promised Lands","Promised Treasure","Rum","Sanguine Flag","Scarlet Flag","Sea Serpent","Sea Wolf","Seven Sails","Seven Seas","Seven Shores","Shade","Shallows","Shores","Silent Bay","Silent Sea","Silver Cannon","Silver Cove","Silver Eye","Silver Moon","Silver Serpent","Silver Sword","Silver Wave","Siren's Call","Siren's Song","South","South Sea","Squid","Sword","Tempest","Thunder","Thunderstorm","Tide","Void","Vortex","West","West Coast","Wicked Seas","Unleashed Kraken","Eternal Curse","Stolen Years"];
var names4 = ["Barnicles","Black Bandana Buccaneers","Black Bandanas","Black Sails","Black Skulls","Black Tooth Grins","Blackbeards","Bloody Bandits","Broken Bandits","Broken bones","Cannon Balls","Cannonball Bandits","Crazy Eyes","Cutlasses","Dividers","Drifters","Driftwood Divers","Eternal Smiles","Filibusters","Fishguts","Flintlocks","Floaters","Golden Guns","Grand Cannoneers","High 'n Dry","Hired Guns","Hired Swords","Hydras","Keel Haulers","Landlocked","Lost Souls","Mad Marauders","Nautical Navigators","Ocean Shadows","Ocean Wanderers","Odd Jobs","Peg Legs","Peglegs","Pelicans","Pieces of Eight","Plagued Pillagers","Plank Walkers","Plunderers and Pillagers","Rattails","Red Raiders","Red Sails","Red Scarfs","Rusty Rustlers","Salty Dogs","Salty Swabbers","Sea Angels","Sea Devils","Sea Dogs","Sea Foxes","Sea Monsters","Sea Sharks","Sea Terrors","Sea Wolves","Seagulls","Shellbacks","Silver Eyes","Silver Sailors","Silver Swords","Siren's Song","Sirens","Skull and Crossbones","Sons of the Sea","South Sea Sailors","Squids","Stray Dogs","Talking Parrots","Thirsty Thieves","Thunder Waves","Water Walkers","Wild Windjammers"];
var br = "";
function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 4){
			rnd = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names2.length);
			names = "The " + names1[rnd] + " " + names2[rnd2];
		}else if(i < 7){
			rnd = Math.floor(Math.random() * names2.length);
			rnd2 = Math.floor(Math.random() * names3.length);
			names = "The " + names2[rnd] + " of the " + names3[rnd2];
		}else{
			rnd = Math.floor(Math.random() * names4.length);
			names = "The " + names4[rnd];
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