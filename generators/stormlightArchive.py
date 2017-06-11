__all__ = ['stormlightArchive']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm24', 'nm29', 'nm16', 'nm23', 'nm31', 'nm3', 'nm33', 'nm34', 'nm2', 'nm27', 'nm26', 'nm30', 'nm22', 'nm14', 'nm7', 'nm10', 'nm21', 'nm25', 'nm15', 'nm20', 'nm12', 'nm32', 'nm5', 'nm6', 'nm4', 'nameGen', 'nm8', 'nm28', 'nm18', 'nm17', 'nm13', 'nm9'])
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
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                if (var.get('rnd6')<Js(6.0)):
                    var.put('rnd7', Js(0.0))
                else:
                    while (var.get('rnd7')<Js(6.0)):
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                var.put('lname', ((((((((var.get('nm9').get(var.get('rnd'))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5')))+var.get('nm12').get(var.get('rnd6')))+var.get('nm13').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd8')))+var.get('nm14').get(var.get('rnd9'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm23').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm25').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm26').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                    if (var.get('rnd6')<Js(1.0)):
                        var.put('rnd7', Js(0.0))
                    else:
                        while (var.get('rnd7')<Js(1.0)):
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm27').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm24').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm28').get('length'))))
                    var.put('sname', ((((((((var.get('nm23').get(var.get('rnd'))+var.get('nm24').get(var.get('rnd2')))+var.get('nm25').get(var.get('rnd3')))+var.get('nm24').get(var.get('rnd4')))+var.get('nm25').get(var.get('rnd5')))+var.get('nm26').get(var.get('rnd6')))+var.get('nm27').get(var.get('rnd7')))+var.get('nm24').get(var.get('rnd8')))+var.get('nm28').get(var.get('rnd9'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    while (var.get('rnd')<Js(3.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+Js(' '))+var.get('lname')))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('lname')))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length'))))
                            while (var.get('rnd')<Js(3.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                            while (var.get('rnd3')<Js(6.0)):
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                            var.put('names', (((((var.get('nm19').get(var.get('rnd'))+var.get('nm20').get(var.get('rnd2')))+var.get('nm22').get(var.get('rnd3')))+var.get('nm20').get(var.get('rnd4')))+Js(' '))+var.get('sname')))
                        else:
                            if (var.get('i')<Js(7.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length'))))
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm22').get('length'))))
                                var.put('names', ((((((var.get('nm19').get(var.get('rnd'))+var.get('nm20').get(var.get('rnd2')))+var.get('nm21').get(var.get('rnd3')))+var.get('nm20').get(var.get('rnd4')))+var.get('nm22').get(var.get('rnd5')))+Js(' '))+var.get('sname')))
                            else:
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm32').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm33').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm34').get('length'))))
                                var.put('names', ((var.get('nm32').get(var.get('rnd'))+var.get('nm33').get(var.get('rnd2')))+var.get('nm34').get(var.get('rnd3'))))
            else:
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('rnd')<Js(3.0)):
                        while (var.get('rnd3')<Js(3.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    else:
                        while (var.get('rnd3')<Js(3.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+Js(' '))+var.get('lname')))
                else:
                    if (var.get('i')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('lname')))
                    else:
                        if (var.get('i')<Js(6.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                            if (var.get('rnd')<Js(3.0)):
                                while (var.get('rnd3')<Js(3.0)):
                                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                            else:
                                while (var.get('rnd3')<Js(3.0)):
                                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                            var.put('names', ((((var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2')))+var.get('nm18').get(var.get('rnd3')))+Js(' '))+var.get('sname')))
                        else:
                            if (var.get('i')<Js(7.0)):
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                                var.put('names', ((((((var.get('nm15').get(var.get('rnd'))+var.get('nm16').get(var.get('rnd2')))+var.get('nm17').get(var.get('rnd3')))+var.get('nm16').get(var.get('rnd4')))+var.get('nm18').get(var.get('rnd5')))+Js(' '))+var.get('sname')))
                            else:
                                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm29').get('length'))))
                                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm30').get('length'))))
                                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm31').get('length'))))
                                var.put('names', ((var.get('nm29').get(var.get('rnd'))+var.get('nm30').get(var.get('rnd2')))+var.get('nm31').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('c'), Js('d'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th'), Js('v'), Js('w'), Js('y')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('oa'), Js('ea'), Js('ia'), Js('ai'), Js('io')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('d'), Js('k'), Js('l'), Js('lh'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('r'), Js('rf'), Js('rr'), Js('rt'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('v')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('b'), Js('ds'), Js('ft'), Js('h'), Js('ks'), Js('l'), Js('lds'), Js('lp'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('rd'), Js('rks'), Js('rl'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('v'), Js('w'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('w')]))
var.put('nm6', Js([Js('a'), Js('ee'), Js('ae'), Js('ia'), Js('ai'), Js('i'), Js('e'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('a'), Js('a'), Js('a')]))
var.put('nm7', Js([Js('d'), Js('l'), Js('lh'), Js('ll'), Js('m'), Js('mm'), Js('n'), Js('nk'), Js('nl'), Js('r'), Js('rh'), Js('sm'), Js('s'), Js('sh'), Js('sn'), Js('t'), Js('th'), Js('v'), Js('w')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('t'), Js('th'), Js('v')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('h'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('st'), Js('t'), Js('v'), Js('w')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('a'), Js('a'), Js('e'), Js('o'), Js('i'), Js('a'), Js('a'), Js('e'), Js('o'), Js('i'), Js('a'), Js('io'), Js('ea')]))
var.put('nm11', Js([Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('v')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('o'), Js('i'), Js('a'), Js('a'), Js('e'), Js('o'), Js('i'), Js('a'), Js('a'), Js('e'), Js('o'), Js('i'), Js('a'), Js('io'), Js('ea')]))
var.put('nm13', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('th'), Js('v')]))
var.put('nm14', Js([Js('c'), Js('d'), Js('g'), Js('m'), Js('n'), Js('s'), Js('t'), Js('th'), Js('v'), Js('w')]))
var.put('nm15', Js([Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('h'), Js('j'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('v'), Js('w')]))
var.put('nm16', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('ue'), Js('ia')]))
var.put('nm17', Js([Js('d'), Js('j'), Js('k'), Js('kk'), Js('l'), Js('m'), Js('n'), Js('r'), Js('sh'), Js('s'), Js('ss'), Js('t'), Js('v')]))
var.put('nm18', Js([Js(''), Js(''), Js(''), Js('d'), Js('l'), Js('n'), Js('m'), Js('r'), Js('s'), Js('sh'), Js('t')]))
var.put('nm19', Js([Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('w')]))
var.put('nm20', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('ue'), Js('ia')]))
var.put('nm21', Js([Js('d'), Js('f'), Js('j'), Js('h'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('ss'), Js('s'), Js('t')]))
var.put('nm22', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('l'), Js('n'), Js('m'), Js('r'), Js('s'), Js('sh'), Js('th')]))
var.put('nm23', Js([Js('b'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm24', Js([Js('a'), Js('e'), Js('i')]))
var.put('nm25', Js([Js('f'), Js('h'), Js('j'), Js('k'), Js('l'), Js('ll'), Js('lm'), Js('m'), Js('n'), Js('r'), Js('v')]))
var.put('nm26', Js([Js(''), Js('a'), Js('e'), Js('i')]))
var.put('nm27', Js([Js(''), Js('f'), Js('h'), Js('j'), Js('k'), Js('l'), Js('ll'), Js('lm'), Js('m'), Js('n'), Js('r'), Js('v')]))
var.put('nm28', Js([Js('d'), Js('l'), Js('n'), Js('r')]))
var.put('nm29', Js([Js('cn'), Js('cl'), Js('dv'), Js('dvl'), Js('dr'), Js('gm'), Js('gl'), Js('gv'), Js('km'), Js('kl'), Js('k'), Js('mn'), Js('mst'), Js('mv'), Js('mw'), Js('mr'), Js('nm'), Js('nr'), Js('nst'), Js('nv'), Js('nw'), Js('nl'), Js('tr'), Js('ts'), Js('tv'), Js('tm'), Js('tn'), Js('t'), Js('tvl'), Js('vl'), Js('vm'), Js('vn'), Js('vst')]))
var.put('nm30', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('y')]))
var.put('nm31', Js([Js('cv'), Js('cl'), Js('cn'), Js('km'), Js('kn'), Js('krn'), Js('k'), Js('kv'), Js('lm'), Js('ln'), Js('lrn'), Js('ll'), Js('lb'), Js('nm'), Js('nr'), Js('nd'), Js('nt'), Js('m'), Js('mt'), Js('mrn'), Js('md'), Js('rn'), Js('lrm'), Js('rm')]))
var.put('nm32', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('hs'), Js('hsh'), Js('hth'), Js('htn'), Js('kn'), Js('km'), Js('ks'), Js('kst'), Js('kh'), Js('lm'), Js('ln'), Js('ll'), Js('lb'), Js('lst'), Js('ls'), Js('lt'), Js('nm'), Js('nr'), Js('nd'), Js('nt'), Js('m'), Js('mt'), Js('ms'), Js('msh'), Js('msl'), Js('md'), Js('shlv'), Js('sn')]))
var.put('nm33', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('y')]))
var.put('nm34', Js([Js('cl'), Js('dv'), Js('dr'), Js('dh'), Js('dl'), Js('gh'), Js('gl'), Js('gm'), Js('gn'), Js('h'), Js('hr'), Js('hl'), Js('kl'), Js('kh'), Js('kn'), Js('km'), Js('kv'), Js('l'), Js('ln'), Js('lm'), Js('ls'), Js('mn'), Js('mw'), Js('mh'), Js('nw'), Js('nl'), Js('nh'), Js('th'), Js('thr'), Js('trh'), Js('ts'), Js('tw'), Js('tm'), Js('tn'), Js('vl'), Js('vn'), Js('r')]))
pass
pass


# Add lib to the module scope
stormlightArchive = var.to_python()