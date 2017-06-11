var nm1 = ["All As One","Amazing Grace","Angel Eyes","Angel's Haven","Angel's Palace","Angelwing","Apple Blossom","Arms of Love","Aurora","Big Buddies","Big Companions","Big Heart","Blossoms","Bluebird","Boy's Town","Bright Horizons","Bright Sides","Building Blocks","Bumble Bee","Butterfly","Cherish","Children of the World","Children's Garden","Comfort Zone","Companions","Cradle of Love","Cradles","Crystal Fountain","Crystal Tree","Darlings","Daybreak","Daydream","Daydreams","Destiny Gardens","Dreamland","Eagle's Nest","Early Rise","Eden","Eternal Sunshine","Family Circle","Fellowship","First Light","Fountain of Life","Fountain of Youth","Fresh Hope","Friendship","Future Happiness","Generous Lives","Genesis","Girl's Town","Grace","Grand Tree","Green Fields","Guardian Angel","Guardian's Garden","Guidance","Halo","Hand in Hand","Happy Days","Happy Hearts","Happy Hill","Happy Home","Happy Mountain","Harmony","Heaven's","Helping Hand","Helping Hands","Home of Peace","Home of the Good","Honey Drop","Hope Springs","Hope Town","Horizon","Humble Bee","Inceptions","Innocence","Junior Angel","Kids Kingdom","Kindred Hearts","Kindred Souls","Kindred Spirits","Laughing Souls","Leg Up","Legacy","Lighthouse","Lily","Lilypad","Little Angel","Little Beginnings","Little Bugs","Little Champions","Little Darlings","Little Delights","Little Dreams","Little Friends","Little Garden","Little Lamb","Little Miracles","Little Palace","Little Petals","Little River","Little Rock","Little Stars","Little Steps","Little Talents","Little Town","Little Treasures","Little Voices","Little Wanderer's","Little Whispers","Littlest Angels","Littlewood","Living Water","Lotus","Lotus Children","Lullaby","Mercy Home","Mini Miracles","Mission of Hope","Mission of Love","Morning Star","Mother Goose","New Beginnings","New Connections","New Dawn","New Haven","New Heritage","New Hope","New Horizons","New Life","New Prospects","New Vision","North Star","Nourish and Flourish","One Heart","Open Doorways","Open Heart","Over the Rainbow","Paradise","Peace Blossoms","Phoenix","Piggyback","Playground","Precious Child","Precious Gems","Precious Home","Prospects","Radiance","Radiant Futures","Rainbow Children","Rainbow Flowers","Rascals","Rays of Life","Renaissance","Robin's Nest","Rose Petals","Rugrats","Sacred Heart","Safe Harbor","Serenity","Shepherd","Shepherd's Home","Silver Oak","Skyreach","Small Miracles","Small Steps","Smiles","Starlight","Step by Step","Stepping Stones","Story Time","Strong Desires","Strong Foundations","Sugerplum","Sunflower","Sunrise","Sweet Children","Sweethearts","Tiny Toes","Tranquil Garden","Transformation","Tree of Life","Treetops","Trinity","Under the Sun","United Voices","United We Stand","Voices of Children","Warm Hearts","Warm Home","We Care","White Lilly","White Orchid","White Tulip","White Warden","White Willow","Wings of Angels","Wings of Love","Wings of Refuge","Zion"];
var nm2 = ["Orphanage","Orphan Home","Home"];
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		rnd2 = Math.floor(Math.random() * nm2.length);
		names = nm1[rnd] + " " + nm2[rnd2];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}