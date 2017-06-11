__all__ = ['pathfinderElf']

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
                    while (var.get('rnd12')<Js(2.0)):
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('nameLast', ((var.get('nm9').get(var.get('rnd10'))+var.get('nm10').get(var.get('rnd11')))+var.get('nm12').get(var.get('rnd12'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(4.0)):
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5')))+Js(' '))+var.get('nameLast')))
                    else:
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
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
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
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('s'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('o'), Js('e'), Js('e'), Js('ae'), Js('ia'), Js('ie'), Js('ea'), Js('ei'), Js('io')]))
var.put('nm3', Js([Js('ch'), Js('cl'), Js('cv'), Js('dr'), Js('dv'), Js('g'), Js('g'), Js('g'), Js('gl'), Js('gr'), Js('ghr'), Js('ght'), Js('h'), Js('h'), Js('h'), Js('j'), Js('j'), Js('l'), Js('l'), Js('l'), Js('l'), Js('l'), Js('l'), Js('lm'), Js('ln'), Js('ldr'), Js('lvr'), Js('ld'), Js('ldl'), Js('ll'), Js('ls'), Js('lth'), Js('lv'), Js('m'), Js('m'), Js('m'), Js('m'), Js('mr'), Js('mv'), Js('n'), Js('n'), Js('n'), Js('n'), Js('nr'), Js('nv'), Js('nvr'), Js('nth'), Js('nd'), Js('ndl'), Js('ndr'), Js('nl'), Js('r'), Js('r'), Js('r'), Js('r'), Js('r'), Js('rl'), Js('rgr'), Js('rg'), Js('rd'), Js('rdl'), Js('rdr'), Js('s'), Js('s'), Js('s'), Js('s'), Js('sh'), Js('shn'), Js('st'), Js('sv'), Js('sr'), Js('sth'), Js('t'), Js('t'), Js('t'), Js('th'), Js('th'), Js('v'), Js('v'), Js('v'), Js('vr'), Js('y'), Js('y'), Js('y')]))
var.put('nm4', Js([Js(''), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('ss'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('ss')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('f'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('y')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('o'), Js('o'), Js('e'), Js('e'), Js('ie'), Js('ia'), Js('ea'), Js('au'), Js('aa'), Js('ao'), Js('eae'), Js('ou'), Js('ae')]))
var.put('nm7', Js([Js('c'), Js('c'), Js('c'), Js('cl'), Js('cn'), Js('cm'), Js('d'), Js('d'), Js('d'), Js('dr'), Js('dn'), Js('dm'), Js('g'), Js('g'), Js('g'), Js('gn'), Js('gh'), Js('gy'), Js('h'), Js('h'), Js('h'), Js('h'), Js('hh'), Js('hh'), Js('hn'), Js('hl'), Js('hr'), Js('l'), Js('l'), Js('l'), Js('l'), Js('l'), Js('ll'), Js('ll'), Js('lm'), Js('ln'), Js('lhr'), Js('lhn'), Js('lv'), Js('ls'), Js('lsh'), Js('ly'), Js('ll'), Js('m'), Js('m'), Js('m'), Js('m'), Js('mm'), Js('mm'), Js('mh'), Js('mn'), Js('mr'), Js('n'), Js('n'), Js('n'), Js('nn'), Js('nn'), Js('nd'), Js('ndl'), Js('ndr'), Js('nn'), Js('nr'), Js('nth'), Js('ns'), Js('nl'), Js('nh'), Js('ny'), Js('r'), Js('r'), Js('r'), Js('rr'), Js('rr'), Js('rdl'), Js('rl'), Js('rn'), Js('rv'), Js('rs'), Js('s'), Js('s'), Js('s'), Js('ss'), Js('ss'), Js('sh'), Js('shr'), Js('sl'), Js('th'), Js('v'), Js('v'), Js('v'), Js('y'), Js('y'), Js('y')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n'), Js('s'), Js('ss')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('w'), Js('y'), Js('z'), Js('zh')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('a'), Js('e'), Js('e'), Js('o'), Js('o'), Js('ai'), Js('ee'), Js('ei'), Js('ia'), Js('ie'), Js('ae'), Js('io')]))
var.put('nm11', Js([Js('cl'), Js('d'), Js('d'), Js('d'), Js('dn'), Js('dr'), Js('g'), Js('g'), Js('g'), Js('gh'), Js('gl'), Js('gr'), Js('h'), Js('h'), Js('h'), Js('hh'), Js('j'), Js('k'), Js('k'), Js('k'), Js('l'), Js('l'), Js('l'), Js('l'), Js('l'), Js('ll'), Js('ll'), Js('ll'), Js('ld'), Js('ldl'), Js('ldr'), Js('lf'), Js('lhn'), Js('lhr'), Js('ll'), Js('llm'), Js('llv'), Js('lm'), Js('ln'), Js('ls'), Js('lv'), Js('lvr'), Js('m'), Js('m'), Js('m'), Js('mm'), Js('mm'), Js('mn'), Js('mr'), Js('mv'), Js('n'), Js('n'), Js('n'), Js('nn'), Js('n'), Js('nd'), Js('ndl'), Js('ndr'), Js('nl'), Js('nn'), Js('nr'), Js('ns'), Js('nth'), Js('nv'), Js('ph'), Js('r'), Js('r'), Js('r'), Js('rr'), Js('rd'), Js('rdl'), Js('rg'), Js('rl'), Js('rm'), Js('rr'), Js('s'), Js('s'), Js('s'), Js('ss'), Js('ss'), Js('sh'), Js('sl'), Js('ss'), Js('st'), Js('th'), Js('tl'), Js('v'), Js('v'), Js('v'), Js('y'), Js('y'), Js('y')]))
var.put('nm12', Js([Js(''), Js(''), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s')]))
pass
pass


# Add lib to the module scope
pathfinderElf = var.to_python()