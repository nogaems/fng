__all__ = ['zeldaHumanNames']

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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((var.get('nm7').get(var.get('rnd2'))+var.get('nm6').get(var.get('rnd')))+var.get('nm8').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5')))+var.get('nm10').get(var.get('rnd6'))))
                else:
                    var.put('names', (((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd5')))+var.get('nm10').get(var.get('rnd6'))))
            else:
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((((var.get('nm2').get(var.get('rnd2'))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('a'), Js('e')]))
var.put('nm2', Js([Js('b'), Js('c'), Js('d'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('z')]))
var.put('nm3', Js([Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o')]))
var.put('nm4', Js([Js('b'), Js('g'), Js('k'), Js('l'), Js('m'), Js('ng'), Js('r'), Js('rr'), Js('ss'), Js('t'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('k'), Js('l'), Js('ll'), Js('lph'), Js('m'), Js('n'), Js('nk'), Js('s')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o')]))
var.put('nm7', Js([Js('c'), Js('f'), Js('h'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('th'), Js('t')]))
var.put('nm8', Js([Js('f'), Js('l'), Js('m'), Js('mb'), Js('n'), Js('p'), Js('ph'), Js('tr'), Js('ld'), Js('r'), Js('s'), Js('sh'), Js('v')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('ia'), Js('ei'), Js('ie'), Js('ea'), Js('a'), Js('e'), Js('i')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('th')]))
pass
pass


# Add lib to the module scope
zeldaHumanNames = var.to_python()