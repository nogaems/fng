var nm1 = [""];
var nm2 = ["ka","ki","ku","ke","ko","sa","si","su","se","so","sha","shi","shu","she","sho","ta","ti","tu","te","to","tha","thi","thu","the","tho","dra","dri","dru","dre","dro","ma","mi","mu","me","mo","na","ni","nu","ne","no","ha","hi","hu","he","ho","fa","fi","fu","fe","fo","ra","ri","ru","re","ro","la","li","lu","le","lo","ya","yi","yu","ye","yo"];
var nm3 = ["n","l","t","k","s","","","","","","","","","","","",""];
var nm4 = ["ka","ki","ku","ke","ko","sa","si","su","se","so","ta","ti","tu","te","to","ma","mi","mu","me","mo","na","ni","nu","ne","no","ha","hi","hu","he","ho","fa","fi","fu","fe","fo","ra","ri","ru","re","ro","la","li","lu","le","lo","ya","yi","yu","ye","yo"];
var nm5 = ["n","l","t","k","s","h","m","","","","","","","","","","","",""];
var nm6 = ["a","e","i","o","u"];
var nm7 = ["n","l","t","k","s"];

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	if(tp === 1){
		nm1 = ["a","e","i","o","u"];
	}else{
		nm1 = [""];
	}
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		rnd4 = Math.floor(Math.random() * nm4.length);
		rnd5 = Math.floor(Math.random() * nm5.length);
		rnd6 = Math.floor(Math.random() * nm2.length);
		rnd7 = Math.floor(Math.random() * nm6.length);
		rnd8 = Math.floor(Math.random() * nm7.length);
		names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm5[rnd5] + " " + nm2[rnd6] + nm6[rnd7] + nm7[rnd8];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}