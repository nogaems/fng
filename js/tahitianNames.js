
function nameGen(type){
	var nm1 = ["Ahurei","Aia","Aiani","Aifeuna","Amo","Arii-fataia","Ariipaea","Aru","Auri","Auriro","Enometua","Farerohi","Haamanemane","Hama","Hamau","Haneti","Hapai","Haururu","Hiro","Hurimaavehi","Itiiti","Mahine","Mahui","Mai","Manea","Manua","Maoae","Matafaahira","Mauaihiti","Mauaroa","Moearu","Moemoe","Namiro","Niuhu","Nohoraa","Nuutere","Ohatatama","Omai","Opuhara","Oreo","Ori","Panee","Paofai","Pati'i","Pena","Pihato","Punua","Punua-teraitua","Taaroa","Taaroa-manahune","Taauaitatanuurua","Taino","Tamatoa","Tapoa","Tati","Tau","Taua-i-taata","Taura","Taura-atua","Tauraatua","Taute","Tavi","Tavihauroa","Te-manutunuu","Te-maui-ari'i","Te-mooiapitia","Teaatoro","Teaej","Tefaaora","Tehapai","Teieie","Teihotu","Temoo","Teohu","Tepau","Tepauarii","Terii","Terii-maevarua","Teriimana","Teruru","Tetohu","Tetumanua","Teu","Teuira","Teuira-arii","Teuraiterai","Teva","Tevahitua","Tiaau","Tiipaarii","Toa","Tuaroa","Tuhei","Tumoehamia","Tunuieaiteatua","Tupaia","Tutaha","Tutahau","Tuutini","Uata","Ui","Uruumatata","Vaetua","Vairatoa","Vanaama","Vari","Vari-mataauhue","Vavahiiteraa","Vehiatua","Veve"];
	var nm2 = ["'Itea","Ahurai","Aimata","Aironoana'a","Airoro","Airotua","Arili-manihinihi","Ariioehau","Ariitaimai","Aroroerua","Auau","Fareahu","Fetefeteui","Hototu","Ino Metua","Maheanuu","Marae-ura","Moe","Murihau","Ourahi","Patea","Pateamai","Peutari","Piharii","Pipiri","Poivai","Purea","Taaroa","Taia","Tapuhote","Taura","Taura-atua","Tauraatua","Taurua","Te-aropoanaa","Te-fete-fete-ui","Teeva","Teeva Pirioi","Tefeau","Tehaapapa","Tehea","Teihotu","Temaehuata","Teraha-tetua","Teraiautia","Teraitua","Teremoemoe","Terero","Teri'i","Teri'itorai","Teriitahi","Teriitua","Teriivau","Teriivua-iterai","Terite","Terito","Teroroeora","Teroroera","Tetua","Tetua-umeritini","Tetuaehuri","Tetuahuri","Tetuanui","Tetuanuireia","Tetuaraenui","Tetuaunurau","Tetunania","Tetupaia","Tetupua","Teuira","Tevurua","Tevurua-hoiatua","Tevuruahoratua","Tiipaarii","Tupuetefa","Ura","Vavea"];

	var br = "";
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.random() * nm2.length | 0;
			names = nm2[rnd];
			nm2.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm1.length | 0;
			names = nm1[rnd];
			nm1.splice(rnd, 1);
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