var nm1 = ["Aggu","Agu","Ar","Arn","Aso","At","Atru","Bar","Bel","Bo","Bor","Brak","Ca","Cra","Do","Dor","Dra","Du","Dur","Ga","Gal","Gan","Gar","Go","Gor","Got","Gram","Grim","Gro","Grom","Gru","Gul","Hag","Han","Har","Hog","Hon","Hor","Hun","Hur","Ka","Kal","Kam","Kar","Karo","Kel","Kil","Ko","Kom","Kor","Kra","Kru","Ku","Kul","Kur","La","Lam","Lu","Lum","Ma","Mag","Mahl","Mak","Mal","Mar","Mo","Mog","Mok","Mor","Mu","Mug","Muk","Mura","Nee","Oggu","Ogu","Ok","Oko","Olla","Or","Oro","Rek","Ron","Rona","Sa","Sar","So","Sor","Tha","Thar","Ther","Thra","Thro","Thru","Thu","Thur","Trak","Truk","Uk","Uko","Ukra","Ukru","Ulla","Ur","Urtha","Urthu","Urtra","Urtru","Za","Zar","Zas","Zav","Zev","Zor","Zu","Zur","Zus"];
var nm2 = ["d","dar","dur","g","gar","gur","l","m","mar","mur","n","nar","nur","t","tar","tur","z","zar","zur","","","","","","","","","","","","","","","","","","","","",""];
var nm3 = ["'Dar","'Dur","'Gald","'Gan","'Gar","'Geld","'Gen","'Gor","'Guld","'Gun","'Phan","'Ral","'Raz","'Rul","'Ruz","'Tar","'Thak","'Thuk","'Thunk","'Tur","ada","agg","agus","ak","ald","am","an","ar","arg","arl","arm","aro","aru","as","ath","ban","da","dan","dar","dok","dor","dran","du","dur","eld","eth","far","fu","ful","fur","gal","gald","gam","gan","gas","geld","gen","gor","gorm","gorn","gosh","grom","gron","gul","guld","gum","gun","gus","kada","kuda","l","lach","lak","lek","loch","ma","mak","mar","mok","nok","ogg","ok","okk","olak","olek","om","oram","oran","osh","ost","phan","phon","phun","rak","ram","ramm","ran","ras","rek","ri","rom","romm","rosh","rost","ru","ruk","rum","rumm","rus","stan","tar","thak","thas","thos","thuk","thus","ton","tor","tunk","tur","u","ud","uda","ugg","uk","ul","uld","um","urg","urk","url","urm","uro","us","uwd","var","ven","vor","zal","zok","zul"];
var nm4 = ["Al","El","Fal","Fel","Fol","Ful","Ga","Gar","Gi","Gija","Go","Gor","Gre","Gro","Gry","Kar","Kat","Ker","Ket","Ki","Kir","Kot","Kur","Kut","Mer","Mir","Mor","Ol","Ra","Rah","Rahk","Ras","Rash","Raw","Ro","Roh","Rohk","Ru","Sa","Sam","San","Se","Sem","Sen","Sha","Shay","She","Shi","Shu","Sin","Su","Sum","Sun","Tam","Tem","Tu","Tum","Um","Uma","Ur","Ure","Zan","Zen","Zon","Zun"];
var nm6 = ["'Kuma","'Kuna","'Kuno","'Te","'Ti","'Tur","'Ula","'Ulo","adu","aja","aju","ala","ami","ano","anu","ar","atra","das","des","dis","dras","dres","dris","drus","dus","eda","edo","ija","ika","iko","iku","ila","ile","ilu","ina","ino","inu","ira","iro","iru","is","kaja","kajo","kamo","kano","kes","ket","kis","kit","kuja","kuji","kujo","kuma","kumo","kuna","kuno","kys","lika","liko","liku","na","nae","nar","ner","nor","oda","odu","ona","onu","os","otra","ra","ras","res","ris","ros","rus","shka","strom","tar","thas","thes","thos","thus","tra","uda","udo","uja","ujo","ula","ulo","ume","umi","una","us","via","vio","viu","yja","yl","yla","yle","ylu","yna","yno","ynu","yra","yro","yru"];
var nm7 = ["Axe","Battle","Black","Thunder","Blood","Burning","Bone","Clan","Dark","Dead","Death","Doom","Dragon","Dream","Fire","Fist","Fore","Frost","Gore","Hell","Iron","Laughing","Lone","Nose","Rage","Red","Rock","Saur","Shadow","Skull","Steel","Stone","Strong","Tusk","War","Wolf"];
var nm8 = ["axe","arm","basher","binder","blade","bleeder","bringer","chewer","cleaver","crusher","eye","fang","fist","fury","hammer","hand","horn","lash","maul","maw","rage","ripper","runner","scream","seeker","slayer","snarl","song","splitter","sword","taker","wolf"];
var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd7 = Math.floor(Math.random() * nm7.length);
		rnd8 = Math.floor(Math.random() * nm8.length);
		if(tp === 1){
			rnd4 = Math.floor(Math.random() * nm4.length);
			rnd6 = Math.floor(Math.random() * nm6.length);
			names = nm4[rnd4] + nm2[rnd2] + nm6[rnd6] + " " + nm7[rnd7] + nm8[rnd8];
		}else{
			rnd4 = Math.floor(Math.random() * nm1.length);
			rnd6 = Math.floor(Math.random() * nm3.length);
			names = nm1[rnd4] + nm2[rnd2] + nm3[rnd6] + " " + nm7[rnd7] + nm8[rnd8];
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