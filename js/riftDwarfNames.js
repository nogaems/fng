var br = "";

function nameGen(type){
	var tp = type;
	if(tp === 1){
		var names1 = ["Ale","Ali","A","Ba","Bari","Be","Bi","Bise","Bo","Bohu","Bori","Boza","Bra","Brani","Bre","Bro","Da","Dani","Dari","De","Deni","Dobri","Do","Dobro","Dra","Draga","Draho","Du","Dusa","Eli","Ela","Go","Gora","Gro","Gra","Ida","Iva","Ja","Jani","Jale","Jase","Jele","Ka","Kali","Ke","La","Le","Li","Ma","Mali","Me","Meli","Mi","Mila","Mile","Miru","Mo","Mora","Ne","Neve","O","Ole","Ra","Radi","Ro","Rosi","Ru","Rumi","Se","Sta","Stani","Suda","Su","Ti","Tiha","Tu","Va","Ve","Veli","Bo","Borghi","Bry","Ei","Fre","Ge","Gri","Gro","Gu","Hei","Hi","Hu","Na","Sa","Si","Ska","Sva","Ve"];
		var names2 = ["bla","bra","briana","bromira","dana","dandi","dania","danka","dda","dka","dmila","domia","domira","drana","drun","duna","dunn","ga","gana","gdana","ghild","ghildr","gna","gny","grun","ha","hana","hild","hildr","homira","humira","jana","kadi","ksana","kuld","lana","lda","ldr","lena","lenka","lica","lika","lina","linka","lmira","mbla","mena","mhild","mhildr","miana","mila","mira","na","nca","nhild","nhildr","nia","nica","nika","nimira","nka","nna","nuska","ra","rana","ranka","rdandi","reyja","ria","riana","rid","rigg","rina","rinka","ritza","rka","rmila","romira","runa","ruska","rvara","rya","rzanna","sana","senka","sera","serka","sica","ska","tka","tza","vana","vara","vena","venka","zana","zanna","zda","zdana","zena","zhana","zka"];
	}else{
		var names1 = ["Ba","Be","Bi","Bla","Bo","Bogo","Bohu","Boji","Bozhi","Bozi","Bra","Bre","Bu","Budi","Buri","Ca","Casi","Da","Dali","De","Di","Do","Dobro","Dra","Fre","Ga","Go","Gode","Gra","Gro","Gu","Ja","Jaro","Ka","Kazi","Kra","Krasi","Kre","Kresi","Lo","Lu","Lubo","Ludo","Ma","Mi","Milo","Mo","Nja","Njo","O","Ode","Odi","Ogni","Orva","Pa","Pre","Pro","Ra","Radi","Rado","Si","Sta","Stani","Straa","Tho","Ty","Va","Ve","Veli","Vi","Volu","Za","Ze","Zeli","Zi","Zito"];
		var names2 = ["ban","bomir","bor","borek","brad","bren","brin","bromir","cimir","dalf","dan","dar","darr","dek","demir","der","dik","dim","dimir","dinn","domer","domir","dos","dovan","dran","dzimir","gan","gdan","gisa","gnian","go","gomil","gomir","gotin","goy","grun","gumil","gun","gurd","gutin","gvi","hdan","himir","homir","hos","hren","humer","humil","humir","jan","jek","jidar","lek","libor","lik","limir","lin","ljan","lko","lon","lorad","los","lovan","lund","lundr","lyan","mard","mek","mer","mil","mir","narr","nat","ndri","nek","nik","nimir","nko","nnarr","ran","rban","rce","rek","rey","reyr","rian","rik","ril","rin","ris","rko","rlin","romer","romir","ros","rut","rvan","rvar","rwan","ser","simir","stan","tek","tik","tomir","van","vis","vor","vril","wan","zan","zdan","zen","zhil","zhin","zidar","zimir","zydar"];
	}
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		rnd2 = Math.floor(Math.random() * names2.length);
		names = names1[rnd] + names2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}