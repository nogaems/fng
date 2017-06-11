var nm1 = ["","","","c","cr","g","gr","k","kr","q","qr","r","sk","skr","sq","sqr","sc","z","zr"];
var nm2 = ["a","i","e","o","u","a","i","i","a","e","e","a","i","e","o","u","a","i","i","a","e","e","ai","ee","ia","ie","oo","ua"];
var nm3 = ["ai","ee","ia","ie","oo","ua"];
var nm4 = ["b","c","cc","k","n","nn","r","rr","s","ss","shr","t","y","w"];
var nm5 = ["","","k","q","t","th","w","ww","wk"];

var nm6 = ["","","","","","c","cr","g","gh","gr","k","kh","q","qh","r","rh","sq","sc","z","zr","zh"];
var nm7 = ["a","i","e","o","u","a","i","i","a","e","e","a","i","e","o","u","a","i","i","a","e","e","ee","ea","ei","ia","ie","oo"];
var nm8 = ["ee","ea","ei","ia","ie","oo"];
var nm9 = ["b","bb","c","l","ll","n","nn","r","rr","s","ss","sh","t","y","w"];
var nm10 = ["","","","","","h","k","n","t","th","w","ww"];

var nm11 = ["","","","","","c","cr","g","gh","gr","k","kr","kh","q","qr","qh","sk","r","rh","skr","sq","sqr","sc","z","zr","zh"];
var nm12 = ["a","i","e","o","u","a","i","i","a","e","e","a","i","e","o","u","a","i","i","a","e","e","ai","ee","ea","ei","ia","ie","oo","ua"];
var nm13 = ["ai","ee","ea","ei","ia","ie","oo","ua"];
var nm14 = ["b","bb","c","cc","k","l","ll","n","nn","r","rr","s","ss","sh","shr","t","y","w"];
var nm15 = ["","","","","","h","k","n","t","th","w","ww","wk"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.random() * nm6.length | 0;
			rnd2 = Math.random() * nm8.length | 0;
			rnd3 = Math.random() * nm10.length | 0;
			if(i < 3){
				while(rnd < 5){
					rnd = Math.random() * nm6.length | 0;
				}
				while(rnd3 < 5){
					rnd3 = Math.random() * nm10.length | 0;
				}
				names = nm6[rnd] + nm8[rnd2] + nm10[rnd3];
			}else{
				rnd2 = Math.random() * nm7.length | 0;
				rnd5 = Math.random() * nm7.length | 0;
				rnd4 = Math.random() * nm9.length | 0;
				if(i < 8){
					names = nm6[rnd] + nm7[rnd2] + nm9[rnd4] + nm7[rnd5] + nm10[rnd3];
				}else{
					rnd7 = Math.random() * nm7.length | 0;
					rnd6 = Math.random() * nm9.length | 0;
					while(nm9[rnd4] === nm9[rnd6]){
						rnd6 = Math.random() * nm9.length | 0;
					}
					names = nm6[rnd] + nm7[rnd2] + nm9[rnd4] + nm7[rnd5] + nm9[rnd6] + nm7[rnd7] + nm10[rnd3];
				}
			}
		}else if(tp === 2){
			rnd = Math.random() * nm11.length | 0;
			rnd2 = Math.random() * nm13.length | 0;
			rnd3 = Math.random() * nm15.length | 0;
			if(i < 3){
				while(rnd < 5){
					rnd = Math.random() * nm11.length | 0;
				}
				while(rnd3 < 5){
					rnd3 = Math.random() * nm15.length | 0;
				}
				names = nm11[rnd] + nm13[rnd2] + nm15[rnd3];
			}else{
				rnd2 = Math.random() * nm12.length | 0;
				rnd5 = Math.random() * nm12.length | 0;
				rnd4 = Math.random() * nm14.length | 0;
				if(i < 8){
					names = nm11[rnd] + nm12[rnd2] + nm14[rnd4] + nm12[rnd5] + nm15[rnd3];
				}else{
					rnd7 = Math.random() * nm12.length | 0;
					rnd6 = Math.random() * nm14.length | 0;
					while(nm14[rnd4] === nm14[rnd6]){
						rnd6 = Math.random() * nm14.length | 0;
					}
					names = nm11[rnd] + nm12[rnd2] + nm14[rnd4] + nm12[rnd5] + nm14[rnd6] + nm12[rnd7] + nm15[rnd3];
				}
			}
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm3.length | 0;
			rnd3 = Math.random() * nm5.length | 0;
			if(i < 3){
				while(rnd < 5){
					rnd = Math.random() * nm1.length | 0;
				}
				while(rnd3 < 5){
					rnd3 = Math.random() * nm5.length | 0;
				}
				names = nm1[rnd] + nm3[rnd2] + nm5[rnd3];
			}else{
				rnd2 = Math.random() * nm2.length | 0;
				rnd5 = Math.random() * nm2.length | 0;
				rnd4 = Math.random() * nm4.length | 0;
				if(i < 8){
					names = nm1[rnd] + nm2[rnd2] + nm4[rnd4] + nm2[rnd5] + nm5[rnd3];
				}else{
					rnd7 = Math.random() * nm2.length | 0;
					rnd6 = Math.random() * nm4.length | 0;
					while(nm4[rnd4] === nm4[rnd6]){
						rnd6 = Math.random() * nm4.length | 0;
					}
					names = nm1[rnd] + nm2[rnd2] + nm4[rnd4] + nm2[rnd5] + nm4[rnd6] + nm2[rnd7] + nm5[rnd3];
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