
function nameGen(type){
	var nm1 = ["Abbas","Abdou","Abdoulaye","Abdoulie","Ablanjaye","Ablie","Abu","Adama","Addo","Alaji","Alansana","Alanso","Alasan","Alieu","Alifa","Amadou","Amat","Antouman","Antu","Assan","Babaja","Babou","Baboucar","Badara","Bai","Bailo","Bakary","Bala","Baluta","Bamba","Bango","Banja","Banta","Bassirou","Baturou","Baturu","Biran","Birom","Bolong","Bora","Boro","Boto","Bouba","Boubacar","Boy","Buba","Bubacar","Bunama","Burama","Buwa","Chenor","Cyper","Daba","Demba","Dembo","Dodou","Duta","Duwa","Ebou","Ebrahima","Ebrima","Ediresa","Edrissa","Ensa","Essa","Fabba","Fafa","Fakebba","Fanding","Fara","Faraba","Filije","Foday","Gereh","Gibril","Habib","Hasimou","Hassan","Hatabu","Idi","Idirissa","Ilman","Isa","Isaka","Ismaela","Jabril","Jalang","Jamang","Janko","Jato","Jebel","Jereh","Jibou","Jibril","Jibrin","Jombo","Jonkong","Juma","Jumu","Jung","Junkung","Kabir","Kabiru","Kairaba","Kamara","Karafa","Karamba","Karamo","Kausu","Kawsu","Kebba","Kekoto","Kekuta","Kemo","Kunta","Kutubo","Lafi","Laity","Lallo","Lalo","Lama","Lamin","Landing","Longcan","Madi","Makang","Malamin","Malick","Malik","Mamadi","Manlafi","Masane","Mohammed","Momodou","Momodu","Muña","Musa","Mustafa","Nfansu","Omar","Ousman","Pa","Paboy","Paoboy","Pateh","Saihou","Saikou","Sainey","Sajo","Sama","Samba","Sarjo","Seedy","Sherif","Sheriff","Sherrif","Sidibeh","Sirif","Sulayman","Suma","Suntukung","Sutay","Tairu","Tamba","Tijan","Tombong","Wandi","Wandy","Wasa","Wassa","Ya","Yakuba","Yankubah","Yaya","Yoro"];
	var nm2 = ["Aba","Abi","Adama","Adel","Aisa","Aja","Ajamboon","Alanso","Alimatou","Ami","Amie","Aminata","Anti","Aramata","Attha","Awa","Bassin","Binta","Bintou","Bintu","Birta","Channeh","Daba","Fanta","Fatou","Fatoumata","Fatoumatta","Filije","Filijee","Hadang","Haddy","Halima","Hawa","Ibironke","Ida","Isa","Isatou","Jabou","Jahou","Jainaba","Jankeh","Jatou","Jeneba","Joñi","Jojo","Joma","Juka","Kabir","Kaddy","Kaddyatou","Kadi","Kadijatou","Kati","Kenenjaye","Khadijatu","Kinteh","Kinti","Koba","Kobba","Kumba","Kunda","Kurukemeh","Kuta","Kutu","Loli","Maimuna","Makuto","Mama","Mamanding","Mampol","Mandiki","Maram","Marang","Mariama","Marie","Maseray","Mbasi","Mbassi","Mboose","Musakuta","Musu","Musukebba","Musukuta","Ndey","Nene","Nyima","Nyonkoling","Oumil","Pahali","Piretta","Ramata","Ramatoulaye","Ramatoulie","Rohey","Saijo","Sainabou","Sainey","Sajo","Sanji","Sara","Sarjo","Satang","Satou","Sibo","Sira","Sirending","Sohna","Sona","Sukai","Sunkarr","Suntukung","Sutay","Tida","Tomaring","Yahar","Yama","Yamma","Yamundow","Yari","Yata"];
	var nm3 = ["Ba","Badjie","Bah","Bajo","Baldeg","Baldeh","Biri","Camara","Ceesay","Ceesay","Colley","Conateh","Condé","Condeh","Coote","Corr","Coulibaly","Dabo","Danso","Daramy","Darboe","Diawara","Dibba","Diene","Dieye","Dione","Diouf","Fadika","Fatty","Faye","Gassama","Gaye","Guissé","Guiss","Hairte","Jagne","Jaiteh","Jallow","Jammeh","Janneh","Jarju","Jassey","Jatta","Jawara","Jawara","Jawo","Jobateh","Jobe","Joof","Kaba","Kabba","Kabbah","Kah","Kairaba","Kakay","Kama","Kambi","Kandeh","Kargbo","Kayode","Keita","Kinte","Kinteh","Kolley","Kouyaté","Kujabi","Kuyateh","Manneh","Mansaré","Mansaray","Marenah","Marong","Mboge","Mboob","Mbye","Mendy","Ndaw","Ndiaye","Ndour","Ngom","Ngum","Niang","Njie","Nyang","Ogoo","Ogunsola","Ouattara","Saidykhan","Sanneh","Sanyang","Sarr","Savaneh","Secka","Sene","Senghore","Sesay","Sey","Sidibeh","Sillah","Singateh","Singhateh","Sohna","Soley","Sonko","Sowe","Suso","Taal","Thiaw","Tiyana","Touré","Touray","Turay","Uster"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.random() * nm3.length | 0;
		if(tp === 1){
			rnd = Math.random() * nm2.length | 0;
			names = nm2[rnd] + " " + nm3[rnd2];
			nm2.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm1.length | 0;
			names = nm1[rnd] + " " + nm3[rnd2];
			nm1.splice(rnd, 1);
		}
		nm3.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}