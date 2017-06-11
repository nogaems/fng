var symArms = [["¯\\","/¯"],["¯\\_","_/¯"],["ƪ","ʃ"],["ɳ","ɲ"],["ʅ","ʃ"],["ε","з"],["ζ","ᶘ"],["щ","щ"],["٩","۶"],["૮","ა"],["୧","୨"],["ლ","ლ"],["ᕙ","ᕗ"],["ᕦ","ᕤ"],["⌐","¬"],["┌","┐"],["┐","┌"],["╚","=┐"],["☜","☞"],["☞","☜"],["ヽ","ﾉ"],["ヾ","ﾉ"],["乁","ㄏ"],["(\\/)","(\\/)"],["\\","/"],["\\,,/","\\,,/"],["\\m/","\\m/"],["~","~"],["/","\\"]];
var rArms = [["¬","¬"],["ɲ","ɲ"],["ʃ","ʃ"],["з","з"],["щ","щ"],["۶","۶"],["૮","૮"],["୨","୨"],["ง","ง"],["ა","ა"],["ᕤ","ᕤ"],["ᶘ","ᶘ"],["∩","⊃"],["┐","┐"],["☞","☞"],["っ","っ"],["づ","づ"],["ノ","ノ"],["ヘ","ヘ"],["ㄏ","ㄏ"],["/","/"],["=┐","=┐"],["~","~"]];
var lArms = [["ƪ","ƪ"],["ɳ","ɳ"],["ʅ","ʅ"],["ε","ε"],["ζ","ζ"],["૮","૮"],["୧","୧"],["ა","ა"],["ღ","ღ"],["ᕕ","ᕕ"],["ᕦ","ᕦ"],["⌐","⌐"],["┌","┌"],["╚","╚"],["☜","☜"],["ノ","ノ"],["ヘ","ヘ"],["ヽ","ヽ"],["乁","乁"],["\\","\\"],["~","~"]];
var armFaces = [["(",")"],["[","]"],["﴾","﴿"],["|","|"],["((","))"],["༼","༽"]];
var faces = [["",""],["ʕ","ʔ"],["﴾","﴿"],["|","|"],["|(",")|"],["ᔑ","ᔐ"],["꒰","꒱"],["((","))"],["[","]"],["|[","]|"],["{","}"],["<",">"],["ʢ","ʡ"],["[","]"],["ᖗ","ᖘ"],["ᕳ","ᕲ"],["୧","୨"],["୨","୧"],["┬┴┬┴┤",")├┬┴┬┴"],["┬┴┬┴┤(","├┬┴┬┴"],["≧","≦"],["༼","༽"]];
var eyes = [["¬","¬"],["°","°"],["°","o"],["´","`"],["º","°"],["º","º"],["ì","í"],["Ɵ͆","Ɵ͆"],["Ȍ","Ȍ"],["ȍ","ő"],["ȍ","ȍ"],["ʘ","ʘ"],["˘","˘"],["͌","͌"],["͠°","°"],["͠°","͠°"],["͡°","͡°"],["͡⎚","͡⎚"],["͡","͡"],["σ","σ"],["ب","ب"],["܍","܍"],["ఠ","ఠ"],["ಠ","ಠ"],["ಥ","ಥ"],["ರ","ರ"],["ළ","ළ"],["๏̯͡","๏̯͡"],["ຈ","ຈ"],["ᗒ","ᗕ"],["ᚖ","ᚖ"],["ᴗ","ᴗ"],["ᵔ","ᵔ"],["ὁ","ὀ"],["•̀","•̀"],["•","•"],["↼","⇀"],["⇀","↼"],["≋","≋"],["⊙","⊙"],["⊜","⊜"],["⌐■","■¬"],["⌒","⌒"],["⍜","⍜"],["⍤","⍤"],["⎚","⎚"],["⏒","⏒"],["⏓","⏓"],["╹","╹"],["■","■"],["▰","▰"],["▶","◀"],["▾","▾"],["◉","◉"],["◍","◍"],["◎","◎"],["◔","◔"],["◕","◕"],["◥","◤"],["☯","☯"],["♥","♥"],["⚆","⚆"],["⚙͠","⚙͠ "],["✘","✘"],["✧","✧"],["✿","✿"],["❂","❂"],["❍","❍"],["⟃","⟄"],["⨱","⨱"],["⨴","⨵"],["⨶","⨶"],["⩹","⩺"],["⩺","⩹"],["⩿","⪀"],["⪦","⪧"],["⪧","⪦"],["⪨","⪩"],["⪩","⪨"],["⪰","⪯"],["⫑","⫒"],["ⱺ","ⱺ"],["⸟","⸟"],["・","・"],["一","一"],["ꔸ","ꔸ"],["ꖘ","ꖘ"],["ꗞ","ꗞ"],["꘠","꘠"],["Ꝋ","Ꝋ"],["︶","︶"],["ﾟ","ﾟ"],["￣","￣"],["'̀","'̀"],["-","-"],[".","."],["<",">"],[">","ლ"],[">","<"],["T","T"],["^","^"],["`","´"],["o","°"],["o","o"],["x","x"]];
var eyeEffects = [["",""],["´","`"],["ˇ","ˇ"],["ღ","ღ"],["ᚖ","ᚖ"],["ᵒ","ᵒ"],["≧","≦"],["▰","▰"],["♪","♪"],["っ","ς"],["｡","｡"],["","´"],["","ʋ"],["","ˇ"],["","ᚖ"],["","‶"],["","✘"],["","✧"],["","✿"],["","ꐦ"],["","\""],["","*ﾟ"],["",";"],["","`"],["=","="],["`","´"]];
var mids = ["³","·","Ĺ̯","ʖ̯","͜ʖ","͜つ","͟ʖ","͟ل͜","ε","ω","ϖ","Д","д","Ѡ","ѽ","ل͜","ڡ","౪","ഌ","෴","Ꮂ","ᗜ","ᗝ","ᗩ","ᨎ","ᴗ","ᴥ","‸","‿‿","‿","∀","∇","⍊","⍘","⏏","╭╮","□","◞౪◟","◡","ロ","ヮ","人","益","ꎁ","ꔢ","호","︿","﹏","!","-",".","V","_","o","v","~"];
var symEffects = [["",""],["♪","♪"],["(.o. )︵","︵( .o.）"],["┻━┻︵","︵┻━┻"],["✿","✿"],["┻━┻ミ","彡┻━┻"],["(.o. )ミ","彡( .o.)"],["( .□.）\\ミ","彡/(.□. ）"],["｡","｡"],["｡゜","゜｡"],["由","由"],["‿︵‿︵‿","‿︵‿︵‿"],["✌","✌"],["ミ","ミ"],["☝","☝"]];
var rightEffects = ["","︵┻━┻","︵( .o.)","︵/(.□. ）","☝","彡┻━┻","彡( .o.)","✿","彡/(.□. ）","┬──┬","由","*:･ﾟ✧","♪♪ ♪","♪♪","♪"];
var leftEffects = ["","┻━┻︵","(.o. )︵","( .□.）\\︵","☝","┻━┻ミ","(.o. )ミ","✿","( .□.）\\ミ","┬──┬","由","✧ﾟ･:*","♪♪ ♪","♪♪","♪"];

var br = "";

	var faceLeft = "";
	var faceRight = "";
	var eyeLeft = "";
	var eyeRight = "";
	var armRight = "";
	var armLeft = "";
	var armInRight = "";
	var armInLeft = "";
	var extraLeft = "";
	var extraRight = "";
	var mid = "";
	var effectLeft = "";
	var effectRight = "";
function nameGens(type){

	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 8; i++){
		if(i < 2){
			rnd = Math.random() * symArms.length | 0;
			rnd2 = Math.random() * armFaces.length | 0;
			rnd3 = Math.random() * eyes.length | 0;
			rnd4 = Math.random() * mids.length | 0;
			rnd7 = Math.random() * 5 | 0;
			rnd8 = Math.random() * 3 | 0;
			if(rnd7 === 0){
				rnd5 = Math.random() * symEffects.length | 0;
			}else{
				rnd5 = 0;
			}
			if(rnd8 === 0){
				rnd6 = Math.random() * eyeEffects.length | 0;
			}else{
				rnd6 = 0;
			}
			names = symEffects[rnd5][0] + symArms[rnd][0] + armFaces[rnd2][0] + eyeEffects[rnd6][0] + eyes[rnd3][0] + mids[rnd4] + eyes[rnd3][1] + eyeEffects[rnd6][1] + armFaces[rnd2][1] + symArms[rnd][1] + symEffects[rnd5][1];
		}else if(i < 4){
			rnd9 = Math.random() * lArms.length | 0;
			rnd10 = Math.random() * armFaces.length | 0;
			rnd11 = Math.random() * eyes.length | 0;
			rnd12 = Math.random() * mids.length | 0;
			rnd13 = Math.random() * 6 | 0;
			rnd14 = Math.random() * 8 | 0;
			if(rnd13 === 0){
				rnd15 = Math.random() * leftEffects.length | 0;
			}else{
				rnd15 = 0;
			}
			if(rnd14 === 0){
				rnd16 = Math.random() * eyeEffects.length | 0;
			}else{
				rnd16 = 0;
			}
			names = leftEffects[rnd15] + lArms[rnd9][0] + armFaces[rnd10][0] + eyeEffects[rnd16][0] + eyes[rnd11][0] + mids[rnd12] + eyes[rnd11][1] + eyeEffects[rnd16][1] + lArms[rnd9][1] + armFaces[rnd10][1];
		}else if(i < 6){
			rnd17 = Math.random() * rArms.length | 0;
			rnd18 = Math.random() * armFaces.length | 0;
			rnd19 = Math.random() * eyes.length | 0;
			rnd20 = Math.random() * mids.length | 0;
			rnd21 = Math.random() * 6 | 0;
			rnd22 = Math.random() * 8 | 0;
			if(rnd21 === 0){
				rnd23 = Math.random() * rightEffects.length | 0;
			}else{
				rnd23 = 0;
			}
			if(rnd22 === 0){
				rnd24 = Math.random() * eyeEffects.length | 0;
			}else{
				rnd24 = 0;
			}
			names = armFaces[rnd18][0] + rArms[rnd17][0] + eyeEffects[rnd24][0] + eyes[rnd19][0] + mids[rnd20] + eyes[rnd19][1] + eyeEffects[rnd24][1] + armFaces[rnd18][1] + rArms[rnd17][1] + rightEffects[rnd23];

		}else{
			rnd25 = Math.random() * faces.length | 0;
			rnd26 = Math.random() * eyes.length | 0;
			rnd27 = Math.random() * mids.length | 0;
			rnd28 = Math.random() * 8 | 0;
			rnd29 = Math.random() * 8 | 0;
			if(rnd28 === 0){
				rnd30 = Math.random() * symEffects.length | 0;
			}else{
				rnd30 = 0;
			}
			if(rnd29 === 0){
				rnd31 = Math.random() * eyeEffects.length | 0;
			}else{
				rnd31 = 0;
			}
			names = symEffects[rnd30][0] + faces[rnd25][0] + eyeEffects[rnd29][0] + eyes[rnd26][0] + mids[rnd27] + eyes[rnd26][1] + eyeEffects[rnd29][1] + faces[rnd25][1] + symEffects[rnd30][1];
		}
		br = document.createElement('br');
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
		}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
};
$(document).ready(function(){

	$("#facesL, #eyesLeft, #eyesRight, #symArmsR, #symArmsL, #rArms, #lArms, #mids, #lExtras, #rExtras, #rEffects, #lEffects, #facesR").click(function(){
		$(".fcPc").css("display", "none");
		$(this).children(".fcPc").css("display", "block");
	});
	$(".fcPc").click(function(){
		if($(this).hasClass("faceR")){
			if($(this).hasClass("selected")){
				$("#facesR > .fcPc").removeClass("selected");
				faceRight = "";
			}else{
				$("#facesR > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				faceRight = $(this).html();
			}
		}else if($(this).hasClass("faceL")){
			if($(this).hasClass("selected")){
				$("#facesL > .fcPc").removeClass("selected");
				faceLeft = "";
			}else{
				$("#facesL > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				faceLeft = $(this).html();
			}
		}else if($(this).hasClass("eyesR")){
			if($(this).hasClass("selected")){
				$("#eyesRight > .fcPc").removeClass("selected");
				eyeRight = "";
			}else{
				$("#eyesRight > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				eyeRight = $(this).html();
			}
		}else if($(this).hasClass("eyesL")){
			if($(this).hasClass("selected")){
				$("#eyesLeft > .fcPc").removeClass("selected");
				eyeLeft = "";
			}else{
				$("#eyesLeft > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				eyeLeft = $(this).html();
			}
		}else if($(this).hasClass("symArmR")){
			if($(this).hasClass("selected")){
				$("#symArmsR > .fcPc").removeClass("selected");
				armRight = "";
			}else{
				$("#symArmsR > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				armRight = $(this).html();
				armInRight = "";
			}
		}else if($(this).hasClass("symArmL")){
			if($(this).hasClass("selected")){
				$("#symArmsL > .fcPc").removeClass("selected");
				armLeft = "";
			}else{
				$("#symArmsL > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				armLeft = $(this).html();
				armInLeft = "";
			}
		}else if($(this).hasClass("rArm")){
			if($(this).hasClass("selected")){
				$("#rArms > .fcPc").removeClass("selected");
				armInRight = "";
			}else{
				$("#rArms > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				armInRight = $(this).html();
				armRight = "";
			}
		}else if ($(this).hasClass("lArm")){
			if($(this).hasClass("selected")){
				$("#lArms > .fcPc").removeClass("selected");
				armInLeft = "";
			}else{
				$("#lArms > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				armInLeft = $(this).html();
				armLeft = "";
			}
		}else if($(this).hasClass("mids")){
			if($(this).hasClass("selected")){
				$("#mids > .fcPc").removeClass("selected");
				mid = "";
			}else{
				$("#mids > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				mid = $(this).html();
			}
		}else if($(this).hasClass("extrasR")){
			if($(this).hasClass("selected")){
				$("#rExtras > .fcPc").removeClass("selected");
				extraRight = "";
			}else{
				$("#rExtras > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				extraRight = $(this).html();
			}
		}else if($(this).hasClass("extrasL")){
			if($(this).hasClass("selected")){
				$("#lExtras > .fcPc").removeClass("selected");
				extraLeft = "";
			}else{
				$("#lExtras > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				extraLeft = $(this).html();
			}
		}else if($(this).hasClass("rEffect")){
			if($(this).hasClass("selected")){
				$("#rEffects > .fcPc").removeClass("selected");
				effectRight = "";
			}else{
				$("#rEffects > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				effectRight = $(this).html();
			}
		}else if($(this).hasClass("lEffect")){
			if($(this).hasClass("selected")){
				$("#lEffects > .fcPc").removeClass("selected");
				effectLeft = "";
			}else{
				$("#lEffects > .fcPc").removeClass("selected");
				$(this).addClass("selected");
				effectLeft = $(this).html();
			}
		}
		$("#faceCons").html(effectLeft + armLeft + faceLeft + armInLeft + extraLeft + eyeLeft + mid + eyeRight + extraRight + armInRight + faceRight + armRight + effectRight);
	});
	
	$("#faceCons").click(function(){
		if (document.selection) { 
			var range = document.body.createTextRange();
			range.moveToElementText(document.getElementById("faceCons"));
			range.select().createTextRange();
			document.execCommand("Copy"); 
			window.getSelection().empty();
		} else if (window.getSelection) {
			var range = document.createRange();
			 range.selectNode(document.getElementById("faceCons"));
			 window.getSelection().addRange(range);
			 document.execCommand("Copy");
			window.getSelection().empty();
		}
		$("#copied").fadeIn(500).delay(500).fadeOut(500);
	});
});