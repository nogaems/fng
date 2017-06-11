
function nameGen(type){
	var nm1 = ["Ah","An","Bai","Bao","Bo","Cai","Chang","Chao","Chen","Cheng","Chin","Chun","Da","De","Delan","Dong","Fang","Fen","Feng","Fu","Gang","Gengxin","Guanting","Guanyu","Guiying","Guo","Hai","Hanying","He","Heng","Hong","Hu","Hua","Huan","Huang","Hui","Huo","Jia","Jiahao","Jian","Jiang","Jianhong","Jie","Jin","Jing","Jingyi","Ju","Jun","Kang","Kun","Lan","Lei","Li","Liang","Lim","Lin","Ling","Lingxin","Liuxian","Long","Luoyang","Meng","Min","Ming","Mu","Ning","Peng","Ping","Qiang","Qigang","Qing","Qiu","Rong","Ru","Ruogang","Shi","Shui","Shun","Shuren","Song","Su","Tai","Tao","Tian","Tu","Wei","Wen","Wu","Wuhan","Wuying","Xia","Xiang","Xieren","Xinya","Xinyi","Xinyue","Xiuying","Xue","Xuefeng","Xuegang","Xun","Yahui","Yan","Yang","Yating","Yazhu","Yi","Yijun","Yimu","Yin","Yong","Yu","Yuhan","Yun","Zan","Zedong","Zemin","Zexi","Zexian","Zhelan","Zhen","ZhenKang","Zheng","Zhenya","Zhi","Zhihao","Zhong","Zhou"];
	var nm2 = ["Ah","Ai","An","Bai","Bao","Bi","Bo","Cai","Chan","Chang","Chao","Chen","Cheng","Chin","Chun","Cui","Da","Dai","Dan","Delan","Fang","Fen","Feng","Fu","Gengxin","Guanting","Guanyu","Guiying","Guo","Hai","Hanying","He","Heng","Hong","Hua","Huan","Huang","Hui","Huo","Jia","Jian","Jiang","Jiao","Jie","Jin","Jing","Jingyi","Ju","Juan","Jun","Kun","Lan","Lei","Li","Lian","Lim","Lin","Ling","Lingxin","Liuxian","Luoyang","Mei","Min","Ming","My","Na","Ning","Nuan","Ping","Qigang","Qing","Qiu","Rong","Ru","Ruogang","Shi","Shu","Shufen","Shui","Shun","Shuren","Su","Tai","Tu","Wei","Wen","Wu","Wuhan","Wuying","Xia","Xiang","Xieren","Xinya","Xinyi","Xinyue","Xiu","Xiulan","Xiuying","Xuefeng","Xuegang","Xun","Ya","Yahui","Yaling","Yan","Yang","Yating","Yawen","Yazhu","Yi","Yijun","Yimu","Yong","Yu","Yuhan","Yun","Zan","Zedong","Zemin","Zexi","Zexian","Zhelan","Zhen","ZhenKang","Zheng","Zhenya","Zhi","Zhihao","Zhong","Zhou"];
	var nm3 = ["Bai","Cai","Cao","Chang","Chen","Cheng","Cui","Dai","Deng","Ding","Dong","Du","Duan","Fan","Fang","Feng","Fu","Gao","Geng","Gong","Gu","Guo","Han","Hao","He","Hou","Hu","Huang","Huo","Jia","Jiang","Jin","Kang","Kong","Lai","Lang","Lei","Li","Lian","Liang","Liao","Lin","Liu","Long","Lu","Luo","Ma","Mao","Meng","Mo","Pan","Peng","Qian","Qiao","Qin","Qiu","Quan","Ren","Shao","Shen","Shi","Song","Su","Sun","Tan","Tang","Tao","Teng","Tian","Wan","Wang","Wei","Wen","Wu","Xia","Xian","Xiang","Xiao","Xie","Xing","Xiong","Xu","Xuan","Xue","Xun","Yan","Yang","Yao","Ye","Yi","Yin","Yu","Yuan","Zeng","Zhan","Zhang","Zhao","Zhen","Zheng","Zhong","Zhou","Zhu","Zhuan","Zi","Zou"];
	var nm4 = ["Ah","An","Bai","Bao","Bo","Cai","Chang","Chao","Chen","Cheng","Chin","Chun","Da","De","Delan","Fang","Fen","Feng","Fu","Gengxin","Guanting","Guanyu","Guiying","Guo","Hai","Hanying","He","Heng","Hong","Hu","Hua","Huan","Huang","Hui","Huo","Jia","Jian","Jiang","Jie","Jin","Jing","Jingyi","Ju","Jun","Kang","Kun","Lan","Lei","Li","Liang","Lim","Lin","Ling","Lingxin","Liuxian","Long","Luoyang","Meng","Min","Ming","Mu","Ning","Peng","Ping","Qigang","Qing","Qiu","Rong","Ru","Ruogang","Shi","Shui","Shun","Shuren","Song","Su","Tai","Tian","Tu","Wei","Wen","Wu","Wuhan","Wuying","Xia","Xiang","Xieren","Xinya","Xinyi","Xinyue","Xiuying","Xue","Xuefeng","Xuegang","Xun","Yahui","Yan","Yang","Yating","Yazhu","Yi","Yijun","Yimu","Yin","Yong","Yu","Yuhan","Yun","Zan","Zedong","Zemin","Zexi","Zexian","Zhelan","Zhen","ZhenKang","Zheng","Zhenya","Zhi","Zhihao","Zhong","Zhou"];
	
	var br = "";

	$('#placeholder').css('textTransform', 'capitalize');
	var tp = type;
	var element = document.createElement("div");
	element.setAttribute("id", "result");
	
	for(i = 0; i < 10; i++){
		rnd2 = Math.random() * nm3.length | 0;
		if(tp === 1){
			rnd = Math.random() * nm2.length | 0;
			names = nm3[rnd2] + " " + nm2[rnd];
			nm2.splice(rnd, 1);
		}else if(tp === 2){
			rnd = Math.random() * nm4.length | 0;
			names = nm3[rnd2] + " " + nm4[rnd];
			nm4.splice(rnd, 1);
		}else{
			rnd = Math.random() * nm1.length | 0;
			names = nm3[rnd2] + " " + nm1[rnd];
			nm1.splice(rnd, 1);
		}
		nm3.splice(rnd2, 1);
		br = document.createElement('br');	
		element.appendChild(document.createTextNode(names));
		element.appendChild(br);
	}
	if(document.getElementById("result")){
		document.getElementById("placeholder").removeChild(document.getElementById("result"));
	}		
	document.getElementById("placeholder").appendChild(element);
}