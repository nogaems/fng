var nm1 = ["","","","","c","g","h","k","n","s","t","th","z"];
var nm2 = ["a","e","a","e","a","e","i","o","a","e","i","o","eo","io","y","y","ia","ea"];
var nm3 = ["d","dh","dr","g","gg","gh","gr","k","kh","kk","kr","lg","lk","nk","nr","rg","rk","sk","th","tr"];
var nm4 = ["m","n","s","t","x"];
var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
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