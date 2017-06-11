
function nameGen(type){
	var nm1 = ["Üzeyir","ßşrÿf","ßdalat","ßlÿsgÿr","ßləkbər","ßliş","ßmin","ßnvÿr","ßsgÿr","İbiş","İbrahim","İlham","İlkin","İlqar","İlyas","İmam","İmran","İnqlab","İntiqam","İsa","İsgÿndÿr","İslam","İsmət","İsmayil","İxtiyar","İzzÿt","Şükür","Şÿfa","Şÿrÿfaddin","Şahin","Şamil","Şamxal","Şirin","Şirzad","Űlvi","Űmid","Əbűlhəsən","Əbdűləli","Əhmad","Əkbər","Əliəkrəm","Əli","Əmir","Ərtoğrul","Aüamÿli","Aüamusa","Aüaxan","Ağahadi","Ağasəfa","Abbas","Abbasqulu","Adil","Agil","Akif","Allahverdi","Anar","Arif","Asif","Asiman","Aslan","Atabala","Aydin","Azər","Azad","Bÿhaulla","Bÿhruz","Başir","Baba","Bahadur","Bakir","Bayram","Behbud","Bilal","Cəlal","Cəlil","Cəmil","Cabbar","Cahan","Cahangir","Cavad","Cavid","Ceymur","Ceyxun","Chingiz","Dadaş","Elçin","Elariz","Eldÿniz","Eldar","Elman","Elxan","Emin","Etibar","Eyyub","Füzuli","Fÿrid","Fÿrxad","Fÿyaz","Fərman","Fəxri","Faiq","Famil","Fazil","Fikrÿt","Firudin","Fuad","Gülaüa","Gündüz","Hümbət","Hüseyn","Hüseynqulu","Hÿmid","Həci","Həsən","Hafiz","Haydÿr","Israfil","Kÿrim","Kəmran","Kənan","Kamal","Kamil","Karlen","Kaz","Mübariz","Müzÿffar","Mÿmmÿd","Mənaf","Mənsur","Mahir","Maqsud","Mehdi","Mikayıl","Mirəli","Mirzÿ","Murad","Musa","Muxtar","Nübar","Nürÿddin","Nüsrət","Nəcəf","Nərmin","Nəsimi","Naği","Namiq","Nazim","Nicat","Niyaz","Nizami","Novruz","Oqtay","Orxan","Orxun","Osman","Paşa","Qabil","Qasim","Qiyas","Qoşqar","Qulam","Rüfət","Rüstÿm","Rÿsul","Rəşad","Rəşid","Rəis","Rafael","Rafiq","Ramiz","Rasim","Riza","Süleyman","Sÿbuhi","Sÿmÿd","Səlahəddin","Səlin","Sərvər","Sərvan","Sərxan","Sabir","Sadix","Saleh","Salman","Samir","Seyfulla","Seyran","Surxey","Tÿrlan","Tahir","Taqor","Teymurçin","Teymur","Teymuraz","Tofiq","Tunar","Tural","Turan","Urfan","Urxan","Vüqar","Vüsal","Vÿli","Vadim","Vahid","Valeh","Valid","Vaqif","Vasif","Xÿlil","Xalid","Xaliq","Xankişi","Xanlar","Yalçın","Yunis","Yusif","Zakir","Zaman","Zamin","Zamir","Zaur","Zeynal","Zeynulla","Ziya"];
	var nm2 = ["Çimnaz","ßdibÿ","ßdilÿ","ßminÿ","İlnarə","İlqarə","İnarə","İnayət","İnna","İntişar","İradə","İrina","İsmət","İzzÿt","Şüküfÿ","Şükür","Şÿfa","Şÿfiqÿ","Şəhrəbanu","Şəmsiyyə","Şərafət","Şirin","Űlviyya","Əcəbnaz","Əcmət","Əntigə","Əsmar","Afət","Afaq","Aidə","Aliyÿ","Almas","Arifÿ","Arzu","Ayçiçək","Ayüun","Aybÿniz","Aygül","Ayla","Aynur","Aysel","Aysu","Aytÿkin","Aytÿn","Bənövşə","Balaxanım","Brilyant","Cəmilə","Cahan","Dünya","Dünyamalı","Dürdanÿ","Dürnisa","Dilşad","Dilarÿ","Durna","Dursun","Elmirÿ","Elnarÿ","Esmeralda","Etiqad","Fÿxriyyÿ","Fatihÿ","Fatimə","Fatma","Fidan","Firəngiz","Firuzÿ","Fizzÿ","Flora","Gülüş","Gülüstan","Gülşÿn","Gülarÿ","Gülbala","Gülnarÿ","Gülnaz","Gültəkin","Günay","Gűlsűm","Hökümə","Həcər","Jalÿ","Könül","Kamalə","Lÿman","Lətifə","Lamiyə","Leyla","Liana","Lyudmila","Mÿdina","Mÿrziyya","Məhəbbət","Məhru","Mənsurə","Məryam","Məsmə","Mətanət","Mahirÿ","Maleykə","Mehparÿ","Meyransa","Minurə","Nüşabÿ","Nübar","Nÿrgiz","Nÿrminÿ","Nÿzakÿt","Nəfisə","Nəriman","Nəsib","Nahidə","Naibÿ","Nailə","Nasreen","Nasrin","Natəvan","Natalya","Natella","Nazilÿ","Nazli","Nigar","Nisÿ","Nonna","Nurşÿrÿf","Nurastÿ","Nurlanÿ","Pÿrvinÿ","Pərişan","Pakizə","Qalina","Qumru","Rübeyda","Rüxşarÿ","Rÿmilÿ","Rÿna","Rəfiqə","Rəhilə","Rəsmiyyə","Rəxşəndə","Raifə","Reyhan","Roza","Ruhÿngiz","Ruhiyyə","Sükeynÿ","Sÿbina","Sÿfurÿ","Sÿidÿ","Sÿriyya","Sűreyyə","Sədaqat","Səhər","Səmayə","Sərəncam","Sabirÿ","Sahibÿ","Samirÿ","Sara","Sevil","Sevinc","Sidiqə","Sima","Solmaz","Sona","Suüra","Tünzalə","Tÿrlan","Təhminə","Təranə","Tamaşa","Tamam","Tamara","Tamilla","Tinatin","Tuquyya","Tura","Turan","Ulduz","Vüsalÿ","Vÿfa","Vahidÿ","Validÿ","Xədicə","Xalidÿ","Xanim","Xatirə","Yana","Yeganÿ","Zöhrə","Züleyxa","Zülfiiyyə","Zümrüd","Zÿrifÿ","Zÿrinÿ","Zÿynÿgül","Zűbeydə","Zəhra","Zərnigar","Zaminÿ","Zarəngiz","Zemfira","Zeynəb","Zinÿt"];
	var nm3 = ["Abbasguliyev","Abbasov","Abdulayev","Abdulin","Abdullayev","Abdulov","Abdurrahimov","Abdurrahmanov","Abiyev","Abulhasanov","Adigozalov","Afandiyev","Aghababayev","Aghakhanov","Aghamaliyev","Aghamedhiyev","Aghamirov","Aghamirzayev","Aghanazarov","Aghayev","Ahadov","Ahmadov","Akbarov","Alakbarov","Alasgarov","Aliyev","Aljanov","Allahverdiyev","Allahyarov","Amirbeyov","Arablinski","Asgarov","Aslanov","Babayev","Baghirov","Bahlulov","Baylarbayov","Behbudov","Dadashov","Farajov","Fattahov","Gajarov","Gambarov","Garakhanov","Garayev","Gasimov","Gayibov","Gaziyev","Gharabaghi","Guliyev","Gurbanov","Hagverdiyev","Hajibabayev","Hajibeyov","Hajiyev","Hasanov","Haziyev","Heybatov","Hidayatov","Humbatov","Huseynov","Ibragimov","Ibrahimbeyov","Ibrahimov","Iravani","Isgandarov","Ismayilov","Jabbarov","Jabiyev","Jabrayilov","Jafarov","Jahangirov","Jalilov","Jamalov","Jamilov","Jamshidov","Janaliyev","Javadov","Karimov","Kazimov","Khalilov","Khanmammadow","Magsudov","Mahammadov","Maharramov","Mahmudov","Majidov","Mamishov","Mammadaliyev","Mammadbeyov","Mammadguliyev","Mammadov","Mehdiuev","Mehraliyev","Mirgasimov","Mirjavadov","Mirzayev","Nabiyev","Naghiyev","Najafov","Narimanbeyov","Orujov","Panahov","Rahimov","Rajabov","Salahov","Salmanov","Samedov","Seyidov","Shahbazov","Sharifov","Taghiyev","Tahmazov","Topchubashov","Vahabov","Valiyev","Vazirov","Zadeh"];
	var nm4 = ["Abbasguliyeva","Abbasova","Abdulayeva","Abdulin","Abdullayeva","Abdulova","Abdurrahimova","Abdurrahmanova","Abiyeva","Abulhasanova","Adigozalova","Afandiyeva","Aghababayeva","Aghakhanova","Aghamaliyeva","Aghamedhiyeva","Aghamirova","Aghamirzayeva","Aghanazarova","Aghayeva","Ahadova","Ahmadova","Akbarova","Alakbarova","Alasgarova","Aliyeva","Aljanova","Allahverdiyeva","Allahyarova","Amirbeyova","Arablinski","Asgarova","Aslanova","Babayeva","Baghirova","Bahlulova","Baylarbayova","Behbudova","Dadashova","Farajova","Fattahova","Gajarova","Gambarova","Garakhanova","Garayeva","Gasimova","Gayibova","Gaziyeva","Gharabaghi","Guliyeva","Gurbanova","Hagverdiyeva","Hajibabayeva","Hajibeyova","Hajiyeva","Hasanova","Haziyeva","Heybatova","Hidayatova","Humbatova","Huseynova","Ibragimova","Ibrahimbeyova","Ibrahimova","Iravani","Isgandarova","Ismayilova","Jabbarova","Jabiyeva","Jabrayilova","Jafarova","Jahangirova","Jalilova","Jamalova","Jamilova","Jamshidova","Janaliyeva","Javadova","Karimova","Kazimova","Khalilova","Khanmammadow","Magsudova","Mahammadova","Maharramova","Mahmudova","Majidova","Mamishova","Mammadaliyeva","Mammadbeyova","Mammadguliyeva","Mammadova","Mehdiueva","Mehraliyeva","Mirgasimova","Mirjavadova","Mirzayeva","Nabiyeva","Naghiyeva","Najafova","Narimanbeyova","Orujova","Panahova","Rahimova","Rajabova","Salahova","Salmanova","Samedova","Seyidova","Shahbazova","Sharifova","Taghiyeva","Tahmazova","Topchubashova","Vahabova","Valiyeva","Vazirova","Zadeh"];
	var nm5 = ["oğlu","lı","li","lu","lü","gil","soy","zadə"];
	var nm6 = ["qızı","lı","li","lu","lü","gil","soy","zadə"];
	var nm7 = ["a","e","i","o","u","y","ə","ÿ"];
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			if(i < 5){
				rnd2 = Math.floor(Math.random() * nm4.length);
				names = nm2[rnd] + " " + nm4[rnd2];
				nm4.splice(rnd2, 1);
			}else{
				rnd2 = Math.floor(Math.random() * nm1.length);
				rnd3 = Math.floor(Math.random() * nm6.length);
				names = nm2[rnd] + " " + nm1[rnd2] + nm6[rnd3];
			}
			nm2.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			if(i < 5){
				rnd2 = Math.floor(Math.random() * nm3.length);
				names = nm1[rnd] + " " + nm3[rnd2];
				nm3.splice(rnd2, 1);
			}else{
				rnd2 = Math.floor(Math.random() * nm1.length);
				rnd3 = Math.floor(Math.random() * nm5.length);
				for(j = 0; j <= nm7.length; j++){
					if(nm1[rnd2].substr(nm1[rnd2].length - 1) === j){
						while(rnd3 === 0){
							rnd3 = Math.floor(Math.random() * nm5.length);
						}
					}
				}
				names = nm1[rnd] + " " + nm1[rnd2] + nm5[rnd3];
			}
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