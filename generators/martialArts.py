__all__ = ['martialArts']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm18', 'nm14', 'nm17', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm20', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('rnd2')>Js(4.0)):
                    while (var.get('rnd4')>Js(4.0)):
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if ((var.get('rnd2')>Js(4.0)) or (var.get('rnd4')>Js(4.0))):
                    while (var.get('rnd6')>Js(4.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6'))))
            else:
                if PyJsStrictEq(var.get('i'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    if (var.get('rnd2')>Js(20.0)):
                        while (var.get('rnd4')>Js(22.0)):
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    if (var.get('rnd4')<Js(2.0)):
                        var.put('rnd5', Js(0.0))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if ((var.get('rnd2')>Js(20.0)) or (var.get('rnd4')>Js(22.0))):
                        while (var.get('rnd6')>Js(20.0)):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', (((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6'))))
                else:
                    if PyJsStrictEq(var.get('i'),Js(3.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('names', ((((((((var.get('nm4').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd8')))+var.get('nm5').get(var.get('rnd9'))))
                    else:
                        if PyJsStrictEq(var.get('i'),Js(4.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                            if PyJsStrictEq(var.get('rnd4'),Js(0.0)):
                                var.put('rnd5', Js(0.0))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                            var.put('names', ((((((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd3')))+var.get('nm13').get(var.get('rnd4')))+var.get('nm14').get(var.get('rnd5')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm15').get(var.get('rnd7'))))
                        else:
                            if (var.get('i')<Js(7.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                                var.put('names', ((((var.get('nm16').get(var.get('rnd'))+var.get('nm17').get(var.get('rnd2')))+var.get('nm18').get(var.get('rnd3')))+var.get('nm17').get(var.get('rnd4')))+var.get('nm19').get(var.get('rnd5'))))
                            else:
                                if PyJsStrictEq(var.get('i'),Js(7.0)):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                    if ((var.get('rnd2')>Js(24.0)) or (var.get('rnd4')>Js(24.0))):
                                        while (var.get('rnd6')>Js(24.0)):
                                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                                    var.put('names', ((((((var.get('nm16').get(var.get('rnd'))+var.get('nm17').get(var.get('rnd2')))+var.get('nm18').get(var.get('rnd3')))+var.get('nm17').get(var.get('rnd4')))+var.get('nm18').get(var.get('rnd5')))+var.get('nm17').get(var.get('rnd6')))+var.get('nm19').get(var.get('rnd7'))))
                                else:
                                    if PyJsStrictEq(var.get('i'),Js(8.0)):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                                        if (var.get('rnd')<Js(3.0)):
                                            while (var.get('rnd3')<Js(12.0)):
                                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                                        var.put('names', ((((((((var.get('nm16').get(var.get('rnd'))+var.get('nm17').get(var.get('rnd2')))+var.get('nm19').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm16').get(var.get('rnd5')))+var.get('nm17').get(var.get('rnd6')))+var.get('nm18').get(var.get('rnd7')))+var.get('nm17').get(var.get('rnd8')))+var.get('nm19').get(var.get('rnd9'))))
                                    else:
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                                        if (var.get('rnd')<Js(3.0)):
                                            while (var.get('rnd3')<Js(12.0)):
                                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                                        var.put('names', ((((((((var.get('nm16').get(var.get('rnd5'))+var.get('nm17').get(var.get('rnd6')))+var.get('nm18').get(var.get('rnd7')))+var.get('nm17').get(var.get('rnd8')))+var.get('nm19').get(var.get('rnd9')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm16').get(var.get('rnd')))+var.get('nm17').get(var.get('rnd2')))+var.get('nm19').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js('b'), Js('d'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('s'), Js('t'), Js('w')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('ai'), Js('oa'), Js('oe')]))
var.put('nm3', Js([Js('b'), Js('gw'), Js('hn'), Js('hl'), Js('ht'), Js('l'), Js('mb'), Js('n'), Js('nt'), Js('nd'), Js('ng'), Js('ngw'), Js('r'), Js('rm'), Js('s')]))
var.put('nm4', Js([Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('cr'), Js('ch'), Js('d'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('sh'), Js('st'), Js('v'), Js('w')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oei'), Js('ou'), Js('ee'), Js('oo'), Js('ea'), Js('eo'), Js('ue'), Js('ua'), Js('ia')]))
var.put('nm6', Js([Js('c'), Js('ch'), Js('d'), Js('gr'), Js('j'), Js('k'), Js('l'), Js('m'), Js('mp'), Js('n'), Js('nch'), Js('nd'), Js('nz'), Js('nt'), Js('nk'), Js('p'), Js('q'), Js('st'), Js('r'), Js('rt'), Js('t'), Js('v')]))
var.put('nm7', Js([Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oei'), Js('ou'), Js('ee'), Js('oo'), Js('ea'), Js('eo'), Js('ue'), Js('ua'), Js('ia')]))
var.put('nm8', Js([Js(''), Js(''), Js('c'), Js('ch'), Js('d'), Js('gr'), Js('j'), Js('k'), Js('l'), Js('m'), Js('mp'), Js('n'), Js('nch'), Js('nd'), Js('nz'), Js('nt'), Js('nk'), Js('p'), Js('q'), Js('st'), Js('r'), Js('rt'), Js('t'), Js('v')]))
var.put('nm9', Js([Js(' '), Js('-')]))
var.put('nm10', Js([Js('b'), Js('d'), Js('f'), Js('h'), Js('k'), Js('khr'), Js('s'), Js('t'), Js('m'), Js('n'), Js('p'), Js('q'), Js('v')]))
var.put('nm11', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm12', Js([Js('c'), Js('d'), Js('df'), Js('dh'), Js('fr'), Js('g'), Js('j'), Js('ht'), Js('k'), Js('kh'), Js('l'), Js('nh'), Js('m'), Js('p'), Js('r'), Js('rs'), Js('sw'), Js('sth'), Js('st'), Js('z')]))
var.put('nm13', Js([Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm14', Js([Js(''), Js(''), Js('c'), Js('d'), Js('df'), Js('dh'), Js('fr'), Js('g'), Js('j'), Js('ht'), Js('k'), Js('kh'), Js('l'), Js('nh'), Js('m'), Js('p'), Js('r'), Js('rs'), Js('sw'), Js('sth'), Js('st'), Js('z')]))
var.put('nm15', Js([Js(''), Js(''), Js('b'), Js('f'), Js('g'), Js('h'), Js('hr'), Js('hn'), Js('k'), Js('m'), Js('n'), Js('p'), Js('r'), Js('sh')]))
var.put('nm16', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('c'), Js('g'), Js('gw'), Js('gy'), Js('h'), Js('hw'), Js('j'), Js('k'), Js('kb'), Js('kr'), Js('ky'), Js('l'), Js('m'), Js('nh'), Js('ny'), Js('p'), Js('pr'), Js('sh'), Js('s'), Js('t'), Js('th'), Js('v'), Js('w'), Js('y')]))
var.put('nm17', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('oi'), Js('ae'), Js('eo'), Js('ua'), Js('ai'), Js('ia'), Js('ei'), Js('oo'), Js('aa'), Js('ou'), Js('ee')]))
var.put('nm18', Js([Js('b'), Js('by'), Js('chk'), Js('ch'), Js('d'), Js('ddh'), Js('dh'), Js('hlw'), Js('hw'), Js('j'), Js('k'), Js('km'), Js('kn'), Js('kw'), Js('ky'), Js('l'), Js('lg'), Js('ll'), Js('mb'), Js('md'), Js('mp'), Js('n'), Js('nb'), Js('nd'), Js('ng'), Js('ngd'), Js('nj'), Js('nk'), Js('nsh'), Js('nt'), Js('p'), Js('pk'), Js('pp'), Js('r'), Js('rn'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('thw'), Js('tk'), Js('ts'), Js('tt'), Js('y')]))
var.put('nm19', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('k'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('r'), Js('s'), Js('t'), Js('w'), Js('y')]))
var.put('nm20', Js([]))
pass
pass


# Add lib to the module scope
martialArts = var.to_python()