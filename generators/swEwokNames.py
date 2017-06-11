__all__ = ['swEwokNames']

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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('namelast', ((((var.get('nm7').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm9').get(var.get('rnd9'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('namelast', (((((var.get('nm7').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm8').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd11'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js('b'), Js('ch'), Js('c'), Js('d'), Js('gr'), Js('g'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('t'), Js('tr'), Js('w')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('ee'), Js('oo'), Js('aa'), Js('y')]))
var.put('nm3', Js([Js('b'), Js('ck'), Js('d'), Js('dr'), Js('gr'), Js('gl'), Js('g'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('pl'), Js('rf'), Js('rp'), Js('rph'), Js('rr'), Js('st'), Js('str')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ck'), Js('k'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js('b'), Js('ch'), Js('d'), Js('f'), Js('g'), Js('gl'), Js('gn'), Js('k'), Js('kn'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('t'), Js('tr')]))
var.put('nm6', Js([Js('ck'), Js('d'), Js('gr'), Js('gl'), Js('gn'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('rph'), Js('rp'), Js('rr'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('zz')]))
var.put('nm7', Js([Js('b'), Js('d'), Js('f'), Js('g'), Js('gr'), Js('gl'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('tr'), Js('w'), Js('z')]))
var.put('nm8', Js([Js('dr'), Js('dd'), Js('gr'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('lr'), Js('m'), Js('mr'), Js('mn'), Js('n'), Js('nr'), Js('nl'), Js('nt'), Js('r'), Js('rr'), Js('rl'), Js('st'), Js('str')]))
var.put('nm9', Js([Js('c'), Js('ck'), Js('k'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('t')]))
pass
pass


# Add lib to the module scope
swEwokNames = var.to_python()