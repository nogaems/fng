var nm1 = ["c","f","g","k","n","ph","s","th","z"];
var nm2 = ["a","e","o","a","e","o","a","e","o","i","i","u"];
var nm3 = ["d","g","h","j","n","r","s","t","y","z"];
var nm4 = ["d","f","h","l","m","n","r","v"];
var nm5 = ["Animus","Avatar","Child","Daughter","Deity","Demigos","Deus","Divinity","Dominus","Essence","Hand","Heir","Heiress","Herald","Keeper","Nobilis","Overbeing","Oversoul","Progeny","Scion","Soul"];
var nm6 = ["Adjustment","Advice","Amusement","Anger","Autumn","Awe","Balance","Battle","Birth","Blades","Blood","Brilliance","Calamity","Carnage","Chaos","Clarity","Compassion","Courage","Death","Deceit","Dedication","Delight","Desire","Despair","Destruction","Discord","Dreams","Elegance","Envy","Fascination","Fealty","Fear","Frailty","Freedom","Fury","Generosity","Grace","Grief","Hate","Hatred","Havoc","Honesty","Honor","Hope","Humility","Humor","Insanity","Intelligence","Justice","Knowledge","Laughter","Liberty","Life","Loss","Loyalty","Luck","Memories","Might","Misery","Omens","Pain","Perseverance","Piety","Power","Pride","Prophecies","Redemption","Revenge","Sanity","Shadows","Slaughter","Solitude","Sorrow","Spring","Strength","Summer","Thrills","Tolerance","Tranquility","Truth","Uncertainty","Vengeance","Victory","Wealth","Will","Winter","Wisdom","Wit","Woe","Wrath","the Mighty","the Resolute","the Stout"];
var nm7 = ["Abandoned","Aethereal","Aggravating","Ancient","Anguished","Animated","Arrogant","Austere","Bitter","Blind","Bright","Brilliant","Broken","Careless","Colossal","Condemned","Corrupt","Crooked","Cruel","Defiant","Delirious","Deserted","Devoted","Diligent","Dismal","Divine","Doubtless","Ebon","Elated","Elegant","Exalted","False","Fearless","Fell","Fickle","Flawless","Forlorn","Forsaken","Funereal","Glorious","Golden","Gracious","Grand","Greedy","Grim","Guilty","Hallowed","Harmonious","Heedless","Hidden","Hollow","Humble","Hungering","Hungry","Illustrious","Impure","Infernal","Jaded","Living","Lone","Lonely","Luminate","Misguided","Molten","Nameless","Obsidian","Prime","Pristine","Pure","Reckless","Revered","Sanguine","Scornful","Selfish","Sepulchral","Serene","Shameless","Silent","Swift","Timeless","Torn","Transcendent","Truthful","Twin","Unbreakable","Undefeated","Unseen","Unwielding","Venerated","Vengeful","Vigilant","Warped","Wicked","Wise","Wrathful","Wretched"];
var nm8 = ["Animus","Avatar","Champion","Deity","Demigod","Deus","Dominus","God","Herald","Incarnation","Keeper","One","Primordial","Scion","Shadow","Shepherd","Soul","Spiritkeeper"];

var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 6){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			rnd3 = Math.floor(Math.random() * nm3.length);
			rnd4 = Math.floor(Math.random() * nm2.length);
			rnd6 = Math.floor(Math.random() * nm5.length);
			rnd7 = Math.floor(Math.random() * nm6.length);
			if(i < 3){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + ", " + nm5[rnd6] + " of " + nm6[rnd7];
			}else{
				rnd8 = Math.floor(Math.random() * nm4.length);
				rnd9 = Math.floor(Math.random() * nm2.length);
				while(nm4[rnd8] === nm3[rnd3]){
					rnd8 = Math.floor(Math.random() * nm4.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd8] + nm2[rnd9] + ", " + nm5[rnd6] + " of " + nm6[rnd7];
			}
		}else if(i < 8){
			rnd = Math.floor(Math.random() * nm5.length);
			rnd2 = Math.floor(Math.random() * nm6.length);
			names = nm5[rnd] + " of " + nm6[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm7.length);
			rnd2 = Math.floor(Math.random() * nm8.length);
			names = nm7[rnd] + " " + nm8[rnd2];
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