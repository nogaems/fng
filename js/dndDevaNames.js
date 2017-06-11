var nm1 = ["Ad","Ans","Ars","Ay","Bav","Ber","Dar","Eb","Ely","Er","Ery","Gal","Gam","Gar","Hiy","Iann","Ker","Mah","Mahr","Man","Mar","Math","Mor","Nat","Neh","Ner","Ob","Or","Rah","Ron","Sam","Sav","Ser","Sor","Tar","Tav","Vat","Ver","Zach","Zay"];
var nm2 = ["ab","ach","ad","ahk","ahm","ahn","ahr","ak","al","am","an","ar","as","ath","eb","ech","ed","ehr","ek","el","em","en","er","es","iah","ihm","ihn","im","in","ir","is"];
var nm3 = ["Ab","Ad","An","Ar","Ash","Chan","Dan","Dar","Dav","Din","Elk","Eran","Eys","Han","Hav","Hen","Idr","Is","Jan","Jen","Kal","Kan","Kay","Len","Lih","Mah","Mar","Nal","Nav","Nom","Paz","Rav","Ren","Riy","Sad","Shar","Sir","Tar","Tel","Tir"];
var nm4 = ["a","ael","aen","ah","ahne","ana","anaeh","anael","anah","ane","anel","aniah","ara","araeh","are","ariah","ea","ehl","ek","el","ele","elle","era","ey","eya","i","ia","iah","im","ima"];

var nm1 = ["","","","","b","d","g","h","k","m","n","r","s","t","v","z"];
var nm2 = ["a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","a","e","i","o","ia","ie","ea","ei"];
var nm3 = ["b","ch","d","h","hr","l","ly","m","n","nn","ns","r","rs","ry","t","th","v","y"];
var nm4 = ["a","e","i"];
var nm5 = ["b","ch","d","h","hk","hm","hn","hr","k","l","m","n","r","s","th"];

var nm6 = ["","","","","","ch","d","h","j","k","l","m","n","p","r","s","sh","t","th"];
var nm7 = ["a","e","i"];
var nm8 = ["b","d","dr","h","l","lk","m","n","r","s","sh","v","y","ys","z"];
var nm9 = ["a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","a","e","i","ia","ae","ea"];
var nm10 = ["hn","l","ll","m","n","r","y"];
var nm11 = ["","","","","","","h","h","hl","k","l","l","n","n","m","m"];

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			nameFem();
			while(nMs === ""){
				nameFem();
			}
		}else{
			nameMas();
			while(nMs === ""){
				nameMas();
			}
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
function nameFem(){
	rnd = Math.floor(Math.random() * nm6.length);
	rnd2 = Math.floor(Math.random() * nm7.length);
	rnd3 = Math.floor(Math.random() * nm8.length);
	rnd4 = Math.floor(Math.random() * nm9.length);
	rnd5 = Math.floor(Math.random() * nm11.length);
	while(nm8[rnd3] === nm6[rnd] || nm8[rnd3] === nm11[rnd5]){
		rnd3 = Math.floor(Math.random() * nm8.length);
	}
	if(i < 6){
		nMs = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm9[rnd4] + nm11[rnd5];
	}else{
		rnd6 = Math.floor(Math.random() * nm10.length);
		rnd7 = Math.floor(Math.random() * nm9.length);
		while(nm10[rnd6] === nm11[rnd5] || nm10[rnd6] === nm8[rnd3]){
			rnd6 = Math.floor(Math.random() * nm10.length);
		}
		nMs = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm9[rnd4] + nm10[rnd6] + nm9[rnd7] + nm11[rnd5];
	}
	testSwear(nMs);
}

function nameMas(){
	rnd = Math.floor(Math.random() * nm1.length);
	rnd2 = Math.floor(Math.random() * nm2.length);
	rnd3 = Math.floor(Math.random() * nm3.length);
	rnd4 = Math.floor(Math.random() * nm4.length);
	rnd5 = Math.floor(Math.random() * nm5.length);
	while(nm3[rnd3] === nm1[rnd] || nm3[rnd3] === nm5[rnd5]){
		rnd3 = Math.floor(Math.random() * nm3.length);
	}
	nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm5[rnd5];
	testSwear(nMs);
}