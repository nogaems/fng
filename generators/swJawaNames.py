__all__ = ['swJawaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2'])
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
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if (PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)) and ((var.get('i')%Js(2.0))!=Js(0.0))):
                while (var.get('rnd7')<Js(4.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                while (var.get('rnd10')<Js(5.0)):
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('namelast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm2').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm2').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
                else:
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('namelast', ((((((var.get('nm9').get(var.get('rnd7'))+var.get('nm2').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd13')))+var.get('nm2').get(var.get('rnd12')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5b')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5b')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('brr'), Js('ch'), Js('d'), Js('h'), Js('hr'), Js('j'), Js('k'), Js('kl'), Js('kr'), Js('kt'), Js('m'), Js('mn'), Js('n'), Js('nb'), Js('p'), Js('pl'), Js('pr'), Js('r'), Js('rk'), Js('sn'), Js('sq'), Js('t'), Js('th'), Js('tt'), Js('ts'), Js('v'), Js('w'), Js('wr'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('oe'), Js('ee'), Js('ii'), Js('ee'), Js('ia'), Js('ui'), Js('eo')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('bl'), Js('bw'), Js('d'), Js('g'), Js('j'), Js('k'), Js("k't"), Js("k'ch"), Js("k'k"), Js('kch'), Js('kk'), Js('kt'), Js('kth'), Js('l'), Js('lh'), Js('lv'), Js('m'), Js('n'), Js('ng'), Js('nz'), Js('pt'), Js('r'), Js('rk'), Js('s'), Js('ss'), Js('t'), Js('th'), Js('thch'), Js('tj'), Js('tk'), Js('tt'), Js('ttj'), Js('z'), Js('zj'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('dt'), Js('g'), Js('h'), Js('k'), Js('kk'), Js('kth'), Js('l'), Js('n'), Js('nk'), Js('nt'), Js('pp'), Js('r'), Js('s'), Js('t'), Js('th'), Js('tk'), Js('w'), Js('x'), Js('zz')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('bl'), Js('ch'), Js('dh'), Js('d'), Js('h'), Js('k'), Js('kh'), Js('kw'), Js('kl'), Js('kn'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('r'), Js('rh'), Js('rw'), Js('s'), Js('sh'), Js('sn'), Js('sl'), Js('th'), Js('ts'), Js('tw'), Js('v'), Js('vl'), Js('w'), Js('wh')]))
var.put('nm7', Js([Js('b'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('t')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js("b'"), Js('b'), Js("d'n"), Js('d'), Js('f'), Js('h'), Js('j'), Js('k'), Js("k'"), Js('kl'), Js('kr'), Js('kk'), Js('l'), Js('m'), Js("m'"), Js('nk'), Js('n'), Js('p'), Js('pt'), Js('q'), Js("q'"), Js('s'), Js('t'), Js('tl'), Js('th'), Js('w')]))
var.put('nm11', Js([Js('c'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('hs'), Js('k'), Js('kt'), Js('kth'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('y'), Js('z')]))
pass
pass


# Add lib to the module scope
swJawaNames = var.to_python()