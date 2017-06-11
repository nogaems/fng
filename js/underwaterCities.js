
function nameGen(){
	var nm1 = ["Aby","Abys","Ache","Acio","Aeg","Amphi","Anu","Aqu","Aqua","Aqui","Asha","Ashe","Atla","Azha","Azu","Beli","Bery","Boy","Bri","Cae","Caenu","Cala","Cata","Cla","Coa","Coara","Cora","Delph","Do","Ebi","Expa","Flu","Gey","Gla","Glaci","Hippo","Hy","Hyd","Jutu","Levi","Levia","Limu","Liqi","Liqu","Liqua","Liqui","Litto","Mari","Mer","Mimi","Nata","Nau","Nauti","Nava","Nep","Neph","Nept","Neptu","Nerei","Neri","Njo","Njor","Oce","Ocea","Osi","Paci","Palae","Pela","Pose","Posei","Pura","Puri","Rive","Sala","Sali","Saph","Saphi","Scy","Sequa","Si","Sire","Squa","Te","Tempe","Teth","Tha","Thala","Thau","The","Tri","Trite","Trito","Tsu","Tsuna","Ty","Typh","Va","Vapo","Voltu","Wata"];
	var nm2 = ["cada","cadis","cia","cique","cis","dor","dore","gia","lean","lin","lina","lis","loch","lona","lor","lora","lore","lune","mari","mon","mond","na","nas","ne","nea","nia","nis","noch","pis","ra","rai","ran","rei","rem","ren","reth","rey","ri","ria","ril","rin","ris","rius","rus","sa","tas","tesh","thas","theas","this","thys","tia","tin","tis","ton","tria","via"];

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