var nm1 = ["Alliance","Amity","Angelstone","Angelvale","Angelwing","Angelwood","Animas","Archangel","Bayhealth","Bayview","Beacon","Bellevue","Bellflower","Big Heart","Big River","Blessings","Blossom","Blossom Valley","Blossomvale","Broadwater","Castle","Charity","Cherry Blossom","Citrus","Clearview","Clearwater Lake","Clearwater Valley","Clemency","Crossroads","Desert Springs","Diamond Grove","East Valley","Eden","Edgewater","Evergreen","Fairbanks","Fairmont","Fairview","Featherfall","Flowerhill","Forest Health","Forest View","Fortuna","Fortune","Fountain Valley","Freeman","Garden City","Garden Grove","Genesis","Golden Oak","Golden Valley","Goldriver","Goldvalley","Good Samaritan","Grace","Grand Garden","Grand Meadow","Grand Mountain","Grand Oak","Grand Plains","Grand River","Grand University","Grand Valley","Grand View","Grand Willow","Grandview","Great Plains","Great River","Green Country","Green Hill","Greengrass","Greenlawn","Greenwood","Griffin","Guardian","Hallmark","Harmony","Harmony Grove","Healthbridge","Healthstone","Heart Center","Heartland","Heartstone","Highland","Highlands","Hill Crest","Hillsdale","Honor","Honor Grave","Hope Garden","Hope Haven","Hope Valley","Hopedale","Hopevale","Horizon","Hot Springs","Hyacinth","Jade Forest","Kindred","Kindred Soul","Laguna","Lakeland","Lakeside","Lakewood","Lifecare","Light Beacon","Lilypad","Lilypad Gardens","Little River","Love","Lowland","Lullaby","Magnolia","Maple Grove","Maple Valley","Marine","Meadowview","Memorial","Mercy","Mercy Vale","Mineral","Morningside","Mountain View","New Eden","New Horizons","Noble","North Star","Northshore","Oak Crest","Oak Valley","Oakdale","Oasis","Olympus","Orange Garden","Overlook","Paradise Grove","Paradise Valley","Parkview","Peace Forest","Peace River","Peak View","Pearl River","Petunia","Phoenix","Pine Rest","Pine Valley","Pinevale","Pinevalley","Pioneer","Primary","Principal","Progress","Promise","Rainbow","Repose","Ridgeview","Riverside","Riverview","Rose","Rose Gardens","Rose Petal","Rose Valley","Rosemary","Rosewood","Ruby Valley","Sacred Heart","Samaritan","Sapphire Lake","Serenity","Silver Birch","Silver Boulder","Silver Gardens","Silver Hill","Silver Lake","Silver Oak","Silver Pine","Silver Wing","Silverstone","Silverwood","Snowflake","Southshore","Specialty","Spring Forest","Spring Fountain","Spring Grove","Spring Harbor","Spring Hill","Spring River","Springfield","Springhill","Stillwater","Summer Springs","Summerfield","Summerhill","Summerstone","Summit","Swan River","Swanlake","Tranquil Valley","Tranquility","Trinity","Tulip","Twin Lakes","Twin Mountains","Union","United","Valley Health","Wellness","West Valley","Westview","White Blossom","White Feather","White Mountain","White Petal","White River","White Willow","White Wing","Wildflower","Willow Gardens","Woodland"]
var nm2 = ["Clinic","Community Hospital","General Hospital","Hospital","Hospital Center","Medical Center","Medical Clinic"];
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