
function nameGen(type){
	var nm1 = ["Chege","Chomba","Ciugũ","Gĩchũki","Gĩchũrũ","Gĩcheha","Gĩchere","Gĩchikũ","Gĩchohi","Gĩchuhĩ","Gĩkonyo","Gĩtũma","Gĩtũra","Gĩtaũ","Gĩtahi","Gĩtari","Gĩthĩnji","Gĩthaiga","Gĩthire","Gĩtonga","Gĩtukũ","Gachũhĩ","Gachagua","Gachanja","Gachara","Gachii","Gakure","Gathaiya","Gathanja","Gathenya","Gathigira","Gathogo","Gathongo","Gathu","Gathua","Gathuuri","Gatimũ","Githendũ","Goko","Hinga","Irũngũ","Ireri","Kĩbachia","Kĩbakĩ","Kĩbunja","Kĩhĩa","Kĩhara","Kĩhiũ","Kĩhoro","Kĩhuna","Kĩmani","Kĩmotho","Kĩmunya","Kĩng’Ori","Kĩnuthia","Kĩnyanjui","Kĩnyua","Kĩoi","Kĩongo","Kĩrĩka","Kĩrĩma","Kĩragũ","Kũngũ","Kabirũ","Kabutha","Kago","Kagoci","Kagwa","Kahũthia","Kahara","Kahiĩ","Kairu","Kamande","Kamangĩ","Kamau","Kamotho","Kaniũ","Kanja","Karĩmi","Karũgũ","Karanja","Kariũki","Karungu","Kenyatta","Kibe","Kimane","Kimaru","Kimathi","Kinũthia","Kogĩ","Koinange","Kuria","Mĩchuki","Mũchene","Mũchoki","Mũciri","Mũgane","Mũgo","Mũhĩa","Mũhũri","Mũhoho","Mũhoro","Mũirũrĩ","Mũite","Mũkundi","Mũnene","Mũngai","Mũngania","Mũrĩgĩ","Mũrĩithi","Mũrĩmi","Mũrĩranja","Mũrĩu","Mũrũngarũ","Mũragũri","Mũrakaru","Mũraya","Mũrira","Mũtũng’Ũ","Mũtegi","Mũthĩnji","Mũthũi","Mũthũngũ","Mũtiga","Mũtugi","Mũya","Macharia","Mahĩhu","Maina","Maitho","Mathani","Mathenge","Matu","Mbĩra","Mbũgua","Mbũrũ","Mogo","Muriũki","Murigo","Mwagĩru","Mwai","Mwanĩki","Mwangi","Mwathi","Ndũn'Gũ","Ndegwa","Nderitũ","Ndiangui","Ndirangũ","Ngũgĩ","Ngũnjiri","Ng'Ang'A","Ngarĩ","Ngechũ","Ngengi","Ngichũ","Ngigĩ","Ngina","Nginyo","Ngure","Njũki","Njaũ","Njagĩ","Njaramba","Njau","Njenga","Njerũ","Njogu","Njoka","Njomo","Njonjo","Njoroge","Njuguna","Nyamu","Nyoike","Nyoro","Thairu","Theuri","Thuũ","Thuku","Wachira,","Wachiru","Wachiuri","Wachiuru","Wahome","Waigwa","Wainaina","Waita","Waititũ","Wakaritũ","Wamũgũnda","Wamahiũ","Wambũgũ","Wamiti","Wanderi","Wang’Ombe","Wang’Ondu","Wang'Ombe","Wanjohi","Wanyoike","Warũĩ","Warũirũ","Warari","Watene","Wawerũ"];
	var nm2 = ["Gakuhĩ","Gathoni","Jata","Kanyi","Kioni","Mũkami","Mũkina","Mũmbi","Mũrĩnga","Mũringo","Mũrugi","Mũthoni","Magiri","Makena","Moombi","Mukami","Mukondi","Mumbi","Murigo","Murugi","Muthoni","Mwara","Mwihaki","Nũngari","Nduta","Ngĩna","Ng’Endo","Ngendo","Ngina","Njambi","Njeri","Njoki","Noni","Nyagũra","Nyagũthiĩ","Nyaguthii","Nyakio","Nyambugi","Nyambura","Nyawĩra","Nyawira","Nyokabi","Wacũ","Waceera","Waceke","Wacuka","Wagichugu","Wahu","Waihumbu","Wairimũ","Wairimu","Wairmu","Waithĩra","Waitherero","Waithira","Wakiuru","Wamũyũ","Wamaitha","Wambũi","Wambeere","Wambugua","Wambui","Wameru","Wamuhu","Wamuiru","Wamweru","Wandia","Wangũ","Wangũi","Wangai","Wangarĩ","Wangari","Wangeci","Wangera","Wangu","Wanjĩra","Wanja","Wanjeri","Wanjikũ","Wanjiku","Wanjirũ","Wanjira","Wanjiru","Wanyiri","Wanyora","Warĩnga","Warũgũrũ","Warigia","Wathira","Wawĩra","Wokabi"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.random() * nm2.length | 0;
			rnd2 = Math.random() * nm2.length | 0;
			names = nm2[rnd] + " " + nm2[rnd2];
			nm2.splice(rnd, 1);
			nm2.splice(rnd2, 1);
		}else{
			rnd = Math.random() * nm1.length | 0;
			rnd2 = Math.random() * nm1.length | 0;
			names = nm1[rnd] + " " + nm1[rnd2];
			nm1.splice(rnd, 1);
			nm1.splice(rnd2, 1);
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