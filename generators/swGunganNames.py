__all__ = ['swGunganNames']

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
                if (var.get('i')<Js(4.0)):
                    if (var.get('rnd')<Js(4.0)):
                        while (var.get('rnd4')<Js(3.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        while (var.get('rnd')<Js(4.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+Js('-'))+var.get('nm5').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(4.0)):
                    if (var.get('rnd')<Js(4.0)):
                        while (var.get('rnd4')<Js(3.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        while (var.get('rnd')<Js(4.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        while (var.get('rnd4')<Js(3.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4')))+Js('-'))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4')))+Js('  '))+var.get('namelast')))
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
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('c'), Js('cr'), Js('cl'), Js('d'), Js('f'), Js('fl'), Js('fr'), Js('g'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sk'), Js('t'), Js('w'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oo'), Js('oe'), Js('ee'), Js('ie'), Js('ue'), Js('ia'), Js('au')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('bl'), Js('bs'), Js('d'), Js('dr'), Js('g'), Js('gg'), Js('k'), Js('kf'), Js('kn'), Js('l'), Js('ll'), Js('llb'), Js('lsb'), Js('lsk'), Js('ly'), Js('m'), Js('mb'), Js('mf'), Js('n'), Js('nb'), Js('nk'), Js('nn'), Js('nt'), Js('p'), Js('pp'), Js('r'), Js('rk'), Js('rs'), Js('rt'), Js('rv'), Js('s'), Js('sm'), Js('ss'), Js('t'), Js('tt'), Js('v'), Js('x'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('ff'), Js('gg'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('nn'), Js('p'), Js('r'), Js('rd'), Js('rt'), Js('s'), Js('sh'), Js('sk'), Js('ss'), Js('w')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('c'), Js('cl'), Js('d'), Js('dh'), Js('f'), Js('fl'), Js('fr'), Js('h'), Js('j'), Js('kl'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('spl'), Js('t'), Js('th'), Js('w'), Js('y')]))
var.put('nm6', Js([Js('bl'), Js('bb'), Js('b'), Js('bs'), Js('d'), Js('dd'), Js('dh'), Js('f'), Js('ff'), Js('g'), Js('l'), Js('ll'), Js('ls'), Js('lb'), Js('ls'), Js('m'), Js('mm'), Js('mb'), Js('mf'), Js('n'), Js('nb'), Js('nn'), Js('nd'), Js('p'), Js('pf'), Js('pd'), Js('pp'), Js('r'), Js('rt'), Js('rs'), Js('s'), Js('ss'), Js('sm'), Js('sn'), Js('sd'), Js('t'), Js('th'), Js('tt'), Js('w'), Js('x'), Js('z')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('f'), Js('ff'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('rs'), Js('s'), Js('ss'), Js('w')]))
var.put('nm8', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('sl'), Js('sq'), Js('t'), Js('tr'), Js('w'), Js('y'), Js('w'), Js('z')]))
var.put('nm9', Js([Js('bb'), Js('bbl'), Js('bl'), Js('d'), Js('db'), Js('dr'), Js('dt'), Js('f'), Js('ff'), Js('g'), Js('gl'), Js('j'), Js('kk'), Js('ll'), Js('lb'), Js('ld'), Js('ls'), Js('m'), Js('mb'), Js('mf'), Js('nd'), Js('ng'), Js('p'), Js('pf'), Js('r'), Js('rd'), Js('rm'), Js('rp'), Js('rs'), Js('rsh'), Js('s'), Js('ss'), Js('sb'), Js('sd'), Js('sm'), Js('th'), Js('tt'), Js('ttl'), Js('w'), Js('z'), Js('zb')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('f'), Js('g'), Js('l'), Js('ls'), Js('m'), Js('mk'), Js('n'), Js('nks'), Js('nt'), Js('p'), Js('pps'), Js('r'), Js('rm'), Js('rr'), Js('rs'), Js('rt'), Js('s'), Js('ss'), Js('th'), Js('w'), Js('wn'), Js('z'), Js('zz')]))
pass
pass


# Add lib to the module scope
swGunganNames = var.to_python()