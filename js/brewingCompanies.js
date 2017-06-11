
function nameGen(type){
	var nm1 = ["Aegis","Aerie","Alabaster","Alchemist","Alesmith","Anchor","Angel Wing","Arcadia","Artisan","Audacity","Aurora","Avalanche","Barbarian","Barrage","Beard and Barrel","Bearded Barrel","Beaver Dam","Belly Hop","Bison","Black Diamond","Black Stallion","Black Swan","Black Widow","Blizzard","Blue Creek","Blueprint","Bootleg","Borealis","Bottom's Up","Boulder","Brass Cannon","Brickstone","Brimstone","Buffalo","Bull Horn","Cackling Hyena","Capital","Cascade","Catfish","Celestial","Cloud Nine","Cosmos","Crescent","Crossroad","Crystal","Dark Horse","Demon Horn","Diamond","Dominion","Dragon Scale","Dragonfire","Dragonmead","Eclipse","Elysium","Emerald","Empyrean","Epic","Epoch","Equinox","Estuary","Expedition","Feather Falling","Feral","Ferocious","Final Frontier","Final Swallow","Flying Compass","Flying Dutchman","Flying Fish","Flying Pig","Forge","Fountain","Full Moon","Glacier","Glass Bottom","Gold Rush","Goodlife","Gorilla","Grand Northern","Great Eastern","Griffin","Gritty","Guerilla","Hairy Turtle","Halo","Hare and Turtle","Hellhound","High Rise","Holy Cow","Hop 'o the Morning","Hop Dog","Hop Notch","Hop Story","Hop of the Hour","Hops and Robbers","Hourglass","Howling Wolf","Hurricane","Infinite","Infinity","Intrepid","Intrepid Journey","Journey","Labyrinth","Lakeside","Last Barrel","Last Glass","Last Whistle","Liquid Hero","Little Pint","Little River","Lone Tree","Lone Wolf","Long Oak","Mad Malts","Magnitude","Marble","Mason","Midnight","Midnight Meteor","Minotaur","Mirror Lake","Moustache","Mutual Friend","New Realm","Nirvana","Noble","Nordic","Norse","Nova","Obelisk","Obsidian","Oceanside","Omega","Omen","One Hop Stop","Onyx","Oracle","Over the Hop","Paradise","Paragon","Passage","Phoenix","Pinnacle","Pioneer","Praying Mantis","Prime Time","Props to Hops","Pyramid","Red Herring","Revolution","Rough Draft","Rough Sketch","Salty Dog","Sanctuary","Sanctum","Sapphire","Seafront","Side Project","Silver Tongue","Single Barrel","Smooth Sailing","Speakeasy","Starlight","Steamworks","Steel Beam","Stone","Strange","Stranger Tides","Summit","Sunshine","Sweetwater","Tall Tales","Thirsty","Thunder","Tidal Wave","Timeless","Tiptop Hop","Torrent","Tributary","Tricerahops","Trouble","Twin Barrel","Two Birds","Up's Bottom","Valiant","Valor","Vertex","Victory","Viking","Vintage","Voyage","Wanderlust","War Horse","Wheelbarrow","White Water","Wild Western","Wingman","Workhop","Zion"];
	var nm2 = ["Brewing Company","Brewers","Brewing","Fermentary","Brewing Co.","Brewery","Aleworks","Craft Ales","Brewing Company","Brewers","Brewing","Brewing Co.","Brewery"];
	var nm3 = ["","","","","","The "];
	
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		names = nm3[rnd3] + nm1[rnd] + " " + nm2[rnd2];
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