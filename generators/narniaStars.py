__all__ = ['narniaStars']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'check'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
            if (var.get('i')<Js(5.0)):
                if (var.get('rnd')<Js(3.0)):
                    while (var.get('rnd5')<Js(4.0)):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                #for JS loop
                var.put('j', Js(0.0))
                while (var.get('j')<var.get('check').get('length')):
                    try:
                        while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
                    finally:
                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            else:
                var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
                #for JS loop
                var.put('j', Js(0.0))
                while (var.get('j')<var.get('check').get('length')):
                    try:
                        while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5'))))
                    finally:
                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('a'), Js('i'), Js('o'), Js('u'), Js('ia'), Js('ea'), Js('ua')]))
var.put('nm3', Js([Js('g'), Js('gn'), Js('l'), Js('lm'), Js('ln'), Js('m'), Js('mn'), Js('n'), Js('r'), Js('rv'), Js('v'), Js('w'), Js('z')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('gn'), Js('gd'), Js('k'), Js('kn'), Js('l'), Js('ll'), Js('ld'), Js('lg'), Js('ln'), Js('mb'), Js('mn'), Js('m'), Js('ml'), Js('nd'), Js('ng'), Js('nm'), Js('nn'), Js('n'), Js('nt'), Js('nz'), Js('rn'), Js('rl'), Js('sn'), Js('sl'), Js('s'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js('d'), Js('l'), Js('m'), Js('n'), Js('s')]))
var.put('check', Js([Js('anal'), Js('anus'), Js('arse'), Js('ass'), Js('balls'), Js('bastard'), Js('biatch'), Js('bigot'), Js('bitch'), Js('bollock'), Js('bollok'), Js('boner'), Js('boob'), Js('bugger'), Js('bum'), Js('butt'), Js('clitoris'), Js('cock'), Js('coon'), Js('crap'), Js('cunt'), Js('damn'), Js('dick'), Js('dildo'), Js('dyke'), Js('fag'), Js('feck'), Js('felching'), Js('fellate'), Js('fellatio'), Js('flange'), Js('fuck'), Js('gay'), Js('lust'), Js('goddamn'), Js('homo'), Js('jackass'), Js('jerk'), Js('jizz'), Js('knobend'), Js('labia'), Js('muff'), Js('nigga'), Js('nigger'), Js('penis'), Js('piss'), Js('poop'), Js('prick'), Js('pube'), Js('pussy'), Js('queer'), Js('scrotum'), Js('sex'), Js('shit'), Js('slut'), Js('smegma'), Js('spunk'), Js('tit'), Js('tosser'), Js('turd'), Js('twat'), Js('vagina'), Js('wank'), Js('whore'), Js('wtf')]))
pass
pass


# Add lib to the module scope
narniaStars = var.to_python()