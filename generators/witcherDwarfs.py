__all__ = ['witcherDwarfs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm18', 'nm14', 'nm17', 'nm3', 'nm7', 'nm9', 'nm10', 'nm21', 'nm2', 'nm15', 'nm20'])
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
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
            var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
            var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
            var.put('rnd13', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length'))))
            var.put('rnd14', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm21').get('length'))))
            if (var.get('rnd11')<Js(60.0)):
                var.put('rnd12', Js(0.0))
                var.put('rnd13', Js(0.0))
            else:
                while PyJsStrictEq(var.get('rnd12'),Js(0.0)):
                    var.put('rnd12', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
            var.put('lname', ((((((var.get('nm15').get(var.get('rnd8'))+var.get('nm16').get(var.get('rnd9')))+var.get('nm17').get(var.get('rnd10')))+var.get('nm18').get(var.get('rnd11')))+var.get('nm19').get(var.get('rnd12')))+var.get('nm20').get(var.get('rnd13')))+var.get('nm21').get(var.get('rnd14'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7')))+Js(' '))+var.get('lname')))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    if (var.get('rnd4')<Js(30.0)):
                        var.put('rnd5', Js(0.0))
                        var.put('rnd6', Js(0.0))
                    else:
                        while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('names', ((((((((var.get('nm8').get(var.get('rnd'))+var.get('nm9').get(var.get('rnd2')))+var.get('nm10').get(var.get('rnd3')))+var.get('nm11').get(var.get('rnd4')))+var.get('nm12').get(var.get('rnd5')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm14').get(var.get('rnd7')))+Js(' '))+var.get('lname')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+Js(' '))+var.get('lname')))
                else:
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('rnd4')<Js(40.0)):
                        var.put('rnd5', Js(0.0))
                        var.put('rnd6', Js(0.0))
                    else:
                        while PyJsStrictEq(var.get('rnd5'),Js(0.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+Js(' '))+var.get('lname')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('bl'), Js('br'), Js('c'), Js('cr'), Js('d'), Js('dh'), Js('f'), Js('fl'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('l'), Js('m'), Js('p'), Js('r'), Js('rh'), Js('shr'), Js('sk'), Js('sh'), Js('th'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('zh')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ie'), Js('au'), Js('ia'), Js('ei'), Js('ou')]))
var.put('nm3', Js([Js('c'), Js('cc'), Js('cr'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gg'), Js('gm'), Js('gn'), Js('h'), Js('l'), Js('lc'), Js('ld'), Js('lfl'), Js('lk'), Js('ll'), Js('lm'), Js('lr'), Js('lt'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('nb'), Js('nc'), Js('nd'), Js('nn'), Js('nr'), Js('nt'), Js('r'), Js('rb'), Js('rcl'), Js('rd'), Js('rg'), Js('rl'), Js('rm'), Js('rn'), Js('rp'), Js('rt'), Js('rth'), Js('s'), Js('sc'), Js('sr'), Js('st'), Js('v'), Js('ym'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ie'), Js('au'), Js('ia'), Js('ei'), Js('ou')]))
var.put('nm5', Js([Js(''), Js('c'), Js('cc'), Js('cr'), Js('d'), Js('dh'), Js('dr'), Js('g'), Js('gg'), Js('gm'), Js('gn'), Js('h'), Js('l'), Js('lc'), Js('ld'), Js('lfl'), Js('lk'), Js('ll'), Js('lm'), Js('lr'), Js('lt'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('nb'), Js('nc'), Js('nd'), Js('nn'), Js('nr'), Js('nt'), Js('r'), Js('rb'), Js('rcl'), Js('rd'), Js('rg'), Js('rl'), Js('rm'), Js('rn'), Js('rp'), Js('rt'), Js('rth'), Js('s'), Js('sc'), Js('sr'), Js('st'), Js('v'), Js('ym'), Js('z')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('ck'), Js('k'), Js('l'), Js('ld'), Js('lm'), Js('n'), Js('nd'), Js('nn'), Js('rn'), Js('rm'), Js('rd'), Js('r'), Js('rk'), Js('rd'), Js('s')]))
var.put('nm8', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('ch'), Js('cl'), Js('d'), Js('dh'), Js('f'), Js('fl'), Js('g'), Js('gh'), Js('gr'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('rh'), Js('sh'), Js('s'), Js('st'), Js('th'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('zh')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('eu'), Js('ea'), Js('ia'), Js('eo'), Js('io')]))
var.put('nm10', Js([Js('c'), Js('cc'), Js('ch'), Js('d'), Js('dh'), Js('dd'), Js('g'), Js('gl'), Js('gn'), Js('gm'), Js('gh'), Js('gr'), Js('h'), Js('l'), Js('ln'), Js('lm'), Js('ll'), Js('lr'), Js('ls'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('ns'), Js('nm'), Js('nl'), Js('ng'), Js('nz'), Js('nw'), Js('p'), Js('ph'), Js('r'), Js('rh'), Js('rl'), Js('rn'), Js('rm'), Js('rs'), Js('s'), Js('sh'), Js('sm'), Js('sn'), Js('st'), Js('v'), Js('w'), Js('lw'), Js('z'), Js('zh'), Js('zn'), Js('zm')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('eu'), Js('ea'), Js('ia'), Js('eo'), Js('io')]))
var.put('nm12', Js([Js(''), Js('c'), Js('cc'), Js('ch'), Js('d'), Js('dh'), Js('dd'), Js('g'), Js('gl'), Js('gn'), Js('gm'), Js('gh'), Js('gr'), Js('h'), Js('l'), Js('ln'), Js('lm'), Js('ll'), Js('lr'), Js('ls'), Js('m'), Js('mm'), Js('mn'), Js('n'), Js('ns'), Js('nm'), Js('nl'), Js('ng'), Js('nz'), Js('nw'), Js('p'), Js('ph'), Js('r'), Js('rh'), Js('rl'), Js('rn'), Js('rm'), Js('rs'), Js('s'), Js('sh'), Js('sm'), Js('sn'), Js('st'), Js('v'), Js('w'), Js('lw'), Js('z'), Js('zh'), Js('zn'), Js('zm')]))
var.put('nm14', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('n'), Js('th'), Js('s')]))
var.put('nm15', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('c'), Js('ch'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('g'), Js('gr'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('sk'), Js('st'), Js('str'), Js('s'), Js('t'), Js('tr'), Js('v'), Js('z')]))
var.put('nm16', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ei'), Js('ia'), Js('ea'), Js('ai')]))
var.put('nm17', Js([Js('c'), Js('cc'), Js('ck'), Js('cr'), Js('dn'), Js('g'), Js('gg'), Js('gl'), Js('gn'), Js('gr'), Js('hl'), Js('hlb'), Js('hln'), Js('hn'), Js('l'), Js('ld'), Js('lm'), Js('ln'), Js('lr'), Js('n'), Js('nd'), Js('ngv'), Js('nl'), Js('nm'), Js('nr'), Js('r'), Js('rd'), Js('rg'), Js('rl'), Js('rn'), Js('rt'), Js('s'), Js('sr'), Js('ssl'), Js('st'), Js('tt'), Js('v'), Js('zd')]))
var.put('nm18', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ei'), Js('ia'), Js('ea'), Js('ai')]))
var.put('nm19', Js([Js(''), Js('c'), Js('cc'), Js('ck'), Js('cr'), Js('dn'), Js('g'), Js('gg'), Js('gl'), Js('gn'), Js('gr'), Js('hl'), Js('hlb'), Js('hln'), Js('hn'), Js('l'), Js('ld'), Js('lm'), Js('ln'), Js('lr'), Js('n'), Js('nd'), Js('ngv'), Js('nl'), Js('nm'), Js('nr'), Js('r'), Js('rd'), Js('rg'), Js('rl'), Js('rn'), Js('rt'), Js('s'), Js('sr'), Js('ssl'), Js('st'), Js('tt'), Js('v'), Js('zd')]))
var.put('nm20', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('au'), Js('ei'), Js('ia'), Js('ea'), Js('ai')]))
var.put('nm21', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('ck'), Js('ggs'), Js('gs'), Js('l'), Js('ld'), Js('ls'), Js('lt'), Js('m'), Js('n'), Js('r'), Js('rd'), Js('rg'), Js('s'), Js('ss'), Js('st'), Js('t'), Js('y'), Js('ys')]))
pass
pass


# Add lib to the module scope
witcherDwarfs = var.to_python()