
function nameGen(){
	var nm1 = ["Absi","Ager","Alus","Arak","Arkis","Arma","Awa","Bassi","Beerus","Bourbu","Bouru","Calva","Calvad","Cha","Champa","Chi","Cid","Cide","Cog","Cogna","Daiqui","Deira","Deiras","Gani","Ginge","Gria","Guino","Gyn","Ider","Ine","Jen","Jenev","Jenne","Jiu","Kari","Karis","Keffi","Kefi","Kumi","Kuras","Lagus","Magna","Magnac","Manche","Manchi","Marsa","Mea","Meada","Meadas","Mez","Mezca","Moonshi","Mooshi","Nac","Neve","Never","Niha","Pache","Pagne","Para","Paras","Perie","Quiri","Rai","Raici","Raicil","Raki","Rakis","Sak","Sakis","Sakus","Sala","Salas","Sangris","Santis","Shou","Sin","Singa","Sinthe","Sojus","Sontis","Teq","Teqi","Tequi","Tes","Tonton","Vado","Vados","Vod","Vodkis","Waine","Whis","Wynn"];

	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd];
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