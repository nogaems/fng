var nm3 = ["-","-","-","-","-","-","-","-","-","-","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"];
var nm4 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z"];
var nm5 = ["1","2","3","4","5","6","7","8","9","0"];
var nm6 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"];

function nameGen(type){
	var nm1 = ["Aegis","Amazon","Arachnid","Arbiter","Armadillo","Atilla","Augury","Aurora","Badger","Bane","Bargaining Chip","Barrage","Basilisk","Bayonet","Beast","Behemoth","Bigwig","Bison","Black Knight","Blitz","Blizzard","Boar","Bolide","Bolt","Bouncer","Bronco","Buffalo","Buffer","Bulldozer","Bulwark","Buttress","Canine","Cavalier","Centurion","Cerberus","Challenger","Chaperon","Chelonian","Chief","Chieftain","Citadel","Cobra","Colossus","Colt","Comet","Commander","Commando","Cooter","Covenant","Coyote","Croc","Cruiser","Cthulu","Curator","Custodian","Cyclone","Cyclops","Czar","Dawn","Deputy","Devil","Diablo","Dire","Dire Wolf","Dirge","Djinn","Doom","Dragon","Drake","Dread","Duster","Edge","Elephant","Emperor","Enigma","Feline","Fiend","Fortress","Fox","Furor","Fury","Gargantua","Gargoyle","Gauntlet","Genesis","Genghis","Gloom","Glutton","Goliath","Gopher","Governor","Grimace","Grizzly","Guardian","Guerilla","Hades","Harmattan","Harvester","Hedgehog","Heimlich","Hellhound","Hellion","Herald","Hercules","Honcho","Honey Badger","Horror","Horus","Hun","Hurricane","Hydra","Hyena","Hymn","Ibis","Imp","Inferno","Jackal","Jaguar","Judge","Judgement","Kaiser","Khamsin","Khan","King Crab","Knave","Knight","Lament","Leatherback","Leonidas","Leopard","Leviathan","Lightning Bolt","Lucifer","Magister","Maharajah","Mammoth","Marshal","Mastodon","Matador","Maverick","Meteor","Minion","Mogul","Mollusk","Monarch","Mongrel","Mug","Mule","Mutt","Ogre","Oracle","Outcast","Overlord","Overseer","Paladin","Pangolin","Panther","Paradox","Paragon","Parapet","Patron","Porcupine","Prime","Primus","Pulse","Purgatory","Rajah","Rampart","Rascal","Rattlesnake","Requiem","Rex","Rhino","Rogue","Ruffian","Samaritan","Samson","Samurai","Savage","Scalawag","Scallion","Scimitar","Scorpion","Scoundrel","Scourge","Scythe","Sentinel","Serpent","Shaitan","Shepherd","Sherpa","Shooting Star","Sickle","Siren","Sirocco","Skunk","Smirk","Snapper","Spartan","Sphinx","Spitfire","Stallion","Stark","Steward","Storm","Striker","Sultan","Swine","Tarantula","Tarragon","Tempest","Templar","Terror","Thor","Thunder","Tigress","Titan","Torment","Tormentor","Tornado","Tortoise","Trooper","Tusker","Tycoon","Typhoon","Tyrant","Valkyrie","Vallation","Varlet","Viking","Viper","Virago","Visage","Vixen","Vulture","Warden","White Knight","Wolfhound","Wyvern"];
	var nm2 = ["Amphibious Vehicle","Anti-Tank Vehicle","Armored Car","Armored Personal Carrier","Armored Security Vehicle","Armored Utility Vehicle","Armored Vehicle","Artillery Command Vehicle","Artillery Tractor","Bridging Vehicle","Cargo Carrier","Carrier","Command Vehicle","Engineering Vehicle","Fire Support Vehicle","Infantry Fighting Vehicle","Launcher","Maintenance and Recovery Vehicle","Mine Clearing Vehicle","Personal Carrier","Reconnaissance Vehicle","Recovery Vehicle","Repair Vehicle","Self-Propelled Anti-Tank Vehicle","Self-Propelled Gun","Self-Propelled Mortar","Supply Vehicle","Tank Destroyer","Transport","Utility Vehicle"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd3 = Math.floor(Math.random() * nm4.length);
		rnd4 = Math.floor(Math.random() * nm3.length);
		rnd5 = Math.floor(Math.random() * nm3.length);
		if(rnd4 < 10){
			while(rnd5 < 10){
				rnd5 = Math.floor(Math.random() * nm3.length);
			}
		}
		rnd6 = Math.floor(Math.random() * nm5.length);
		rnd7 = Math.floor(Math.random() * nm6.length);
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm4[rnd3] + nm3[rnd4] + nm3[rnd5] + nm5[rnd6] + nm6[rnd7] + " " + nm1[rnd] + " " + nm2[rnd2];
		nm1.splice(rnd, 1);
		nm2.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}