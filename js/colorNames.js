var nm1 = ["Almond","Amaranth","Amber","Amethyst","Aquamarine","Auburn","Azure","Beige","Black","Blond","Blue","Bone","Brass","Bronze","Brown","Cerulean","Cherry","Chrome","Coal","Cobalt","Coffee","Coral","Cream","Crimson","Cyan","Ebony","Emerald","Fuchsia","Gold","Green","Grey","Indigo","Ivory","Jade","Jasmine","Jasper","Khaki","Lava","Lavender","Lemon","Chocolate","Lilac","Magenta","Malachite","Maroon","Mauve","Moss","Obsidian","Onyx","Orange","Peach","Pink","Purple","Red","Rose","Ruby","Saffron","Sand","Sanguine","Sapphire","Satin","Scarlet","Sienna","Silver","Tan","Teal","Turquoise","Ultramarine","Umber","Vanilla","Velvet","Vermilion","Violet","White","Yellow"];
var nm2 = ["Abstract","Abyss","Abyssal","Aged","Ageless","Airy","Alien","Ancient","Angelic","Antique","Archaic","Arctic","Argent","Aristocratic","Ashy","Astral","August","Aura","Aurora","Autumn","Baby","Big","Bland","Blazing","Bleached","Bleak","Blemished","Bloated","Blossom","Botanic","Bouncy","Bright","Brilliant","Burned","Burning","Burnished","Caribbean","Castle","Celestial","Charged","Charming","Charred","Classic","Classy","Clear","Cloudy","Coarse","Common","Cool","Corrupt","Cosmic","Crazed","Crazy","Cyber","Dark","Dawn","Dazzling","Deep","Delicate","Deluxe","Dignified","Dim","Distorted","Divine","Dreary","Dull","Dusk","Dynamic","Eerie","Electric","Empyral","Enchanting","Eternal","Exciting","Experimental","Faded","Faint","Field","Fierce","Fiery","Flamboyant","Flaming","Flawless","Floral","Fluid","Forest","Freaky","Fresh","Frigid","Frosty","Frozen","Fuzzy","Galactic","Garden","Generic","Generous","Gentle","Ghastly","Ghostly","Giant","Glamorous","Glistening","Gloomy","Glorious","Glossy","Glowing","Grim","Groovy","Happy","Harsh","Harvest","Herbal","Hot","Illuminated","Immortal","Imperial","Imposing","Intense","Irresistible","Joyful","Jungle","Lavish","Light","Livid","Loud","Loving","Low","Lucent","Lucid","Luminous","Lush","Lustrous","Luxurious","Magic","Magical","Majestic","Marsh","Mechanical","Medieval","Medium","Mellow","Metallic","Midnight","Mild","Misty","Moderate","Modern","Modest","Monster","Moonlit","Mountain","Murky","Mystery","Mystical","Mythic","Noble","Noisy","Obscure","Old","Old-Fashioned","Ordinary","Pale","Paradise","Parched","Pastel","Pasture","Peaceful","Pleasant","Polar","Polished","Precious","Premium","Primitive","Proud","Psychedelic","Putrid","Radiant","Regal","Rich","Rigid","Rough","Royal","Rusty","Seductive","Shadow","Silky","Smooth","Smoldering","Soft","Somber","Sonic","Sovereign","Spectral","Spicy","Spring","Steamy","Strong","Sublime","Summer","Sunlit","Sunrise","Sunset","Superior","Supernatural","Supreme","Swamp","Sweet","Tacky","Tempting","Tender","Timeless","Tired","Tranquil","Tropical","Twilight","Undead","Unsullied","Vague","Vampiric","Vineyard","Vintage","Violent","Virtual","Vivid","Volatile","Washed Out","Wild","Wilderness","Winter","Youthful"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm2[rnd2] + " " + nm1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}