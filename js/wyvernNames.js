var nm1 = ["","","","","","","br","c","cr","ch","dr","g","gr","j","k","kr","n","q","r","t","tr","x","v","z"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ai","au","ei","ia","ua","uu","aa","ui"];
var nm3 = ["dj","dg","dr","gr","gz","j","k","kk","kt","kg","kz","ndr","nz","ng","ngr","nn","q","qq","qr","r","rd","rg","rr","rq","rv","rch","sq","t","tr","tz","v","vr","z","zz"];
var nm4 = ["c","cc","cr","d","g","gr","k","kk","kr","n","nd","ndr","q","r","rr","sq","t","z","zz"];
var nm5 = ["","c","d","g","k","n","q","t","x","z"];

var nm6 = ["","","","","bh","c","ch","dr","g","gn","gh","h","k","kn","kh","khr","n","q","r","rh","t","th","thr","x","v","z"];
var nm7 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ai","ao","ei","ia","ue","ua","aa","ae"];
var nm8 = ["dd","dt","dr","g","gn","hr","hn","k","kk","kn","kr","kh","nd","nz","ng","nn","nq","q","qq","qh","qr","r","rz","rg","rr","rq","rv","rch","rh","sq","sh","t","th","v","vr","z","zz"];
var nm9 = ["c","cc","ch","d","dh","g","k","kk","kh","n","nd","nz","q","r","rr","sh","t","z","zz"];
var nm10 = ["","","","c","d","h","n","q","s","t","th"];

var nm11 = ["","","","","","b","c","ch","dr","g","gn","gr","k","kr","n","q","r","t","tr","x","v","z"];
var nm12 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ai","ao","ei","ia","ue","ua","aa","ui"];
var nm13 = ["d","dd","dr","g","k","kk","kr","kg","nd","ndr","nz","ng","nn","q","qq","qr","r","rh","rq","rr","rz","rv","sq","t","tr","th","v","vr","z","zz"];
var nm14 = ["c","cc","ch","d","g","k","kk","kh","n","nd","q","r","rr","s","ss","t","z","z"];
var nm15 = ["","","c","d","g","k","n","s","q","t"];

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
			rnd3 = Math.random() * nm8.length | 0;
			rnd4 = Math.random() * nm7.length | 0;
			rnd5 = Math.random() * nm10.length | 0;
			while(nm6[rnd] === nm8[rnd3]){
				rnd3 = Math.random() * nm8.length | 0;
			}
			while(nm10[rnd5] === nm8[rnd3]){
				rnd5 = Math.random() * nm10.length | 0;
			}
			if(i < 7){
				names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm10[rnd5];
			}else{
				rnd6 = Math.random() * nm9.length | 0;
				rnd7 = Math.random() * nm7.length | 0;
				while(nm9[rnd6] === nm8[rnd3]){
					rnd6 = Math.random() * nm9.length | 0;
				}
				names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd6] + nm7[rnd7] + nm10[rnd5];
			}
		}else if(tp === 2){
			rnd = Math.random() * nm11.length | 0;
			rnd2 = Math.random() * nm12.length | 0;
			rnd3 = Math.random() * nm13.length | 0;
			rnd4 = Math.random() * nm12.length | 0;
			rnd5 = Math.random() * nm15.length | 0;
			while(nm11[rnd] === nm13[rnd3]){
				rnd3 = Math.random() * nm13.length | 0;
			}
			while(nm15[rnd5] === nm13[rnd3]){
				rnd5 = Math.random() * nm15.length | 0;
			}
			if(i < 7){
				names = nm11[rnd] + nm12[rnd2] + nm13[rnd3] + nm12[rnd4] + nm15[rnd5];
			}else{
				rnd6 = Math.random() * nm14.length | 0;
				rnd7 = Math.random() * nm12.length | 0;
				while(nm14[rnd6] === nm13[rnd3]){
					rnd6 = Math.random() * nm14.length | 0;
				}
				names = nm11[rnd] + nm12[rnd2] + nm13[rnd3] + nm12[rnd4] + nm14[rnd6] + nm12[rnd7] + nm15[rnd5];
			}
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm3.length | 0;
			rnd4 = Math.random() * nm2.length | 0;
			rnd5 = Math.random() * nm5.length | 0;
			while(nm1[rnd] === nm3[rnd3]){
				rnd3 = Math.random() * nm3.length | 0;
			}
			while(nm5[rnd5] === nm3[rnd3]){
				rnd5 = Math.random() * nm5.length | 0;
			}
			if(i < 7){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
			}else{
				rnd6 = Math.random() * nm4.length | 0;
				rnd7 = Math.random() * nm2.length | 0;
				while(nm4[rnd6] === nm3[rnd3]){
					rnd6 = Math.random() * nm4.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
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