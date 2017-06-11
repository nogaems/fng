var nm1 = ["Ancestor's Rest","Angel Point","Angelwatch","Angelwing","Autumn Spring","Azure Gardens","Azure River","Big Rock","Bliss Garden","Boulder Creek","Cedar Grove","Cherry Blossom","Crescent Garden","Crown Hill","Crystal Grove","Crystal Lake","Darkwood","Eastlawn","Eastpark","Eden","Elmwood","Emerald Forest","Eternal Light","Eternal Rest","Evergreen","Fairhill","Fairmount","Fairview","Felicity","Field of Ancestry","Field of Honor","Flowerbed","Forest View","Free Spirit","Garden Terrace","Gentle Heart","Gentle Oak","Glory Gardens","Golden Gate","Golden Road","Goodheart Garden","Goodrest","Goodsprings","Graceland","Grand Lake","Grandforest","Grandview","Green Grass","Greenhill","Harmony","Harmony Grove","Harmony Springs","Heirloom Garden","Heritage","Heroes' Field","Heroes' Rest","Hillcrest","Holly Grove","Holy Oak","Hope Hill","Independence","Jade Forest","Juniper Gardens","Keystone","Kingshill","Lakeview","Last Honor","Last Rest","Legacy Lawn","Liberty","Little Light","Little River","Little Rock","Loving Oak","Maple Hill","Memorial Park","Memory Field","Memory Garden","Moonlight","Mountain Crest","Mountain Ridge","Mountain View","Mountainside","New Forest","North Hill","North Park","Oceanview","Old Forest","Olivewood","Paradise","Paradise Garden","Park Lawn","Peace Blossom","Peace Gardens","Peace of Mind","Pearly Gates","Pine Grove","Pinewood","Pioneer","Pleasant Green","Pleasant Valley","Prestige","Rainbow Gardens","Repose Grove","Revered Grove","Riverside","Riverview","Rose Petal","Rosendale","Rosevale","Sapphire Springs","Sea Breeze","Seastone","Serenity","Serenity Park","Small Isle","Snowcrystal","Snowfall","Snowflake","Songbird","South Hill","Spring Garden","Spring Grove","Spring Heights","Spring Meadow","Spring River","Starview","Summer Grove","Summer Hill","Summer Isle","Summer Peaks","Sunnyside","Sunrise","Sunset","Swan Lake","Tranquility Gardens","Tribute Field","Tribute Lawn","Trinity","Venerate Grove","White Angel","White Beach","White Light","White Oak","White Willow","Willow Grove","Willow Park","Skyreach","Lily Vale","Lilypad Lake"];
var nm2 = ["Abandoned","Abandoned Hope","Ash Field","Ash River","Ashen Oak","Ashenvale","Ashvale","Autumn Grove","Bad Judgement","Banewood","Banshee Hill","Barren Field","Beast Forest","Beast Mountain","Black Ruins","Black Snow","Black Soul","Blackburn","Blackhill","Bleak Mountain","Bloodriver","Bone Yard","Broken Bones","Broken Soul","Burned Forest","Burning Forest","Burning River","Burning Rock","Burning Ruin","Burning Soul","Burning Wrath","Calamity Park","Chaos","Condemnation Park","Corruption","Crimson Flow","Dark Willow","Darkhill","Darkview","Darkwood","Demonic Eye","Demonvale","Demonwing","Depravity Grove","Desolate Field","Desparity","Devil's Playground","Devilry Gardens","Devilswood","Diablo","Doomvale","Dragonash","Dreadfield","Dry River","Duskwallow","Ebonwood","Eternal Fire","Eternal Sorrow","Evil Eye","Extinct Park","Extinction Grove","Fallen Oak","Fireside","Fireview","Forgotten","Forsaken","Foulvale","Furyvale","Gargoyle","Ghost Town","Gloomview","Grim Garden","Grim Reaper","Grimview","Grimwood","Guilty Vale","Hallowgate","Haunted","Haunted Woods","Hollow Gardens","Hollowvale","Immortal Fire","Imp Forest","Infamy","Infernal Grove","Inferno","Lost Soul","Maleficent","Malevolent Garden","Malign","Misery Field","Mortified Grove","Murkwood","Necropolis","Nefarious Grove","Nefarious Hill","Nemesis","Netherspring","Nightmare","Nightshade","No Rest","Obsidian Grove","Obsidian Hill","Perished Grove","Plague City","Plaguewoods","Poison Spring","Reaper Garden","Rotten Grove","Rottingvale","Sanguine River","Shade","Shadow","Shadow Garden","Shadowland","Silent Gardens","Sinner Field","Sinstone","Skeletalview","Skeleton Hill","Skullside","Sombre Oak","Sorrow Pit","Sorrowwood","Soulburn","Soulriver","Spitegrove","Stiff Park","Terrorvale","Thornbush","Tragedy Grove","Tragedy Park","Twisted Oak","Unholy Oak","Venomriver","Vile Field","Vile River","Vile Spring","Vilewood","Warpwood","Wasted Forest","Wasteland","Wayward","Wicked Eye","Wicked Willow","Wicked Wood","Wickedvale","Wickedwood","Woe Garden","Wrathriver"];
var nm3 = ["Cemetery","Memorial Park","Burial Grounds","Memorial Gardens","Cemetery","Cemetery"];
var nm4 = ["Graveyard","Graveyard","Graveyard","Mausoleum","Mortuary","Necropolis","Crypts","Catacombs","Tombs"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm3.length);
			names = nm1[rnd] + " " + nm3[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm2.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			names = nm2[rnd] + " " + nm4[rnd2];
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