var nm1 = ["","","","b","c","d","f","g","l","m","p","r","s","t"];
var nm2 = ["a","a","a","a","a","aa","ai","ao","ea","ei","eo","i","i","ia","io","o","o","oi","u","u","ui"];
var nm3 = ["b","bh","bhr","ch","d","dh","g","ghn","hl","l","ll","lmh","lp","lr","lt","m","mh","mhl","mhn","n","ng","ngh","nn","nnch","nngh","rd","rgh","rn","rt","s","sg","th"];
var nm4 = ["","","","bh","c","ch","d","dh","g","gh","ll","m","mh","n","nn","r","s","th"];

var nm5 = ["","","","","","b","c","d","f","fl","h","l","m","r","s","t"];
var nm6 = ["a","a","a","a","ai","e","e","e","ea","ei","eo","eu","i","i","io","iu","o","o","oi","u"];
var nm7 = ["b","bh","bl","dh","g","ghd","ghn","ghr","l","lr","m","mh","n","ng","ngh","nn","ns","r","rdr","rn","s","t","thr","tl","tr"];
var nm8 = ["","","","","","d","dh","g","l","ld","ll","n","r","s"];

var nm9 = ["","","","b","c","d","f","l","m","r","s","t"];
var nm10 = ["a","a","a","a","ai","ea","ei","eo","i","i","ia","io","o","o","oi","u"];
var nm11 = ["b","bh","d","dh","g","ghn","l","ll","lr","m","mh","n","ng","ngh","nn","rd","rn","s","t","tr"];
var nm12 = ["","","","","","d","dh","g","gh","l","ll","m","mh","n","nn","r","s","th"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.random() * nm5.length | 0;
			rnd2 = Math.random() * nm6.length | 0;
			rnd3 = Math.random() * nm8.length | 0;
			if(i < 4){
				while(rnd < 5){
					rnd = Math.random() * nm5.length | 0;
				}
				while(rnd3 < 5){
					rnd3 = Math.random() * nm8.length | 0;
				}
				names = nm5[rnd] + nm6[rnd2] + nm8[rnd3];
			}else{
				rnd4 = Math.random() * nm7.length | 0;
				rnd5 = Math.random() * nm6.length | 0;
				while(nm7[rnd4] === nm5[rnd] || nm7[rnd4] === nm8[rnd3]){
					rnd4 = Math.random() * nm7.length | 0;
				}
				if(i < 8){
					names = nm5[rnd] + nm6[rnd2] + nm7[rnd4] + nm6[rnd5] + nm8[rnd3];
				}else{
					rnd6 = Math.random() * nm7.length | 0;
					while(nm7[rnd6] === nm7[rnd4]){
						rnd6 = Math.random() * nm7.length | 0;
					}
					rnd7 = Math.random() * nm6.length | 0;
					names = nm5[rnd] + nm6[rnd2] + nm7[rnd4] + nm6[rnd5] + nm7[rnd6] + nm6[rnd7] + nm8[rnd3];
				}
			}
		}else if(tp === 2){
			rnd = Math.random() * nm9.length | 0;
			rnd2 = Math.random() * nm10.length | 0;
			rnd3 = Math.random() * nm12.length | 0;
			if(i < 4){
				while(rnd < 3){
					rnd = Math.random() * nm9.length | 0;
				}
				while(rnd3 < 5){
					rnd3 = Math.random() * nm12.length | 0;
				}
				names = nm9[rnd] + nm10[rnd2] + nm12[rnd3];
			}else{
				rnd4 = Math.random() * nm11.length | 0;
				rnd5 = Math.random() * nm10.length | 0;
				while(nm11[rnd4] === nm10[rnd] || nm11[rnd4] === nm12[rnd3]){
					rnd4 = Math.random() * nm11.length | 0;
				}
				if(i < 8){
					names = nm9[rnd] + nm10[rnd2] + nm11[rnd4] + nm10[rnd5] + nm12[rnd3];
				}else{
					rnd6 = Math.random() * nm11.length | 0;
					while(nm11[rnd6] === nm11[rnd4]){
						rnd6 = Math.random() * nm11.length | 0;
					}
					rnd7 = Math.random() * nm10.length | 0;
					names = nm9[rnd] + nm10[rnd2] + nm11[rnd4] + nm10[rnd5] + nm11[rnd6] + nm10[rnd7] + nm12[rnd3];
				}
			}
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm4.length | 0;
			if(i < 4){
				while(rnd < 5){
					rnd = Math.random() * nm1.length | 0;
				}
				while(rnd3 < 5){
					rnd3 = Math.random() * nm4.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm4[rnd3];
			}else{
				rnd4 = Math.random() * nm3.length | 0;
				rnd5 = Math.random() * nm2.length | 0;
				while(nm3[rnd4] === nm1[rnd] || nm3[rnd4] === nm4[rnd3]){
					rnd4 = Math.random() * nm3.length | 0;
				}
				if(i < 8){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm4[rnd3];
				}else{
					rnd6 = Math.random() * nm3.length | 0;
					while(nm3[rnd6] === nm3[rnd4]){
						rnd6 = Math.random() * nm3.length | 0;
					}
					rnd7 = Math.random() * nm2.length | 0;
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm3[rnd6] + nm2[rnd7] + nm4[rnd3];
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