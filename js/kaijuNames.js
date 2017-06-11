
function nameGen(){
	var nm1 = ["Aby","Abys","Ae","Aeri","Aethe","Amphi","Ana","Anar","Aqu","Aqua","Ata","Ataxi","Au","Aura","Bar","Barba","Barbar","Bas","Bla","Bli","Boul","Bri","Bru","Bruta","Canni","Canniba","Carni","Cata","Catacly","Chao","Cin","Coba","Cobal","Cor","Corp","Cra","Crim","Cro","Crown","Cry","Cryo","Cryp","Crys","Daw","Dia","Diablo","Diabo","Diamo","Ebo","Ebon","Elec","Elepha","Elu","Em","Eme","Emera","Eter","Ethe","Ether","Eva","Fera","Fero","Fi","Fie","Fla","Fren","Fri","Fro","Garga","Gargan","Giga","Gigan","Gla","Grie","Grim","Gris","Griz","Hanniba","Infer","Iro","Ivo","Levi","Levia","Male","Malevo","Mas","Matri","Mon","Mons","Mour","Neth","Nethe","Obsi","Obsidi","Ony","Ore","Patri","Pha","Phan","Phanto","Phibi","Pri","Prima","Prime","Primi","Pyro","Ra","Rabi","Rava","Raz","Saphi","Sava","Scar","Sco","Scor","Scree","Sha","Shado","Sil","Slen","Som","Spec","Spi","Spiri","Stal","Sten","Ston","Stor","Storm","Sty","Su","Supre","Tacly","Talo","Ter","Thor","Thun","Tita","Titan","Tor","Tox","Tran","Tus","Ven","Veno","Vi","Vic","Vici","Vole","Vor","War"];
	var nm2 = ["bara","borg","cada","coatl","da","dan","dius","don","dorah","dorg","doro","doru","dos","dragon","dun","dus","dusa","gami","gan","gar","garu","gary","gas","gauros","gira","go","gon","gora","guar","guera","guma","hara","jin","ju","lak","lar","laria","las","lios","lon","lus","majin","mera","mon","mutul","nar","nula","nulon","pede","pod","por","ra","ragon","rah","ran","randa","rappa","ras","rashi","rax","ria","rigar","rola","ron","ros","rugon","rus","sari","saurus","sis","sos","sus","talak","tax","thrax","tor","tori","tra","tul","vern","vore","yah","zilla"];
	var br = "";

	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + nm2[rnd2];
		nm1.splice(rnd, 1);
		nm2.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}