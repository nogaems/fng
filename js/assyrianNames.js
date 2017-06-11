var nm1 = ["Hermes","Nenos","Toma","Abazu","Abel","Abudemio","Adad-nirari","Adad-salulu","Adamu","Adasi","Ador","Ador eil","Ador palasar","Aileen","Ajdina","Akhiban","Akhiqar","Akhiseen","Akiya","Aminu","Ammina","Anlel","Anokeen","Apiashal","Aprim","Aram","Aram seen","Arik-den-ili","Arseen","Ashur","Ashur ban","Ashur dan","Ashur leed","Ashur ram","Ashur seen","Ashur-Dan","Ashur-apla-idi","Ashur-bel-nisheshu","Ashur-dugul","Ashur-etil-ilani","Ashur-nadin-ahhe","Ashur-nadin-apli","Ashur-nasir-pal","Ashur-nirari","Ashur-rabi","Ashur-rim-nisheshu","Ashur-shaduni","Ashur-uballit","Ashurbanipal","Asinum","Asor","Asor khadon","Asu","Athan","Atrus","Aulada","Aumana","Auneir","Aurnina","Awa","Awbaleet","Awi bail","Awi eil","Awidan","Awimalich","Awinam","Awiqam","Awiram","Awiseen","Awitar","Awiya","Awrahim","Awshalim","Azarah","Bail","Bailbrone","Baildan","Bailnam","Bailram","Bailseen","Bailshar","Banipal","Bardeen","Bardisan","Bareil","Barseen","Barsheen","Baryamin","Baryoom","Bazaya","Bel-bani","Belu","Bibla","Binatour","Bineil","Borseen","Dani eil","Dem ashur","Dem atour","Dem eil","Dem seen","Didanu","Dinkha","Domara","Dorara","Eil","Eilbra","Eilbroon","Eilmar","Eilram","Eliya","Enlil","Enlil-kudurri-usur","Enlil-nasir","Enlil-nirari","Eriba-Adad","Erishum","ErishumI","Esarhaddon","Esho","Gamri eil","Gawri eil","Gbar eil","Giliana","Ha wail","Habib","Hadirseen","Hale","Hamed","Hanodeen","Hanu","Harharu","Harshu","Hayani","Hda eil","Ikunum","Ila-kabkabu","Ilu-Mer","Ilu-shuma","Imshu","Ipqi-Ishtar","Iptar-Sin","Ishme-Dagan","Khaled","Khalil","Khammo","Khnan eil","Khnan seen","KhnanishoAa","Khnanya","Khonayn","Khza eil","Kikkiya","Kushi","Laith","Lammo bail","Lammo eil","Libaya","Lullaya","Madsa","Malik","Man'nah","Mandaru","Mar bail","Mar eil","Mardeen","Mardokh","Maro eil","Marodeen","Maron","Marona","Meesha","Mekha eil","Mlimar","Musa","Mut-Ashkur","NaSsir","Nabo","Nabo bail","Nabo eil","Nabo need","Nabo pal","Nabo ram","Naheer seen","Nahroona","Naram eil","Naram seen","Naram-Suen","Nardeen","Nasir-Sin","Nasirpal","Natan","Natni eil","Nebu","Nebuchadnezzar","Neen eil","Nin seen","Nineel","Ninos","Ninurta-apal-Ekur","Nirar","Nosard eil","Nuabu","Nur-ili","Paldeen","Paseena","Pera","Pnu eil","Pol","Puzur-Ashur","Rab bail","Rab eil","Rab seen","Rabila","Rabona","Rafa eil","Ram bail","Ram eil","Ram seen","Raman","Ramsen","Rimush of Assyria","Romrama","Samani","Sard eil","Sardanapal","Sargon","Seen","Seen eil","Seena","Semiramis","Sennacherib","Sha'ol","Shalim-ahum","Shalmaneser","Shalmanisar","Shammina","Shamshi-Adad","Shar eil","Sharma-Adad","Sharo","Sharokeen","Shaybo","Shimmokeen","Shmou eil","Shnina","Shu-Ninua","Sin-namir","Sin-shar-ishkun","Sin-shumu-lishir","Suhlamu","Sulili","Tiglath-Pileser","Ttwa eil","Tudiya","Tukulti-Ninurta","Ushpia","Ward eil","Ward seen","Warda","Wardeen","Yadida","Yakmeni","Yakmesi","Yangi","Yau seen","Yaw bail","Yaw eil","Yazkur-el","Yomadan","Zah eil","Zah seen","Zaia","Zda eil","Zomaya","Zuabu"];
var nm2 = ["Mariam","Nardeen","Yamima","Danila","Sadi","Abella","Achadina","Adorina","Akhita","Anochina","Aramina","Arbella","Ari eil","Ashourina","Asia","Asia","Asiah","Atourina","Aurhai","Aurya","Awijil","Awita","Baila","Baileet","Beerta","Bet eil","Biblina","Brat bail","Brat eil","Brat youm","Damrina","Domarina","Eilbrat","Eilina","Emmita","Hani'ata","Hano","Huda","Ishtar","Ishtar","Khannah","Kushi","Larsa","Lawita","Lea","Leah","Leah","Leja","Lejka","Lelu","Lilith","Lolita","Lwita","Madjida","Marbita","Mardina","Marina","Marjanita","Marnita","Martha","Milta","Muneera","Nahida","Nahrina","Naramsina","Nardina","Nashiram","Nasibin","Nineveh","Ninorta","Ninsina","Ninsun","Osmet","Paldina","Panna","Pari","Ramina","Ramsina","Rashomta","Rdita","Sahdina","Sawrina","Shamiram","Shamiran","Shamyran","Shamreta","Shamrina","Shamura","Sharokina","Shimta","Shirat","Simta","Sorme","Ur","Walita","Wardina","Wardiya","Yaeeta","Yata","Yayota"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd];
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