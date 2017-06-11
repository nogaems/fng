var nm2 = ["beak","belly","bill","breast","claw","crest","crown","eye","eyes","feather","head","mantle","plume","tail","talon","wing","wings"];

function nameGen(type){
	var nm1 = ["Acid","Anger","Angry","Beam","Bitter","Black","Blade","Bleak","Blood","Bold","Bone","Brass","Bright","Broad","Bronze","Chaos","Cloud","Crazy","Crimson","Crown","Dark","Dawn","Dead","Death","Demon","Devil","Doom","Draft","Dread","Dream","Dusk","Dust","Ebon","Ember","Fire","Flame","Fog","Foul","Frost","Fume","Fury","Ghost","Giant","Glass","Gloom","Gold","Grave","Great","Grey","Grim","Grin","Half","Hate","Hell","Hollow","Ice","Iron","Jade","Kill","Kite","Light","Lightning","Lone","Lunar","Mad","Marsh","Metal","Mist","Moon","Night","Onyx","Phantom","Primal","Prime","Putrid","Quill","Rabid","Rage","Rain","Rapid","Rash","Razor","Red","River","Shadow","Silent","Smoke","Solar","Spark","Spite","Star","Stark","Steel","Stitch","Storm","Sun","Swift","Terror","Thorn","Thrill","Thunder","Twilight","Venom","Warp","Whip"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0;
		names = nm1[rnd] + nm2[rnd2];
		nm1.splice(rnd, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}