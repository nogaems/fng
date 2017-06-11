__all__ = ['starTrekTellarites']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('names', (((((((((var.get('nm6').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+Js(' '))+var.get('nm12').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm14').get(var.get('rnd9'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    def PyJs_LONG_0_(var=var):
                        return var.put('names', ((((((((((var.get('nm6').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm12').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm13').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm14').get(var.get('rnd10'))))
                    PyJs_LONG_0_()
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+Js(' '))+var.get('nm12').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm13').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm14').get(var.get('rnd9'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+Js(' '))+var.get('nm12').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm14').get(var.get('rnd9'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('Br'), Js('Ch'), Js('C'), Js('Cr'), Js('D'), Js('Dv'), Js('Fr'), Js('F'), Js('G'), Js('Gl'), Js('Gr'), Js('H'), Js('J'), Js('K'), Js('Kh'), Js('L'), Js('M'), Js('N'), Js('Pr'), Js('R'), Js('Sh'), Js('Sk'), Js('T'), Js('Th'), Js('Tr'), Js('V'), Js('W'), Js('X'), Js('Z'), Js('Zh')]))
var.put('nm2', Js([Js('aa'), Js('ao'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o')]))
var.put('nm3', Js([Js('bl'), Js('fr'), Js('g'), Js('gr'), Js('hr'), Js('l'), Js('ll'), Js('nn'), Js('nk'), Js('r'), Js('rgg'), Js('rk'), Js('s'), Js('shl'), Js('shn'), Js('vr'), Js('rt')]))
var.put('nm4', Js([Js('ch'), Js('g'), Js('gm'), Js('k'), Js('llv'), Js('m'), Js('n'), Js('nn'), Js('nch'), Js('nd'), Js('r'), Js('rsh'), Js('rc'), Js('rg'), Js('rv'), Js('th'), Js('s'), Js('sh'), Js('ss'), Js('v')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(' bav'), Js(' bim'), Js(' blasch'), Js(' chim'), Js(' glasch'), Js(' glov'), Js(' lorin'), Js(' jav')]))
var.put('nm6', Js([Js('B'), Js('Bl'), Js('Ch'), Js('C'), Js('Cl'), Js('D'), Js('Fr'), Js('Fr'), Js('F'), Js('G'), Js('Gl'), Js('Gh'), Js('H'), Js('J'), Js('K'), Js('Kh'), Js('L'), Js('M'), Js('N'), Js('P'), Js('R'), Js('Sh'), Js('Sk'), Js('T'), Js('Th'), Js('Tl'), Js('V'), Js('W'), Js('Z'), Js('Zh')]))
var.put('nm8', Js([Js('bl'), Js('f'), Js('ff'), Js('g'), Js('gg'), Js('gr'), Js('hr'), Js('hl'), Js('l'), Js('ll'), Js('nn'), Js('nk'), Js('r'), Js('rk'), Js('s'), Js('ss'), Js('shl'), Js('shn'), Js('v'), Js('rth'), Js('th'), Js('t'), Js('tt')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('f'), Js('g'), Js('gh'), Js('hg'), Js('hk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('nsh'), Js('nd'), Js('p'), Js('r'), Js('rr'), Js('rs'), Js('rg'), Js('rn'), Js('th'), Js('s'), Js('sh'), Js('ss'), Js('v'), Js('w')]))
var.put('nm10', Js([Js('ch'), Js('f'), Js('g'), Js('gh'), Js('hg'), Js('hk'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('nsh'), Js('nd'), Js('p'), Js('r'), Js('rr'), Js('rs'), Js('rg'), Js('rn'), Js('th'), Js('s'), Js('sh'), Js('ss'), Js('v'), Js('w')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('aa'), Js('ao'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o')]))
var.put('nm12', Js([Js('B'), Js('Bl'), Js('Br'), Js('C'), Js('Ch'), Js('Cl'), Js('Cr'), Js('D'), Js('Dv'), Js('F'), Js('Fr'), Js('G'), Js('Gh'), Js('Gl'), Js('Gr'), Js('H'), Js('J'), Js('K'), Js('Kh'), Js('L'), Js('M'), Js('N'), Js('P'), Js('Pr'), Js('R'), Js('Sh'), Js('Sk'), Js('T'), Js('Th'), Js('Tl'), Js('Tr'), Js('V'), Js('W'), Js('X'), Js('Z'), Js('Zh')]))
var.put('nm13', Js([Js('bl'), Js('f'), Js('ff'), Js('fr'), Js('g'), Js('gg'), Js('gr'), Js('hl'), Js('hr'), Js('l'), Js('ll'), Js('nk'), Js('nn'), Js('r'), Js('rgg'), Js('rk'), Js('rth'), Js('s'), Js('shl'), Js('shn'), Js('ss'), Js('t'), Js('th'), Js('tt'), Js('v'), Js('vr')]))
var.put('nm14', Js([Js('ch'), Js('f'), Js('g'), Js('gh'), Js('gm'), Js('hg'), Js('hk'), Js('k'), Js('l'), Js('ll'), Js('llv'), Js('m'), Js('n'), Js('nch'), Js('nd'), Js('nn'), Js('nsh'), Js('p'), Js('r'), Js('rc'), Js('rg'), Js('rn'), Js('rr'), Js('rs'), Js('rsh'), Js('rv'), Js('s'), Js('sh'), Js('ss'), Js('th'), Js('v'), Js('w')]))
pass
pass


# Add lib to the module scope
starTrekTellarites = var.to_python()