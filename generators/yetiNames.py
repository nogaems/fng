__all__ = ['yetiNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm4b', 'nm7', 'nm9', 'nm10', 'nm13', 'nm2', 'nm6'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(6.0)):
                    while PyJsStrictEq(var.get('nm5').get(var.get('rnd')),var.get('nm7').get(var.get('rnd3'))):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    if (var.get('rnd')<Js(5.0)):
                        while ((var.get('rnd5')<Js(15.0)) or PyJsStrictEq(var.get('nm7').get(var.get('rnd3')),var.get('nm8').get(var.get('rnd5')))):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        while PyJsStrictEq(var.get('nm5').get(var.get('rnd')),var.get('nm7').get(var.get('rnd3'))):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm8').get(var.get('rnd5'))):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm7').get(var.get('rnd3'))):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        while PyJsStrictEq(var.get('nm5').get(var.get('rnd')),var.get('nm7').get(var.get('rnd3'))):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        while PyJsStrictEq(var.get('nm7').get(var.get('rnd3')),var.get('nm8').get(var.get('rnd5'))):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm7').get(var.get('rnd3'))):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    if (var.get('i')<Js(6.0)):
                        while PyJsStrictEq(var.get('nm10').get(var.get('rnd')),var.get('nm12').get(var.get('rnd3'))):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        if (var.get('rnd')<Js(5.0)):
                            while ((var.get('rnd5')<Js(15.0)) or PyJsStrictEq(var.get('nm12').get(var.get('rnd3')),var.get('nm13').get(var.get('rnd5')))):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('names', ((((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd5'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                            while PyJsStrictEq(var.get('nm10').get(var.get('rnd')),var.get('nm12').get(var.get('rnd3'))):
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                            while PyJsStrictEq(var.get('nm14').get(var.get('rnd6')),var.get('nm13').get(var.get('rnd5'))):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                            while PyJsStrictEq(var.get('nm14').get(var.get('rnd6')),var.get('nm12').get(var.get('rnd3'))):
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                            var.put('names', ((((((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm11').get(var.get('rnd7')))+var.get('nm13').get(var.get('rnd5'))))
                        else:
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                            while PyJsStrictEq(var.get('nm10').get(var.get('rnd')),var.get('nm12').get(var.get('rnd3'))):
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                            while PyJsStrictEq(var.get('nm14').get(var.get('rnd6')),var.get('nm13').get(var.get('rnd5'))):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                            while PyJsStrictEq(var.get('nm14').get(var.get('rnd6')),var.get('nm12').get(var.get('rnd3'))):
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                            var.put('names', ((((((var.get('nm10').get(var.get('rnd'))+var.get('nm11').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm11').get(var.get('rnd7')))+var.get('nm12').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(5.0)):
                        while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        if (var.get('rnd')<Js(5.0)):
                            while ((var.get('rnd5')<Js(2.0)) or PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd5')))):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                    else:
                        if (var.get('i')<Js(8.0)):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4b').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            while PyJsStrictEq(var.get('nm4b').get(var.get('rnd6')),var.get('nm4').get(var.get('rnd5'))):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                            while PyJsStrictEq(var.get('nm4b').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))):
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4b').get('length'))))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4b').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5'))))
                        else:
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4b').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm3').get(var.get('rnd3'))):
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd5'))):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                            while PyJsStrictEq(var.get('nm4b').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))):
                                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4b').get('length'))))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4b').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ch'), Js('dz'), Js('dj'), Js('g'), Js('gy'), Js('h'), Js('j'), Js('k'), Js('ky'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sz'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('dd'), Js('h'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('z'), Js('dd'), Js('h'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('lr'), Js('m'), Js('n'), Js('ng'), Js('nr'), Js('nz'), Js('r'), Js('rr'), Js('s'), Js('sh'), Js('sr'), Js('t'), Js('ts'), Js('vr'), Js('y'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js('c'), Js('hn'), Js('hl'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('r'), Js('rs'), Js('s'), Js('sh')]))
var.put('nm4b', Js([Js('h'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('gy'), Js('h'), Js('k'), Js('ky'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('th'), Js('w'), Js('y'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i')]))
var.put('nm7', Js([Js('b'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('rr'), Js('s'), Js('t'), Js('w'), Js('z'), Js('b'), Js('f'), Js('g'), Js('gy'), Js('h'), Js('hn'), Js('hl'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('ng'), Js('nn'), Js('r'), Js('rr'), Js('rl'), Js('ry'), Js('rs'), Js('s'), Js('sh'), Js('t'), Js('ty'), Js('th'), Js('w'), Js('z')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('hn'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('ph'), Js('s'), Js('sh'), Js('th'), Js('y')]))
var.put('nm9', Js([Js('b'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('rr'), Js('s'), Js('t'), Js('w'), Js('z')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('g'), Js('gy'), Js('h'), Js('k'), Js('ky'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('th'), Js('v'), Js('w'), Js('y'), Js('z')]))
var.put('nm11', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a')]))
var.put('nm12', Js([Js('b'), Js('dd'), Js('g'), Js('h'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('t'), Js('w'), Js('y'), Js('z'), Js('b'), Js('dd'), Js('g'), Js('gy'), Js('h'), Js('hn'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('lr'), Js('m'), Js('n'), Js('ng'), Js('nn'), Js('nr'), Js('r'), Js('rr'), Js('ry'), Js('s'), Js('sh'), Js('sr'), Js('t'), Js('th'), Js('ts'), Js('vr'), Js('w'), Js('y'), Js('z')]))
var.put('nm13', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('hl'), Js('hn'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('ph'), Js('r'), Js('rs'), Js('s'), Js('sh'), Js('th')]))
var.put('nm14', Js([Js('b'), Js('dd'), Js('g'), Js('h'), Js('k'), Js('kk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('t'), Js('w'), Js('y'), Js('z')]))
pass
pass


# Add lib to the module scope
yetiNames = var.to_python()