var nm3 = ["-","-","-","-","-","-","-","-","-","-","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"];
var nm4 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z"];
var nm5 = ["1","2","3","4","5","6","7","8","9","0"];
var nm6 = ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"];

function nameGen(type){
	var nm1 = ["Achilles","Aegis","Alaric","Ancestor","Anteater","Apache","Arbiter","Arist","Aristodemus","Armadillo","Arminius","Attila","Aurora","Authority","Awe","Badger","Bandit","Bane","Barrage","Basil","Basilisk","Basin","Battlemaster","Beast","Beelzebub","Beetle","Behemoth","Bigwig","Bison","Black Knight","Blitz","Blizzard","Bloodlust","Brass","Brass Knuckle","Buffalo","Bull","Bulldozer","Bulwark","Buster","Butcher","Buttress","Caesar","Centaur","Centurion","Challenger","Chaos","Chaperon","Citadel","Colossus","Comanche","Comet","Commander","Commando","Courage","Covenant","Coyote","Creator","Creature","Cruiser","Crusher","Crux","Cthulu","Curator","Custodian","Cyclone","Cyclops","Czar","Daemon","Dawn","Deluge","Demon","Deputy","Devil","Diablo","Djinn","Dragon","Dragoon","Drake","Dread","Duster","Ecstasy","Elephant","Emperor","Eternal","Fortress","Furor","Fury","Gargantua","Gargoyle","Genesis","Genghis","Gladiator","Glutton","Goliath","Governor","Guardian","Gurkha","Hades","Hammerhead","Hannibal","Harvester","Hellhound","Hellion","Herald","Hippo","Hog","Horatius","Hydra","Immortal","Impaler","Impulse","Infernal","Inferno","Infidel","Judge","Judgement","Julius","Justice","Kaiser","Khan","Legion","Leonidas","Leopard","Liberty","Lionheart","Lucifer","Lurker","Lynx","Maharajah","Mamluk","Mammoth","Maori","Mastadon","Matador","Matriarch","Maverick","Meteor","Miltiades","Minotaur","Misery","Miyamoto","Mogul","Monarch","Mongrel","Musashi","Myriad","Napoleon","Nightmare","Overlord","Overseer","Paladin","Panther","Paragon","Patriarch","Patriot","Perseverance","Phantom","Primal","Prime","Primus","Pyrrhus","Quake","Reaper","Requiem","Rhino","Samurai","Savage","Scipio","Scorpion","Scoundrel","Scourge","Scythe","Seism","Sentinel","Shepherd","Shockwave","Slayer","Spartacus","Spartan","Spirit","Spitfire","Stallion","Stark","Steward","Storm","Sultan","Sun Tzu","Sundry","Tarragon","Tempest","Templar","Terror","Thor","Thunder","Thunderclap","Thunderstrike","Titan","Titanium","Torment","Tornado","Tremor","Trooper","Tusker","Typhoon","Vercingetorix","Viking","Viper","Visigoth","Volcano","Wallace","Warden","White Knight","Widowmaker","Wyvern","Xiahou","Zephyr"];

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
		names = nm4[rnd3] + nm3[rnd4] + nm3[rnd5] + nm5[rnd6] + nm6[rnd7] + " " + nm1[rnd];
		nm1.splice(rnd, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}