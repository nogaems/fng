var nm1 = ["","","","b","c","d","g","l","m","n","r","s","sh","tr"];
var nm2 = ["a","o","u"];
var nm3 = ["b","br","d","dr","l","ll","lv","m","n","t","r","rr"];
var nm4 = ["e","i"];
var nm5 = ["","","","l","m","n","r"];

var nm6 = ["","","","","","b","f","h","l","m","n","r","t"];
var nm7 = ["a","i","a","i","a","i","e","e","o"];
var nm8 = ["d","g","h","l","m","n","r","t"];
var nm9 = ["l","m","n","r","t","v"];
var nm10 = ["ln","m","mn","n","nn","ph","rn","s","sh","t","th"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.random() * nm6.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			rnd3 = Math.random() * nm10.length | 0;
			if(i < 4){
				while(rnd < 5){
					rnd = Math.random() * nm6.length | 0;
				}
				names = nm6[rnd] + nm7[rnd2] + nm10[rnd3];
			}else{
				rnd4 = Math.random() * nm8.length | 0;
				rnd5 = Math.random() * nm7.length | 0;
				if(i < 7){
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd4] + nm7[rnd5] + nm10[rnd3];
				}else{
					rnd6 = Math.random() * nm9.length | 0;
					rnd7 = Math.random() * nm7.length | 0;
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd4] + nm7[rnd5] + nm9[rnd6] + nm7[rnd7] + nm10[rnd3];
				}
			}
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm5.length | 0;
			if(i < 5){
				while(rnd < 3){
					rnd = Math.random() * nm1.length | 0;
				}
				if(rnd3 < 3){
					rnd3 = rnd3 + 3;
				}
				names = nm1[rnd] + nm2[rnd2] + nm5[rnd3];
			}else{
				rnd4 = Math.random() * nm3.length | 0;
				rnd5 = Math.random() * nm4.length | 0;
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm4[rnd5] + nm5[rnd3];
			}
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