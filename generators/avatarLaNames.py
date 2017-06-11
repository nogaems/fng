__all__ = ['avatarLaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm19b', 'nm1', 'nm11', 'nm24', 'nm16', 'nm23', 'nm3', 'nm2', 'nm27', 'nm26', 'nm22', 'nm14', 'nm7', 'nm10', 'nm21', 'nm25', 'nm15', 'nm20', 'nm12', 'nm5', 'nm6', 'nm4', 'nameGen', 'nm8', 'nm18', 'nm17', 'nm13', 'nm9'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(12.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(3.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('names', (((((var.get('nm12').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd3')))+var.get('nm13').get(var.get('rnd4')))+var.get('nm14').get(var.get('rnd5')))+var.get('nm13').get(var.get('rnd6'))))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                            var.put('names', (((var.get('nm12').get(var.get('rnd'))+var.get('nm13').get(var.get('rnd2')))+var.get('nm14').get(var.get('rnd3')))+var.get('nm13').get(var.get('rnd4'))))
                        else:
                            if (var.get('i')<Js(7.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length'))))
                                var.put('names', ((((var.get('nm19').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm20').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm21').get(var.get('rnd5'))))
                            else:
                                if (var.get('i')<Js(9.0)):
                                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19b').get('length'))))
                                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length'))))
                                    var.put('names', ((var.get('nm19b').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm21').get(var.get('rnd3'))))
                                else:
                                    if (var.get('i')<Js(10.0)):
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length'))))
                                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                        var.put('names', (((((var.get('nm25').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm26').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm26').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6'))))
                                    else:
                                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                        var.put('names', ((var.get('nm25').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd3'))))
            else:
                if (var.get('i')<Js(3.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('names', ((((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5'))))
                    else:
                        if (var.get('i')<Js(7.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                            if (var.get('rnd2')<Js(3.0)):
                                while (var.get('rnd4')<Js(3.0)):
                                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                            var.put('names', ((((var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2')))+var.get('nm17').get(var.get('rnd3')))+var.get('nm16').get(var.get('rnd4')))+var.get('nm18').get(var.get('rnd5'))))
                        else:
                            if (var.get('i')<Js(9.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                                var.put('names', ((var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2')))+var.get('nm18').get(var.get('rnd3'))))
                            else:
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm23').get('length'))))
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length'))))
                                if (var.get('rnd')<Js(2.0)):
                                    while (var.get('rnd5')<Js(2.0)):
                                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length'))))
                                var.put('names', ((((var.get('nm22').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm23').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm24').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('gy'), Js('p'), Js('r'), Js('s'), Js('t')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o')]))
var.put('nm3', Js([Js('h'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('ng'), Js('nz'), Js('r'), Js('s'), Js('sh'), Js('ts')]))
var.put('nm4', Js([Js(''), Js('hn'), Js('l'), Js('ng'), Js('n')]))
var.put('nm5', Js([Js(''), Js('h'), Js('l'), Js('n'), Js('m'), Js('p'), Js('r'), Js('s'), Js('y')]))
var.put('nm6', Js([Js('h'), Js('l'), Js('m'), Js('ng'), Js('n'), Js('sh'), Js('r'), Js('rr')]))
var.put('nm7', Js([Js(''), Js(''), Js('hn'), Js('h'), Js('n')]))
var.put('nm8', Js([Js('h'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm9', Js([Js('a'), Js('i'), Js('o')]))
var.put('nm10', Js([Js('cc'), Js('dd'), Js('kk'), Js('lr'), Js('sr'), Js('nr'), Js('rr'), Js('vr')]))
var.put('nm11', Js([Js(''), Js(''), Js('ck'), Js('k'), Js('r'), Js('m'), Js('n'), Js('s')]))
var.put('nm12', Js([Js('h'), Js('k'), Js('r'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm13', Js([Js('a'), Js('i'), Js('o')]))
var.put('nm14', Js([Js('h'), Js('k'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('t')]))
var.put('nm15', Js([Js('ch'), Js('b'), Js('f'), Js('g'), Js('h'), Js('l'), Js('m'), Js('p'), Js('r'), Js('sh'), Js('x')]))
var.put('nm16', Js([Js('ao'), Js('uo'), Js('aa'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm17', Js([Js('h'), Js('l'), Js('m'), Js('n'), Js('sh'), Js('t')]))
var.put('nm18', Js([Js(''), Js(''), Js(''), Js('h'), Js('ng'), Js('n'), Js('r')]))
var.put('nm19', Js([Js(''), Js(''), Js('b'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('n'), Js('m'), Js('s'), Js('sh'), Js('t'), Js('w')]))
var.put('nm19b', Js([Js('b'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('n'), Js('m'), Js('s'), Js('sh'), Js('t'), Js('w')]))
var.put('nm20', Js([Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('sh'), Js('v'), Js('y')]))
var.put('nm21', Js([Js(''), Js(''), Js('ph'), Js('h'), Js('ng'), Js('n')]))
var.put('nm22', Js([Js(''), Js(''), Js('ch'), Js('d'), Js('j'), Js('m'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('y'), Js('z')]))
var.put('nm23', Js([Js('d'), Js('g'), Js('k'), Js('m'), Js('r'), Js('z')]))
var.put('nm24', Js([Js(''), Js(''), Js('h'), Js('k'), Js('m'), Js('n'), Js('ng'), Js('w')]))
var.put('nm25', Js([Js(''), Js(''), Js('ch'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('t'), Js('y'), Js('z')]))
var.put('nm26', Js([Js('k'), Js('l'), Js('rs'), Js('s'), Js('z')]))
var.put('nm27', Js([Js(''), Js(''), Js('ch'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('t'), Js('y'), Js('z')]))
pass
pass


# Add lib to the module scope
avatarLaNames = var.to_python()