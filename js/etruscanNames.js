
function nameGen(type){
	var nm1 = ["Aranth","Aranthur","Arnth","Arnthur","Arnza","Arte","Aule","Aulza","Cae","Cai","Caille","Ccaile","Cneve","Cuinte","Cure","Cutu","Kaisie","Kavie","Lar","Larce","Laris","Lars","Larth","Larza","Laxu","Lecne","Luci","Mamarce","Marce","Metie","Nerie","Numesie","Pesna","Plecu","Pup","Pupli","Rasce","Sethre","Shertur","Spurie","Spurinna","Sure","Tages","Tarquin","Tarxi","Teitu","Teucer","Thefarie","Thefri","Thesanthei","Thocero","Thresu","Thucer","Tite","Vel","Velthur","Velxe","Venel","Venthi","Venza","Vulca"];
	var nm2 = ["Alfia","Arathia","Araziia","Arnthi","Arnthia","Arntlei","Arria","Arunthia","Ati","Atilia","Aula","Aulia","Caesia","Cafatia","Caia","Cainei","Culni","Fasti","Fastia","Hasti","Hastia","Hercna","Hethli","Larcia","Lartha","Larthi","Larthia","Messia","Metli","Munatia","Nerinai","Panatia","Peci","Perca","Pevtha","Pinaria","Ramtha","Ramthia","Ramutha","Rantha","Raunthu","Ravntha","Ravnthy","Scarpia","Seianthi","Seianti","Semni","Sesanseia","Sethra","Sethria","Stenia","Tetia","Thana","Thanchvil","Thancvil","Thania","Thanica","Thanusa","Thanxvil","Thiphilia","Thiphilnia","Thupeltha","Tita","Veilia","Vela","Velia","Velthuria","Vesia","Vitellia","Vivinna"];
	var nm3 = ["Acilu","Aclni","Acsi","Alfa","Alfni","Alpiu","Alu","Alvni","Amre","Amthne","Anani","Anei","Ani","Apice","Aprthe","Aris","Arntile","Artni","Artnle","Ashia","Ataris","Ate","Athnu","Aule","Aulni","Avaini","Avle","Axu","Axuni","Cacni","Cae","Cai","Calisna","Calisni","Canath","Cancu","Canthusa","Carcu","Casni","Cazrtu","Cencu","Cestna","Cesu","Cicu","Claniu","Clanti","Clauce","Cnare","Cnevna","Crapilu","Craufa","Craupa","Creice","Crespe","Cretly","Cucu","Cuishla","Culpiu","Cumere","Cutlis","Cutu","Cvenle","Eple","Etrnis","Faltusa","Faru","Fastntru","Ferme","Feru","Fetiu","Frentinate","Fulu","Halistre","Haltu","Hamphna","Hanu","Hanusa","Hele","Helzu","Hercle","Herini","Herme","Hisu","Hulu","Hurace","Huzlu","Ianzu","Larce","Larci","Larthru","Latini","Latuni","Lecne","Leixu","Lentis","Lethiu","Letis","Leusa","Litithe","Lule","Lupu","Lusce","Luscesa","Macre","Macute","Marale","Marcna","Marcni","Masu","Meluta","Metus","Minate","Mlnane","Mute","Namult","Natis","Nemsu","Nufre","Nufrzna","Numna","Numsi","Nurziu","Nushte","Paci","Pacre","Papa","Patu","Pece","Penthe","Peris","Pestiu","Pethna","Petru","Phauxa","Phauxane","Phesu","Piste","Plancure","Plaute","Precu","Prexu","Prute","Pulfna","Pulpae","Pultus","Pumpna","Pumpu","Purni","Rafe","Ranazu","Raufe","Razis","Remzna","Resciu","Rufe","Rusina","Rutane","Saeru","Sale","Satna","Sceva","Scire","Secu","Seiante","Sentinate","Sepre","Serice","Sethre","Sethrni","Shali","Shalie","Shalvi","Shelvashl","Shemna","Shene","Shepu","Sherturi","Shinu","Shuza","Spaspu","Strume","Sulu","Svea","Svetu","Talce","Taphu","Teltiu","Teti","Tetina","Thansi","Thare","Theprini","Theresh","Thethure","Thuceri","Thurmna","Tiazu","Tite","Tlapu","Tlapuni","Tlesna","Trepa","Trepu","Tumu","Tushnu","Tutna","Ucar","Ulthe","Umithe","Umpre","Urfa","Uthle","Uvilane","Uxumzna","Valashna","Vari","Varna","Varni","Velcialu","Veli","Velimna","Velsi","Venetesh","Vente","Venu","Vepu","Vercna","Verpe","Versni","Veru","Vescu","Veti","Vetu","Vezra","Vilia","Vipi","Visce","Zixu","Zuxu"];
	var nm4 = ["Acilunia","Acilunn","Aclinia","Acsi","Alcni","Alfania","Alfnia","Alpui","Aluni","Alunia","Amria","Amthni","Amthnia","Ananla","Aneinei","Aneinia","Ani","Apicnei","Aprthia","Arigia","Arntilia","Arntnei","Ashiania","Atarissia","Athnu","Athnui","Atia","Aulia","Aulni","Aulnia","Avainia","Axui","Axunei","Axuni","Cacni","Cai","Cainei","Calisnei","Calisnia","Cancunia","Canetha","Canthusania","Carcui","Carcunia","Casnia","Cazrtunia","Cencunia","Censunia","Cestnei","Cicunia","Claniuniu","Clanti","Claucia","Cnaria","Cnevnei","Crapilunia","Craufania","Craupania","Creicia","Crespia","Cretlu","Cucunia","Cuishlania","Culpiunia","Cumeria","Cumurunia","Cutlisnei","Cutui","Cutunia","Cvenlia","Eplia","Etanigia","Faltusania","Farui","Fastntrunia","Fermia","Ferui","Ferunia","Fetiunia","Freninatia","Fului","Fuluni","Halistrea","Haltuni","Hamphnei","Hanunia","Hanusnei","Helia","Helzunia","Herclenia","Hermia","Hirinia","Hisunia","Huluni","Huracia","Huzlunia","Ianzunia","Larci","Larcia","Larthruni","Latini","Latithia","Latuni","Lecnia","Leixunia","Lentisnei","Lethiunia","Letisa","Leusei","Lulia","Lupunia","Luscenia","Luscesei","Macri","Macutia","Maralia","Marcnei","Masui","Melutnei","Metusnei","Minatia","Muteni","Mutenia","Namulta","Nemsdui","Netienei","Nufria","Nufrznei","Numnei","Numsinei","Nurziunia","Nushtenia","Nusthia","Pacinei","Pacrenia","Papania","Patunia","Peciania","Penthia","Perisnei","Pestui","Pestuinia","Pethnei","Petrui","Phauxania","Phesu","Pistia","Plancuria","Plauti","Precuni","Precunia","Prexunia","Prutia","Pulfnei","Pulpainei","Pultunia","Pumpnei","Pumpuni","Purninei","Rafia","Ranazunia","Raufia","Razisnei","Remznei","Resciunia","Rufia","Rusinei","Rutania","Salla","Sameruni","Samerunia","Satnei","Scevania","Sciria","Secunia","Seianti","Sentinati","Sepria","Sericia","Sethria","Sethrnei","Shalia","Shalvi","Shalvia","Shelvashlia","Shemnei","Shenevia","Shepunia","Sherturi","Shinunia","Shuzania","Spaspunia","Strumiana","Sulunia","Svenia","Svetunia","Talcei","Taphunia","Teltiunia","Tetinei","Tetu","Thansinei","Tharia","Thepainia","Theresha","Thethuria","Thuceria","Thurmnei","Tiazunia","Titi","Tlapuni","Tlapunia","Tlesnei","Trpei","Trpunia","Tumunia","Tushni","Tutnei","Ucara","Ulthia","Umithea","Umprea","Urfania","Uthli","Uthlia","Uvilania","Uxumznei","Valcialui","Valshnei","Vari","Varnei","Varni","Veli","Velia","Velimnei","Velsi","Velsia","Venetesha","Ventia","Venunia","Vepunia","Vercnei","Verpia","Versnia","Verunia","Vescunia","Veti","Vetui","Vezrania","Viliania","Vipi","Vipia","Viscenea","Viscenei","Viscia","Zixunia","Zuxunia"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.random() * nm2.length | 0;
			rnd2 = Math.random() * nm4.length | 0;
			names = nm2[rnd] + " " + nm4[rnd2];
			nm2.splice(rnd, 1);
			nm4.splice(rnd2, 1);
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm3.length | 0;
			names = nm1[rnd] + " " + nm3[rnd2];
			nm1.splice(rnd, 1);
			nm3.splice(rnd2, 1);
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