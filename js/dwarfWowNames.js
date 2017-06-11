var nm1 = ["Am","Arm","Bal","Ban","Bar","Bel","Beng","Bhal","Bhar","Bhel","Bram","Bran","Brom","Brum","Bun","Dal","Dar","Dol","Dram","Drom","Drum","Dul","Em","Erm","Gal","Gar","Ger","Gim","Gir","Gol","Gor","Gral","Gram","Gran","Grem","Gren","Gril","Grim","Grom","Grul","Grum","Grun","Gry","Gul","Har","Hjal","Hjol","Hjul","Hor","Hulf","Hur","Irom","Iron","Jar","Jor","Kar","Khar","Kram","Krom","Krum","Mag","Mal","Mel","Muir","Mur","Ol","Orim","Orm","Rag","Reg","Rot","Shel","Sog","Sogn","Sug","Sugn","Thal","Thar","Thel","Ther","Tho","Thor","Thul","Thur","Thy","Tor","Ty","Um","Urm"];
var nm2 = ["o","a","u","i","ia","iu","ou","ua","ah","uh","oh","ihr","ahr","ohr","","","","","","","","","","","","","","","","","","","","","","","",""];
var nm3 = ["brek","dahr","dan","dar","dir","dohr","donore","dor","dram","dren","drom","drum","drus","duhr","dur","dus","edon","g","garn","gas","gorn","gos","gram","gran","grom","gron","grum","grun","gurn","gus","han","hann","hun","hunn","iggs","kahm","kam","kohm","kom","kuhm","kum","kyl","m","man","mand","mar","mek","miir","min","mir","mond","mor","mun","mund","mur","mus","myl","myr","n","nam","nar","ni","nik","nir","nom","nu","num","nur","nus","nyl","ram","ren","rig","rigg","rim","rom","ron","rum","rus","ruuk","ryl","tharm","tharn","thorm","thorn","thran","throm","thron","thrum","thrun","thurm","thurn","thus","yth"];
var nm4 = ["Ang","Angr","Bel","Bell","Bon","Bonn","Braen","Bral","Brall","Bran","Bril","Brill","Bren","Bret","Brett","Brol","Broll","Bron","Brul","Brull","Bryl","Bryll","Bryn","Bryt","Byl","Byll","Daer","Dear","Dim","Ed","Ein","Eyn","Gwan","Gwen","Gwin","Gwyn","Gim","Gym","Ing","Ingr","Jen","Jenn","Jin","Jinn","Jyn","Jynn","Kait","Kar","Kat","Ket","Las","Lass","Les","Less","Lyes","Lys","Lyss","Maev","Mar","Mis","Mist","Myr","Mys","Myss","Myst","Nal","Nas","Nass","Nes","Ness","Nis","Niss","Nys","Nyss","Ong","Ongr","Ov","Raen","Ran","Red","Reyn","Run","Ryn","Sar","Sol","Tas","Taz","Tis","Tish","Tiz","Tys","Tysh","Ung","Ungr"];
var nm5 = ["o","a","i","ia","io","ou","ua","ah","um","oh","ir","ar","or","un","eo","ea","in","im","an","am","","","","",""];
var nm6 = ["leil","nar","nyl","myl","lyl","dyl","ris","ras","res","ros","win","wyn","waen","whin","whyn","whaen","tin","tyn","lyn","lin","lynn","linn","wynn","va","van","rin","ryn","ryl","nas","nan","ria","nia","ri","rip","nip","dora","leen","len","ma","la","mora","mura","mera","nura","nera","nora","glia","glian","giel","thiel","diel","thel","nis","niss","nys","nyss"];
var nm7 = ["Barley","Battle","Black","Bone","Boulder","Bright","Bronze","Cask","Cliff","Cold","Crag","Dark","Deep","Dirge","Doom","Fire","Flint","Frost","Fuse","Gold","Hammer","High","Iron","Long","Marble","Molten","Mountain","Pale","Red","Slate","Snow","Steel","Stern","Stone","Storm","Stout","Thunder"];
var nm8 = ["arm","axe","beard","belly","blade","braid","branch","brand","breaker","brew","brow","crag","dust","fall","fist","flayer","forge","fury","gem","grip","hammer","hand","helm","mane","mantle","ore","pike","river","roar","rock","shaper","shield","shout","steel","stone","toe"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd4 = Math.floor(Math.random() * nm7.length);
		rnd5 = Math.floor(Math.random() * nm8.length);
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm4.length);
			rnd2 = Math.floor(Math.random() * nm5.length);
			rnd3 = Math.floor(Math.random() * nm6.length);
			names = nm4[rnd] + nm5[rnd2] + nm6[rnd3] + " " + nm7[rnd4] + nm8[rnd5];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + " " + nm7[rnd4] + nm8[rnd5];
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