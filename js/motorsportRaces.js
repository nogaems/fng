
function nameGen(){
	var nm1 = ["Annual","Arctic","International","Acclaimed","Accomplished","Adamant","Advanced","Extreme","Bold","Classic","Creative","Dynamic","Economic","Exalted","Exclusive","Fearless","Fierce","First","General","Golden","Grand","Great","Long","National","Velvet","Nocturnal","Nimble","Obsidian","Jade","Sapphire","Oceanic","Original","Parallel","Prime","Premium","Radiant","Rapid","Swift","Silver","Silk","Sanguine","Crimson","Super","Supreme","Twin","Ultimate","Ultra","Ivory","Sapphire","Emerald","Ruby","Ebon","Wild","Solar","Lunar"];
	var nm2 = ["Achiever","Ambition","Aspect","Audience","Basin","Beach","Beast","Border","Bridge","Capital","Celebration","Challenge","Classic","Cloud","Coast","Cold","Community","Creation","Creator","Crew","Crown","Desert","Diamond","District","Divide","Downtown","Dream","Earth","Enhancement","Experience","Field","Foundation","Freedom","Harbor","Hill","Holiday","Honor","Impulse","Independence","Intelligence","Invention","Island","Liberty","Marsh","Member","Mirror","Sunset","Sunrise","Mobile","Monument","Motion","Mountain","Movement","Network","Night","Opportunity","Passage","Patriot","Performance","Perseverance","Pinnacle","Revolution","Specialist","Swamp","Territory","Thrill","Thunder","Tradition","Trail","Victory","Voyage","Wilderness"];
	var nm3 = ["Acclaimed","Accomplished","Achiever","Adamant","Advanced","Ambition","Annual","Arctic","Aspect","Audience","Basin","Beach","Beast","Bold","Border","Bridge","Capital","Celebration","Challenge","Classic","Cloud","Coast","Cold","Community","Creation","Creative","Creator","Crew","Crimson","Crown","Desert","Diamond","District","Divide","Downtown","Dream","Dynamic","Earth","Ebon","Economic","Emerald","Enhancement","Exalted","Exclusive","Experience","Extreme","Fearless","Field","Fierce","First","Foundation","Freedom","General","Golden","Grand","Great","Harbor","Hill","Holiday","Honor","Impulse","Independence","Intelligence","International","Invention","Island","Ivory","Jade","Liberty","Long","Lunar","Marsh","Member","Mirror","Mobile","Monument","Motion","Mountain","Movement","National","Network","Night","Nimble","Nocturnal","Obsidian","Oceanic","Opportunity","Original","Parallel","Passage","Patriot","Performance","Perseverance","Pinnacle","Premium","Prime","Radiant","Rapid","Revolution","Ruby","Sanguine","Sapphire","Silk","Silver","Solar","Specialist","Sunrise","Sunset","Super","Supreme","Swamp","Swift","Territory","Thrill","Thunder","Tradition","Trail","Twin","Ultimate","Ultra","Velvet","Victory","Voyage","Wild","Wilderness"];
	var nm4 = ["All Star","All Stars","Climb","Cross","Drag","Drag Race","Dragster","Drift","Drifter","Drifting","Elite","Endurance","Formula","Full Throttle","Hill","Hill Climb","Hot Rod","Kart","Legacy","Mini","Miniature","Modified","Motorcross","Off Road","Off-Road","Outlaw","Performance","Pro","Production Car","Rally","Rallycross","Road Racing","Speed","Speedway","Sports","Sportscar","Spring Car","Sprint","Stock","Stock Car","Superbike","Supercar","Supercross","Superkart","Supermodified","Superstar","Touring","Touring Car","Velocity"];
	var nm5 = ["Champion Series","Championship","Championship Series","Cup","Formula Masters","Junior Championship","Juniors","League","Masters","Pro Series","Racing Series","Series","Superleague","World Championship","World Series"];
	
	var br = "";

	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd4 = Math.floor(Math.random() * nm4.length);
		rnd5 = Math.floor(Math.random() * nm5.length);
		if(i < 3){
			names = "The " + nm4[rnd4] + " " + nm5[rnd5];
		}else if(i < 6){
			rnd = Math.floor(Math.random() * nm1.length);
			names = "The " + nm1[rnd] + " " + nm4[rnd4] + " " + nm5[rnd5]
			nm1.splice(rnd, 1);
		}else if(i < 8){
			rnd = Math.floor(Math.random() * nm3.length);
			names = "The " + nm3[rnd] + " " + nm4[rnd4] + " " + nm5[rnd5]
			nm3.splice(rnd, 1);
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			rnd2 = Math.floor(Math.random() * nm2.length);
			while(nm1[rnd] === nm2[rnd2]){
				rnd2 = Math.floor(Math.random() * nm2.length);
			}
			names = "The " + nm1[rnd] + " " + nm2[rnd2] + " " + nm4[rnd4] + " " + nm5[rnd5]
			nm1.splice(rnd, 1);
			nm2.splice(rnd2, 1);
		}
		nm4.splice(rnd4, 1);
		nm5.splice(rnd5, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}