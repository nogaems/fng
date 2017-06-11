__all__ = ['drWhoSilurianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js('d'), Js('h'), Js('k'), Js('l'), Js('m'), Js('r'), Js('t')]))
var.put('nm2', Js([Js('o'), Js('e'), Js('a'), Js('i')]))
var.put('nm3', Js([Js('d'), Js('dr'), Js('cth'), Js('ct'), Js('cl'), Js('cr'), Js('hr'), Js('hk'), Js('hl'), Js('kd'), Js('kl'), Js('kr'), Js('l'), Js('lr'), Js('ln'), Js('n'), Js('lm'), Js('ml'), Js('nl'), Js('nr'), Js('nl'), Js('ld'), Js('r'), Js('rk'), Js('rl')]))
var.put('nm4', Js([Js('h'), Js('k'), Js('l'), Js('n'), Js('m'), Js('r')]))
var.put('nm5', Js([Js('e'), Js('a'), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('d'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v')]))
var.put('nm7', Js([Js('o'), Js('e'), Js('a')]))
var.put('nm8', Js([Js('d'), Js('dr'), Js('hr'), Js('hl'), Js('hn'), Js('lr'), Js('ln'), Js('n'), Js('lm'), Js('ln'), Js('ml'), Js('mn'), Js('l'), Js('r'), Js('rl'), Js('rk'), Js('sk'), Js('sl'), Js('sn'), Js('sm'), Js('st'), Js('str'), Js('y')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('c'), Js('l'), Js('n'), Js('m'), Js('s')]))
pass
pass


# Add lib to the module scope
drWhoSilurianNames = var.to_python()