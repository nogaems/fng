var nm1 = ["br","cr","d","dr","g","gr","p","r","th","tr","thr"];
var nm2 = ["a","i","e","o","u"];
var nm3 = ["bl","bbl","ckl","dl","ddl","ffl","fl","gl","ggl","d","g","gg","k","l","ll","n","v","z","sn","gn","gd",,"d","g","gg","k","l","ll","n","v","z","sn","gn","gd","d","g","gg","k","l","ll","n","v","z","sn","gn","gd","dsh","lnd","lng","mdr","mgl","mpk","ndr","ngd","ngb","nkr","rgl","rnb","sdr","sgl"];
var nm4 = ["br","bl","dr","dn","fn","fd","fl","ld","ln","lm","mb","md","ml","nl","nd","rb","rl","rbr","th"];
var nm5 = ["d","g","k","lk","ld","n","nk","nks","t"];

var nm6 = ["b","cl","d","f","fl","g","gl","m","n","w"];
var nm7 = ["a","e","i","o"];
var nm8 = ["bb","bl","ch","fl","fs","fn","fm","gs","ks","ln","ls","lp","ms","mn","nl","nt","ns","nf","pf","ps","sl","sn","sm"];
var nm9 = ["ie","ey","ee","i","e","iy"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.random() * nm6.length | 0;
			rnd2 = Math.random() * nm7.length | 0
			rnd3 = Math.random() * nm8.length | 0;
			rnd4 = Math.random() * nm9.length | 0;
			names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm9[rnd4];
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0
			rnd3 = Math.random() * nm3.length | 0;
			if(rnd3 < 9){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + "e";
			}else{
				lng = Math.random() * 2 | 0;
				rnd4 = Math.random() * nm2.length | 0;
				rnd5 = Math.random() * nm5.length | 0;
				if(lng === 0){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
				}else{
					rnd6 = Math.random() * nm4.length | 0;
					rnd7 = Math.random() * nm7.length | 0;
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm7[rnd7] + nm5[rnd5];
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