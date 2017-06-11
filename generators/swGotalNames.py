__all__ = ['swGotalNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('namelast', ((var.get('nm5').get(var.get('rnd6'))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd8'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('namelast', ((((var.get('nm5').get(var.get('rnd6'))+var.get('nm6').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd9')))+var.get('nm6').get(var.get('rnd11')))+var.get('nm8').get(var.get('rnd8'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(5.0)):
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
var.put('nm1', Js([Js('f'), Js('gl'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('t'), Js('th'), Js('v'), Js('vl'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('aa'), Js('uu'), Js('ee')]))
var.put('nm3', Js([Js("'h"), Js('hs'), Js("h'sh"), Js("h'l"), Js('hx'), Js('hk'), Js("hk'kh"), Js("'k"), Js('k'), Js('kh'), Js("'kh"), Js("'l"), Js('lt'), Js('p'), Js('ph'), Js("r'ph"), Js('r'), Js("'r"), Js("r'l"), Js('rl'), Js('sk'), Js("s'kh"), Js("s'm"), Js('sl'), Js('shn'), Js("sh'n"), Js("sh'm"), Js('sz'), Js('shm'), Js('t'), Js("t'm"), Js('tm'), Js('tn'), Js('tl'), Js("t'n"), Js('xs'), Js('xz')]))
var.put('nm4', Js([Js('c'), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('r'), Js('rn'), Js('tt'), Js('th'), Js('x')]))
var.put('nm5', Js([Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('m'), Js('n'), Js('r'), Js('s'), Js('tr'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm7', Js([Js('hs'), Js('hx'), Js('k'), Js('kh'), Js('l'), Js('ll'), Js('r'), Js('rr'), Js('rl'), Js('rs'), Js('s'), Js('ss'), Js('sl'), Js('sk'), Js('sh'), Js('sm'), Js('st'), Js('t'), Js('th'), Js('tl'), Js('v'), Js('x'), Js('z')]))
var.put('nm8', Js([Js('c'), Js('gg'), Js('gh'), Js('l'), Js('m'), Js('n'), Js('nth'), Js('r'), Js('rn'), Js('rk'), Js('ss'), Js('t'), Js('th'), Js('x')]))
pass
pass


# Add lib to the module scope
swGotalNames = var.to_python()