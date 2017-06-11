__all__ = ['swGandNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            var.put('namelast', (((var.get('nm5').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd8')))+var.get('nm7').get(var.get('rnd9'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(5.0)):
                while (var.get('rnd4')<Js(2.0)):
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
var.put('nm1', Js([Js(''), Js(''), Js('c'), Js("c'n"), Js('d'), Js("d'k"), Js('k'), Js('l'), Js('n'), Js("r'k"), Js('r'), Js('s'), Js("s'z"), Js('t'), Js("t'r"), Js('v'), Js("v'l"), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('aa'), Js('oo'), Js('uu'), Js('ee'), Js('ay'), Js('ai'), Js('ey'), Js('ya'), Js('yu'), Js('yi')]))
var.put('nm3', Js([Js('b'), Js('ck'), Js('d'), Js('dn'), Js('ff'), Js('fn'), Js('fl'), Js('g'), Js('gn'), Js('gl'), Js('k'), Js('kk'), Js('kn'), Js('kl'), Js('l'), Js('ll'), Js('ln'), Js('ls'), Js('ld'), Js('nl'), Js('nf'), Js('q'), Js('r'), Js('rn'), Js('rl'), Js('s'), Js('ss'), Js('sl'), Js('ssl'), Js('t'), Js('z'), Js('zl')]))
var.put('nm4', Js([Js(''), Js('d'), Js('k'), Js('l'), Js('n'), Js('r'), Js('sh'), Js('ss'), Js('x')]))
var.put('nm5', Js([Js('cr'), Js('cn'), Js('d'), Js('dr'), Js('k'), Js('kr'), Js('l'), Js('n'), Js('p'), Js('pr'), Js('pn'), Js('q'), Js('qr'), Js('sr'), Js('shr'), Js('tr'), Js('v'), Js('vr'), Js('z')]))
var.put('nm6', Js([Js('ck'), Js('cl'), Js('d'), Js('ff'), Js('fr'), Js('gg'), Js('gl'), Js('k'), Js('kk'), Js('kr'), Js('q'), Js('ql'), Js('qr'), Js('rr'), Js('rn'), Js('rl'), Js('sl'), Js('th'), Js('t'), Js('tr'), Js('z'), Js('zz'), Js('zl')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('aa'), Js('oo'), Js('uu'), Js('ee'), Js('ay'), Js('ai'), Js('ey'), Js('ya'), Js('yu'), Js('yi')]))
pass
pass


# Add lib to the module scope
swGandNames = var.to_python()