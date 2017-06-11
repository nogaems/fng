
function nameGen(type){
	var nm1 = ["Afamefula","Afamefuna","Agu","Akabueze","Akachi","Akubundu","Akuchi","Akumjeli","Amadi","Amazu","Azubuike","Belonwu","Beluchi","Buchi","Chee","Chi","Chibueze","Chibuike","Chibuzo","Chidea","Chidee","Chidey","Chidi","Chidie","Chidiebere","Chidiebube","Chidiegwu","Chidike","Chidubem","Chidy","Chiemeka","Chijindum","Chijioke","Chika","Chike","Chikelu","Chikere","Chima","Chimaijem","Chinasa","Chinaza","Chinedu","Chinelo","Chinese","Chineze","Chino","Chinou","Chinua","Chinuah","Chinwe","Chinweike","Chinwendu","Chinweuba","Chioke","Chioma","Chizoba","Chononso","Chuks","Chukwubuikem","Chukwudi","Chukwuemeka","Chukwuma","Chydea","Chydee","Chydey","Chydi","Chydie","Chydy","Chyke","Diji","Dike","Ebele","Ekene","Ekenedilichukwu","Ekwueme","Emeka","Enyinnaya","Fumnanya","Halim","Halimnye","Ibeabuchi","Ibezimako","Ifeanyichukwu","Ifeatu","Ijeawele","Ijendu","Ikem","Ikenna","Iweobiegbulam","Izuchukwu","Jaja","Jajah","Jamuike","Jel","Jelan","Jelanea","Jelanee","Jelaney","Jelani","Jelanie","Jelany","Jideofor","Jioke","Koofrey","Madou","Madu","Maduabuchim","Madue","Madukaife","Madukwe","Mazi","Mazzi","Munachiso","Ndidi","Ndulu","Ngozi","Nkechi","Nkemdilim","Nnamdi","Nwabudike","Nwankwo","Nweke","Nwoye","Obasea","Obasee","Obasey","Obasi","Obasie","Obasy","Obea","Obee","Obey","Obi","Obie","Obike","Oby","Obyke","Odion","Ogbonna","Ogbonnia","Okafo","Okechukwu","Okeke","Okeli","Okonkwo","Okorie","Okpara","Okparo","Okparra","Okparro","Oluchi","Onuchukwu","Onyekachi","Onyekachukwu","Orjea","Orjee","Orjey","Orji","Orjie","Orjy","Ozioma","Ozoemena","Somayina","Tobechukwu","Uche","Uchea","Uchechea","Uchechee","Uchechey","Uchechi","Uchechie","Uchechy","Uchee","Uchey","Uchi","Uchie","Uchy","Udegbulam","Udegbunam","Udo","Ugochukwu","Ugonna","Ugoorji","Uwaezuoke","Uzochi","Uzochukwu","Uzoma","Yobachukwu","Yobanna","Zebenjo","Zikoranaudodimma"];
	var nm2 = ["Adaeze","Adaezennaya","Adamma","Adanma","Adanna","Adannaya","Adaobi","Adaoma","Adaora","Akachi","Akuchi","Akumjeli","Amachea","Amacheah","Amachee","Amachey","Amachi","Amachie","Amachy","Amachye","Amaka","Amaogechukwu","Amara","Amarachi","Amarachukwu","Anuli","Anulika","Chi","Chiamaka","Chibueze","Chibuifem","Chibuike","Chibuzo","Chichi","Chidea","Chideah","Chidee","Chidey","Chidi","Chidie","Chidiebere","Chidiebube","Chidiegwu","Chidimma","Chidinma","Chidy","Chijindum","Chika","Chikanso","Chike","Chikelu","Chikere","Chimaijem","Chinagorom","Chinaka","Chinasa","Chinaza","Chinecherem","Chinedu","Chineze","Chinonso","Chinwe","Chinweike","Chinwendu","Chinweuba","Chinyelu","Chinyere","Chioma","Chizoba","Chukwudi","Chukwuebuka","Daluchi","Daluchineke","Ebele","Ebuka","Echerem","Ekene","Ekenedilichukwu","Eshe","Fumnanya","Funanya","Gorom","Halim","Halimnye","Ifama","Ifamah","Ifamma","Ifammah","Ifenyinwa","Ifeoma","Ifunanya","Ijendu","Iruka","Iweobiegbulam","Kambiri","Maduabuchim","Madukaego","Mgbankwo","Mgbeke","Mgborie","Munachiso","Ndidi","Ngozi","Nkechi","Nkechinyere","Nkemdilim","Nkiru","Nkiruka","Nneka","Nnenna","Nnenne","Nwanneka","Odera","Ogechi","Ogechukwukama","Olisa","Oluchi","Onochie","Onuchukwu","Onyeka","Onyekachi","Onyekachukwu","Otuosoro","Ozioma","Uchena","Uchenah","Uchenna","Uchennah","Udo","Ula","Urenna","Urunwa","Uzoamaka","Uzochi","Uzochukwu","Uzoma","Yobachukwu","Yobanna","Zikoranaudodimma"];
	var nm3 = ["Akachi","Akuchi","Akumjeli","Chi","Chibueze","Chibuike","Chibuzo","Chidi","Chidiebere","Chidiebube","Chidiegwu","Chijindum","Chika","Chike","Chikelu","Chikere","Chinasa","Chinaza","Chinedu","Chinwe","Chinweike","Chinwendu","Chinweuba","Chioma","Chizoba","Chononso","Ebele","Ekene","Ekenedilichukwu","Fumnanya","Halim","Halimnye","Ijendu","Iweobiegbulam","Maduabuchim","Munachiso","Ndidi","Ngozi","Nkechi","Nkemdilim","Oluchi","Onuchukwu","Onyekachi","Onyekachukwu","Ozioma","Udo","Uzochi","Uzochukwu","Uzoma","Yobachukwu","Yobanna","Zikoranaudodimma"];

	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.floor(Math.random() * nm1.length);
		if(tp === 1){
			rnd = Math.floor(Math.random() * nm2.length);
			names = nm2[rnd] + " " + nm1[rnd2];
			nm2.splice(rnd, 1);
		}else if(tp === 2){
			rnd = Math.floor(Math.random() * nm3.length);
			names = nm3[rnd] + " " + nm1[rnd2];
			nm3.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd] + " " + nm1[rnd2];
			nm1.splice(rnd, 1);
		}
		nm1.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}