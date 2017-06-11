var nm1 = ['Ditid','Quivilt','Mohanlal','Sollix','Equinus','Gamjee','Matuna','Kurzol','Erodjan','Alwan','Anje','Azibo','Ajin','Ekon','Erasto','Haijen','Hamedi','Hokima','Jaafan','Jabir','Jalai','Javyn','Jijel','Juma','Jumoke','Kaijin','Kazko','Maalik','Makas','Malak','Nyabingi','Rahjin','Rakash','Rashi','Razi','Reji','Rujabu','Rujin','Seji','Senwe','Seshi','Teshi','Tzane','Tzuljin','Voyambi','Vuzashi','Vuzembi','Yamike','Yavo','Yawan','Zaejin','Zallah','Zebajin','Zelaji','Zevrij','Zinjo','Zufem','Alzim','Ayagi','Ayargajin','Dorkuraz','Hakalai','Halasuwa','Hokajin','Hoodah','Hyptu','Jaryaya','Jayunya','Jinjin','Jojin','Kelraz','Kuroji','Lakjin','Laojin','Melkree','Mezilkree','Napokue','Nuenvan','Paikei','Rapshider','Rhazin','Shaktilar','Shengis','Sligo','Tanjin','Tazingo','Tedar','Trezzahn','Trolgar','Ttarmek','Ugoki','Vekuzz','Venjo','Vulzal','Wanjin','Wonjin','Xukundi','Yetu','Zengu','Zoljin','Zulabar','Zulbaljin','Zulgeteb','Zulkaz','Zulkis','Zulrajas','Zulyafi','Zunabar'];
var nm2 = ['Gilta','Vitchen','Tirezi','Fefeya','Aradya','Nepita','Damari','Meenah','Kenaya','Vriska','Ajia','Aketa','Altoa','Aszea','Atae','Azra','Ecia','Ejie','Eleja','Esha','Illa','Kea','Keja','Kina','Kiya','Kizi','Moza','Oyana','Raca','Rasha','Seshia','Suja','Suli','Talisa','Tasiya','Tayo','Teja','Teza','Tezzi','Tizali','Xia','Yaci','Yajdna','Yashi','Yera','Yeree','Yesha','Yishi','Zara','Zashi','Zea','Zelea','Zesa','Zeti','Zola','Zoti','Zujia','Zyra','Alunja','Anji','Arany','Bajin','Baliaja','Benni','Bie','Boonoo','Bunjin','Csini','Feylin','Girisha','Hailith','Ithra','Javilla','Javinda','Jezemalu','Jinthaiya','Jiranty','Jozala','Jubukraa','Juljin','Kanjin','Katanja','Katzine','Khelynn','Khijazi','Khuwei','Kululu','Lujin','Makali','Mandula','Meimei','Melelea','Nelina','Prerrahar','Pujati','Rangi','Renjai','Renji','Ronjaty','Saedmara','Saonji','Segawa','Senzala','Shadrala','Shakawatha','Shaktila','Shamra','Sharimara','Shubre','Soniya','Sonja','Suliya','Sulynn','Titamor','Tsaijo','Usitutie','Valja','Vanjin','Venmara','Vinji','Vinjin','Vonjai','Vujii','Vulzala','Watu','Yuhai','Zalma','Zalmea','Zenma','Zhonya','Zhoumai','Ziataaman','Ziataima','Ziataja','Ziatajie','Ziatakraa','Zonraja','Zulja','Zulja','Zuljah','Zuljin','Zulkraa','Zulmara','Zulraja','Zulrea','Zulwatha'];
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