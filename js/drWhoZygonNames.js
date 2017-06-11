var nm1 = ["B","Br","Cr","D","Dr","G","Gr","K","Kr","R","S","Sr","Str","St","T","Tr","V","Vr"];
var nm2 = ["e","a","o"];
var nm3 = ["d","g","k","l","m","n","s","t","v","w","z"];
var nm4 = ["l","m","n","r","rm","rn","s","st"];

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		rnd3 = Math.floor(Math.random() * nm3.length);
		rnd4 = Math.floor(Math.random() * nm2.length);
		rnd5 = Math.floor(Math.random() * nm4.length);
		names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd5];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}