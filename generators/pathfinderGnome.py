__all__ = ['pathfinderGnome']

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
                    while (var.get('rnd10')<Js(5.0)):
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    while (var.get('rnd12')<Js(5.0)):
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('nameLast', ((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm12').get(var.get('rnd12'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                    else:
                        if (var.get('i')<Js(9.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                        else:
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('names', ((((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd9')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(4.0)):
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
                        if (var.get('i')<Js(9.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                        else:
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('kr'), Js('n'), Js('p'), Js('q'), Js('r'), Js('shm'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ie'), Js('iu'), Js('ou'), Js('ee'), Js('uo'), Js('ua')]))
var.put('nm3', Js([Js('b'), Js('b'), Js('b'), Js('br'), Js('bn'), Js('ck'), Js('cr'), Js('cd'), Js('dp'), Js('dq'), Js('dw'), Js('k'), Js('k'), Js('k'), Js('kq'), Js('kr'), Js('kw'), Js('l'), Js('l'), Js('l'), Js('ll'), Js('ll'), Js('lm'), Js('lz'), Js('lb'), Js('ld'), Js('m'), Js('m'), Js('m'), Js('mb'), Js('mz'), Js('n'), Js('n'), Js('n'), Js('nn'), Js('nd'), Js('ndr'), Js('ng'), Js('nt'), Js('nz'), Js('nq'), Js('p'), Js('p'), Js('p'), Js('pq'), Js('pr'), Js('r'), Js('r'), Js('r'), Js('rgr'), Js('rn'), Js('rw'), Js('rz'), Js('shm'), Js('sht'), Js('sn'), Js('st'), Js('t'), Js('t'), Js('t'), Js('th'), Js('tq'), Js('tr'), Js('v'), Js('v'), Js('v'), Js('z'), Js('z'), Js('z'), Js('zz'), Js('zn')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('ck'), Js('d'), Js('m'), Js('n'), Js('nt'), Js('r'), Js('rd'), Js('s'), Js('st'), Js('t'), Js('tt'), Js('x')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('f'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sn'), Js('t'), Js('tr'), Js('y'), Js('v'), Js('w'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ue'), Js('io'), Js('ie'), Js('ia'), Js('ai')]))
var.put('nm7', Js([Js('b'), Js('b'), Js('b'), Js('b'), Js('bl'), Js('c'), Js('c'), Js('c'), Js('c'), Js('d'), Js('d'), Js('d'), Js('f'), Js('f'), Js('f'), Js('ff'), Js('ff'), Js('fl'), Js('fn'), Js('fr'), Js('fl'), Js('g'), Js('g'), Js('g'), Js('g'), Js('gn'), Js('gg'), Js('h'), Js('h'), Js('h'), Js('hh'), Js('hh'), Js('j'), Js('j'), Js('j'), Js('k'), Js('k'), Js('k'), Js('k'), Js('kn'), Js('kz'), Js('l'), Js('l'), Js('l'), Js('l'), Js('l'), Js('lm'), Js('ln'), Js('lz'), Js('lb'), Js('lf'), Js('m'), Js('m'), Js('m'), Js('m'), Js('mm'), Js('mm'), Js('mz'), Js('ml'), Js('mb'), Js('mp'), Js('n'), Js('n'), Js('n'), Js('n'), Js('nn'), Js('nk'), Js('np'), Js('nz'), Js('nl'), Js('ns'), Js('nk'), Js('p'), Js('p'), Js('p'), Js('p'), Js('ph'), Js('pr'), Js('pn'), Js('r'), Js('r'), Js('r'), Js('r'), Js('rz'), Js('rl'), Js('rs'), Js('rr'), Js('s'), Js('s'), Js('s'), Js('s'), Js('sh'), Js('sl'), Js('sn'), Js('sm'), Js('t'), Js('t'), Js('t'), Js('th'), Js('thr'), Js('tr'), Js('v'), Js('v'), Js('v'), Js('vr'), Js('vl'), Js('vn'), Js('x'), Js('x'), Js('x'), Js('z'), Js('z'), Js('z'), Js('z'), Js('zz'), Js('zn'), Js('zl')]))
var.put('nm8', Js([Js('ck'), Js('g'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('t'), Js('th')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('ch'), Js('d'), Js('f'), Js('fr'), Js('g'), Js('gl'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('kr'), Js('m'), Js('n'), Js('p'), Js('q'), Js('qr'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('w'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('ee'), Js('ae'), Js('oo'), Js('ie'), Js('ua'), Js('uo'), Js('io'), Js('ia')]))
var.put('nm11', Js([Js('b'), Js('bbl'), Js('bl'), Js('br'), Js('c'), Js('cl'), Js('cn'), Js('d'), Js('ddl'), Js('dl'), Js('dn'), Js('dr'), Js('df'), Js('gn'), Js('g'), Js('gl'), Js('ggl'), Js('gw'), Js('l'), Js('lp'), Js('lf'), Js('lb'), Js('ld'), Js('ldr'), Js('lm'), Js('ln'), Js('ll'), Js('m'), Js('mb'), Js('nd'), Js('n'), Js('nc'), Js('ngn'), Js('ns'), Js('nt'), Js('nz'), Js('p'), Js('pl'), Js('pp'), Js('ppl'), Js('pr'), Js('pn'), Js('psw'), Js('r'), Js('rl'), Js('rnd'), Js('rnf'), Js('sn'), Js('tr'), Js('th'), Js('tl'), Js('ttl'), Js('v'), Js('vr'), Js('w'), Js('wl'), Js('z'), Js('zb'), Js('zl')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bs'), Js('d'), Js('ck'), Js('cks'), Js('g'), Js('h'), Js('m'), Js('ms'), Js('n'), Js('ng'), Js('r'), Js('sp'), Js('ss'), Js('st'), Js('th')]))
pass
pass


# Add lib to the module scope
pathfinderGnome = var.to_python()