__all__ = ['elezenNames']

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
            if PyJsStrictEq(var.get('type'),Js(1.0)):
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('rnd8')<Js(16.0)):
                        var.put('rnd9', Js(0.0))
                    if (var.get('rnd8')>Js(15.0)):
                        while PyJsStrictEq(var.get('rnd9'),Js(0.0)):
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd5')))+Js(' '))+var.get('nm3').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd7')))+var.get('nm9').get(var.get('rnd8')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10')))+var.get('nm12').get(var.get('rnd11'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('rnd8')<Js(16.0)):
                        var.put('rnd9', Js(0.0))
                    if (var.get('rnd8')>Js(15.0)):
                        while PyJsStrictEq(var.get('rnd9'),Js(0.0)):
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    def PyJs_LONG_0_(var=var):
                        return var.put('names', ((((((((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('nm3').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd7')))+var.get('nm9').get(var.get('rnd8')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10')))+var.get('nm12').get(var.get('rnd11'))))
                    PyJs_LONG_0_()
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('rnd8')<Js(16.0)):
                        var.put('rnd9', Js(0.0))
                    if (var.get('rnd8')>Js(15.0)):
                        while PyJsStrictEq(var.get('rnd9'),Js(0.0)):
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd5')))+Js(' '))+var.get('nm3').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd7')))+var.get('nm9').get(var.get('rnd8')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10')))+var.get('nm12').get(var.get('rnd11'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('rnd8')<Js(16.0)):
                        var.put('rnd9', Js(0.0))
                    if (var.get('rnd8')>Js(15.0)):
                        while PyJsStrictEq(var.get('rnd9'),Js(0.0)):
                            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    def PyJs_LONG_1_(var=var):
                        return var.put('names', ((((((((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+Js(' '))+var.get('nm3').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd7')))+var.get('nm9').get(var.get('rnd8')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm11').get(var.get('rnd10')))+var.get('nm12').get(var.get('rnd11'))))
                    PyJs_LONG_1_()
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A'), Js('E'), Js('I'), Js('O'), Js('U'), Js('Au'), Js('Eau'), Js('A'), Js('E'), Js('I'), Js('O')]))
var.put('nm2', Js([Js('b'), Js('d'), Js('f'), Js('j'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z'), Js('br'), Js('dr'), Js('fr'), Js('gr'), Js('str'), Js('tr'), Js('vr'), Js('rr'), Js('fl'), Js('gl'), Js('ll'), Js('pl'), Js('rl'), Js('ch'), Js('ph'), Js('sh'), Js('lb'), Js('ld'), Js('lf'), Js('lm'), Js('ln'), Js('lp'), Js('ls'), Js('lv'), Js('lw')]))
var.put('nm3', Js([Js('B'), Js('C'), Js('D'), Js('F'), Js('G'), Js('H'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('P'), Js('R'), Js('S'), Js('T'), Js('V'), Js('Z'), Js('Br'), Js('Dr'), Js('Gr'), Js('Pr'), Js('Tr'), Js('Cl'), Js('Gl'), Js('Sh'), Js('Ph')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('eau'), Js('oi'), Js('au'), Js('io'), Js('ai'), Js('eo'), Js('ou'), Js('ei'), Js('io'), Js('ia')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('ff'), Js('ll'), Js('mm'), Js('nn'), Js('rr'), Js('ss'), Js('tt'), Js('sh'), Js('ph'), Js('ch')]))
var.put('nm6', Js([Js('onne'), Js('inne'), Js('anne'), Js('ionne'), Js('ianne'), Js('one'), Js('ine'), Js('ane'), Js('ione'), Js('iane'), Js('ette'), Js('elle'), Js('itte'), Js('ie'), Js('iene'), Js('enne'), Js('ene'), Js('eanne'), Js('eane'), Js('eone'), Js('eonne')]))
var.put('nm7', Js([Js('ant'), Js('ault'), Js('aut'), Js('aux'), Js('ax'), Js('eaux'), Js('ent'), Js('ert'), Js('eux'), Js('ex'), Js('ix'), Js('oix'), Js('ont'), Js('ort'), Js('oux')]))
var.put('nm8', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ui'), Js('eau'), Js('ai'), Js('ou'), Js('au'), Js('ui'), Js('ea'), Js('ie')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v')]))
var.put('nm10', Js([Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm11', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v')]))
var.put('nm12', Js([Js('ain'), Js('air'), Js('aire'), Js('ame'), Js('anc'), Js('and'), Js('ane'), Js('ant'), Js('ard'), Js('at'), Js('ault'), Js('aut'), Js('aux'), Js('eaux'), Js('elle'), Js('ent'), Js('eois'), Js('ert'), Js('ette'), Js('eur'), Js('eux'), Js('ie'), Js('ier'), Js('iere'), Js('ieu'), Js('in'), Js('ine'), Js('ins'), Js('ione'), Js('ionne'), Js('ois'), Js('oix'), Js('on'), Js('ond'), Js('ont'), Js('ort'), Js('oud'), Js('oux'), Js('oy'), Js('uet'), Js('uste')]))
pass
pass


# Add lib to the module scope
elezenNames = var.to_python()