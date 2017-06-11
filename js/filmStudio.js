function nameGen(){
	var names1 = ["Active","Adorable","Amazing","Amusing","Ancient","Angel","Angry","Awesome","Baby","Bad","Big","Big Bad","Black","Bold","Brave","Bright","Busy","Cinematic","Classic","Clever","Clumsy","Crazy","Creative","Curious","Cute","Dancing","Dapper","Dark","Dear","Dirty","Dopey","Dream","Dreaming","Eager","Eastern","Ecstatic","Elegant","Exalted","Excited","Exotic","Famous","Fancy","Fantasy","Fluffy","Free","Funny","Galactic","Gentle","Glass","Golden","Good","Green","Grumpy","Hairy","Happy","Imaginary","Infamous","Jade","Jolly","Joyful","Kind","Laughing","Legendary","Light","Little","Lost","Lucky","Lunar","Mad","Merry","Moving","Naughty","Night","Northern","Odd","Orange","Original","Playful","Playing","Proud","Quick","Rare","Red","Regal","Royal","Running","Silent","Silly","Silver","Sleeping","Smart","Smiling","Southern","Tiny","Twin","Virtual","Western","Wild","Working","Young"];
	var names2 = ["Albatross","Alligator","Ant","Ape","Bandicoot","Barnacle","Barracuda","Bat","Bear","Beaver","Beetle","Bird","Bison","Boar","Bull","Bunny","Butterfly","Camel","Canary","Cat","Caterpillar","Chicken","Cobra","Cow","Coyote","Crab","Crane","Crow","Deer","Dingo","Dino","Dog","Donkey","Dove","Dragon","Duck","Eagle","Elephant","Falcon","Fish","Fly","Fox","Frog","Goat","Gopher","Gorilla","Hippo","Horse","Kitten","Kiwi","Lamb","Lemur","Leopard","Lion","Lizard","Llama","Lobster","Moose","Mouse","Otter","Owl","Ox","Panda","Panther","Pelican","Penguin","Pig","Pigeon","Pony","Prawn","Pug","Puppy","Rabbit","Raccoon","Rat","Raven","Rhino","Rooster","Seal","Shark","Sheep","Shrimp","Sloth","Snail","Snake","Spider","Squid","Squirrel","Stork","Swan","Tiger","Toad","Tortoise","Turtle","Walrus","Wasp","Whale","Wolf","Yak","Zebra"];
	var names3 = ["Ancient","Angelic","Antique","Aquatic","Arctic","Artisan","Bad","Blessed","Blue","Bright","Bronze","Burning","Cinematic","Classic","Clockwork","Crystal","Curious","Dark","Diamond","Double","Eastern","Electric","Elegant","Emerald","Eternal","Evony","Exalted","Exotic","Fancy","Fantasy","Flaming","Floating","Flying","Frozen","Giant","Glass","Glowing","Golden","Granite","Greater","Green","Happy","Ice","Imaginary","Immortal","Infamous","Infinite","Ivory","Jade","Laughing","Legendary","Light","Little","Lonely","Lost","Lunar","Magma","Magnificent","Mammoth","Marble","Master","Miracle","Monochromatic","Moving","Night","Northern","Odd","Orange","Original","Perfect","Premium","Primal","Rare","Red","Regal","Remote","Rising","Royal","Ruby","Rusty","Sapphire","Shifting","Shining","Silent","Silver","Smiling","Smooth","Snow","Solar","Super","Surprise","Timeless","Tiny","Twin","Universal","Vibrant","Virtual","Western","Wild","Wonder"];
	var names4 = ["Angel","Apple","Arena","Assistant","Avenue","Bandit","Blossom","Bond","Branch","Bridge","Brothers","Candle","Champion","Cloud","Companion","Cosmos","Crown","Dimension","Dream","Earth","Edge","Embassy","Empire","Enigma","Fantasy","Figurine","Fire","Flow","Flower","Gadget","Galaxy","Gate","Giant","Globe","Halo","Heart","Heaven","Knight","Lantern","Media","Mind","Ministry","Mirror","Monolith","Monument","Moon","Motion","Mountain","Nation","Nature","Obelisk","Orb","Paradise","Path","Petal","Pinnacle","Planet","Portal","Prism","Puzzle","Pyramid","Rainbow","Realm","Ring","River","Road","Robot","Sapling","Screen","Shrine","Signal","Sisters","Sky","Spire","Spirit","Sprite","Star","Statue","Summit","Sun","System","Temple","Tiara","Tower","Town","Toy","Tree","Trinket","Union","Universe","Utopia","Vault","Vertex","Village","Vortex","Wall","Water","Wings","Workshop","World"];
	var names5 = ["Angel","Autumn","Bright","Chrono","Cine","Clock","Cloud","Digi","Film","Fire","Free","Frozen","Imagi","Imagine","Inter","Intro","Light","Lime","Liquid","Lunar","Mega","Micro","Mind","Moon","Motion","Movie","Nether","Photo","Pic","Pro","Puzzle","Road","Silver","Sky","Snow","Solar","Star","Summer","Sun","Thunder","Uni","Wing","Winter"];
	var names6 = ["art","blossom","bolt","bunch","cloud","dream","film","fire","flix","flux","glass","graphs","less","light","line","magic","magine","mark","matic","motion","myth","pix","play","realm","saga","scope","screen","soft","sphere","storm","tainment","tale","topia","verse","wood","works","world","zone"];
	var names7 = ["Ambience","Angel Wings","Anomaly","Aspect","Aura","Aurora","Azure","Bliss","Bullettime","Century","Clairvoyant","Climax","Crown","Cyclops","Destiny","Dreamland","Eclipse","Emerald","Enchanted","Enigma","Enterprise","Eternity","Eventide","Exile","Fable","Fantasy","Fluke","Fortune","Galaxy","Giant","Gold","Graphic","Harmony","Illusion","Imagination","Imagine","Immortal","Karma","Knight","Legend","Limbo","Limelight","Little Spirit","Locomotion","Lunar","Maximum","Midnight","Millenium","Miracle","Mithril","Moon","Motion","Mystery","Mystic","Mythic","Nirvana","Oblivion","Obscure","Oracle","Outcast","Paradox","Paragon","Perception","Phenomenon","Picture","Pinnacle","Platinum","Prodigy","Renegade","Reverse","Rising Star","Rogue","Ruby","Saga","Sapphire","Sensation","Silver","Silver Cloud","Solar","Stardust","Starlight","Summit","Sun","Supreme","Surprise","Thunder","Titan","Tomorrow","Transcend","Trinket","Twilight","Ultimate","Underground","Utopia","Vertigo","Vision","Vortex","Wild","Zion","Zodiac"];
	var names8 = ["Entertainment","Film Company","Studio","Pictures","Productions","Cinema","Film","Filmworks","Studios","Film Productions","Films","Film Studios"];
	
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names8.length);
		if(i < 2){
			rnd1 = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names2.length);
			names = names1[rnd1] + " " + names2[rnd2] + " " + names8[rnd];
		}else if(i < 5){
			rnd1 = Math.floor(Math.random() * names3.length);
			rnd2 = Math.floor(Math.random() * names4.length);
			names = names3[rnd1] + " " + names4[rnd2] + " " + names8[rnd];
		}else if(i < 8){
			rnd1 = Math.floor(Math.random() * names5.length);
			rnd2 = Math.floor(Math.random() * names6.length);
			names = names5[rnd1] + names6[rnd2] + " " + names8[rnd];
		}else{
			rnd1 = Math.floor(Math.random() * names7.length);
			names = names7[rnd1] + " " + names8[rnd];
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