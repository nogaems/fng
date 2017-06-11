__all__ = ['swQuarrenNames']

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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                while (var.get('rnd7')<Js(3.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('namelast', ((var.get('nm5').get(var.get('rnd7'))+var.get('nm6').get(var.get('rnd8')))+var.get('nm8').get(var.get('rnd10'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('namelast', ((((var.get('nm5').get(var.get('rnd7'))+var.get('nm6').get(var.get('rnd8')))+var.get('nm7').get(var.get('rnd11')))+var.get('nm6').get(var.get('rnd9')))+var.get('nm8').get(var.get('rnd10'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(5.0)):
                while (var.get('rnd')<Js(3.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd3')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('chr'), Js('d'), Js('dh'), Js('f'), Js('fr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('nr'), Js('p'), Js('ph'), Js('pw'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('sq'), Js('t'), Js('th'), Js('tr'), Js('ts'), Js('v'), Js('w'), Js('wh'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('y'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('io'), Js('oe'), Js('ue'), Js('ui'), Js('ua'), Js('ea')]))
var.put('nm3', Js([Js('b'), Js('bk'), Js('ck'), Js('ct'), Js('d'), Js('dk'), Js('dg'), Js('dl'), Js('dm'), Js('dr'), Js('g'), Js('gg'), Js('gk'), Js('k'), Js('kk'), Js('l'), Js('lb'), Js('lg'), Js('ll'), Js('lm'), Js('lp'), Js('lw'), Js('m'), Js('mt'), Js('n'), Js('ndr'), Js('nt'), Js('p'), Js('pp'), Js('q'), Js('r'), Js('rgl'), Js('rh'), Js('rl'), Js('rr'), Js('rrh'), Js('rth'), Js('rz'), Js('sq'), Js('ss'), Js('ssth'), Js('st'), Js('sth'), Js('w')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('d'), Js('f'), Js('g'), Js('hlg'), Js('k'), Js('l'), Js('lg'), Js('mp'), Js('n'), Js('nn'), Js('q'), Js('r'), Js('rg'), Js('rgg'), Js('rl'), Js('rn'), Js('rr'), Js('rsk'), Js('s'), Js('sh'), Js('sk'), Js('t'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('d'), Js('fr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('pr'), Js('r'), Js('pr'), Js('sl'), Js('sq'), Js('sll'), Js('t'), Js('th'), Js('tr'), Js('ts'), Js('v'), Js('w'), Js('y'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ee'), Js('aa')]))
var.put('nm7', Js([Js('bn'), Js('br'), Js('c'), Js('ck'), Js('cp'), Js('cm'), Js('dk'), Js('dm'), Js('g'), Js('gg'), Js('hl'), Js('k'), Js('kk'), Js('kr'), Js('km'), Js('l'), Js('lb'), Js('lp'), Js('lg'), Js('lm'), Js('nm'), Js('n'), Js('nn'), Js('nd'), Js('nr'), Js('nt'), Js('p'), Js('pp'), Js('q'), Js('r'), Js('rk'), Js('rr'), Js('rt'), Js('rh'), Js('rz'), Js('s'), Js('ss'), Js('st'), Js('sm'), Js('sq'), Js('t'), Js('v'), Js('w'), Js('wm')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js('d'), Js('dd'), Js('ff'), Js('g'), Js('k'), Js('l'), Js('lg'), Js('ll'), Js('ls'), Js('m'), Js('n'), Js('nk'), Js('nx'), Js('q'), Js('r'), Js('rg'), Js('rn'), Js('rv'), Js('s'), Js('sk'), Js('t'), Js('z')]))
pass
pass


# Add lib to the module scope
swQuarrenNames = var.to_python()