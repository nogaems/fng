__all__ = ['speciesNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm8', 'nm3', 'nm7', 'nm2', 'check'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4'))))
                #for JS loop
                var.put('j', Js(0.0))
                while (var.get('j')<var.get('check').get('length')):
                    try:
                        while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                            var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4'))))
                    finally:
                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            else:
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd7'))))
                #for JS loop
                var.put('j', Js(0.0))
                while (var.get('j')<var.get('check').get('length')):
                    try:
                        while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                            var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd6')))+var.get('nm8').get(var.get('rnd7'))))
                    finally:
                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('ai'), Js('ea'), Js('eo'), Js('oi'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('ch'), Js('chr'), Js('chl'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('sr'), Js('tr'), Js('str'), Js('bl'), Js('cl'), Js('fl'), Js('kl'), Js('pl'), Js('sl'), Js('vl'), Js('ph'), Js('sh')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('ai'), Js('ea'), Js('eo'), Js('oi'), Js('y')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js('bl'), Js('br'), Js('bb'), Js('bs'), Js('bd'), Js('bn'), Js('ch'), Js('chl'), Js('chr'), Js('cl'), Js('ck'), Js('cn'), Js('cr'), Js('cc'), Js('dr'), Js('dl'), Js('ds'), Js('dn'), Js('dd'), Js('fl'), Js('ff'), Js('fr'), Js('fn'), Js('gr'), Js('gn'), Js('gs'), Js('gl'), Js('gg'), Js('kl'), Js('kh'), Js('kn'), Js('kk'), Js('kr'), Js('ll'), Js('ln'), Js('lm'), Js('ls'), Js('ld'), Js('lb'), Js('mm'), Js('mn'), Js('md'), Js('ml'), Js('ms'), Js('nn'), Js('nd'), Js('ng'), Js('nt'), Js('ns'), Js('nst'), Js('pp'), Js('ph'), Js('pl'), Js('ps'), Js('pd'), Js('pr'), Js('rr'), Js('rd'), Js('rn'), Js('rl'), Js('rs'), Js('rt'), Js('ss'), Js('sh'), Js('sht'), Js('sl'), Js('sn'), Js('sr'), Js('st'), Js('str'), Js('tr'), Js('tt'), Js('th'), Js('tn'), Js('tm'), Js('tv'), Js('vv'), Js('vl'), Js('vn')]))
var.put('nm7', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('x'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('x'), Js('ch'), Js('ck'), Js('th'), Js('gs'), Js('rd'), Js('rg'), Js('rk'), Js('rm'), Js('rn'), Js('rq'), Js('rs'), Js('rst'), Js('rx'), Js('ds'), Js('cs'), Js('fs'), Js('gs'), Js('ks'), Js('ls'), Js('ms'), Js('ns'), Js('ps'), Js('rs'), Js('ts'), Js('st'), Js('ph'), Js('sh'), Js('ln'), Js('lm'), Js('lk'), Js('ld'), Js('lt')]))
var.put('nm8', Js([Js('c'), Js('gian'), Js('lese'), Js('lian'), Js('n'), Js('nan'), Js('ne'), Js('nee'), Js('nes'), Js('nian'), Js('nin'), Js('no'), Js('nsian'), Js('r'), Js('rd'), Js('rn'), Js('se'), Js('sh'), Js('t'), Js('te'), Js('vese'), Js('vian')]))
var.put('check', Js([Js('anal'), Js('anus'), Js('arse'), Js('ass'), Js('balls'), Js('bastard'), Js('biatch'), Js('bigot'), Js('bitch'), Js('bollock'), Js('bollok'), Js('boner'), Js('boob'), Js('bugger'), Js('bum'), Js('butt'), Js('clitoris'), Js('cock'), Js('coon'), Js('crap'), Js('cunt'), Js('damn'), Js('dick'), Js('dildo'), Js('dyke'), Js('fag'), Js('feck'), Js('felching'), Js('fellate'), Js('fellatio'), Js('flange'), Js('fuck'), Js('gay'), Js('lust'), Js('goddamn'), Js('homo'), Js('jackass'), Js('jerk'), Js('jizz'), Js('knobend'), Js('labia'), Js('muff'), Js('nigga'), Js('nigger'), Js('penis'), Js('piss'), Js('poop'), Js('prick'), Js('pube'), Js('pussy'), Js('queer'), Js('scrotum'), Js('sex'), Js('shit'), Js('slut'), Js('smegma'), Js('spunk'), Js('tit'), Js('tosser'), Js('turd'), Js('twat'), Js('vagina'), Js('wank'), Js('whore'), Js('wtf')]))
pass
pass


# Add lib to the module scope
speciesNames = var.to_python()