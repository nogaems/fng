var nm1 = ["Aku","Anra","Ari","Axio","Bera","Bi","Bia","Bru","Dena","Dira","Do","Dri","Ja","Jeru","Jia","Jo","Ka","Kara","Kia","Kru","Lira","Lita","Lo","Lori","Me","Mekri","Mi","Mia","Na","Ni","Nira","Nori","Obi","Onu","Ora","Ovi","R'Da","R'Ki","R'Ve","R'Xi","Ra","Rena","Ria","Risu","S'Ha","S'Ki","S'Ma","S'Ri","Sa","Si","Sio","Sira","Tare","Te","Tena","Ti","Tira","Via","Vkru","Vri","Vro","Xa","Xena","Xio","Xiro"];
var nm2 = ["clado","clek","crek","crix","kad","karix","kir","kirud","kix","krax","krikuk","kruvek","kuk","marik","mek","mix","mosik","muk","narix","natek","nuk","nuvik","nux","rad","rarix","rix","ruk","ruvix","sarix","sek","sik","srix","stuk","tek","tix","trik","tuk","turik","vek","vik","vrex","vurik","vux"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}