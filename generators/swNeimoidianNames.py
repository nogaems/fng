__all__ = ['swNeimoidianNames']

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
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
            var.put('namelast', ((((var.get('nm9').get(var.get('rnd7'))+var.get('nm10').get(var.get('rnd8')))+var.get('nm11').get(var.get('rnd11')))+var.get('nm10').get(var.get('rnd9')))+var.get('nm12').get(var.get('rnd10'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(4.0)):
                    while (var.get('rnd')<Js(5.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(5.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5')))+Js('  '))+var.get('namelast')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kl'), Js('kr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('sm'), Js('t'), Js('th'), Js('v'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('u'), Js('i'), Js('u'), Js('u'), Js('u'), Js('ai'), Js('au'), Js('oo'), Js('ee'), Js('ui'), Js('oa'), Js('uu')]))
var.put('nm3', Js([Js('b'), Js('bm'), Js('d'), Js('dm'), Js('dml'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('hv'), Js('k'), Js('kv'), Js('l'), Js('lf'), Js('lv'), Js('lr'), Js('lt'), Js('m'), Js('md'), Js('mv'), Js('n'), Js('nv'), Js('nd'), Js('ndd'), Js('nj'), Js('nr'), Js('nt'), Js('p'), Js('r'), Js('rg'), Js('rl'), Js('rr'), Js('sh'), Js('shr'), Js('ss'), Js('t'), Js('th'), Js('w'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('f'), Js('gh'), Js('hn'), Js('k'), Js('l'), Js('lb'), Js('ll'), Js('n'), Js('nd'), Js('p'), Js('ph'), Js('r'), Js('rs'), Js('s'), Js('sk'), Js('t'), Js('th'), Js('tt'), Js('v'), Js('x'), Js('y')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('sn'), Js('sm'), Js('t'), Js('th'), Js('v'), Js('y'), Js('z')]))
var.put('nm6', Js([Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('u'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('u'), Js('uu'), Js('ia'), Js('ai'), Js('ee'), Js('ue'), Js('ui')]))
var.put('nm7', Js([Js('d'), Js('f'), Js('ff'), Js('fn'), Js('g'), Js('gg'), Js('h'), Js('hv'), Js('l'), Js('ll'), Js('m'), Js('mm'), Js('mv'), Js('md'), Js('n'), Js('nn'), Js('nv'), Js('nd'), Js('ph'), Js('s'), Js('sh'), Js('ss'), Js('th'), Js('r'), Js('rr'), Js('rh'), Js('rv'), Js('rl'), Js('rs'), Js('v'), Js('w'), Js('z')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('f'), Js('ff'), Js('h'), Js('l'), Js('ll'), Js('n'), Js('ph'), Js('rn'), Js('s'), Js('ss'), Js('th'), Js('y')]))
var.put('nm9', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('ch'), Js('d'), Js('dr'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('k'), Js('kr'), Js('kh'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('r'), Js('s'), Js('sr'), Js('sh'), Js('t'), Js('tr'), Js('v'), Js('z'), Js('zr')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('o'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('o'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('o'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('o'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('i'), Js('o'), Js('a'), Js('ii'), Js('io'), Js('ai'), Js('ui'), Js('iu'), Js('ee')]))
var.put('nm11', Js([Js('f'), Js('ff'), Js('fr'), Js('fd'), Js('g'), Js('gg'), Js('gr'), Js('gn'), Js('gb'), Js('k'), Js('kk'), Js('kv'), Js('kr'), Js('ll'), Js('lv'), Js('lr'), Js('my'), Js('m'), Js('md'), Js('mm'), Js('mv'), Js('mr'), Js('n'), Js('nn'), Js('nv'), Js('nd'), Js('nk'), Js('nkk'), Js('rt'), Js('tb'), Js('tr'), Js('th'), Js('t'), Js('tt'), Js('tz'), Js('tg'), Js('tf')]))
var.put('nm12', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('th'), Js('y'), Js('x')]))
pass
pass


# Add lib to the module scope
swNeimoidianNames = var.to_python()