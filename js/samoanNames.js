
function nameGen(type){
	var nm1 = ["Afasa","Afu","Ainalani","Akeakami","Ala'i","Aleki","Alepati","Alesana","Amosa","Aneterea","Apa","Apelu","Aperamo","Apineru","Apisaloma","Aputi","Arona","Atamu","Atini","Elekana","Eli","Elia","Elisaia","Elisara","Enele","Esekielu","Esera","Etano","Etena","Falaniko","Falelauli'i","Falevalu","Faresa","Fatu","Feleti","Fetu","Filiki","Fiti","Hawea","Hemana","Henare","Iakopo","Iareto","Iasona","Iese","Ietero","Ieti","Ioelu","Iona","Ionatana","Iosefa","Iosia","Iosua","Ira","Isaako","Isaia","Iuta","Kainano","Kaisara","Kalepo","Kaperielu","Kiliona","Kisona","Kitiona","Kiuga","Kuresa","Lafi","Lagi","Laki","Lalo","Lasalo","Leasu","Levi","Losi","Loto","Malosi","Manaia","Manuia","Mareko","Mariota","Mataio","Mauga","Mo'e","Natano","Ne'igalomeatiga","Niko","Nikotemo","Noa","Nu'u","Nunu","Ofo","Omeri","Opetaia","Pati","Patolomaio","Peni","Peniamina","Pili","Pisa","Pita","Pu'a","Pule","Rangi","Reupena","Ropati","Sailo","Saipele","Sakaria","Salema","Samasoni","Samuelu","Saulo","Setu","Siaki","Siali","Siaosi","Sila","Simi","Siona","Sione","Solomona","Tala","Tamasese","Tamati","Tamotu","Tanielu","Tapu","Tariua","Tasura","Tataio","Tau","Taua","Tavita","Temetiu","Timoteo","Toa","Tolani","Toma","Ualese","Ualesi","Ula","Vai","Viliamu"];
	var nm2 = ["Agelu","Aiono","Akenese","Alea","Ali'tasi","Alofa","Ana","Aokuso","Aperila","Apikaila","Arieta","Arihi","Asoese","Ata","Atalia","Elei","Elisapeta","Emere","Eseta","Etena","Eunike","Eva","Fa'afetai","Fa'alupe","Fa'atasi","Fa'auma","Faigofie","Felesita","Fetu","Fetuilelagi","Fiafia","Fili","Hana","Ioana","Ituau","Iulia","Iuni","Iutita","Kaila","Kalautia","Kanake","Keise","Keloe","Kenese","Kolone","La'ei","Lagi","Lalago","Lama","Lanuola","Lea","Leigalo","Lele","Lelei","Lili","Lisa","Litia","Loi","Lua","Lulu","Lupelele","Lusi","Makatala","Makerita","Malae","Malamaisaua","Malia","Malie","Manamea","Maota","Mara","Mareta","Masina","Mata","Mere","Miriama","Moana","Mura","Nafanua","Naomi","Natia","Nuanua","Onosa'i","Peka","Pele","Penina","Pepe","Perenike","Rongomaiwhenua","Sa'ea","Salamasina","Sali","Samaria","Seepa","Sefina","Seine","Siliva","Sina","Sinasamoa","Solosolo","Suluama","Taeao","Tagilima","Taimane","Talalelei","Talia","Taligi","Tama","Tamah","Tava'esina","Telila","Tepora","Teuila","Tiana","Tina","Tui'uli","Tupuasa","Tusila","Upumoni","Venis","Wiki"];
	var nm3 = ["Afakasi","Afamasaga","Ala'ilima","Alofipo","Alovili","Anae","Apatu","Asau","Asiata","Asoau","Ausage","Autagavaia","Enesi","Esera","Fa'amoe","Faaeteete","Faamate","Faamoana","Faasoo","Faatasi","Faiivae","Fainu'u","Falagi","Faleafa","Fanaafi","Fanene","Faraimo","Faresa","Fepuleai","Feresa","Fiso","Foai","Fualema","Fuga","Fuima","Galuvao","Ierome","Ioane","Isaia","Kuresa","Latu","Lavea","Le'au","Lea'ai","Leapai","Leapama","Lemalu","Lemaota","Leniu","Leoso","Levaai","Levaopolo","Lofipo","Lopamaua","Lotomau","Lotulelei","Maiava","Malaitai","Malemo","Manaia","Matautia","Maugatai","Maulalo","Multiauaopele","Naea","Nanai","Niko","Niu","Paea","Palamo","Papani","Pelesa","Perelini","Pule","Pulefaasisina","Safenu","Sale","Salesa","Saluni","Sapani","Sativaa","Savali","Savaliga","Savea","Seiuli","Seko","Seuava","Sifu","Silao","Siosifa","Siulai","Suega","Taalitua","Taito","Talatonu","Tamatoa","Tameifuna","Tanielu","Tau","Tauaalo","Taualai","Tauati","Taueu","Taupo","Tautu","Tele","Tilo","Timu","Toelau","Toleafoa","Tonumaipe'a","Tuala","Tufele","Tui","Tuiaa","Tuiasosopo","Tuigamala","Tuitama","Tupu","Tupua","Tuputala","Uta'i","Vailili","Vavau"];

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