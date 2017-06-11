var nm1 = ["","","","","b","br","c","d","f","g","l","m","n","p","r","s","t"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","aoi","ai","ea","á","ó","í","ú","á","ó","í","ú","éi","ói","éa","eá","aoi","ao","ío","eò"];
var nm3 = ["bb","bh","bhn","c","cc","ch","chl","d","dbh","dh","dhl","g","gh","gn","l","lb","lbh","ll","lp","lt","m","mh","mhl","mhr","n","nbh","nd","ndr","nf","ng","ngh","nl","nm","nmch","nn","nndr","nnl","nr","nt","r","rbh","rch","rd","rdg","rdgh","rh","rn","rr","rt","rth","s","sd","sg","st","t","th","thgh"];
var nm4 = ["bh","ch","cht","d","dh","g","gh","l","lg","ll","lm","lt","m","mh","mhn","mn","mth","n","nn","r","rr","rt","sd","sl","st","th"];
var nm5 = ["","","","","","bh","ch","cht","d","dh","gh","l","ll","m","mh","n","nn","r","rd","rt","s"];

var nm6 = ["","","","","","","b","bl","br","c","d","f","l","m","n","r","s","t"];
var nm7 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","á","é","í","ì","ó","á","é","í","ì","ó","ái","ói","aí","ìo","ío","úa","úi","ea","ei","io","ia","ai","ua","aoi"];
var nm8 = ["b","bh","bhgr","bhl","bhn","ch","chn","d","dhn","f","ffr","g","gh","ghd","ghn","gs","l","lbh","ll","lm","lmh","m","mh","mhn","mn","mphn","ms","n","nbh","ng","nn","nnl","nt","phn","r","rb","rbh","rch","rdr","rl","rn","sl","st","str","t","thch","thn","thr","tr"];
var nm9 = ["b","bhl","bl","g","gh","l","m","mh","mhn","n","ngh","r","rg","rn","s","str"];
var nm10 = ["","","","","","","","","l","ll","n","ng","nn","r","s","sh","th"];

var nm11 = ["","","","","b","br","c","d","f","l","m","n","r","s","t"];
var nm12 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","á","ó","í","á","ó","í","é","é","aoi","ai","ea","ói","ío","ái","úi","éa","eá"];
var nm13 = ["bh","bhn","ch","d","dh","dhn","g","gh","gn","l","lb","lbh","ll","m","mh","mhn","mhl","n","nbh","nd","nf","ng","ngh","nl","nm","nn","nnl","nr","nt","r","rb","rch","rd","rdr","rn","s","sd","st","t","th"];
var nm14 = ["bh","bhl","g","gh","l","ll","lm","m","mh","mhn","mn","n","nn","r","rr","s","sd","sl","st","th"];
var nm15 = ["","","","","","l","ll","m","mh","n","nn","r","rd","rt","s","sh","th"];

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
			if(i < 3){
				while(rnd < 6){
					rnd = Math.random() * nm6.length | 0;
				}
				while(rnd3 < 8){
					rnd3 = Math.random() * nm10.length | 0;
				}
				names = nm6[rnd] + nm7[rnd2] + nm10[rnd3];
			}else{
				rnd4 = Math.random() * nm8.length | 0;
				while(nm8[rnd4] === nm6[rnd]){
					rnd4 = Math.random() * nm8.length | 0;
				}
				while(nm8[rnd4] === nm10[rnd3]){
					rnd3 = Math.random() * nm10.length | 0;
				}
				rnd5 = Math.random() * nm7.length | 0;
				if(i < 7){
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd4] + nm7[rnd5] + nm10[rnd3];
				}else{
					rnd6 = Math.random() * nm9.length | 0;
					while(nm9[rnd6] === nm10[rnd3] || nm9[rnd6] === nm8[rnd4]){
						rnd6 = Math.random() * nm9.length | 0;
					}
					rnd7 = Math.random() * nm7.length | 0;
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd4] + nm7[rnd5] + nm9[rnd6] + nm7[rnd7] + nm10[rnd3];
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
				while(rnd3 < 5){
					rnd3 = Math.random() * nm15.length | 0;
				}
				names = nm11[rnd] + nm12[rnd2] + nm15[rnd3];
			}else{
				rnd4 = Math.random() * nm13.length | 0;
				while(nm13[rnd4] === nm11[rnd]){
					rnd4 = Math.random() * nm13.length | 0;
				}
				while(nm13[rnd4] === nm15[rnd3]){
					rnd3 = Math.random() * nm15.length | 0;
				}
				rnd5 = Math.random() * nm12.length | 0;
				if(i < 7){
					names = nm11[rnd] + nm12[rnd2] + nm13[rnd4] + nm12[rnd5] + nm15[rnd3];
				}else{
					rnd6 = Math.random() * nm14.length | 0;
					while(nm14[rnd6] === nm15[rnd3] || nm14[rnd6] === nm13[rnd4]){
						rnd6 = Math.random() * nm14.length | 0;
					}
					rnd7 = Math.random() * nm12.length | 0;
					names = nm11[rnd] + nm12[rnd2] + nm13[rnd4] + nm12[rnd5] + nm14[rnd6] + nm12[rnd7] + nm15[rnd3];
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
				while(rnd3 < 5){
					rnd3 = Math.random() * nm5.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm5[rnd3];
			}else{
				rnd4 = Math.random() * nm3.length | 0;
				while(nm3[rnd4] === nm1[rnd]){
					rnd4 = Math.random() * nm3.length | 0;
				}
				while(nm3[rnd4] === nm5[rnd3]){
					rnd3 = Math.random() * nm5.length | 0;
				}
				rnd5 = Math.random() * nm2.length | 0;
				if(i < 7){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm5[rnd3];
				}else{
					rnd6 = Math.random() * nm4.length | 0;
					while(nm4[rnd6] === nm5[rnd3] || nm4[rnd6] === nm3[rnd4]){
						rnd6 = Math.random() * nm4.length | 0;
					}
					rnd7 = Math.random() * nm2.length | 0;
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm2[rnd5] + nm4[rnd6] + nm2[rnd7] + nm5[rnd3];
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