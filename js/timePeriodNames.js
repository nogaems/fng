var nm1 = ["Accord","Agency","Alchemy","Alliance","Ambitious","Anarchy","Ancestral","Android","Apocalypse","Arcane","Atomic","Aura","Aurora","Battle","Beauty","Bionic","Blissful","Bloodshed","Bloody","Blooming","Blossom","Carnage","Celestial","Civil","Clone","Collapsing","Collision","Colonial","Combat","Confusion","Conjured","Counterfeit","Covert","Crystal","Darkness","Deception","Delusion","Design","Destiny","Destruction","Diamond","Disabled","Discovery","Disinformation","Divine","Doom","Dread","Dream","Ecstasy","Electric","Elimination","Enlightened","Enmity","Eradication","Eternal","Euphoria","Evolution","Exalted","Exhausted","Exotic","Exploration","Extinction","Extraterrestrial","Extreme","Fable","Failure","False","Forgotten","Fright","Frozen","Fury","Fusion","Gadget","Glamor","Glass","Gleeful","Glory","Grandiose","Happy","Harmony","Havoc","Herculean","Hero","High","Holy","Honest","Horror","Idealist","Identity","Imagination","Infinity","Information","Intimidation","Invention","Isolation","Judgment","Karma","Limitless","Lost","Machine","Magic","Malignant","Martial","Massacre","Mechanical","Medical","Memorial","Metaphysical","Migration","Molten","Multicultural","Mutation","Mystery","Mystic","Mythical","Nationalistic","Nature","Noble","Nuclear","Nurture","Obliteration","Occult","Other","Panic","Paradise","Paragon","Paranormal","Peaceful","Perfection","Perversion","Phantom","Pinnacle","Plastic","Poison","Primal","Prime","Pristine","Private","Progress","Prophecy","Prophetic","Protection","Putrid","Radical","Rage","Rapture","Rebirth","Regal","Regression","Relic","Revelation","Revolution","Romantic","Ruin","Rune","Sacred","Scientific","Secrecy","Secret","Separation","Shadow","Shattered","Silent","Slaughter","Sleeping","Social","Solidarity","Solitude","Sorcery","Space","Spirit","Stealth","Strive","Struggle","Superhuman","Suppression","Supreme","Surrender","Synthetic","Tender","Terraforming","Territorial","Terror","Timeless","Titan","Toxic","Trepidation","Truce","Uncanny","Unity","Utopian","Venom","Visionary","Vitality","Voodoo","Warfare","Widget","Witchcraft","Wood","Wreckage","Youth"];
var nm2 = ["Abundances","Advancement","Alterations","Amendments","Ancestors","Ancients","Annihilation","Ascension","Ashes","Attraction","Barbarians","Battle","Beauty","Bionics","Blessings","Blood","Bones","Brilliance","Brutes","Carnage","Change","Chaos","Clones","Combat","Confusion","Control","Correction","Creation","Cruelty","Cultivation","Darkness","Death","Deception","Deities","Demise","Destinies","Deterioration","Development","Disaster","Discipline","Discoveries","Divination","Divines","Doom","Downfalls","Dread","Dreams","Duplicates","Duplicity","Dust","Electricity","Enchantment","Enhancement","Enlightenment","Eradication","Euphoria","Evolution","Existence","Extinction","Failure","Fortune","Foundations","Fraudulence","Freedom","Fright","Frost","Fury","Gadgets","Ghosts","Glamor","Glass","Glory","Gods","Grandeur","Growth","Guidance","Guile","Harmony","Havoc","Health","Heroes","Honesty","Hypocrisy","Illusions","Immortality","Indifference","Indulgence","Injury","Insignificance","Intimidation","Inventions","Isolation","Karma","Kindness","Liberty","Life","Loss","Machines","Magic","Magnificence","Marvels","Massacres","Medicines","Might","Migration","Miracles","Misfortune","Mortality","Mutations","Mythics","Myths","Nature","Neglect","No Return","Nobility","Nothingness","Oblivion","Opulence","Originations","Origins","Oversight","Panic","Peace","Penance","Perdition","Perversion","Phantoms","Phenomenons","Plenty","Poison","Pretense","Progress","Prophecies","Protection","Punishment","Radicals","Rage","Raptures","Rebirth","Recovery","Reformation","Regeneration","Regulations","Release","Renovation","Repetition","Retribution","Revelations","Revisal","Revision","Revolutions","Romance","Rubble","Ruins","Sacrifice","Savagery","Scapegoats","Science","Secrecy","Secrets","Seduction","Silence","Sincerity","Slaughter","Solitude","Souls","Space","Spells","Spirits","Splendor","Spoils","Stagnation","Stealth","Storms","Strive","Struggle","Subjection","Success","Suffering","Suppression","Surprises","Temptation","Terror","Titans","Torture","Tragedy","Treachery","Trials","Trickery","Triumph","Trust","Turbulence","Turmoil","Unities","Utopia","Venom","Victims","Violence","Warfare","Waste","Whitewashing","Witchcraft","Wonder"];
var nm3 = ["Age","Era","Aeon","Ages"];
var br = "";

function nameGen(type){
	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm3.length);
		if(i < 5){
			rnd = Math.floor(Math.random() * nm1.length);
			names = "The " + nm1[rnd] + " " + nm3[rnd2];
		}else{
			rnd = Math.floor(Math.random() * nm2.length);
			names = "The " + nm3[rnd2] + " of " + nm2[rnd];
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