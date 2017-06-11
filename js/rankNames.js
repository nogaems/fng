var nm1 = ["Adept","Adjunct","Administrator","Admiral","Advisor","Alpha","Alpha Chieftain","Alpha King","Ambassador","Apostle","Apprentice","Archbishop","Archduke","Archjusticar","Archmage","Archpaladin","Archpriest","Archsage","Archseer","Archsentinel","Archwarrior","Assistant","Attendant","Baron","Beta","Bishop","Blessed","Caesar","Chairman","Chamberlain","Chancellor","Chaplain","Chief","Chieftain","Cleric","Clerk","Congressman","Consort","Consul","Council Chief","Council Member","Councillor","Count","Demonlord","Dictator","Director","Disciple","Divine","Dom","Dragonlord","Duke","Earl","Elder","Emperor","Ensign","Exarch","Executive","Executor","Father","First Secretary","Foreman","General","Governer","Grand Admiral","Grand Vizier","Hand of the King","Head of State","Herald","High Baron","High Chairman","High Chancellor","High Chief","High Cleric","High Councillor","High Duke","High Earl","High Emperor","High Father","High General","High Governor","High Justicar","High King","High Mage","High Magister","High Marshal","High Minister","High Paladin","High Priest","High Prince","High Prophet","High Regent","High Sage","High Saint","High Secretary","High Seer","High Senator","High Sentinel","High Shaman","High Strategos","High Templar","Imperator","Inquisitor","Junior Adept","Junior Apprentice","Justicar","King","King's Advisor","King's Guard","King's Knight","Knight","Knight Commander","Librarian","Lord","Lord Commander","Lord General","Mage","Magister","Marshal","Master","Master Chief","Master Father","Mayor","Mentor","Mercenary","Minister","Neophyte","Overlord","Paladin","Palatine","Patriarch","Patroon","Pharaoh","Pilgrim","President","Prime","Prime Chief","Prime General","Prime Justicar","Prime Minister","Prime Paladin","Prime Patriarch","Prime Secretary","Prime Sentinel","Prime Templar","Prince","Professor","Prophet","Protector","Purifier","Ranger","Ranger Commander","Regent","Rogue","Royal Administrator","Royal Advisor","Royal Ambassador","Royal Chamberlain","Royal Consort","Royal Consul","Royal Councillor","Royal Executor","Royal Inquisitor","Royal Justicar","Royal Knight","Royal Mentor","Royal Mercenary","Royal Paladin","Royal Professor","Royal Sage","Royal Saint","Royal Scholar","Royal Secretary","Royal Sentinel","Royal Spokesman","Royal Strategos","Royal Templar","Royal Vizier","Sage","Saint","Scholar","Secretary","Seer","Sellsword","Senator","Sentinel","Shaman","Shogun","Specialist","Spokesman","Squire","Strategos","Sultan","Supervisor","Templar","Trainee","Vizier","Warchief","Warlord","Warmaster","Warrior","Zealot"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}