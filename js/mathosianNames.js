function nameGen(type){
	var tp = type;
	if(tp === 1){
		var names1 = ["Ad","Adel","Ag","Agn","Al","Am","Amal","And","Ang","Bar","Bern","Birg","Brun","Car","Cec","Cel","Christ","Char","Cor","Clar","Dan","Den","Dor","Ed","El","Elf","Elis","Els","Em","Emil","Er","Es","Est","Flor","Fel","Frid","Gabr","Gen","Gertr","Gret","Gund","Hann","Heid","Helg","Herm","Hild","Ing","Isab","Jan","Johann","Jul","Kar","Kat","Kath","Lar","Lill","Lin","Madel","Marg","Marl","Mel","Mon","Nat","Nic","Petr","Ren","Ros","Sabr","Saman","Ser","Seraph","Sof","Soph","Sus","Ther","Urs","Val","Valer","Ver","Veron","Yv"];
		var names2 = ["a","adette","alena","alie","anda","andra","anie","anna","anze","ara","arete","arie","arina","ascha","atha","auke","ea","eanor","een","efine","egard","ekka","ele","eli","elin","eline","eliy","ella","elle","elore","ena","enie","esia","eth","ette","eva","ia","iane","ice","icia","ie","iela","ienne","ies","ika","ilde","ilia","ily","ina","ind","ine","ion","issa","istel","istin","itha","ivia","izia","olin","oline","onia","onora","ora","ore","othea","otte","ucie","udis","ula","urga","usta"];
	}else{
		var names1 = ["Aar","Ab","Abr","Ach","Ad","Adr","Alb","Ant","Aug","Bast","Ben","Bern","Clem","Den","Diet","Dom","Eb","Eber","Eck","Ed","Edm","Em","Emm","Er","Erh","Erw","Fab","Fer","Ferd","Gab","Ger","Gerw","Gun","Gunt","Har","Hil","Joh","Jos","Kar","Kas","Kon","Len","Mag","Man","Mar","Mark","Mik","Nic","Pat","Patr","Rein","Rob","Ron","Rud","Sam","Stef","Thom","Tob","Vict","Wal","Wolf"];
		var names2 = ["ald","am","amin","an","and","ang","ank","ann","annes","antin","ar","ard","art","aus","echt","ed","egor","elar","emar","end","ens","ent","eph","erhard","ert","etan","ian","ias","ich","ick","ict","ied","iel","ilian","ill","ilus","in","inic","ix","oah","ob","of","olas","old","olf","oman","on","uard","uin","und","ur","ut"];
	}
	
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		rnd2 = Math.floor(Math.random() * names2.length);
		names = names1[rnd] + names2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}