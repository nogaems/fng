function nameGen(){
	var nm1 = ["Abbi-Teshub","Akhsheri","Aki-Teshup","Akia","Alakshandu","Alarandu","Ambaris","Ammikhatna","Anittas","Anuwanza","Arame","Arandas","Arandash","Arnuanta","Arnuwandas","Artatamash","Asiri","Aulkia","Bakhianu","Bit-Burutish","Biyassili","Burutash","Dudkaliya","Dudkhalia","Dushratta","Erisinni","Esarhaddon","Etaqama","Gil-Teshup","Giliyash","Gunzinanu","Hasammeli","Hattusilis","Hishimisharruma","Ishganshar","Ishtanu","Kali-Teshup","Karparune","Katuzili","Khalpashshulubis","Khapashshubilish","Khattasulis","Khattushar","Khulli","Kielranu","Kil-Teshup","Kili-Teshup","Kilundu","Kundashpi","Kurirpa","Kuruntash","Kushtashpi","Labarnas","Lubarna","Lutipri","Manapa-Tarhunda","Manapa-Teshup","Murshil","Murshilish","Mursilis","Mutallu","Muttallu","Muwatalis","Muwatallis","Nabushezibanni","Pappash","Pikkandu","Pilandu","Pisandu","Pisiris","Pisirish","Piyamaradus","Purutash","Qatazilu","Sangar","Sapalulme","Sardur","Shadi-Teshup","Shalmaneser","Shama-Teshup","Sharkenkate-Ashira","Shaushkash","Shipa","Shirindu","Shubbiluliuma","Sin-Teshupash","Suppiliamus","Suppiliumash","Suppiluliuma","Surash","Surri","Sutarna","Sutatarra","Tarhu","Tarhunnas","Tarkhundapi","Tarkhundaraba","Tarkhundarabush","Tarkhuntash","Tarkondemos","Tashshu-Dasha","Te-Teshub","Telipinus","Teshub","Teti","Tudhaliuas","Tudhaliyas","Tudkhalias","Tudkhaliya","Tushratta","Ualli","Uassurme","Ullusunu","Urhiteshub","Uriah","Urikki","Urimme","Ushkhitti","Zananzash","Zannanza","Zurashar"];

	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		names = nm1[rnd];
		nm1.splice(rnd, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}