__all__ = ['swSullustanNames']

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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if ((var.get('i')%Js(2.0))!=Js(0.0)):
                while (var.get('rnd10')<Js(15.0)):
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('namelast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(10.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(6.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('c'), Js('d'), Js('dl'), Js('dw'), Js('f'), Js('fr'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('w'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('eo'), Js('ie'), Js('uu'), Js('ea'), Js('ee'), Js('ia'), Js('ao'), Js('ue'), Js('ae'), Js('ay'), Js('y'), Js('ii'), Js('ei'), Js('iu'), Js('ui'), Js('oo'), Js('ua'), Js('yu')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('br'), Js('d'), Js('dm'), Js('fr'), Js('g'), Js('ggl'), Js('gl'), Js('hs'), Js('j'), Js('kk'), Js('l'), Js('ll'), Js('llr'), Js('lth'), Js('m'), Js('md'), Js('n'), Js('nb'), Js('nch'), Js('nd'), Js('ng'), Js('nn'), Js('nr'), Js('pl'), Js('r'), Js('rg'), Js('rk'), Js('rl'), Js('rn'), Js('rr'), Js('rth'), Js('rw'), Js('shr'), Js('ss'), Js('st'), Js('t'), Js('th'), Js('w'), Js('xt'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bb'), Js('c'), Js('d'), Js('dt'), Js('gg'), Js('k'), Js('kk'), Js('l'), Js('ld'), Js('lld'), Js('ln'), Js('lss'), Js('m'), Js('n'), Js('nb'), Js('nt'), Js('pt'), Js('r'), Js('rm'), Js('rs'), Js('rt'), Js('s'), Js('sh'), Js('ss'), Js('t'), Js('tz'), Js('v'), Js('vv'), Js('x')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('d'), Js('f'), Js('fr'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('w'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('ee'), Js('uo'), Js('ee'), Js('aa'), Js('uu'), Js('ae'), Js('ya'), Js('yu')]))
var.put('nm7', Js([Js('b'), Js('bb'), Js('f'), Js('ff'), Js('fr'), Js('gr'), Js('gg'), Js('gl'), Js('hl'), Js('hn'), Js('hm'), Js('l'), Js('ll'), Js('lb'), Js('lm'), Js('ln'), Js('ld'), Js('m'), Js('md'), Js('mb'), Js('ml'), Js('mm'), Js('n'), Js('nb'), Js('nm'), Js('ng'), Js('nd'), Js('p'), Js('pp'), Js('r'), Js('rr'), Js('rb'), Js('rd'), Js('rl'), Js('rn'), Js('s'), Js('st'), Js('sth'), Js('sd'), Js('sh'), Js('ss'), Js('t'), Js('th'), Js('tt'), Js('vv')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('l'), Js('n'), Js('nn'), Js('r'), Js('s'), Js('ss'), Js('th'), Js('v'), Js('x')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bd'), Js('br'), Js('f'), Js('fr'), Js('g'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('nh'), Js('nr'), Js('p'), Js('pl'), Js('r'), Js('s'), Js('sch'), Js('sn'), Js('sq'), Js('st'), Js('sw'), Js('t'), Js('ts'), Js('v'), Js('vh'), Js('w'), Js('y'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('ie'), Js('ei'), Js('oo'), Js('ee'), Js('uu'), Js('aa'), Js('au'), Js('ya'), Js('ea'), Js('ii'), Js('iu'), Js('ua')]))
var.put('nm11', Js([Js('b'), Js('bb'), Js('bbb'), Js('d'), Js('g'), Js('gg'), Js('gn'), Js('hnt'), Js('j'), Js('kk'), Js('l'), Js('lk'), Js('ll'), Js('m'), Js('mb'), Js('mbl'), Js('n'), Js('nd'), Js('ng'), Js('nr'), Js('ns'), Js('ntr'), Js('r'), Js('rb'), Js('rr'), Js('rt'), Js('rt'), Js('s'), Js('sc'), Js('st'), Js('tt'), Js('v'), Js('vn'), Js('wn')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bb'), Js('bbs'), Js('bl'), Js('c'), Js('cb'), Js('d'), Js('h'), Js('k'), Js('l'), Js('ll'), Js('ls'), Js('m'), Js('mb'), Js('mm'), Js('mp'), Js('n'), Js('nb'), Js('nd'), Js('nn'), Js('nr'), Js('nt'), Js('p'), Js('pt'), Js('r'), Js('rb'), Js('rl'), Js('rr'), Js('rs'), Js('rss'), Js('s'), Js('st'), Js('t'), Js('th'), Js('v'), Js('vv'), Js('wn'), Js('z')]))
pass
pass


# Add lib to the module scope
swSullustanNames = var.to_python()