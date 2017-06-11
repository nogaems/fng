var nm1 = ["'","'","'","'","'","'","'","b","ch","d","dh","f","g","gh","h","hl","k","kh","l","m","n","p","q","r","s","sh","ss","t","th","tl","ts","v","w","y","z","zh"];
var nm1c = ["'","'","'","'","'","'","'","B","Ch","D","Dh","F","G","Gh","H","Hl","K","Kh","L","M","N","P","Q","R","S","Sh","Ss","T","Th","Tl","Ts","V","W","Y","Z","Zh"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","y","a","e","i","o","u","a","e","i","o","u","a","e","o","i","u","au","ai","ua","ue","ae","ai","oi"];
var nm2c = ["A","E","I","O","U","A","E","I","O","U","A","E","I","O","U","A","E","I","O","U","Y","A","E","I","O","U","A","E","I","O","U","A","E","O","I","U","Au","Ai","Ua","Ue","Ae","Ai","Oi"];
var nm3 = ["","","","","","","","","","","","","l","m","n","ng","r","s","sh","ss","y"];
var nm4 = ["hl","k","kh","l","l","l","l","l","l","l","m","n","m","n","m","n","m","n","ng","r","r","r","s","sh","tl"];
var nm5 = ["hi","hi","hi","hi","hi","hi","hi","hi","dhu","vu"];

var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm1.length);
			rnd4 = Math.floor(Math.random() * nm3.length);
			rnd5 = Math.floor(Math.random() * nm2.length);
			rnd6 = Math.floor(Math.random() * nm1.length);
			rnd7 = Math.floor(Math.random() * nm3.length);
			rnd8 = Math.floor(Math.random() * nm2.length);
			rnd9 = Math.floor(Math.random() * nm4.length);
			
			rnd10 = Math.floor(Math.random() * nm1.length);
			rnd11 = Math.floor(Math.random() * nm2.length);
			rnd12 = Math.floor(Math.random() * nm1.length);
			rnd13 = Math.floor(Math.random() * nm3.length);
			rnd14 = Math.floor(Math.random() * nm2.length);
			rnd15 = Math.floor(Math.random() * nm1.length);
			rnd16 = Math.floor(Math.random() * nm3.length);
			rnd17 = Math.floor(Math.random() * nm2.length);
			rnd18 = Math.floor(Math.random() * nm4.length);
			rnd19 = Math.floor(Math.random() * nm5.length);
			if(i % 2 === 0){
				lName = nm5[rnd19] + nm1c[rnd10] + nm2[rnd11] + nm1[rnd12] + nm3[rnd13] + nm2[rnd14] + nm4[rnd18];
			}else if(i % 3 === 0){
				lName = nm5[rnd19] + nm1c[rnd10] + nm2[rnd11] + nm1[rnd12] + nm3[rnd13] + nm2[rnd14];
			}else{
				lName = nm5[rnd19] + nm2c[rnd11] + nm1[rnd12] + nm3[rnd13] + nm2[rnd14] + nm4[rnd18];
			}
			if(i < 2){
				names = nm2c[rnd2] + nm1[rnd3] + nm3[rnd4] + nm2[rnd5] + " " + lName;
			}else if(i < 4){
				names = nm2c[rnd2] + nm1[rnd3] + nm3[rnd4] + nm2[rnd5] + nm4[rnd9] + " " + lName;
			}else if(i === 4){
				names = nm2c[rnd2] + nm1[rnd3] + nm3[rnd4] + nm2[rnd5] + nm1[rnd6] + nm3[rnd7] + nm2[rnd8] + " " + lName;
			}else if(i === 5){
				names = nm1c[rnd] + nm2[rnd2] + nm4[rnd9] + " " + lName;
			}else if(i === 6){
				names = nm1c[rnd] + nm2[rnd2] + nm1[rnd3] + nm3[rnd4] + nm2[rnd5] + " " + lName;
			}else if(i === 7){
				names = nm1c[rnd] + nm2[rnd2] + nm1[rnd3] + nm3[rnd4] + nm2[rnd5] + nm4[rnd9] + " " + lName;
			}else if(i === 8){
				names = nm1c[rnd] + nm2[rnd2] + nm1[rnd3] + nm3[rnd4] + nm2[rnd5] + nm1[rnd6] + nm3[rnd7] + nm2[rnd8] + " " + lName;
			}else if(i === 9){
				names = nm1c[rnd] + nm2[rnd2] + nm1[rnd3] + nm3[rnd4] + nm2[rnd5] + nm1[rnd6] + nm3[rnd7] + nm2[rnd8] + nm4[rnd9] + " " + lName;
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