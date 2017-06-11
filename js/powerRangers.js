
var br = "";

function nameGen(){
	var nm1 = ["Action","Ancient","Angel","Angelic","Animal","Animorph","Aqua","Arachnid","Arch","Arctic","Aspect","Balance","Battle","Beast","Beastly","Berserker","Brass","Canine","Chain","Challenger","Champion","Chaos","Chemical","Chrono","Cloud","Corrupted","Corruption","Courage","Covert","Crown","Cryo","Dark","Diamond","Digital","Division","Dream","Dual","Dynamic","Electric","Elite","Enchanted","Ethereal","Fearless","Feline","Force","Former","Forsaken","Freedom","Future","Ghost","Giant","Glorious","Grand","Grave","Great","Grim","Hidden","Hollow","Honorable","Ice","Infernal","Infinite","Infinity","Invincible","Jewel","Junior","Justice","Juvenile","Liberty","Lizard","Lone","Mad","Magic","Majestic","Mammoth","Masked","Metal","Meteor","Midnight","Mighty","Mini","Monster","Monstrous","Mysterious","Mystery","Mythic","Mythical","Night","Nightmare","Nova","Obsidian","Peace","Phantom","Poison","Prime","Pyro","Radiant","Radical","Rebel","Reckless","Redemption","Secret","Serpent","Shadow","Silent","Snow","Spirit","Storm","Supernova","Thunder","True","Twin","Ultimate","Ultra","Unsung","Vagabond","Venom","Wicked","Wild","Winged"];
	var nm2 = ["Ancient","Angel","Aqua","Arachnid","Arch","Arctic","Battle","Beast","Beastly","Berserk","Blind","Boulder","Canine","Chain","Chaos","Covert","Dark","Death","Dino","Dragon","Dread","Dream","Dual","Extreme","Fearless","Feline","Fierce","Fire","Flame","Flawless","Free","Freedom","Ghost","Golden","Grand","Grave","Great","Grim","Heavy","Hidden","High","Hollow","Ice","Infinite","Iron","Joint","Jungle","Liberty","Life","Light","Livid","Lunar","Mad","Mass","Metal","Mighty","Monster","Moon","Mystery","Mythic","Night","Nightmare","Ninja","Omen","Phantom","Phase","Phoenix","Poison","Primal","Prime","Radiant","Reckless","Rush","Secret","Serpent","Serpentine","Shadow","Silent","Silver","Smoke","Snow","Solar","Stark","Stone","Storm","Sun","Surprise","Swift","Terror","Time","Turbo","Twin","Ultra","Venom","Virus","Void","Water","Wild","World"];
	var nm3 = ["Aspect","Charge","Crew","Edge","Force","Fury","Heart","Mark","Mask","Path","Point","Power","Rush","Spark","Spirit","Steel","Strike","Wrath"];

	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.random() * nm1.length | 0;
			names = nm1[rnd] + " Rangers";
			nm1.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm2.length | 0;
			rnd2 = Math.random() * nm3.length | 0;
			names = nm2[rnd] + " " + nm3[rnd2] + " Rangers";
			nm2.splice(rnd, 1);
			nm3.splice(rnd2, 1);
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