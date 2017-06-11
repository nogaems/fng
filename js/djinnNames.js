var nm1 = ["","","","","","b","bh","d","dh","g","gh","h","j","k","m","n","r","s","sh","y","z"];
var nm2 = ["a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","a","e","i","o","u","aa","ee","ua","ai","oo"];
var nm3 = ["b","bb","br","d","h","k","kh","m","n","nq","q","s","sh","sm","ss","sf","st","t","z","zz"];
var nm4 = ["b","bb","d","h","k","m","n","r","rr","rh","s","sh","ss","z","zz"];
var nm5 = ["","","","","d","f","l","m","n","sh","z"];

var nm6 = ["","","","","","","","","f","g","gh","h","j","k","kh","l","m","n","ph","r","s","sh","t","th","w","y","z"];
var nm7 = ["a","e","i","o","u","a","a","i","a","e","i","o","u","a","a","i","a","e","i","o","u","a","a","i","aa","ee","ai","ia"];
var nm8 = ["b","d","dh","dr","f","ff","l","ll","m","mn","r","s","sh","ss","t","th","w","y","z"];
var nm9 = ["d","f","ff","l","ll","m","n","r","s","ss","t","w","y","z"];
var nm10 = ["","","","","","","","","h","l","n"];

var nm11 = ["","","","","","bh","d","dh","g","gh","h","j","k","kh","m","n","r","s","sh","y","z"];
var nm12 = ["a","e","i","o","u","a","a","i","a","e","i","o","u","a","a","i","a","e","i","o","u","a","a","i","aa","ee","ai"];
var nm13 = ["b","bb","d","h","kh","l","m","n","r","rr","s","sh","ss","t","th","z","zz"];
var nm14 = ["b","d","h","l","ll","m","n","r","rr","s","ss","t","y","z","zz"];
var nm15 = ["","","","h","l","m","n","s","z"];

var nm16 = ["Accomplished","Adored","Adventurous","Amazing","Ancient","Austere","Beloved","Better","Bold","Bountiful","Brilliant","Carefree","Courageous","Creative","Cruel","Daring","Devoted","Dreamy","Elegant","Enchanted","Enlightened","Exalted","Extravagant","Fair","Fantastic","Fearless","Fesity","First","Flawless","Fortunate","Friendly","Generous","Gentle","Gifted","Giving","Glamorous","Glorious","Gorgeous","Graceful","Gracious","Grand","Grandiose","Great","Handsome","Happy","Harmonious","Heavenly","Honest","Honored","Humble","Idolized","Illustrious","Impeccable","Incredible","Intrepid","Jolly","Joyful","Joyous","Kind","Kindhearted","Light","Lovable","Loyal","Lucky","Luminous","Lustrous","Luxurious","Magnificent","Majestic","Marvelous","Mighty","Mysterious","Original","Pleasant","Pleasing","Powerful","Precious","Proud","Pure","Radiant","Rewarding","Rich","Royal","Sane","Scented","Serene","Silent","Simple","Spectacular","Stunning","Superior","Swift","Tender","Terrific","Treasured","Tremendous","Trustworthy","Truthful","Unequaled","Venerated","Vibrant","Victorious","Virtuous","Wealthy","Wise","Wonderful"];

var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd16 = Math.floor(Math.random() * nm16.length);
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm6.length);
			rnd2 = Math.floor(Math.random() * nm7.length);
			rnd3 = Math.floor(Math.random() * nm8.length);
			rnd4 = Math.floor(Math.random() * nm7.length);
			rnd5 = Math.floor(Math.random() * nm10.length);
			while(nm8[rnd3] === nm6[rnd]){
				rnd3 = Math.floor(Math.random() * nm8.length);
			}
			if(i < 6){
				names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm10[rnd5] + " the " + nm16[rnd16];
			}else{
				rnd6 = Math.floor(Math.random() * nm9.length);
				rnd7 = Math.floor(Math.random() * nm7.length);
				while(nm9[rnd6] === nm8[rnd3]){
					rnd6 = Math.floor(Math.random() * nm9.length);
				}
				if(i < 8){
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm7[rnd4] + nm9[rnd6] + nm7[rnd7] + nm10[rnd5] + " the " + nm16[rnd16];
				}else{
					names = nm6[rnd] + nm7[rnd2] + nm8[rnd3] + nm9[rnd6] + nm7[rnd7] + nm7[rnd4] + nm10[rnd5] + " the " + nm16[rnd16];
				}
			}
		}else if(tp === 2){
			rnd = Math.floor(Math.random() * nm11.length);
			rnd2 = Math.floor(Math.random() * nm12.length);
			rnd3 = Math.floor(Math.random() * nm13.length);
			rnd4 = Math.floor(Math.random() * nm12.length);
			rnd5 = Math.floor(Math.random() * nm15.length);
			while(nm13[rnd3] === nm11[rnd]){
				rnd3 = Math.floor(Math.random() * nm13.length);
			}
			if(i < 6){
				names = nm11[rnd] + nm12[rnd2] + nm13[rnd3] + nm12[rnd4] + nm15[rnd5] + " the " + nm16[rnd16];
			}else{
				rnd6 = Math.floor(Math.random() * nm14.length);
				rnd7 = Math.floor(Math.random() * nm12.length);
				while(nm14[rnd6] === nm13[rnd3]){
					rnd6 = Math.floor(Math.random() * nm14.length);
				}
				if(i < 8){
					names = nm11[rnd] + nm12[rnd2] + nm13[rnd3] + nm12[rnd4] + nm14[rnd6] + nm12[rnd7] + nm15[rnd5] + " the " + nm16[rnd16];
				}else{
					names = nm11[rnd] + nm12[rnd2] + nm14[rnd6] + nm12[rnd7] + nm13[rnd3] + nm12[rnd4] + nm15[rnd5] + " the " + nm16[rnd16];
				}
			}
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			rnd5 = Math.floor(Math.random() * nm5.length);
			while(nm3[rnd3] === nm1[rnd]){
				rnd3 = Math.floor(Math.random() * nm3.length);
			}
			if(i < 6){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + " the " + nm16[rnd16];
			}else{
				rnd6 = Math.floor(Math.random() * nm4.length);
				rnd7 = Math.floor(Math.random() * nm2.length);
				while(nm4[rnd6] === nm3[rnd3]){
					rnd6 = Math.floor(Math.random() * nm4.length);
				}
				if(i < 8){
					names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5] + " the " + nm16[rnd16];
				}else{
					names = nm1[rnd] + nm2[rnd2] + nm4[rnd6] + nm2[rnd7] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + " the " + nm16[rnd16];
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