function nameGen(type){
	var nm1 = ["Ablabius","Achila","Agila","Agiwulf","Agriwulf","Aidoingus","Aithanarid","Alaric","Alatheus","Alaviv","Alica","Aligern","Alla","Amal","Amalaric","Ammius","Anagastes","Andagis","Anianus","Ansila","Ansis","Aoric","Apahida","Ardabur","Ardaric","Argaith","Ariaric","Arimir","Arius","Arnegliscus","Arvandus","Asbad","Aspar","Ataulf","Ataulph","Athalaric","Athanagild","Athanaric","Atharid","Athaulf","Babai","Badua","Baduila","Baza","Berig","Berimud","Berimund","Bessa","Bessas","Bessi","Beuca","Beucad","Bigelis","Bilimer","Borani","Braga","Brandila","Candac","Cannabas","Cannabaudes","Cethegus","Chindasuinth","Cniva","Cnivida","Colias","Crocus","Cunigast","Cunimund","Cyrila","Dubius","Duda","Ebermud","Eberwolf","Ebrimud","Edica","Eraric","Eriulf","Ermanaric","Ermelandus","Ervig","Euric","Eutharic","Farnobius","Fastida","Feletheus","Feva","Filimer","Flaccitheus","Fravitta","Fredegar","Fretela","Frideric","Fridigern","Frigeridus","Frithila","Fritigern","Gadaric","Gainas","Gaiseric","Galindo","Galindus","Gaut","Gauterit","Geberic","Gelimer","Gento","Gerung","Gesalec","Gesimund","Getica","Goar","Goddas","Godegisel","Godigisclus","Goiaricus","Gouththas","Gundehar","Gundiok","Gundobad","Gunteric","Gunthigis","Gutthikas","Hadubrand","Heldebald","Heldefredus","Heribrand","Hermangild","Hermenigild","Herminafrid","Hernegliscus","Hildebad","Hildebrand","Hilderic","Hilderith","Himnerith","Hisarna","Hulmul","Huml","Huneric","Hunigild","Hunimund","Hunulf","Hunumund","Ibba","Ildebad","Inna","Irnfried","Jordanes","Lagariman","Lampridius","Leovigild","Leuvibild","Livila","Marcomir","Modaharius","Modares","Munderic","Mundo","Namatius","Naulabates","Nidada","Niketas","Odoin","Odotheus","Odovacar","Ostrogotha","Osuin","Ovida","Patza","Radagaisus","Rausimod","Recared","Reccared","Recceswinth","Rechiar","Rechimund","Recitach","Rekitach","Remismund","Respa","Retemeris","Rhima","Ricimer","Rictiovarus","Rikiar","Roderic","Rodolf","Roduulf","Rudesind","Saba","Sadagares","Safrax","Salla","Sangiban","Sansalas","Saphrax","Sarus","Segeric","Selenas","Shapur","Sidimund","Sigeric","Sigesar","Sigibald","Sigismund","Sigisvult","Sindila","Sisbert","Sisebut","Sisenand","Soas","Suatrius","Sueridus","Sunericus","Sunnia","Tanais","Tanca","Teias","Teja","Tharuaro","Thela","Theodahad","Theodehad","Theodemer","Theoderic","Theoderid","Theodoric","Theodulf","Theudegisel","Theudegisklos","Theudis","Thidrek","Thiudimir","Thorismud","Thorismund","Thrasamund","Thrasaric","Thraustila","Totila","Tribigild","Tufa","Tuluin","Ulfilas","Unigild","Unila","Unimund","Uraias","Valamer","Valamir","Valaravans","Valia","Vandalarius","Vandil","Veduco","Vetericus","Vetranio","Videric","Vidigoia","Vidimir","Viliaris","Vinitharius","Visimar","Vithimiris","Vithmiris","Vitigis","Vittamar","Vultuulf","Wala","Walahmar","Wallia","Wamba","Wella","Winguric","Witige","Wittigis","Wittiza"];
	var nm2 = ["Aalissa","Adosinda","Aleyda","Algonda","Alisa-Sophie","Alwina","Amala","Amalafrida","Amalasontha","Amalasuintha","Amalasuntha","Amalaswinth","Amalaswintha","Amalberga","Amalberta","Amalburga","Amalda","Amalfrida","Amalfrieda","Amalfriede","Amalgard","Amalgunda","Amalgundis","Amalina","Amalindis","Amalwara","Amelie","Amelina","Anouk","Areagne","Arika","Attala","Avagisa","Avina","Bjarka","Brenhilda","Brunhilda","Brunichild","Brunihild","Buffy","Chlodoswintha","Chlotsuintha","DÃ¶rthe-Julia","Elianor","Elisaweta","Elja","Emalia","Emelia","Ereleuva","Erelieva","Feenja","Fredegonda","Gaatha","Gailavira","Gailesvintha","Garsendis","Geleswintha","Geloyra","Gelvira","Giso","Glismoda","Goisvintha","Gosvintha","Gudeliva","Heidrun-Gabriela","Helchen","Hermangild","Hermesind","Heva","Hilduara","Hunila","Jeanne-Alice","Kaethe","Kriemhild","Limiteti","Lioba","Liuva","Lorelei","Lucienne","Malasintha","Matasuntha","Matasvintha","Megan-Laureen","Melisanda","Melisande","Melisenda","Melle","Melusine","Mia-Selina","Mira","Monia","Narin","Oonagh","Ostrogotho","Radegond","Radegonda","Rasha","Rautgundis","Richildis","Riciberga","Seda","Sunigilda","Sunilda","Talida","Teja","Theodananda","Thiudigotho","Vadamerca","Valdamerca","Wilgefortis"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
			nm2.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
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