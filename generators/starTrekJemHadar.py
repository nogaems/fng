__all__ = ['starTrekJemHadar']

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
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names1', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('rnd5')<Js(2.0)):
                    var.put('rnd6', Js(1.0))
                var.put('names1', (((((var.get('nm2').get(var.get('rnd'))+var.get('nm3').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            if (var.get('rnd7')<Js(6.0)):
                var.put('rnd11', Js(7.0))
                var.put('rnd12', Js(0.0))
            if (var.get('rnd11')>Js(5.0)):
                var.put('rnd12', Js(0.0))
            var.put('names', (((((((var.get('names1')+Js("'"))+var.get('nm7').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8')))+var.get('nm3').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd10')))+var.get('nm7').get(var.get('rnd11')))+var.get('nm5').get(var.get('rnd12'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('i'), Js('o'), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm3', Js([Js('a'), Js('u'), Js('o'), Js('i'), Js('e'), Js('a')]))
var.put('nm4', Js([Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js('d'), Js('g'), Js('k'), Js('n'), Js('t')]))
var.put('nm6', Js([Js('a'), Js(''), Js(''), Js(''), Js('')]))
var.put('nm7', Js([Js('i'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm8', Js([Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('y'), Js('z'), Js('kl'), Js('cl')]))
var.put('nm9', Js([Js('i'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
starTrekJemHadar = var.to_python()