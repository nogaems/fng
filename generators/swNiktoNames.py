__all__ = ['swNiktoNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm9', 'nm10', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                while (var.get('rnd7')<Js(4.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                while (var.get('rnd10')<Js(5.0)):
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('namelast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            if (var.get('i')<Js(3.0)):
                while (var.get('rnd')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd4b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        if ((var.get('rnd6')<Js(20.0)) and (var.get('rnd3')<Js(32.0))):
                            while (var.get('rnd3b')<Js(32.0)):
                                var.put('rnd3b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        if ((var.get('rnd6')>Js(19.0)) or (var.get('rnd3')>Js(31.0))):
                            while (var.get('rnd3b')>Js(31.0)):
                                var.put('rnd3b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((((var.get('nm5').get(var.get('rnd6'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd3b')))+var.get('nm2').get(var.get('rnd4b')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bh'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('f'), Js('fh'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('kl'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sr'), Js('sl'), Js('t'), Js('ts'), Js('v'), Js('wl')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('au'), Js('oo'), Js('io'), Js('ia'), Js('ou'), Js('aa'), Js('ai'), Js('oi'), Js('ea')]))
var.put('nm3', Js([Js('b'), Js('bb'), Js('bd'), Js('d'), Js('dd'), Js('dr'), Js('dg'), Js('dr'), Js('g'), Js('gr'), Js('gg'), Js('gb'), Js('k'), Js('kt'), Js('kr'), Js('kn'), Js('kh'), Js('l'), Js('lf'), Js('ll'), Js('lv'), Js('m'), Js('n'), Js('nd'), Js('ndl'), Js('ndr'), Js('ng'), Js('ns'), Js('nt'), Js('r'), Js('rd'), Js('rk'), Js('rsk'), Js('s'), Js('sh'), Js('ss'), Js('t'), Js('th'), Js('v'), Js('x'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('d'), Js('gg'), Js('k'), Js('kk'), Js('kt'), Js('l'), Js('m'), Js('n'), Js('nc'), Js('nn'), Js('r'), Js('rsk'), Js('s'), Js('sh'), Js('sk'), Js('t'), Js('th'), Js('v'), Js('wl'), Js('x')]))
var.put('nm5', Js([Js("b'r"), Js("d'r"), Js("d'w"), Js("f'w"), Js("f'r"), Js("g'r"), Js("g'w"), Js("g'l"), Js("g'n"), Js("k'w"), Js("k'r"), Js("k'l"), Js("m'tr"), Js("n'r"), Js("n'tr"), Js("s'r"), Js("s'v"), Js("t'r"), Js("t'sr"), Js("v'r"), Js('b'), Js('bh'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('f'), Js('fh'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('kl'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sr'), Js('sl'), Js('t'), Js('ts'), Js('v'), Js('wl')]))
var.put('nm6', Js([Js("'b"), Js("'d"), Js("b'd"), Js("b'r"), Js("d'r"), Js("d'g"), Js("d'gr"), Js("g'b"), Js("g'r"), Js("'g"), Js("'j"), Js("'k"), Js("k'tr"), Js("k'r"), Js("k'n"), Js("l'v"), Js("l'm"), Js("l'r"), Js("'m"), Js("'n"), Js("n'dr"), Js("n'd"), Js("'p"), Js("'r"), Js("r'r"), Js("r'kr"), Js("r's"), Js("s'sh"), Js("s'th"), Js("'t"), Js("t'r"), Js("t'v"), Js('b'), Js('bb'), Js('bd'), Js('d'), Js('dd'), Js('dr'), Js('dg'), Js('dr'), Js('g'), Js('gr'), Js('gg'), Js('gb'), Js('k'), Js('kt'), Js('kr'), Js('kn'), Js('kh'), Js('l'), Js('lf'), Js('ll'), Js('lv'), Js('m'), Js('n'), Js('nd'), Js('ndl'), Js('ndr'), Js('ng'), Js('ns'), Js('nt'), Js('r'), Js('rd'), Js('rk'), Js('rsk'), Js('s'), Js('sh'), Js('ss'), Js('t'), Js('th'), Js('v'), Js('x'), Js('z')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ee'), Js('oo'), Js('uu'), Js('au'), Js('ou'), Js('oi'), Js('ai'), Js('ei')]))
var.put('nm11', Js([Js('b'), Js('cc'), Js('g'), Js('g'), Js('gg'), Js('gt'), Js('gn'), Js('gm'), Js('gl'), Js('gt'), Js('gr'), Js('k'), Js('kt'), Js('kk'), Js('kn'), Js('km'), Js('kl'), Js('m'), Js('mk'), Js('mp'), Js('mpl'), Js('n'), Js('nd'), Js('nk'), Js('ng'), Js('nt'), Js('p'), Js('pl'), Js('pt'), Js('r'), Js('rc'), Js('rk'), Js('rd'), Js('rt'), Js('rs'), Js('s'), Js('st'), Js('t'), Js('z')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('g'), Js('k'), Js('l'), Js('n'), Js('nn'), Js('nk'), Js('m'), Js('mk'), Js('rch'), Js('rk'), Js('rg'), Js('rc'), Js('rr'), Js('s'), Js('sh'), Js('sk'), Js('t'), Js('th'), Js('tt'), Js('x')]))
pass
pass


# Add lib to the module scope
swNiktoNames = var.to_python()