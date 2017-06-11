__all__ = ['destinyHiveNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('cr'), Js('d'), Js('g'), Js('gr'), Js('k'), Js('kr'), Js('m'), Js('n'), Js('r'), Js('s'), Js('tr'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('u'), Js('oo')]))
var.put('nm3', Js([Js('c'), Js('cr'), Js('gr'), Js('k'), Js('kr'), Js('m'), Js('n'), Js('nd'), Js('r'), Js('rd'), Js('rg'), Js('rn'), Js('rv'), Js('rz'), Js('t'), Js('tr'), Js('v'), Js('z')]))
var.put('nm4', Js([Js(''), Js('c'), Js('k'), Js('k'), Js('n'), Js('r'), Js('x')]))
var.put('nm5', Js([Js('c'), Js('ch'), Js('h'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('th'), Js('v'), Js('z'), Js('zh')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('e'), Js('i'), Js('o')]))
var.put('nm7', Js([Js('g'), Js('lk'), Js('lm'), Js('ln'), Js('m'), Js('mn'), Js('n'), Js('nl'), Js('nr'), Js('rm'), Js('sh'), Js('sm'), Js('sn'), Js('sr'), Js('st'), Js('th'), Js('tr'), Js('v'), Js('vn'), Js('vr'), Js('z'), Js('zd'), Js('zl'), Js('zn')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('s'), Js('th')]))
pass
pass


# Add lib to the module scope
destinyHiveNames = var.to_python()