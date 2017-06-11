var nm1 = ["Akamaru","Alfalfa","Alien","Alphonso","Alvin","Aokuro","Aono","Avalanche","BananaHammock","BananaPunch","Bananas","Bananerz","Banjo","Bannanas","Banzai","Barnaby","Belvedere","Beppo","BigPete","BigSteve","Bleach","Bobo","Bones","Bonkbek","Bonkers","Bonzo","Boots","Brass","BrassMonkey","Bubbles","Business","Butters","Cedric","Chappal","Chawworra","Cheruurrik","Chimes","Chimp","ChimpCharlie","Chipmunkey","Chubaka","Chuckapoo","ChunkyMonkey","ChunkyMunkey","Claw","Clide","Clyde","Cooter","Corky","Cornelious","Cornelius","Cosmo","Couch","Darwin","Dejen","Dookie","Duffy","Eggo","Elgon","Elmer","FecalFlinger","Fidget","Fido","FirstMate","Fivel","Fleabag","Fred","Fredrick","Frowrakich","Fujioka","Funky","FunkyMonkey","FuriousJorge","Gaspode","George","Gerbil","Gigantor","Giggles","Gilley","Gilligan","Ginhon","Gordon","Gorilladin","Grapeape","Grawahrr","Grease","Grillya","Grums","Guantichosd","Hanatoyo","Harahon","HearNoEvil","Herashorr","Ichimura","Iflingpoo","Igawa","Igby","Infernape","Iwaharu","Iwato","Jaccuka","Jade","JarJar","Jello","Jim","Jimmy","Jingles","JoJo","Juice","Jumana","Justin","Kachrarc","Kahlua","Kamiyama","Kar","Katie","Kawakita","Kenhira","Kep","KingKong","Kinue","Kitaka","Klepto","Knuckles","Koko","Kong","KungFuPoo","Linus","Lochanhakk","Lockjaw","Lokaap","Lucas","Lugnut","Lunatic","Magilla","Mankey","Marley","Maruikei","Matsumura","Matsuoo","Moco","Mojo","MojoJojo","Momo","Monkey","MonkeyBone","MonkeysUncle","Montgomery","Moptop","Morida","Morikami","Morikawa","Morishima","Moroto","Morruuna","Motewnawr","MrNilsson","Mugsy","Munky","Murdock","Murny","Nabe","Noelle","Noharu","Noken","Nokin","Nostradamus","NutJob","Nyrka","Ohoh","Omori","Onu","Ooga","OptimusPrimal","Pancakes","Pansy","Peaches","Pewner","Pickles","Pimple","PooFlinger","Pootapult","Popeye","Poppa","Predator","Primeape","Rafiki","Reyrrrwacca","Roobarb","Ruxpin","Sakakei","Sakamori","Sakanaka","Sakiko","Sakizaki","Sarah","Sawa","Sebastian","SeeNoEvil","Seymour","Sinclair","Situation","Slingshot","Spank","Spanks","SpeakNoEvil","Suzu","Suzukin","Takakei","Takazawa","Tater","Tbone","TheSituation","Thunder","Thunderstomp","Tim","Timmy","Tiny","TinyTim","Tipster","Tizzy","Tooter","Tremor","Truffles","Truk","TrunkMonkey","Tulip","Turdis","Tygarr","Tyrock","Ueshima","Utcharrakk","Waffles","Wilbur","Wingnut","Worrawrowr","Yama","Yamakami","Zach","Zawabashi","Zawaoo","Zimba","Zippy","iFlingPoo","iPoo"];

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