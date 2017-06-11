__all__ = ['manticoreNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['result', 'type'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
            while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm5').get(var.get('rnd3'))):
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
            if (var.get('i')<Js(3.0)):
                while (var.get('rnd')<Js(5.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                while (var.get('rnd3')<Js(6.0)):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
            else:
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd4')),var.get('nm5').get(var.get('rnd3'))):
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                if (var.get('i')<Js(7.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd3'))))
                else:
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm5').get(var.get('rnd3'))):
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('m'), Js('n'), Js('r'), Js('sh'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('a'), Js('a'), Js('e'), Js('i'), Js('u'), Js('u'), Js('a'), Js('a'), Js('a'), Js('e'), Js('i'), Js('u'), Js('u'), Js('a'), Js('a'), Js('a'), Js('e'), Js('i'), Js('u'), Js('u'), Js('a'), Js('a'), Js('a'), Js('e'), Js('i'), Js('u'), Js('u'), Js('ia'), Js('ou'), Js('oo'), Js('ee')]))
var.put('nm3', Js([Js('fr'), Js('hk'), Js('hm'), Js('hr'), Js('kb'), Js('khg'), Js('kr'), Js('lt'), Js('lv'), Js('m'), Js('n'), Js('pr'), Js('r'), Js('rh'), Js('rkh'), Js('rm'), Js('rr'), Js('rsh'), Js('rt'), Js('ry'), Js('rz'), Js('sh'), Js('shk'), Js('t'), Js('v'), Js('vg'), Js('z'), Js('zy')]))
var.put('nm4', Js([Js('b'), Js('dd'), Js('dv'), Js('dy'), Js('gm'), Js('gn'), Js('j'), Js('khz'), Js('lf'), Js('ll'), Js('md'), Js('nb'), Js('nd'), Js('ndy'), Js('nsh'), Js('r'), Js('rb'), Js('rd'), Js('rt'), Js('rz'), Js('s'), Js('shy'), Js('v'), Js('y'), Js('zh'), Js('zm')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('hr'), Js('k'), Js('kh'), Js('n'), Js('nd'), Js('r'), Js('rd'), Js('rz'), Js('sh'), Js('shk'), Js('v'), Js('z'), Js('zl')]))
pass
pass


# Add lib to the module scope
manticoreNames = var.to_python()