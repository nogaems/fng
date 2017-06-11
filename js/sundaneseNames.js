
function nameGen(type){
	var nm1 = ["Aa","Aam","Aang","Ace","Aceng","Adang","Ade","Adeng","Adun","Aep","Agah","Agan","Ageng","Agus","Ahmad","Ajang","Ajat","Amar","Amat","Amin","Amir","Ammaar","Anang","Aqan","Asep","Asta","Astrajingga","Atang","Atep","Atong","Badjuri","Bagja","Bagong","Barna","Bayu","Botak","Cahya","Cece","Ceceng","Cecep","Cepot","Cucu","Dadan","Dadang","Dana","Dani","Dawala","Dayat","Deden","Dedeng","Dedi","Dewata","Dewawarman","Dian","Didin","Djaka","Durahman","Ece","Edi","Eep","Elan","Empep","Ence","Encep","Endang","Endeung","Engkos","Engkus","Enjang","Entang","Fauzan","Galih","Gandana","Ganjar","Gareng","Gembira","Gilang","Ginanjar","Gugum","Gugun","Gumbira","Gumelar","Gun-gun","Guna","Hamdan","Hardi","Harisdarma","Harja","Harsana","Hendra","Henhen","Hikmat","Idang","Idi","Idih","Ihin","Ijang","Indra","Jajang","Jaka","Jalu","Jangkung","Jaya","Jayadarma","Kabayan","Kamandaka","Karta","Kartasasmita","Kertarajasa","Komar","Koswara","Kurniawan","Kuswara","Kusworo","Lalan","Linggabuwana","Maman","Mamat","Markasih","Marsudi","Memed","Mulyana","Nanang","Nandang","Nang","Nataprawira","Nugraha","Odang","Oleh","Oman","Oto","Otong","Otoy","Parta","Pepep","Permana","Petruk","Prawatasari","Prawira","Prawiraharja","Purnama","Purnawarman","Ragasuci","Raharja","Rahmat","Rakha","Romli","Rosidi","Sadeli","Sanjaya","Sapari","Sapariah","Sasmita","Sastranagara","Semar","Sepri","Sesep","Setiadji","Setiaji","Sobarna","Solihin","Soma","Somawisesa","Sudarsana","Sudarsono","Sudirja","Sudrajat","Suganda","Sujana","Sujoni","Sukarsa","Sukarso","Sukarya","Sumantri","Supardi","Sura","Surawijaya","Surya","Suteja","Sutikno","Sutisna","Sutresna","Sutrisno","Tangguh","Tata","Tatang","Tetep","Tirta","Tisna","Totong","Udung","Ujang","Ule","Undang","Usep","Uus","Wahyu","Waluya","Wawan","Wijaya","Wisesa","Wowon","Yanyan","Yayan","Yayat"];
	var nm2 = ["Adang","Ade","Ai","Ani","Asih","Atikah","Ayi","Cempaka","Dadah","Dahlia","Dasimah","Dedeh","Denok","Dewi","Diah","Dian","Eem","Een","Ela","Ema","Emar","Enah","Enang","Endah","Eneng","Engkom","Ening","Enok","Enong","Entin","Eros","Esih","Etty","Euis","Galuh","Gina","Icih","Ida","Idah","Iin","Ijah","Imas","Ira","Irma","Ita","Iteung","Itoh","Iyah","Jayanti","Kanaya","Kania","Karomah","Kartika","Kartikasari","Karto","Kencana","Khodijah","Kokom","Komariah","Lia","Lilis","Lina","Malati","Mamah","Mariah","Mariam","Meida","Melati","Nani","Nenden","Neneng","Neni","Neny","Nia","Nining","Nonon","Nunung","Nurlaela","Nurlela","Nyai","Ocih","Odah","Omah","Ombah","Omoh","Onong","Oom","Pitaloka","Purbasari","Puspita","Putri","Ratih","Ratna","Ratnasari","Ratnasih","Ratu","Rela","Rella","Rengganis","Rusita","Sadiyah","Saidah","Saodah","Sapariah","Sari","Sartika","Sekar","Sinar","Suminar","Tati","Teti","Tia","Tiktik","Tini","Tirta","Tita","Titin","Ule","Unung","Wati","Wida","Wulan","Wulansari","Yani","Yanti","Yayah","Yoyoh","Yuyu","Yuyun"];

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