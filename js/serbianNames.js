function nameGen(type){
	var nm1 = ["Časlav","Čedomir","Đoko","Đorđe","Đorđije","Đurađ","Đura","Đuro","Žarko","Željko","Živan","Živko","Živojin","Živorad","Života","Aca","Adam","Aleksa","Aleksandar","Anastasije","Andrej","Andrija","Arsenije","Atanasije","Avram","Berislav","Blagoje","Boško","Boža","Božidar","Boban","Bogdan","Bogoljub","Bojan","Boris","Borislav","Borivoje","Borjan","Braco","Brajan","Brajko","Branimir","Branislav","Branko","Bratislav","Budimir","Cvetko","Cvijetin","Dabiživ","Dalibor","Damir","Damjan","Danijel","Danilo","Danko","Darko","David","Davor","Dejan","Desimir","Dimitrije","Dobrivoje","Dobroslav","Draško","Dražen","Dragan","Dragiša","Drago","Dragoje","Dragoljub","Dragomir","Dragoslav","Dragutin","Dušan","Dubravko","Emilijan","Filip","Filotije","Gabrijel","Gavrilo","Gligorije","Gojko","Goran","Gordan","Grgur","Grigorije","Hvalimir","Igor","Ilarion","Ilija","Ingwar","Ivan","Ivica","Jakov","Janko","Jezdimir","Jovan","Jugoslav","Kalinik","Konstantin","Kosta","Kostadin","Kristijan","Krsto","Kuzman","Lazar","Lješ","Ljuba","Ljubiša","Ljubisav","Ljubivoje","Ljubomir","Lubomir","Luka","Marinko","Marko","Matija","Matko","Miša","Miško","Mihailo","Mihajlo","Mijat","Mika","Mikica","Miladin","Milan","Milanko","Milenko","Mileta","Milić","Milivoj","Milivoje","Miljan","Miljko","Milko","Miloš","Miloje","Milomir","Milorad","Milovan","Milutin","Miodrag","Miomir","Miran","Mirko","Miroslav","Mitar","Mladen","Mojsije","Momčilo","Momir","Nebojša","Nedeljko","Nemanja","Nenad","Neven","Nikša","Nikola","Novak","Obrad","Obren","Ognjen","Pavle","Pera","Petar","Predimir","Predrag","Pribislav","Raško","Radenko","Radič","Radiša","Radivoje","Radmilo","Radoš","Radoje","Radojko","Radoman","Radomir","Radonja","Radoslav","Radovan","Radul","Rajko","Ranko","Rastko","Ratimir","Ratko","Risto","Saša","Sava","Savatije","Sergej","Simo","Siniša","Slaven","Slaviša","Slavko","Slavoljub","Slavomir","Slobodan","Spasoje","Srđan","Srećko","Sredoje","Sreten","Sretomir","Staniša","Stanimir","Stanislav","Stanko","Stanoje","Stefan","Stevan","Stojan","Stracimir","Strahinja","Svetislav","Svetozar","Tadija","Teodor","Teodosije","Tihomir","Todor","Toma","Tomislav","Uroš","Vasilije","Vasko","Velibor","Velichko","Velimir","Velizar","Veljko","Veselin","Višeslav","Vidak","Vidoje","Vikentije","Vitomir","Vlada","Vladan","Vladeta","Vladimir","Vladislav","Vlado","Vlatko","Vojin","Vojislav","Vojkan","Vujadin","Vuk","Vukašin","Vukajlo","Vukan","Vukmir","Vukota","Vuksan","Zdeslav","Zdravko","Zlatan","Zlatko","Zoran","Zvezdan","Zvonimir","Zvonko"];
	var nm2 = ["Đurica","Žaklina","Adrijana","Aleksandra","Amina","Anđela","Ana","Anastasija","Andrea","Andrijana","Anica","Anja","Anka","Biljana","Blagica","Bobana","Bogdana","Bojana","Bora","Borka","Bosiljka","Branka","Dajana","Daliborka","Damjanka","Dana","Danica","Danijela","Danka","Darija","Darina","Darinka","Dejana","Desanka","Dijana","Divna","Dobrica","Dobrila","DoroteaLalić","Draga","Dragana","Dragica","Draginja","Dušanka","Dušica","Duška","Dubravka","Dunja","Elena","Emilija","Gabrijela","Gorana","Gordana","Hana","Ivana","Ivanka","Jadranka","Jana","Jasmina","Jasna","Jelena","Jovana","Jovanka","Katarina","Kristina","Ksenija","Lada","Leposava","Lidija","Ljiljana","Ljuba","Ljubica","Ljubinka","Ludmila","Magdalena","Maja","Malina","Marica","Marija","Marina","Mila","Milana","Milanka","Milena","Milica","Miljana","Milka","Mina","Minna","Mira","Mirjana","Mirka","Mirna","Nađa","Nada","Nadezhda","Nastja","Nataša","Natalija","Natasa","Neda","Nevena","Nikolina","Nina","Olga","Peruna","Petra","Petrija","Radana","Radina","Radmila","Radojka","Rakita","Renja","Roksana","Ruža","Ružica","Sandra","Sanja","Sara","Sava","Simonida","Slađana","Slava","Slavica","Slavka","Slobodanka","Smiljana","Snežana","Sofija","Sonja","Sonya","Stanislava","Stefana","Steva","Stojanka","Suzana","Svetlana","Tamara","Tanja","Tatjana","Teodora","Tijana","Una","Varadinka","Vera","Verica","Veselinka","Vesna","Vida","Violeta","Vladana","Vlatka","Vojislava","Vujica","Vukica","Zeljana","Zlata","Zora","Zorana","Zorica","Zorka"];
	var nm3 = ["Čarapić","Đorđević","Šaponjić","Šiljan","Živanović","Živić","Aleksić","Andrić","Antić","Arsić","Bačić","Blagojević","Bojanić","Bojević","Borisavljević","Borisov","Brđanin","Brkić","Cvetković","Dapčević","Darković","Despotović","Ević","Filipović","Gavrilović","Georgijević","Gišić","Gojković","Golubović","Grgurović","Hristov","Ignjatović","Janketić","Janković","Jelić","Jocić","Jovanović","Jović","Karanović","Kostić","Krsmanović","Krstić","Kuzmanović","Lazarević","Lazić","Mandić","Marinković","Marković","Mijatović","Moldovan","Nanuševski","Nastasić","Nešić","Nedeljković","Nestorovski","Nikolić","Novaković","Obradović","Pajić","Pap","Pavlović","Pešić","Pejakovski","Pejić","Petrović","Popadić","Popović","Rajković","Rakočević","Ristić","Ristovski","Sandić","Savić","Savićević","Simić","Stefanović","Stevanović","Tadić","Tanacković","Tasić","Todorović","Tomić","Trkulja","Ugljanin","Urošević","Vasić","Vasiljević","Velimirović","Vladić","Vladimirović","Vlahović","Vujić","Vukašinović","Vukomanović","Zebić","Zorić"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm3.length);
		nm3.splice(rnd2, 1);
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			nm2.splice(rnd, 1);
			names = nm2[rnd] + " " + nm3[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			nm1.splice(rnd, 1);
			names = nm1[rnd] + " " + nm3[rnd2];
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