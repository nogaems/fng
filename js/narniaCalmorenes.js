var nm1 = ["","","","","","c","chl","d","g","gh","h","k","kh","m","n","r","v","z"];
var nm2 = ["a","e","i","o","u"];
var nm3 = ["b","br","dr","h","l","lg","lls","ld","lb","ldr","lbr","m","ml","nr","ng","nm","nsh","r","rph","rr","rd","rsh","rs","rb","shd","sd","sh","shb","sb","sht","x","zr","b","h","l","m","r","s"];
var nm4 = ["b","d","l","ld","lb","m","mbr","mb","n","nd","ndr","nt","ntr","nth","rt","rd","rg","rth","sht","st","sh"];
var nm5 = ["","","","","","b","d","h","m","n","s","sh","t","th"];

var nm6 = ["","","","","","d","f","h","l","m","n","ph","s","v","z"];
var nm7 = ["a","i","o","a","i","o","a","i","o","a","i","o","a","i","o","a","i","o","ee","ei","aa"];
var nm8 = ["d","h","l","ln","lm","m","n","r","rd","s","v","z"];
var nm9 = ["d","h","l","m","n","r","rd","sh","v","z"];
var nm10 = ["h","l","m","n","s","v","w","y","z"];
var nm11 = ["h","n","s","sh","th","h","n","s","sh","th","v","z"];

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
			rnd5 = Math.random() * nm11.length | 0;
			while(nm8[rnd3] === nm6[rnd] || nm8[rnd3] === nm11[rnd5]){
				rnd3 = Math.random() * nm8.length | 0;
			}
			if(i < 4){
				names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm11[rnd5];
			}else{
				rnd6 = Math.random() * nm9.length | 0;
				rnd7 = Math.random() * nm7.length | 0;
				while(nm9[rnd6] === nm8[rnd3]){
					rnd6 = Math.random() * nm9.length | 0;
				}
				if(i < 7){
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd6] + nm7[rnd7] + nm11[rnd5];
				}else{
					rnd8 = Math.random() * nm10.length | 0;
					rnd9 = Math.random() * nm7.length | 0;
					while(nm9[rnd6] === nm10[rnd8]){
						rnd8 = Math.random() * nm10.length | 0;
					}
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd6] + nm7[rnd7] + nm10[rnd8] + nm7[rnd9] + nm11[rnd5];
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
			if(i < 5){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5];
			}else{
				rnd6 = Math.random() * nm4.length | 0;
				rnd7 = Math.random() * nm2.length | 0;
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