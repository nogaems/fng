
function nameGen(type){
	var nm1 = ["Appan-Il","Apuulluunideeszu","Ariistuun","Arishaka","Ataneedusu","Anti'iikusu","Aplaa","Ar'siuqqa","Arshaka","Attii'kusu","Baassiia","Balashi","Balathu","Bashaa","Burnaburiash","Dadanum","Dee'qiteesu","Deemeethresu","Deemethereesu","Deemethresi","Deemethresu","Deemuukratee","Demeetheresu","Demetheriia","Dii'duuresu","Diimeritia","Diipaa'ni","Diipanii","Diipatusu","Dipatusu","Dudu","Ea-nasir","Ekurzakir","Enshunu","Enusat","Gina","Hillalum","Hunzuu","Iaazipaa","Ibbi-Adad","Ikuppi-Adad","Ipqu-Annunitum","Ipqu-Aya","Ishme-Ea","Isiratuu","Issaruutunu","Kadashman-Enlil","Kiipluu'","Kiipluuu'","Kinaa","Kuri","Kurigalzu","Labashi","Laliya","Laqip","Ligish","Libluth","Manishtusu","Manishtushu","Manuiqapu","Mannuiqapi","Mannuiqapu","Naram-Sin","Nidintu-Bel","Nidintulugal","Niiqiarqusu","Niiqarquusu ","Niiqquulamuusu","Nikanuur","Nikiiarqusu","Nigsummu","Nigsummulugal","Nigsummunu","Nutesh","Numunia","Nur-Ayya","Puzur-Ishtar","Rabi-Sillashu","Rihat","Rimush","Ripaa","Samsuiluna","Sargon","Seluku","Shamash-Andulli","Shamash-Nasir","Shar-kali-sharri","Shu-Turul","Sin-Nasir","Suusaandar","Tattannu","Timgiratee","Ubar","Ugurnaszir","Uktannu","Uppulu","Utuaa","Yahatti-Il","Zuuthusu"];
	var nm2 = ["Adeeshuduggaat","Ahassunu","Ahati-waqrat","Ahatsunu","Alittum","Amata","Anagalmeshshu","Anagalshu","Arahunaa","Arwia","Ashlultum","Banunu","Belessunu","Beletsunu","Enheduana","Erishti-Aya","Ettu","Gashansunu","Gemegishkirihallat","Gemekaa","Gemeti","Humusi","Ia","Iltani","Ishtar-gamelat","Ku-Aya","Ku-Baba","Kullaa","Munawwirtum","Mushezibitu","Mushezibti","Nidintu","Ninsunu","Tabni-Ishtar","Ubalnu","Yadidatum","Zakiti"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.random() * nm2.length | 0;
			names = nm2[rnd];
			nm2.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm1.length | 0;
			names = nm1[rnd];
			nm1.splice(rnd, 1);
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