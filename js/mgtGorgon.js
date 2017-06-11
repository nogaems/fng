var nm1 = ["d","f","h","l","m","n","s","v","w","z"];
var nm2 = ["a","e","i","o","y"];
var nm3 = ["c","g","h","l","ll","m","n","nn","s","th","z"];
var nm4 = ["l","ll","n","r","s","sh"];
var nm5 = ["a","e","a","e","i","i","ia","ea","ae"];

var nm6 = ["Abandoned","Aggressive","Agonized","Ancient","Angry","Arid","Barbarous","Bitter","Blind","Broken","Brutal","Calculated","Callous","Careless","Cold","Corrupt","Corrupted","Crazy","Crone","Crooked","Cruel","Dead","Defiant","Delirious","Deserted","Dire","Dreadful","Dreary","Evil","False","Feral","Fickle","Fierce","Forked","Forsaken","Foul","Grave","Greedy","Grim","Gross","Grotesque","Gruesome","Hag","Harsh","Hateful","Haunting","Heartless","Heinous","Hollow","Impure","Infernal","Insane","Insidious","Jaded","Loathsome","Mad","Maleficent","Malevolent","Malicious","Merciless","Needy","Nefarious","Noxious","Pitiless","Rash","Reckless","Relentless","Ruthless","Sadistic","Savage","Shady","Shallow","Skeletal","Spiteful","Swift","Toxic","Unrelenting","Vicious","Vile","Villain","Villainous","Vindictive","Violent","Warped","Wicked","Wild","Wrathful","Wretched"];

var nm7 = ["Archetype","Sage","Gorgon","Medusa","Mender","Reaper","Sister","Binder","Sentinel","Curator","Custodian","Overseer","Warden","Shepherd","Keeper","Guard","Attendant","Caretaker","Conservator","Sentry","Steward","Warden","Gorgon","Gorgon","Gorgon","Gorgon","Gorgon","Medusa","Medusa","Vixen","Sorceress"];
var nm8 = ["Relics","Souvenirs","Keepsakes","Boulder Beings","Busts","Carnage","Carving","Certitude","Corruption","Crystallization","Despair","Destruction","Dust","Effigies","Ends","Eternal Rest","Figures","Finality","Fossilization","Foundations","Granite","Granite Trophies","Living Fossils","Living Ornaments","Living Statues","Marble","Marble Memories","Memorials","Ornaments","Petrification","Rubble","Ruins","Sculpting","Sculptures","Solid Ends","Solid Sleep","Solidification","Statues","Stiffening","Stone","Stone Cemeteries","Stone Creatures","Stone Death","Stone Desire","Stone Flesh","Stone Images","Stone Memorials","Stone Servants","Stone Skin","Stone Surprise","Stone Trophies","Stonework","the Basin","the Cavern","the Field of Statues","the Forest","the Granite Territory","the Isle","the Lake","the Marsh","the Meadows","the Mountain","the Ruins","the Statue Army","the Statue Shore","the Stone Army","the Stone Cemetery","the Stone Cold Heart","the Stone Garden","the Stone Lake","the Stone Playground","the Swamp","the Wilds"];

var nm9 = ["Aged","Ancient","Angry","Attentive","Austere","Beautiful","Bitter","Blind","Bold","Careless","Cheerful","Cold","Composed","Corrupt","Corrupted","Crooked","Cruel","Defiant","Disfigured","Envious","Evil","Exotic","False","Fearless","Feisty","Forsaken","Fragrant","Glaring","Gleeful","Grave","Grim","Grotesque","Hidden","Hollow","Hungry","Idle","Infamous","Infernal","Insidious","Jaded","Juvenile","Lone","Lonely","Lost","Mad","Masked","Mysterious","Needy","Noxious","Petty","Playful","Prime","Radiant","Scornful","Selfish","Shady","Silent","Somber","Sore","Spiteful","Swift","Tired","Tragic","Twilight","Twin","Unknown","Vengeful","Vicious","Violent","Warped","Wicked","Wrathful","Wretched"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			rnd3 = Math.random() * nm3.length | 0;
			while(nm3[rnd3] === nm1[rnd]){
				rnd = Math.random() * nm1.length | 0;
			}
			rnd4 = Math.random() * nm5.length | 0;
			rnd7 = Math.random() * nm6.length | 0;
			if(i < 3){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm5[rnd4] + " the " + nm6[rnd7];
			}else{
				rnd5 = Math.random() * nm4.length | 0;
				while(nm4[rnd5] === nm3[rnd3]){
					rnd5 = Math.random() * nm4.length | 0;
				}
				rnd6 = Math.random() * nm2.length | 0;
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd6] + nm4[rnd5] + nm5[rnd4] + " the " + nm6[rnd7];
			}
		}else if(i < 8){
			rnd = Math.random() * nm7.length | 0;
			rnd2 = Math.random() * nm8.length | 0;
			names = nm7[rnd] + " of " + nm8[rnd2];
		}else{
			rnd = Math.random() * nm9.length | 0;
			rnd2 = Math.random() * nm7.length | 0;
			names = nm9[rnd] + " " + nm7[rnd2];
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