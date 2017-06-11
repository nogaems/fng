var nm1 = ["Aegis","Aello","Aethon","Albatross","Alicanto","Alicorn","Ambrosia","Amrita","Angel","Aphrodite","Apollo","Apostle","Ara","Argo","Aria","Arondight","Artemis","Arthur","Ascalon","Ash","Astra","Aura","Aurora","Avalanche","Avalerion","Avalon","Azoth","Bandit","Barbarian","Beast","Behemoth","Big Bird","Blaze","Blizzard","Boomer","Brawl","Broxa","Bumblebee","Bustard","Cinder","Cockatrice","Condor","Cormorant","Cosmos","Crane","Creature","Critter","Cryobird","Cupid","Cyclone","Cyclops","Demon","Devil Bird","Diablo","Dustdevil","Dynamite","Eagle","Echo","Effigy","Ellida","Enigma","Ether","Ethereal","Excalibur","Exile","Falcon","Feather","Fiend","Firebird","Flamingo","Flash","Fluke","Fray","Frenzy","Frigatebird","Fury","Gale","Gargoyle","Ghost","Glory","Glutton","Goliath","Gram","Griffin","Growler","Guerrilla","Gungnir","Gust","Hades","Harpy","Hawk","Hawker","Helix","Herald","Heretic","Hippogriff","Hornet","Hover Dove","Hoverbird","Howler","Hummingbird","Hunter","Huntress","Huricane","Husk","Hussle","Hydra","Illume","Inferno","Javelin","Juvenile","Kindle","Kingfisher","Kookaburra","Lark","Leviathan","Lightning Bird","Loki","Lumina","Lyrebird","Mammoth","Medusa","Miracle","Mithril","Mjolnir","Monsoon","Mother Hen","Naglfar","Nebula","Nightingale","Nova","Nurse","Omen","Oracle","Orb","Ozone","Pamola","Pandora","Paradox","Parakeet","Pelican","Phantom","Phoenix","Poseidon","Pterodactyl","Pterosaur","Pyre","Pyrobird","Quail","Quarrel","Queen Bee","Rebel","Rebound","Renegade","Riot","Roc","Rumbler","Sanddevil","Seahawk","Silver","Siren","Sliver","Snake","Spot","Spotlight","Squall","Stalker","Stallion","Stark","Stork","Storm","Strife","Striker","Swan","Swift","Swiftstrike","Talaria","Tempest","Teratorn","Terrorbird","Thor","Thunder Bird","Thunderbolt","Tigress","Tinder","Trumpet","Tucan","Typhoon","Varmint","Veil","Vermillion","Vimana","Void","Volley","Vulture","Warbler","Wasp","Zephyr","Zeus","Zion"];
var br = "";

function nameGen(){
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