
function nameGen(type){
	var nm1 = ["Aberrant","Absurd","Acrobatic","Adamant","Adapting","Advanced","Advancing","Aged","Aggressive","Agile","Altering","Anchored","Ancient","Angelic","Angler","Animal","Aquatic","Awoken","Barbarian","Barraging","Battle","Berserker","Besieging","Blade","Blazing","Blind","Blinding","Blond","Blood","Bone","Bony","Boosting","Brass","Brawling","Building","Burning","Burrowing","Cackling","Careless","Chain","Champion","Chaos","Charging","Chuckling","Clawing","Clever","Climbing","Commanding","Conquering","Crawling","Crazy","Creature","Crooked","Cruel","Crying","Dancing","Darkness","Dashing","Defiant","Delirious","Destroyer","Dimpled","Disappearing","Dodging","Dread","Dribbling","Drunk","Earthquake","Echoing","Elderly","Elite","Enormous","Enraged","Evading","Excited","Feigning","Feline","Fierce","Fire","Flailing","Flame","Frog","Frogleap","Fuming","Furry","Fuzzy","Game","Gargantuan","Ghost","Gigantic","Giggling","Golden","Grappling","Grim","Grimacing","Grinning","Grotesque","Growling","Guardian","Hammer","Hardening","Head-Butting","Heavy","Herald","Hideous","Hiding","Hissing","Hook","Horror","Howling","Igniting","Infernal","Inhaling","Intelligent","Iron","Junior","Juvenile","Lanky","Laughing","Leader","Leading","Learning","Light","Lightning","Luminous","Lunging","Marked","Masked","Massive","Mentor","Metal","Mimic","Miming","Miniature","Monkey","Mumbling","Night","Nightmare","Nimble","Nocturnal","Omen","Parroting","Patrolling","Phantom","Pouncing","Prime","Protecting","Prowling","Punishing","Quick","Rabid","Raging","Rain","Rainstorm","Rapid","Resting","Roaring","Roasting","Rummaging","Running","Rushing","Shepherd","Shield","Shielded","Shielding","Shrieking","Silver","Sizzling","Skeletal","Slinging","Slingshot","Smoking","Smouldering","Sneaking","Speedy","Sprinting","Squealing","Stalking","Staring","Storm","Strange","Swift","Tackling","Thinking","Thundering","Tracing","Tracking","Trained","Trap","Trapping","Tremor","Vengeful","Vicious","Volatile","Volcano","Vomitting","Whistling","Wicked","Winking","Wise"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		names = nm1[rnd] + " Titan";
		nm1.splice(rnd, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}