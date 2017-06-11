var nm1 = ["Angel","Asp","Ghost","Aspen","Avalon","Ayalon","Bay","Birr","Blitz","Blitzen","Bolt","Boomerang","Bou","Brake","Browne","Brutus","Buck","Buckeye","Buckley","Bucky","Buff","Buttons","Champion","Chantler","Charger","Chase","Chestnut","Colt","Comet","Covert","Cupid","Dancer","Dapper","Darby","Dart","Darton","Dash","Dearborn","Derland","Devin","Doc","Doe","Donner","Dot","Drummer","Edge","Elk","Elwood","Fable","Forest","Forester","Freckles","Gallop","Giggle","Grayson","Grove","Grover","Hersh","Hershel","Indy","Ivor","Jingle","John Doe","Jumbo","Juno","Knob","Knobs","Legacy","Lightning","Lockhart","Lucky","Magnum","Mahony","Midnight","Mohawk","Prancer","Quest","Ray","Rocky","Roe","Rohan","Romulus","Roscoe","Rowan","Rush","Russet","Scooter","Shade","Shadow","Silver","Sky","Snow","Solace","Spike","Spot","Springer","Sprinter","Sprite","Spruce","Spurt","Starbuck","Storm","Stormy","Sunny","Tawn","Thicket","Thunder","Timber","Titan","Umber","Ward","Weald","Willow","Wonder","Woods","Woody","Yogi"];
var nm2 = ["Aphra","Afra","Hymn","Ayala","Bambi","Fawn","Fawne","Doe","Raleigh","Hinda","Hynd","Hynda","Hynde","Luna","Willow","Lyric","Dash","Milo","Fern","Melrose","Ficus","Spryte","Lucky","Dance","Ayala","Summer","Spring","Autumn","Winter","Elain","Tabby","Tibby","Ivory","Pearl","Snow","Snowflake","Hazel","Bay","Umber","Amber","Cinnamon","Coco","Tawny","Cookie","Muffin","Beauty","Buttercup","Freckles","Spot","Speckle","Speckles","Grace","Ivy","Promise","Raidrop","Serenity","Speckles","Zoe","Dyani","Hinda","Jane Doe","Daisy","Dear","Pepper","Princess","Queen","Elli","Elkee","Vixen","Dash","Silka","Boubou","Harmony","Flower","Furball","Buttercup","Nutmeg","Aurora","Aura","Heiress","Liberty","Jasmine","Ashley","Jewel","Enigma","Toffee","Patches","Shye","Huntress","Cotton","Luna","Breeze","Breezy","Dashful","Whiskers","Nighte","Brooke","Moone","Winde","Windy","Enya","Cloude","Hope","Lace","Silk","Orchid","Lullaby","Pebbles","River","Cupcake","Mystique","Ginger","Destiny"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd];
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