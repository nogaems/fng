var nm1 = ["","","","","","b","br","d","g","h","j","k","l","m","n","r","s","t"];
var nm2 = ["a","e","i","o","u","a","e","a","e","i","a","e","i","o","u","a","e","a","e","i","a","e","i","o","u","a","e","a","e","i","au","ia","ie","io","aa"];
var nm3 = ["br","c","dr","g","k","kr","kn","l","ll","ln","lm","m","my","n","nv","ny","r","rr","s","v","y","z"];
var nm4 = ["c","l","ll","m","n","nr","ndr","r","rd","rn","rl","s","ss","sn","t","th","z"];
var nm5 = ["","","","","","","","h","l","n"];
var nm6 = ["Angel","Cerberus","Champion","Curator","Guardian","Herald","Keeper","Magister","Reaper","Sentinel","Seraph","Shepherd","Shield","Voice"];
var nm7 = ["All","Authority","Balance","Battle","Blood","Bones","Carnage","Chains","Chance","Change","Dawn","Death","Deliverance","Desire","Despair","Destruction","Discovery","Dread","Dusk","Duty","Existence","Finality","Fury","Grace","Guidance","Harmony","Health","Invention","Iron","Jubilation","Justice","Knowledge","Law","Light","Memories","Mercy","Pleasure","Power","Punishment","Purpose","Regret","Reason","Renewal","Retribution","Scales","Serenity","Servitude","Shades","Shadows","Silence","Silver","Smoke","Solitude","Sustenance","Thrills","Time","Twilight","War","Wealth","Worth","Wrath","the Blade","the Crown","the Feast","the Flame","the Flock","the Inferno","the Light","the Masses","the Morning","the Nether","the Provinces","the Realm","the Shield","the Sword","the Wild"];
var nm8 = ["Adept","Aged","Agile","Ancient","Austere","Battle","Belated","Bitter","Blood","Bone","Brilliant","Careless","Chain","Colossal","Cruel","Deathless","Defiant","Delirious","Deserted","Desire","Desolation","Devoted","Diligent","Dread","Elegant","Emancipation","Enormous","Enraged","Exalted","Fallen","Flame","Flawless","Forsaken","Gargantuan","Giant","Gleaming","Glorious","Golden","Graceful","Gracious","Grand","Grim","Guardian","Harmonious","Hidden","Hollow","Illustrious","Impure","Infernal","Infinite","Juvenile","Light","Livid","Lone","Lonely","Luminous","Lustrous","Magnificent","Majestic","Merciless","Mindless","Monstrous","Mysterious","Prime","Radiant","Serene","Shady","Silent","Silver","Skeletal","Storm","Twilight","Twin","Unknown","Vengeful","Vigilant","Violent","Watchful","Whirlwind","Wicked","Wrathful","Wretched"];
var nm9 = ["Angel","Cerberus","Champion","Curator","Guardian","Herald","Keeper","Reaper","Sentinel","Seraph"];

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
			rnd5 = Math.floor(Math.random() * nm5.length);
			rnd6 = Math.floor(Math.random() * nm6.length);
			rnd7 = Math.floor(Math.random() * nm7.length);
			if(i < 3){
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm5[rnd5] + ", " + nm6[rnd6] + " of " + nm7[rnd7];
			}else{
				rnd8 = Math.floor(Math.random() * nm4.length);
				rnd9 = Math.floor(Math.random() * nm2.length);
				while(nm4[rnd8] === nm3[rnd3]){
					rnd8 = Math.floor(Math.random() * nm4.length);
				}
				names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd8] + nm2[rnd9] + nm5[rnd5] + ", " + nm6[rnd6] + " of " + nm7[rnd7];
			}
		}else if(i < 8){
			rnd = Math.floor(Math.random() * nm6.length);
			rnd2 = Math.floor(Math.random() * nm7.length);
			names = nm6[rnd] + " of " + nm7[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm8.length);
			rnd2 = Math.floor(Math.random() * nm9.length);
			names = nm8[rnd] + " " + nm9[rnd2];
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