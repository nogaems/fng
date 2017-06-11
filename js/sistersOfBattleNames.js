var nm1 = ["Agn","Al","Alic","Am","An","Ar","Arab","Asp","Bell","Bren","Brig","Bris","Cel","Celest","Chr","Chris","Chrism","Dec","Diss","Dor","Dyl","Ell","Ephr","Ess","Est","Gal","Gell","Gin","Gwyn","Hann","Hel","Hen","Hild","Imm","Immac","Ion","Ish","Jen","Jess","Josm","Jul","Kat","Kath","Kess","Kyl","Let","Leth","Luc","Lyn","Mesh","Min","Mir","Mor","Og","Ol","Oliv","Osh","Pal","Palm","Phan","Prax","Res","Rhian","Rhiann","Rienn","Sab","Sabr","Sar","Sel","Seph","Silv","Syl","Venn","Ver","Viss","Vyl"];
var nm2 = ["a","ael","ais","ana","ane","anon","ata","atea","arya","ahla","e","ea","edes","ella","ena","enta","erina","erine","es","enya","i","ia","iael","iah","icia","ien","ima","ina","ine","ira","iro","isma","itta","ity","iya","on","one","osha","oya","olis","oia","onya","olla","o","oris","ora","ulata","uya","une","uah","una"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}