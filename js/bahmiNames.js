function nameGen(type){
	var tp = type;
	if(tp === 1){
		var names1 = ["Altan","Bat","Bayar","Bolor","Ene","Enkh","Erdene","Gan","Gerel","Hon","Khün","Khen","Khon","Mönkh","Medekh","Munkh","Muuno","Naran","Ner","Od","Ogt","Oyun","Oyuun","Saran","Sertuun","Solon","Ter","Uran"];
		var names2 = ["bileg","bish","chimeg","güi","gerel","go","gorzol","gorzul","jargal","khoi","maa","tsatsral","tsetseg","tungalag","tuyaa","val","zorig"];
	}else{
		var names1 = ["Bat","Batu","Chin","Chuluun","Ene","Enkh","Gan","Khün","Khen","Mönkh","Medekh","Munoo","Naran","Ner","Ogt","Otgon","Sühk","Tömör","Ter","Yul"];
		var names2 = ["baatar","bat","bataar","bayar","bish","bold","güi","gis","jargal","khan","khoi","saikhan","sukh","tulga","zorig"];
	}
	
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		rnd2 = Math.floor(Math.random() * names2.length);
		names = names1[rnd] + names2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}