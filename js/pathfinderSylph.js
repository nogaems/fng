var nm1 = ["","","","","","c","d","f","g","h","j","l","m","n","s","v","w","z"];
var nm2 = ["a","e","i","u","a","e","i","u","a","e","i","u","a","e","i","u","a","e","i","u","aa","uu","ii"];
var nm3 = ["d","f","g","j","k","l","m","n","s","v","w","z"];
var nm4 = ["d","l","m","n","sh"];
var nm5 = ["","","","","","d","f","h","k","l","m","n","r","s","t","v","w","z"];
var nm6 = ["a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","a","a","a","ee","aa"];
var nm7 = ["d","f","ff","h","l","ll","m","mm","n","nn","s","ss","v","y","w"];
var nm8 = ["","","","","","","","","","","","","","","","","","","","","h","m","n","sh"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm5.length);
			rnd2 = Math.floor(Math.random() * nm6.length);
			rnd3 = Math.floor(Math.random() * nm7.length);
			rnd4 = Math.floor(Math.random() * nm6.length);
			if(i < 5){
				rnd5 = Math.floor(Math.random() * nm8.length);
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm8[rnd5];
			}else{
				rnd6 = Math.floor(Math.random() * nm7.length);
				rnd7 = Math.floor(Math.random() * nm6.length);
				names = nm5[rnd] + nm6[rnd2] + nm7[rnd3] + nm6[rnd4] + nm7[rnd6] + nm6[rnd7];
			}
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd5 = Math.floor(Math.random() * nm4.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
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