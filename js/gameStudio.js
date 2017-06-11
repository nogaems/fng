var names1 = ["Acid","Active","Adorable","Aggressive","Agile","Alarming","Amazing","Amusing","Ancient","Angelic","Angry","Antique","Arctic","Awesome","Baby","Bad","Big","Big Bad","Black","Black and White","Blind","Bold","Brave","Bright","Broken","Bronze","Buzy","Calm","Classic","Clever","Clumsy","Confused","Crazy","Creative","Cute","Dapper","Dark","Deadly","Dear","Defiant","Digital","Dirty","Dizzy","Dopey","Eager","Elegant","Evil","Exalted","Excited","Exotic","Fake","False","Fancy","Fast","Feisty","Filthy","Fluffy","Foolish","Forsaken","Free","Fuzzy","Gentle","Glass","Gloomy","Golden","Good","Gray","Green","Grumpy","Hairy","Happy","Hidden","Hollow","Honest","Hungry","Infamous","Intelligent","Intrepid","Jade","Jolly","Kind","Light","Liquid","Little","Lonely","Lost","Lucky","Mad","Massive","Mellow","Merry","Misty","Naughty","Nervous","Nice","Nifty","Night","Numb","Obvious","Odd","Old","Orange","Original","Peaceful","Plump","Pretty","Proud","Quick","Rare","Red","Royal","Rude","Rusty","Scary","Shadow","Shady","Silent","Silly","Silver","Smart","Snappy","Steel","Strange","Sunny","Sweet","Tiny","Twin","Ugly","Urban","Vicious","Violet","Virtual","Weird","Wild","Wise","Young"];
var names2 = ["Albatross","Alligator","Ant","Ape","Armadillo","Bandicoot","Barnacle","Barracuda","Basilisk","Bat","Bear","Beaver","Beetle","Bird","Bison","Boa","Boar","Bull","Bulldog","Bunny","Butterfly","Calf","Camel","Canary","Cat","Caterpillar","Chicken","Cobra","Cougar","Cow","Coyote","Crab","Crane","Crow","Deer","Dingo","Dino","Dinosaur","Dog","Dolphin","Donkey","Dove","Dragon","Duck","Eagle","Elephant","Falcon","Fish","Fly","Fox","Frog","Gecko","Giraffe","Goat","Gopher","Gorilla","Hamster","Hare","Hippo","Horse","Hyena","Ibis","Jellyfish","Kitten","Kiwi","Lamb","Lemur","Leopard","Lion","Lizard","Llama","Lobster","Manta","Mantis","Moose","Mouse","Newt","Otter","Owl","Ox","Panda","Panther","Pelican","Penguin","Pig","Pigeon","Piranha","Pony","Poodle","Prawn","Pug","Puppy","Rabbit","Raccoon","Rat","Raven","Ray","Rhino","Rooster","Scorpion","Seahorse","Seal","Shark","Sheep","Shrimp","Sloth","Snail","Snake","Spider","Squid","Squirrel","Starfish","Stork","Swan","Tiger","Toad","Tortoise","Turtle","Vulture","Walrus","Wasp","Weasel","Whale","Wolf","Yak","Zebra"];
var names3 = ["Alien","Amulet","Android","Angel","Apple","Assassin","Banana","Bandit","Banshee","Beast","Bigfoot","Blossom","Bow","Boy","Candle","Castle","Cave","Centaur","Champion","Chest","Citadel","Clock","Companion","Crown","Crystal","Cup","Cyborg","Cyclops","Demon","Devil","Diamond","Door","Dwarf","Elf","Emperor","Enigma","Eyes","Face","Fairy","Fire","Flag","Flower","Forest","Fortress","Friend","Fungus","Ghost","Ghoul","Giant","Girl","Gnome","Goblin","Golem","Gryphon","Guardian","Halfling","Helmet","Imp","King","Kiwi","Knight","Lake","Lantern","Light","Lighthouse","Mage","Man","Manor","Mansion","Melon","Mermaid","Merman","Mirror","Monster","Mountain","Mushroom","Nation","Necklace","Nymph","Ogre","Orc","Palace","Paladin","Peanut","Pear","Petal","Phantom","Phoenix","Pirate","Pixy","Potato","Queen","Ring","River","Road","Robot","Satyr","Shadow","Shield","Sidekick","Siren","Skeleton","Slime","Spaceship","Spear","Spectre","Spire","Statue","Stranger","Sword","Thief","Tiara","Tower","Treasure","Tree","Trinket","Troll","Vampire","Viking","Walnut","Watch","Water","Werewolf","Windmill","Wisp","Witch","Wizard","Woman","Wraith","Yeti"];
var names4 = ["angel","astral","auto","autumn","bio","chrono","cyber","dead","demon","feral","fire","free","frost","frozen","ghost","half","info","inter","intro","jade","lightning","liquid","lunar","mega","micro","mist","moon","nether","phantom","real","reflex","silver","snow","solar","star","stray","sub","summer","sun","super","thunder","trick","winter"];
var names5 = ["berg","blast","blossom","bolt","bullet","byte","cloud","control","domain","door","dream","fire","flux","fly","fun","ice","jam","lab","less","line","ly","petal","pixel","play","punch","rain","realm","soft","sphere","storm","tale","trap","ware","water","web","wire","world","zone"];
var names6 = ["Afterlife","Amnesia","Anomaly","Asteroid","Blessing","Bullettime","Cataclysm","Century","Cherry Blossom","Clairvoyant","Climax","Cloudburst","Comet","Crown","Cyclone","Deluge","Destiny","Downpour","Dumb Luck","Dynamic","Enigma","Enterprise","Eternity","Exile","Extinction","Falling Star","Fate","Fierce","Fluke","Flytrap","Fortune","Hellfire","Heretic","Honor","Hurricane","Idol","Immortal","Immortality","Insomnia","Insurgent","Isolation","Karma","Limbo","Locomotion","Lonely","Maximum","Mental","Meteoroid","Millenium","Miracle","Mithril","Monsoon","Motion","Mystery","Mystic","Nirvana","Oblivion","Occult","Outcast","Paradox","Phenomenon","Pinnacle","Prodigy","Psychic","Radical","Rebel","Refugee","Relentless","Renegade","Revelation","Reverse","Rogue","Rose Petal","Ruthless","Sensation","Serendipity","Shooting Star","Skyward","Solarflare","Stardust","Summit","Supreme","Surprise","Thunder","Thunderstorm","Tidal Wave","Time Traveler","Tomorrow","Tragedy","Trinket","Typhoon","Typical","Ultimate","Underground","Untouchable","Vagabond","Vault","Vigor","Void","Zion"];
var names7 = ["Games","Entertainment","Studios","Interactive","Game Studios","Media","Productions","Arts"];
function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names7.length);
		if(i < 3){
			rnd1 = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names2.length);
			names = names1[rnd1] + " " + names2[rnd2] + " " + names7[rnd];
		}else if(i < 5){
			rnd1 = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names3.length);
			names = names1[rnd1] + " " + names3[rnd2] + " " + names7[rnd];
		}else if(i < 8){
			rnd1 = Math.floor(Math.random() * names4.length);
			rnd2 = Math.floor(Math.random() * names5.length);
			names = names4[rnd1] + names5[rnd2] + " " + names7[rnd];
		}else{
			rnd1 = Math.floor(Math.random() * names6.length);
			names = names6[rnd1] + " " + names7[rnd];
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