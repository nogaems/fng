var nm1 = ["Aaan","Aadt","Aaetpio","Aanaa","Aaodt","Aaoxaif","Aavan","Aavna","Aax","Abamo","Abaoz","Abmo","Aboz","Acar","Acca","Acmbicu","Acps","Acrar","Acuca","Acups","Aczinor","Adaeoet","Adi","Adire","Adnop","Adop","Adopa","Adota","Adre","Adta","Agb","Aglm","Agmlm","Ahaozpi","Aiaoai Oiiit","Aigra","Aira","Amox","Amsox","Ancro","Animotix","Anpiel","Anvaa","Apa","Apahr","Apdoce","Aphr","Aplst","Apm","Apst","Arizl","Arn","Arylic","Arzl","Ataad","Atdim","Ato","Avtotar","Baradiel","Barnabas","Bataivah","Bivhd","Brap","Brcn","Briap","Cadaamp","Camael","Castiel","Cms","Cnabr","Cnbr","Cpsa","Cpusa","Diari","Dimnt","Dimt","Diom","Diri","Dixom","Dmx","Dolop","Donpa","Doop","Dopa","Dtaa","Dtoaa","Dxagz","Dxgz","Eac","Eboza","Ecanus","Ecaop","Ecop","Edlprnaa","Ephra","Erg","Ern","Erubey","Erzla","Eutpa","Exarp","Exr","Faax","Fmnd","Gabriel","Galgalliel","Gbal","Gbeal","Glma","Glmma","Gmdnm","Habioro","Hbr","Hcnbr","Hcoma","Hipotga","Hraap","Hrap","Hroan","Hru","Htmorda","Hua","Hxgzd","Iczhihal","Imntd","Imtd","Izaz","Izinr","Izixp","Iznr","Izraz","Izxp","Kokabiel","Lairz","Lang","Laoaxrp","Larz","Lavavoth","Leaoc","Leoc","Levanael","Ligdisa","Lmag","Lmmag","Lsraphm","Masgm","Mgam","Michael","Miz","Mma","Msal","Msmal","Mtdi","Mtndi","Mto","Naaa","Nanta","Naoo","Naooo","Navaa","Nbarc","Nbrc","Ndazn","Ndzn","Nhdd","Nhodd","Nlirx","Nlrx","Npat","Nrcoa","Nroa","Oacnr","Oanr","Oap","Obgota Aabco","Ocnm","Omagg","Omgg","Omia","Omsia","Ona","Onh","Onp","Oodpz","Oopz","Opad","Opama","Opamn","Ophaniel","Opmn","Opna","Opnad","Ormn","Oro Ibah Aozpi","Orpmn","Otoi","Otroi","Oyaub","Oyub","Ozaab","Ozab","Paco","Pado","Paeoc","Paico","Piz","Pmagl","Pmox","Pmzox","Ppsac","Raagiosl","Raph","Raphael","Rbnh","Rbznh","Rcanb","Rcnb","Rda","Rgan","Rgoan","Rlemu","Rlmu","Rpa","Rrb","Rrl","Rsi","Rsni","Rsoni","Ruoi","Ruroi","Rxao","Rxinl","Rxnl","Rxp","Rxpao","Rzila","Rzionr Nrzfm","Rzla","Saaiz","Sacp","Saiinou","Saiinov","Saucp","Scmio","Shonda","Siosp","Sisp","Slgaiol","Soniznt","Tdim","Tdnim","Tpau","Tplau","Uriel","Uspsn","Ussn","Utipa","Utpa","Uvb","Vaasa","Vasa","Volxdo Sioda","Xai","Xcz","Xdz","Xgazd","Xgzd","Xii","Xnilr","Xom","Xoy","Xpa","Xpaxn","Xpcn","Xrinh","Xrnh","Xxan","Yasen","Zaabo","Zabo","Zarnaah","Zarzi","Zarzilg","Zazi","Zdaxg","Zdxg","Zedekiel","Zinggen","Ziracah","Zirz","Ziza","Zurchol"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = nm1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}