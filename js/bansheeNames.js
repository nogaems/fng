
function nameGen(){
	var nm1 = ["Abandoned","Aching","Agony","Anguish","Anguished","Bawling","Bitter","Blaring","Blind","Bloodied","Bloody","Broken","Burning","Cackling","Craven","Crazed","Crying","Dark","Deafening","Depraved","Deranged","Dire","Distressed","Drained","Dread","Dreadful","Enraged","Evanescent","Faded","Fading","Flustered","Forsaken","Frail","Grave","Grieving","Grievous","Grim","Haunted","Haunting","Heartrending","Heartsick","Hollow","Hopeless","Howling","Humming","Hurt","Hysterical","Ivory","Lamenting","Lone","Lonely","Lost","Mad","Maniacal","Manic","Mewling","Miserable","Misery","Moaning","Mournful","Mourning","Praying","Ringing","Roaming","Screaming","Screeching","Searching","Seeking","Shadowy","Shady","Shrieking","Silver","Sinister","Skeletal","Skinny","Slivery","Sniveling","Sobbing","Sorrowing","Sorrowing","Spiteful","Tearful","Torment","Tormented","Tortured","Vengeful","Vexed","Vicious","Wailing","Wandering","Warped","Waving","Weeping","Whimpering","Whining","Wicked","Woeful","Worn","Wretched","Yammering","Yelling","Yelping"];
	var nm2 = ["Apparition","Banshee","Bride","Bridesmaid","Dame","Damsel","Daughter","Gal","Girl","Lady","Maid","Maiden","Matriarch","Matron","Mother","Nurse","Priestess","Soul","Specter","Spirit","Widow","Woman","Wraith","Angel","Lover","Fiancee","Child","Youth","Aunt"];
	
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0;
		names = "The " + nm1[rnd] + " " + nm2[rnd2];
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