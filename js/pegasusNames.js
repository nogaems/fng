var nm1 = ["Abde","Aby","Aca","Ache","Achi","Acta","Ade","Adme","Adra","Ae","Aea","Aeto","Agame","Aja","Ale","Amy","Ando","Anta","Ante","Apo","Arca","Arce","Arche","Argo","Arse","Arte","Asca","Atha","Atla","Baccu","Bazy","Bry","Cae","Cali","Capa","Casea","Cepha","Cory","Cyra","Dae","Dama","Damia","Damio","Daria","Dario","Deme","Demo","Dio","Dora","Dra","Era","Ere","Este","Eury","Fe","Gae","Gela","Hae","Helio","Hera","Hero","Ia","Ico","Ja","Ko","Koru","Kra","Kyri","La","Laiu","Lea","Leo","Leoni","Lo","Lu","Mela","Mida","Myro","Nau","Ne","Obe","Obia","Ocea","Pano","Pelia","Phanta","Phy","Pria","Pyra","Ra","Rho","Saba","Sote","Ste","Tara","Tela","Tha","Thano","Thau","The","Thye","Ti","Tiva","Tri","Ty","Tyro","Vasi","Xa","Ze","Zeno","Zo"];
var nm2 = ["carus","celos","chus","clus","cnaeon","cos","dalus","dareus","das","demus","des","don","dras","dros","jax","kon","lan","laus","leimon","lemus","leon","les","lios","lius","lix","lles","llos","lops","los","lpheus","lphos","maeus","mas","medes","meon","mion","mnon","mon","morus","naeon","nder","ndras","neus","nidas","nios","nis","nius","nnos","nous","peros","pheus","phon","phos","phyr","pios","pius","rdanus","reus","rgos","rgus","rian","ridon","rios","ritus","rnus","ron","ros","rtus","rus","ses","seus","sidas","sios","sius","smus","ssus","stheus","sthus","stolos","stos","stus","teon","teus","thes","thon","tone","tos","trios","trius","tros","tus","xio","xus"];
var nm3 = ["Aca","Ada","Ade","Ado","Aga","Agne","Ai","Ala","Aldo","Ale","Ali","Aly","Ana","Ane","Aphro","Apo","Are","Ari","Athe","Axe","Ba","Bella","Ca","Cala","Casca","Cassa","Cha","Che","Co","Cyna","Da","Dama","Deni","Dia","Dio","Dy","Ebo","Eire","Ele","Elea","Eli","Eu","Eudo","Euphe","Eva","Fae","Fe","Gela","Ha","Hele","Hya","Hypa","Ido","Io","Iri","Isa","Ja","Ka","Kare","Kari","Katha","Ko","Ky","La","Lari","Lea","Leo","Li","Liva","Mae","Mari","Me","Melai","Meli","Mine","Nai","Nare","Ne","Neo","No","Obe","Ode","Oly","Ophe","Ophi","Pene","Perse","Phe","Phy","Rai","Re","Sa","Sele","Sire","Ste","Ta","Tere","Tha","The","Tia","Tima","Tita","Tre","Vane","Xe","Yale","Yola","Za","Zani","Ze","Zera"];
var nm4 = ["cia","da","dia","dite","dora","la","lanie","lena","leta","lia","lina","lla","llia","lline","lona","mara","meda","mena","mia","misia","mona","mone","na","ndia","ndra","neta","nia","nie","nne","nor","nora","ntha","nthe","nthea","phelia","phine","phira","phne","phone","ra","rena","rene","resa","rine","rise","rissa","rria","sia","sima","sine","ssa","tasia","teia","tha","thea","thia","thy","tia","tine","tria","vana","xis"];
var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			names = nm3[rnd] + nm4[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + nm2[rnd2];
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