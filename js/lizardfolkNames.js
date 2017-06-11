var nm1 = ["","","","","bh","br","ch","dr","g","gr","j","k","kr","q","qr","r","rh","th","thr","tr","v","y","z"];
var nm2 = ["a","i","o","u","a","i","o","u","a","i","o","u","a","i","o","u","a","i","o","u","a","i","o","u","a","i","o","u","a","i","o","u","a","i","o","u","a","i","o","u","ao","au","ou","iu","oa","ua","uu"];
var nm3 = ["g","gr","h","j","k","kz","kx","kn","lt","ll","m","mz","nt","nj","r","rq","rs","rz","rn","rl","sh","sz","shr","szr","t","tt","th","tr","thr","tz","tsz","tl","x","xl","z","zz"];
var nm4 = ["c","cc","ch","g","j","k","kk","q","x","xx","z"];
var nm5 = ["","","","k","sz","sk","shk","t","x","xl","z","zk"];

var nm6 = ["","","","","","","b","cr","ch","d","dh","dr","h","j","k","kh","kr","q","r","rh","s","sh","sr","shr","th","thr","y","z"];
var nm7 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","ae","ie","ia","ei"];
var nm8 = ["c","cc","ch","d","dr","g","gn","gz","gy","k","kk","kr","kz","kl","kn","lq","lz","n","nq","nr","nz","r","rs","rq","rt","rz","rsh","rzh","t","tt","th","thr","thl","tl","z","zd"];
var nm9 = ["c","j","k","q","r","s","t","x","y","z"];
var nm10 = ["","","","","h","s","sk","ss","x","z"];

var nm11 = ["","","","","","b","ch","d","dr","j","k","kh","kr","q","r","rh","sr","shr","th","thr","y","z"];
var nm12 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","u","u","u","ae","ia","ao","au","ou","oa"];
var nm13 = ["g","gr","k","kk","kz","kl","kn","lz","r","rs","rq","rt","rz","t","tt","th","thr","tl","z","zd"];
var nm14 = ["c","j","k","q","r","t","x","z"];
var nm15 = ["","","","","s","sk","ss","x","xl","z"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.random() * nm3.length | 0;
		if(tp === 1){
			rnd = Math.random() * nm6.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			rnd3 = Math.random() * nm10.length | 0;
			if(i < 3){
				while(rnd < 6){
					rnd = Math.random() * nm6.length | 0;
				}
				while(rnd3 < 4){
					rnd3 = Math.random() * nm10.length | 0;
				}
				names = nm6[rnd] + nm7[rnd2] + nm10[rnd3];
			}else if(i < 6){
				rnd4 = Math.random() * nm7.length | 0;
				rnd5 = Math.random() * nm8.length | 0;
				while(nm10[rnd3] === nm8[rnd5]){
					rnd5 = Math.random() * nm8.length | 0;
				}
				names = nm6[rnd] + nm7[rnd2] + nm8[rnd5] + nm7[rnd4] + nm10[rnd3];
			}else{
				rnd4 = Math.random() * nm7.length | 0;
				rnd5 = Math.random() * nm8.length | 0;
				rnd6 = Math.random() * nm7.length | 0;
				rnd7 = Math.random() * nm9.length | 0;
				while(nm10[rnd3] === nm8[rnd5]){
					rnd5 = Math.random() * nm8.length | 0;
				}
				while(nm9[rnd7] === nm8[rnd5]){
					rnd7 = Math.random() * nm9.length | 0;
				}
				if(i < 8){
					names = nm6[rnd7] + nm7[rnd2] + nm9[rnd7] + nm7[rnd4] + nm8[rnd5] + nm7[rnd6] + nm10[rnd3];
				}else{
					names = nm6[rnd7] + nm7[rnd4] + nm8[rnd5] + nm7[rnd2] + nm9[rnd7] + nm7[rnd6] + nm10[rnd3];
				}
			}
		}else if(tp === 2){
			rnd = Math.random() * nm11.length | 0;
			rnd2 = Math.random() * nm12.length | 0;
			rnd3 = Math.random() * nm15.length | 0;
			if(i < 3){
				while(rnd < 4){
					rnd = Math.random() * nm11.length | 0;
				}
				while(rnd3 < 4){
					rnd3 = Math.random() * nm15.length | 0;
				}
				names = nm11[rnd] + nm12[rnd2] + nm15[rnd3];
			}else if(i < 6){
				rnd4 = Math.random() * nm12.length | 0;
				rnd5 = Math.random() * nm13.length | 0;
				while(nm12[rnd3] === nm13[rnd5]){
					rnd5 = Math.random() * nm13.length | 0;
				}
				names = nm11[rnd] + nm12[rnd2] + nm13[rnd5] + nm12[rnd4] + nm15[rnd3];
			}else{
				rnd4 = Math.random() * nm12.length | 0;
				rnd5 = Math.random() * nm13.length | 0;
				rnd6 = Math.random() * nm12.length | 0;
				rnd7 = Math.random() * nm14.length | 0;
				while(nm15[rnd3] === nm13[rnd5]){
					rnd5 = Math.random() * nm13.length | 0;
				}
				while(nm14[rnd7] === nm13[rnd5]){
					rnd7 = Math.random() * nm14.length | 0;
				}
				if(i < 8){
					names = nm11[rnd7] + nm12[rnd2] + nm14[rnd7] + nm12[rnd4] + nm13[rnd5] + nm12[rnd6] + nm15[rnd3];
				}else{
					names = nm11[rnd7] + nm12[rnd4] + nm13[rnd5] + nm12[rnd2] + nm14[rnd7] + nm12[rnd6] + nm15[rnd3];
				}
			}
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm5.length | 0;
			if(i < 3){
				while(rnd < 4){
					rnd = Math.random() * nm1.length | 0;
				}
				while(rnd3 < 3){
					rnd3 = Math.random() * nm5.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm5[rnd3];
			}else if(i < 6){
				rnd4 = Math.random() * nm2.length | 0;
				rnd5 = Math.random() * nm3.length | 0;
				while(nm2[rnd3] === nm3[rnd5]){
					rnd5 = Math.random() * nm3.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd5] + nm2[rnd4] + nm5[rnd3];
			}else{
				rnd4 = Math.random() * nm2.length | 0;
				rnd5 = Math.random() * nm3.length | 0;
				rnd6 = Math.random() * nm2.length | 0;
				rnd7 = Math.random() * nm4.length | 0;
				while(nm5[rnd3] === nm3[rnd5]){
					rnd5 = Math.random() * nm3.length | 0;
				}
				while(nm4[rnd7] === nm3[rnd5]){
					rnd7 = Math.random() * nm4.length | 0;
				}
				if(i < 8){
					names = nm1[rnd7] + nm2[rnd2] + nm4[rnd7] + nm2[rnd4] + nm3[rnd5] + nm2[rnd6] + nm5[rnd3];
				}else{
					names = nm1[rnd7] + nm2[rnd4] + nm3[rnd5] + nm2[rnd2] + nm4[rnd7] + nm2[rnd6] + nm5[rnd3];
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