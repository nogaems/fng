var nm1 = ["b","c","d","f","g","h","i","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z","","","","",""];
var nm2 = ["a","e","o","u"];
var nm3 = ["br","cr","dr","fr","gr","pr","str","tr","bl","cl","gl","pl","sl","sc","sk","sm","sn","sp","st","sw","ch","sh","th","wh"];
var nm4 = ["ae","ai","ao","au","a","ay","ea","ei","eo","eu","e","ey","ua","ue","ui","uo","u","uy","ia","ie","iu","io","iy","oa","oe","ou","oi","o","oy"];
var nm5 = ["stan","dor","vania","nia","lor","cor","dal","bar","sal","ra","la","lia","jan","rus","ze","tan","wana","sil","so","na","le","bia","ca","ji","ce","ton","ssau","sau","sia","ca","ya","ye","yae","tho","stein","ria","nia","burg","nia","gro","que","gua","qua","rhiel","cia","les","dan","nga"];
var nm6 = ["ia","a","en","ar","istan","aria","ington","ua","ijan","ain","ium","us","esh","os","ana","il","ad","or","ea","eau","ax","on","ana","ary","ya","ye","yae","ait","ein","urg","al","ines","ela"];
var vowel = ["a","e","i","o","u","y"];
var dVowel = ["aa","ae","ai","ao","ae","ea","ee","ei","eo","eu","ia","ie","ii","io","iu","oa","oe","oi","oo","ou","ua","ue","ui","uo","uu"];
var ranNames = [];
var br = "";
var cust = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var endings = ["n","an","ian","anian","nian","in","ine","ite","r","er","eno","ino","ish","ene","ensian","ard","ese","lese","vese","nese","i","ic","iot","iote","asque","gian","onian","vian"];
	var endingSplice = ["an","ian","anian","in","ine","ite","er","eno","ino","ish","ene","ensian","ard","ese","i","ic","iot","iote","asque","onian"];
	var endingNoSplice = ["nan","nian","nin","no","ne","nsian","lese","vese","nese","gian","vian","lian"];
	var cEndingSplice = ["an","ian","anian","in","ine","ite","er","eno","ino","ish","ene","ensian","ard","ese","i","ic","iot","iote","asque","onian"];
	var cEndingNoSplice = ["n","an","an","anian","nian","in","ine","ite","er","eno","ino","ish","ene","ensian","ard","ese","lese","vese","nese","i","ic","ot","ote","asque","gian","onian","vian"];
	var vowelLast = "no";
	var dVowelLast = "no";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(j = 0; j < 10; j++){
		if(j < 2){
			rnd = (Math.random() * nm1.length | 0);
			rnd2 = (Math.random() * nm2.length | 0);
			rnd3 = (Math.random() * nm3.length | 0);
			rnd5 = (Math.random() * cEndingSplice.length | 0);
			ranNames[j] =  nm1[rnd] + nm2[rnd2] + nm3[rnd3] + cEndingSplice[rnd5];
		}else if(j < 4){
			rnd = (Math.random() * nm1.length | 0);
			rnd2 = (Math.random() * nm2.length | 0);
			rnd3 = (Math.random() * nm3.length | 0);
			rnd4 = (Math.random() * nm6.length | 0);
			ranNames[j] = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm6[rnd4];
		}else if(j < 6){
			rnd = (Math.random() * nm3.length | 0);
			rnd2 = (Math.random() * nm4.length | 0);
			rnd3 = (Math.random() * nm5.length | 0);
			ranNames[j] = nm3[rnd] + nm4[rnd2] + nm5[rnd3];
		}else if(j < 8){
			rnd = (Math.random() * nm2.length | 0);
			rnd2 = (Math.random() * nm3.length | 0);
			rnd3 = (Math.random() * nm6.length | 0);
			ranNames[j] = nm2[rnd] + nm3[rnd2] + nm6[rnd3];
		}else{
			rnd = (Math.random() * nm3.length | 0);
			rnd2 = (Math.random() * nm4.length | 0);
			rnd3 = (Math.random() * nm1.length | 0);
			rnd4 = (Math.random() * cEndingSplice.length | 0);
			ranNames[j] =  nm3[rnd] + nm4[rnd2] + nm1[rnd3] + cEndingSplice[rnd4];
		}
	}

	for(i = 0; i < 10; i++){
		if($('#custName').is(':checked')){
			cust = $(".custName").val();
		}else{
			cust = ranNames[i];
		}
		custLast = cust.slice(-1);
		custLastTwo = cust.slice(-2);
		for(j = 0; j < vowel.length; j++){
			if(custLast === vowel[j]){
				vowelLast = "yes";
				cEndingSplice = ["an","ian","anian","in","ine","ite","er","eno","ino","ish","ene","ensian","ard","ese","i","ic","iot","iote","asque","onian"];
				cEndingNoSplice = ["n","an","an","anian","nian","in","ine","ite","er","eno","ino","ish","ene","ensian","ard","ese","lese","vese","nese","i","ic","ot","ote","asque","gian","onian","vian"];
			}else{
				vowelLast = "no";
			}
		}
		for(k = 0; k < dVowel.length; k++){
			if(custLastTwo === dVowel[k]){
				dVowelLast = "yes";
				endingSplice = ["an","ian","anian","in","ine","ite","er","eno","ino","ish","ene","ensian","ard","ese","i","ic","iot","iote","asque","onian"];
				endingNoSplice = ["nan","nian","nin","no","ne","nsian","lese","vese","nese","gian","vian","lian"];
			}else{
				dVowelLast = "no";
			}
		}
		var cRan = (Math.random() * cEndingNoSplice.length | 0);
		var ran = (Math.random() * endingNoSplice.length | 0);
		var csRan = (Math.random() * cEndingSplice.length | 0);
		var sran = (Math.random() * endingSplice.length | 0);
		if(vowelLast === "yes"){
			if(i < 5){
				names = cust.slice(0, -1) + endingSplice[sran];
				endingSplice.splice(sran, 1);
			}else{
				names = cust.slice(0, -1) + endingNoSplice[ran];
				endingNoSplice.splice(ran, 1);
			}
		}else if(dVowelLast === "yes"){
			if(i < 5){
				if(cust.length < 5){
					names = cust.slice(0, -1) + endingSplice[cran];
					endingSplice.splice(sran, 1);
				}else{
					names = cust.slice(0, -2) + cEndingSplice[csRan];
					cEndingSplice.splice(csRan, 1);
				}
			}else{
				if(cust.length < 5){
					names = cust.slice(0, -1) + endingSplice[cran];
					endingSplice.splice(sran, 1);
				}else{
					names = cust.slice(0, -2) + cEndingNoSplice[cRan];
					cEndingNoSplice.splice(cRan, 1);
				}
			}
		}else{
			if(i < 4){
				names = cust + endingSplice[sran];
				endingSplice.splice(sran, 1);
			}else if(i < 6){
				names = cust.slice(0, -1) + endingSplice[sran];
				endingSplice.splice(sran, 1);
			}else if(i < 8){
				if(cust.length < 5){
					names = cust.slice(0, -1) + endingSplice[sran];
					endingSplice.splice(sran, 1);
				}else{
					names = cust.slice(0, -2) + endingSplice[sran];
					endingSplice.splice(sran, 1);
				}
			}else{
				if(cust.length < 5){
					names = cust.slice(0, -1) + endingSplice[sran];
					endingSplice.splice(sran, 1);
				}else{
					names = cust.slice(0, -3) + endingSplice[sran];
					endingSplice.splice(sran, 1);
				}
			}
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