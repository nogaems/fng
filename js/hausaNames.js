function nameGen(type){
	var nm1 = ["Abashe","Abdul","Adamu","Ahmedu","Ali","Alkali","Aminu","Amir","Audu","Babangida","Bakano","Balarabe","Barmani","Bashir","Bature","Bello","Bilal","Bulu","Danasabe","Danjuma","Danladi","Danlami","Daren","Fa'izu","Faisal","Faizu","Faruq","Finn","Fu'ad","Fuad","Gambo","Genet","Guban","Gure","Haben","Habib","Hadi","Hafiz","Hajari","Hamzah","Hassan","Hirsi","Huso","Hussain","Hussein","Ibeamaka","Ibrahim","Idris","Ife","Imam","Isa","Ismaila","Ja","Jabilo","Jabulani","Jafaru","Jalil","Jamal","Jibril","Junaidu","Kamil","Kareem","Katungi","Khairi","Khalifah","Kiho","Kijana","Kimoni","Kinfe","Kione","Kirabo","Kiros","Kitoko","Koda","Kojo","Kupakwashe","Kuron","Kwame","Madaki","Mahdi","Mahmud","Malomo","Mansa","Mansur","Mariatu","Mashaka","Messina","Mhina","Mikaili","Milandu","Morathi","Muhktar","Muhsin","Mukasa","Musa","Musawenkosi","Musoke","Mustafa","Nabil","Nabulung","Naiser","Nakima","Nalo","Nasir","Natine","Nikeese","Nyack","Nyako","Nyoka","Oafe","Oba","Obiajulu","Ochen","Odion","Okal","Okapi","Okoth","Ola","Omayma","Oni","Onika","Oringo","Otieno","Oto","Paki","Panyin","Paulo","Pemba","Phomello","Polo","Rabia","Rach","Rafiki","Rahid","Raimi","Ramses","Ranyshia","Rasheed","Rashidi","Razi","Reth","Roho","Runako","Russom","Ruzna","Sabola","Sadiki","Safina","Sahansan","Saidi","Salim","Sarda","Sarki","Seghen","Sekai","Selas","Shagari","Shehu","Tahir","Umar","Umaru","Usman","Yakubu","Yohance","Yohanna","Yusuf"];
	var nm2 = ["A'isha","Adia","Aishatu","Aminah","Arria","Arziki","Asabe","Asma'u","Assibi","Atikah","Auta","Bahijjah","Balaraba","Baturiya","Cof","Coffee","Coffi","Coffie","Colee","Coley","Colie","Danuwa","Daurama","Delu","Dura","Durah","Durrah","Fa'idah","Fa'iqah","Fa'izah","Fara","Faraa","Fari","Farih","Farra","Farry","Fatima","Fatimah","Fatuma","Fayola","Femi","Finesse","Finn","Gaddo","Gambo","Gerda","Gimbya","Gobad","Gogo","Gzifa","Habiba","Habibah","Habika","Hada","Hafsah","Halimah","Hamidah","Hanna","Hassana","Hazika","Hola","Hova","Husiana","Huso","Hussaina","Ice","Ifama","Ifeoma","Ifiok","Ifrah","Ijaba","Iman","Ina","Iverem","Iyangura","Izefia","Izza","Jabulela","Jaha","Jahzara","Jamilah","Jummai","Kaka","Keyara","Khadija","Khadijah","Khamees","Khamisa","Khari","Khatiti","Kia","Kianga","Kibibi","Kiden","Kifle","Kiho","Kijana","Kima","Kimmy","Kinfe","Kione","Kirabo","Kiros","Kisser","Kitoko","Koda","Koko","Kubra","Kuron","Kwesi","Kya","Ladi","Lami","Lantana","Laraba","Larai","Latifah","Lawanna","Layla","Lehana","Lina","Lisha","Lubabah","Maimuna","Malomo","Mandze","Manica","Mansa","Mansurah","Mapenzi","Mardea","Mariama","Mariatu","Marka","Markabo","Maryam","Mashaka","Massassi","Mawunyaga","Meria","Messina","Mhina","Mikaili","Milandu","Miniya","Miyanda","Monifa","Montsho","Muna","Musoke","Mutia","Myeisha","Na'imah","Nabilah","Nadifa","Nadira","Nafisa","Nafisah","Nafuna","Nagesa","Nailah","Naiser","Naja","Najja","Naki","Nakima","Nala","Naliaka","Nalo","Namazzi","Nana","Nangila","Nantale","Nasha","Nashwa","Nasiche","Natine","Nazi","Ndila","Neema","Nehanda","Neliah","Nia","Nini","Njemile","Nkechi","Nuru","Nyack","Nyaga","Nyako","Nyeki","Nyoka","Okimma","Oafe","Oba","Obax","Okal","Okapi","Okoth","Ola","Olayinka","Olisa","Onaedo","Oni","Ontibile","Orma","Pangi","Panya","Panyin","Pemba","Phenyo","Qwara","Raashida","Rabi'ah","Rabia","Rach","Radhiya","Rafiki","Rahmah","Ramla","Raniesha","Rashidah","Raziya","Rehema","Rena","Renah","Renna","Ruqayyah","Saada","Sade","Sadiki","Sadio","Safara","Safia","Safina","Safiyah","Saida","Saidah","Saidi","Sakinah","Salama","Salihah","Salimah","Samirah","Sanura","Sarama","Saran","Sarda","Sarki","Sauda","Seghen","Sekai","Selam","Selamawit","Selas","Semira","Shukriyah","Sumayyah","Talatu","Tani","Zahrah","Zainab","Zakiyyah","Zaytun","Zorra","Zubaydah"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd];
			nm2.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
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