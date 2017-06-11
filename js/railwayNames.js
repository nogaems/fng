var nm1 = ["Alligator Shallows","Ancient Heights","Angel Harbor","Arrow Point","Bamboo Park","Bamboo Wetland","Black Loch","Black Waters","Bog Forest","Borderlands","Boreal Plains","Boulder Shore","Boulderland","Breakwater","Central Snowland","Chasewater","Cherry Blossom","City Hall","Coastway","Community","Cottonfield","Creekside","Cross Country","Crystal Castle","Crystal Lake","Distant Waters","Dragonfly","Eagle Forest","East Coast","East Tropics","Eastern","Eastern City","Eastern Hills","Eastern Steppes","Echo Valley","Ethereal Wilds","Evergreen Glades","False River","Flat Water","Flower Gardens","Fogland","Fozen Tundra","Frost Mountain","Frostfire","Frozen Pinnacle","Gentle Coast","Glacier Forest","Golden Palace","Grand Central","Grand Coastal","Grand Continental","Grand Forest","Grand Island","Grand Meadows","Grand Temple","Grand Valley","Gray Pinnacle","Great Central","Greenbelt","Greencoast","Grizzly Forest","Harborview","Harmony Creek","Harmony Morass","High Mountain","High Valley","Highland","Hollow Rock","Hope Meadows","Hope Valley","Ice Crowned","Iceberg","Iron Fjord","Iron Lake","Ironbark","Ivory Fields","Jade Gardens","Jade Waters","Kings Harbor","Lillypad","Little Rock","Little Valley","Lonely Mountain","Lotus Lake","Low Valley","Lowland","Maiden Stone","Maple Grove","Marble Cliff","Marble Coast","Marble Harbor","Maritime","Marshland","Meltwater","Midland","Midnight","Midsummer","Midwinter","Mighty Mountains","Mirror Lake","Mirror Pools","Misty Meadow","Molten Bay","Moonshadow","Murky Marsh","Narrow Fields","Narrow Wilds","New Channel","New Forest","New Haven","New North","New South","Nightingale","North Central","Northbound","Northern","Northern City","Oakland","Observatory","Old Forest","Orchard Park","Palm Shore","Paradise Coast","Pelican Beach","Phantom Falls","Pleasant View","Precious Wilds","Pristine Gardens","Quiet Field","Quiet Fields","Rain Forest","Red Wasteland","Redwood","Riverfront","Rivermouth","Riverview","Coal Belt","Hunter Country","Sacred Woods","Salmon Pier","Salt Lake","Sapphire Coast","Savage Coast","Savannah","Sea Breeze","Serenity","Serenity Beach","Serenity Hills","Serpent Channel","Serpent Falls","Settlers Point","Seven Palace","Shadow Fields","Shadow Lake","Shark Harbor","Shrimp Bay","Silent Tundra","Silver Hills","Silver Lake","Silver Wall","Silverstone","Six Mountain","Sleeping Mountain","Sleeping Rivers","Snow Crystal","Snow Meadow","Snowman","Somerset","Songbird","Soundscape","South Beach","South Central","Southern","Southside","Spring Blossom","Spring Valley","Spruce Forest","Stone Coast","Stone Lake","Storm Coast","Sunflower","Sunny Cay","Sunny Fields","Sunrise","Sunset","Sunshine Coast","Surfer Coast","Tadpole River","Tree Valley","Tropic Wetland","Turtle Coast","Turtle Swamp","Twelve City","Twin Mountain","Twin River","Uncanny Valley","University","Virgin Garden","Virgin Rapids","Virgin Valley","West Beach","West Coast","Wester Bog","Western","Wetlands","Whale Water","Whisper Valley","White Bay","White Sand","White Tundra","White Water","Whitehaven","Wild Ocean","Wild Rose","Willowvale","Windy Woods","Wolf Meadow"];
var nm2 = ["Route","Main Line","Speed Line","Loop Line","Branch Line","Line","Rail Line","Tracks","Train Line","Line","Line","Line","Route","Route","Route","Tracks","Tracks","Tracks"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + " " + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}