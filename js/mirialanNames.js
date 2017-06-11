var nm1 = ["i","a","o","e","u","","","","","","","","","","","","","","","","","","","",""];
var nm2 = ["b","c","ch","d","f","fl","g","h","j","k","l","m","n","p","q","r","s","sh","t","v","v","w","y","z","z"];
var nm3 = ["i","a","o","e","u"];
var nm4 = ["b","c","d","f","g","h","k","l","m","n","p","q","r","s","t","v","v","w","y","z","z"];
var nm5 = ["b","c","d","f","g","h","k","l","m","n","p","q","r","s","t","v","v","w","y","z","z","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""];
var nm6 = ["i","a","o","e","u","","","","","","","","","",""];
var nm7 = ["b","c","ch","d","f","g","h","k","l","m","n","p","q","r","s","sh","t","v","v","w","y","z","z","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""];

var nm8 = ["b","c","ch","d","f","fl","g","h","i","j","k","l","m","n","p","q","r","s","sh","t","v","w","y","z"];
var nm9 = ["b","c","ch","d","f","g","h","i","k","l","m","n","p","q","r","s","sh","t","v","v","w","y","z","z","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""];
var nm10 = ["i","a","o","e","u","",""];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		rnd4 = Math.floor(Math.random() * nm4.length);
		rnd5 = Math.floor(Math.random() * nm5.length);
		rnd6 = Math.floor(Math.random() * nm6.length);
		if(tp === 1){
			rnd2 = Math.floor(Math.random() * nm8.length);
			rnd9 = Math.floor(Math.random() * nm10.length);
			rnd7 = Math.floor(Math.random() * nm9.length);
			names = nm1[rnd] + nm8[rnd2] + nm3[rnd3] + nm4[rnd4] + nm5[rnd5] + nm6[rnd6] + nm9[rnd7] + nm10[rnd9];
		}else{
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd9 = Math.floor(Math.random() * nm6.length);
			rnd7 = Math.floor(Math.random() * nm7.length);
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm5[rnd5] + nm6[rnd6] + nm7[rnd7] + nm6[rnd9];
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