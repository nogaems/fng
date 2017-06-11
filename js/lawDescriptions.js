function nameGen(){
	var nm1 = ["local","federal","state","national","regional","international","provincial","territorial","community"];
	var nm2 = ["a hit and run","a run and hit","sucker punching","abandoning a child","abducting a minor","abusing a domestic pet","abusing financial trade secrets","abusing superpowers","abusing, killing or otherwise harming a royal animal","accidental arson","aggravated armed assault","aggravated assault","annoying prank calls","armed robbery","assassinations or assassination attempts","assault leading to serious or deadly injury","assault on a public official","assault with chemicals","assaulting a minor","attempting to or succeeding in bribing a betting official","attempting to or succeeding in bribing a government official","attempting to or succeeding in commercial bribery","battery","being a public nuisance","being intoxicated while working a government job","being part of a violent gang","being really, really annoying","being the leader of a violent gang","blackmailing","blackmailing a government official","body invasion","body snatching","breaking and entering","breaking or otherwise failing to uphold a contract","breaking, repairing and entering","brewing alcohol drinks without a license","bringing back a human being from the dead","burglary with explosives","buying or otherwise receiving stolen property","buying or possessing dangerous chemicals","buying or selling endangered animal parts","buying or selling slaves","carrying a concealed harmless weapon","carrying a concealed weapon","carrying a loaded weapon","carrying an unloaded weapon","carrying or possessing explosives without a license","carrying or possessing illegal substances","carrying or possessing illegal weapons","causing property damage while under the influence of substances","causing the death of a human being","causing the endangerment or extinction of an animal species","child neglect","committing any acts of public indecency","committing fraud","committing one or multiple acts of treason","committing an imperfect crime","committing the perfect crime","conspiring with the enemy","contempt of court","continuing to be a public nuisance","criminal negligence","defacing of public monuments","denying service based on race or gender","destroying crime scene evidence","destroying government documents","destroying, counterfeiting or otherwise altering official currency","disposing waste in public","domestic fighting","drinking in public in the morning","eavesdropping","eavesdropping on secret conversations","embezzlement","endangering a child","endangering a human life through careless actions","endangering human lives while under the influence of substances","engaging in any form of piracy","escaping imprisonment","evading a peace officer","evading justice by travelling in time","evading taxes","excessive littering","extorting a government official","extorting a minor","extortion","failing to control a dangerous animal","fake imprisonment","false imprisonment","fighting in public","forgery of documents","forgery of government documents","gambling fraud","grand theft auto","happy slapping","harboring enemies","harboring fugitives","harming an officer of the law in any way","home invasion","identity theft","inciting or attempting to incite a rebellion","inciting or participating in a riot","inciting public mayhem","insider trading","intentionally spreading a disease","invasion of privacy","kidnapping a child","kidnapping a human being","kidnapping an animal","killing another human being","lewd acts in public","littering","loitering","looting","looting during a disaster","looting during an emergency","love crimes","making somebody else commit a crime","manslaughter","manufacturing of illegal substances","manufacturing of weapons","manufacturing or selling fake IDs","marrying another human being under false pretenses","money laundering","mutilation","mutiny of any form","negligent acts that lead to the endangerment of lives","negligent animal abuse","negligent endangerment of a child","negligent homicide","negligently spreading a disease","not obeying a curfew","not providing employees with proper safety measures","operating machines, vehicles or other large objects while intoxicated","organizing or participating in animal fights","organizing or participating in fights to the death","owning or operating a chop shop","participating in an illegal strike or rally","participating in any way in human trafficking","participating in discrimination of any form","paying an employee below the minimum wage","paying an employee in anything but money","performing torture in any form","perverting the course of justice","petty theft","pickpocketing","plotting to kidnap a human being","plotting to murder a human being","plotting to overthrow the government","political slander","possessing a fake ID","practicing censorship","practicing espionage","practicing medicine without a license","pretending to be a ghost","pretending to be your evil twin","pretending to be your own twin","private disorderly conduct","providing false information to an officer of peace","public disorderly conduct","public drunkenness","public drunkenness in the morning","public indecency","purposely endangering a human life","race or gender based assaults","releasing animals in unsuitable habitats","releasing harmful substances in any form","reporting a fake crime","reporting a fake emergency","resisting arrest","selling or otherwise exchanging government secrets","setting up a contract under false pretenses","shooting or otherwise harming a messenger","shoplifting","sightseeing at a crime scene","smuggling any goods","smuggling illegal goods","smuggling wildlife","spreading propaganda","stalking","tampering with evidence","the abuse of animals, dead or alive,","the destruction of books","the destruction of crops","the destruction of private property","the destruction of public art","the miscarriage of justice","the obstruction of justice","the theft of big arms","the theft of corpses","the theft of lifestock","the theft of private property","the theft of small arms","theft of a public statue","threatening the destruction of property","threatening with murder","trading illegal goods","trafficking illegal substances","travelling back in time to alter the future for personal gain","trespassing on government property","trespassing on private property","unarmed robbery","unhappy slapping","unlawful removal or planting of flora","unlicensed animal hunting","unorganized gambling","using an animal not suitable to be used as a mount as a mount","vandalism of art","vandalism of public property","violently resisting arrest","arson"];
	var nm3 = ["a brief prison sentence","a high fine","a long term exile","a long term prison sentence","a low fine","a moderate fine","a moderate term exile","a moderate term prison sentence","a paddling","a short term exile","a short term prison sentence","a stern warning","a warning","an 'eye for an eye'","bodily harm","branding","brief public service","compensation to the victims in cash","compensation to the victims in servitude","execution","exile for life","imprisonment for life","incapacitation that prevent repeats of this crime","long term forced rehabilitation","long term public service","long term servitude","loss of civil privileges","medium term forced rehabilitation","long term solitary confinement","medium term solitary confinement","short term solitary confinement","moderate term public service","moderate term servitude","public humiliation","short term forced rehabilitation","short term public service","short term servitude","whatever the wheel of justice lands on"];
	
	var rnd1 = parseInt(Math.floor(Math.random() * nm1.length));
	var rnd2 = parseInt(Math.floor(Math.random() * nm2.length));
	var rnd3 = parseInt(Math.floor(Math.random() * nm3.length));
	var rnd4 = parseInt(Math.floor(Math.random() * nm1.length));
	var rnd5 = parseInt(Math.floor(Math.random() * nm2.length));
	var rnd6 = parseInt(Math.floor(Math.random() * nm3.length));
	var rnd7 = parseInt(Math.floor(Math.random() * nm1.length));
	var rnd8 = parseInt(Math.floor(Math.random() * nm2.length));
	var rnd9 = parseInt(Math.floor(Math.random() * nm3.length));
	var rnd10 = parseInt(Math.floor(Math.random() * nm1.length));
	var rnd11 = parseInt(Math.floor(Math.random() * nm2.length));
	var rnd12 = parseInt(Math.floor(Math.random() * nm3.length));
	var rnd13 = parseInt(Math.floor(Math.random() * nm1.length));
	var rnd14 = parseInt(Math.floor(Math.random() * nm2.length));
	var rnd15 = parseInt(Math.floor(Math.random() * nm3.length));
	
	var name = "This " + nm1[rnd1] + " law dictates all those found guilty of " + nm2[rnd2] + " will face the punishment of " + nm3[rnd3] + ".";
	var name2 = "----------------------------";
	var name3 = "This " + nm1[rnd4] + " law dictates all those found guilty of " + nm2[rnd5] + " will face the punishment of " + nm3[rnd6] + ".";
	var name4 = "----------------------------";
	var name5 = "This " + nm1[rnd7] + " law dictates all those found guilty of " + nm2[rnd8] + " will face the punishment of " + nm3[rnd9] + ".";
	var name6 = "----------------------------";
	var name7 = "This " + nm1[rnd10] + " law dictates all those found guilty of " + nm2[rnd11] + " will face the punishment of " + nm3[rnd12] + ".";
	var name8 = "----------------------------";
	var name9 = "This " + nm1[rnd13] + " law dictates all those found guilty of " + nm2[rnd14] + " will face the punishment of " + nm3[rnd15] + ".";
	
	var br = [];
	for(i = 0; i < 8; i++){
		br[i] = document.createElement('br');	
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}
	
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	element.appendChild(document.createTextNode(name));
	element.appendChild(br[0]);
	element.appendChild(document.createTextNode(name2));
	element.appendChild(br[1]);
	element.appendChild(document.createTextNode(name3));
	element.appendChild(br[2]);
	element.appendChild(document.createTextNode(name4));
	element.appendChild(br[3]);
	element.appendChild(document.createTextNode(name5));
	element.appendChild(br[4]);
	element.appendChild(document.createTextNode(name6));
	element.appendChild(br[5]);
	element.appendChild(document.createTextNode(name7));
	element.appendChild(br[6]);
	element.appendChild(document.createTextNode(name8));
	element.appendChild(br[7]);
	element.appendChild(document.createTextNode(name9));
	document.getElementById("placeholder").appendChild(element);
}	