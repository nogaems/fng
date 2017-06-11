__all__ = ['miqoteNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if PyJsStrictEq(var.get('rnd11'),Js(1.0)):
                        var.put('rnd14', Js(0.0))
                    var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    if (var.get('rnd12')<Js(6.0)):
                        while (var.get('rnd15')<Js(6.0)):
                            var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd17', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (PyJsStrictEq(var.get('rnd11'),Js(1.0)) or PyJsStrictEq(var.get('rnd14'),Js(1.0))):
                        var.put('rnd17', Js(0.0))
                    var.put('rnd18', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('rnd16')<Js(16.0)):
                        var.put('rnd17', Js(0.0))
                        var.put('rnd18', Js(0.0))
                    else:
                        while PyJsStrictEq(var.get('rnd18'),Js(0.0)):
                            var.put('rnd18', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd19', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    def PyJs_LONG_0_(var=var):
                        return var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd10')))+var.get('nm5').get(var.get('rnd11')))+var.get('nm7').get(var.get('rnd12')))+var.get('nm6').get(var.get('rnd13')))+var.get('nm5').get(var.get('rnd14')))+var.get('nm7').get(var.get('rnd15')))+var.get('nm9').get(var.get('rnd16')))+var.get('nm5').get(var.get('rnd17')))+var.get('nm10').get(var.get('rnd18'))))
                    PyJs_LONG_0_()
                else:
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('rnd8')<Js(5.0)):
                        var.put('rnd6', Js(0.0))
                        while (var.get('rnd5')<Js(3.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if PyJsStrictEq(var.get('rnd6'),Js(1.0)):
                        var.put('rnd7', Js(0.0))
                    if (var.get('rnd5')<Js(3.0)):
                        var.put('rnd8', Js(0.0))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if PyJsStrictEq(var.get('rnd11'),Js(1.0)):
                        var.put('rnd14', Js(0.0))
                    var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    if (var.get('rnd12')<Js(6.0)):
                        while (var.get('rnd15')<Js(6.0)):
                            var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd17', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (PyJsStrictEq(var.get('rnd11'),Js(1.0)) or PyJsStrictEq(var.get('rnd14'),Js(1.0))):
                        var.put('rnd17', Js(0.0))
                    var.put('rnd18', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('rnd16')<Js(16.0)):
                        var.put('rnd17', Js(0.0))
                        var.put('rnd18', Js(0.0))
                    else:
                        while PyJsStrictEq(var.get('rnd18'),Js(0.0)):
                            var.put('rnd18', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    def PyJs_LONG_1_(var=var):
                        return (((((((((((var.get('nm8').get(var.get('rnd2'))+var.get('nm5').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd8')))+Js(' '))+var.get('nm6').get(var.get('rnd10')))+var.get('nm5').get(var.get('rnd11')))+var.get('nm7').get(var.get('rnd12')))+var.get('nm6').get(var.get('rnd13')))
                    var.put('names', (((((PyJs_LONG_1_()+var.get('nm5').get(var.get('rnd14')))+var.get('nm7').get(var.get('rnd15')))+var.get('nm9').get(var.get('rnd16')))+var.get('nm5').get(var.get('rnd17')))+var.get('nm10').get(var.get('rnd18'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if PyJsStrictEq(var.get('rnd6'),Js(1.0)):
                        var.put('rnd7', Js(0.0))
                    if (var.get('rnd5')<Js(3.0)):
                        var.put('rnd8', Js(0.0))
                    var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd8'))))
                else:
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('rnd8')<Js(5.0)):
                        var.put('rnd6', Js(0.0))
                        while (var.get('rnd5')<Js(3.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if PyJsStrictEq(var.get('rnd6'),Js(1.0)):
                        var.put('rnd7', Js(0.0))
                    if (var.get('rnd5')<Js(3.0)):
                        var.put('rnd8', Js(0.0))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if PyJsStrictEq(var.get('rnd11'),Js(1.0)):
                        var.put('rnd14', Js(0.0))
                    var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    if (var.get('rnd12')<Js(6.0)):
                        while (var.get('rnd15')<Js(6.0)):
                            var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd16', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd17', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (PyJsStrictEq(var.get('rnd11'),Js(1.0)) or PyJsStrictEq(var.get('rnd14'),Js(1.0))):
                        var.put('rnd17', Js(0.0))
                    var.put('rnd18', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('rnd16')<Js(16.0)):
                        var.put('rnd17', Js(0.0))
                        var.put('rnd18', Js(0.0))
                    else:
                        while PyJsStrictEq(var.get('rnd18'),Js(0.0)):
                            var.put('rnd18', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd19', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    def PyJs_LONG_2_(var=var):
                        return (((((((((((var.get('nm8').get(var.get('rnd2'))+var.get('nm5').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd19')))+Js(' '))+var.get('nm6').get(var.get('rnd10')))+var.get('nm5').get(var.get('rnd11')))+var.get('nm7').get(var.get('rnd12')))
                    var.put('names', ((((((PyJs_LONG_2_()+var.get('nm6').get(var.get('rnd13')))+var.get('nm5').get(var.get('rnd14')))+var.get('nm7').get(var.get('rnd15')))+var.get('nm9').get(var.get('rnd16')))+var.get('nm5').get(var.get('rnd17')))+var.get('nm10').get(var.get('rnd18'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js("A'"), Js("B'"), Js("C'"), Js("D'"), Js("E'"), Js("F'"), Js("G'"), Js("H'"), Js("I'"), Js("J'"), Js("K'"), Js("L'"), Js("M'"), Js("N'"), Js("O'"), Js("P'"), Js("Q'"), Js("R'"), Js("S'"), Js("T'"), Js("U'"), Js("V'"), Js("W'"), Js("X'"), Js("Y'"), Js("Z'")]))
var.put('nm2', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('u')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('o'), Js('i'), Js('u')]))
var.put('nm5', Js([Js(''), Js('h')]))
var.put('nm6', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bb'), Js('cc'), Js('dd'), Js('ff'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt'), Js('ww'), Js('zz'), Js('cb'), Js('gb'), Js('lb'), Js('mb'), Js('nb'), Js('rb'), Js('bd'), Js('cd'), Js('gd'), Js('ld'), Js('md'), Js('nd'), Js('sd'), Js('rd'), Js('bf'), Js('df'), Js('kf'), Js('lf'), Js('mf'), Js('nf'), Js('pf'), Js('rf'), Js('sf'), Js('tf'), Js('bg'), Js('dg'), Js('lg'), Js('mg'), Js('ng'), Js('rg'), Js('sg'), Js('ck'), Js('lk'), Js('mk'), Js('nk'), Js('pk'), Js('rk'), Js('sk'), Js('tk'), Js('bl'), Js('dl'), Js('fl'), Js('gl'), Js('kl'), Js('ml'), Js('nl'), Js('pl'), Js('rl'), Js('sl'), Js('tl'), Js('bm'), Js('dm'), Js('fm'), Js('gm'), Js('km'), Js('lm'), Js('nm'), Js('pm'), Js('rm'), Js('sm'), Js('tm'), Js('bn'), Js('dn'), Js('fn'), Js('gn'), Js('kn'), Js('mn'), Js('ln'), Js('pn'), Js('rn'), Js('sn'), Js('tn'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('lr'), Js('mr'), Js('nr'), Js('pr'), Js('sr'), Js('tr'), Js('vr'), Js('wr'), Js('zr'), Js('bs'), Js('cs'), Js('ds'), Js('fs'), Js('gs'), Js('ks'), Js('ls'), Js('ms'), Js('ns'), Js('ps'), Js('rs'), Js('ts'), Js('bt'), Js('ct'), Js('kt'), Js('lt'), Js('mt'), Js('nt'), Js('pt'), Js('rt'), Js('st'), Js('by'), Js('cy'), Js('dy'), Js('fy'), Js('gy'), Js('ky'), Js('ly'), Js('my'), Js('ny'), Js('py'), Js('ry'), Js('sy'), Js('ty')]))
var.put('nm7', Js([Js('ei'), Js('au'), Js('aa'), Js('ee'), Js('oo'), Js('aia'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z')]))
var.put('nm10', Js([Js(''), Js('a'), Js('e'), Js('o'), Js('i'), Js('u')]))
var.put('nm11', Js([Js("'a"), Js("'to"), Js("'li"), Js("'sae"), Js("'ra"), Js("'ir"), Js("'wo"), Js("'ya"), Js("'zi"), Js("'tan")]))
pass
pass


# Add lib to the module scope
miqoteNames = var.to_python()