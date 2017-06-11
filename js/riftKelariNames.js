var br = "";

function nameGen(type){
	var tp = type;
	if(tp === 1){
		var names1 = ["Ac","Ad","Adem","Adon","Adr","Ag","Agl","Ail","Air","Al","Alet","Alex","Alys","Am","An","Anas","And","Ang","Aph","Aphr","Apol","Ar","Aret","Art","As","Asp","Ath","Bar","Cal","Call","Cas","Casc","Cath","Cel","Char","Cher","Cos","Cres","Cyr","Daphn","Del","Delph","Dem","Den","Dian","Dion","Dor","Dorin","Dun","Eil","Elean","Elen","Elin","Eud","Euph","Evan","Evang","Gel","Hel","Hyac","Hyp","Ir","Is","Isad","Kal","Kol","Lar","Lyd","Mar","Mel","Nel","Ner","Nes","Nor","Ol","Olym","Oph","Pan","Pand","Phed","Phil","Ren","San","Sel","Stel","Tar","Ter","Thel","Xand","Xen","Zan","Zer"];
		var names2 = ["acia","adia","agia","aina","ala","alia","anda","andia","andra","ania","antha","ara","arria","asia","atha","atia","eanor","ectra","eda","eia","ela","elia","elina","emia","emona","emone","ena","enia","ephone","erine","erise","esa","eta","etha","ethea","etina","etria","exis","ia","ice","ida","ienne","illa","ina","ine","inthe","ira","isia","isma","issa","ite","itha","iza","ocia","odite","odora","omeda","omena","ona","one","onia","onne","ora","osine","othea","othy","yllis","yne","ysa"];
	}else{
		var names1 = ["Ab","Abd","Abs","Absyr","Ac","Acas","Ach","Achat","Achel","Achil","Achl","Acr","Act","Ad","Adber","Adel","Adelp","Adm","Adr","Adras","Aeac","Aeg","Aegis","Aegyp","Aen","Aeol","Aes","Aescul","Aet","Ag","Agam","Agat","Ain","Aj","Ak","Al","Alcan","Alcin","Ales","Alex","Alp","Am","And","Andr","Ant","Antil","Apo","Apol","Arc","Arg","Aris","At","Bal","Bas","Baz","Bem","Bor","But","Cadm","Cap","Cas","Cast","Cel","Cep","Cerb","Cir","Col","Cor","Corid","Cro","Dam","Damar","Damas","Dar","Darr","Dem","Demet","Demod","Demor","Diom","Dion","Dn","Dor","Dun","Erasm","Erys","Eur","Gan","Gor","Greg","Grig","Hec","Hect","Hel","Her","Herc","Herm","Hes","Hom","Homer","Icar","Jul","Kor","Krat","Krik","Kyr","Lean","Leon","Lys","Maur","Morp","Nar","Nect","Nem","Ob","Obel","Or","Orp","Pal","Pat","Pen","Per","Phant","Plat","Pos","Proct","Ras","Rhod","Socr","Spyr","Stam","Tak","Thad","Ther","Trit","Vas","Xer","Zen"];
		var names2 = ["acus","aemon","aeon","aethon","aeus","annos","antes","apius","areus","arios","arius","arus","asius","astos","ates","atius","aus","avros","eas","elous","emas","emus","enios","eon","eos","epios","erios","eron","eros","erus","es","etheus","etrios","etrius","etus","eus","hates","heus","hile","hos","ian","icus","idas","illes","illos","ion","is","isius","iss","issus","isthus","isto","ites","iton","ius","obus","ocles","olemus","olos","olus","onis","orgon","orior","orus","os","osios","othius","ous","ycus","ymion","yros","ysius","ystheus","ysus","ytus"];
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