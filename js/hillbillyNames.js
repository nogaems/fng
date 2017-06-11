var nm1 = ["Abel","Abner","Ace","Amos","Arlo","Austin","Barney","Bart","Beau","Billy","Billy Bob","Billy Ray","Blue","Bo","Bob","Bobby Joe","Bodean","Bryar","Bubba","Bubba Blue","Buck","Buckley","Bud","Buddy","Burl","Cal","Carson","Casey","Charles Ray","Charlton","Chester","Cleavon","Cleetus","Clem","Cleon","Cletus","Clifton","Clint","Clyde","Cody","Cooper","Cooter","Coy","Cy","Cyrus","Dale","Darrel","Darryl","Delmont","Doc","Don","Donny","Duane","Duke","Dwayne","Earl","Eli","Elmer","Elrod","Enos","Eustice","Floyd","Floyd William","Ford","Forrest","Garth","George","Gomer","Gus","Harlan","Harley","Homer","Horace","Houston","Hoyt","Huckleberry","Ike","Jackson","Jasper","Jeb","Jed","Jefferson","Jerry Lee","Jessie","Jethro","Jim Bob","Jimmy Don","Jimmy James","Joe Bob","John Boy","Junior","Lee","Leewon","Lem","Lenny","Lester","Lloyd","Lonnie","Luke","Lum","Luther","Lynn","Merle","Mose","Orville","Otis","Ottis","Pervis","Quentin","Randy","Ray","Ray Nathan","Ray-Nathan","Rebel","Reuben","Ricky","Robbie","Rocky","Roscoe","Rowan","Roy","Rufus","Rusty","Scooter","Sherman","Silas","Skeeter","Spencer","Tommy","Tommy Lee","Trigger","Tyler","Verne","Vinton","Virgil","Wade","Wayne","Wilbur","Wilfred","Willie","Winchester","Winslow","Woody","Wyatt","Zeb","Zed","Zeke"];
var nm2 = ["Aleigh","Amaleen","Amber","Amberly","Angel","Annabelle","Audrey-Anne","Avalon","Bailie","Bambi","Baylee","Baylee-Ann","Bayleigh","Belle","Betty Jo","Betty Lou","Betty Sue","Billie Jean","Billy Jo","Bobbi Jo","Bobbie Sue","Bobby Jean","Bobby Jo","Brandine","Brandyne","Breanna","Breannona","Brittney-Anne","Buffy","Cambria","Candy","Charity","Chastity","Cherry","Claudette","Claudine","Crystal","Cyndi Beth","Dakota","Dale","Debbie","Delilah","Desiree","Destiny","Diamond","Earlene","Ellie Mae","Erin","Erneshia","Eva Jo","Faylene","Gracelyn","Gretchen","Harmony","Hattie","January","Jasmynn Mae","Jaylnn Jo","Jaylyne","Jaylynne","Jazlean","Jazzinelle","Jazznellie","Jerleecia","Jicelle","JoLener","Jolene","Joy","Jozelle","Kandy","Larlene","Layla","Leanne","Lexus","Lilah","Linda Sue","Lindieanne","Loriabelle","Loribelle","Lynndie","Maddison","Maddy","Mandy-Lynn","Martha Mae","Mary Beth","Mary Ellen","Mary Jane","Mary Jo","Mary Lou","Melody","Mercadies","Misty","Misty Dawn","Naomi","Natasha","Norma","Nyla","Nylette","Patty Sue","Peach","Pegg","Peggy Sue","Porsha","Pristine","Randa Lynn","Randee Leigh","Raylene","Roxxy","Roxxy-Lynn","Ruby Jane","Sammie Jo","Sandy","Savannah Jean","September","Shanamarie","Shaney","Sharlexia","Shayla","Shayna","Sheena","Shelby","Shirlene","Shorna","Sienna","Sierra","Stasha","Sue Ellen","Sunny","Tabitha","Tammie","Tasha","Tierra","Tiffany","Trista-Lynn","Trixie","Trixiebelle","Vanity","Vicki Lynn","Vienna","Waynelle","Willa","Wilma"];
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