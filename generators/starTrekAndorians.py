__all__ = ['starTrekAndorians']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                def PyJs_LONG_0_(var=var):
                    return (((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm14').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm15').get(var.get('rnd6')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+var.get('nm1').get(var.get('rnd8')))+var.get('nm8').get(var.get('rnd9')))+var.get('nm9').get(var.get('rnd10')))+var.get('nm10').get(var.get('rnd11')))
                var.put('names', ((PyJs_LONG_0_()+var.get('nm11').get(var.get('rnd12')))+var.get('nm12').get(var.get('rnd13'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    def PyJs_LONG_1_(var=var):
                        return (((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+Js(' '))+var.get('nm6').get(var.get('rnd5')))+var.get('nm1').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd7')))+var.get('nm9').get(var.get('rnd8')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10')))+var.get('nm12').get(var.get('rnd11')))
                    var.put('names', PyJs_LONG_1_())
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    def PyJs_LONG_2_(var=var):
                        return (((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+Js(' '))+var.get('nm6').get(var.get('rnd7')))+var.get('nm1').get(var.get('rnd8')))+var.get('nm8').get(var.get('rnd9')))+var.get('nm9').get(var.get('rnd10')))+var.get('nm10').get(var.get('rnd11')))
                    var.put('names', ((PyJs_LONG_2_()+var.get('nm11').get(var.get('rnd12')))+var.get('nm12').get(var.get('rnd13'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('k'), Js('r'), Js('sh'), Js('shr'), Js('t'), Js('th'), Js('s'), Js('b')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('y')]))
var.put('nm4', Js([Js('r'), Js('b'), Js('l'), Js('v'), Js('n'), Js('s'), Js('ss'), Js('th'), Js('hr'), Js('hl')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('ia'), Js('ao'), Js('aa')]))
var.put('nm6', Js([Js("Th'"), Js("Ch'")]))
var.put('nm7', Js([Js("Sh'"), Js("Zh'")]))
var.put('nm8', Js([Js('zh'), Js('sh'), Js('th'), Js('z'), Js('v'), Js('rh'), Js('shr'), Js('vh'), Js('k'), Js('t'), Js('r'), Js('ch'), Js('q')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('y'), Js('ao'), Js('ia'), Js('aa')]))
var.put('nm10', Js([Js('r'), Js('l'), Js('v'), Js('n'), Js('th'), Js('hr'), Js('hl'), Js('nn'), Js('rh'), Js('lr'), Js('sr'), Js('kr'), Js('tr'), Js('ln'), Js('thr'), Js('q'), Js('ll'), Js('rr')]))
var.put('nm11', Js([Js('a'), Js('e'), Js('o'), Js('i')]))
var.put('nm12', Js([Js('th'), Js('s'), Js('ss'), Js('n'), Js('t'), Js('r'), Js('hr'), Js('rh'), Js('l'), Js('k'), Js('q')]))
var.put('nm13', Js([Js('vr'), Js('thr'), Js('v'), Js('jh'), Js('p'), Js('t'), Js('th'), Js('s'), Js('shr'), Js('s'), Js('z')]))
var.put('nm14', Js([Js('th'), Js('r'), Js('m'), Js('ss'), Js('v'), Js('l'), Js('ll'), Js('r'), Js('z'), Js('t'), Js('tt'), Js('sh')]))
var.put('nm15', Js([Js('h'), Js('s'), Js('l'), Js('ss'), Js('n'), Js('t'), Js('th'), Js('sh'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
starTrekAndorians = var.to_python()