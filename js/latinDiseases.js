
function nameGen(){
	var nm1 = [["Abscessus","Abscess"],["Accessio","Seizure"],["Agonia","Cramps"],["Ambustio","Burn"],["Aneurisma","Aneurysm"],["Angina","Chest pain"],["Apoplexia","Stroke"],["Asthenia","Atrophy"],["Ataxia","Ataxia"],["Atrophia","Atrophy"],["Calculus","Stones"],["Cancrum","Canker"],["Carbunculus","Carbuncle"],["Carcinoma","Cancer"],["Catarrhus","Catarrh"],["Cholerica","Cholera"],["Chorea","Dance"],["Colica","Colic"],["Commotio","Concussion"],["Contracture","Stricture"],["Contuses","Bruised"],["Contusio","Contusion"],["Convulsio","Convulsion"],["Convulsionis","Convulsions"],["Crampus","Cramps"],["Debilitas","Weakness"],["Dolor","Pain"],["Ecclampsia","Convulsions"],["Exhaustio","Exhaustion"],["Explosio","Explosion"],["Fatuitas","Idiocy"],["Febris","Fever"],["Fracture","Fracture"],["Fulmen","Lightning"],["Galbanus","Jaundice"],["Gangraena","Gangrene"],["Gelatio","Frost"],["Glarea","Gravel"],["Haemorrhagia","Hemorrhage"],["Haemorrhois","Hemorrhoids"],["Hydrocephalus","Hydrocephalus"],["Hydropisis","Dropsis"],["Hydrops","Dropsis"],["Ictus","Trauma"],["Ignis","Burning"],["Infectio","Infection"],["Infirmus","Weak"],["Inflammatio","Inflammation"],["Intessusceptio","Intussusception"],["Lepra","Leprosy"],["Marasmus","Weakness"],["Mollities","Softening"],["Morbilli","Measles"],["Morbus","Disease"],["Mors","Death"],["Myelitis","Paraplegia"],["Noctis","of the Night"],["Noma","Canker"],["Obitus","Death"],["Obstructiones","Obstruction"],["Otitis","Inflammation"],["Peritus","Deceased"],["Perniciose","Pernicious"],["Pestis","Plague"],["Phthisis","Consumption"],["Plaga","Plague"],["Pleuritis","Pleuritis"],["Privatio","Priviation"],["Rheumatismus","Rheumatism"],["Scophulosis","Scrofula"],["Scorbutus","Scurvy"],["Senilis","Weakness"],["Spasmus","Spasms"],["Tussis","Cough"],["Ulcus","Ulcer"],["Venenatio","Poisoning"],["Vermis","Worms"],["Vitium","Disease"]];
	var nm2 = [["Abdmonis","Abdominal"],["Abdominalis","Abdominal"],["Acerbus","Sharp"],["Agita","Shaking"],["Alvus","Belly"],["Articulorum","Joint"],["Bracium","Arm"],["Caput","Head"],["Cerebralis","Cerebrum"],["Cerebri","Brain"],["Cerebri","Cerebral"],["Clarus","Clear"],["Collum","Neck"],["Cordis","Heart"],["Coxa","Hip"],["Cutis","Skin"],["Dentes","Teeth"],["Dextra","Right"],["Epiglottidis","Eppiglotis"],["Flava","Yellow"],["Flores","Flower"],["Folia","Leaf"],["Frigor","Cold"],["Fuscus","Brown"],["Fuscus","Dark"],["Glottidis","Glottis"],["Hectica","Hectic"],["Hirudo","Leech"],["Ilii","Ilium"],["Incisum","Cut"],["Incognita","Unidentified"],["Infantilis","Infantile"],["Inflammatoria","Inflammatory"],["Intermittens","Intermittent"],["Jecoris","Liver"],["Laceratum","Lacerated"],["Laryngea","Larynx"],["Luteus","Yellow"],["Magnus","Mighty"],["Membranacea","Membrane"],["Motus","Locomotion"],["Nervosa","Nervous"],["Niger","Black"],["Molle","Soft"],["Mollis","Soft"],["Os","Mouth"],["Ovarii","Ovarian"],["Pancreatis","Pancreas"],["Pectus","Breast"],["Pedicularis","Louse"],["Pes","Foot"],["Petechialis","Spotted"],["Prostata","Prostate"],["Puerperalis","Puerperal"],["Pulmonum","Lung"],["Punctum","Stabbed"],["Putrida","Rotten"],["Remittens","Remittent"],["Rheumatica","Rheumatic"],["Rubra","Scarlet"],["Rumen","Throat"],["Siccus","Dry"],["Spissus","Dense"],["Sacer","Sacred"],["Senilis","Dry"],["Vulnus","Wounded"],["Ustus","Burnt"],["Sinistra","Left"],["Tonsillaris","Tonsils"],["Ulna","Arm"],["Ulna","Elbow"],["Uteri","Uterus"],["Ventriculi","Stomach"],["Verminosa","Verminous"],["Astuosa","Hot"],["Aquaticum","Aquatic"],["Arenosum","Sandy"],["Candidulum","Shining"],["Cavum","Hollow"],["Cerritum","Frantic"]];
	var nm3 = ["Ab","Absce","Acce","Ago","Am","Ambu","Aneu","Angi","Apo","As","Asthe","Atro","Ca","Cal","Calcu","Can","Car","Carbu","Cata","Cho","Chole","Co","Coli","Commo","Con","Contra","Contu","Convu","Cra","Cram","Debi","Do","Eccla","Ex","Explo","Fa","Fatui","Fe","Fi","Fra","Ga","Gal","Galba","Gela","Gla","Haemo","Hy","Hydro","In","Infe","InfiInfla","Inte","Intes","Le","Ma","Mara","Molli","Mor","Morbi","Mye","Noc","Peri","Perni","Pes","Phthi","Pla","Pleu","Pri","Priva","Rheu","Sco","Scophu","Scor","Se","Seni","Spa","Spas","Tu","Ve","Vene","Ver","Vi"];
	var nm4 = ["banus","bus","cinoma","ciose","crum","culus","cus","drops","fectio","firmus","ga","gina","graena","hagia","li","lica","lis","litas","lities","litis","lor","losis","lus","ma","matio","men","mis","motio","mus","natio","nia","nis","noma","nus","phalus","phia","pisis","plexia","pus","ra","rea","rhagia","rhus","rica","ris","risma","ritis","sceptio","ses","sia","sio","sionis","sis","sus","tas","ties","tio","tiones","tis","tismus","tium","ture","tus","tuses","vatio","xia"];
	
	var br = "";

	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd][0] + " " + nm2[rnd2][0] + " ("  + nm2[rnd2][1] + " " + nm1[rnd][1] + ")";
			nm1.splice(rnd, 1);
			nm2.splice(rnd2, 1);
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			rnd2 = Math.floor(Math.random() * nm4.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			while(rnd === rnd3){
				rnd3 = Math.floor(Math.random() * nm3.length);
			}
			rnd4 = Math.floor(Math.random() * nm4.length);
			while(rnd2 === rnd4){
				rnd4 = Math.floor(Math.random() * nm4.length);
			}
			names = nm3[rnd] + nm4[rnd2] + " " + nm3[rnd3] + nm4[rnd4];
			nm3.splice(rnd, 1);
			nm3.splice(rnd3, 1);
			nm4.splice(rnd2, 1);
			nm4.splice(rnd4, 1);
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