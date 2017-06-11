
function nameGen(type){
	var nm1 = ["Abahag","Abidine","Aboura","Adebir","Aflan","Agag","Ahag","Ahmed","Ahmedu","Ahu","Aitarel","Akhemouk","Akhiou","Akorebi","Akrud","Alemhok","Allgoui","Amanrassa","Amar'l","Amastame","Amayas","Amder","Amellal","Amer","Amjer","Amma","Amoud","Anaba","Ansar","Aqqasen","Askiou","Attici","Aziouel","Baba","Badjhoud","Bay","Beh","Beketa","Bekkai","Biska","Bouhen","Brahim","Bubekir","Buzin","Chekkadh","Chikat","Danguchi","Echerif","Ehenkouen","Ehenu","El Boghari","El Hamous","El Hosseyni","El Khir","El Kounti","El Menir","El Mokhtar","El Mostafa","El Mouden","Elwafil","Goma","Hama","Heguir","Hosseyni","Howedi","Ibrahim","Ihemma","Ihemod","Iherhe","Ikemma","Ikhenoukhen","Iklan","Ilaman","Ilbak","Ilou","Kenan","Keneiss","Keradji","Khabte","Khebbi","Khelba","Khemidou","Khyar","Lamine","Louen","Louki","Makhia","Mama","Marli","Mellou","Meslar","Mohammed","Moussa","Musa","Okha","Othman","Ou-Fenait","Ould","Ourzig","Rali","Rezkou","Salah","Salla","Ser'ada","Sid Ahmed","Sidi","Sidi Mohammed","Souri","Tamaklast","Tinekerbas","Tissi","Uksem","Uray","Yakhia","Younes"];
	var nm2 = ["Aisha","Amena","Baya","Bella","Dasha","Dassine","Demu","Dhabba","El Jamit","El Kubra","El Mamoum","Eljamit","Elkubra","Elmamoum","Essebet","Fadimata","Fatma","Feduda","Hadada","Hadeja","Hariza","Hashisha","Kahina","Kana","Katouh","Kella","Khaouila","Khatti","Kodda","Lalla","Lella","Lemtuna","Malla","Meriama","Mimi","Raeraou","Rahma","Rahmadu","Raisha","Ratma","Raysha","Rayshabu","Regida","Seda","Sekata","Shemama","Sherifa","Sheyma","Tabehaout","Taber'ourt","Tagouzamt","Tahat","Tahe","Tahenkot","Tahyart","Takama","Tamagit","Tamat","Tamerouelt","Tamu","Tandarine","Tanelhir","Tanermat","Tanloubouh","Tar'aoussit","Tebeshit","Tebubirt","Tekawilt","Tiguent","Tihit","Tinhert","Tinhinan","Tioueyin","Umeyda","Wertenezzu","Zahara"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.random() * nm1.length | 0;
		if(tp === 1){
			rnd = Math.random() * nm2.length | 0;
			names = nm2[rnd] + " ult " + nm1[rnd2];
			nm2.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm1.length | 0;
			names = nm1[rnd] + " ag " + nm1[rnd2];
			nm1.splice(rnd, 1);
		}
		nm1.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}