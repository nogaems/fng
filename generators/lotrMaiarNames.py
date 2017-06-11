__all__ = ['lotrMaiarNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('rnd2')>Js(6.0)):
                    while (var.get('rnd4')>Js(6.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('rnd2')>Js(6.0)):
                    while (var.get('rnd4')>Js(6.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('names', (((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5')))+var.get('nm10').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('f'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('w'), Js('y'), Js('z'), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('ó'), Js('é'), Js('ie'), Js('ui'), Js('ia'), Js('ea'), Js('ae'), Js('ua')]))
var.put('nm3', Js([Js('l'), Js('lm'), Js('ln'), Js('ls'), Js('n'), Js('nn'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('ss'), Js('th')]))
var.put('nm4', Js([Js('r'), Js('n'), Js('s'), Js('th'), Js('l'), Js('m')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('ë'), Js('é'), Js('ó'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('c'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('th'), Js(''), Js('')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('ó'), Js('é'), Js('ai'), Js('eo'), Js('io'), Js('eö'), Js('uo'), Js('ua')]))
var.put('nm8', Js([Js('l'), Js('ll'), Js('lm'), Js('ln'), Js('ls'), Js('m'), Js('md'), Js('n'), Js('nd'), Js('nm'), Js('nw'), Js('r'), Js('s'), Js('ss'), Js('t'), Js('w')]))
var.put('nm9', Js([Js('l'), Js('m'), Js('n'), Js('nd'), Js('r'), Js('s'), Js('t'), Js('th')]))
var.put('nm10', Js([Js('o'), Js('e'), Js('ë'), Js('ó'), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
lotrMaiarNames = var.to_python()