__all__ = ['destinyAwokenNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            var.put('rndA', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rndB', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rndE', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('nmLast', ((var.get('nm9').get(var.get('rndA'))+var.get('nm10').get(var.get('rndB')))+var.get('nm12').get(var.get('rndE'))))
            else:
                var.put('rndC', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rndD', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('nmLast', ((((var.get('nm9').get(var.get('rndA'))+var.get('nm10').get(var.get('rndB')))+var.get('nm11').get(var.get('rndC')))+var.get('nm10').get(var.get('rndD')))+var.get('nm12').get(var.get('rndE'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+Js(' '))+var.get('nmLast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('nmLast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nmLast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('g'), Js('j'), Js('k'), Js('q'), Js('r'), Js('v'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('a'), Js('u'), Js('u'), Js('e'), Js('i'), Js('a'), Js('a'), Js('u'), Js('u'), Js('e'), Js('i'), Js('a'), Js('a'), Js('u'), Js('u'), Js('e'), Js('i'), Js('oo'), Js('ou'), Js('uu'), Js('aa')]))
var.put('nm3', Js([Js('d'), Js('dr'), Js('g'), Js('gd'), Js('gr'), Js('h'), Js('j'), Js('ldr'), Js('lgr'), Js('ndr'), Js('ngr'), Js('q'), Js('r'), Js('rg'), Js('rj'), Js('sg'), Js('v'), Js('vg'), Js('x'), Js('z'), Js('zg')]))
var.put('nm4', Js([Js('c'), Js('ch'), Js('g'), Js('l'), Js('n'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('f'), Js('l'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('s'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('e'), Js('e'), Js('a'), Js('a'), Js('i'), Js('o'), Js('e'), Js('e'), Js('a'), Js('a'), Js('i'), Js('o'), Js('e'), Js('e'), Js('a'), Js('a'), Js('i'), Js('o'), Js('ia'), Js('ua'), Js('ea'), Js('aa')]))
var.put('nm7', Js([Js('l'), Js('lm'), Js('ln'), Js('lr'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('nn'), Js('r'), Js('rh'), Js('rl'), Js('rm'), Js('rn'), Js('rr'), Js('rt'), Js('sr'), Js('ss'), Js('tr'), Js('x'), Js('y'), Js('z')]))
var.put('nm8', Js([Js('f'), Js('n'), Js('nn'), Js('ph'), Js('s'), Js('ss'), Js('sh'), Js('x')]))
var.put('nm9', Js([Js('c'), Js('g'), Js('j'), Js('m'), Js('q'), Js('s'), Js('th'), Js('v'), Js('x'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa')]))
var.put('nm11', Js([Js('d'), Js('f'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('sh'), Js('v'), Js('z')]))
var.put('nm12', Js([Js('hl'), Js('hn'), Js('j'), Js('l'), Js('m'), Js('n'), Js('nj'), Js('s'), Js('sh'), Js('v')]))
pass
pass


# Add lib to the module scope
destinyAwokenNames = var.to_python()