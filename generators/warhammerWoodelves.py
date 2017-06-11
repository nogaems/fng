__all__ = ['warhammerWoodelves']

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
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                else:
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
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('dh'), Js('g'), Js('k'), Js('kh'), Js('sc'), Js('str'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('o'), Js('a'), Js('o'), Js('o'), Js('a'), Js('io'), Js('aa'), Js('ae'), Js('ia')]))
var.put('nm3', Js([Js('c'), Js('d'), Js('k'), Js('l'), Js('r'), Js('c'), Js('d'), Js('k'), Js('l'), Js('r'), Js('c'), Js('cc'), Js('cr'), Js('dr'), Js('d'), Js('k'), Js('kk'), Js('lc'), Js('lg'), Js('lk'), Js('ll'), Js('lt'), Js('lv'), Js('l'), Js('r'), Js('rl'), Js('rt'), Js('rc'), Js('rg'), Js('rn'), Js('sc'), Js('sr'), Js('st'), Js('sl'), Js('th'), Js('tr'), Js('tt'), Js('zc'), Js('zk'), Js('zl')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('c'), Js('n'), Js('s'), Js('t'), Js('th')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('dh'), Js('dr'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('q'), Js('s'), Js('th'), Js('v'), Js('y')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('y'), Js('a'), Js('e'), Js('i'), Js('y'), Js('a'), Js('e'), Js('i'), Js('y'), Js('a'), Js('e'), Js('a'), Js('a'), Js('e'), Js('e'), Js('ie'), Js('ae')]))
var.put('nm7', Js([Js('c'), Js('cc'), Js('ch'), Js('d'), Js('dd'), Js('dr'), Js('h'), Js('hh'), Js('lc'), Js('ll'), Js('lv'), Js('ls'), Js('lt'), Js('lth'), Js('ln'), Js('lm'), Js('l'), Js('n'), Js('nn'), Js('nr'), Js('nv'), Js('nd'), Js('ph'), Js('r'), Js('rl'), Js('rr'), Js('rv'), Js('rl'), Js('s'), Js('ss'), Js('sh'), Js('st'), Js('str'), Js('sv'), Js('t'), Js('th'), Js('tr'), Js('v')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('l'), Js('n'), Js('s'), Js('th')]))
pass
pass


# Add lib to the module scope
warhammerWoodelves = var.to_python()