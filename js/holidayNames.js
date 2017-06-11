var names1 = ["All Souls","Ancestor","Animal","Armistice","Art","Autumn","Beer","Bliss","Bounty","Bravery","Bread","Brew","Candle","Carnival","Cheese","Children's","Clean Water","Community","Culinary","Culture","Diversity","Dragon","Elder's","Emancipation","Emperor's","Empress'","Fairy","Family","Farming","Father's","Fertility","Fisher","Flag","Flower","Food","Friendship","Full Moon","Ghost","Harvest","Heroes","Independence","Independence","King's","Labor","Lantern","Liberation","Light","Lunar Eclipse","Martyrs'","Meat","Midsummer","Midwinter","Mother's","Music","National Flag","National Heroes","National Youth","Nature","New Moon","New Year's","Parents","Planting","Proclamation","Prosperity","Queen's","Rainbow","Recreation","Reincarnation","Relaxation","Remembrance","Republic","Respect","Science","Solar Eclipse","Solidarity","Spirit","Sport","Spring","Summer","Summer Solstice","Sunrise","Sunset","Teacher's","Traditional","Truth","Victory","Wine","Winter","Winter Solstice","Woodland"];
var names2 = ["Festival","Day","Fest","Celebration","Feast"];
var names3 = ["Age","All Souls","Ancestors","Animals","Armistice","Art","Ashes","Asteroids","Astronomy","Auras","Auroras","Autumn","Awe","Baking","Ballet","Beer","Birds","Birth","Blacksmiths","Bliss","Blood","Blossoms","Books","Bounties","Brass","Bravery","Bread","Brewing","Brews","Candles","Candy","Carnival","Cats","Celebration","Champions","Cheese","Chickens","Children","Chocolate","Clean Water","Clouds","Color","Colors","Comets","Communities","Competition","Construction","Conversation","Coronations","Cows","Creativity","Culinary Arts","Culture","Dance","Danger","Darkness","Death","Diversity","Dogs","Dragons","Dreams","Earth","Elders","Emancipation","Embers","Enlightenment","Fairies","Faith","Falling Stars","Families","Farming","Farms","Fathers","Fear","Fertility","Film","Films","Fire","Fireworks","Fish","Fishermen","Flames","Flight","Flowers","Folklore","Food","Forests","Friends","Friendship","Fruits","Games","Generosity","Ghosts","Gods","Grandeur","Happiness","Harmony","Harvests","Heroes","Honey","Hope","Horses","Hospitality","Hymns","Ice","Ice And Snow","Illumination","Independence","Insects","Joy","Labor","Lakes","Language","Languages","Lanterns","Laughter","Life","Light","Lights","Literature","Love","Luminescence","Magic","Meat","Medicine","Melodies","Men","Merchants","Midsummer","Midwinter","Miracles","Mirrors","Mothers","Mountains","Music","Names","National Heroes","Nations","Nature","New Life","Nightfall","Nightmares","Nights","Oceans","Ores","Our Flag","Our Freedom","Our Liberation","Paint","Parents","Parks","Peace","People","Petals","Pigs","Planting","Politics","Pollination","Proclamation","Prophets","Prosperity","Rainbows","Recreation","Reflection","Reincarnation","Relaxation","Remembrance","Respect","Rest","Resting Spirits","Restoration","Rivers","Safety","Sales","Science","Seafood","Seasons","Seeds","Serenity","Service","Shadows","Silence","Sleep","Snow","Solidarity","Solstices","Sound","Spirits","Sport","Sports","Spring","Strangers","Strength","Sugar","Summer","Superstitions","Taverns","Teachers","Technology","The Arts","The Bees","The Emperor","The Empress","The First Born","The First Moon","The Forest","The Full Moon","The God","The Goddess","The Gods","The King","The Lunar Eclipse","The Martyr","The Media","The Mountain","The National Flag","The New Moon","The New Rain","The New Sunrise","The New Sunset","The New Year","The Night","The Ocean","The Phoenix","The Prophet","The Queen","The Republic","The Sea","The Seafarer","The Solar Eclipse","The Stars","The Summer Solstice","The Virgin","The Volcano","The Wind","The Winter Solstice","Time","Titans","Trade","Traditions","Tranquility","Trees","Truth","Unity","Vegetables","Victory","Voices","Warmth","Water","Waves","Whispers","Wine","Winter","Women","Wonders","Wood","Worship","Writing","Youth"];
var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(i < 4){
			rnd = Math.floor(Math.random() * names1.length);
			rnd1 = Math.floor(Math.random() * names2.length);
			names = names1[rnd] + " " + names2[rnd1];
		}else{
			rnd = Math.floor(Math.random() * names2.length);
			rnd1 = Math.floor(Math.random() * names3.length);
			names = names2[rnd] + " of " + names3[rnd1];
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