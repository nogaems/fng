function nameGen(){
	var nm1 = ["aloe","anise","apple","aster","beet","bloom","blossom","breeze","butter","cabbage","carrot","cherry","clover","cluster","coco","cocoa","comet","cotton","crocus","daisy","feather","fern","flake","flannel","flora","floral","flower","fluff","fluffy","garden","gilly","gravel","grotto","grove","herb","holly","iris","jewel","jute","laurel","lemon","lilac","lily","lotus","mango","marble","melon","mistle","moss","myrtle","nugget","onion","orchid","parsnip","pebble","pepper","petal","plume","poppy","prim","puff","pumpkin","quill","radish","ribbon","rose","shell","shrub","thistle","truffle","tuber","tulip","tumble","turnip","veggie","vine","violet","whisper","wool"];
	var nm2 = ["ball","bead","blanket","bloom","bow","brim","bud","bump","cap","cloak","clog","coat","comb","cup","drape","feet","fig","flake","flint","fluff","foot","frill","gem","glove","gloves","glow","hat","hoop","leaf","lid","lock","lump","mask","mitt","mitten","moss","plume","puff","rout","sash","scarf","scarfs","shawl","shell","shoe","shoes","shrub","sock","socks","stem","stone","straw","tie","web","wig","wrap"];

	var br = "";
	$('#placeholder').css('textTransform', 'capitalize');

	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.random() * nm1.length | 0;
		rnd2 = Math.random() * nm2.length | 0;
		while(nm1[rnd] === nm2[rnd2]){
			rnd2 = Math.random() * nm2.length | 0;
		}
		names = nm1[rnd] + nm2[rnd2];
		nm1.splice(rnd, 1);
		nm2.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}