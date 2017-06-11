var nm1 = ["","","","","b","br","c","ch","d","fr","g","gr","j","k","m","n","p","q","r","t","x","z"];
var nm2 = ["u","u","u","u","u","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","ai","ay","ei","eo","ia","ie","oi"];
var nm3 = ["d","ddr","dr","g","gh","k","lb","ldr","lr","lzr","m","mb","mm","mr","n","nd","ndr","nn","r","rd","rg","rr","rs","rv","s","t","th","v","vr","z","zz"];
var nm4 = ["cr","d","n","nt","r","rr","sd"];
var nm5 = ["","","d","g","m","n","nth","r","rth","s","ss","t"];

var nm6 = ["","","","","","","b","c","ch","d","f","fr","g","h","l","m","n","p","q","r","s","sh","t","v","z"];
var nm7 = ["u","u","u","u","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","a","e","i","o","y","ae","ai","ay","ei","eo","ie","io","oa"];
var nm8 = ["d","dh","g","gh","k","ldr","ll","m","mm","mr","n","nd","ndr","nn","p","ph","r","rg","rl","rm","rr","rs","rv","s","ss","t","th","v","vn","z","zz"];
var nm9 = ["d","l","n","nt","ph","r","rr","ss"];
var nm10 = ["","","","","","l","lth","n","nth","r","rth","s","ss","t","th"];

var nm11 = ["","","","","b","c","ch","d","fr","g","m","n","p","q","r","s","t","v","x","z"];
var nm12 = ["u","u","u","u","a","e","i","o","y","ae","ai","ay","ei","eo","ia","ie","io","oa","oi"];
var nm13 = ["d","dh","dr","g","gh","k","l","ldr","ll","lr","m","mm","mr","n","nd","ndr","nn","p","ph","r","rl","rm","rr","rs","rv","s","ss","t","th","v","vn","vr","z","zz"];
var nm14 = ["d","l","n","nt","ph","r","rr","ss"];
var nm15 = ["","","","d","g","l","lth","n","nth","r","rth","s","ss","t","th"];

var nm16 = ['the Nocturnal','the Protective','the Clever','the Bright','the Dark','the Dark One','the Dark','the Eternal','the Firestarter','the Eternal One','the Calm','the Gentle','the Redeemer','the Champion','the Evil One','the Chosen','the Great','the Kind','the Fierce','the Strong','the Tiran','the Dragonlord','the Warrior','the Barbarian','the Tall','the Magnificent','the Clean','the Adorable','the Gifted','the Tender','the Powerful One','the Gifted One','the Powerful','the Black','the White','the White One','the Careful','the Clumsy One','the Grumpy','the Jealous One','the Mysterious','the Mysterious One','the Scary','the Scary One','the Brave','the Victorious','the Skinny One','the Mammoth','the Puny','the Quiet','the Voiceless','the Loud','the Voiceless One','the Fast One','the Swift','the Young One','the Youngling','the Slow','the Creep','the Warm','Warmheart','Braveheart','Gentleheart','the Strong Minded','the Stubborn','Firebreath','Icebreath','the Squeeler','Champion of Dragons','Eternal Fire','Gentle Mind','Longtail','Redeemer of Men','Protector of the Weak','Protector of the Forest','Protector of the Sky','Lord of the Skies','Champion of the Skies','Champion of Men','Lord of Fire','Lord of Ice','Lord of the Red','Lord of the Black','Lord of the White','Lord of the Blue','Lord of the Green','Lord of the Yellow','Lord of the Brown','Champion of the Red','Champion of the White','Champion of the Black','Champion of the Blue','Champion of the Yellow','Champion of the Brown','Champion of the Green','Protector of Creatures','Protector of Life','Giver of Life','Bringer of Death','the Deathlord','the Dead','Destroyer of Life','Destroyer of Men','Eater of Sheep','Eater of All','the Hungry','Eater of Bunnies','the Bunny Killer','the Rabbit Slayer','the Taker of Life','the Insane','the Life Giver'];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd16 = Math.random() * nm16.length | 0;
		if(tp === 1){
			rnd = Math.random() * nm6.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			rnd3 = Math.random() * nm8.length | 0;
			rnd4 = Math.random() * nm7.length | 0;
			rnd5 = Math.random() * nm10.length | 0;
			while(nm6[rnd] === nm8[rnd3]){
				rnd3 = Math.random() * nm8.length | 0;
			}
			while(nm10[rnd5] === nm8[rnd3]){
				rnd5 = Math.random() * nm10.length | 0;
			}
			if(i < 7){
				names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm10[rnd5] + ", " + nm16[rnd16];
			}else{
				rnd6 = Math.random() * nm9.length | 0;
				rnd7 = Math.random() * nm7.length | 0;
				while(nm9[rnd6] === nm8[rnd3]){
					rnd6 = Math.random() * nm9.length | 0;
				}
				names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd6] + nm7[rnd7] + nm10[rnd5] + ", " + nm16[rnd16];
			}
		}else if(tp === 2){
			rnd = Math.random() * nm11.length | 0;
			rnd2 = Math.random() * nm12.length | 0;
			rnd3 = Math.random() * nm13.length | 0;
			rnd4 = Math.random() * nm12.length | 0;
			rnd5 = Math.random() * nm15.length | 0;
			while(nm11[rnd] === nm13[rnd3]){
				rnd3 = Math.random() * nm13.length | 0;
			}
			while(nm15[rnd5] === nm13[rnd3]){
				rnd5 = Math.random() * nm15.length | 0;
			}
			if(i < 7){
				names = nm11[rnd] + nm12[rnd2] + nm13[rnd3] + nm12[rnd4] + nm15[rnd5] + ", " + nm16[rnd16];
			}else{
				rnd6 = Math.random() * nm14.length | 0;
				rnd7 = Math.random() * nm12.length | 0;
				while(nm14[rnd6] === nm13[rnd3]){
					rnd6 = Math.random() * nm14.length | 0;
				}
				names = nm11[rnd] + nm12[rnd2] + nm13[rnd3] + nm12[rnd4] + nm14[rnd6] + nm12[rnd7] + nm15[rnd5] + ", " + nm16[rnd16];
			}
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm3.length | 0;
			rnd4 = Math.random() * nm2.length | 0;
			rnd5 = Math.random() * nm5.length | 0;
			while(nm1[rnd] === nm3[rnd3]){
				rnd3 = Math.random() * nm3.length | 0;
			}
			while(nm5[rnd5] === nm3[rnd3]){
				rnd5 = Math.random() * nm5.length | 0;
			}
			if(i < 7){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + ", " + nm16[rnd16];
			}else{
				rnd6 = Math.random() * nm4.length | 0;
				rnd7 = Math.random() * nm2.length | 0;
				while(nm4[rnd6] === nm3[rnd3]){
					rnd6 = Math.random() * nm4.length | 0;
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5] + ", " + nm16[rnd16];
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