__all__ = ['swDarthNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(13.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    while (var.get('rnd5')<Js(10.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', (((Js('Darth ')+var.get('nm5').get(var.get('rnd')))+var.get('nm6').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', (((((Js('Darth ')+var.get('nm5').get(var.get('rnd')))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm8').get(var.get('rnd5'))))
                    else:
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                        var.put('names', (((((((Js('Darth ')+var.get('nm5').get(var.get('rnd')))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+var.get('nm8').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(10.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    while (var.get('rnd5')<Js(7.0)):
                        var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', (((Js('Darth ')+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((Js('Darth ')+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('ch'), Js('chr'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gl'), Js('gr'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kh'), Js('l'), Js('m'), Js('mh'), Js('n'), Js('pl'), Js('pr'), Js('q'), Js('r'), Js('s'), Js('sc'), Js('sk'), Js('st'), Js('str'), Js('sr'), Js('t'), Js('th'), Js('tr'), Js('v'), Js('w'), Js('wr'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('y'), Js('y'), Js('ou'), Js('ae'), Js('ea'), Js('ui'), Js('ia'), Js('ue'), Js('ei'), Js('uy')]))
var.put('nm3', Js([Js('ct'), Js('cn'), Js('cm'), Js('gr'), Js('kk'), Js('kr'), Js('kt'), Js('ll'), Js('lf'), Js('lg'), Js('lr'), Js('ld'), Js('nn'), Js('nt'), Js('nr'), Js('mr'), Js('mm'), Js('md'), Js('rr'), Js('rk'), Js('rt'), Js('st'), Js('sn'), Js('sm'), Js('th'), Js('sh'), Js('tt'), Js('tr'), Js('zz')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('d'), Js('dd'), Js('ft'), Js('hl'), Js('k'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('r'), Js('rd'), Js('rn'), Js('rr'), Js('s'), Js('t'), Js('th'), Js('wn'), Js('x')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('bh'), Js('c'), Js('ch'), Js('f'), Js('fr'), Js('g'), Js('gh'), Js('h'), Js('j'), Js('k'), Js('kh'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('phr'), Js('phl'), Js('q'), Js('r'), Js('rh'), Js('s'), Js('sh'), Js('st'), Js('t'), Js('tr'), Js('th'), Js('thr'), Js('v'), Js('w'), Js('wh'), Js('x'), Js('xh'), Js('z'), Js('zh')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ae'), Js('ia'), Js('ie'), Js('ei'), Js('ui')]))
var.put('nm7', Js([Js('b'), Js('ch'), Js('chr'), Js('cr'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gr'), Js('gn'), Js('gm'), Js('gl'), Js('k'), Js('kn'), Js('km'), Js('kh'), Js('kk'), Js('l'), Js('ll'), Js('lm'), Js('lr'), Js('ld'), Js('lm'), Js('m'), Js('mn'), Js('mr'), Js('mm'), Js('n'), Js('nn'), Js('nr'), Js('ns'), Js('nz'), Js('nl'), Js('r'), Js('rm'), Js('rl'), Js('rz'), Js('rg'), Js('rr'), Js('tr'), Js('ttr'), Js('th'), Js('thr'), Js('thn'), Js('thm'), Js('y')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('f'), Js('h'), Js('l'), Js('n'), Js('ph'), Js('r'), Js('s'), Js('sh'), Js('ss'), Js('th'), Js('w'), Js('x')]))
pass
pass


# Add lib to the module scope
swDarthNames = var.to_python()