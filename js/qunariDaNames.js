var namesFemale = ["As","Bah","Bir","Birs","Can","Dem","Fad","Giz","Hat","Kar","Kard","Kub","Kubr","Kut","Mel","Naz","Nazl","Nih","Or","Ork","Oz","Ozen","Ras","San","Say","Sem","Ser","Sol","Solm","Sum","Tam","Tamg","Tur","Turn","Yas","Yasem","Yen","Yon"];
var namesFemale2 = ["a","aan","al","am","an","anem","ar","asan","ay","ayar","az","azik","azli","e","ek","elek","elen","em","emin","en","ena","ener","enli","er","era","et","ice","ide","ie","iha","ihan","ik","in","onal","ul","umer"];
var namesMale = ["Ak","Akin","Akor","Al","Ar","Aris","Arm","Arv","As","Ask","Askh","Asl","Bas","Bast","Bur","Dur","Gun","Gund","Gur","Gurh","Jar","Jarv","Kan","Ket","Kub","Mar","Met","Naz","Ok","Okan","Or","Orn","Oz","Ozk","Sal","Sen","S","St","Tam","Ten","Yag","Yagm"];
var namesFamily = ["aarad","aari","aas","aca","ad","ak","alit","amay","an","anat","aner","ant","arad","ari","as","at","ay","azim","ehan","ek","en","enol","er","ilay","im","iner","ishok","it","ogan","ojan","ok","ol","oren","ri","ug","ul","urak","urhan","utlu"];
var br = "";

function nameGen(namesMale, namesFamily){
	var names1 = namesMale;
	var names2 = namesFamily;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd0 = Math.floor(Math.random() * names1.length);
		rnd1 = Math.floor(Math.random() * names2.length);
		names = names1[rnd0] + names2[rnd1];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}