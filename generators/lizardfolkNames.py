__all__ = ['lizardfolkNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(6.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    while (var.get('rnd3')<Js(4.0)):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3'))))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm10').get(var.get('rnd3')),var.get('nm8').get(var.get('rnd5'))):
                            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                        var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd3'))))
                    else:
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm10').get(var.get('rnd3')),var.get('nm8').get(var.get('rnd5'))):
                            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd7')),var.get('nm8').get(var.get('rnd5'))):
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        if (var.get('i')<Js(8.0)):
                            var.put('names', ((((((var.get('nm6').get(var.get('rnd7'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd3'))))
                        else:
                            var.put('names', ((((((var.get('nm6').get(var.get('rnd7'))+var.get('nm7').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm10').get(var.get('rnd3'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(3.0)):
                        while (var.get('rnd')<Js(4.0)):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        while (var.get('rnd3')<Js(4.0)):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm15').get(var.get('rnd3'))))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                            while PyJsStrictEq(var.get('nm12').get(var.get('rnd3')),var.get('nm13').get(var.get('rnd5'))):
                                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                            var.put('names', ((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd5')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd3'))))
                        else:
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                            while PyJsStrictEq(var.get('nm15').get(var.get('rnd3')),var.get('nm13').get(var.get('rnd5'))):
                                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                            while PyJsStrictEq(var.get('nm14').get(var.get('rnd7')),var.get('nm13').get(var.get('rnd5'))):
                                var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                            if (var.get('i')<Js(8.0)):
                                var.put('names', ((((((var.get('nm11').get(var.get('rnd7'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd7')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd5')))+var.get('nm12').get(var.get('rnd6')))+var.get('nm15').get(var.get('rnd3'))))
                            else:
                                var.put('names', ((((((var.get('nm11').get(var.get('rnd7'))+var.get('nm12').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd5')))+var.get('nm12').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd7')))+var.get('nm12').get(var.get('rnd6')))+var.get('nm15').get(var.get('rnd3'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(3.0)):
                        while (var.get('rnd')<Js(4.0)):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                        while (var.get('rnd3')<Js(3.0)):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                            while PyJsStrictEq(var.get('nm2').get(var.get('rnd3')),var.get('nm3').get(var.get('rnd5'))):
                                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd3'))))
                        else:
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                            while PyJsStrictEq(var.get('nm5').get(var.get('rnd3')),var.get('nm3').get(var.get('rnd5'))):
                                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                            while PyJsStrictEq(var.get('nm4').get(var.get('rnd7')),var.get('nm3').get(var.get('rnd5'))):
                                var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                            if (var.get('i')<Js(8.0)):
                                var.put('names', ((((((var.get('nm1').get(var.get('rnd7'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd3'))))
                            else:
                                var.put('names', ((((((var.get('nm1').get(var.get('rnd7'))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('bh'), Js('br'), Js('ch'), Js('dr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('q'), Js('qr'), Js('r'), Js('rh'), Js('th'), Js('thr'), Js('tr'), Js('v'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('ao'), Js('au'), Js('ou'), Js('iu'), Js('oa'), Js('ua'), Js('uu')]))
var.put('nm3', Js([Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kz'), Js('kx'), Js('kn'), Js('lt'), Js('ll'), Js('m'), Js('mz'), Js('nt'), Js('nj'), Js('r'), Js('rq'), Js('rs'), Js('rz'), Js('rn'), Js('rl'), Js('sh'), Js('sz'), Js('shr'), Js('szr'), Js('t'), Js('tt'), Js('th'), Js('tr'), Js('thr'), Js('tz'), Js('tsz'), Js('tl'), Js('x'), Js('xl'), Js('z'), Js('zz')]))
var.put('nm4', Js([Js('c'), Js('cc'), Js('ch'), Js('g'), Js('j'), Js('k'), Js('kk'), Js('q'), Js('x'), Js('xx'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('k'), Js('sz'), Js('sk'), Js('shk'), Js('t'), Js('x'), Js('xl'), Js('z'), Js('zk')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('cr'), Js('ch'), Js('d'), Js('dh'), Js('dr'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('kr'), Js('q'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('sr'), Js('shr'), Js('th'), Js('thr'), Js('y'), Js('z')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('ae'), Js('ie'), Js('ia'), Js('ei')]))
var.put('nm8', Js([Js('c'), Js('cc'), Js('ch'), Js('d'), Js('dr'), Js('g'), Js('gn'), Js('gz'), Js('gy'), Js('k'), Js('kk'), Js('kr'), Js('kz'), Js('kl'), Js('kn'), Js('lq'), Js('lz'), Js('n'), Js('nq'), Js('nr'), Js('nz'), Js('r'), Js('rs'), Js('rq'), Js('rt'), Js('rz'), Js('rsh'), Js('rzh'), Js('t'), Js('tt'), Js('th'), Js('thr'), Js('thl'), Js('tl'), Js('z'), Js('zd')]))
var.put('nm9', Js([Js('c'), Js('j'), Js('k'), Js('q'), Js('r'), Js('s'), Js('t'), Js('x'), Js('y'), Js('z')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js('h'), Js('s'), Js('sk'), Js('ss'), Js('x'), Js('z')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('d'), Js('dr'), Js('j'), Js('k'), Js('kh'), Js('kr'), Js('q'), Js('r'), Js('rh'), Js('sr'), Js('shr'), Js('th'), Js('thr'), Js('y'), Js('z')]))
var.put('nm12', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('u'), Js('u'), Js('u'), Js('ae'), Js('ia'), Js('ao'), Js('au'), Js('ou'), Js('oa')]))
var.put('nm13', Js([Js('g'), Js('gr'), Js('k'), Js('kk'), Js('kz'), Js('kl'), Js('kn'), Js('lz'), Js('r'), Js('rs'), Js('rq'), Js('rt'), Js('rz'), Js('t'), Js('tt'), Js('th'), Js('thr'), Js('tl'), Js('z'), Js('zd')]))
var.put('nm14', Js([Js('c'), Js('j'), Js('k'), Js('q'), Js('r'), Js('t'), Js('x'), Js('z')]))
var.put('nm15', Js([Js(''), Js(''), Js(''), Js(''), Js('s'), Js('sk'), Js('ss'), Js('x'), Js('xl'), Js('z')]))
pass
pass


# Add lib to the module scope
lizardfolkNames = var.to_python()