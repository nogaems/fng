var nm1 = ["b","c","d","g","gl","gr","m","n","r","rh","s","sc"];
var nm2 = ["a","e","i","o","u"];
var nm3 = ["cn","ct","g","gt","gr","gn","l","lp","lv","lt","nd","nn","nv","p","r","rg","rl","rs","rt","sp","st","sn","thl","th","tr","tv","v","vr","vl","z"];
var nm4 = ["g","l","ll","m","n","r","s"];
var nm5 = ["","","","d","m","n","r","rn","s","z"];

var nm6 = ["b","br","d","dr","h","l","m","n","pr","s","t","tr"];
var nm7 = ["a","e","i","u"];
var nm8 = ["d","l","ll","m","n","nn","r","rr","s","ss","v","y","z"];
var nm9 = ["dn","dl","fn","fl","ffl","gn","gl","gs","ll","ln","lm","ls","ml","mml","nl","nnl","ns","sm","sl","ssl","sn","zl","zn","zzl"];
var nm10 = ["e","i","ia","ea","ei"];

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
			rnd3 = Math.random() * nm9.length | 0;
			rnd4 = Math.random() * nm10.length | 0;
			if(i < 6){
				names = nm6[rnd] + nm7[rnd2] + nm9[rnd3] + nm10[rnd4];
			}else{
				rnd5 = Math.random() * nm6.length | 0;
				rnd6 = Math.random() * nm7.length | 0;
				rnd7 = Math.random() * nm8.length | 0;
				rnd8 = Math.random() * nm7.length | 0;
				if(i < 7){
					names = nm6[rnd] + nm7[rnd2] + nm9[rnd3] + nm7[rnd8] + nm6[rnd5] + nm7[rnd6] + nm8[rnd7] + nm10[rnd4];
				}else{
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd7] + nm7[rnd8] + nm6[rnd5] + nm7[rnd6] + nm9[rnd3] + nm10[rnd4];
				}
			}
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm3.length | 0;
			rnd4 = Math.random() * nm2.length | 0;
			rnd5 = Math.random() * nm5.length | 0;
			while(nm3[rnd3] === nm5[rnd5] || nm3[rnd3] === nm1[rnd]){
				rnd3 = Math.random() * nm3.length | 0;
			}
			if(i < 4){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
			}else{
				rnd6 = Math.random() * nm4.length | 0;
				rnd7 = Math.random() * nm2.length | 0;
				if(i < 7){
					names = nm1[rnd] + nm2[rnd2] + nm4[rnd6] + nm2[rnd7] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
				}else{
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
				}
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