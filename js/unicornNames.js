var nm1 = ["Aeolus","Ainsel","Aiolos","Albion","Alewar","Amyntas","Anor","Argus","Argyros","Arion","Aron","Arryn","Auris","Baine","Bastion","Blythe","Boaz","Brand","Cadillac","Calimerio","Calimero","Chant","Chanted","Chipper","Colbolt","Corin","Craze","Dashing","Demetrius","Dryade","Elgar","Elmas","Elwyn","Eos","Erwin","Estar","Euros","Fernaco","Garvin","Giddy","Gil","Giulio","Grace","Grant","Gwayne","Gwyn","Happy","Hart","Helios","Hesperos","Iris","Izar","Jada","Jaden","Jasper","Jolly","Joshi","Julius","Kaisa","Kimber","Knight","Lance","Lancelot","Lanstrom","Linus","Lothir","Majesty","Marcello","Marjallo","Matia","Mawu","Meara","Merry","Midnight","Mika","Milky Way","Monterya","Moriba","Mortus","Mystery","Mystic","Nestor","Nightwind","Olwen","Olwin","Ozzy","Perky","Phaeton","Placido","Poseidon","Prancer","Rainbow","Robin","Roshan","Rune","Sable","Sapphire","Sigil","Silly","Silvesse","Silvester","Sly","Snow","Snowflake","Solstice","Sparkles","Starburst","Stardust","Sterling","Sunny","Sunshine","Titanius","Tomo","Tryne","Twilight","Twinkle","Unity","Virgil","Wilbur","Willow","Wrynn","Wynn","Wynstar","Xavier","Zane","Zion"];
var nm2 = ["Aalona","Acorna","Adiana","Aerowen","Agaloa","Aglaea","Ainsel","Alairia","Alanala","Albany","Aletha","Alice","Alize","Allena","Alona","Amandaria","Amara","Andra","Angelina","Annamika","Arryn","Astra","Aura","Aurae","Auris","Aurora","Baine","Bellini","Benicia","Bennettia","Biancha","Blissia","Bonita","Brandi","Breanna","Breena","Bryanne","Bubbles","Candice","Carna","Cassiopeia","Celeste","Celestia","Celina","Chant","Chanted","Chipper","Cindi","Claire","Clare","Clementine","Cortesia","Crystal","Daisy","Danika","Daphne","Della","Denali","Dessa","Deva","Drisana","Dulcea","Duscha","Electra","Elen","Elita","Elmas","Eluna","Elune","Elwyn","Emerald","Enigma","Eos","Eowyn","Epona","Estar","Estrellita","Etana","Eternia","Euros","Evania","Fae","Faith","Faye","Felicia","Fenella","Fenna","Fiona","Fleta","Floriana","Gerda","Giddy","Gil","Glamor","Grace","Gratiana","Grizelda","Gwyn","Gwynth","Happy","Hope","Hyacinthie","Hylzarie","Inara","Ira","Irene","Iris","Jada","Jade","Jaden","Javiera","Jewel","Jolly","Kaisa","Kenzie","Kimber","Langaria","Laqueta ","Larissa","Leila","Lily","Lotus","Luna","Lunaria","Lunette","Mae","Majesty","Marya","Matia","Mawu","Meara","Merry","Midnight","Mika","Milky Way","Mona","Monterya","Moriba","Mystery","Mystic","Mystique","Nadira","Necia","Nightwind","Nola","Opal","Oracle","Orielle","Pearl","Perky","Primara","Rainbow","Robin","Roshan","Ruby","Rune","Sable","Samantha","Sapphire","Sassy","Selena","Serenity","Shakti","Shanna","Sigil","Silly","Silvesse","Simona","Snow","Snowflake","Solstice","Sparkles","Speranza","Starburst","Stardust","Sterling","Sugar","Suki","Sunny","Sunshine","Sylvie","Tacita","Tama","Tara","Trixie","Tryne","Twilight","Twinkle","Unity","Valeria","Wilda","Willow","Wynn","Xaveria","Xenia","Yashiana","Yasmin","Yennaria","Yoriara","Yvonne","Zane","Zara"];
var nm3 = ["Ainsel","Arryn","Auris","Baine","Chant","Chanted","Chipper","Elmas","Elwyn","Eos","Estar","Euros","Giddy","Gil","Grace","Gwyn","Happy","Iris","Jada","Jaden","Jolly","Kaisa","Kimber","Majesty","Matia","Mawu","Meara","Merry","Midnight","Mika","Milky Way","Monterya","Moriba","Mystery","Mystic","Nightwind","Perky","Rainbow","Robin","Roshan","Rune","Sable","Sapphire","Sigil","Silly","Silvesse","Snow","Snowflake","Solstice","Sparkles","Starburst","Stardust","Sterling","Sunny","Sunshine","Tryne","Twilight","Twinkle","Unity","Willow","Wynn","Zane"];
var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
		}else if(tp === 2){
			rnd = Math.floor(Math.random() * nm3.length);
			names = nm3[rnd];
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