var names1 = ["Abdication","Abuse","Amalgamation","Ambitions","Anarchy","Angels","Ashes","Assassinations","Autarchy","Autonomy","Awakening","Backdoors","Backstabs","Betrayal","Blackmail","Blessings","Bliss","Blood","Bloodshed","Blunders","Bowing","Broken Armies","Broken Souls","Brutalities","Burning Flags","Carnage","Certain Demise","Certain Doom","Charity","Clean Hands","Cleansing Rains","Coalitions","Comraes","Condemnation","Control","Corruption","Covert Affairs","Cowards","Crooks","Damnation","Darkness","Death","Deaths","Deceit","Deception","Defamation","Delusion","Demands","Democracy","Denial","Desire","Destruction","Devotion","Dilemmas","Disgrace","Disguises","Dishonor","Disloyalty","Disorder","Disruption","Disunion","Domination","Duality","Duplicity","Duty","Eradication","Essence","Evaded War","Executions","Exiles","Expansion","Extermination","Extortion","Faith","Favor","Flying Colors","Fortune","Fraud","Freedom","Fusions","Gluttony","Greed","Growth","Guilt","Harmony","Heart","Heaven","Hidden Goals","Hoaxes","Honesty","Honor","Hope","Humiliation","Humility","Hypocrisy","Ignorance","Illusions","Impostors","Independence","Individuality","Innocent Victims","Innocents","Integrity","Intelligence","Interruption","Justice","Kindness","Law","Legitimacy","Liberty","Lies","Life","Loyalty","Luxury","Magic","Malignance","Martial Law","Mergers","Miracles","Mistakes","Mysteries","Mystics","Necrosis","Neglect","New Hope","Nothing","Obedience","Obscurity","Oppression","Oversights","Passivism","Patriots","Perfection","Persecution","Pressure","Privacy","Promises","Promotions","Prosperity","Protection","Public Order","Public Unrest","Purity","Rebirth","Recovery","Reincarnation","Rejuvenation","Reparation","Resignation","Respect","Restoration","Resurgence","Revelations","Revival","Riches","Righteousness","Sanctification","Sanctions","Scams","Scarred Lands","Secrets","Security","Separation","Severance","Shams","Shrouded Lies","Shrouded Truths","Silence","Slander","Slavery","Slaves","Solutions","Sovereignty","Stagnation","Submission","Subterfuge","Support","Surrender","Survival","Terminality","The Bastard","The Brotherhood","The Burning City","The Curse","The Dictator","The False King","The Forest","The Forsaken","The Greater Good","The Grim Reaper","The Impasse","The Iron Hand","The Lands","The Light","The Massacre","The Meek","The Mountains","The Occult","The Oracle","The Pure","The Silver Angel","The Trojan Horse","The True King","Theft","Thieves","Torment","Torture","Traitors","Treachery","Triumph","Truth","Unanimity","Unification","Unions","Unison","Utopia","Vetos","Victims","Victory","Vigor","Virtues","Vitality","Wealth","Wellfare","Wonder"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
			rnd = Math.floor(Math.random() * names1.length);
			names = "Treaty of " + names1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}