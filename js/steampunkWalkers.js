
function nameGen(){
	var nm1 = ["Abomination","Achiever","Albatross","Ambition","Ant","Arachne","Arachnid","Atlas","Badger","Bear","Beast","Beetle","Behemoth","Beholder","Bender","Bigg","Black Bear","Boar","Booster","Bouncer","Bovine","Brass Knuckle","Brawler","Bruiser","Brute","Bull","Bumble Bee","Burrower","Butcher","Calf","Centaur","Challenger","Champion","Cleanser","Cockroach","Colossus","Commander","Companion","Courier","Crab","Crane","Crawler","Creator","Creature","Crustacean","Curator","Cyclops","Defender","Diagnosis","Digger","Dino","Dispatcher","Divebomb","Diver","Dodger","Donkey","Dozer","Drone","Eagle","Echo","Effigy","Elephant","Escort","Fairy","Fire Ant","Fireman","Forger","Frankenstein","Gargantua","Gargoyle","Gift","Godzilla","Goliath","Gorilla","Grizzly","Grunt","Guardian","Guide","Handyman","Harvester","Herald","Hercules","Hermit","Hornet","Hummingbird","Hypnotizer","Idol","Infernal","Insect","Inspector","Jack","Jack-Of-All-Trades","Jacket","Judge","Kraken","Leapfrog","Logger","Lumberjack","Lurker","Mammoth","Mare","Matriarch","Medic","Messenger","Minotaur","Model","Mole","Monkey","Mosquito","Muscle","Night Mare","Officer","Ogre","Operator","Ox","Passenger","Patriarch","Patriot","Pincer","Pioneer","Professor","Quaker","Rabbit","Rambler","Recruit","Rhino","Rig","Rigg","Roach","Robin","Rumbler","Scarab","Scarecrow","Scientist","Seahorse","Servant","Sheriff","Shoulder","Shrieker","Siren","Snail","Songbird","Spider","Sprite","Stallion","Stinger","Suit","Supporter","Surgeon","Thunder","Titan","Toddler","Vessel","Volunteer","Voyager","Walker","Wanderer","Whistler","Yak","Zealot"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		names = "The " + nm1[rnd];
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