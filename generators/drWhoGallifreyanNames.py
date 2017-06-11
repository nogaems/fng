__all__ = ['drWhoGallifreyanNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    def PyJs_LONG_0_(var=var):
                        return ((((((((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm13').get(var.get('rnd11')))
                    var.put('names', PyJs_LONG_0_())
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        def PyJs_LONG_1_(var=var):
                            return ((((((((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm12').get(var.get('rnd11')))
                        var.put('names', ((PyJs_LONG_1_()+var.get('nm2').get(var.get('rnd12')))+var.get('nm13').get(var.get('rnd13'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        def PyJs_LONG_2_(var=var):
                            return ((((((((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm10').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm12').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm12').get(var.get('rnd11')))
                        var.put('names', ((((PyJs_LONG_2_()+var.get('nm2').get(var.get('rnd12')))+var.get('nm12').get(var.get('rnd13')))+var.get('nm2').get(var.get('rnd14')))+var.get('nm13').get(var.get('rnd15'))))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    def PyJs_LONG_3_(var=var):
                        return ((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm7').get(var.get('rnd11')))
                    var.put('names', PyJs_LONG_3_())
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        def PyJs_LONG_4_(var=var):
                            return ((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm6').get(var.get('rnd11')))
                        var.put('names', ((PyJs_LONG_4_()+var.get('nm2').get(var.get('rnd12')))+var.get('nm7').get(var.get('rnd13'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd15', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        def PyJs_LONG_5_(var=var):
                            return ((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm5').get(var.get('rnd7')))+var.get('nm2').get(var.get('rnd8')))+var.get('nm6').get(var.get('rnd9')))+var.get('nm2').get(var.get('rnd10')))+var.get('nm6').get(var.get('rnd11')))
                        var.put('names', ((((PyJs_LONG_5_()+var.get('nm2').get(var.get('rnd12')))+var.get('nm6').get(var.get('rnd13')))+var.get('nm2').get(var.get('rnd14')))+var.get('nm7').get(var.get('rnd15'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gl'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('q'), Js('r'), Js('s'), Js('st'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia')]))
var.put('nm3', Js([Js('bl'), Js('br'), Js('bj'), Js('d'), Js('ff'), Js('g'), Js('gn'), Js('gr'), Js('kk'), Js('kl'), Js('kr'), Js('lj'), Js('l'), Js('lg'), Js('ll'), Js('lr'), Js('lm'), Js('ly'), Js('lp'), Js('m'), Js('mr'), Js('md'), Js('mt'), Js('nd'), Js('ndr'), Js('nc'), Js('ng'), Js('nn'), Js('ns'), Js('nt'), Js('nz'), Js('p'), Js('pp'), Js('r'), Js('rn'), Js('rb'), Js('rt'), Js('rl'), Js('rkh'), Js('rv'), Js('sb'), Js('sm'), Js('sp'), Js('ss'), Js('sk'), Js('t'), Js('th'), Js('tth'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wtr'), Js('x'), Js('xr'), Js('xt'), Js('zm')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('f'), Js('k'), Js('l'), Js('ld'), Js('ll'), Js('n'), Js('nd'), Js('r'), Js('rg'), Js('s'), Js('sh'), Js('th'), Js('t'), Js('w'), Js('x')]))
var.put('nm5', Js([Js('br'), Js('dr'), Js('g'), Js('gr'), Js('gl'), Js('k'), Js('kl'), Js('kr'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('z')]))
var.put('nm6', Js([Js('br'), Js('cr'), Js('ctr'), Js('dr'), Js('dd'), Js('d'), Js('gr'), Js('gl'), Js('gg'), Js('g'), Js('l'), Js('ll'), Js('lgr'), Js('lsr'), Js('lbr'), Js('lk'), Js('ldr'), Js('m'), Js('mr'), Js('ms'), Js('n'), Js('ng'), Js('ngr'), Js('nt'), Js('ntr'), Js('ndr'), Js('p'), Js('pr'), Js('phr'), Js('r'), Js('rd'), Js('rth'), Js('s'), Js('sk'), Js('str'), Js('sr'), Js('v'), Js('vr')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js('d'), Js('l'), Js('ll'), Js('m'), Js('m'), Js('n'), Js('nn'), Js('s'), Js('ss'), Js('st'), Js('th'), Js('tkh')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('cl'), Js('d'), Js('dh'), Js('dr'), Js('f'), Js('gl'), Js('h'), Js('j'), Js('kh'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('pr'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('sc'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm9', Js([Js('br'), Js('d'), Js('ff'), Js('gn'), Js('gl'), Js('hr'), Js('hn'), Js('k'), Js('kr'), Js('l'), Js('ll'), Js('ly'), Js('lm'), Js('ln'), Js('lph'), Js('lt'), Js('lr'), Js('m'), Js('mn'), Js('mm'), Js('n'), Js('nn'), Js('nd'), Js('ns'), Js('nt'), Js('nz'), Js('ndr'), Js('nt'), Js('p'), Js('pp'), Js('pr'), Js('r'), Js('rr'), Js('ry'), Js('rl'), Js('rs'), Js('rk'), Js('sf'), Js('sm'), Js('sn'), Js('sh'), Js('sp'), Js('st'), Js('tth'), Js('th'), Js('v'), Js('vy'), Js('vr'), Js('y')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('oie'), Js('ea')]))
var.put('nm11', Js([Js('br'), Js('bl'), Js('dv'), Js('dh'), Js('dr'), Js('f'), Js('ff'), Js('gl'), Js('gr'), Js('h'), Js('l'), Js('lm'), Js('ln'), Js('m'), Js('n'), Js('pr'), Js('ph'), Js('q'), Js('r'), Js('rr'), Js('rl'), Js('s'), Js('st'), Js('sr'), Js('sh'), Js('th'), Js('tr'), Js('x')]))
var.put('nm12', Js([Js('bv'), Js('ch'), Js('c'), Js('dr'), Js('d'), Js('dd'), Js('dv'), Js('gr'), Js('gl'), Js('gg'), Js('g'), Js('nm'), Js('hn'), Js('h'), Js('l'), Js('ll'), Js('lm'), Js('lt'), Js('ls'), Js('lz'), Js('m'), Js('mm'), Js('mr'), Js('nd'), Js('ng'), Js('nt'), Js('ns'), Js('nl'), Js('nph'), Js('p'), Js('pp'), Js('ph'), Js('phr'), Js('q'), Js('r'), Js('rh'), Js('rl'), Js('rm'), Js('st'), Js('sv'), Js('str'), Js('tr'), Js('th'), Js('v')]))
var.put('nm13', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('l'), Js('ll'), Js('m'), Js('m'), Js('n'), Js('nn'), Js('r'), Js('s'), Js('ss'), Js('sh'), Js('th')]))
pass
pass


# Add lib to the module scope
drWhoGallifreyanNames = var.to_python()