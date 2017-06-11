var names1 = ["Ailing Woods","Angelwood","Ashfield","Ashgate","Ashmount","Ashtomb","Atonement","Big Spring","Bitterhold","Black Castle","Black Citadel","Black Crow","Black Forest","Black Fortress","Black Garden","Black Mountain","Iron Valley","Black Tower","Blackford","Blackport","Blackstorm","Blacktomb","Blackwater","Boarwood","Boulder Mountain","Bouldergate","Boulderkeep","Brinestone","Broken Bridge","Broken Dreams","Broken Hill","Broken Mountain","Bronzefield","Burned Bridge","Butcher's Cove","Charred Cove","Closed Gate","Cold Heart","Coldwater","Crimson Cove","Dark Citadel","Dark Fortress","Dark Portal","Dark Vaults","Darkside","Darkwater","Deadwater","Deephold","Desolation","Desperation","Devil's Gate","Doveport","Downwater","Dragon Isle","Dragontooth","Early Grave","Edgefield","Edgeville","Ember Island","Firevault","Flamewood","Forest Edge","Forsaken Forest","Frenzy Cay","Frost Cave","Frost Mountain","Frostgate","Frozen Citadel","Frozen Desert","Frozen Lake","Frozen River","Frozen Time","Game Over","Gatehouse","Ghost Isle","Golden Cay","Goldengate","Goldfield","Grandhaven","Graveworth","Greyrock","Grimway","Hallow Hill","Hellbound","Hot Spring","Howling Fjord","Howling Wind","Illwood","Imp Mountain","Iron Gate","Iron Keep","Ironbolt","Ironfist","Irongate","Irongrasp","Ironport","Joyville","Killingfield","Last Chance","Last Door","Last Rites","Limbo","Lonewood","Long Bay","Long Wait","Madstone","Maincastle","Mallhaven","New Chance","New Hope","Newgate","Nightmare","Nightstone","No Refuge","Numb Mountain","Numbwater","Oak Creek","Oakwood","Oblivion","Obsidian Dungeon","Obsidian Maze","Obsidian Retreat","Obsidian Tower","Old Mountain","Outcast","Pale Forest","Phoenix","Pineneedle","Pinewood","Purgatory","Pyreford","Raven's Nest","Ravenhold","Ravenwing","Ravenwood","Red Garden","Redemption","Retirement","River Bank","River Garrison","Riverbend","Rockwood","Rotten Creek","Saltwater","Sanctuary","Sanguine Isle","Sanguine Wood","Scarlet Bay","Scarlet Mountain","Scarlet Tower","Scorchwood","Shadow Citadel","Shadow Isle","Shadow Keep","Shark Bay","Shroudcliff","Silent Gallows","Silent Heights","Silent Wind","Silver Lining","Silver Shield","Silverbay","Silverchain","Silvercloud","Silverhold","Silverwater","Sky Vaults","Solidgate","Solitude","Stillwater","Stoneward","Storm Bay","Storm Cape","Storm Cave","Storm Desert","Stormford","Stormpits","Stormvault","Strongford","Strongwall","Terminus","Thunder Bay","Time Out","Tinderland","Tortoise Isle","Turtle Bay","Ultimatum","Wallbottom","Warfield","Wargate","Wasteland","Whisperwind","White Forest","White Garden","Wild River","Wildlands","Willow Creek","Winter Fortress","Woodford","Wormwood","Wrong Path"];
var names2 = ["Asylum","Correctional Center","Correctional Facility","Detention Center","Holding Center","Institute","Institution","Juvenile Holding Center","Low Security Prison","Max Security Prison","Medium Security Prison","Penitentiary","Prison","Regional Prison","Work Camp"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		rnd2 = Math.floor(Math.random() * names2.length);
		names = names1[rnd] + " " + names2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}