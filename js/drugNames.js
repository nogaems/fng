var nm1 = ["After Burner","Ammo","Angel","Anvil","Aqua","Arachnid","Ash","Barb","Blaze","Nitro","Cookie Dough","Sugar","Flour","Paste","Blitz","Haunt","Blue","Bonedust","Boogie","Boom","Bronze","Buffoon","Burnout","Buster","Cactus","Caine","Catnip","Change","Chaos","Chocolate","Chopsticks","Chow","Chrono","Claw","Coco","Comet","Crimson","Crisps","Crocodile Tears","Crow","Crush","Crypt","Daydream","Deluge","Devil's Tongue","Dew","Diamond","Doom","Dragon","Dragontail","Droplet","Dwarf","Dyno","Echo","Ecto","Enigma","Epiphany","Ether","Fairy Tale","Fate","Feather","Fizz","Fizzy Drink","Flare","Flashbang","Flinch","Fluff","Fluke","Frenzy","Frost","Fury","Gadgets","Galaxy","Gloom","Glory","Glue","Grave Dust","Green","Grunt","Hoarse","Hog","Honey","Hood","Howler","Hush","Icicles","Impact","Jade","Jetlag","Jiggy","Juice","Knockout","Lag","Leaves","Leech","Liftoff","Light Speed","Lightyear","Lizard","Luna","Lupus","Lyrics","Mane","Marbles","Mask","Merch","Miracle","Mirage","Mist","Mistress","Mithril","Moisturizer","Moon Rocks","Morbid","Morph","Mud","Musk","Muze","Myth","Nails","Necro","Nether","Nibble","Nova","Nuggets","Nuts","Onyx","Oracle","Orb","Ozone","Ozz","Phoenix","Pipes","Pixel","Powder","Quills","Rabbit's Foot","Rainbow","Rampage","Raptor","Reaper","Red","Rock Salt","Roots","Roth","Ruby","Runes","Sanguine","Sapphire","Serenity","Silver","Slush","Smut","Snowflake","Soil","Songbird","Soot","Spice","Spirit","Stake","Steel","Storm","Stripes","Sugar Cane","Sunburn","Supernova","Tails","Taint","Talon","Tears","Tease","Thimble","Third Eye","Thorn","Thunder","Titanium","Tombstone","Tranquil","Trinity","Twin","Twinkle","Twist","Twister","Typhoon","Vacuum","Vamp","Vampire Dust","Vanilla","Vapor","Venom","Vibe","Vintage","Visage","Void","Warp","Waves","Wax","Whiskers","Whisper","Wish","Wizard","Wolf","Wrath","Wrathhog","Wyvern","Xp"];
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