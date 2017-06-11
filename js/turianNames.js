var names3 = ["Ab","Aber","Abi","Aca","Acha","Acil","Ada","Adep","Adju","Adra","Aebu","Aet","Ag","Aga","Ago","Al","Alba","Albi","Albu","Ale","Ba","Bar","Barba","Bell","Bella","Belli","Bibu","Bitu","Bola","Boni","Brom","Bromi","Bru","Bruc","Bul","Cae","Cael","Caep","Cal","Cala","Calp","Calpo","Cam","Campa","Can","Candi","Capi","Dar","Darda","Dec","Dexi","Didi","Domi","Domiti","Doni","Drus","Drusi","Duvi","Ebo","Egna","Elvo","Enni","Epi","Epidi","Epo","Eras","Eudo","Fa","Fal","Faus","Fel","Fim","Flo","Flori","Frum","Gai","Gal","Gari","Gav","Gene","Glob","Gor","Gra","Grat","Hab","Hel","Hil","Hila","Hono","Hora","Horten","Igna","Ind","Inda","Isa","Ita","Lae","Laevi","Lin","Lucce","Luci","Lupi","Mac","Macri","Mal","Marce","Mau","Maur","Maxi","Mel","Merca","Mola","Mur","Muti","Nar","Nata","Naza","Neme","Numo","Octa","Octavi","Olym","Opi","Opti","Orien","Oro","Paet","Pali","Pan","Pap","Peta","Pho","Pos","Pota","Pro","Proc","Prota","Qua","Quen","Qui","Quin","Ram","Rami","Rece","Regi","Remi","Romul","Ruf","Sabe","Salvi","San","Sanc","Scri","Seve","Sim","Simp","Stra","Sul","Suli","Sur","Syl","Tan","Tani","Ter","Tib","Tibur","Tremo","Treni","Umbo","Ursi","Var","Vari","Veli","Veri","Vibi","Vic","Victo","Victri","Vita"];
var names4 = ["cius","colus","culus","cus","das","donis","dos","dros","dus","gatus","gius","ion","lianus","lienus","lin","linus","lius","lus","mius","mus","nian","nianus","nion","nis","nius","nus","panus","raka","rian","ril","rinus","rius","scus","sis","so","tion","tis","tius","tumus","tus"];
var br = "";

function nameGen(gender){	
	var tp = gender;
	if(tp === 1){
		var names1 = ["Agri","Am","Amu","Amul","Amuli","Ap","Ar","Arru","Au","Augu","Augus","Aul","Bri","Bru","Brut","Ca","Cae","Cael","Cai","Cam","Cami","Can","Cas","Cna","Cnae","Cos","De","Dec","Deci","Dru","Drus","Fa","Fau","Faus","Fla","Flavi","Ga","Gai","Gal","Galer","He","Her","Heri","Ho","Hos","Ju","Juli","Julian","Ka","Kae","Kaes","La","Lar","Lu","Luc","Luci","Ma","Mame","Mamer","Man","Mani","Mar","Marce","Max","Maxi","Met","No","Nu","Num","Nume","Octa","Octavi","Op","Opi","Oppi","Pa","Paul","Pla","Po","Posti","Postu","Pot","Poti","Pri","Prim","Pro","Proc","Procu","Pu","Publi","Qui","Quin","Se","Sec","Secu","Sep","Septi","Ser","Servi","Si","Sis","Spu","Te","Ter","Terti","Ti","Tibe","Tiber","Tiberi","Tu","Tul","Tull","Ve","Vel","Vi","Vibi","Vo","Vopi"];
		var names2 = ["bius","bus","cus","eus","ius","lio","lius","lus","mius","mus","na","nus","pius","rius","runs","sius","so","ter","tis","tius","tus","us","vius","vus"];
	}else{
		var names1 = ["Abu","Ac","Aci","Aebu","Aedi","Aemi","Al","An","Anto","Avi","Bae","Ban","Barba","Betu","Bruc","Cae","Caeci","Cael","Caese","Caeso","Cali","Calve","Came","Cami","Cani","Cice","Clo","Comi","Conse","Decu","Desti","Dexi","Di","Duro","Epi","Equ","Fadi","Fla","Flo","Flori","Floro","Furi","Gabi","Gale","Gega","Gra","Here","Hermi","Hora","Ici","Ju","Juve","La","Lae","Libu","Livi","Luta","Mae","Mal","Mani","Mari","Maxi","Me","Mene","Meti","Milo","Nae","Nepi","Ni","Novi","Octa","Oppi","Pa","Pae","Ped","Pina","Pli","Pol","Pompe","Popi","Por","Qu","Qui","Ru","Ruso","Ruti","Salo","Secu","Sei","Sen","Septi","Si","Sido","Sil","Ta","Tani","Treba","Treme","Tu","Tul","Ul","Va","Vale","Vel","Vera","Vi","Vibi","Viri","Vite","Vitel","Volu","Vore"];
		var names2 = ["ana","bia","cia","cidia","dia","ginia","ia","lea","lia","lonia","mia","na","naria","nea","nia","pia","pilia","ponia","retia","ria","sia","tana","teia","tia","tilia","tina","tiria","toria","vea","via"];
	}
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		rnd1 = Math.floor(Math.random() * names2.length);
		rnd2 = Math.floor(Math.random() * names3.length);
		rnd3 = Math.floor(Math.random() * names4.length);
		names = names1[rnd] + names2[rnd1] + " " + names3[rnd2] + names4[rnd3];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}