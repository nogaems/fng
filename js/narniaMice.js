var nm1 = ["b","ch","d","h","k","l","m","n","r","p","t","s","z"];
var nm2 = ["c","ch","d","j","k","m","n","t"];
var nm3 = ["k","p","t"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0
		rnd3 = Math.random() * nm3.length | 0;
		names = nm1[rnd] + "eepi" + nm2[rnd2] + "ee" + nm3[rnd3];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}