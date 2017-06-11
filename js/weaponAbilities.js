var nm1 = ["Absolving","Ambush","Ancestral","Annihilation","Beastly","Behemoth","Betrayal","Blackout","Blazing","Bleeding","Blessed","Blind","Blinding","Blocking","Branding","Brutal","Burning","Burst","Carving","Cataclysmic","Chain","Cleaving","Colossal","Combo","Combustion","Commanding","Confusion","Corrosive","Corrupting","Corruption","Counter","Crackling","Crippling","Critical","Cruel","Crumbling","Cunning","Darkness","Dazzling","Defiled","Defiling","Demon","Destruction","Detonation","Disabling","Dishonor","Dismembering","Disrupting","Disruption","Dissecting","Dissection","Distracting","Divided","Divine","Division","Dizzying","Doom","Elusive","Enveloping","Eternal","False","Fatal","Fire","Fissure","Flame","Focusing","Fracture","Freezing","Frenzied","Frenzy","Fury","Gloom","Gore","Grave","Hemorrhaging","Holy","Honor","Howling","Hungering","Igniting","Ignition","Immobilizing","Immortal","Incinerating","Incineration","Infinity","Insanity","Interrupting","Judgment","Justice","Karma","Knockout","Lacerating","Lava","Legacy","Lightning","Mad","Mammoth","Melting","Mighty","Mirror","Molten","Mortal","Mutilation","Needle","Nimble","Overpowering","Paralyzing","Perforating","Perforation","Perpetual","Phantom","Piercing","Poison","Power","Primal","Provoking","Puncturing","Purging","Rampage","Reckless","Relentless","Righteous","Rogue","Rupturing","Ruthless","Sacrificial","Savage","Searing","Shadow","Shattering","Shocking","Shrouded","Singing","Sinister","Sliding","Smoldering","Splinter","Stealth","Stinging","Subtle","Summoning","Sundering","Sweeping","Terminal","Thunder","Titan","Titanic","Trance","Trick","Turbulent","Twin","Ultimatum","Unholy","Vampiric","Vanishing","Venom","Vital","Volley","Whirling","Whirlwind","Whispering","Wild"];
var nm2 = ["Strike","Shot","Burst","Crash","Force","Thrust","Bash","Slash","Slice","Gash","Rip","Smash","Blow","Slam","Cleave","Strikes","Strike","Strike","Shot"];
var nm3 = ["Absolve","Ambush","Amputate","Annihilation","Backbite","Backstab","Bait","Barrage","Battery","Betrayal","Bite","Blackout","Blockade","Bloodlust","Bombardment","Bone Crusher","Bonedust","Brand","Brutality","Bunker Buster","Burst","Calamity","Carve","Cauterize","Char","Cheat","Chomp","Chop","Chopchop","Cleave","Clobber","Cloud Burst","Combo Breaker","Combust","Conflagrate","Corrupt","Crack","Crackle","Cripple","Cruelty","Crumble","Crunch","Dance","Dark Descent","Decapitate","Decoy","Defiance","Defile","Destruction","Detonate","Devastate","Disable","Disassemble","Disjoin","Dismember","Disperse","Disrupt","Dissect","Dissever","Dissolve","Distract","Divide","Divine Division","Double-Cross","Eclipse","Energize","Energy Drain","Entangle","Envenom","Evaporate","Eviscerate","Execute","Exorcism","Fade","Feint","Ferocity","Fissure","Flare","Flurry","Fracture","Fragment","Freeze","Frenzy","Fury","Garrote","Gash","Gore","Gouge","Hamstring","Hemorrhage","Howl","Hunger","Ignite","Immobilize","Impale","Incinerate","Interruption","Jab","Jitter","Knockout","Lacerate","Lash","Life Drain","Lightning Flash","Lightspeed","Liquefy","Maim","Mangle","Melt","Mince","Mind Disrupt","Mortify","Muster","Mutilate","Myriad","Needle Rain","Nova","Overload","Overpower","Paralyze","Perforate","Pierce","Plunge","Pummel","Puncture","Purge","Rampage","Ravish","Reap","Rebuke","Rend","Riposte","Rive","Roar","Rupture","Savagery","Seize","Sever","Shatter","Shiv","Shiver","Shock","Shove","Shriek","Skewer","Skiver","Slice 'n Dice","Slide","Smash","Smother","Snap","Snapshot","Snare","Soul Drain","Spite","Splinter","Split","Split Second","Sting","Sully","Summon","Sunder","Surge","Sweep","Tear","Tempest","Terminus","Titan's Favor","Trance","Turbulence","Unleash","Vanish","Wail","Warstrike","Weaken","Weaken Mind","Whip","Whirlwind","Wither","Wrath"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i <  5){
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm1[rnd] + " " + nm2[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm3.length);
			names = nm3[rnd];
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