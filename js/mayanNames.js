var nm1 = ["Acan","Acat","Ah Ciliz","Ah Mun","Ah Tabai","Ah-Bolom-Dz'acab","Ah-Bolom-Tzacab","Ah-Cancum","Ah-Chun-Caan","Ah-Chuy-Kat","Ah-Ciliz","Ah-Cun-Can","Ah-Cuxtal","Ah-Hulneb","Ah-Kin","Ah-Kinchil","Ah-Kuhmix-Unicob","Ah-Mun","Ah-Muzencab","Ah-Patnar-Unicob","Ah-Pekku","Ah-Puch","Ah-Tabai","Ah-Uncir-Dz'acab","Ah-Uuc-Ticab","Ah-Xoc-Xin","Ahau Chamahez","Ahau-Chamahez","Ahau-Kin","Ahluic","Ahmakiq","Ahmucen-Cab","Ahulane","Ajbit","Ajtzak","Akbit","Alom","Atl","Backlum Chaam","Balam","Bitol","Bolon-D'zacab","Buluc-Chabtan","Cabaguil","Cabrakan","Cacoch","Cakulha","Camalotz","Camaxtli","Camazotz","Caprakan","Chac","Chac-Uayab-Xoc","Chamer","Chicahua","Chicchan","Chipahua","Cit-Bolon-Tum","Cizin","Colop-U-Uichikin","Cotzbalam","Coyopa","Cualli","Cuauc","Cuchumaquic","Cum Hau","Ekchauh","Ekchuah","Eztli","Gucumatz","Gucup Cakix","Gukumatz","Hacha'kyum","Hapikern","Hobnil","Hozanek","Hun Batz","Hun-Batz","Hun-Came","Hun-Cane","Hun-Chowen","Hun-Hunahpu","Hun-Nal-Ye","Hunab-Ku","Hunaphu","Hunaphu-Gutch","Hunaphu-Utiu","Huracan","Ikal","Iktan","Itzam-Ye","Itzamatul","Itzamna","Ix","Ix-Tub-Tun","Ixbalanque","Ixmacane","Ixmucane","Ixpiyacoc","Izel","K'awai","K'awi","Kabil","Kan","Kan-U-Uayeyab","Kan-Xib-Yui","Kawil","Kianto","Kichigonai","Kinich Ahau","Kinich Kakmo","Kisin","Kukulcan","Manik","Metnal","Mitnal","Mulac","Muluc","Nacon","Nanochacyum","Necahual","Och-Kan","Papan","Pawahtuun","Poxlom","Q'uq'umatz","Qaholom","Tecumbalam","Tepeu","Teyacapan","Tlacolotl","Tohil","Tzacol","Tzultacaj","Uc-Zip","Usukan","Uyitzin","Voltan","Votan","Vucub-Caquix","Vukub-Cakix","Vukubcane","Xaman Ek","Xaman'Ek","Xamaniqinqu","Xbalanque","Xecotcovach","Xibalba","Xipil","Xpiayoc","Xumucane","Yaluk","Yantho","Yaotl","Yum Caax","Yum Cimil","Yumbalamob","Yumchakob","Zac-Cimi","Zipacna","Zotz","Zyanya"];
var nm2 = ["Ah-Uaynih","Ah-Wink-Ir-Masa","Akhustal","Akna","Alaghom-Naom-Tzentel","Amoxtili","Chachiuitl","Chen","Chichuaton","Chimalmat","Chin","Chirakan-Ixmucane","Citlali","Citlamina","Colel","Colel Cab","Coszcatl","Cualli","Eleuia","Ichtaca","Ihuicatl","Iktan","Itotia","Itzamatul","Itzel","Iuitl","Ix Kaknab","Ixazaluoh","Ixazalvoh","Ixchel","Ixcuiname","Ixik","Ixtab","Ixtel","Ixtli","Mecatl","Meztli","Nelli","Nenetl","Patli","Sacniete","Sacnite","Tecuith","Tepin","Tlalli","Tonalnan","Xmucane","Xoc","Xochitl","Xoco","Xpiayoc","Xquic","Xquiq","Yatzil","Yoltzin","Zac-Kuk","Zeltzin","Zyanya"];
var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd];
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