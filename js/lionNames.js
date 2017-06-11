var nm1 = ["Ajax","Alfie","Anger","Artemis","Aslan","Astro","Axe","Bale","Bandit","Bane","Bazal","Begal","Bengo","Biscuit","Bleach","Blitz","Bones","Boots","Brownie","Bruno","Brutus","Bubba","Bubble","Buster","Butters","Catastrophe","Chance","Chase","Chester","Chewy","Chili","Clawde","Cloud","Cosmo","Cotton","Cuddles","Dash","Domino","Dova","Duke","Dusty","Echo","Fang","Fetch","Fire","Flynn","Frisky","Fury","Fyre","Ghost","Giggles","Gnaw","Grinch","Hannibal","Haze","Hector","Hooch","Indi","Jag","Khan","Kimba","Lash","Lecter","Leo","Leon","Licorice","Lightning","Lionel","Loki","Lycan","Marble","Maw","Max","Mello","Midnight","Miles","Mittens","Muffin","Nemesis","Nibble","Nibbler","Nightmare","Nightshade","Nine","Nocturn","Nova","Nugget","Onyx","Patch","Pax","Peanut","Pebble","Perseus","Phantom","Pounce","Pouncer","Puff","Pyre","Quicksilver","Rage","Raja","Rambo","Ranger","Rawr","Reaper","Render","Rock","Rocky","Scar","Scratches","Shadow","Shiv","Shrapnel","Shredder","Silver","Skip","Skittles","Skye","Sly","Smiles","Smokey","Snickers","Snow","Snowball","Snowflake","Snuggle","Sparks","Spike","Spot","Stalker","Stitch","Storm","Strike","Striker","Stripe","Stripes","Swipes","Thunder","Tickles","Tiny","Tooth","Truffle","Tygar","Tyson","Victor","Whiskers","Woods","Wrath"];
var nm2 = ["Aggy","Alexi","Amber","Anger","Ashelia","Aslana","Athena","Azure","Babe","Bambino","Beauty","Belle","Biscuit","Blitze","Boots","Brownie","Bubbles","Buttercup","Cara","Cato","Chance","Cinnamon","Clawdia","Cloe","Coco","Cookie","Cosmo","Cotton","Crystal","Cupcake","Daisy","Dash","Dawn","Delilah","Dot","Dottie","Dutchess","Echo","Enigma","Enya","Eve","Faith","Fawn","Flame","Giggles","Ginny","Grace","Harley","Haze","Hazel","Hope","Huntress","Iris","Jade","Jasmine","Jinx","June","Jynx","Kara","Karma","Kat","Kate","Kathy","Kisses","Kitty","Lilly","Lola","Lucy","Lullaby","Luna","Lyla","Mae","Mango","Maya","Mello","Mila","Misty","Mocha","Muffin","Myst","Mystique","Nala","Neko","Nemo","Nibble","Nibbles","Nipsey","Nora","Nugget","Nutmeg","Oracle","Patches","Paws","Peaches","Pebble","Pebbles","Pepper","Phantom","Pickles","Precious","Princess","Puff","Roxy","Ruby","Sabrina","Sage","Sandy","Sapphire","Scratches","Selena","Serenity","Shade","Shadow","Shiba","Shinx","Smooch","Smudges","Snow","Snowball","Snowflake","Snuggles","Song","Sphinx","Spot","Stripes","Sugar","Summer","Sundance","Sweetie","Tickles","Tigress","Tiny","Toots","Trixie","Truffles","Twilight","Twinkle","Umbreon","Violet","Waffles","Whiskers","Whisper","Wiggles","Willow","Winter"];
var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd];
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