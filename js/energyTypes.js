var nm1 = ["Adrenaline","Ancestral Energy","Ancestral Spirit","Ancient Power","Angelic Power","Animus","Arcane","Arch Energy","Ardor","Artifacts","Aspect","Astral Power","Aura","Beastly Power","Blood","Blood Energy","Bloodlust","Carnal Energy","Celestial Energy","Chakra","Chaos Energy","Chi","Chrono Power","Corruption","Courage","Crystal Power","Death","Demonic Aura","Demonic Power","Devotion","Diabolic Energy","Divine Grace","Divinity","Draconic Power","Druidic Energy","Electricity","Elemental Energy","Elemental Power","Empyrean Power","Endurance","Energy","Essence","Excitement","Fealty","Fell Energy","Feral Energy","Fire","Fire Power","Flux","Focus","Fortitude","Fragment Power","Frenzy","Frost Power","Furor","Fury","Fusion Power","Ghost Energy","Glory","Godly Power","Grace","Grave Energy","Grim Energy","Guardian Spirit","Hallowed Energy","Heat","Heirlooms","Higher Power","Holy Might","Hunger","Immortal Power","Immunity","Impurity","Incorporeal Energy","Infinity Energy","Initiative","Innocence","Juice","Life Force","Lifeblood","Lifeforce","Love","Lunar Energy","Magnetism","Mana","Mastery","Memory","Metamorphosis","Might","Mindpower","Mojo","Momentum","Mutation","Mystery Power","Nether Energy","Occult Energy","Paragon Power","Phase Power","Plague Energy","Potency","Pressure","Primal Power","Prime Power","Primeval Power","Purity","Rage","Relic Energy","Resistance","Righteousness","Rush","Sacred Energy","Sacred Power","Satanic Power","Sanctity","Sanity","Savagery","Scraps","Seraphic Energy","Serpentine Power","Shadow Energy","Solar Energy","Soul Energy","Soul Pressure","Souls","Spirit","Spirit Energy","Spiritual Focus","Spiritual Power","Sprites","Stamina","Star Power","Starpower","Steam","Stellar Power","Stress","Strength","Stress","Surge","Synthesis","Terror","Thirst","Thunder","Timeless Power","Timelost Power","Token","Torment","Totemic Power","Transfiguration","Tribal Energy","Twisted Energy","Unholy Might","Ursine Power","Vigor","Virility","Virtue","Vitality","Void Energy","Warpower","Wicked Energy","Will","Willpower","Wrath","Yin Yang","Zeal","Zen"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}