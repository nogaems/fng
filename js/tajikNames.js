var nm1 = ["Anoushirvan","Arash","Ardavan","Ardshir","Armeen","Aryan","Arzhang","Ashkan","Atash","Awrang","Azad","Azada","Azarkhsh","Azerm","Babak","Bahman","Bahram","Bamdad","Behnam","Behrang","Behruz","Behzad","Buzurgmehr","Dara","Darab","Daryush","Dehqan","Esfandyar","Faramarz","Faraz","Fardad","Fardin","Farhad","Farhang","Fariad","Fariborz","Farrukh","Farrukhzad","Farshad","Farzad","Farzam","Farzann","Farzin","Feda","Firuz","Forood","Fraidun","Fruhar","Giv","Goudarz","Gulab","Gushtasb","Hamasa","Hoshang","Houshmand","Housyar","Human","Humayon","Hurmoz","Iraj","Jahandar","Jahangeer","Jahanshah","Jawid","Kaihan","Kaikhosrow","Kaiqubad","Kaiyan","Kambiz ","Kamran","Kamshad","Kamyar","Kanishka","Kasra","Kavah","Kavoos","Khashyar","Khoram","Khuda Dad","Kia","Kianoosh","Kiumars","Kohyar","Kosha","Koshan","Kourash","Mahyar","Mani","Manuchehar","Mazdak","Mehrab","Mehrak","Mehran","Mehrang","Mehrdad","Mehrzad","Morad","Namdar","Namvar","Naraiman","Neda","Niyoosha","Noushzad","Omaid","Padshah","Paghahan","Pagzman","Paikan","Paiman","Parsa","Parwaaze","Payam","Pazhman","Pendar","Piruz","Poya","Qiomars","Qubad","Rastin","Rohina","Roozbeh","Roshan","Royan","Rozi","Rukhshan","Rustam","Salar","Sam","Saman","Sasan","Sepehr","Shadan","Shahbaz","Shaheen","Shahpur","Shahram","Shahrdad","Shahrukh","Shahryar","Shaya","Shayan","Shuhab","Siamak","Siamu","Siawash","Sina","Soroush","Sougand","Suhrab","Tahmaseb","Toktam","Tooraj","Tora","Toramana","Varshasb","Veda","Vishtasb","Yama","Zal","Zand ","Zardusht","Khosrow"];
var nm2 = ["Afareen","Afsana","Afsar","Afshan","Afsoon","Anahita","Anoosheh","Ara","Arezo","Arghavan","Armaghan","Asa","Asal","Ava","Avizeh","Awa","Azar","Azin","Bahar","Baharah","Baharak","Banafshah","Banou","Behnaz","Behrukh","Belour","Belourine","Bizhan","Boosah","Darya","Delaram","Delbar","Delkash","Delruba","Dorri","Farahnak","Farahnaz","Faranghis","Farhana","Farkhonda","Farrin","Farrukh","Farzaneh","Fila","Firoza","Forogh","Forozan","Forozenda","Freba","Freshta","Fruzan","Gawhar","Geesou","Ghoncheh","Giti","Golbahar","Gulgun","Gulnar","Gulnaz","Gulnessa","Gulpari","Gulshan","Gurdia","Hangahma","Hasti","Huma","Jahan Ara","Javaneh","Katayoun","Khandan","Khaterah","Khojasta","Khorsheed","Lala","Lila","Lily","Mahasti","Mahdokht","Mahnaz","Mahrukh","Mahsa","Mahtab","Mahwash","Manizha","Marjan","Marmar","Mastana","Mehrangiz","Mehrnaz","Mehrnoosh","Mehry","Mina","Minoo","Mitra","Mona","Murwarid","Muzghan","Muzhdah","Nahal","Najela","Nargis","Nasreen","Nastaran","Nava","Naz","Naz Gul","Nazaneen","Nazhin","Nazhla","Nazy","Neelab","Neelufar","Negar","Negeen","Negha","Niki","Nikoo","Nousafarin","Noushin","Padidah","Parand","Parastoo","Pareeya","Pari","Paricheher","Parirow","Parisa","Pariwash","Parwana","Parween","Paymaneh","Paywand","Poran Dokht","Rasa","Roudabeh","Rukhsana","Rukhshan","Saaman","Saghar","Sahar","Sahba","Sapedah","Seema","Setara","Shabnam","Shadan","Shahla","Shahnaz","Shahnoza","Shahrbano","Shahrnaz","Shahrzad","Shahzadah","Shameem","Shararah","Sheeftah","Sheela","Sheeva","Shervin","Shirin","Shirin Bano","Shogofa","Shokouh","Sholah","Simin","Soudabah","Souzan","Tahminah","Tanaz","Taneen","Tara","Tarana","Taranum","Yagana","Yakta","Yalda","Yasaman","Zarrin","Zarrin Dokht","Zarrina","Zeba","Zhalah","Zheela"];
var br = "";

function nameGen(type){
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
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