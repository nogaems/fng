__all__ = ['dndBeholders']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nameMas', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
    if (var.get('i')<Js(2.0)):
        while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
        var.put('nMs', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3'))))
    else:
        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
        if (var.get('i')<Js(6.0)):
            while (PyJsStrictEq(var.get('nm3').get(var.get('rnd4')),var.get('nm1').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd4')),var.get('nm7').get(var.get('rnd3')))):
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            var.put('nMs', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd3'))))
        else:
            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
            if (var.get('i')<Js(9.0)):
                while (PyJsStrictEq(var.get('nm5').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd4'))) or PyJsStrictEq(var.get('nm5').get(var.get('rnd6')),var.get('nm7').get(var.get('rnd3')))):
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('nMs', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd3'))))
            else:
                var.put('rnd8', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('rnd9', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm5').get(var.get('rnd8')),var.get('nm5').get(var.get('rnd6'))):
                    var.put('rnd8', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('nMs', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd9'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameMas_.func_name = 'nameMas'
var.put('nameMas', PyJsHoisted_nameMas_)
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.get('nameMas')()
            while PyJsStrictEq(var.get('nMs'),Js('')):
                var.get('nameMas')()
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('d'), Js('dh'), Js('f'), Js('g'), Js('gh'), Js('j'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('q'), Js('qh'), Js('r'), Js('s'), Js('th'), Js('v'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('aa'), Js('oa'), Js('ua'), Js('ia'), Js('au'), Js('ao'), Js('ou')]))
var.put('nm3', Js([Js('d'), Js('dd'), Js('dr'), Js('dl'), Js('dh'), Js('dtr'), Js('dthr'), Js('g'), Js('gh'), Js('gth'), Js('k'), Js('kk'), Js('kh'), Js('kht'), Js('l'), Js('ld'), Js('ldr'), Js('lb'), Js('lbr'), Js('lm'), Js('ln'), Js('ls'), Js('lsh'), Js('lth'), Js('lthdr'), Js('lx'), Js('m'), Js('ml'), Js('md'), Js('mdr'), Js('mn'), Js('n'), Js('nt'), Js('nth'), Js('nthr'), Js('ndr'), Js('ntr'), Js('r'), Js('rb'), Js('rd'), Js('rg'), Js('rgr'), Js('rt'), Js('rthr'), Js('rth'), Js('rl'), Js('rn'), Js('rm'), Js('t'), Js('th'), Js('thr'), Js('thdr'), Js('tr'), Js('z'), Js('zd'), Js('zdr')]))
var.put('nm4', Js([Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm5', Js([Js('c'), Js('k'), Js('ks'), Js('q'), Js('qs'), Js('r'), Js('rs'), Js('rx'), Js('s'), Js('sc'), Js('sk'), Js('x'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('o'), Js('ia'), Js('ai'), Js('ie'), Js('ee'), Js('io'), Js('ae'), Js('ea')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('cs'), Js('csh'), Js('hl'), Js('hm'), Js('hn'), Js('hx'), Js('hs'), Js('hsh'), Js('ks'), Js('ksh'), Js('ll'), Js('lm'), Js('ln'), Js('lk'), Js('lks'), Js('ls'), Js('lsh'), Js('lx'), Js('ph'), Js('r'), Js('rq'), Js('rv'), Js('s'), Js('sh'), Js('x')]))
pass
pass
pass


# Add lib to the module scope
dndBeholders = var.to_python()