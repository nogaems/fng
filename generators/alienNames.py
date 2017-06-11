__all__ = ['alienNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm14', 'nm17', 'nm3', 'nm13', 'nm7', 'nm10', 'nm2', 'nm15', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('rnd3')<Js(46.0)):
                    while (var.get('rnd4')>Js(5.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('rnd4')>Js(5.0)):
                        var.put('rnd5', Js(0.0))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('names', (((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd6'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    if (var.get('rnd3')<Js(46.0)):
                        while (var.get('rnd4')>Js(5.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                    var.put('names', (((((var.get('nm12').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd3')))+var.get('nm15').get(var.get('rnd4')))+var.get('nm16').get(var.get('rnd5')))+var.get('nm17').get(var.get('rnd6'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('br'), Js('c'), Js('cr'), Js('ch'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('kn'), Js('km'), Js('p'), Js('pr'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('st'), Js('str'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('xr'), Js('z'), Js('zr'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('au'), Js('ou'), Js('ei'), Js('uy'), Js('oe'), Js('ua'), Js('ue'), Js('uo'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('km'), Js('pr'), Js('qr'), Js('st'), Js('tr'), Js('vr'), Js('wr'), Js('xx'), Js('zz'), Js('bb'), Js('dd'), Js('g'), Js('kk'), Js("q'"), Js("k'"), Js('rr'), Js("r'"), Js("t'"), Js('tt'), Js('vv'), Js("v'"), Js('wr'), Js("x'"), Js("z'"), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('hr'), Js('ht'), Js('hn'), Js('hm'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('lk'), Js('lz'), Js('lp'), Js('lt'), Js('m'), Js('mt'), Js('nt'), Js('p'), Js('pt'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rq'), Js('rk'), Js('rc'), Js('rb'), Js('rd'), Js('sk'), Js('t'), Js('th'), Js('ts'), Js('wth'), Js('x'), Js('z')]))
var.put('nm6', Js([Js('b'), Js('bl'), Js('c'), Js('cl'), Js('ch'), Js('d'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gl'), Js('gn'), Js('h'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('ph'), Js('q'), Js('ql'), Js('s'), Js('st'), Js('sl'), Js('t'), Js('v'), Js('vl'), Js('w'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ae'), Js('ea'), Js('eo'), Js('oe'), Js('ie'), Js('ue'), Js('ua'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm8', Js([Js('b'), Js('c'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('w'), Js('bb'), Js('bl'), Js('cl'), Js('ff'), Js('fl'), Js('gl'), Js('gn'), Js('ks'), Js('ll'), Js('lh'), Js('kh'), Js('bh'), Js('ch'), Js('dh'), Js('lm'), Js('ln'), Js('lph'), Js('ls'), Js('lf'), Js('mm'), Js('mn'), Js('ms'), Js('nn'), Js('ns'), Js('p'), Js('ph'), Js('ps'), Js('rf'), Js('ss'), Js('st'), Js('sh'), Js('th'), Js('ts'), Js("s'"), Js("l'"), Js("n'"), Js("m'"), Js("f'"), Js("h'")]))
var.put('nm10', Js([Js(''), Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hs'), Js('ht'), Js('hn'), Js('hm'), Js('hl'), Js('k'), Js('l'), Js('ll'), Js('kh'), Js('lh'), Js('lm'), Js('ln'), Js('lph'), Js('ls'), Js('lf'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('ns'), Js('p'), Js('ms'), Js('ph'), Js('ps'), Js('s'), Js('ss'), Js('sh'), Js('th'), Js('ts'), Js('w')]))
var.put('nm11', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ae'), Js('ea'), Js('eo'), Js('oe'), Js('ie'), Js('ue'), Js('ua'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm12', Js([Js('b'), Js('bl'), Js('br'), Js('c'), Js('ch'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fl'), Js('fr'), Js('g'), Js('gl'), Js('gn'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('km'), Js('kn'), Js('kr'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('pl'), Js('pr'), Js('q'), Js('ql'), Js('qr'), Js('r'), Js('s'), Js('sl'), Js('sr'), Js('st'), Js('str'), Js('t'), Js('tl'), Js('tr'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('xr'), Js('z'), Js('zr'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm13', Js([Js('a'), Js('ae'), Js('au'), Js('e'), Js('ea'), Js('ei'), Js('eo'), Js('i'), Js('ie'), Js('o'), Js('oe'), Js('ou'), Js('u'), Js('ua'), Js('ue'), Js('uo'), Js('uy'), Js('y')]))
var.put('nm14', Js([Js('b'), Js('bb'), Js('bh'), Js('bl'), Js('br'), Js('c'), Js('ch'), Js('cl'), Js('cr'), Js('d'), Js('dd'), Js('dh'), Js('dr'), Js('f'), Js('ff'), Js('fl'), Js('g'), Js('gl'), Js('gn'), Js('gr'), Js('h'), Js('hh'), Js('hl'), Js('hm'), Js('hn'), Js('hs'), Js('hsh'), Js('j'), Js('k'), Js("k'"), Js('kh'), Js('kk'), Js('km'), Js('kr'), Js('ks'), Js('l'), Js('lf'), Js('lh'), Js('ll'), Js('lm'), Js('ln'), Js('lph'), Js('ls'), Js('m'), Js('mm'), Js('mn'), Js('ms'), Js('n'), Js('nn'), Js('ns'), Js('p'), Js('ph'), Js('pr'), Js('ps'), Js('q'), Js("q'"), Js('qr'), Js('r'), Js("r'"), Js('rf'), Js('rr'), Js('s'), Js('sh'), Js('ss'), Js('st'), Js('t'), Js("t'"), Js('th'), Js('tr'), Js('ts'), Js('tt'), Js('v'), Js("v'"), Js('vr'), Js('vv'), Js('w'), Js('wr'), Js('x'), Js("x'"), Js('xx'), Js('z'), Js('zz')]))
var.put('nm15', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('ae'), Js('au'), Js('e'), Js('ea'), Js('ei'), Js('eo'), Js('i'), Js('ie'), Js('o'), Js('oe'), Js('ou'), Js('u'), Js('ua'), Js('ue'), Js('uo'), Js('uy'), Js('y'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm16', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hl'), Js('hm'), Js('hn'), Js('hq'), Js('hr'), Js('hs'), Js('hsh'), Js('hst'), Js('ht'), Js('hx'), Js('hz'), Js('k'), Js('kh'), Js('ks'), Js('kx'), Js('l'), Js('lf'), Js('lh'), Js('lk'), Js('ll'), Js('lm'), Js('ln'), Js('lp'), Js('lph'), Js('ls'), Js('lst'), Js('lt'), Js('lz'), Js('m'), Js('mm'), Js('mn'), Js('ms'), Js('mt'), Js('n'), Js('nn'), Js('ns'), Js('nt'), Js('p'), Js('ph'), Js('ps'), Js('pt'), Js('q'), Js('r'), Js('rb'), Js('rc'), Js('rd'), Js('rf'), Js('rk'), Js('rq'), Js('rs'), Js('rst'), Js('rt'), Js('s'), Js('sh'), Js('sk'), Js('sp'), Js('ss'), Js('st'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
var.put('nm17', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ae'), Js('ea'), Js('eo'), Js('oe'), Js('ie'), Js('ue'), Js('ua'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
alienNames = var.to_python()