var names1 = ["Abandoned","Aberration","Abnormality","Abomination","Acid","Acidic","Acrid","Amnesia","Anomaly","Armageddon","Asylum","Babylon","Black Ashes","Black Dust","Black Earth","Black Moon","Black Rain","Black Sun","Blessed","Burning World","Cataclysm","Chaos","Cockroach","Decimation","Desolate","Deviant","Dominance","Eclipse","Ember","Enigma","Eternal","Eternal Darkness","Eternal Eclipse","Eternal Fire","Eternal Void","Evolution","Extinction","Fallen Star","Fallout","False Prophet","Forsaken","Found Fortune","Gifts of Mutation","Godless","Honor","Honorbound","Human Expiration","Human Extinction","Human Hunter","Isolation","Law Abiding","Lawless","Legion","Limbo","Lost Soul","Martial Law","Metamorphosis","Miracle","Misery","Monster","Monster Hunter","Mutant","Mutant Hunter","Myriad","Neo-Human","New Friends","New God","New Haven","New Hope","New Law","New Monster","New Moon","New Prophet","New Start","New Sun","New Supremacy","New World","No Legacy","Nuclear","Oath","Oblivion","Old Ruins","Orphan","Our Legacy","Outcast","Paragon","Phoenix","Prodigy","Rebirth","Red Moon","Red Sun","Reincarnation","Resurrection","Revelation","Risen Ashes","Sanctuary","Survivor","Total Eclipse","Traitor","Warhead"];
var names2 = ["Alliance","Association","Brotherhood","Clan","Coalition","Confederacy","Cooperative","Federation","Gang","League","Order","Republic","Syndicate","Tribe","Nation","Union"];
var names3 = ["Abandoned","Aberrations","Abnormalities","Invincible","Abominations","Anomalies","Armageddons","Asylum","Babylonians","Black Ashes","Blessed","Chosen Ones","Cleansed","Cockroaches","Dead","Defiance","Deviants","Droplets","Enigmas","Eternals","Evolved","Expired","Extinct","Fallen","Flock","Forsaken","Freaks","Giants","Gifted","Godless","Hermits","Hidden","Homeless","Honorbound","Honorless","Horned Ones","Immune","Impure","Infected","Invisible","Law","Lawless","Legion","Living","Lost Ones","Lost Souls","Miracles","Monsters","Mutants","Myriad","Neo-Human","New Friends","New Humans","New Monsters","Newmans","Orphans","Outcasts","Paragons","Phantoms","Phoenixes","Prodigies","Pure","Purified","Rats","Reincarnated","Resurrected","Risen","Roaches","Salvation","Shadows","Stalkers","Survivors","Tails","Tormented","Vanished","Walkers","Warheads","White Ashes"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 5){
			rnd = Math.floor(Math.random() * names1.length);
			rnd1 = Math.floor(Math.random() * names2.length);
			names = names1[rnd] + " " + names2[rnd1];
		}else{
			rnd = Math.floor(Math.random() * names3.length);
			names = "The " + names3[rnd];
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