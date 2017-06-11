var names1 = ["Ancient","Antique","Aquamarine","Atlantic","Atlantis","Autumn","Azure","Brass","Bronze","Cerulean","Crimson","Crown","Double","Dual","Eastern","Ebony","Elder","Elite","Emerald","Exalted","Gentle","Glorious","Golden","Grand","Grandiose","Historic","Illustrious","Ivory","Jade","King's","Light","Lord's","Lunar","Majestic","Malachite","Marina","Mellow","Modest","Noble","Northern","Obsidian","Olive","Onyx","Oriental","Pacific","Parallel","Peaceful","Pleasant","Primal","Prince's","Private","Queen's","Quiet","Regal","Remote","Riverside","Rose","Royal","Ruby","Saffron","Sapphire","Scarlet","Secluded","Secret","Serene","Silver","Snowy","Soft","Southern","Spring","Sublime","Summer","Sunny","Sunrise","Sunset","Supreme","Tranquil","Triple","Twin","Viridian","Western","White","Winter"];
var names2 = ["Aegis","Angel","Arc","Atoll","Aurora","Baron","Basin","Bay","Bazaar","Beach","Bear","Bliss","Blossom","Bluff","Brewery","Brook","Cabin","Camp","Canopy","Canyon","Carnaval","Castle","Cave","Cavern","Chasm","Circus","Citadel","Cliff","Cloak","Cloud","Coast","Comfort","Cosmos","Cottage","Court","Courtyard","Cove","Covert","Creek","Crow","Crown","Dawn","Dome","Dream","Dune","Echo","Elephant","Emperor","Estate","Excalibur","Expanse","Fjord","Flower","Forest","Galaxy","Garden","Gardens","Gem","Gorge","Grotto","Grove","Gulf","Harbor","Haven","Heights","Heirloom","Heritage","Hill","Horizon","House","Island","Isle","Jewel","Jungle","Keep","Lagoon","Lake","Landscape","Legacy","Lion","Loch","Lodge","Luxury","Majesty","Manor","Mansion","Mantle","Maple","Market","Meadows","Memorial","Mill","Mirror","Monarch","Mountain","Nebula","Nimbus","Nugget","Oak","Obelisk","Ocean","Orb","Oyster","Palace","Palms","Panorama","Paradise","Park","Pass","Pastures","Peak","Peaks","Peninsula","Petal","Phoenix","Pier","Pinnacle","Plains","Plaza","Point","Pool","Prairie","Pyramid","Quest","Rainbow","Raven","Refuge","Renaissance","Residence","Ribbon","Ridge","River","Rose","Safari","Sanctuary","Sanctum","Seashore","Seaside","Season","Shack","Shield","Shore","Shores","Shrine","Shroud","Sierra","Spa","Spire","Spring","Square","Star","Summit","Sword","Temple","Thicket","Tide","Time","Tower","Treasure","Trinket","Tropic","Tundra","Universe","Vale","Valley","Veil","Vertex","View","Vista","Willow","Wolf","Woodland"];
var names3 = ["Abundance","Amber","Amenity","Amuse","Anomaly","Antique","Antiquity","Apex","Asylum","Azure","Baroque","Beverage","Blizzard","Breakwater","Celestial","Chateau","Cinnamon","Citadel","Cloud","Coastline","Coffee","Comfort","Copper","Cosmos","Countryside","Courtyard","Cozy","Crescent","Crown","Curiosity","Daydream","Delight","Deluge","Deluxe","Diamond","Diorama","Drizzle","Echo","Elegant","Elysium","Emerald","Enigma","Enterprise","Epitome","Essence","Everland","Exalted","Excursion","Expedition","Fairyland","Fancy","Fantasy","Farmhouse","Felicity","Freedom","Galaxy","Glacier","Glee","Globetrotter","Golden Nugget","Grand","Harborview","History","Holiday","Iceberg","Icecap","Imperial","Jade","Leisure","Lethargy","Liberty","Lunar","Luxury","Mahogany","Majestic","Mirage","Mirror","Mirth","Monolith","Monsoon","Moonlight","Moss","Mountain","Muse","Nature","Nebula","Nimbus","Nostalgia","Nourish","Nova","Obelisk","Ocean","Oceanside","Oceanview","Opportunity","Oracle","Orbit","Oriental","Ornate","Outlook","Palace","Panorama","Paradise","Paragon","Parellel","Pinnacle","Prism","Prophecy","Radiance","Rain","Rainbow","Ranch","Recreation","Refresh","Regal","Relaxation","Renaissance","Repose","Retro","Revelation","Road Trip","Rosewood","Royal","Salt Water","Sanctuary","Sanctum","Sapphire","Seacoast","Seascape","Seashore","Seaside","Seven Seas","Shoreline","Sierra","Sightsee","Slumber","Smile","Snooze","Solar","Spare Time","Spectrum","Stardust","Stargaze","Starlight","Stellar","Stratosphere","Summit","Sunway","Sweet Dreams","Tower","Travel","Traveller","Triumph","Troposphere","Universe","Utopia","Vacation","Vanilla","Vertex","Viewpoint","Vision","Vortex","Voyage","Voyager","Wanderlust","Windmill","Wonderland","Yesteryear","Zion"];
var names4 = ["Hotel","Resort","Resort & Spa","Hotel & Spa","Hotel","Hotel","Resort"];

function nameGen(){
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names2.length);
			rnd3 = Math.floor(Math.random() * names4.length);
			names = names1[rnd] + " " + names2[rnd2] + " " + names4[rnd3];
		}else{
			rnd = Math.floor(Math.random() * names3.length);
			rnd2 = Math.floor(Math.random() * names4.length);
			names = names3[rnd] + " " + names4[rnd2];
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