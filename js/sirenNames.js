var nm1 = ["Aba","Aca","Acale","Ado","Adra","Aeleo","Aethe","Aethi","Agla","Aglao","Aiga","Ala","Alci","Ama","Amali","Amy","Ani","Ara","Aroa","Asi","Aste","Asteo","Ate","Boli","Bor","Cali","Calli","Calo","Caly","Cela","Cha","Ciri","Cla","Cly","Cora","Cori","Coro","Cria","Daei","Dana","Daph","Daphi","Dio","Dori","Dory","Echi","Echo","Eli","Elu","Ephe","Euphe","Eva","Evi","Gali","Hai","Heli","Hi","Hime","Ia","Iana","Iao","Ida","Idah","Ila","Ile","Ipha","Kahli","Kali","Kalli","Kela","Kimo","Kle","Kleo","Lame","Lami","Lao","Laome","Lari","Leu","Leuco","Li","Limo","Ma","Mai","Mali","Mary","Me","Meli","Meni","Meti","Metio","Mol","More","Mys","Nai","Nea","Neame","Neda","Neme","Nemen","Nephe","Neri","Nesa","Nona","Nysa","Ole","Ori","Pala","Palle","Par","Pasi","Pei","Peisi","Perei","Peri","Peti","Peto","Phali","Phe","Phero","Phi","Phia","Phio","Phri","Physa","Pi","Pire","Pisi","Porei","Rai","Rhae","Rhe","Rhene","Sabri","Sala","Salo","Sapha","Sava","Syli","Syna","Tania","Te","Tele","The","Thel","Thelxie","Themi","Thoni","Zeli"];
var nm2 = ["cea","cia","cine","danea","deia","delia","della","dia","dise","doe","done","dora","dorise","ete","gale","geia","genia","gina","gonia","goria","kaia","kea","kharei","lacia","laeno","laira","lane","lato","lea","leia","lenia","leora","les","lia","liana","lina","linai","liphis","lira","lirea","liria","lis","lise","lodia","lopei","lophi","lyse","mea","mei","meia","meine","melle","mellia","mene","meni","menis","mia","milia","mine","mis","misa","misia","moni","naera","nara","nassa","nea","nei","neira","nele","nia","niassi","nilla","nise","nisse","noe","nohre","noire","nome","nope","nophe","nore","nos","pe","pea","peia","phaeia","phaia","phei","pheia","pheme","pheu","phia","phine","phise","phite","phonos","pise","rane","rea","reanes","recea","rei","reia","reino","reisis","relia","rephis","ria","rianne","riko","rila","riope","ris","rise","riye","rodia","ronei","ronis","rope","rose","sa","sea","seis","seise","sesis","sia","sine","siphe","sis","sise","tai","tea","teia","the","thea","thei","theis","thelia","thera","thilei","thise","thoe","thusa","thyia","thylia","tiax","xera","xiope"];
var nm3 = ["Adra","Adre","Adrea","Adri","Adria","Adrie","Ae","Aega","Aere","Aeri","Aethe","Allu","Alu","Ama","Ana","Aqea","Aqia","Aqua","Aqui","Ari","Arie","Arri","Arrie","Assa","Aura","Ava","Aza","Bri","Calla","Chel","Chene","Cheri","Cora","Corae","Corde","Corea","Corra","Corrae","Dali","Dela","Delma","Delo","Dia","Dio","Do","Dorea","Doria","Dorie","Eathe","Echo","Eire","Fonta","Gene","Geni","Gine","Guine","Hali","Hy","Jenie","Jenni","Jeny","Kai","Ky","Lagu","Lai","Larai","Lorae","Lorai","Lore","Mari","Mary","Maya","Mello","Melo","Mere","Meri","Mira","Morga","Muri","Murie","Na","Nada","Nah","Nari","Nau","Nauti","Nerei","Neri","Noe","Oara","Oce","Ocea","Ora","Rae","Sere","Serei","She","Shei","Sire","Sirei","Tali","Talo","Tha","Thala","The","Thessa","Undi","Vivi","Vivia","Vivie","Ya","Zha"];
var nm4 = ["bel","belle","ciane","da","dah","denah","dina","dine","fa","fer","gana","guna","gune","haneh","la","lea","lee","leh","lei","lena","lia","lila","lin","lina","lis","lise","lla","lle","lody","lora","lori","lura","lure","ly","lyn","ma","mala","mara","mare","me","meda","mere","mora","na","nah","ne","neh","nella","nelle","neva","ney","nia","nna","nne","noe","nora","nore","ny","ra","rah","rea","reida","rena","rene","renna","ria","rial","rian","riel","rien","rin","rina","rinda","rinia","ris","rissa","rith","roe","ros","sana","sea","shell","shi","ssa","sura","ta","thea","thia","tina","tune","va","ve","vere","via","viane","vianna","vien","wai","wen","xie"];
var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + nm2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			names = nm3[rnd] + nm4[rnd2];
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