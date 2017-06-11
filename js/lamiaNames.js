var nm1 = ["Absyr","Acast","Acher","Adelph","Adr","Aeac","Aes","Aesc","Agath","Alc","Alex","Alph","Amph","Amyc","Anast","Anaszt","Anath","Anc","Anch","Anst","Ant","Antiph","Aphol","Aphr","Arist","Ars","Arth","Ashat","Ath","Athan","Bas","Bast","Baz","Bras","Buth","Caes","Caphan","Cas","Cast","Cel","Ceph","Cir","Cyr","Das","Dath","Demith","Demoph","Deph","Deuc","Dionys","Eph","Eras","Erasm","Eus","Eust","Hel","Heph","Her","Hesp","Ibys","Icel","Inach","Iphicr","Iphit","Isocr","Ix","Jas","Kos","Kosm","Krath","Laest","Lich","Lox","Lyc","Lys","Mops","Mos","Naph","Nis","Ocean","Oediph","Orthr","Paph","Parth","Pestr","Phaeth","Phal","Phalaem","Phant","Phil","Phleg","Phyl","Phrix","Priaph","Proph","Protes","Pyras","Rasm","Rist","Salm","Scop","Socr","Sot","Soter","Spyr","Stam","Stef","Steph","Taras","Thadd","Thal","Than","Tharas","Thelam","Theoph","Ther","Therr","Thers","Thes","Thim","Thit","Thyest","Troph","Tyliss","Typh","Ulyss","Vas","Vasil","Xanth","Xen","Xerx","Xuth","Zal","Zeph","Zet"];
var nm2 = ["ades","adus","aestus","aethon","aeus","alus","amas","anos","anthus","aphus","apius","aris","as","asius","asos","astos","astus","ates","athan","athis","atius","atos","aus","ax","eas","edes","eithes","elaus","elix","elos","elous","elphos","ephon","epios","erios","eros","ersis","erus","es","eseus","esio","etheus","ethon","etrios","etus","eus","exei","exia","exis","iaraus","ias","ice","idas","illes","inos","ios","ippus","ips","ipus","is","ises","isius","iss","iste","isthus","istos","ithous","itos","itrius","itus","ix","ixi","ixus","obus","ochus","ocia","oebus","oeus","olas","olos","oneus","onis","oph","ophe","ophon","ophor","ophoros","orus","os","ose","osyne","otheos","othius","ous","ukas","us","ux","ypnos","yptus","yrtus","ys","ysios","yx"];
var nm3 = ["Acal","Acos","Acs","Adoz","Adras","Ael","Aeth","Akis","Aleth","Alethr","Alex","Amath","Amiph","Anth","Aph","Areth","Ash","Astr","Ath","Athil","Athiz","Axiph","Bath","Breth","Calyph","Cast","Chal","Cir","Cnass","Creph","Creth","Daph","Daphn","Dios","Dor","Eriph","Eth","Ethem","Euph","Euth","Evith","Galix","Gath","Harph","Has","Hys","Ias","Idaph","Iph","Is","Kaliph","Kaph","Kath","Kis","Kiss","Kleph","Leph","Leuc","Lis","Lith","Lys","Math","Meniph","Meph","Mess","Mis","Myrith","Myst","Neph","Nes","Neth","Nix","Nys","Nysh","Nyx","Olith","Ophi","Oreth","Oriph","Orph","Othr","Paph","Pas","Pesh","Peth","Phaeth","Phais","Phal","Pher","Phil","Pho","Phrix","Phys","Pix","Prax","Pris","Prix","Pros","Psal","Rhaen","Rheth","Sab","Sag","Sal","Salaph","Sam","Saph","Savar","Sel","Selest","Sil","Sin","Sylph","Syn","Syr","Taph","Thal","Than","Theam","Thean","Theis","Thel","Thes","Thesp","Thos","Thron","Thyx","Xan","Zel","Zeph","Zeux"];
var nm4 = ["acia","aeia","ahria","aia","ais","ali","alise","allis","alphia","anea","anise","anthe","anthei","aphaura","aphine","assa","assea","axaura","axise","ea","easi","edice","eila","eilise","eilla","eis","eisa","eithe","eleia","elia","elis","elphise","elsa","enia","enis","eosis","ephia","ephila","ephine","eris","ertes","ertise","eshi","esi","esis","essei","ethe","ethia","ethis","etis","eusa","ia","iaphe","iasse","iax","ice","iche","ilis","ine","inix","ionis","iophai","iphae","iphaeia","iphe","iphei","iphelia","iphi","iphia","iphis","iphise","iphite","iphoia","is","isa","ise","isei","isha","ishae","ishia","ishis","isia","issis","istae","ite","ithe","ithea","ithis","ithise","ithoe","iusei","ixa","ixera","ixia","ixie","oche","oesa","ohsa","olphi","one","ophai","ophe","opheu","ophi","ophia","ophila","ophis","ophise","orise","osa","ose","osi","osia","osise","ossia","thise","usa","usei","usi","ymes","yphe","yphise","ypise","ypso","yse","yxio","yxo"];
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