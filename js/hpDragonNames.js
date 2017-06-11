var nm1 = ["Algerian","American","Angolan","Antarctic","Argentinian","Armenian","Australian","Austrian","Bolivian","Brazilian","British","Bulgarian","Cambodian","Canadian","Chilean","Chinese","Croatian","Cuban","Danish","Egyptian","Finnish","French","German","Hungarian","Indian","Irish","Italian","Jamaican","Japanese","Mexican","Mongolian","Moroccan","Nepalese","Norwegian","Peruvian","Romanian","Russian","Slovenian","South-African","Spanish","Swedish","Thai","Turkish","Ukrainian","Vietnamese"];
var nm2 = ["Barb","Blaze","Bristle","Dart","Demon","Ember","Fire","Flame","Foul","Fury","Giant","Glow","Horn","Iron","Jade","Long","Mammoth","Monster","Opal","Plate","Rage","Ridge","Ruby","Short","Smooth","Snake","Soft","Spark","Spike","Steel","Storm","Swift","Thin","Thorn","Thunder","Venom","Vile","Viper","Warp","Wide"];
var nm3 = ["back","belly","bottom","claw","crown","dart","eye","fang","frame","gut","head","horn","muzzle","paw","rump","scale","skull","snout","spike","stub","tail","tooth","trunk","tusk","wing"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		names = nm1[rnd] + " " + nm2[rnd2] + nm3[rnd3];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}