__all__ = ['chineseNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'nm4', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Ah'), Js('An'), Js('Bai'), Js('Bao'), Js('Bo'), Js('Cai'), Js('Chang'), Js('Chao'), Js('Chen'), Js('Cheng'), Js('Chin'), Js('Chun'), Js('Da'), Js('De'), Js('Delan'), Js('Dong'), Js('Fang'), Js('Fen'), Js('Feng'), Js('Fu'), Js('Gang'), Js('Gengxin'), Js('Guanting'), Js('Guanyu'), Js('Guiying'), Js('Guo'), Js('Hai'), Js('Hanying'), Js('He'), Js('Heng'), Js('Hong'), Js('Hu'), Js('Hua'), Js('Huan'), Js('Huang'), Js('Hui'), Js('Huo'), Js('Jia'), Js('Jiahao'), Js('Jian'), Js('Jiang'), Js('Jianhong'), Js('Jie'), Js('Jin'), Js('Jing'), Js('Jingyi'), Js('Ju'), Js('Jun'), Js('Kang'), Js('Kun'), Js('Lan'), Js('Lei'), Js('Li'), Js('Liang'), Js('Lim'), Js('Lin'), Js('Ling'), Js('Lingxin'), Js('Liuxian'), Js('Long'), Js('Luoyang'), Js('Meng'), Js('Min'), Js('Ming'), Js('Mu'), Js('Ning'), Js('Peng'), Js('Ping'), Js('Qiang'), Js('Qigang'), Js('Qing'), Js('Qiu'), Js('Rong'), Js('Ru'), Js('Ruogang'), Js('Shi'), Js('Shui'), Js('Shun'), Js('Shuren'), Js('Song'), Js('Su'), Js('Tai'), Js('Tao'), Js('Tian'), Js('Tu'), Js('Wei'), Js('Wen'), Js('Wu'), Js('Wuhan'), Js('Wuying'), Js('Xia'), Js('Xiang'), Js('Xieren'), Js('Xinya'), Js('Xinyi'), Js('Xinyue'), Js('Xiuying'), Js('Xue'), Js('Xuefeng'), Js('Xuegang'), Js('Xun'), Js('Yahui'), Js('Yan'), Js('Yang'), Js('Yating'), Js('Yazhu'), Js('Yi'), Js('Yijun'), Js('Yimu'), Js('Yin'), Js('Yong'), Js('Yu'), Js('Yuhan'), Js('Yun'), Js('Zan'), Js('Zedong'), Js('Zemin'), Js('Zexi'), Js('Zexian'), Js('Zhelan'), Js('Zhen'), Js('ZhenKang'), Js('Zheng'), Js('Zhenya'), Js('Zhi'), Js('Zhihao'), Js('Zhong'), Js('Zhou')]))
    var.put('nm2', Js([Js('Ah'), Js('Ai'), Js('An'), Js('Bai'), Js('Bao'), Js('Bi'), Js('Bo'), Js('Cai'), Js('Chan'), Js('Chang'), Js('Chao'), Js('Chen'), Js('Cheng'), Js('Chin'), Js('Chun'), Js('Cui'), Js('Da'), Js('Dai'), Js('Dan'), Js('Delan'), Js('Fang'), Js('Fen'), Js('Feng'), Js('Fu'), Js('Gengxin'), Js('Guanting'), Js('Guanyu'), Js('Guiying'), Js('Guo'), Js('Hai'), Js('Hanying'), Js('He'), Js('Heng'), Js('Hong'), Js('Hua'), Js('Huan'), Js('Huang'), Js('Hui'), Js('Huo'), Js('Jia'), Js('Jian'), Js('Jiang'), Js('Jiao'), Js('Jie'), Js('Jin'), Js('Jing'), Js('Jingyi'), Js('Ju'), Js('Juan'), Js('Jun'), Js('Kun'), Js('Lan'), Js('Lei'), Js('Li'), Js('Lian'), Js('Lim'), Js('Lin'), Js('Ling'), Js('Lingxin'), Js('Liuxian'), Js('Luoyang'), Js('Mei'), Js('Min'), Js('Ming'), Js('My'), Js('Na'), Js('Ning'), Js('Nuan'), Js('Ping'), Js('Qigang'), Js('Qing'), Js('Qiu'), Js('Rong'), Js('Ru'), Js('Ruogang'), Js('Shi'), Js('Shu'), Js('Shufen'), Js('Shui'), Js('Shun'), Js('Shuren'), Js('Su'), Js('Tai'), Js('Tu'), Js('Wei'), Js('Wen'), Js('Wu'), Js('Wuhan'), Js('Wuying'), Js('Xia'), Js('Xiang'), Js('Xieren'), Js('Xinya'), Js('Xinyi'), Js('Xinyue'), Js('Xiu'), Js('Xiulan'), Js('Xiuying'), Js('Xuefeng'), Js('Xuegang'), Js('Xun'), Js('Ya'), Js('Yahui'), Js('Yaling'), Js('Yan'), Js('Yang'), Js('Yating'), Js('Yawen'), Js('Yazhu'), Js('Yi'), Js('Yijun'), Js('Yimu'), Js('Yong'), Js('Yu'), Js('Yuhan'), Js('Yun'), Js('Zan'), Js('Zedong'), Js('Zemin'), Js('Zexi'), Js('Zexian'), Js('Zhelan'), Js('Zhen'), Js('ZhenKang'), Js('Zheng'), Js('Zhenya'), Js('Zhi'), Js('Zhihao'), Js('Zhong'), Js('Zhou')]))
    var.put('nm3', Js([Js('Bai'), Js('Cai'), Js('Cao'), Js('Chang'), Js('Chen'), Js('Cheng'), Js('Cui'), Js('Dai'), Js('Deng'), Js('Ding'), Js('Dong'), Js('Du'), Js('Duan'), Js('Fan'), Js('Fang'), Js('Feng'), Js('Fu'), Js('Gao'), Js('Geng'), Js('Gong'), Js('Gu'), Js('Guo'), Js('Han'), Js('Hao'), Js('He'), Js('Hou'), Js('Hu'), Js('Huang'), Js('Huo'), Js('Jia'), Js('Jiang'), Js('Jin'), Js('Kang'), Js('Kong'), Js('Lai'), Js('Lang'), Js('Lei'), Js('Li'), Js('Lian'), Js('Liang'), Js('Liao'), Js('Lin'), Js('Liu'), Js('Long'), Js('Lu'), Js('Luo'), Js('Ma'), Js('Mao'), Js('Meng'), Js('Mo'), Js('Pan'), Js('Peng'), Js('Qian'), Js('Qiao'), Js('Qin'), Js('Qiu'), Js('Quan'), Js('Ren'), Js('Shao'), Js('Shen'), Js('Shi'), Js('Song'), Js('Su'), Js('Sun'), Js('Tan'), Js('Tang'), Js('Tao'), Js('Teng'), Js('Tian'), Js('Wan'), Js('Wang'), Js('Wei'), Js('Wen'), Js('Wu'), Js('Xia'), Js('Xian'), Js('Xiang'), Js('Xiao'), Js('Xie'), Js('Xing'), Js('Xiong'), Js('Xu'), Js('Xuan'), Js('Xue'), Js('Xun'), Js('Yan'), Js('Yang'), Js('Yao'), Js('Ye'), Js('Yi'), Js('Yin'), Js('Yu'), Js('Yuan'), Js('Zeng'), Js('Zhan'), Js('Zhang'), Js('Zhao'), Js('Zhen'), Js('Zheng'), Js('Zhong'), Js('Zhou'), Js('Zhu'), Js('Zhuan'), Js('Zi'), Js('Zou')]))
    var.put('nm4', Js([Js('Ah'), Js('An'), Js('Bai'), Js('Bao'), Js('Bo'), Js('Cai'), Js('Chang'), Js('Chao'), Js('Chen'), Js('Cheng'), Js('Chin'), Js('Chun'), Js('Da'), Js('De'), Js('Delan'), Js('Fang'), Js('Fen'), Js('Feng'), Js('Fu'), Js('Gengxin'), Js('Guanting'), Js('Guanyu'), Js('Guiying'), Js('Guo'), Js('Hai'), Js('Hanying'), Js('He'), Js('Heng'), Js('Hong'), Js('Hu'), Js('Hua'), Js('Huan'), Js('Huang'), Js('Hui'), Js('Huo'), Js('Jia'), Js('Jian'), Js('Jiang'), Js('Jie'), Js('Jin'), Js('Jing'), Js('Jingyi'), Js('Ju'), Js('Jun'), Js('Kang'), Js('Kun'), Js('Lan'), Js('Lei'), Js('Li'), Js('Liang'), Js('Lim'), Js('Lin'), Js('Ling'), Js('Lingxin'), Js('Liuxian'), Js('Long'), Js('Luoyang'), Js('Meng'), Js('Min'), Js('Ming'), Js('Mu'), Js('Ning'), Js('Peng'), Js('Ping'), Js('Qigang'), Js('Qing'), Js('Qiu'), Js('Rong'), Js('Ru'), Js('Ruogang'), Js('Shi'), Js('Shui'), Js('Shun'), Js('Shuren'), Js('Song'), Js('Su'), Js('Tai'), Js('Tian'), Js('Tu'), Js('Wei'), Js('Wen'), Js('Wu'), Js('Wuhan'), Js('Wuying'), Js('Xia'), Js('Xiang'), Js('Xieren'), Js('Xinya'), Js('Xinyi'), Js('Xinyue'), Js('Xiuying'), Js('Xue'), Js('Xuefeng'), Js('Xuegang'), Js('Xun'), Js('Yahui'), Js('Yan'), Js('Yang'), Js('Yating'), Js('Yazhu'), Js('Yi'), Js('Yijun'), Js('Yimu'), Js('Yin'), Js('Yong'), Js('Yu'), Js('Yuhan'), Js('Yun'), Js('Zan'), Js('Zedong'), Js('Zemin'), Js('Zexi'), Js('Zexian'), Js('Zhelan'), Js('Zhen'), Js('ZhenKang'), Js('Zheng'), Js('Zhenya'), Js('Zhi'), Js('Zhihao'), Js('Zhong'), Js('Zhou')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm3').get(var.get('rnd2'))+Js(' '))+var.get('nm2').get(var.get('rnd'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm3').get(var.get('rnd2'))+Js(' '))+var.get('nm4').get(var.get('rnd'))))
                    var.get('nm4').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm3').get(var.get('rnd2'))+Js(' '))+var.get('nm1').get(var.get('rnd'))))
                    var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
chineseNames = var.to_python()