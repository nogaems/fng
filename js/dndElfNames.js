var nm1 = ["Ad","Ae","Bal","Bei","Car","Cra","Dae","Dor","El","Ela","Er","Far","Fen","Gen","Glyn","Hei","Her","Ian","Ili","Kea","Kel","Leo","Lu","Mira","Mor","Nae","Nor","Olo","Oma","Pa","Per","Pet","Qi","Qin","Ralo","Ro","Sar","Syl","The","Tra","Ume","Uri","Va","Vir","Waes","Wran","Yel","Yin","Zin","Zum"];
var nm2 = ["balar","beros","can","ceran","dan","dithas","faren","fir","geiros","golor","hice","horn","jeon","jor","kas","kian","lamin","lar","len","maer","maris","menor","myar","nan","neiros","nelis","norin","peiros","petor","qen","quinal","ran","ren","ric","ris","ro","salor","sandoral","toris","tumal","valur","ven","warin","wraek","xalim","xidor","yarus","ydark","zeiros","zumin"];
var nm3 = ["Ad","Ara","Bi","Bry","Cai","Chae","Da","Dae","Eil","En","Fa","Fae","Gil","Gre","Hele","Hola","Iar","Ina","Jo","Key","Kris","Lia","Lora","Mag","Mia","Neri","Ola","Ori","Phi","Pres","Qi","Qui","Rava","Rey","Sha","Syl","Tor","Tris","Ula","Uri","Val","Ven","Wyn","Wysa","Xil","Xyr","Yes","Ylla","Zin","Zyl"];
var nm4 = ["banise","bella","caryn","cyne","di","dove","fiel","fina","gella","gwyn","hana","harice","jyre","kalyn","krana","lana","lee","leth","lynn","moira","mys","na","nala","phine","phyra","qirelle","ra","ralei","rel","rie","rieth","rona","rora","roris","satra","stina","sys","thana","thyra","tris","varis","vyre","wenys","wynn","xina","xisys","ynore","yra","zana","zorwyn"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			nameFem();
			while(nMs === ""){
				nameFem();
			}
		}else{
			nameMas();
			while(nMs === ""){
				nameMas();
			}
		}
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(nMs));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}
function nameFem(){
	rnd = Math.floor(Math.random() * nm3.length);
	rnd2 = Math.floor(Math.random() * nm4.length);
	nMs = nm3[rnd] + nm4[rnd2];
	testSwear(nMs);
}

function nameMas(){
	rnd = Math.floor(Math.random() * nm1.length);
	rnd2 = Math.floor(Math.random() * nm2.length);
	nMs = nm1[rnd] + nm2[rnd2];
	testSwear(nMs);
}