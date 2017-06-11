var nm1 = ["Abra","Acri","Aera","Alche","Alcho","Alli","Allu","Ana","Ano","Anomali","Apo","Aqua","Aqui","Ar","Arach","Arca","Arcani","Arka","Armada","Aro","Astro","Augu","Aura","Auro","Aurora","Ava","Avala","Avia","Barba","Barra","Blaiz","Blo","Bloo","Boul","Bri","Cala","Cani","Car","Carbo","Ceru","Ceruli","Chakra","Chao","Char","Charo","Chrono","Cim","Clai","Clari","Clou","Colo","Conju","Crea","Cree","Cryo","Crys","Curio","Cyclo","Dae","Daw","Debri","Devi","Dia","Dino","Divi","Divina","Divino","Domi","Domina","Dra","Draca","Draco","Drago","Droi","Dubi","Dyna","Ecli","Eido","Ele","Emera","Emeral","Empea","Enig","Equi","Ethe","Ethere","Exo","Exorci","Fae","Fe","Fel","Feli","Feni","Fer","Fero","Fie","Fiero","Fir","Fla","Flore","Forre","Fossi","Fro","Fue","Furi","Fusi","Fye","Garga","Gargo","Gaze","Gela","Geno","Gho","Giga","Gira","Gla","Glaci","Glamo","Gloo","Gori","Grani","Gro","Grotto","Guru","Halo","Har","Heini","Helli","Herbo","Hocu","Horo","Horro","Hurica","Hydra","Hydro","Hye","Icicli","Igli","Igni","Illu","Imme","Imperi","Impero","Inca","Incanto","Ince","Incorpo","Infer","Infi","Iri","Iro","Jagua","Juju","Kata","Katana","Kine","Kni","Knigh","Koa","Lavi","Le","Leo","Levi","Levia","Lily","Liqui","Ludi","Lumi","Luminu","Lussio","Ma","Mag","Magma","Magne","Mali","Mammo","Mana","Maxi","Meta","Mino","Mobo","Monsoo","Mor","Mosqi","Muta","Myste","Mysteri","Ne","Nefar","Nemo","Neptu","Nero","Nexi","Ninja","Nova","Novi","Octo","Ome","Omega","Ori","Oxy","Ozo","Paci","Para","Parado","Perma","Perra","Peta","Phan","Phanta","Phi","Phili","Phoe","Plu","Pocu","Pow","Precipi","Pri","Prophi","Psy","Puri","Pye","Qua","Quai","Radi","Rag","Ray","Razo","Reve","Rhino","Rive","Robo","Rubi","Sabe","Safri","Sala","Sali","Saphi","Saru","Sava","Scal","Scor","Scorpi","Sere","Serpen","Shado","Shay","Shri","Shy","Sire","Skele","Skye","Slai","Smol","Smoldo","Sola","Soro","Speci","Spiri","Spoo","Squi","Stor","Tempe","Tempri","Terbi","Tero","Terra","Terri","Thau","Thauma","Thor","Tini","Tira","Tita","Tremo","Tropo","Twi","Twilei","Typho","Unani","Uni","Uno","Uvee","Vala","Vapo","Veilio","Veni","Veno","Vexi","Volu","Voodoo","Vultu","Walla","Were","Whimsi","Willo","Windi","Xyge","Zeno","Zephy"];
var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd] + "mon";
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}