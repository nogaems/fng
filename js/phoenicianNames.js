
function nameGen(type){
	var nm1 = ["Abdastartus","Abdeshmun","Abdmelqart","Abdosir","Abibaal","Adad","Addir","Addonia","Aderbaal","Adohnes","Adon","Adones","Adonia","Adoniah","Adonias","Adonibaal","Adonis","Adonys","Ahinadab","Ahiram","Ahirom","Akbar","Amilcare","Anibal","Annaba","Annibale","Aqhat","Aradus","Arvad","Ashtartyaton","Ashtzaph","Astartus","Azmelqart","Baalhanno","Baalshillek","Baldassare","Baldo","Baltasar","Baltazar","Balthasar","Balthazar","Balthezar","Baltsar","Baltser","Balzer","Barekbaal","Batrun","Bedezorus","Beirut","Belshazzar","Berut","Bodashtart","Bodeshmun","Bodinelqart","Bodmelqart","BoldizsÃ¡r","Botrys","Byblos","Carthage","Danel","Donis","Eshmun","Eshmunamash","Eshmunazar","Gebal","Germelqart","Hailama","Hamilcar","Hammon","Hanibal","Hannibal","Hanno","Hasdrubal","Himilco","Hiram","Hyrum","Itthobaal","Jebel","Kanmi","Khilletzbaal","Maharbaal","Melqartpilles","Milkherem","Milkpilles","Milkyaton","Paltibaal","Philosir","Qarnaim","Resheph","Sakarbaal","Shamayim","Shemen","Sidon","Sikarbaal","Tabnit","Tammuz","Tyre","Ugarit","Utica","Yarikh","Yehawwielon","Yutpan","Zephon","Zidon","Zimrida"];
	var nm2 = ["Adoncia","Adonia","Adoniah","Adonica","Adonna","Adonya","Adonyah","Alissa","Amatashtart","Amatbal","Amma","Amotmilqart","Anath","Arashtibal","Arisha","Arishat","Arishot","Arshut","Ashdanot","Ashdonbal","Asherah","Ashmonrabti","Ashtoreth","Astarte","Athirat","Azibal","Baalat","Barkitbal","Batnoam","Birkana","Birkanda","Bisha","Bitnima","Coriander","Coriender","Coryander","Coryender","Demna","Dido","Domina","Elissa","Emeshmoon","Imashmon","Imashtart","Izabel","Izavel","Jesibel","Jessabel","Jessebel","Jetzabel","Jez","Jezabel","Jezabella","Jezebel","Jezebela","Jezebele","Jezebelle","Jezibel","Melita","Mitunbaal","Muttunbaal","Nikkal","Pawly","Quarta","Septy","Shapash","Shiba","Sisa","Tanis","Tanit","Tanith","Tanitha","Tanithe","Tanni","Tanyih","Tanyth","Tanythe","Ummashtart","Yasha","Zibqet"];

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