var nm3 = ["Commendation","Crescent","Cross","Decoration","Heart","Laurel","Medal","Medallion","Order","Ribbon","Sigil","Star"];
	
function nameGen(type){
	var nm1 = ["Adamant","Angel's","Angelic","Blessed","Brass","Brave","Bright","Cooperative","Courageous","Crown's","Dependable","Dependent","Devoted","Diamond","Diligent","Distinguished","Divine","Dutiful","Earnest","Elated","Emerald","Eternal","Ethereal","Exalted","Fearless","Flawless","Fragile","Gilded","Glorious","Golden","Grateful","Grieving","Hallowed","Heavenly","Honorable","Honored","Infinite","Ivory","Jade","Loyal","Majestic","Marbled","Merciful","Mighty","Radiant","Resonant","Royal","Ruby","Sapphire","Serene","Silent","Silver","Tranquil","United","Velvet","Venerated","Vibrant","Victorious","Vigilant","Winged"];
	var nm2 = ["Air Force","Army","Bravery","Clarity","Conduct","Corps","Defense","Efficiency","Excellence","Flying","Freedom","Gallantry","Independence","Liberation","Liberty","Loyalty","Marine","Marksmanship","Merit","Navy","Peace","Regiment","Service","Services","Soldier","Special Operations","Virtue","Volunteer","Volunteering"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd3 = Math.random() * nm3.length | 0;
		if(i < 4){
			rnd = Math.random() * nm2.length | 0;
			names = nm2[rnd] + " " + nm3[rnd3];
			nm2.splice(rnd, 1);
		}else if(i < 7){
			rnd = Math.random() * nm1.length | 0;
			names = nm1[rnd] + " " + nm3[rnd3];
			nm1.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			names = nm1[rnd] + " " + nm2[rnd2] + " " + nm3[rnd3];
			nm1.splice(rnd, 1);
			nm2.splice(rnd2, 1);
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