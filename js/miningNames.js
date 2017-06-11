var nm1 = ["Apex","Apex Empire","Astral","Astral Minerals","Avalon","Base Works","Basic Burrows","Bedrock Bed","Bedrock Bonanza","Bedrock Bottom","Big Burrows","Black Burrows","Blackrock","Bottom's Up","Bouldercreek","Boulderfist","Brave Depths","Brave Ventures","Breakwater","Brimming Grounds","Brimstone","Broken Hill","Bursting Gorge","Carbon Copy","Carbon in the Rough","Carbonhill","Centurion","Century","Coal Creek","Coal Field","Cobalt Cove","Cobalt Grove","Copper Capers","Coppervale","Covert Coal","Crag Works","Crevice Creek","Dark Depths","Darkness","Deep Delves","Delta Depths","Deposit Depths","Depth Delvers","Diamond Delta","Diamond Depths","Diamond Downs","Diamond Drifts","Diamond Hill","Diamond Rush","Diamonds in the Rough","Dirty Delves","Dirty Depths","Draft Shaft","Eager Extracts","East Range","Ebon Depths","Ebony Abyss","Ebony Hill","Echo Depths","Echo Grounds","Elemental Elevation","Elemental Expanse","Elemental Extents","Elemental Extracts","Elemental Fundamentals","Energy Grounds","Extension Hill","Firestone","Fortune Fields","Fracture Field","Fracture Hill","Gem Packed","Gem-Packed Expanse","Gold Banks","Gold Creek","Gold Drops","Gold Field","Gold Grove","Gold Nugget","Gold Springs","Goldrush","Goldworth","Grand Chasm","Grand Expedition","Grand Exploration","Grand Grounds","Grand Measures","Grand Metal","Grand Nugget","Grand Quarry","Grand Range","Grand Resources","Grand Ridge","Grand Ventures","Grimestone","Grimstone","Groundworks","Hidden Gem","Hidden Nugget","Hope Downs","Intrepid Depths","Intrepid Ventures","Iron Baron","Iron Field","Iron Isles","Iron Legacy","Iron Mountain","Iron Peaks","Ironskin","Ironwing","Landscrape","Lead Leaders","Lead Legacy","Legacy","Metal Depths","Metal Exploration","Metal Miles","Metal Picks","Metal Springs","Metal Ventures","Minecorp","Mineral Chasm","Mineral Creek","Mineral Expanse","Mineral Field","Mineral Foundations","Mineral Grove","Mineral Picks","Mineral Pit","Mineral Reserve","Mineral Store","Mineral Ventures","Mount Venture","Mulligan","Nether Region","Netherwork","Nordic Gold","Nordic Ventures","North Peak","Nugget Field","Obsidian Depths","Onyx Depths","Opulence Depths","Panworks","Pinnacle","Precipice Paradise","Prosperity Hill","Prosperity Precipice","Quarry Query","Rainbow Minerals","Rare Reserve","Rich Rocks","Rock Bottom","Rocky Road","Sediment Banks","Sediment Creek","Sediment Hill","Sediment Vale","Silver Banks","Silver Expanse","Silver Nugget","Silver Shovel","Silver Silts","Silver Slivers","Silver Surveys","Silver Veil","Silverstone","Slate Works","Smashing Works","Smudgehill","Soothill","Southstone","Sparkling Grounds","Stonework","Talc Treasures","Talc Trench","Terra Firma","Terra Formations","Terra Nova","Terra Territory","Terra Tunnels","Terrain Titans","Thunder","Thunderrock","Tin Terrains","Tin Terrane","Tin Titans","Tin Trench","Tin Trove","Tin Tunnels","Titan Trove","Treasure Trove","Tunnelworks","Twin Creek","Twin Springs","Underground","Wealth Well","Wellspring","West Field","Zinc Holes"];
var nm2 = ["Mining","Mining Companies","Mines","Mining Group","Mineshaft","Company","Corporation","Industries","Mining Corporation"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
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