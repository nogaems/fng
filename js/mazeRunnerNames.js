function nameGen(type){
	var nm1 = ["Abu","Ahm","Al","Albert","Albis","Alby","Aldo","Alex","Alexander","Alf","Alfred","Andre","Antony","Arb","Archi","Aris","Arnold","Art","Arthur","August","Augustus","Bell","Ben","Benji","Bernard","Bernie","Bert","Bill","Billy","Boyle","Brian","Buns","Bunsen","Carl","Carson","Cav","Caven","Charles","Charlie","Chris","Christian","Clarence","Clark","Claude","Cloud","Clyde","Coper","Dalton","Dave","David","Davy","Ed","Eddie","Edwin","Ernest","Erwin","Farad","Ford","Francis","Frank","Franklin","Fred","Freddie","Frederick","Gale","George","Georgey","Gibbs","Glenn","Graham","Gray","Greg","Harold","Harvey","Hawk","Henry","Hodgkin","Hooke","Hops","Hubble","Hubs","Isaac","Isic","Ivan","Jack","James","Jamie","John","Johnie","Jules","Julian","Karl","Ken","Leo","Leonard","Locke","Luis","Luther","Marcello","Mario","Max","Mendel","Mich","Michael","Mike","Mikey","Mitchell","Morgan","Murray","Neil","Newt","Nick","Nobel","Nobs","Otto","Paul","Percy","Pete","Peter","Quimby","Raman","Ramon","Ramsay","Randy","Rob","Robbie","Robert","Ron","Ronald","Ross","Russ","Russel","Sal","Sheldon","Shin","Siggie","Simon","Smith","Stephen","Steven","Sven","Teller","Theo","Theodor","Thom","Thomas","Thommie","Tim","Timmy","Timothy","Tom","Tommie","Tyson","Vince","Volt","Wallace","Wallie","Wally","Walt","Walter","Watson","Wilhelm","Will","Willard","Willia","Wolf"];
	var nm2 = ["Ada","Aga","Age","Aggie","Agnes","Alex","Alexis","Alva","Ana","Anaxi","Andie","Andrea","Angel","Anni","Ava","Avi","Babs","Barba","Barbara","Barbs","Bea","Beatrix","Beckie","Belle","Beth","Bethe","Binet","Birdie","Blaise","Bri","Bria","Carla","Carol","Celsie","Charlie","Christy","Clarence","Cori","Dana","Diana","Dorothy","Eliza","Elizabeth","Elli","Em","Emile","Emmy","Eva","Evangeline","Gale","Georgie","Gertrude","Gerty","Gibbs","Grace","Gracy","Haley","Halley","Hally","Harriet","Illy","Inge","Irene","Iva","Jackie","Jane","Jean","Jenny","Joce","Jocelyn","Joyce","Kat","Kath","Katharine","Kristi","Lace","Lea","Lela","Leona","Libby","Lina","Lisa","Lise","Louise","Love","Lucy","Lye","Lynn","Mae","Maria","Marie","Mary","May","Michel","Moli","Nea","Neila","Nikol","Nikola","Noa","Nobs","Pascal","Paula","Pearl","Rachel","Rene","Renee","Rita","Rosalin","Ruth","Sally","Shelly","Sherri","Sherry","Siggy","Simone","Sommer","Steph","Stephanie","Thabita","Thea","Theador","Theodore","Theresa","Torri","Trix","Trixie","Willy","Zora"];
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