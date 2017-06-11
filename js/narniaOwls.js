var nm2 = ["beak","belly","bill","breast","claw","crest","crown","eye","eyes","feather","head","mantle","plume","tail","talon","wing","wings"];

function nameGen(type){
	var nm1 = ["arch","band","beam","bell","bend","bleak","bold","brash","brass","cave","cloud","clue","cold","cream","dark","dawn","dim","dirt","dive","draft","dusk","dust","edge","fan","flame","flight","flock","flow","fluke","fog","force","frost","ghost","gift","glass","glim","glint","gloom","glow","glum","gold","grace","grand","great","grim","hex","high","hook","ice","ink","iron","light","lock","lone","long","loud","lush","mad","mass","mist","moon","mud","murk","night","pale","perk","phantom","phase","plume","plump","prime","quick","quill","rain","rash","shade","shadow","silk","silver","sky","slim","smoke","soot","spirit","spite","spot","star","steel","storm","stout","sun","thick","thorn","thrift","thunder","tranquil","trim","veil","vex","wild","woe"];

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
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}