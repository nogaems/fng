function nameGen(){
	var names1 = ["Ale","Brandy","Tea","Tea","Sherry","Brew","Cappuchino","Cider","Coffee","Cognac","Dark Ale","Dark Beer","Drink","Espresso","Gin","Java","Lager","Light Ale","Light Beer","Mead","Mocha","Red Wine","Rum","Sake","Tea","Tonic","Vodka","Whiskey","White Wine","Wine","Almond","Amazing","Ancient","Angel","Angelic","Apple","Apricot","Arctic","Aromatic","Autumn","Avocado","Balanced","Banana","Basil","Bay Leaf","Beautiful","Beetroot","Black","Blue","Blueberry","Boiled","Brilliant","Brown","Brutal","Burning","Calm","Capital","Caramel","Catnip","Cherry","Cherry Blossom","Chestnut","Chilled","Chilli","Cinnamon","Clouded","Cloudy","Coconut","Cool","Coriander","Cosmic","Cranberry","Crazy","Crimson","Cucumber","Demon","Demonic","Dire","Eastern","Easy","Electric","Elemental","Evil","Extreme","Fainting","Fallen","Fancy","Fantasy","Fast","Final","First","Flaming","Flower","Flying","Forest","Fresh","Frosted","Frozen","Fruity","Garlic","Gentle","Ginger","Gingerroot","Gleaming","Glowing","Grape","Grapefruit","Green","Hazelnut","High","Holy","Honest","Honey","Hot","Hushed","Icy","Imaginary","Incredible","Infinite","Innocent","Insane","Insanity","Jasmine","Kiwi","Lavender","Lavish","Lemon","Lemonade","Lemongrass","Lemony","Lime","Low","Lucky","Mad","Mango","Melon","Mild","Milk","Milky","Mint","Minty","Molten","Mountain","Mystic","Nasty","Nimble","Noble","Northern","Noxious","Numb","Nutmeg","Nutty","Oak","Oaken","Oblivious","Obvious","Orange","Oregano","Palm","Paranoid","Passion Fruit","Peacan","Peanut","Pear","Peppermint","Perfect","Pineapple","Pink","Potato","Precious","Pure","Rainbow","Red","River","Rose","Rose Petal","Rosemary","Rotten","Rough","Rude","Rushed","Saffron","Salt 'n Pepper","Salty","Sanguine","Savage","Scented","Secret","Silent","Smooth","Southern","Spearmint","Spiced","Spicy","Spirit","Spring","Stale","Steamy","Sticky","Strawberry","Sugar","Sugary","Summer","Surprised","Sweet","Tarragon","Thyme","Tiny","Tomato","Tropic","Tropical","Twisting","Ultimate","Unholy","Universal","Unlucky","Vanilla","Vanillabean","Vibrant","Warm","Wasabi","Watermelon","Western","Wet","Whimsical","Whipped","White","Wicked","Wild","Willow","Winged","Winter","Wonderful","Wonderous","Yellow"];
	var names2 = ["Ale","Brandy","Tea","Tea","Sherry","Brew","Cappuchino","Cider","Coffee","Cognac","Dark Ale","Dark Beer","Drink","Espresso","Gin","Java","Lager","Light Ale","Light Beer","Mead","Mocha","Red Wine","Rum","Sake","Tea","Tonic","Vodka","Whiskey","White Wine","Wine","Amigo","Arrow","Ball","Barrage","Bear","Blast","Blaze","Bliss","Blitz","Blizzard","Blood","Blossom","Bolt","Bomb","Breeze","Bruiser","Bubble","Bull","Burst","Buzzer","Cooler","Crash","Critter","Crush","Crusher","Crystal","Delight","Dog","Double","Drop","Duke","Dutchess","Earthquake","Eclipse","Eight","Enigma","Eye","Five","Flash","Fluff","Fluffy","Four","Freedom","Fury","Giant","Gloom","Grog","Heaven","Hell","Hopper","Horn","Horror","Hound","Howler","Infusion","Jam","Joke","Joker","Joy","Killer","Kiss","Kisses","Knight","Lady","Lagoon","Light","Lion","Lord","Lotus","Lover","Major","Minor","Mix","Monsoon","Moonshine","Mud","Murder","Nectar","Night","Nightfall","Orb","Paradise","Paralyzer","Parody","Passion","Pearl","Pecker","Petal","Phantom","Plus","Pop","Puff","Punch","Rage","Riddle","Roar","Rumble","Rush","Score","Scream","Seven","Shadow","Shield","Shot","Shrub","Silence","Sip","Six","Sizzle","Slammer","Slap","Slapper","Sling","Slingshot","Slush","Smash","Smooch","Snake","Snowball","Sour","Special","Squeeze","Stardust","Starlight","Stinger","Storm","Striker","Sunrise","Sunset","Surge","Talon","Teaser","Temper","Tempest","Thrill","Thriller","Thunder","Ticker","Tickle","Tonic","Tornado","Torrent","Touch","Tremor","Twilight","Twister","Velour","Velvet","Vengeance","Volcano","Volley","Wacker","Walk","Walker","Wave","Whisper","Whistle","Wink","Wonder","Zombie"];
	
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * names1.length);
		rnd2 = Math.floor(Math.random() * names2.length);
		if(rnd < 30){
			while(rnd2 < 30){
				rnd2 = Math.floor(Math.random() * names2.length);
			}
		}
		names = names1[rnd] + " " + names2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}