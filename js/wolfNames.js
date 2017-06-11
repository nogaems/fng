var nm1 = ["Ace","Akira","Alistair","Alpha","Apache","Apollo","Archer","Artemis","Astro","Athene","Atlas","Avalanche","Axis","Bandit","Bane","Baron","Beacon","Bear","Blaze","Blitz","Bolt","Bones","Boomer","Boon","Booth","Boulder","Brawn","Brick","Brock","Browne","Bruno","Brutus","Buck","Bud","Buddy","Bullet","Buster","Butch","Buzz","Caesar","Camelot","Chase","Chewy","Chronos","Cloud","Colt","Comet","Conan","Courage","Dagger","Dane","Danger","Dash","Delta","Dexter","Diablo","Digger","Drake","Duke","Dust","Dutch","Echo","Edge","Excalibur","Fang","Farkas","Flash","Frost","Fury","Ghost","Goliath","Gray","Grunt","Hannibal","Havoc","Hawke","Hawkeye","Hector","Hercules","Hooch","Hulk","Hunter","Hyde","Ice","Jaws","Jax","Jeckyll","Jethro","Judge","Kaine","Kane","Khan","Killer","King","Lad","Laika","Lecter","Lightning","Logan","Loki","Lupin","Lupus","Magnus","Mako","Mason","Maverick","Max","Maximus","Mayhem","Menace","Midnight","Miles","Murdoch","Myst","Nanook","Nero","Nightmare","Nova","Oak","Obsidian","Odin","Omega","Omen","Onyx","Orbit","Outlaw","Patriot","Phantom","Prince","Pyro","Quicksilver","Rage","Ralph","Ranger","Razor","Rebel","Rex","Rider","Riggs","Ripley","Riptide","Rogue","Rover","Scar","Scout","Shade","Shadow","Shepherd","Shredder","Silver","Skye","Slate","Sly","Smoke","Splinter","Steele","Storm","Striker","Summit","Tank","Thor","Thunder","Timber","Titan","Tooth","Trace","Trapper","Trouble","Tundra","Vapor","Whisper","Wolf"];
var nm2 = ["Acadia","Aiyana","Akita","Alaska","Alexia","Alexis","Alize","Alpine","Amber","Amethyst","Angel","Ares","Ari","Aspen","Astral","Athena","Atilla","Aura","Aurora","Avril","Babe","Banshee","Beauty","Blaze","Blitz","Blitzen","Blossom","Bo","Boone","Breeze","Charm","Chronis","Clarity","Cleo","Codex","Coral","Crystal","Dakota","Dash","Dawn","Delphi","Destiny","Dharma","Diva","Dodger","Dot","Duchess","Ebony","Echo","Eclipse","Enigma","Faith","Fern","Gemini","Gia","Girl","Grace","Hailey","Heather","Heaven","Helen","Hope","Ice","Indigo","Iris","Ivory","Ivy","Jade","Jasmine","Jewel","Jinx","June","Juno","Justice","Jynx","Karma","Kenya","Lady","Laika","Levi","Lexis","Liberty","Lore","Lotus","Luna","Maple","Maxima","Meadow","Mello","Melody","Mercy","Midnight","Mona","Moone","Myst","Mysti","Mystique","Myth","Nanook","Nova","Nymph","Nyx","Omen","Onyxia","Opal","Oracle","Pandora","Paws","Pearl","Pepper","Phantom","Phoenix","Precious","Princess","Pyro","Queen","Rags","Raine","Raven","Rogue","Sable","Saffron","Sapphire","Satin","Scarlet","Shade","Shadow","Silver","Snow","Snowball","Snowflake","Solstice","Star","Twilight","Vapor","Velvet","Violet","Vixen","Whisper","Willow","Winter","Xena","Zelda"];
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