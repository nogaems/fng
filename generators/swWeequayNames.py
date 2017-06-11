__all__ = ['swWeequayNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm3b', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                if (var.get('rnd7')<Js(6.0)):
                    while (var.get('rnd10')<Js(8.0)):
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
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd5')<Js(10.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(4.0)):
                    if (var.get('rnd')<Js(5.0)):
                        while (var.get('rnd5')<Js(4.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('f'), Js('g'), Js('gr'), Js('gw'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('pr'), Js('q'), Js('s'), Js('sh'), Js('t'), Js('tr'), Js('v'), Js('w'), Js('y')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('ia'), Js('ie'), Js('ea'), Js('ei'), Js('ee'), Js('aa'), Js('ai')]))
var.put('nm3', Js([Js('-m'), Js('-n'), Js('-h'), Js('-l'), Js('-v'), Js('b'), Js('b-r'), Js('bl'), Js('b-d'), Js('b-z'), Js('d'), Js('d-r'), Js('d-z'), Js('dl'), Js('ds'), Js('dd'), Js('g'), Js('g-r'), Js('gg'), Js('gr'), Js('gd'), Js('gl'), Js('h'), Js('j'), Js('k-b'), Js('k-r'), Js('kd'), Js('k-z'), Js('kn'), Js('kr'), Js('kb'), Js('km'), Js('l'), Js('ll'), Js('ln'), Js('m'), Js('mb'), Js('nm-b'), Js('mr'), Js('n-d'), Js('nd'), Js('nl'), Js('nn'), Js('ns'), Js('r'), Js('r-z'), Js('r-b'), Js('r-g'), Js('r-d'), Js('rg'), Js('rr'), Js('rs'), Js('rt'), Js('s-d'), Js('s-b'), Js('s-l'), Js('s-g'), Js('t'), Js('tt'), Js('v'), Js('z')]))
var.put('nm3b', Js([Js('b'), Js('bl'), Js('d'), Js('dl'), Js('ds'), Js('dd'), Js('g'), Js('gg'), Js('gr'), Js('gd'), Js('gl'), Js('h'), Js('j'), Js('kd'), Js('kn'), Js('kr'), Js('kb'), Js('km'), Js('l'), Js('ll'), Js('ln'), Js('m'), Js('mb'), Js('mr'), Js('nd'), Js('nl'), Js('nn'), Js('ns'), Js('r'), Js('rg'), Js('rr'), Js('rs'), Js('rt'), Js('t'), Js('tt'), Js('v'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js('bl'), Js('c'), Js('g'), Js('h'), Js('k'), Js('kk'), Js('l'), Js('m'), Js('mbl'), Js('mm'), Js('n'), Js('nn'), Js('r'), Js('rb'), Js('rg'), Js('rk'), Js('rm'), Js('rs'), Js('rt'), Js('s'), Js('sk'), Js('t'), Js('ts'), Js('v'), Js('wn'), Js('y'), Js('z')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('f'), Js('g'), Js('h'), Js('k'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('o'), Js('a'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('o'), Js('a'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('o'), Js('a'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('o'), Js('a'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('o'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('o'), Js('a'), Js('ie'), Js('ii'), Js('ee'), Js('ei')]))
var.put('nm7', Js([Js('c'), Js('cr'), Js('cn'), Js('cm'), Js('g'), Js('gg'), Js('gm'), Js('gr'), Js('gs'), Js('h'), Js('hm'), Js('hn'), Js('hr'), Js('hs'), Js('km'), Js('kn'), Js('kr'), Js('kl'), Js('ks'), Js('l'), Js('ll'), Js('lm'), Js('lk'), Js('lc'), Js('lr'), Js('ls'), Js('mk'), Js('mr'), Js('n'), Js('mm'), Js('m'), Js('nn'), Js('nd'), Js('nk'), Js('r'), Js('rk'), Js('rm'), Js('rr'), Js('s'), Js('ss'), Js('sk'), Js('sm')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('x'), Js('z')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('d'), Js('dr'), Js('dl'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gh'), Js('k'), Js('kr'), Js('kl'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('st'), Js('sv'), Js('sw'), Js('sl'), Js('t'), Js('th'), Js('tr'), Js('tl'), Js('v'), Js('vr'), Js('vl')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ee'), Js('ie'), Js('ei'), Js('oo')]))
var.put('nm11', Js([Js('bk'), Js('b'), Js('bb'), Js('bg'), Js('br'), Js('d'), Js('dd'), Js('dk'), Js('dr'), Js('ff'), Js('f'), Js('fk'), Js('g'), Js('gr'), Js('gg'), Js('gl'), Js('hn'), Js('hm'), Js('hk'), Js('hl'), Js('k'), Js('kk'), Js('kr'), Js('kl'), Js('kd'), Js('kb'), Js('l'), Js('ls'), Js('lm'), Js('ld'), Js('lg'), Js('m'), Js('mk'), Js('mt'), Js('mm'), Js('nk'), Js('nd'), Js('ng'), Js('nn'), Js('nt'), Js('r'), Js('rk'), Js('rs'), Js('rt'), Js('rtr'), Js('s'), Js('sk'), Js('sr'), Js('st'), Js('str'), Js('t'), Js('tr')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('k'), Js('lq'), Js('lk'), Js('lc'), Js('mk'), Js('m'), Js('mz'), Js('n'), Js('nk'), Js('nd'), Js('nc'), Js('nz'), Js('q'), Js('r'), Js('rd'), Js('s'), Js('sh'), Js('sk'), Js('x'), Js('y')]))
pass
pass


# Add lib to the module scope
swWeequayNames = var.to_python()