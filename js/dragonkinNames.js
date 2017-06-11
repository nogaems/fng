var nm1 = ["","","","","","b","br","dr","g","gr","h","k","kr","m","n","r","s","sr","str","t","tr","v","z"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ai","ae","ia","iu","io","eo"];
var nm3 = ["cr","cg","cn","csh","cd","cdr","dr","dg","dgr","dk","dkr","k","kr","kt","kth","ksh","l","lk","lt","ldr","lg","lgr","lsh","lz","n","nd","ndr","nsh","nsk","r","rc","rph","rsh","rth","rd","rdr","rgr","rg","rz","rzr","rsh","s","sth","shk","sk","sg","skr","th","tr","tr","tg","z","zz","zg","zk"];
var nm4 = ["b","d","g","j","k","l","n","r","s","sh","z"];
var nm5 = ["","","","c","d","g","gg","k","ks","n","nd","ph","s","th","x","z"];

var nm6 = ["","","","","","","","","","","b","bh","c","ch","d","g","h","kh","l","m","n","ph","phr","r","s","shr","str","sth","t","th","tr","z","zh"];
var nm7 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ai","ae","ia","ea","ie","ei"];
var nm8 = ["dr","dh","dn","dhr","gn","gr","ghr","gtr","gt","k","kk","kh","kt","kth","l","lk","ll","lg","ld","ldr","lgr","ln","lm","lkh","ls","lz","n","nd","ndh","ndr","ns","nsh","nz","nh","nhr","ng","ngh","r","rc","rph","rsh","rz","rl","s","sh","ss","sth","sht","shl","sn","sg","sk","th","thr","thn","tr","z","zh"];
var nm9 = ["l","m","n","r","s","sh","t","th","x","z"];
var nm10 = ["","","","","","","","","","","h","s","sh","th","x","z"];

var nm11 = ["","","","","","","","b","ch","d","g","h","k","kr","l","m","n","r","s","sr","str","sth","t","tr","th","z"];
var nm12 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","ai","ae","ia","ea","io","ie"];
var nm13 = ["cr","cn","cd","dr","dh","dg","dhr","gn","gr","ghr","k","kk","kt","kth","l","lk","ll","lg","ld","ldr","lgr","lz","n","nd","ndr","ns","nsh","nz","ng","r","rc","rph","rsh","rz","rd","rdr","rgr","rg","s","sh","ss","sth","sht","sth","sn","sg","sk","th","thr","tr","z","zg","zh"];
var nm14 = ["b","d","g","l","n","r","s","sh","t","th","z"];
var nm15 = ["","","","h","n","s","sh","t","th","x","z"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm6.length);
			rnd2 = Math.floor(Math.random() * nm7.length);
			rnd3 = Math.floor(Math.random() * nm8.length);
			rnd4 = Math.floor(Math.random() * nm7.length);
			rnd5 = Math.floor(Math.random() * nm10.length);
			while(nm8[rnd3] === nm6[rnd] || nm8[rnd3] === nm10[rnd5]){
				rnd3 = Math.floor(Math.random() * nm8.length);
			}
			if(i < 6){
				names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm10[rnd5];
			}else{
				rnd6 = Math.floor(Math.random() * nm9.length);
				rnd7 = Math.floor(Math.random() * nm7.length);
				while(nm8[rnd3] === nm9[rnd6] || nm9[rnd6] === nm10[rnd5]){
					rnd6 = Math.floor(Math.random() * nm9.length);
				}
				if(i < 8){
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd6] + nm7[rnd7] + nm10[rnd5];
				}else{
					names = nm6[rnd] + nm7[rnd2] + nm9[rnd6] + nm7[rnd7] + nm8[rnd3] + nm7[rnd4] + nm10[rnd5];
				}
			}
		}else if(tp === 2){
			rnd = Math.floor(Math.random() * nm11.length);
			rnd2 = Math.floor(Math.random() * nm12.length);
			rnd3 = Math.floor(Math.random() * nm13.length);
			rnd4 = Math.floor(Math.random() * nm12.length);
			rnd5 = Math.floor(Math.random() * nm15.length);
			while(nm13[rnd3] === nm11[rnd] || nm13[rnd3] === nm15[rnd5]){
				rnd3 = Math.floor(Math.random() * nm13.length);
			}
			if(i < 6){
				names = nm11[rnd] + nm12[rnd2] + nm13[rnd3] + nm12[rnd4] + nm15[rnd5];
			}else{
				rnd6 = Math.floor(Math.random() * nm14.length);
				rnd7 = Math.floor(Math.random() * nm12.length);
				while(nm13[rnd3] === nm14[rnd6] || nm14[rnd6] === nm15[rnd5]){
					rnd6 = Math.floor(Math.random() * nm14.length);
				}
				if(i < 8){
					names = nm11[rnd] + nm12[rnd2] + nm13[rnd3] + nm12[rnd4] + nm14[rnd6] + nm12[rnd7] + nm15[rnd5];
				}else{
					names = nm11[rnd] + nm12[rnd2] + nm14[rnd6] + nm12[rnd7] + nm13[rnd3] + nm12[rnd4] + nm15[rnd5];
				}
			}
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			rnd5 = Math.floor(Math.random() * nm5.length);
			while(nm3[rnd3] === nm1[rnd] || nm3[rnd3] === nm5[rnd5]){
				rnd3 = Math.floor(Math.random() * nm3.length);
			}
			if(i < 6){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
			}else{
				rnd6 = Math.floor(Math.random() * nm4.length);
				rnd7 = Math.floor(Math.random() * nm2.length);
				while(nm3[rnd3] === nm4[rnd6] || nm4[rnd6] === nm5[rnd5]){
					rnd6 = Math.floor(Math.random() * nm4.length);
				}
				if(i < 8){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
				}else{
					names = nm1[rnd] + nm2[rnd2] + nm4[rnd6] + nm2[rnd7] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
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