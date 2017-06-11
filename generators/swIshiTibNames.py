__all__ = ['swIshiTibNames']

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
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                while (var.get('rnd7')<Js(3.0)):
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                while (var.get('rnd10')<Js(4.0)):
                    var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                var.put('namelast', ((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm12').get(var.get('rnd10'))))
            else:
                var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(6.0)):
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd5b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5b')))+var.get('nm6').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(3.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(4.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd5b', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5b')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('c'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('uu'), Js('ue'), Js('ia'), Js('ie'), Js('ui'), Js('ua'), Js('aa'), Js('ee')]))
var.put('nm3', Js([Js('br'), Js('bl'), Js('b'), Js('g'), Js('gg'), Js('gr'), Js('ht'), Js('hk'), Js('hr'), Js('hz'), Js('k'), Js('kz'), Js('kr'), Js('kl'), Js('km'), Js('kn'), Js('l'), Js('ll'), Js('lz'), Js('lr'), Js('lb'), Js('lg'), Js('lt'), Js('m'), Js('mb'), Js('ml'), Js('mk'), Js('mr'), Js('mz'), Js('n'), Js('nn'), Js('ng'), Js('nr'), Js('nk'), Js('nl'), Js('nt'), Js('nz'), Js('pl'), Js('pr'), Js('pz'), Js('r'), Js('rl'), Js('rg'), Js('rk'), Js('rm'), Js('rn'), Js('rt'), Js('rz'), Js('t'), Js('tch'), Js('tl'), Js('zk'), Js('zl'), Js('zr')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js('bb'), Js('c'), Js('ch'), Js('g'), Js('k'), Js('ks'), Js('l'), Js('lk'), Js('m'), Js('n'), Js('nd'), Js('rc'), Js('rt'), Js('s'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('f'), Js('gh'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('w'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ya'), Js('ye'), Js('ie'), Js('ia'), Js('ea'), Js('eo')]))
var.put('nm7', Js([Js('bl'), Js('ff'), Js('gn'), Js('gl'), Js('gm'), Js('gh'), Js('hr'), Js('hn'), Js('hm'), Js('hl'), Js('k'), Js('kh'), Js('kl'), Js('l'), Js('ll'), Js('lr'), Js('ln'), Js('lm'), Js('lg'), Js('lt'), Js('ls'), Js('lz'), Js('m'), Js('mm'), Js('mr'), Js('mz'), Js('mn'), Js('mh'), Js('mf'), Js('n'), Js('nn'), Js('ng'), Js('nr'), Js('nl'), Js('nt'), Js('nz'), Js('ns'), Js('nf'), Js('nh'), Js('ph'), Js('pl'), Js('pr'), Js('ps'), Js('r'), Js('rr'), Js('rl'), Js('rs'), Js('tz'), Js('rth'), Js('s'), Js('sp'), Js('sh'), Js('sn'), Js('sm'), Js('th'), Js('t')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('th')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('dr'), Js('f'), Js('gr'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sl'), Js('sh'), Js('t'), Js('tr'), Js('th'), Js('v'), Js('z')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ae'), Js('aa'), Js('ie'), Js('oo'), Js('ay')]))
var.put('nm11', Js([Js('br'), Js('b'), Js('d'), Js('dr'), Js('g'), Js('gg'), Js('gr'), Js('hr'), Js('ht'), Js('k'), Js('kz'), Js('kr'), Js('kl'), Js('km'), Js('l'), Js('ll'), Js('lr'), Js('lz'), Js('lg'), Js('ld'), Js('lb'), Js('ls'), Js('ln'), Js('m'), Js('mb'), Js('mz'), Js('mr'), Js('mk'), Js('mm'), Js('n'), Js('nn'), Js('nr'), Js('nd'), Js('ng'), Js('r'), Js('rd'), Js('rg'), Js('rk'), Js('rm'), Js('rl'), Js('ssh'), Js('sh'), Js('t'), Js('tl'), Js('th'), Js('zk'), Js('zl'), Js('z')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js('c'), Js('ff'), Js('l'), Js('m'), Js('n'), Js('ng'), Js('rr'), Js('tz'), Js('w')]))
pass
pass


# Add lib to the module scope
swIshiTibNames = var.to_python()