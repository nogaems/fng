__all__ = ['pathfinderUndine']

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
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('bh'), Js('d'), Js('dh'), Js('g'), Js('gh'), Js('j'), Js('kh'), Js('m'), Js('n'), Js('r'), Js('rh'), Js('sh'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('aa'), Js('oo')]))
var.put('nm3', Js([Js('b'), Js('bd'), Js('c'), Js('cd'), Js('d'), Js('dd'), Js('db'), Js('g'), Js('gd'), Js('gv'), Js('gn'), Js('gm'), Js('j'), Js('k'), Js('kb'), Js('kd'), Js('kn'), Js('km'), Js('kv'), Js('m'), Js('md'), Js('mm'), Js('mb'), Js('n'), Js('nn'), Js('nb'), Js('nd'), Js('r'), Js('rd'), Js('rg'), Js('rv'), Js('rz'), Js('v'), Js('b'), Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v')]))
var.put('nm4', Js([Js('d'), Js('hz'), Js('j'), Js('k'), Js('m'), Js('n'), Js('r'), Js('sh'), Js('v')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('w'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('u'), Js('y'), Js('y'), Js('y'), Js('ya'), Js('aa')]))
var.put('nm7', Js([Js('b'), Js('bh'), Js('d'), Js('dz'), Js('dh'), Js('fd'), Js('fn'), Js('ff'), Js('f'), Js('fz'), Js('hn'), Js('hl'), Js('hr'), Js('hm'), Js('h'), Js('hh'), Js('l'), Js('lg'), Js('ld'), Js('lb'), Js('lf'), Js('ln'), Js('m'), Js('mm'), Js('mn'), Js('mr'), Js('mf'), Js('n'), Js('nn'), Js('nr'), Js('nd'), Js('nf'), Js('nh'), Js('r'), Js('rh'), Js('rb'), Js('rv'), Js('rd'), Js('rz'), Js('v'), Js('vr'), Js('b'), Js('d'), Js('f'), Js('h'), Js('l'), Js('n'), Js('m'), Js('r'), Js('v'), Js('b'), Js('d'), Js('f'), Js('h'), Js('l'), Js('n'), Js('m'), Js('r'), Js('v')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('n')]))
pass
pass


# Add lib to the module scope
pathfinderUndine = var.to_python()