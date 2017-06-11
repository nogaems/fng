var nm1 = [["long","dragon"],["long","dragon"],["long","dragon"],["long","dragon"],["she","snake"],["shen","Sea monster"],["teng","Flying dragon"]];
var nm2 = [["bao","leopard"],["chong","pet"],["da","elephant"],["da","rat"],["die","father"],["duan","alligator"],["er","son"],["gou","dog"],["he","hippo"],["hei","chimp"],["hou","monkey"],["hu","fox"],["jie","sister"],["jing","whale"],["lang","wolf"],["lao","tiger"],["lie","hyena"],["lu","deer"],["ma","horse"],["mao","cat"],["mu","mother"],["nai","cow"],["niao","bird"],["qi","wife"],["shan","goat"],["she","snake"],["shi","lion"],["tu","rabbit"],["xi","rhino"],["xiao","mouse"],["xiong","bear"],["xiong","brother"],["xiong","panda"],["yang","sheep"],["ying","eagle"],["yu","fish"],["zufu","grandfather"],["zumu","grandmother"]];
var nm3 = [["an","quiet"],["an","shore"],["bai","white"],["bo","thin"],["cao","grass"],["chang","long"],["cheng","orange"],["da","big"],["dao","island"],["di","Earth"],["duan","short"],["fei","flying"],["fen","pink"],["guo","foreign"],["guo","orchard"],["hai","ocean"],["hai","sea"],["han","cold"],["hao","good"],["he","river"],["hei","black"],["hei","dark"],["hong","red"],["hou","thick"],["hu","lake"],["hua","flower"],["huan","slow"],["huang","yellow"],["hui","gray"],["jin","gold"],["ju","hurricane"],["kuan","wide"],["lan","blue"],["lao","old"],["li","maroon"],["lu","green"],["nian","young"],["pan","coiled"],["peng","friend"],["pu","waterfall"],["qian","light blue"],["qiang","powerful"],["qing","light"],["qiu","curling"],["re","hot"],["ruan","soft"],["ruo","weak"],["sen","forest"],["sha","desert"],["shan","mountain"],["shen","spirit"],["shu","tree"],["tai","sun"],["teng","soaring"],["tian","heavenly"],["tian","sky"],["wu","fog"],["xing","star"],["xuan","cliff"],["xue","snow"],["yao","herb"],["yin","silver"],["ying","hard"],["ying","responsive"],["yu","rain"],["yuan","garden"],["yun","cloud"],["zhai","narrow"],["zhang","husband"],["zhi","plant"],["zhong","heavy"],["zi","purple"]];
var nm4 = [["bei","back"],["fu","belly"],["geng","neck"],["huo","throat"],["jing","mind"],["lian","cheeks"],["lian","face"],["she","tongue"],["tou","head"],["wei","stomach"],["xin","heart"],["xiong","chest"],["ya","teeth"],["yan","eye"],["yan","throat"],["zui","mouth"]];
var br = "";

function nameGen(){
	$('#placeholder').css('textTransform', 'capitalize');
	var element = document.createElement("div");
	element.setAttribute("id", "result");

	for(i = 0; i < 10; i++){
		if(i < 3){
			rnd = Math.random() * nm2.length | 0;
			names = "Long" + nm2[rnd][0] + " (Dragon + " + nm2[rnd][1] + ")";
		}else if(i < 7){
			rnd = Math.random() * nm3.length | 0;
			rnd2 = Math.random() * nm1.length | 0;
			names = nm3[rnd][0] + nm1[rnd2][0] + " (" + nm3[rnd][1] + " + " + nm1[rnd2][1] + ")";
		}else{
			rnd = Math.random() * nm3.length | 0;
			rnd2 = Math.random() * nm4.length | 0;
			names = nm3[rnd][0] + nm4[rnd2][0] + " (" + nm3[rnd][1] + " + " + nm4[rnd2][1] + ")";
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