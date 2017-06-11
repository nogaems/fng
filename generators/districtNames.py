__all__ = ['districtNames']

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
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            if (var.get('rnd6')<Js(20.0)):
                while PyJsStrictEq(var.get('rnd7'),Js(0.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            else:
                var.put('rnd7', Js(0.0))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            if (var.get('i')<Js(2.0)):
                var.put('names', ((((((var.get('nm6').get(var.get('rnd6'))+Js(' '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd5')))+Js('  '))+var.get('nm7').get(var.get('rnd7'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((((var.get('nm6').get(var.get('rnd6'))+Js(' '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js('  '))+var.get('nm7').get(var.get('rnd7'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm6').get(var.get('rnd6'))+Js(' '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js('  '))+var.get('nm7').get(var.get('rnd7'))))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((((((((var.get('nm6').get(var.get('rnd6'))+Js(' '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js('  '))+var.get('nm7').get(var.get('rnd7'))))
                        else:
                            var.put('names', ((((((((((var.get('nm6').get(var.get('rnd6'))+Js(' '))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js('  '))+var.get('nm7').get(var.get('rnd7'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('w'), Js('y'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bl'), Js('br'), Js('ch'), Js('cl'), Js('cr'), Js('dr'), Js('fl'), Js('fr'), Js('gl'), Js('gr'), Js('pl'), Js('pr'), Js('sc'), Js('sh'), Js('sk'), Js('sl'), Js('sm'), Js('sn'), Js('sp'), Js('st'), Js('sw'), Js('tr'), Js('tw'), Js('wh'), Js('wr'), Js('sch'), Js('scr'), Js('sph'), Js('shr'), Js('spl'), Js('spr'), Js('str'), Js('thr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ai'), Js('eo'), Js('ea'), Js('ee'), Js('oo'), Js('oa'), Js('ia'), Js('io')]))
var.put('nm3', Js([Js('br'), Js('bl'), Js('c'), Js('ch'), Js('cl'), Js('ct'), Js('ck'), Js('cc'), Js('d'), Js('dg'), Js('dw'), Js('dr'), Js('dl'), Js('f'), Js('g'), Js('gg'), Js('gl'), Js('gw'), Js('gr'), Js('h'), Js('k'), Js('kr'), Js('kw'), Js('l'), Js('ll'), Js('lb'), Js('ld'), Js('lg'), Js('lm'), Js('ln'), Js('lr'), Js('lw'), Js('lz'), Js('m'), Js('mr'), Js('ml'), Js('nw'), Js('n'), Js('nn'), Js('ng'), Js('nl'), Js('p'), Js('ph'), Js('r'), Js('rb'), Js('rc'), Js('rd'), Js('rg'), Js('rl'), Js('rm'), Js('rn'), Js('rr'), Js('rs'), Js('rst'), Js('rt'), Js('rth'), Js('rtr'), Js('rw'), Js('rv'), Js('s'), Js('ss'), Js('sh'), Js('st'), Js('sth'), Js('str'), Js('sl'), Js('sw'), Js('t'), Js('tb'), Js('tl'), Js('tg'), Js('tm'), Js('tn'), Js('tw'), Js('th'), Js('tt'), Js('v'), Js('w'), Js('wl'), Js('wn'), Js('x'), Js('z')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('f'), Js('ff'), Js('g'), Js('gg'), Js('h'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('nn'), Js('p'), Js('pp'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('t'), Js('tt'), Js('w')]))
var.put('nm5', Js([Js('st'), Js('sk'), Js('sp'), Js('nd'), Js('nt'), Js('nk'), Js('mp'), Js('rd'), Js('ld'), Js('lp'), Js('rk'), Js('lt'), Js('lf'), Js('pt'), Js('ft'), Js('ct'), Js('t'), Js('d'), Js('k'), Js('n'), Js('p'), Js('l'), Js('g'), Js('m'), Js('s'), Js('b'), Js('c'), Js('t'), Js('d'), Js('k'), Js('n'), Js('p'), Js('l'), Js('g'), Js('m'), Js('s'), Js('b'), Js('c')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('West'), Js('East'), Js('North'), Js('South'), Js('Little'), Js('Upper'), Js('Lower'), Js('Fort'), Js('Upper West'), Js('Upper East'), Js('Upper North'), Js('Upper South'), Js('Lower West'), Js('Lower East'), Js('Lower North'), Js('Lower South'), Js('Midtown'), Js('Waterside'), Js('Bayside'), Js('Downtown')]))
var.put('nm7', Js([Js(''), Js('Acre'), Js('Avenue'), Js('Bazaar'), Js('Boulevard'), Js('Center'), Js('Circle'), Js('Corner'), Js('Cross'), Js('District'), Js('East'), Js('Garden'), Js('Grove'), Js('Heights'), Js('Hill'), Js('Hills'), Js('Market'), Js('North'), Js('Park'), Js('Place'), Js('Plaza'), Js('Point'), Js('Road'), Js('Row'), Js('Side'), Js('South'), Js('Square'), Js('Street'), Js('Town'), Js('Vale'), Js('Valley'), Js('West'), Js('Wood'), Js('Yard')]))
pass
pass


# Add lib to the module scope
districtNames = var.to_python()