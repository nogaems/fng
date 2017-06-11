var names1 = ["200 minute","24 hour","50 minute","Abrupt","Almighty","Ambush","Annihilation","Blessed","Blight","Blocked","Boosted","Brief","Carnage","Cataclysmic","Cleansing","Collapsing","Corrupting","Crashing","Deception","Delayed","Demolition","Dire","Directed","Disrupted","Dormant","Double","Early Morning","Eclipse","Elimination","Endless","Eradication","Eternal","Evaded","Expiration","Exploding","Extermination","Extinction","Final","Gentle","Grave","Grim Reaper","Growing","Harmless","Idle","Intended","Interrupted","Last Minute","Lazy","Life-giving","Living","Man-made","Midnight","Midsummer","Midwinter","Mighty","Necrotic","Nightmare","Nonstop","Noxious","Obliteration","Overlooked","Persistent","Positive","Predicted","Rapid","Record","Released","Relentless","Seven Day","Shock","Shrouded","Silence","Sleeping","Sudden","Supported","Surreal","Swift","Tainted","Tainting","Tenacious","Tense","Thunder","Total Destruction","Toxic","Triple","Trivial","Twilight","Twin","Unbound","Unconstrained","Unforeseen","Unlimited","Unnatural","Unstoppable","Veiled","Vicious","Void","Weak","Wreckage","Wrecking"];
var names2 = ["Hurricane","Flood","Tornado","Eruption","Avalanche","Drought","Hail Storm","Blizzard","Tsunami","Wildfire","Epidemic","Cyclone","Heat Wave","Solar Flare"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		rnd2 = Math.floor(Math.random() * names2.length);
		names = "The " + names1[rnd] + " " + names2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}