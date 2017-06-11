var nm1 = ["Achorage","Acorn","Amber","Anchor","Angel","Apollo","Apostle","Arcade","Arch","Archer","Arctic","Art","Ash","Ashland","Auburn","Aurora","Autumn","Aviation","Azure","Baker","Bard","Barley","Bath","Bay","Bay View","Beach","Beachside","Beacon","Beaver","Beech","Bell","Bellow","Berry","Blessing","Bliss","Bloomfield","Blossom","Boulder","Brewer","Bridgewater","Bridgeway","Bright","Broad","Brook","Broom","Brown","Bury","Bush","Butcher","Campus","Canal","Cannon","Castle","Cathedral","Cave","Cavern","Cedar","Central","Centre","Champion","Chapel","Cherry","Chestnut","Circus","Clarity","Clearance","Cliff","Clove","Coach","Coastline","College","Colonel","Commercial","Congress","Copper","Coral","Corporation","Cottage","Crescent","Crimson","Cross","Crown","Crystal","Cypress","Dawn","Delta","Dew","Diamond","Dove","Duchess","Duke","Earl","East","Ebon","Elm","Elmwood","Ember","Emerald","Estate","Fair","Farmer","Feathers","Ferry","Flax","Fleet","Fletcher","Flint","Forest","Fortune","Fountain","Fox","Frost","Garden","Garnet","Gem","General","Gilded","Globe","Gold","Grace","Grand","Granite","Gravel","Gray","Great","Green","Greenfield","Grime","Grotto","Grove","Guild","Harbor","Hart","Haven","Hawthorne","Hazelnut","Heart","Heirloom","Heritage","High","Highland","Hill","Hind","Honor","Hope","Innovation","Ironwood","Ivory","Ivy","Jade","Java","Jewel","Judge","Juniper","Justice","King","Kings","Kingwood","Knight","Lake","Lavender","Law","Lawn","Legend","Liberty","Lily","Lilypad","Little","Locust","Long","Lotus","Love","Low","Lower","Lowland","Lumber","Luna","Main","Mandarin","Manor","Maple","Marble","Marine","Market","Mason","Meadow","Medieval","Merchant","Middle","Mill","Monument","Moon","Moonlight","Mount","Museum","National","New Castle","Nightingale","Noble","North","Nova","Oak","Ocean","Oceanview","Old","Olive","Onyx","Orchard","Orchid","Oval","Palm","Paradise","Park","Parkside","Parkview","Peace","Pearl","Pebble","Pegasus","Penrose","Petal","Phoenix","Pine","Pinnacle","Pioneer","Plaza","Polygon","Poplar","Prince","Princess","Prospect","Providence","Quarry","Queen","Railway","Ranger","Redwood","Revolution","River","Rose","Rosemary","Rowan","Royalty","Ruby","Saffron","Sapphire","School","Seacoast","Seaview","Senna","Serenity","Shade","Shadow","Silver","Smith","Snowflake","South","Spring","Spruce","Star","Starfall","Starlight","Station","Steam","Stone","Storm","Sugarplum","Summer","Summit","Sun","Sunny","Sunshine","Sycamore","Temple","Terrace","Theater","Timber","Tower","Trinity","Underwood","Union","University","Upper","Vale","Valley","Vermilion","Victory","Vine","Vista","Walnut","Water","Wellness","West","Wetland","Wharf","Willow","Windmill","Winter","Wright","Yew"];
var nm2 = ["Street","Avenue","Lane","Row","Boulevard","Way","Route","Passage","Street","Avenue","Lane"];
var br = "";

function nameGen(type){
	var tp = type;
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