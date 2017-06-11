var nm1 = ["year","2 years","9 months","6 months","4 months"];
var nm2 = ["Age","All Souls","Ancestors","Animals","Art","Ashes","Asteroids","Auras","Auroras","Awe","Baking","Ballet","Beer","Birds","Birth","Bliss","Blossoms","Books","Bounties","Brass","Bravery","Bread","Brewing","Brews","Candles","Candy","Carnival","Cats","Champions","Cheese","Chickens","Children","Chocolate","Clouds","Color","Comets","Communities","Competition","Construction","Coronations","Cows","Creativity","Culinary Arts","Culture","Dance","Darkness","Death","Diversity","Dogs","Dragons","Dreams","Earth","Elders","Embers","Enlightenment","Fairies","Faith","Falling Stars","Families","Farming","Fear","Fertility","Film","Fire","Fireworks","Fish","Flames","Flight","Flowers","Folklore","Food","Forests","Friends","Friendship","Fruits","Games","Generosity","Ghosts","Gods","Grandeur","Happiness","Harmony","Harvests","Heroes","Honey","Hope","Horses","Hospitality","Hymns","Ice","Ice and Snow","Independence","Insects","Joy","Lakes","Languages","Lanterns","Laughter","Life","Light","Lights","Literature","Love","Luminescence","Magic","Meat","Melodies","Merchants","Miracles","Mirrors","Mountains","Music","Names","Nations","Nature","New Life","Nightfall","Nights","Oceans","Paint","Parents","Parks","Peace","Petals","Pigs","Planting","Prophets","Prosperity","Rainbows","Recreation","Reflection","Reincarnation","Relaxation","Remembrance","Respect","Rest","Restoration","Rivers","Seafood","Seeds","Serenity","Shadows","Silence","Sleep","Snow","Solidarity","Solstices","Sound","Spirits","Sports","Strangers","Strength","Sugar","Superstitions","Taverns","Technology","Time","Titans","Trade","Tranquility","Trees","Truth","Unity","Victory","Voices","Warmth","Water","Waves","Whispers","Wine","Wonders","Wood","Worship","Writing","Youth"];
var nm3 = ["great pleasure","much enthusiasm","great participation","a lot of anticipation","pure delight","enchanted hearts","much gratification","a lot of gusto","great expectations","many preparations","high hopes","eager participation","a lot of fascination","much bewilderment","excited hearts","awe and wonder","much creativity","big imaginations","grandeur","much joy"];
var nm4 = ["age-old","ancient","archaic","distant","divine","fairly modern","long established","long-lived","mysterious","mystical","mythical","relatively young","religious","seemingly ancient","spiritual","time lost","time-honored","undiscovered","unknown","untold"];
var nm5 = ["acts of courage","athletic competitions","bonding with family","bonding with friends","celebrating imagination","charitable donations","colorful lights","coming of age rituals","costumed mascots","creating charity gift baskets","creation of art","dance parties","decorating homes","decorating the streets","exchanging gifts","face painting","fireworks","forgiving others","gag gifts","games of chance","giving compliments","going out for dinner","group games","hanging around campfires","helping strangers","helping those in need","holiday meals","holiday related drinks","holiday themed sports games","holiday treats","homemade costumes","homemade gifts","homemade holiday decorations","hot beverages","humility","kindness for others","lighting candles","love and romance","marriage proposals","neighborhood parties","night walks","outdoor food parties","parades","playing board games","playing instruments","playing pranks","playing with pets","preparing big feasts","preparing holiday themed foods","random acts of kindness","rights of passage","romantic gestures","scavenger hunts","secret gift giving","seeing holiday movies","self discovery","singing songs","skill-based contests","spirituality","telling jokes","telling of stories","togetherness","traditional clothing","traditional dances","traditional hair styling","traditional plays","truth and dare games","watching a natural phenomena","watching special shows","wearing homemade costumes"];
var nm6 = ["one day","two days","three days","four days","five days","six days","1 week","eight days","nine days","ten days","eleven days","twelve days","thirteen days","2 weeks","1 week","2 weeks"];
var nm7 = ["decorations and festivities are often found well before and after that time as well","decorations are often found well before and after that time as well","it often continues well after that time as well","festivities often start earlier than that as well","the final half is often celebrated more strongly and looked forward to the most","the first half is often celebrated more strongly and looked forward to the most","the periods before and after that time are so festive it may as well be 4 weeks long","the final celebrations often lasts deep into the night and even into the next day","decorations often stay around for weeks after the celebrations","decorations are often seen weeks before the actual celebrations","a generally festive atmosphere continues to fill the streets for weeks after the celebrations","it can be both shorter and longer, depending on personal preferences","enthusiastic people often celebrate it for a few days more by starting earlier","a strong sense of community often gets people to celebrate it for a few days more","the final hours are by far the most intense and the most beloved hours","the opening hours are by far the most beloved hours and looked forward to by all","the opening ceremony is often the part with the most participation","the closing celebrations are what everybody looks forward to the most","it's not until the second half that celebrations really go all out","the climax of the celebrations are in the final hours and is what everybody looks forward to","another holiday starts soon after this one ends, resulting in a much longer period of festivities","this holiday ties in closely with another, so festivities continue for a much longer time","preparations often start weeks before, so many decorations can be seen much earlier","there's a long period of joy and satisfaction after the celebrations, adding to the festive atmosphere","many people will celebrate it longer by starting earlier and ending later"];
var br = [];

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	for(i = 0; i < 3; i ++){
	var rnd1 = parseInt(Math.floor(Math.random() * nm1.length));
	var rnd2 = parseInt(Math.floor(Math.random() * nm2.length));
	var rnd3 = parseInt(Math.floor(Math.random() * nm3.length));
	var rnd4 = parseInt(Math.floor(Math.random() * nm4.length));
	var rnd5a = parseInt(Math.floor(Math.random() * nm5.length));
	var rnd5b = parseInt(Math.floor(Math.random() * nm5.length));
	while(rnd5a === rnd5b){
		rnd5b = parseInt(Math.floor(Math.random() * nm5.length));
	}
	var rnd5c = parseInt(Math.floor(Math.random() * nm5.length));
	while(rnd5a === rnd5c || rnd5b === rnd5c){
		rnd5c = parseInt(Math.floor(Math.random() * nm5.length));
	}
	var rnd5d = parseInt(Math.floor(Math.random() * nm5.length));
	while(rnd5a === rnd5d || rnd5b === rnd5d || rnd5c === rnd5d){
		rnd5d = parseInt(Math.floor(Math.random() * nm5.length));
	}
	var rnd6 = parseInt(Math.floor(Math.random() * nm6.length));
	var rnd7 = parseInt(Math.floor(Math.random() * nm7.length));
	
	var name = "Every " + nm1[rnd1] + " the Festival of " + nm2[rnd2] + " is celebrated with " + nm3[rnd3] + ". It's a holiday with " + nm4[rnd4] + " roots, but today it is mostly associated with " + nm5[rnd5a] + ", " + nm5[rnd5b] + ", " + nm5[rnd5c] + " and " + nm5[rnd5d] + ".";
	var name2 = "It is officially celebrated for " + nm6[rnd6] + ", but " + nm7[rnd7] + ".";
	var name3 = "";
	if(i < 2){
		name3 = "------------------------------------------"
	}

	for(j = 0; j < 3; j++){
		br[j] = document.createElement('br');	
	}	
	element.appendChild(document.createTextNode(name));
	element.appendChild(br[0]);
	element.appendChild(document.createTextNode(name2));
	element.appendChild(br[1]);
	element.appendChild(document.createTextNode(name3));
	element.appendChild(br[2]);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}
	document.getElementById("placeholder").appendChild(element);
}	