__all__ = ['swFalleenNames']

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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('namelast', ((var.get('nm8').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd8'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('namelast', ((((var.get('nm8').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm9').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd8'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd4')<Js(3.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd4')<Js(3.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('cz'), Js('h'), Js('j'), Js('k'), Js('s'), Js('t'), Js('th'), Js('tr'), Js('x'), Js('xz'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('uu'), Js('ee')]))
var.put('nm3', Js([Js('b'), Js('h'), Js('j'), Js('n'), Js('nn'), Js('m'), Js('mr'), Js('mn'), Js('mm'), Js('rr'), Js('sh'), Js('sz'), Js('t'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('l'), Js('n'), Js('nn'), Js('r'), Js('s'), Js('st'), Js('t'), Js('x')]))
var.put('nm5', Js([Js(''), Js(''), Js('b'), Js('d'), Js('f'), Js('g'), Js('gl'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('s'), Js('th'), Js('x'), Js('z')]))
var.put('nm6', Js([Js('d'), Js('dv'), Js('f'), Js('ff'), Js('ll'), Js('m'), Js('mm'), Js('ml'), Js('n'), Js('nl'), Js('nr'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('st'), Js('sn'), Js('sm'), Js('sv'), Js('t'), Js('v')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js('bs'), Js('l'), Js('m'), Js('n'), Js('s'), Js('t')]))
var.put('nm8', Js([Js('br'), Js('b'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('s'), Js('t'), Js('w'), Js('x'), Js('z')]))
var.put('nm9', Js([Js('d'), Js('dv'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('gn'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('mr'), Js('ms'), Js('nr'), Js('nn'), Js('n'), Js('ns'), Js('s'), Js('ss'), Js('st'), Js('sm'), Js('sn'), Js('sv'), Js('rr'), Js('t'), Js('tr'), Js('thr'), Js('v'), Js('vr'), Js('z')]))
var.put('nm10', Js([Js('c'), Js('d'), Js('j'), Js('l'), Js('m'), Js('n'), Js('r'), Js('ss'), Js('t'), Js('x')]))
pass
pass


# Add lib to the module scope
swFalleenNames = var.to_python()