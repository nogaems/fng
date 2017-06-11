__all__ = ['chineseDragons']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', ((((Js('Long')+var.get('nm2').get(var.get('rnd')).get('0'))+Js(' (Dragon + '))+var.get('nm2').get(var.get('rnd')).get('1'))+Js(')')))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('names', ((((((var.get('nm3').get(var.get('rnd')).get('0')+var.get('nm1').get(var.get('rnd2')).get('0'))+Js(' ('))+var.get('nm3').get(var.get('rnd')).get('1'))+Js(' + '))+var.get('nm1').get(var.get('rnd2')).get('1'))+Js(')')))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('names', ((((((var.get('nm3').get(var.get('rnd')).get('0')+var.get('nm4').get(var.get('rnd2')).get('0'))+Js(' ('))+var.get('nm3').get(var.get('rnd')).get('1'))+Js(' + '))+var.get('nm4').get(var.get('rnd2')).get('1'))+Js(')')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js([Js('long'), Js('dragon')]), Js([Js('long'), Js('dragon')]), Js([Js('long'), Js('dragon')]), Js([Js('long'), Js('dragon')]), Js([Js('she'), Js('snake')]), Js([Js('shen'), Js('Sea monster')]), Js([Js('teng'), Js('Flying dragon')])]))
var.put('nm2', Js([Js([Js('bao'), Js('leopard')]), Js([Js('chong'), Js('pet')]), Js([Js('da'), Js('elephant')]), Js([Js('da'), Js('rat')]), Js([Js('die'), Js('father')]), Js([Js('duan'), Js('alligator')]), Js([Js('er'), Js('son')]), Js([Js('gou'), Js('dog')]), Js([Js('he'), Js('hippo')]), Js([Js('hei'), Js('chimp')]), Js([Js('hou'), Js('monkey')]), Js([Js('hu'), Js('fox')]), Js([Js('jie'), Js('sister')]), Js([Js('jing'), Js('whale')]), Js([Js('lang'), Js('wolf')]), Js([Js('lao'), Js('tiger')]), Js([Js('lie'), Js('hyena')]), Js([Js('lu'), Js('deer')]), Js([Js('ma'), Js('horse')]), Js([Js('mao'), Js('cat')]), Js([Js('mu'), Js('mother')]), Js([Js('nai'), Js('cow')]), Js([Js('niao'), Js('bird')]), Js([Js('qi'), Js('wife')]), Js([Js('shan'), Js('goat')]), Js([Js('she'), Js('snake')]), Js([Js('shi'), Js('lion')]), Js([Js('tu'), Js('rabbit')]), Js([Js('xi'), Js('rhino')]), Js([Js('xiao'), Js('mouse')]), Js([Js('xiong'), Js('bear')]), Js([Js('xiong'), Js('brother')]), Js([Js('xiong'), Js('panda')]), Js([Js('yang'), Js('sheep')]), Js([Js('ying'), Js('eagle')]), Js([Js('yu'), Js('fish')]), Js([Js('zufu'), Js('grandfather')]), Js([Js('zumu'), Js('grandmother')])]))
var.put('nm3', Js([Js([Js('an'), Js('quiet')]), Js([Js('an'), Js('shore')]), Js([Js('bai'), Js('white')]), Js([Js('bo'), Js('thin')]), Js([Js('cao'), Js('grass')]), Js([Js('chang'), Js('long')]), Js([Js('cheng'), Js('orange')]), Js([Js('da'), Js('big')]), Js([Js('dao'), Js('island')]), Js([Js('di'), Js('Earth')]), Js([Js('duan'), Js('short')]), Js([Js('fei'), Js('flying')]), Js([Js('fen'), Js('pink')]), Js([Js('guo'), Js('foreign')]), Js([Js('guo'), Js('orchard')]), Js([Js('hai'), Js('ocean')]), Js([Js('hai'), Js('sea')]), Js([Js('han'), Js('cold')]), Js([Js('hao'), Js('good')]), Js([Js('he'), Js('river')]), Js([Js('hei'), Js('black')]), Js([Js('hei'), Js('dark')]), Js([Js('hong'), Js('red')]), Js([Js('hou'), Js('thick')]), Js([Js('hu'), Js('lake')]), Js([Js('hua'), Js('flower')]), Js([Js('huan'), Js('slow')]), Js([Js('huang'), Js('yellow')]), Js([Js('hui'), Js('gray')]), Js([Js('jin'), Js('gold')]), Js([Js('ju'), Js('hurricane')]), Js([Js('kuan'), Js('wide')]), Js([Js('lan'), Js('blue')]), Js([Js('lao'), Js('old')]), Js([Js('li'), Js('maroon')]), Js([Js('lu'), Js('green')]), Js([Js('nian'), Js('young')]), Js([Js('pan'), Js('coiled')]), Js([Js('peng'), Js('friend')]), Js([Js('pu'), Js('waterfall')]), Js([Js('qian'), Js('light blue')]), Js([Js('qiang'), Js('powerful')]), Js([Js('qing'), Js('light')]), Js([Js('qiu'), Js('curling')]), Js([Js('re'), Js('hot')]), Js([Js('ruan'), Js('soft')]), Js([Js('ruo'), Js('weak')]), Js([Js('sen'), Js('forest')]), Js([Js('sha'), Js('desert')]), Js([Js('shan'), Js('mountain')]), Js([Js('shen'), Js('spirit')]), Js([Js('shu'), Js('tree')]), Js([Js('tai'), Js('sun')]), Js([Js('teng'), Js('soaring')]), Js([Js('tian'), Js('heavenly')]), Js([Js('tian'), Js('sky')]), Js([Js('wu'), Js('fog')]), Js([Js('xing'), Js('star')]), Js([Js('xuan'), Js('cliff')]), Js([Js('xue'), Js('snow')]), Js([Js('yao'), Js('herb')]), Js([Js('yin'), Js('silver')]), Js([Js('ying'), Js('hard')]), Js([Js('ying'), Js('responsive')]), Js([Js('yu'), Js('rain')]), Js([Js('yuan'), Js('garden')]), Js([Js('yun'), Js('cloud')]), Js([Js('zhai'), Js('narrow')]), Js([Js('zhang'), Js('husband')]), Js([Js('zhi'), Js('plant')]), Js([Js('zhong'), Js('heavy')]), Js([Js('zi'), Js('purple')])]))
var.put('nm4', Js([Js([Js('bei'), Js('back')]), Js([Js('fu'), Js('belly')]), Js([Js('geng'), Js('neck')]), Js([Js('huo'), Js('throat')]), Js([Js('jing'), Js('mind')]), Js([Js('lian'), Js('cheeks')]), Js([Js('lian'), Js('face')]), Js([Js('she'), Js('tongue')]), Js([Js('tou'), Js('head')]), Js([Js('wei'), Js('stomach')]), Js([Js('xin'), Js('heart')]), Js([Js('xiong'), Js('chest')]), Js([Js('ya'), Js('teeth')]), Js([Js('yan'), Js('eye')]), Js([Js('yan'), Js('throat')]), Js([Js('zui'), Js('mouth')])]))
pass
pass


# Add lib to the module scope
chineseDragons = var.to_python()