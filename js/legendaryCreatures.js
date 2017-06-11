var nm1 = ["Aklo","Alec","Ama","Anu","Ara","Arach","Ase","Asu","Ban","Basi","Behe","Bi","Bun","Ca","Cal","Cala","Chi","Chu","Cro","Cy","Dha","Dham","Dra","Du","Dulla","Gol","Gor","Gri","Grif","Hai","Har","Hell","Hi","Hiba","Hy","Incu","Ja","Jac","Jacka","Kel","La","Lam","Lama","Lin","Man","Manti","Me","Medu","Melu","Mi","Mino","Ouro","Pa","Pabi","Pabil","Pe","Pega","Pery","Phoe","Sa","Sel","Si","Sil","Sile","Su","Succu","Tara","Taras","Un","Uni","Va","Vam","Vana","Wol","Wolper","Wy","Ye","Zla","Zlato"];
var nm2 = ["berus","bis","boros","bra","bus","cabra","camp","clops","core","corn","cotta","dine","dorm","dra","drius","dusa","fin","ger","gon","griff","han","horn","ket","kie","leni","lenus","lez","lisk","lope","lops","mera","moth","nara","ne","ni","nix","nost","nus","pad","pie","pir","pire","py","que","quix","ren","rion","rog","rok","ron","ros","sag","sena","shee","sine","ssu","su","sura","sus","taur","tinger","ton","torog","trice","tryon","tyr","vern","yip","zum"];
var nm3 = ["a","e","i","o","u"];
var nm4 = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","x","y","z"];

var nm6 = ["","","","","","","","","","","b","c","d","f","g","h","j","k","l","m","n","p","r","s","t","v","w","y","z","br","ch","cr","dh","dr","fr","gn","gr","kn","kr","kh","ph","sc","sh","sk","st","str","th","tr","vr","wr"];
var nm7 = ["a","a","a","a","aa","ai","ao","au","e","e","e","e","ea","ee","ei","eo","i","i","i","i","ia","ie","io","o","o","o","o","oa","oo","ou","u","u","u","ua","ue"];
var nm8 = ["b","br","c","cc","ch","chn","cl","d","dr","ff","g","h","kl","l","lk","ll","lp","ls","m","mp","n","nd","ng","nsh","nt","p","pp","q","r","rb","rg","rp","s","sh","sq","ss","t","tr","tt","v","y","z"];
var nm9 = ["","","","","","","","","","","","","","","","d","ff","g","k","m","mp","n","nd","nx","p","ps","r","rm","rn","s","sk","st","t","th","x","z"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd7 = Math.random() * nm7.length | 0;
		if(i < 5){
			rnd = Math.random() * nm1.length | 0;
			rnd7b = Math.random() * nm7.length | 0;
			rnd8 = Math.random() * nm8.length | 0;
			rnd9 = Math.random() * nm9.length | 0;
			if(i < 3){
				names = nm1[rnd] + nm8[rnd8] + nm7[rnd7b] + nm9[rnd9];
			}else{
				nmRep = Math.random() * nm1[rnd].length | 0;
				if(nm1[rnd].charAt(nmRep) === "a" || nm1[rnd].charAt(nmRep) === "e" || nm1[rnd].charAt(nmRep) === "i" || nm1[rnd].charAt(nmRep) === "o" || nm1[rnd].charAt(nmRep) === "u" || nm1[rnd].charAt(nmRep) === "y"){
					nmRepl = nm3[Math.random() * nm3.length | 0];
				}else{
					nmRepl = nm4[Math.random() * nm4.length | 0];
				}
				nmR = nm1[rnd].substr(0,nmRep) + nmRepl + nm1[rnd].substr(nmRep+1);
				names = nmR + nm8[rnd8] + nm7[rnd7b] + nm9[rnd9];
			}
		}else{
			rnd = Math.random() * nm2.length | 0;
			rnd6 = Math.random() * nm6.length | 0;
			if(i < 8){
				names = nm6[rnd6] + nm7[rnd7] + nm2[rnd];
			}else{
				nmRep = Math.random() * nm2[rnd].length | 0;
				if(nm2[rnd].charAt(nmRep) === "a" || nm2[rnd].charAt(nmRep) === "e" || nm2[rnd].charAt(nmRep) === "i" || nm2[rnd].charAt(nmRep) === "o" || nm2[rnd].charAt(nmRep) === "u" || nm2[rnd].charAt(nmRep) === "y"){
					nmRepl = nm3[Math.random() * nm3.length | 0];
				}else{
					nmRepl = nm4[Math.random() * nm4.length | 0];
				}
				nmR = nm2[rnd].substr(0,nmRep) + nmRepl + nm1[rnd].substr(nmRep+1);
				names = nm6[rnd6] + nm7[rnd7] + nmR;
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