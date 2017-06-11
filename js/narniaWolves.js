var nm1 = ["","","","d","g","h","l","m","n","t","v","z"];
var nm2 = ["a","a","a","a","e","e","i","i","o","o","u","u","u","au","ao","ou","ua"];
var nm3 = ["br","cr","cl","cz","dr","gr","gn","gd","gdr","kn","kr","kl","kd","ld","ldr","lg","lgr","lk","mdr","mk","mr","ng","ngr","nd","ndr","nz","rb","rd","rv","rz","rg","sb","sk","sl","sm","zn","zr","zl"];
var nm4 = ["a","i","a","i","a","i","e","o","u","u"];
var nm5 = ["","k","l","m","n","s","x"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0;
		rnd3 = Math.random() * nm3.length | 0;
		rnd4 = Math.random() * nm4.length | 0;
		rnd5 = Math.random() * nm5.length | 0;
		if(rnd < 3){
			while(rnd5 === 0){
				rnd5 = Math.random() * nm5.length | 0;
			}
		}
		names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm4[rnd4] + nm5[rnd5];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}