var nm1 = ["Angel Peaks","Angelic Gardens","Angelic Heights","Angelwings","Angelwood","Aurora Grove","Aurora Heights","Aurora Valley","Azure Heights","Azure Lake","Azure Valley","Beacon Point","Bellevue","Bliss Meadows","Blissful Heights","Blooming Fields","Blossoms","Blue Laguna","Blue River","Celestial Gardens","Celestial Heights","Cerulean Gardens","Cerulean Lake","Charity","Cherry Blossom","Clearwater","Cloudy Heights","Dawn Garden","Dawn Grove","Dawn Valley","Dayspring","Dragonfly Lake","Dream Forest","Dream Garden","Edgewater","Emerald Grove","Emerald Mountain","Eternal Gardens","Eternity Meadows","Evergreen Forest","Evergreen Valley","Felicity Gardens","Firefly Meadows","Firefly Waters","Flower Valley","Flowerfield","Flowerhill","Forest Vale","Fountain Vale","Fresh Meadows","Garden Springs","Genesis","Golden Halo","Golden Vale","Good Samaritan","Grand Meadow","Grand Oasis","Grand Valley","Great Garden","Green Valley","Grove Garden","Guardian Angel","Harmony","Harmony Heights","Harmony Lake","Harmony Meadows","Harmony Mountains","Harmony Valley","High Garden","Highland Garden","Holy Oak","Hope Garden","Hope Valley","Horizon","Hummingbird Garden","Koi Pond","Lakeside","Lilypad","Lilypad Meadows","Lilypad Water","Little Feather","Little Peak","Littlerock","Love Garden","Maple Grove","Mapleleaf","Meadow Isle","Mirror Lake","Misty Meadow","Misty Vale","Moonlight","Moonlight Meadows","Morningrise","Morningtide","Moss Forest","New Blessings","New Eden","New Horizon","Nirvana Heights","Noble Gardens","Noble Vale","Oak Meadow","Oak Valley","Olympus","Paradise Garden","Paradise Meadows","Paragon Heights","Paragon Valley","Peace Meadows","Peace Vale","Peace Valley","Pearl Garden","Pearly Lake","Pine River","Pine Valley","Rainbow Meadow","Renaissance","Repose Meadows","Riverside","Rose Garden","Rose Petal","Rosemary","Rosewood","Sacred Heart","Sacred Heights","Sage Forest","Sanctuary Gardens","Sanctuary Meadows","Sapphire Valley","Satin Gardens","Serenity","Serenity Falls","Serenity Grove","Serenity Heights","Serenity Lake","Serenity Peaks","Silence Lake","Silk Meadow","Silk River","Silver Birch","Silver Oak","Silverwing","Silverwood","Smooth Meadows","Smooth Valley","Snow Gardens","Snow Valley","Snowfall Valley","Snowflake","Soft Gardens","Soft Meadows","Solitude Gardens","Solitude Heights","Spirit Fields","Spirit Meadows","Spring Blossom","Spring Forest","Spring Garden","Spring Grove","Spring Horizon","Spring Pond","Springfield","Sprite Gardens","Sprite Valley","Starfall Lake","Starlight","Stillwater","Summer Gardens","Summerhill","Sunrise","Sunrise Grove","Sunrise Valley","Swan Lake","Swan River","Tranquil Falls","Tranquil Heights","Tranquil Peaks","Tranquil River","Tranquil Summit","Tranquil Valley","Tranquility Lake","Trinity Heights","Tulip Gardens","Twin Lakes","Twin Rivers","Velvet Gardens","Waterfall Gardens","Waterfall Meadow","Waterfall Valley","West Valley","Westwood","Whisperwood","White Dove","White Feather","White Mountain","White Valley","White Willow","White Wing","White Wings","Wildflower","Willow Vale","Willow Waters"];
var nm2 = ["Asylum","Mental Institution","Sanatorium","Psychiatric Hospital","Mental Hospital","Psychiatric Institution","Mental Asylum"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + " " + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}