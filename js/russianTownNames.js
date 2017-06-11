var nm1 = ["Aba","Achi","Ale","Alme","Ana","Anga","Apa","Arma","Arse","Arza","Astra","Bala","Bata","Bele","Belgo","Belo","Belore","Bere","Beryo","Biro","Birobi","Blago","Blagove","Bori","Boriso","Boro","Bra","Budyo","Bugu","Buyna","Buzu","Chapa","Chayko","Che","Chebo","Chelya","Chere","Cherno","Chi","Chisto","De","Dmi","Do","Dolgo","Domo","Domode","Done","Du","Eli","Frya","Ga","Gele","Gla","Go","Gro","Gu","Guko","Irku","Ishi","Iski","Iva","Ka","Kali","Kalini","Kalu","Kame","Kamy","Kaspi","Keme","Kha","Khaba","Khasa","Khi","Kine","Kiri","Kiro","Kise","Kislo","Kli","Klimo","Ko","Koga","Kolo","Komso","Kope","Koro","Kostro","Kovro","Krasno","Kropo","Kry","Ku","Kume","Kuzne","Ky","Labi","Leni","Lenino","Lesn","Leso","Li","Lipe","Lo","Ly","Lyu","Lyube","Ma","Maga","Magni","Magnito","Makha","Me","Mezhdu","Mia","Michu","Mikhay","Mine","Minu","Mo","Mu","My","Myti","Na","Nabe","Nakho","Navere","Naza","Nefte","Nefteyu","Neryu","Nevi","Nizhne","Nogi","Nori","Novo","Novoa","Novoche","Novoku","Novomo","Novorossi","Novotroi","Novou","Noya","Nya","Obni","Odi","Oktya","Ore","Ory","Ozyo","Pavlo","Pervou","Podo","Pole","Pro","Proko","Pu","Pya","Pyati","Rame","Reu","Ro","Rosla","Rosso","Rya","Rybi","Sala","Sama","Sara","Saro","Serpu","Seve","Severo","Sha","Shchyo","Shu","Si","Siba","Sla","Smo","So","Soli","Solne","Soso","Sta","Stavro","Ste","Sterli","Stu","Stupi","Su","Svo","Svobo","Taga","Tambo","Tikho","Tima","To","Tobo","Tolya","Troi","Tu","Tua","Tuyma","Tve","Tyu","Ula","Ulya","Uso","Ussu","Ussuri","Uzlo","Veli","Vidno","Vladi","Volgo","Volo","Vorku","Voro","Voskre","Vse","Vsevo","Vya","Vybo","Yaku","Yaro","Yego","Yeka","Yekate","Yela","Yele","Yesse","Yu","Zare","Zele","Zeleno","Zhele","Zhelezno","Zhi","Zhigu","Zhuko","Zla"];
var nm2 = ["bay","bey","binsk","birsk","bkin","bna","bnya","bodny","boksarsk","borg","buga","byshevsk","chensk","chkala","chny","dar","dedovo","dimir","dnoye","dny","dolsk","dorozhny","dovo","drinsk","drov","dzhan","gadan","gan","gansk","garsk","gda","ginsk","giyev","glebsk","godonsk","gorod","gorsk","grad","grosk","gulma","kala","kamensk","kamsk","kan","karino","kavkaz","khan","khladny","khna","khov","khovo","khtinsk","kin","kiye","kovo","kovsky","ksa","ksary","ksin","kutsk","labuga","lavat","lchik","lensk","leuz","liky","litamak","lkovo","lma","lovka","lovsk","lozhsk","lsk","ltaysk","luga","luk","lym","lyovsk","lzhsky","mara","mas","mbay","mbov","mkhovo","mki","mna","movsk","myssk","naksk","napa","ndzhik","netsk","nezh","ngelsk","ngrad","ngru","ninsk","nnovsk","nomyssk","novo","novsk","nrog","nsk","nskoy","nskoye","ntsovo","ntsy","nyev","nza","pa","petsk","peysk","pol","povets","prudny","pukhov","pul","pyevsk","ralsk","ransk","rapul","ratov","rbash","rbent","rechny","retsk","rga","rgan","rgut","rilsk","rino","rinsk","riysk","rkassk","rkuta","rmansk","rod","rodvinsk","rom","romorsk","rov","rovo","rovsk","rsk","rtau","rtovsk","rtsy","ry","ryevsk","ryol","rzhinsk","scow","sensk","shchensk","shchi","shevsk","shi","shikha","shin","shma","shny","shov","sinsk","ski","skovsk","skoye","slavl","snovy","snoy","ssosh","ssyisk","sta","stal","stroma","tamak","tim","tity","tkinsk","tlas","toust","tov","troitsk","trov","tsk","turynisk","tyevsk","vartovsk","vat","vaya","vda","versk","vets","vgrad","vichi","vir","vkar","vny","vo","vodsk","vostok","vropol","vrov","vsk","vskoy","vsky","vyurt","ya","yarsk","yev","yevka","yevsk","ylovka","ylovsk","ysk","yugansk","yungri","zan","zino","zma","znetsk","zniki","znogorsk","zny","zov","zovsky","zran","zuluk","zyl"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
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