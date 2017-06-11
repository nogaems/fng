var nm1 = ["A","A'","Al","All","Aly","An","Am","As","Ay","Ar","Cy","Ca","E","E'","El","Ely","Em","En","Er","Es","Ey","F","Fa","Fy","Fil","Fel","Fyl","Ga","Gal","Ha","He","Hy","I","Il","Ily","Ill","Iy","Ji","Ja","K","Ka","Ke","Ky","L","Lil","Lyl","Lel","La","Le","Ly","M","Ma","Me","My","Myt","Myth","Mor","Math","Mil","Myl","Mel","N","Na","Ne","Nyl","Nil","Nel","Nyt","Nyth","Ny","Re","Ra","Ry","S","Sa","Sil","Syl","Sel","Sh","Sha","She","Sy","Shyl","Th","Tha","The","Thel","Thyl","Thil","Thy","U","Uy","W","Wa","We","Y","Y'","Ya","Ye","Yl","Yll"];
var nm2 = ["al","el","en","an","ana","ena","aena","a","i","ren","ran","eth","ath","a","e","o","h","ha","he","ho","f","fa","fe","l","le","la","m","me","ma","ne","na","n","s","sa","se","ve","va"];
var nm3 = ["dris","ris","dral","dos","dlas","rion","idan","gyl","nul","gos","dras","dran","dryn","adros","dlass","lass","dlaess","dleass","laess","leass","thiel","engyl","annul","aenul","aenal","aenel","eanal","eanel","edon","adon","aedon","eadon","llian","llean","lian","lean","llaen","laen","nath","naeth","neath","shar","tharion","arion","erian","aerian","dent","elir","gorn","egorn","agorn","elor","ellor","aelor","aellor","elorn","ellorn","aelorn","aellorn","dren","odren","draen","odraen","adan","aedan","adaen","adean","draen","odraen","adarn","aedarn","adaern","adearn","drus","nrus","dryn","dan","andiir","diir","gyl","gyal","gyael","'dir","umon","elar","aelar","ealar","oren","oraen","orean","'las","thas","thaes","theas","sam","saem","seam","rand","ldor","dron","eth","gorm","rin","anas","anaes","aenas","anelle","dris","erias","thae","n'ra","nas","aste","ethil","driel","rieth","drieth","draeth","dreath","raeth","reath","ries","dries","draes","dreas","raes","reas","rai","rea","rae","raei","anai","laeth","leath","alas","aelas","alaes","aleas","aeleas","ealaes","aelleas","eallaes","allas","aellas","allaes","alleas","alias","alaeas","alath","aelath","alaeth","aleath","aeleath","ealaeth","aelleath","eallaeth","allath","aellath","allaeth","alleath","aliath","alaeath","aeith","eaith","ileath","ilaeth","aleath","illeath","illaeth","wen"];
var nm4 = ["A","A'","Al","All","Aly","An","Am","As","Ay","Ar","Cy","Ca","E","E'","El","Ely","Em","En","Er","Es","Ey","F","Fa","Fy","Fil","Fel","Fyl","Ga","Gal","Ha","He","Hy","I","Il","Ily","Ill","Iy","Ji","Ja","K","Ka","Ke","Ky","L","Lil","Lyl","Lel","La","Le","Ly","M","Ma","Me","My","Myt","Myth","Mil","Myl","Mel","N","Na","Ne","Nyl","Nil","Nel","Nyt","Nyth","Ny","S","Sa","Sil","Syl","Sel","Sh","Sha","She","Sy","Shyl","Th","Tha","The","Thel","Thyl","Thil","Thy","U","Uy","W","Wa","We","Y","Y'","Ya","Ye","Yl","Yll"];
var nm5 = ["a","e","o","h","f","l","m","n","s","va","a","e","o","h","ha","he","ho","f","fa","fe","l","le","la","m","me","ma","ne","na","n","s","sa","se","ve","va",""];
var nm6 = ["anas","anaes","aenas","anelle","dris","liene","aria","anaria","alaria","cina","ina","ene","erias","eria","ora","lora","thea","thae","inne","rnae","rnea","is'ta","n'ra","nas","aste","arii","riia","hara","ethil","driel","'lynn","'lyn","india","adyia","adya","aedya","indea","indae","ania","aenia","eana","aenea","iyell","yell","ythis","ethis","rieth","drieth","draeth","dreath","raeth","reath","ynna","yna","enna","aenna","eanna","eana","aena","anna","rai","rea","rae","raei","anai","anea","lea","lae","laei","laeth","leath","yssa","lyssa","lyssae","lysae","ysae","lysea","ysea","asia","aesia","easia","asea","asae","aesa","easa","alas","aelas","alaes","aleas","aeleas","ealaes","aelleas","eallaes","allas","aellas","allaes","alleas","ercia","aercia","earcia","enia","aenia","enya","aenya","lia","alia","alaea","alias","alaeas","ysa","yssea","ysea","yssae","ysae","nya","nyae","nysa","nysea","nysae","nyssa","nyssae","nyssea","yssia","aeith","eaith","ileath","ilaeth","aleath","illeath","illaeth","yura","yurea","yurae","wen","leae","laea"];
var nm7 = ["Amber","Autumn","Bear","Black","Blade","Blue","Dark","Dawn","Dew","Dusk","Even","Far","Feather","Fog","Forest","Green","Leaf","Light","Luna","Mist","Moon","Moss","Night","Ocean","Rain","Rapid","Raven","Sage","Sea","Shade","Shadow","Shield","Silent","Silver","Sky","Spirit","Stag","Star","Still","Stone","Storm","Strong","Summer","Sun","Swift","Thunder","Tree","True","Void","Wild","Wind","Winter","Wood"];
var nm8 = ["arrow","blade","bloom","blower","bough","bow","branch","breath","breeze","caller","cloud","clouds","crest","dancer","dew","eye","feather","fire","flower","forest","gazer","grove","heart","helm","lance","leaf","light","mane","might","moon","oak","rage","runner","scribe","seeker","shade","shadow","shot","singer","sky","snow","song","spear","spirit","spyre","stalker","star","strike","striker","swift","sword","thorn","tree","walker","watcher","water","weaver","whisper","wind","wing"];
var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd7 = Math.floor(Math.random() * nm7.length);
		rnd8 = Math.floor(Math.random() * nm8.length);
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm4.length);
			rnd3 = Math.floor(Math.random() * nm6.length);
			if(i < 5){
				names = nm4[rnd] + nm6[rnd3] + " " + nm7[rnd7] + nm8[rnd8];
			}else{
				rnd2 = Math.floor(Math.random() * nm5.length);
				names = nm4[rnd] + nm5[rnd2] + nm6[rnd3] + " " + nm7[rnd7] + nm8[rnd8];
			}
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			if(i < 5){
				names = nm1[rnd] + nm3[rnd3] + " " + nm7[rnd7] + nm8[rnd8];
			}else{
				rnd2 = Math.floor(Math.random() * nm2.length);
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + " " + nm7[rnd7] + nm8[rnd8];
			}
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