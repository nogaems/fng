var nm1 = ["Ag","Agg","Ar","Arn","As","At","Atr","B","Bar","Bel","Bor","Br","Brak","C","Cr","D","Dor","Dr","Dur","G","Gal","Gan","Gar","Gna","Gor","Got","Gr","Gram","Grim","Grom","Grum","Gul","H","Hag","Han","Har","Hog","Hon","Hor","Hun","Hur","K","Kal","Kam","Kar","Kel","Kil","Kom","Kor","Kra","Kru","Kul","Kur","Lum","M","Mag","Mahl","Mak","Mal","Mar","Mog","Mok","Mor","Mug","Muk","Mura","N","Oggu","Ogu","Ok","Oll","Or","Rek","Ren","Ron","Rona","S","Sar","Sor","T","Tan","Th","Thar","Ther","Thr","Thur","Trak","Truk","Ug","Uk","Ukr","Ull","Ur","Urth","Urtr","Z","Za","Zar","Zas","Zav","Zev","Zor","Zur","Zus"];
var nm2 = ["a","a","a","o","o","e","i","u","u","u"];
var nm3 = ["bak","bar","bark","bash","bur","burk","d","dak","dall","dar","dark","dash","dim","dur","durk","g","gak","gall","gar","gark","gash","glar","gul","gur","m","mak","mar","marsh","mash","mir","mur","n","nar","nars","nur","rak","rall","rash","rim","rimm","rk","rsh","rth","ruk","sk","tar","tir","tur","z","zall","zar","zur"];
var nm4 = ["Al","Ar","Br","Ek","El","Fal","Fel","Fol","Ful","G","Gaj","Gar","Gij","Gor","Gr","Gry","Gyn","Hur","K","Kar","Kat","Ker","Ket","Kir","Kot","Kur","Kut","Lag","M","Mer","Mir","Mor","N","Ol","Oot","Puy","R","Rah","Rahk","Ras","Rash","Raw","Roh","Rohk","S","Sam","San","Sem","Sen","Sh","Shay","Sin","Sum","Sun","Tam","Tem","Tu","Tum","Ub","Um","Ur","Van","Zan","Zen","Zon","Zun"];
var nm5 = ["a","a","o","o","e","i","i","u"];
var nm6 = ["d","da","dar","dur","g","gar","gh","gri","gu","sh","sha","shi","gum","gume","gur","ki","mar","mi","mira","me","mur","ne","ner","nir","nar","nchu","ni","nur","ral","rel","ri","rook","ti","tah","tir","tar","tur","war","z","zar","zara","zi","zur","zura","zira"];

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
	rnd = Math.floor(Math.random() * nm4.length);
	rnd2 = Math.floor(Math.random() * nm5.length);
	rnd3 = Math.floor(Math.random() * nm6.length);
	nMs = nm4[rnd] + nm5[rnd2] + nm6[rnd3];
	testSwear(nMs);
}

function nameMas(){
	rnd = Math.floor(Math.random() * nm1.length);
	rnd2 = Math.floor(Math.random() * nm2.length);
	rnd3 = Math.floor(Math.random() * nm3.length);
	nMs = nm1[rnd] + nm2[rnd2] + nm3[rnd3];
	testSwear(nMs);
}