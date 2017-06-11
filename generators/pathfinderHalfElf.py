__all__ = ['pathfinderHalfElf']

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
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if (PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)) and ((var.get('i')%Js(2.0))!=Js(0.0))):
                var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('nameLast', ((((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd14')))+var.get('nm12').get(var.get('rnd12'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('nameLast', ((((((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm10').get(var.get('rnd14')))+var.get('nm11').get(var.get('rnd15')))+var.get('nm10').get(var.get('rnd16')))+var.get('nm12').get(var.get('rnd12'))))
                else:
                    while (var.get('rnd10')<Js(4.0)):
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    while (var.get('rnd12')<Js(7.0)):
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('nameLast', ((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm12').get(var.get('rnd12'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(3.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('nameLast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('jh'), Js('k'), Js('kh'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('z'), Js('zr')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('y'), Js('ai'), Js('ae'), Js('ia'), Js('ue'), Js('ie'), Js('ui')]))
var.put('nm3', Js([Js('d'), Js('d'), Js('d'), Js('dr'), Js('dl'), Js('dw'), Js('g'), Js('g'), Js('g'), Js('gr'), Js('gl'), Js('gg'), Js('gw'), Js('l'), Js('l'), Js('l'), Js('l'), Js('ld'), Js('lv'), Js('lgr'), Js('lbr'), Js('lc'), Js('ldr'), Js('lg'), Js('lgg'), Js('lr'), Js('lt'), Js('lth'), Js('m'), Js('m'), Js('m'), Js('mr'), Js('ml'), Js('n'), Js('n'), Js('n'), Js('nc'), Js('nn'), Js('nr'), Js('nd'), Js('ngr'), Js('nv'), Js('nvr'), Js('r'), Js('r'), Js('r'), Js('rc'), Js('rg'), Js('rr'), Js('rth'), Js('rv'), Js('rvr'), Js('rl'), Js('rd'), Js('rdr'), Js('rgr'), Js('rw'), Js('s'), Js('s'), Js('s'), Js('sh'), Js('sl'), Js('sr'), Js('ss'), Js('st'), Js('str'), Js('svr'), Js('t'), Js('t'), Js('t'), Js('th'), Js('tt'), Js('tr')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('c'), Js('h'), Js('k'), Js('l'), Js('n'), Js('nn'), Js('r'), Js('s')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('d'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('thr'), Js('th'), Js('tr'), Js('v'), Js('vr'), Js('vh'), Js('z'), Js('zr'), Js('zh')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('au'), Js('ie'), Js('ua'), Js('oi'), Js('ou'), Js('ae')]))
var.put('nm7', Js([Js('b'), Js('b'), Js('br'), Js('cl'), Js('cr'), Js('d'), Js('d'), Js('gs'), Js('gl'), Js('gn'), Js('gm'), Js('gsh'), Js('l'), Js('l'), Js('l'), Js('lm'), Js('lr'), Js('lsr'), Js('ltr'), Js('ly'), Js('lly'), Js('ld'), Js('ll'), Js('lsb'), Js('lv'), Js('m'), Js('m'), Js('m'), Js('my'), Js('mr'), Js('n'), Js('n'), Js('n'), Js('nd'), Js('nr'), Js('nw'), Js('nn'), Js('ns'), Js('nv'), Js('ny'), Js('pt'), Js('pr'), Js('r'), Js('r'), Js('r'), Js('r'), Js('rg'), Js('rr'), Js('rl'), Js('rv'), Js('ry'), Js('s'), Js('s'), Js('s'), Js('ss'), Js('sy'), Js('str'), Js('sw'), Js('thr'), Js('tr'), Js('th'), Js('y'), Js('y'), Js('y')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n'), Js('s'), Js('ss'), Js('th')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('cl'), Js('d'), Js('dr'), Js('f'), Js('fl'), Js('fr'), Js('g'), Js('gl'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('s'), Js('sl'), Js('sk'), Js('st'), Js('t'), Js('tr'), Js('wr'), Js('y'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('io'), Js('ei'), Js('iu'), Js('ai'), Js('ea'), Js('ee')]))
var.put('nm11', Js([Js('d'), Js('d'), Js('d'), Js('dr'), Js('dw'), Js('gr'), Js('gw'), Js('gn'), Js('g'), Js('g'), Js('gg'), Js('h'), Js('h'), Js('h'), Js('j'), Js('j'), Js('j'), Js('k'), Js('k'), Js('k'), Js('kr'), Js('kl'), Js('km'), Js('kn'), Js('l'), Js('l'), Js('ll'), Js('l'), Js('lr'), Js('lg'), Js('ld'), Js('ldr'), Js('lmr'), Js('ly'), Js('m'), Js('mg'), Js('mr'), Js('m'), Js('m'), Js('m'), Js('n'), Js('n'), Js('n'), Js('nn'), Js('n'), Js('nr'), Js('ng'), Js('ngr'), Js('ndr'), Js('nd'), Js('nsh'), Js('ntr'), Js('r'), Js('r'), Js('r'), Js('r'), Js('rr'), Js('rd'), Js('rdr'), Js('rg'), Js('rgr'), Js('rl'), Js('rm'), Js('rt'), Js('s'), Js('s'), Js('s'), Js('sdr'), Js('sgr'), Js('sg'), Js('sh'), Js('ssr'), Js('t'), Js('tr'), Js('t'), Js('t'), Js('th'), Js('v'), Js('v'), Js('vr'), Js('vl'), Js('w'), Js('xh'), Js('xt'), Js('y'), Js('yh'), Js('zm')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('ht'), Js('l'), Js('m'), Js('n'), Js('nd'), Js('nn'), Js('r'), Js('rks'), Js('rt'), Js('s'), Js('th'), Js('w'), Js('ys')]))
pass
pass


# Add lib to the module scope
pathfinderHalfElf = var.to_python()