var nm1 = ["Al","Ari","Bil","Bri","Cal","Cor","Dav","Dor","Eni","Er","Far","Fel","Ga","Gra","His","Hor","Ian","Ipa","Je","Jor","Kas","Kel","Lan","Lo","Man","Mer","Nes","Ni","Or","Oru","Pana","Po","Qua","Quo","Ras","Ron","Sa","Sal","Sin","Tan","To","Tra","Um","Uri","Val","Vor","War","Wil","Wre","Xal","Xo","Ye","Yos","Zan","Zil"];
var nm2 = ["bar","ben","bis","corin","cryn","don","dri","fan","fiz","gim","grim","hik","him","ji","jin","kas","kur","len","lin","min","mop","morn","nan","ner","ni","pip","pos","rick","ros","rug","ryn","ser","ston","tix","tor","ver","vyn","win","wor","xif","xim","ybar","yur","ziver","zu"];
var nm3 = ["Alu","Ari","Ban","Bree","Car","Cel","Daphi","Do","Eili","El","Fae","Fen","Fol","Gal","Gren","Hel","Hes","Ina","Iso","Jel","Jo","Klo","Kri","Lil","Lori","Min","My","Ni","Ny","Oda","Or","Phi","Pri","Qi","Que","Re","Rosi","Sa","Sel","Spi","Ta","Tifa","Tri","Ufe","Uri","Ven","Vo","Wel","Wro","Xa","Xyro","Ylo","Yo","Zani","Zin"];
var nm4 = ["bi","bys","celi","ci","dira","dysa","fi","fyx","gani","gyra","hana","hani","kasys","kini","la","li","lin","lys","mila","miphi","myn","myra","na","niana","noa","nove","phina","pine","qaryn","qys","rhana","roe","sany","ssa","sys","tina","tra","wyn","wyse","xi","xis","yaris","yore","za","zyre"];

function nameGen(type){
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
	rnd = Math.floor(Math.random() * nm3.length);
	rnd2 = Math.floor(Math.random() * nm4.length);
	nMs = nm3[rnd] + nm4[rnd2];
	testSwear(nMs);
}

function nameMas(){
	rnd = Math.floor(Math.random() * nm1.length);
	rnd2 = Math.floor(Math.random() * nm2.length);
	nMs = nm1[rnd] + nm2[rnd2];
	testSwear(nMs);
}