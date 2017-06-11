__all__ = ['gardenGnomes']

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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(5.0)):
                    while (var.get('rnd')<Js(4.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(7.0)):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm7').get(var.get('rnd5'))))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm12').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm6').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    if (var.get('i')<Js(5.0)):
                        while (var.get('rnd')<Js(4.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('names', ((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                    else:
                        if (var.get('i')<Js(7.0)):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd5'))))
                        else:
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((var.get('nm8').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm9').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    if (var.get('i')<Js(5.0)):
                        var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                    else:
                        if (var.get('i')<Js(7.0)):
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm4').get(var.get('rnd5'))))
                        else:
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('cl'), Js('d'), Js('fr'), Js('g'), Js('gn'), Js('h'), Js('j'), Js('kn'), Js('kl'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('sc'), Js('sl'), Js('sn'), Js('sm'), Js('t'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('y'), Js('y'), Js('y'), Js('oo'), Js('ee'), Js('aa'), Js('ie'), Js('ai')]))
var.put('nm3', Js([Js('bbn'), Js('bk'), Js('bn'), Js('bbr'), Js('db'), Js('dd'), Js('ddw'), Js('dn'), Js('ddn'), Js('gn'), Js('gb'), Js('k'), Js('km'), Js('kn'), Js('kp'), Js('kw'), Js('lk'), Js('lb'), Js('llb'), Js('lv'), Js('mb'), Js('mj'), Js('mm'), Js('mp'), Js('mt'), Js('mw'), Js('mz'), Js('md'), Js('nb'), Js('nj'), Js('nk'), Js('nkk'), Js('nsb'), Js('nsm'), Js('nsn'), Js('nz'), Js('nzb'), Js('ngn'), Js('pn'), Js('pp'), Js('pr'), Js('r'), Js('rk'), Js('rb'), Js('rw'), Js('v')]))
var.put('nm4', Js([Js('c'), Js('ck'), Js('g'), Js('m'), Js('p'), Js('r'), Js('rt'), Js('ss'), Js('st'), Js('t')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('bl'), Js('c'), Js('cl'), Js('f'), Js('fl'), Js('fn'), Js('g'), Js('gl'), Js('gn'), Js('h'), Js('l'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('sh'), Js('sl'), Js('sn'), Js('sm'), Js('t'), Js('th'), Js('w')]))
var.put('nm6', Js([Js('bbl'), Js('bbn'), Js('bn'), Js('bl'), Js('db'), Js('dd'), Js('ddl'), Js('dl'), Js('dw'), Js('ddw'), Js('dn'), Js('ddn'), Js('gn'), Js('gb'), Js('gl'), Js('km'), Js('kn'), Js('kw'), Js('lk'), Js('lm'), Js('lw'), Js('lb'), Js('llb'), Js('llm'), Js('ln'), Js('lln'), Js('lv'), Js('mb'), Js('mm'), Js('mw'), Js('md'), Js('nb'), Js('nk'), Js('nkl'), Js('nsm'), Js('nsn'), Js('ngl'), Js('ngn'), Js('pn'), Js('pp'), Js('pw'), Js('pr'), Js('r'), Js('rb'), Js('rw'), Js('v')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js('l'), Js('ll'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('ss'), Js('t'), Js('th')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('c'), Js('cl'), Js('d'), Js('f'), Js('fl'), Js('fn'), Js('g'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('kl'), Js('kn'), Js('l'), Js('m'), Js('n'), Js('p'), Js('ph'), Js('r'), Js('sc'), Js('sh'), Js('sl'), Js('sn'), Js('sm'), Js('t'), Js('th'), Js('w'), Js('z')]))
var.put('nm9', Js([Js('bbl'), Js('bbn'), Js('bk'), Js('bn'), Js('bl'), Js('bbr'), Js('db'), Js('dd'), Js('ddl'), Js('dl'), Js('dw'), Js('ddw'), Js('dn'), Js('ddn'), Js('gn'), Js('gb'), Js('gl'), Js('k'), Js('kl'), Js('km'), Js('kn'), Js('kp'), Js('kw'), Js('lk'), Js('lm'), Js('lw'), Js('lb'), Js('llb'), Js('llm'), Js('ln'), Js('lln'), Js('lv'), Js('mb'), Js('mj'), Js('mm'), Js('mp'), Js('mt'), Js('mw'), Js('mz'), Js('md'), Js('nb'), Js('nj'), Js('nk'), Js('nkk'), Js('nkl'), Js('nsb'), Js('nsm'), Js('nsn'), Js('nz'), Js('nzb'), Js('ngl'), Js('ngn'), Js('pn'), Js('pp'), Js('pw'), Js('pr'), Js('r'), Js('rk'), Js('rb'), Js('rw'), Js('v')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ck'), Js('g'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('p'), Js('r'), Js('rt'), Js('s'), Js('ss'), Js('st'), Js('t')]))
var.put('nm11', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('v')]))
var.put('nm12', Js([Js('b'), Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('v'), Js('w')]))
var.put('nm13', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('w')]))
pass
pass


# Add lib to the module scope
gardenGnomes = var.to_python()