
function nameGen(type){
	var nm1 = ["Achariya","Akara","Amara","Anchaly","Arun","Atith","Bona","Bora","Boran","Borey","Bourey","Bunroeun","Chakara","Chakra","Chakriya","Chamroeun","Chankrisna","Chann","Chanthou","Chantou","Chantrea","Chanvatey","Chariya","Charya","Chea","Chhay","Chhaya","Dara","Darany","Davuth","Heng","Khemera","Kiri","Kosal","Kravann","Leap","Makara","Many","Mao","Mau","Meaker","Mittapheap","Montha","Mony","Munney","Munny","Narith","Nhean","Nimith","Nimol","Nisay","Noreaksey","Oudom","Peou","Phala","Pheakdei","Phirum","Phirun","Pich","Piseth","Pisey","Poeu","Ponleak","Ponleu","Ponlok","Prak","Pros","Puthyrith","Rachana","Rainsey","Raksmei","Rangsei","Rasmey","Rath","Rathana","Rathanak","Reasmey","Rith","Rithipol","Rithisak","Rithy","Roth","Rotha","Rothana","Rothanak","Rottana","Sakngea","Samang","Samay","Sambath","Samlain","Samnang","Samphy","Samrin","Sangha","Sann","Serey","Sokha","Sokhem","Sokhom","Sokun","Somnang","Sonith","Sopat","Sopath","Sophat","Sophea","Sopheaktra","Sopheap","Sopheara","Soriya","Sorya","Sotearith","Sotha","Sotharith","Sothea","Sothear","Sothiya","Sothy","Sourkea","Sov","Sovann","Sovanna","Sovannarith","Sros","Thom","Vannak","Veasna","Veha","Vibol","Vichear","Vichet","Vireak","Vireakboth","Visal","Viseth","Visna","Visoth","Visothirith","Vithara","Vithu"];
	var nm2 = ["Achariya","Akara","Anchaly","Arunny","Ary","Bopha","Botum","Boupha","Chakriya","Champei","Chamroeun","Chan","Chankrisna","Chanlina","Chanmony","Channary","Chanthavy","Chanthou","Chantou","Chantrea","Chanvatey","Chariya","Charya","Chavy","Chaya","Chenda","Chhaya","Chhean","Chhorvin","Chhorvon","Chivy","Choum","Da","Daevy","Dara","Darareaksmey","Davi","Davy","Devi","Jorani","Kalianne","Kaliyan","Kaliyanei","Kalliyan","Kanleakhana","Kannareth","Kannitha","Kanya","Kesor","Khean","Kolab","Koliyan","Kolthida","Kravann","Kunthea","Leakena","Leap","Mach","Makara","Malis","Maly","Many","Mao","Mau","Mean","Mliss","Mony","Nakry","Narin","Nary","Nearidei","Neary","Nuon","Peou","Phally","Phary","Pheakdei","Pheakkley","Phhoung","Pich","Pisey","Poeu","Ponlok","Punthea","Putrea","Rachana","Rachany","Raksmei","Rangsei","Rasmey","Rath","Rathana","Reach","Reaksmey","Reasmey","Roth","Rotha","Rotha","Rothana","Rottana","Roumduol","Roumjong","Saley","Samphy","Sathea","Savady","Sawatdee","Seda","Serey","Setha","Seyha","Sikha","Sinuon","Sita","Sobin","Soboen","Socheat","Sok","Sokha","Sokhanya","Sokhom","Sombo","Sonisay","Sophal","Sophea","Sopheap","Sopheary","Sophon","Sophorn","Soportevy","Soriya","Soriya","Sorpheny","Sorya","Sotear","Sotear","Sotearith","Sothea","Sotheara","Sothy","Sourkea","Sovanara","Sovandary","Sovaneary","Sovann","Sovanna","Sovannary","Sraem","Srey","SreyPek","Sreymom","Sreynuon","Sreypich","Sros","Suorsdey","Taevy","Tevy","Thavary","Theary","Thida","Thom","Thyda","Tina","Toch","Touch","Vanna","Veasna","Veata","Vimean","Visal","Visna"];
	var nm3 = ["Aang","Aek","Ang","Aok","Ben","Bun","Chak","Chan","Chea","Chen","Chey","Chhan","Chhay","Chhem","Chhet","Chhim","Chhit","Chhorn","Chhoub","Chim","Chin","Choem","Choeun","Din","Dith","Dul","Duong","Eam","Eav","Ek","Em","Heang","Ho","Hong","Hoy","Hu","Hun","Iam","Iem","Im","Iv","Jan","Jay","Jen","Jey","Jin","Keo","Khai","Khan","Khat","Khay","Khiev","Khin","Khlot","Khoun","Khun","Kim","Kong","Lim","Long","Lorn","Loun","Ma","Mak","Mao","Mean","Meang","Meas","Meng","Mok","Mon","Moul","Mul","Muoy","Muy","Neak","Nhek","Noung","Nourn","Nout","Ok","Om","On","Ong","Or","Ou","Ouch","Ouk","Pang","Pen","Phan","Phann","Pheng","Phon","Phy","Pok","Prak","Preap","Prum","Ros","Rous","Saluk","Sam","San","Sang","Sar","Sat","Say","Seang","Sen","Seng","Sieng","Sin","So","Sok","Sok ","Som","Son","Song","Sor","Sorm","Soun","Su","Suy","Tang","Tat","Tep","Thith","Thy","Toch","Touch","Tum","Ty","Uch","Um","Ung","Uy","Vang","Voeum","Yim","Yos","Yous","Yu","Yun"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm3.length);
		if(tp === 1){
			rnd2 = Math.floor(Math.random() * nm2.length);
			names = nm3[rnd] + " " + nm2[rnd2];
		}else{
			rnd2 = Math.floor(Math.random() * nm1.length);
			names = nm3[rnd] + " " + nm1[rnd2];
		}
		nm3.splice(rnd, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}