var nm1 = ["Aspect","Attunement","Aura","Blessing","Bond","Boon","Brand","Breath","Chant","Charge","Core","Crest","Crux","Curse","Emblem","Enchantment","Favor","Gift","Grace","Hymn","Infusion","Mantra","Mark","Miracle","Oath","Order","Pledge","Seal","Secrets","Seed","Spark","Symbol","Token","Tribute","Vow","Whisper","Word"];
var nm2 = ["","","","","","Advanced","Bolstered","Brilliant","Colossal","Elite","Enhanced","Eternal","Exceptional","Faultless","Fortified","Glorious","Grand","Greater","Immortal","Impeccable","Increased","Lesser","Light","Major","Mighty","Minor","Mortal","Mystic","Mythic","Potent","Prime","Reinforced","Renewed","Strengthened","Superior","Supreme","Titanic","Toughened","Vampiric","Vicious"];
var nm3 = ["the Archer","the Armageddon","the Bear","the Beast","the Berserker","the Boar","the Cataclysm","the Crane","the Crescent Moon","the Crusader","the Day","the Dragonborn","the Eagle","the Eclipse","the End","the Enigma","the Fox","the Full Moon","the Gargoyle","the Gladiator","the Hunter","the Isles","the King","the Knight","the Light","the Lion","the Mage","the Moon","the Mountain","the Night","the Oracle","the Phoenix","the Prince","the Princess","the Prisoner","the Prodigy","the Prophecy","the Prophet","the Queen","the Rising Sun","the River","the Scourge","the Seer","the Serpent","the Setting Sun","the Steward","the Sun","the Swamp","the Tiger","the Void","the Volcano","the Ward","the Warrior","the Whale","the Wolf","Absorption","Accuracy","Adaptability","Adventure","Affliction","Agility","Air","Amnesia","Angel Wings","Anger","Anguish","Animalistic Cunning","Annihilation","Anxiety","Magic","Power","Archery","Armor","Ashes","Assassination","Assassins","Assaults","Attack","Attunement","Auras","Awareness","Balance","Barriers","Battle","Beginnings","Binding","Blades","Blast Protection","Blasting","Blindness","Bliss","Blood","Bloodshed","Boulderfists","Bravery","Brawn","Brilliance","Calamities","Calmness","Camouflage","Caring","Carnage","Cat Eyes","Cataclysms","Catastrophes","Chains","Charisma","Chills","Clarity","Cloud Walking","Combat","Conjurations","Conjuring","Constitution","Conviction","Convulsion","Courage","Cover","Creation","Crushing","Crystal Barriers","Crystal Clarity","Cunning","Dancing Blades","Danger","Dangers","Dark Magic","Dark Powers","Darkness","Dawn","Defense","Defiance","Deflection","Delight","Delirium","Demolition","Demonic Eyes","Demonic Wings","Demons","Depressions","Despair","Destruction","Determination","Devotion","Dexterity","Diplomacies","Disbelief","Discipline","Diseases","Disgust","Dishonor","Dismay","Distress","Dodging","Dominance","Domination","Doom","Doubt","Dread","Dreams","Duels","Dusk","Elimination","Enchanting","Enchantments","Ends","Endurance","Executions","Expertise","Explosions","Extinction","Faith","Fear","Feather Falling","Finesse","Fire","Focus","Fog","Force","Foresight","Forging","Fortitude","Fortune","Fright","Frost","Fury","Ghostly Essences","Ghosts","Glee","Gloom","Glory","Gluttony","Grace","Greed","Grief","Guardians","Guards","Happiness","Harm","Haste","Hate","Hatred","Havoc","Healing","Health","Health Absorption","Heaven","Hell","Hellfire","Higher Spirits","Honor","Horror","Horrors","Hostility","Hot Tempers","Hunger","Hurricanes","Ice","Icewalking","Illusions","Incantations","Infinity","Insight","Intellect","Invisibility","Judgment","Killing","Kings","Laughter","Lava","Lavawalking","Life","Lifemending","Lifestealing","Light","Lightning","Limbo","Loot","Loss","Lost Souls","Love","Luck","Magic","Magic Barriers","Magical Defenses","Magma","Mana","Mana Restoration","Massacres","Mastery","Mending","Might","Miracles","Misery","Misfortune","Mist","Moonlight","Multistrike","Murder","Mutation","Mysteries","Nature","Neglect","Nightmares","Oblivion","Pain","Panic","Paradise","Parry","Patience","Peace","Pessimism","Phantoms","Phoenix Ashes","Pickpocketing","Piercing","Pleasure","Poise","Poison","Poison Resist","Potency","Potions","Power","Praise","Prayers","Precision","Preservation","Prestige","Prophecies","Protection","Recoil","Regeneration","Reincarnation","Relics","Relief","Renewal","Resilience","Respect","Restoration","Revenge","Ruins","Runes","Salvation","Sanity","Shadow Resist","Shadows","Shock","Sight","Silence","Awareness","Slaughter","Slaying","Smite","Smiting","Sneaking","Solitude","Sorcery","Soulmending","Souls","Soulstealing","Speed","Spellpower","Spells","Spirits","Spite","Stability","Stamina","Stealth","Stone","Storms","Strength","Striking","Subtlety","Success","Suffering","Summoning","Sunfire","Sunlight","Swiftness","Swordbreaking","Tears","Tenacity","Terror","Terrors","Thieves","Thorns","Thunder","Titanic Bravery","Torment","Torture","Treasures","Tributes","Trickery","Triumph","Trouble","Trust","Twilight","Understanding","Undoing","Unending Attacks","Unseen Dangers","Valiance","Valor","Vengeance","Venom","Versatility","Vigor","Visibility","Vitality","Voodoo","War","Water Walking","Weakness","Wealth","Wind","Windwalking","Wisdom","Witchcraft","Woe","Wonders","Worship"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm3.length);
		if(i < 3){
			names = nm1[rnd] + " of " + nm3[rnd2];
		}else if(i < 7){
			rnd3 = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd3] + "  " + nm1[rnd] + " of " + nm3[rnd2];
		}else{
			rnd3 = Math.floor(Math.random() * nm2.length);
			while(rnd2 < 55){
				rnd2 = Math.floor(Math.random() * nm3.length);
			}
			while(rnd3 < 5){
				rnd3 = Math.floor(Math.random() * nm2.length);
			}
			names = nm1[rnd] + " of " + nm2[rnd3] + "  " + nm3[rnd2];
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