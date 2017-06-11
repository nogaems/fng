function nameGen(){
	var nm1 = ["At last","Awake, warriors","Bathe in their blood","Behold our power","Blood for the blood god","Blood for the emperor","Bow before us","Bring it on","Bring me their guts","Bring me their heads","Bring me their teeth","Bring on the pain","Bring them to their knees","Burn","By our blade","By our blades you shall perish","By the power bestowed upon us","Chaos and anarchy","Charge","Charge forward","Come and get us","Cower before us","Cut them down","Death and glory","Death can wait no longer","Death comes tomorrow","Death to the enemy","Death to the weak","Destroy everything","Destroy everything in your path","Destroy them all","Die","Don't run, you're already dead","Eternally great","Feed them to the maggots","Feel our might","Fertilize these lands with their corpses","Fill them with regret","Fire at will","Follow me to glory","For blood and glory","For chaos","For gold and glory","For honor","For justice","For king and country","For our people","For the light","Forever as one","Forever unbroken","Freedom","Glory to us all","God watches over us","God's on our side","Here we come","In god's name","It's feeding time","Kill every last one of them","Kill them all, leave no-one standing","Kneel before our lord","Leave none alive","Leave nothing standing","Leave only ashes","Leave them with nothing","Let the crows feast tonight","Let them feel true pain","Let them meet our best","Let them meet their maker","Let them taste our blades","Let there be blood","Let's get to know who they are on the inside","Let's go","Let's taste their flesh","Let's teach them how it's done","Make them fear our name","Make them suffer","None shall remember them","Obliterate them from history","Once more","Our blades hunger","Our life for god","Our time has come","Our time is now","Paint the fields in their blood","Praise the people","Prepare for destruction","Prepare to die","Remove them from this Earth","Send them to their maker","Shine in the light","Spit on their corpses","Stand united","Strike true","Swift and savage","Take everything","Take no prisoners","Take them down","Take what is ours","Tear them down","Tear them to pieces","Thank you for your sacrifice","That one is mine","The end is here","The god of death demands its pay","They will remember","Time for a warm up","Time to have fun","Time to pay","To glory","To victory","Trample them beneath your feet","Turn them to ash","United under god","Until eternity","Victory or death","We are eternal","We are immortal","We are the apocalypse","We are the dead","We are the greatest","We are the reapers","We fight as one","We have arrived","We have awoken","We have risen","We never tire","We reign forever","We ride forever","We shall be remembered","We shall be victorious","We shall conquer all","We shall feast tonight","We stand together","We stand united","We will be victorious","We will never stop","We're not afraid","Wipe them from history","With me, as one","Witness our might","You belong to us now","You're already dead","Your souls are ours"];

	var br = "";
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 11; i++){
		if(i % 2 === 0){
			names = "--------";
		}else{
			rnd = Math.floor(Math.random() * nm1.length);
			names = nm1[rnd] + "!";
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