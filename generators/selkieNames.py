__all__ = ['selkieNames']

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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                if (var.get('i')<Js(3.0)):
                    while (var.get('rnd')<Js(6.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    while (var.get('rnd3')<Js(8.0)):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3'))))
                else:
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm8').get(var.get('rnd4')),var.get('nm6').get(var.get('rnd'))):
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm8').get(var.get('rnd4')),var.get('nm10').get(var.get('rnd3'))):
                        var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm10').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(7.0)):
                        var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm10').get(var.get('rnd3'))))
                    else:
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        while (PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm10').get(var.get('rnd3'))) or PyJsStrictEq(var.get('nm9').get(var.get('rnd6')),var.get('nm8').get(var.get('rnd4')))):
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                        var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                        var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd3'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(3.0)):
                        while (var.get('rnd')<Js(4.0)):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm11').get('length'))|Js(0.0)))
                        while (var.get('rnd3')<Js(5.0)):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm15').get(var.get('rnd3'))))
                    else:
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm13').get(var.get('rnd4')),var.get('nm11').get(var.get('rnd'))):
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm13').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm13').get(var.get('rnd4')),var.get('nm15').get(var.get('rnd3'))):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm15').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                        if (var.get('i')<Js(7.0)):
                            var.put('names', ((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm15').get(var.get('rnd3'))))
                        else:
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                            while (PyJsStrictEq(var.get('nm14').get(var.get('rnd6')),var.get('nm15').get(var.get('rnd3'))) or PyJsStrictEq(var.get('nm14').get(var.get('rnd6')),var.get('nm13').get(var.get('rnd4')))):
                                var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm14').get('length'))|Js(0.0)))
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm12').get('length'))|Js(0.0)))
                            var.put('names', ((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm15').get(var.get('rnd3'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                    if (var.get('i')<Js(3.0)):
                        while (var.get('rnd')<Js(4.0)):
                            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                        while (var.get('rnd3')<Js(5.0)):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
                    else:
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm3').get(var.get('rnd4')),var.get('nm1').get(var.get('rnd'))):
                            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                        while PyJsStrictEq(var.get('nm3').get(var.get('rnd4')),var.get('nm5').get(var.get('rnd3'))):
                            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                        if (var.get('i')<Js(7.0)):
                            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd3'))))
                        else:
                            var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                            while (PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm5').get(var.get('rnd3'))) or PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd4')))):
                                var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                            var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('d'), Js('f'), Js('g'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aoi'), Js('ai'), Js('ea'), Js('á'), Js('ó'), Js('í'), Js('ú'), Js('á'), Js('ó'), Js('í'), Js('ú'), Js('éi'), Js('ói'), Js('éa'), Js('eá'), Js('aoi'), Js('ao'), Js('ío'), Js('eò')]))
var.put('nm3', Js([Js('bb'), Js('bh'), Js('bhn'), Js('c'), Js('cc'), Js('ch'), Js('chl'), Js('d'), Js('dbh'), Js('dh'), Js('dhl'), Js('g'), Js('gh'), Js('gn'), Js('l'), Js('lb'), Js('lbh'), Js('ll'), Js('lp'), Js('lt'), Js('m'), Js('mh'), Js('mhl'), Js('mhr'), Js('n'), Js('nbh'), Js('nd'), Js('ndr'), Js('nf'), Js('ng'), Js('ngh'), Js('nl'), Js('nm'), Js('nmch'), Js('nn'), Js('nndr'), Js('nnl'), Js('nr'), Js('nt'), Js('r'), Js('rbh'), Js('rch'), Js('rd'), Js('rdg'), Js('rdgh'), Js('rh'), Js('rn'), Js('rr'), Js('rt'), Js('rth'), Js('s'), Js('sd'), Js('sg'), Js('st'), Js('t'), Js('th'), Js('thgh')]))
var.put('nm4', Js([Js('bh'), Js('ch'), Js('cht'), Js('d'), Js('dh'), Js('g'), Js('gh'), Js('l'), Js('lg'), Js('ll'), Js('lm'), Js('lt'), Js('m'), Js('mh'), Js('mhn'), Js('mn'), Js('mth'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('rt'), Js('sd'), Js('sl'), Js('st'), Js('th')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('bh'), Js('ch'), Js('cht'), Js('d'), Js('dh'), Js('gh'), Js('l'), Js('ll'), Js('m'), Js('mh'), Js('n'), Js('nn'), Js('r'), Js('rd'), Js('rt'), Js('s')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('c'), Js('d'), Js('f'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('á'), Js('é'), Js('í'), Js('ì'), Js('ó'), Js('á'), Js('é'), Js('í'), Js('ì'), Js('ó'), Js('ái'), Js('ói'), Js('aí'), Js('ìo'), Js('ío'), Js('úa'), Js('úi'), Js('ea'), Js('ei'), Js('io'), Js('ia'), Js('ai'), Js('ua'), Js('aoi')]))
var.put('nm8', Js([Js('b'), Js('bh'), Js('bhgr'), Js('bhl'), Js('bhn'), Js('ch'), Js('chn'), Js('d'), Js('dhn'), Js('f'), Js('ffr'), Js('g'), Js('gh'), Js('ghd'), Js('ghn'), Js('gs'), Js('l'), Js('lbh'), Js('ll'), Js('lm'), Js('lmh'), Js('m'), Js('mh'), Js('mhn'), Js('mn'), Js('mphn'), Js('ms'), Js('n'), Js('nbh'), Js('ng'), Js('nn'), Js('nnl'), Js('nt'), Js('phn'), Js('r'), Js('rb'), Js('rbh'), Js('rch'), Js('rdr'), Js('rl'), Js('rn'), Js('sl'), Js('st'), Js('str'), Js('t'), Js('thch'), Js('thn'), Js('thr'), Js('tr')]))
var.put('nm9', Js([Js('b'), Js('bhl'), Js('bl'), Js('g'), Js('gh'), Js('l'), Js('m'), Js('mh'), Js('mhn'), Js('n'), Js('ngh'), Js('r'), Js('rg'), Js('rn'), Js('s'), Js('str')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('l'), Js('ll'), Js('n'), Js('ng'), Js('nn'), Js('r'), Js('s'), Js('sh'), Js('th')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('d'), Js('f'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm12', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('á'), Js('ó'), Js('í'), Js('á'), Js('ó'), Js('í'), Js('é'), Js('é'), Js('aoi'), Js('ai'), Js('ea'), Js('ói'), Js('ío'), Js('ái'), Js('úi'), Js('éa'), Js('eá')]))
var.put('nm13', Js([Js('bh'), Js('bhn'), Js('ch'), Js('d'), Js('dh'), Js('dhn'), Js('g'), Js('gh'), Js('gn'), Js('l'), Js('lb'), Js('lbh'), Js('ll'), Js('m'), Js('mh'), Js('mhn'), Js('mhl'), Js('n'), Js('nbh'), Js('nd'), Js('nf'), Js('ng'), Js('ngh'), Js('nl'), Js('nm'), Js('nn'), Js('nnl'), Js('nr'), Js('nt'), Js('r'), Js('rb'), Js('rch'), Js('rd'), Js('rdr'), Js('rn'), Js('s'), Js('sd'), Js('st'), Js('t'), Js('th')]))
var.put('nm14', Js([Js('bh'), Js('bhl'), Js('g'), Js('gh'), Js('l'), Js('ll'), Js('lm'), Js('m'), Js('mh'), Js('mhn'), Js('mn'), Js('n'), Js('nn'), Js('r'), Js('rr'), Js('s'), Js('sd'), Js('sl'), Js('st'), Js('th')]))
var.put('nm15', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('l'), Js('ll'), Js('m'), Js('mh'), Js('n'), Js('nn'), Js('r'), Js('rd'), Js('rt'), Js('s'), Js('sh'), Js('th')]))
pass
pass


# Add lib to the module scope
selkieNames = var.to_python()