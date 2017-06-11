var nm1 = ["Agile","Beauty","Blitz","Breeze","Brisk","Buck","Charge","Class","Dart","Dash","Draft","Fleet","Flow","Flurry","Flux","Gale","Gentle","Glamor","Grace","Guard","Gust","Hale","Hate","Hurricane","Iron","Keen","Loud","Mellow","Nimble","Quick","Quiet","Rough","Rush","Sharp","Silk","Soft","Spirit","Spry","Stark","Steel","Storm","Stout","Strong","Surge","Swift","Tame","Tender","Thunder","Wild","Wind"];
var nm2 = ["beak","bill","claw","colt","eye","feather","fluff","fringe","hoof","hook","mane","plume","quill","scream","screech","steed","tail","talon","tuft","wing"];

function nameGen(type){
	var tp = type;
	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}