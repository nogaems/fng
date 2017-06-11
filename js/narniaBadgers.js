function nameGen(type){
	var nm1 = ["acorn","almond","apple","barley","bean","beet","beetroot","berry","bloom","bulb","button","carrot","cherry","corn","cress","crop","earthnut","fig","fruit","fungi","fungus","gourd","grain","grape","honey","jalap","kernel","maize","melon","morel","mushroom","nectar","oat","okra","onion","orange","parsnip","peach","peanut","pear","pecan","peel","plum","plume","pod","poppet","potato","prune","pulp","pumpkin","radish","root","rye","salep","sapling","shoot","spice","sprout","spud","squash","stalk","sugar","sugarbeet","taro","tater","toadstool","tomato","truffle","tuber","turnip","vine","walnut","yam"];
	var nm2 = ["baker","belcher","biter","boiler","bringer","browser","bundler","burper","burrower","catcher","chaser","chopper","collector","cooker","counter","devourer","digger","diner","diver","dreamer","drooler","dropper","dunker","feeder","feeler","finder","fryer","gatherer","groomer","grower","guard","helper","hider","hoarder","hogger","holder","hunter","keeper","lover","masher","picker","planter","plucker","reacher","remover","rester","robber","savorer","scooper","scourer","seeker","shaker","shuffler","snatcher","sniffer","snooper","spotter","stacker","stasher","stealer","stocker","taker","taster","tender","tracker","washer"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0;
		while(nm1[rnd] === nm2[rnd2]){
			rnd2 = Math.random() * nm2.length | 0;
		}
		names = nm1[rnd] + nm2[rnd2];
		nm1.splice(rnd, 1);
		nm2.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}