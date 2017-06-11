var nm1 = ["C","Ch","D","Dh","G","Gh","K","Kh","R","S","Th","V"];
var nm2 = ["a","aa","e","a","e","a","e","i","o"];
var nm3 = ["c","d","k","m","n","r","s","ss","st","t","th","y"];

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	var ext = Math.floor(Math.random() * 150);
	
	for(i = 0; i < 10; i++){
		if(ext === 1){
			names = "Exterminate! Exterminate! Exterminate!";
			if(i === 9){
				names = "Just kidding. :) Enjoy this Easter egg."
			}
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			names = nm1[rnd] + nm2[rnd2] + nm3[rnd3];
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