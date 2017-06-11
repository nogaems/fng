function nameGen(type){
	var tp = type;
	if(tp === 1){
		var names1 = ["Aah","Ah","Amen","Amun","Ankh","Bek","Bith","Ebon","Hal","Hab","Hem","Hon","Is","Kam","Kar","Kan","Khep","Khuns","Mak","Mad","Manet","Meh","Mer","Mukan","Mum","Naham","Nan","Nef","Nen","Nes","Nofr","Nub","Olab","Pen","Ran","Raz","Sam","San","Sen","Shen","Shan","Tam","Ten","Tet","Therm"];
		var names2 = ["agara","anath","ankhnas","arama","arta","astis","atra","ekhu","ela","emi","enen","enet","ense","epet","erit","es","ese","iah","ibah","ibeu","ika","ila","ilah","ima","ina","inah","inoe","ira","irye","isi","isis","itis","iya","iza","onee","orisis","otep","ukura","unta","ura","utaraa","utis"];
	}else{
		var names1 = ["Aah","Aakh","Abaal","Abay","Abdil","Abdam","Abub","Abus","Abuskh","Achen","Acher","Amen","Ankh","Apron","Baken","Bakar","Chat","Dar","Fen","Fun","Hak","Ham","Han","Har","Hek","Hor","Im","Jab","Jaf","Kam","Kak","Kef","Khab","Khaf","Khons","Man","Makal","Mem","Menk","Ment","Nar","Neb","Nekht","Osir","Osor","Pad","Phan","Phrah","Psam","Sem","Seph","Ser","Sok","Smen","Tab","Tah","Tat","Thoth","Thutm","Tosor"];
		var names2 = ["aesis","ahersef","aka","akar","akaruti","aken","akhsas","amelek","amen","aphos","aphres","aphris","apis","asenb","astes","auhor","ehemto","ekhet","ekhtou","emheb","emhebi","emhet","emhotep","enaten","ennifi","entu","ephers","epthah","epthes","eramen","erermes","eres","eri","erres","ertum","eru","erumes","esseker","ihiti","iris","is","isaba","otep","oteph","oubis","ouris","ubis","umah","urmes"];
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