
function nameGen(){
	var nm1 = ["ail","alder","amber","arach","ash","ashen","bane","bare","barren","bitter","black","bleak","bligh","blight","boon","brow","burn","cease","char","charring","ebon","onyx","cinder","clear","cold","crag","cri","crow","dark","dawn","death","deci","demo","dew","dia","diabo","dire","dread","dusk","dust","ember","fall","fallen","far","farrow","fes","fester","fire","flame","flaw","fog","fore","forge","forging","frost","full","gaze","ghos","gloom","glum","glumming","gore","gray","grim","grimming","hard","hazel","il","ill","kil","lo","lon","lone","low","mad","mali","mar","mause","maw","mise","mourn","mourning","mur","murk","nec","necro","nether","ni","nigh","night","pyre","reaper","reaver","ridge","rip","ripping","saur","scorch","ser","serpen","shadow","shar","shard","shel","shell","sla","slate","sly","spi","spine","talon","thorn","thorne","vile","vin","vine","wear","weep","weeping","wither","woe","wrath"];
	var nm2 = ["borough","brook","brooke","burg","burgh","burn","bury","fall","ford","fort","gate","helm","mere","mire","moor","more","moure","mourn","rest","ridge","thorn","thorne","ton","town","ville"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		while(nm1[rnd] === nm2[rnd2]){
			rnd2 = Math.floor(Math.random() * nm2.length);
		}
		names = nm1[rnd] + nm2[rnd2];
		nm1.splice(rnd, 1);
		nm2.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}