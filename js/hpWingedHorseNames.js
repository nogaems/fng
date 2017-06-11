var nm1 = ["a","ae","ea","i","o","","","","","","","","","","","","","",""];
var nm2 = ["ba","bli","blo","bra","bri","cae","ci","cra","cro","da","do","dra","dro","fae","fo","fra","fre","glo","gra","gre","gri","la","lea","lia","lo","ma","mae","me","mea","nae","nea","nei","ni","phae","phri","pio","po","pri","ra","rae","rea","ro","she","sho","sli","sna","tae","the","tho","tri"];
var nm3 = ["ban","bian","bral","can","cian","ddan","dial","dian","din","hal","han","hian","lan","lian","lin","llan","man","mian","min","mman","nan","nial","nian","nnal","nnan","phal","phian","phion","ppan","ral","ran","rian","rin","rran","sal","san","sin","ssin","stral","tan","thian","tian","tin","tral","xal","xan","xian","xxin"];

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		names = nm1[rnd] + nm2[rnd2] + nm3[rnd3];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}