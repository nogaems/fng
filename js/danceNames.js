var nm1 = ["Aeris","Aggi","Badger","Banty","Beast","Bibbot","Biddy","Big Beat","Birch","Bird","Blaze","Bleep","Bobble","Bounce","Bubble","Buffet","Bulldozer","Bungle","Champ","Changle","Chic","Chime","Chomp","Corkscrew","Crochet","Crowle","Crumble","Cuckoo","Cudge","Dart","Daydream","Dimpel","Dither","Divet","Doodle","Dove","Drub","Dynamo","Dynomite","Eags","Edge","Engage","Faddy","Fav","Fitter","Flinch","Flitter","Flogger","Flub","Folly","Freebie","Frump","Fuss","Gallop","Gambol","Garble","Ghost","Gliss","Glitch","Goad","Goose","Grind","Grizzle","Growl","Gyro","Hash","Hitch","Hotfoot","Hush","Ide","Jar","Jaral","Jerk","Jigger","Jiggle","Jiggle Jaggle","Jimjam","Jog","Joggle","Joggy","Joker","Jolly","Jostle","Jounce","Jumble","Jump Step","Kink","Klink","Lagger","Lambal","Lax","Leapfrog","Libble","Little Beat","Loon","Maggle","Magic","Manic","Mash","Mellow","Melo","Mirage","Mit","Mockingbird","Muddle","Nazzle","Nidge","Nittle","Nudge","Paddle","Pep 'n Punch","Pint","Pivot","Poch","Privy","Puff","Pulp","Pulse","Quake","Rane","Rass","Rubble","Sarge","Sault","Scant","Scouge","Scrunch","Sembla","Serk","Shamble","Shidder","Shifshof","Shift","Shift Shuffle","Shimsham","Siggy","Skippit","Skitter","Slapdash","Slither","Sliver","Snaff","Snap","Snapper","Snats","Snipsnap","Spark","Spigot","Spout","Spurrit","Squash","Squeek","Squish","Squish Squash","Staggle","Starlight Dance","Stip Step","Stir","Stragle","Streak","Stripstrap","Stritstrat","Surge","Swagger","Sway","Swerve","Swiggy","Swivel","Swivel 'n Swerve","Swoop","Tangle","Thrib","Thump","Thump 'n Stump","Thunder","Tirin","Toots","Totter","Trebble","Tribble","Trifle","Trimble","Triptrap","Trotter","Tweak","Twiddle","Twiddlefitch","Twilight","Twine","Twinkle Toes","Twitch","Twitter","Vex","Vice","Vigger","Vortex","Wade","Wallis","Waver","Whim","Whirl","Whisker","Whisper","Wicked","Widget","Wig","Wiggle","Wix","Wobble","Wraith","Yoke","Zigzag"]
var br = "";

function nameGen(){
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd = Math.floor(Math.random() * nm1.length);
		names = "The " + nm1[rnd];
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}