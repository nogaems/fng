__all__ = ['starTrekKlingon']

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
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    if PyJsStrictEq(var.get('rnd6'),Js(0.0)):
                        var.put('rnd7', Js(0.0))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    def PyJs_LONG_0_(var=var):
                        return (((((((((((var.get('nm8').get(var.get('rnd7'))+var.get('nm1').get(var.get('rnd')))+var.get('nm9').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+Js(' '))+var.get('nm13').get(var.get('rnd8')))+var.get('nm3').get(var.get('rnd9')))+var.get('nm14').get(var.get('rnd10')))+var.get('nm3').get(var.get('rnd11')))
                    var.put('names', ((PyJs_LONG_0_()+var.get('nm15').get(var.get('rnd12')))+var.get('nm6').get(var.get('rnd13'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        if PyJsStrictEq(var.get('rnd7'),Js(0.0)):
                            var.put('rnd8', Js(0.0))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        def PyJs_LONG_1_(var=var):
                            return (((((((((((var.get('nm8').get(var.get('rnd8'))+var.get('nm9').get(var.get('rnd')))+var.get('nm3').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5')))+var.get('nm12').get(var.get('rnd6')))+Js(' '))+var.get('nm13').get(var.get('rnd9')))+var.get('nm3').get(var.get('rnd10')))+var.get('nm15').get(var.get('rnd13')))
                        var.put('names', (PyJs_LONG_1_()+var.get('nm6').get(var.get('rnd12'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        def PyJs_LONG_2_(var=var):
                            return (((((((((((var.get('nm8').get(var.get('rnd5'))+var.get('nm9').get(var.get('rnd')))+var.get('nm3').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+Js(' '))+var.get('nm13').get(var.get('rnd8')))+var.get('nm3').get(var.get('rnd9')))+var.get('nm14').get(var.get('rnd10')))+var.get('nm3').get(var.get('rnd11')))+var.get('nm15').get(var.get('rnd12')))+var.get('nm6').get(var.get('rnd13')))
                        var.put('names', PyJs_LONG_2_())
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    if PyJsStrictEq(var.get('rnd6'),Js(0.0)):
                        var.put('rnd7', Js(0.0))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    def PyJs_LONG_3_(var=var):
                        return (((((((((((var.get('nm8').get(var.get('rnd7'))+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+Js(' '))+var.get('nm13').get(var.get('rnd8')))+var.get('nm3').get(var.get('rnd9')))+var.get('nm14').get(var.get('rnd10')))+var.get('nm3').get(var.get('rnd11')))
                    var.put('names', ((PyJs_LONG_3_()+var.get('nm15').get(var.get('rnd12')))+var.get('nm6').get(var.get('rnd13'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        if PyJsStrictEq(var.get('rnd7'),Js(0.0)):
                            var.put('rnd8', Js(0.0))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        def PyJs_LONG_4_(var=var):
                            return (((((((((((var.get('nm8').get(var.get('rnd8'))+var.get('nm2').get(var.get('rnd')))+var.get('nm3').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm13').get(var.get('rnd9')))+var.get('nm3').get(var.get('rnd10')))+var.get('nm15').get(var.get('rnd13')))
                        var.put('names', (PyJs_LONG_4_()+var.get('nm6').get(var.get('rnd12'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                        var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        def PyJs_LONG_5_(var=var):
                            return (((((((((((var.get('nm8').get(var.get('rnd5'))+var.get('nm2').get(var.get('rnd')))+var.get('nm3').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+Js(' '))+var.get('nm13').get(var.get('rnd8')))+var.get('nm3').get(var.get('rnd9')))+var.get('nm14').get(var.get('rnd10')))+var.get('nm3').get(var.get('rnd11')))+var.get('nm15').get(var.get('rnd12')))+var.get('nm6').get(var.get('rnd13')))
                        var.put('names', PyJs_LONG_5_())
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('o'), Js('u'), Js('e')]))
var.put('nm2', Js([Js('b'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('ts'), Js('th'), Js('tr'), Js('st'), Js('sh'), Js('gr'), Js('ch'), Js('kr'), Js('kl'), Js('dr')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('o')]))
var.put('nm4', Js([Js('k'), Js('k'), Js('k'), Js('m'), Js('t'), Js('r'), Js('v'), Js('g'), Js('p'), Js('n'), Js('l'), Js('d'), Js('z'), Js('b'), Js('h'), Js('m'), Js('t'), Js('r'), Js('v'), Js('g'), Js('p'), Js('n'), Js('l'), Js('d'), Js('z'), Js('b'), Js('h'), Js('r'), Js('r'), Js('r'), Js('cl'), Js('dm'), Js('dr'), Js('gh'), Js('gr'), Js('hl'), Js('hm'), Js('ll'), Js('mp'), Js('mt'), Js('nk'), Js('nm'), Js('nt'), Js('rg'), Js('rk'), Js('rl'), Js('rn'), Js('rp'), Js('rr'), Js('rt'), Js('sk'), Js('th'), Js('tr'), Js('wr'), Js('yb')]))
var.put('nm5', Js([Js('k'), Js('k'), Js('m'), Js('r'), Js('k'), Js('l'), Js('n'), Js('rgh'), Js('ng'), Js('x'), Js('s'), Js('n'), Js('th'), Js('hk'), Js('hl'), Js('d'), Js('l'), Js('c'), Js('gh'), Js('ss'), Js('z'), Js('ll'), Js('rrd'), Js('rd'), Js('t'), Js('q'), Js('sh'), Js('w'), Js('rf')]))
var.put('nm6', Js([Js('o'), Js('a'), Js('i'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm7', Js([Js("'"), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm8', Js([Js(''), Js("Ch'"), Js("D'"), Js("H'"), Js("J'"), Js("K'"), Js("L'"), Js("T'"), Js("W'"), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm9', Js([Js('b'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('ts'), Js('th'), Js('tr'), Js('st'), Js('sh'), Js('gr'), Js('ch'), Js('kr'), Js('kl'), Js('dr')]))
var.put('nm10', Js([Js('d'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('x'), Js('z'), Js('lk'), Js('nn'), Js('tb'), Js('hl'), Js('rs'), Js('ll'), Js('lkr'), Js('km'), Js('dr'), Js('rl'), Js('lk'), Js('lg'), Js('rg'), Js('sk'), Js('th'), Js('tr'), Js('dm'), Js('hm'), Js('ng'), Js('nk'), Js('l'), Js('n'), Js('l'), Js('n'), Js('k')]))
var.put('nm11', Js([Js('r'), Js('nn'), Js('l'), Js('h'), Js('g'), Js('n'), Js('ss'), Js('s'), Js('yr'), Js('st'), Js('th'), Js('j'), Js('m'), Js('v'), Js('ll'), Js('sh'), Js('hl'), Js('ng'), Js('w')]))
var.put('nm12', Js([Js('o'), Js('a'), Js('i'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm13', Js([Js(''), Js(''), Js(''), Js('b'), Js('c'), Js("g'g"), Js('d'), Js("d'gh"), Js('dr'), Js('f'), Js("g'"), Js('g'), Js('gr'), Js('h'), Js('j'), Js("k'g"), Js("k't"), Js("k'mp"), Js('k'), Js('kh'), Js('kl'), Js('kr'), Js('l'), Js('m'), Js('mn'), Js('mr'), Js('mv'), Js('n'), Js('ng'), Js('p'), Js('q'), Js('r'), Js('rr'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('x'), Js('z')]))
var.put('nm14', Js([Js('c'), Js('ct'), Js('ck'), Js('ch'), Js('b'), Js('d'), Js('g'), Js('gg'), Js('ggr'), Js('hn'), Js('hnr'), Js('k'), Js("k'M"), Js('ll'), Js('lk'), Js('lv'), Js('lm'), Js('lt'), Js('mm'), Js('mmr'), Js('m'), Js('mp'), Js('mr'), Js('nn'), Js('nk'), Js('nl'), Js('nj'), Js('nz'), Js('ndl'), Js('ns'), Js('n'), Js('nt'), Js('r'), Js('rr'), Js('rs'), Js('rmd'), Js('rn'), Js('rp'), Js('rtr'), Js('rst'), Js('rt'), Js('rg'), Js('rm'), Js('rd'), Js('rsh'), Js('ss'), Js('str'), Js('sht'), Js('tzh'), Js('v'), Js('wr'), Js('x'), Js('yg'), Js('z'), Js('zh')]))
var.put('nm15', Js([Js('bh'), Js('c'), Js('ct'), Js('ck'), Js('cx'), Js('ch'), Js('d'), Js('dh'), Js('j'), Js('g'), Js('gh'), Js('h'), Js('k'), Js('l'), Js('lt'), Js('m'), Js('n'), Js('nn'), Js('ng'), Js('r'), Js('rc'), Js('rr'), Js('rgh'), Js('rk'), Js('rv'), Js('rn'), Js('rg'), Js('sh'), Js('sht'), Js('s'), Js('ss'), Js('t'), Js('th'), Js('v'), Js('x'), Js('z'), Js('zh')]))
pass
pass


# Add lib to the module scope
starTrekKlingon = var.to_python()