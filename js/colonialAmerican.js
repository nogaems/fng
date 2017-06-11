function nameGen(type){
	var nm1 = ["Abel","Abiel","Abijah","Abimael","Abner","Abraham","Absalom","Adonijah","Ajax","Alden","Amias","Amiel","Ammiras","Amos","Amzi","Ansel","Archibald","Asa","Asahel","Azariah","Balthasar","Barnabas","Bartholomew","Bazel","Benajah","Boaz","Chauncey","Christopher","Clement","Comfort","Constant","Cotton","Cyrus","Degory","Duncan","Ebenezer","Edward","Elbert","Eleazar","Eleazer","Eli","Eliab","Eliakim","Elias","Elihu","Elijah","Eliphalet","Elisha","Emanuel","Emory","Enoch","Enos","Ephraim","Experience","Ezekiel","Francis","Garvan","Gawen","Gerrard","Gideon	","Gideon","Giles","Hannibal","Henry","Hercules","Hezekiah","Hiram","Holmes","Homer","Horatio","Hosea","Increase","Isaac","Isaiah","Isham","Israel","Jabez","James","Jared","Jasper","Jedidiah","Jehu","Jeremiah","Jethro","Job","John","Jonas","Josiah","Jothan","Kenelm","Lazarus","Lemuel","Levi","Linus","Love","Matthias","Micajah","Miles","Moses","Myles","Nehemiah","Noble","Obadiah","Oceanus","Philo","Philomon","Phineas","Prosperity","Reason","Resolved","Richard","Robert","Rufus","Salmon","Sampson","Samuel","Seth","Silas","Simon","Solomon","Thaddeus","Theophilus","Thomas","Truth","William","Wrestling","Zaccheus","Zachariah","Zadock","Zadok","Zebulon","Zephaniah","Zophar"];
	var nm2 = ["Abigail","Abitha","Alice","Amity","Ann","Anne","Aphra","Aurinda","Azuba","Candace","Catherine","Charity","Charlotte","Chastity","Clarity","Comfort","Constance","Cornelia","Damarus","Deliverance","Desire","Dorcas","Dorothy","Edith","Eleanor","Electa","Eliza","Elizabeth","Ellen","Emeline","Ester","Esther","Experience","Fanny","Felicity","Fidelity","Georgine","Grace","Harriet","Hecuba","Helen","Henrietta","Hephzibah","Hepzibah","Hester","Humility","Increase","Isabella","Jane","Joan","Joy","Judith","Katherine","Keturah","Keziah","Lydia","Mahala","Martha","Mary","Mercy","Modesty","Patience","Phila","Phoebe","Piety","Primrose","Priscilla","Prosperity","Prudence","Reason","Rebekah","Remember","Rosanna","Rose","Sarah","Selah","Silence","Susanna","Tabitha","Temperance","Thankfull","Theodosia","Truth","Verity","Virginia","Zipporah"];
	var nm3 = ["Adair","Adams","Aigar","Alexander","Allen","Alloways","Amos","Anderson","Andrews","Atkins","Attyte","Badders","Bailey","Baird","Barnard","Barnet","Barnett","Barton","Bean","Bennett","Best","Bohannon","Bohnanon","Bond","Bourne","Bowles","Boyd","Bradley","Bradshaw","Brady","Brannon","Brown","Buchannon","Caldwell","Camble","Carson","Chamberlain","Chambers","Channel","Clark","Clement","Clements","Collins","Cooper","Cord","Cornelius","Couzens","Cowan","Cowgil","Cowgill","Crawford","Cresswell","Criswel","Crockett","Cromey","Crummey","Cunningham","Curley","Davison","Dickson","Dinsmore","Dixon","Dodson","Donald","Donnell","Doran","Doras","Duncan","Dunlap","Eastburn","Eaton","Ebaugh","Edgar","Edmiston","Edmundson","Elder","Emenheiser","Emmitt","Erwin","Ewing","Fansant","Farr","Feit","Foster","Fulton","Galbraith","Gale","Gest","Gibson","Gillcrest","Glasgow","Gordon","Gorley","Graham","Graydon","Griffith","Grove","Growden","Hair","Hall","Hamilton","Hartman","Hawkins","Hershey","Hill","Hopkins","Hughey","Irwin","Jarret","Jarrett","John","Johnston","Jones","Jordan","Kenly","Kennard","Kersey","Kilgore","Kimble","Kincaid","Kinnard","Kirk","Kisiner","Lanius","Lawson","Leeper","Lewden","Ligget","Liggett","Liggit","Lineboro","Litten","Livingston","Lukey","Mackey","Major","Manifold","Mantle","Mare","Marlin","Martin","Mason","Matthews","McCalla","McCalmont","McCanless","McCaskey","McClelland","McClemont","McConnal","McConnel","McCord","McCourtney","McCoy","McCullough","McCurdy","McDaniel","McFadden","McGee","McMullen","McNamee","McPherson","Means","Mears","Miller","Milligen","Millikan","Milliken","Mitchell","Moffett","Montgomery","Morgan","Morris","Morrison ","Munn","Murphy","Murray","Neiper","Nichol","Nichols","Nickle","Oâ€™Brian","Obrian","Oliver","Onion","Osborn","PERKINGS","Paine","Parker","Patterson","Payne","Pedan","Pennel","Perkins","Peters","Pickart","Pierson","Poole","Power","Price","Purdy","Pymer","Quigly","Ramsey","Redman","Reed","Richardson","Robinson","Rogers","Roland","Ross","Rouse","Rowan","Sample","Schotts","Scott","Scotts","Semple","Siddall","Sinclair","Sinkler","Smille","Smith","Snyder","Stalsworth","Stedman","Steel","Sterret","Sterrett","Stevenson","Stewart","Suitor","Switzer","Taggert","Taylor","Templeton","Thompson","Tomkin","Toule","Traverse","Vansant","Wallace","Watt","Webb","Wentz","West","White","Whiteford","Whitelock","Wiley","Williams","Williamson","Wilson","Wise","Woodbury"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm3.length);
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd] + " " + nm3[rnd2];
			nm2.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
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