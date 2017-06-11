var names3 = ["Ah","Boora","Hamnu","Jar","Khar","Ka","Mahr","Ravi","Rou","Sah","Sih","Sohl","Tawak","Zah","Ahr","Bava","Havnu","Java","Kahra","Kihr","Marah","Rawi","Roj","Saj","Sij","Sal","Tarvak","Zahj","Ahj","Bahraja","Hannu","Jahk","Khanj","Kiji","Mahri","Rajiv","Rahk","Sara","Sira","Sajil","Tovik","Xa","A","Bara","Hammu","Ja","Kha","Ki","Mah","Rai","Ro","Sa","Si","Sol","Tavak","Za"];
var names4 = ["biri","bus","davi","han","hir","kar","manni","mnin","nai","oni","rabi","spoor","stae","tani","vandi","bari","bes","dawi","haan","hior","kahr","mahni","mnihn","naihn","ani","rabbi","spaer","stee","tanni","vadni","bihrri","bussi","dhari","rhan","hirn","ghar","mhan","mnirn","nair","onihr","garvi","kpoor","stavir","tannil","gandihr","bihrith","busihr","dawihn","hasin","hirin","karon","manrin","nmin","nahir","ohin","radir","sopor","stahe","tamil","vanadi"];
var br = "";
function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	tp = type;
	if(tp === 2){
		var names1 = ["Dra'","Daro'","Ko'","Ab'","Ak'","Akh'","Dar'","Do'","Dro'","Fa'","J'","Ja'","Ji'","Jo'","K'","M'","Ma'","Qa'","R'","Ra'","Ri'","S'","Za'","Zan'","Ab'","Ak'","Akh'","Dar'","Do'","Dro'","Fa'","J'","Ja'","Ji'","Jo'","K'","M'","Ma'","Qa'","R'","Ra'","Ri'","S'","Za'","Zan'","Am","Baa","Baad","Bhi","Bhis","Dah","Dahl","Dro","Has","Hass","Hel","Heln","Hus","Job","Joba","Jod","Jodh","Jos","Josh","Jot","Joto","Kaz","Kaza","Kes","Kesh","Kha","Khar","Mo","Moham","Moj","Na","Om","Ran","Rana","Sha","Sho","Shol","Sin","The","Then","Ther","Urj","Urja","Urjo","Vas","Vash","Wad","Wada","Zoa","Zoar"];
		var names2 = ["barri","qanar","sakhar","shavir","tasarr","zah","zaymar","zhirr","farahn","marash","shanji","zharim","bassa","dar","dara","darsha","dumiwa","fazir","jahirr","jhan","jidarr","jirr","karim","khar","kothre","mhirr","raska","ren-dar","sava","shajirr","tesh","thri-dar","vassa","virr","zaadha","zahn","zahr","zakar","zhid","aaj-Dar","aana","aasha","abhi","addha","adirr","agh","akha","aksa","amha","andra","anir","anni","ara","argo","ari","arkhu","arr","arr-Jo","arsha","asha","ashi","athad","atharr","athra","ato","ava","averr","azha","azirr","dargo","dirsha","dran","enji","esi","fer","ha","had","han","hani","hannar","har","harr","hasta","hirr","hur","idzo","ier","in-Dar","iq","irr","iska","jhad","jhera","jiradh","jirr","kar","kheran","lani","lima","ngil","nor","orad","randru-jo","rassa","raym","rjo","rris","saad","sha","siri","tasarr","zaddha","zaka","ar","bar","bil","der","dul","gh","ir","kir","med","nir","noud","sien","soud","taba","tabe","urabi"];
	}else{
		var names1 = ["Dra'","Daro'","Ko'","La'","Dar'","Do'","Dro'","J'","Ja'","Ji'","Jo'","M'","Ma'","Qa'","Ra'","Ri'","S'","Dar'","Do'","Dro'","J'","Ja'","Ji'","Jo'","M'","Ma'","Qa'","Ra'","Ri'","S'","Dar'","Do'","Dro'","J'","Ja'","Ji'","Jo'","M'","Ma'","Qa'","Ra'","Ri'","S'","A","Aba","Aban","Abh","Abhu","Ada","Adan","Add","Addh","Adh","Adha","Aff","Affr","Ahd","Ahda","Ahdn","Ahdr","Ahj","Ahja","Ahji","Ahk","Ahka","Ahn","Ahna","Ahnd","Ahni","Ahz","Ahzi","Ain","Aina","Aji","Ajir","Anj","Anja","Anu","Anur","Ara","Arab","Arav","Ash","Ashi","Ashn","Ata","Atah","Atr","Atra","Ayi","Ayis","Azi","Bah","Bahd","Bai","Bais","Bhi","Bhis","Bhu","Bhus","Chi","Chir","Dah","Dahl","Dahn","Dro","Eka","Ekap","Ela","Fa","Hab","Haba","Har","Hara","Idh","Idha","Ine","Iner","Ino","Inor","Kaa","Kaas","Kha","Kham","Khay","Khaz","Khi","Khin","Ki","Kis","Kise","Kish","Kisi","Mo","Na","Nah","Nahs","Nis","Nisa","Ra","Rab","Rabi","Ri","Sa","Sha","Shab","Sham","Shav","Shi","Shiv","Sho","Shom","Shot","Shu","Shun","Shur","So","Ta","Tal","Tala","Tsa","Tsab","Tsaj","Tsal","Tsan","Tsar","Tsav","Tsi","Tsiy","Tsr","Tsra","Uba","Ubaa","Uda","Udar","Unj","Unja","Vaj","Vajh","Van","Vanj","Yus","Yush","Za","Zab","Zabh","Zah","Zahr","Zay","Zayn"];
		var names2 = ["aba","abhi","abi","ada","adhi","ahin","ahna","ahni","ahra","aji","ajma","amla","ani","ara","aranji","ari","arji","arra","asa","asha","ashi","asi","asma","assa","assi","asuna","ava","avi","azami","azda","ba","bah","bhi","dahna","dahra","dasha","drashi","eena","ena","feliz","hana","hasa","hashi","hba","hbah","heh","herra","hi","hila","hinda","hira","hiranirr","hni","hrazad","ia","idasha","ila","imba","ini","inna","ira","iranirr","irra","isa","isi","ivva","ja","jadhi","jarsi","ji","jirra","jjan","khtar","ki","la","lajma","lani","leena","mada","mara","mba","mla","muzi","nabi","nara","nari","ni","nita","nja","njarsi","nji","nna","pi","ra","raji","ranirr","ranji","rasha","rashi","rassa","ravi","raya","ri","riba","rina","rivva","rji","rra","rranirr","rri","rrina","sa","sari","sha","shima","si","sma","srin","ssa","ssi","suna","therra","tima","uki","ura","uzi","va","vani","vari","vi","ya","yla","zami","zda","zhinda","zita","zura"];
	}
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names2.length);
			names = names1[rnd] + names2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * names1.length);
			rnd2 = Math.floor(Math.random() * names2.length);
			rnd3 = Math.floor(Math.random() * names3.length);
			rnd4 = Math.floor(Math.random() * names4.length);
			names = names1[rnd] + names2[rnd2] + " " + names3[rnd3] + names4[rnd4];
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