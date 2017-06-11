var nm1 = ["","","","","","b","c","ch","d","dh","f","g","gh","j","kh","l","m","n","q","qh","r","s","th","v","x","z"];
var nm2 = ["a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","aa","oa","ua","ia","au","ao","ou"];
var nm3 = ["d","dd","dr","dl","dh","dtr","dthr","g","gh","gth","k","kk","kh","kht","l","ld","ldr","lb","lbr","lm","ln","ls","lsh","lth","lthdr","lx","m","ml","md","mdr","mn","n","nt","nth","nthr","ndr","ntr","r","rb","rd","rg","rgr","rt","rthr","rth","rl","rn","rm","t","th","thr","thdr","tr","z","zd","zdr"];
var nm4 = ["a","i","o","u","a","i","o","u","y"];
var nm5 = ["c","k","ks","q","qs","r","rs","rx","s","sc","sk","x","z"];
var nm6 = ["a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","o","o","ia","ai","ie","ee","io","ae","ea"];
var nm7 = ["","","","","","ch","cs","csh","hl","hm","hn","hx","hs","hsh","ks","ksh","ll","lm","ln","lk","lks","ls","lsh","lx","ph","r","rq","rv","s","sh","x"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		nameMas();
		while(nMs === ""){
			nameMas();
		}
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(nMs));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}

function nameMas(){
	rnd = Math.random() * nm1.length | 0;
	rnd2 = Math.random() * nm2.length | 0;
	rnd3 = Math.random() * nm7.length | 0;
	if(i < 2){
		while(nm1[rnd] === nm3[rnd3]){
			rnd3 = Math.random() * nm7.length | 0;
		}
		nMs = nm1[rnd] + nm2[rnd2] + nm7[rnd3];
	}else{
		rnd4 = Math.random() * nm3.length | 0;
		rnd5 = Math.random() * nm4.length | 0;
		if(i < 6){
			while(nm3[rnd4] === nm1[rnd] || nm3[rnd4] === nm7[rnd3]){
				rnd4 = Math.random() * nm3.length | 0;
			}
			nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm4[rnd5] + nm7[rnd3]
		}else{
			rnd6 = Math.random() * nm5.length | 0;
			rnd7 = Math.random() * nm6.length | 0;
			if(i < 9){
				while(nm5[rnd6] === nm3[rnd4] || nm5[rnd6] === nm7[rnd3]){
					rnd6 = Math.random() * nm5.length | 0;
				}
				nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm4[rnd5] + nm5[rnd6] + nm6[rnd7] + nm7[rnd3];
			}else{
				rnd8 = Math.random() * nm5.length | 0;
				rnd9 = Math.random() * nm6.length | 0;
				while(nm5[rnd8] === nm5[rnd6]){
					rnd8 = Math.random() * nm5.length | 0;
				}
				nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd4] + nm4[rnd5] + nm5[rnd6] + nm6[rnd7] + nm5[rnd8] + nm6[rnd9];
			}
		}
	}
	testSwear(nMs);
}