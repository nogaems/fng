__all__ = ['narniaFauns']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'check'])
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
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4'))))
                #for JS loop
                var.put('j', Js(0.0))
                while (var.get('j')<var.get('check').get('length')):
                    try:
                        while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                            var.put('names', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4'))))
                    finally:
                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            else:
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js('u'))+var.get('nm4').get(var.get('rnd4'))))
                #for JS loop
                var.put('j', Js(0.0))
                while (var.get('j')<var.get('check').get('length')):
                    try:
                        while PyJsStrictEq(var.get('names'),var.get('check').get(var.get('j'))):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js('u'))+var.get('nm4').get(var.get('rnd4'))))
                    finally:
                            (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('t'), Js('v')]))
var.put('nm2', Js([Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('a'), Js('o'), Js('u'), Js('au'), Js('oa'), Js('ua'), Js('aa')]))
var.put('nm3', Js([Js('lm'), Js('ln'), Js('ll'), Js('lr'), Js('l'), Js('lb'), Js('mm'), Js('mn'), Js('mr'), Js('mt'), Js('n'), Js('nn'), Js('nt'), Js('nm'), Js('rr'), Js('rn'), Js('rm'), Js('rl'), Js('rv'), Js('r'), Js('s'), Js('ss'), Js('sm'), Js('sl'), Js('st')]))
var.put('nm4', Js([Js('ns'), Js('ms'), Js('ls'), Js('s'), Js('s'), Js('s'), Js('s'), Js('s'), Js('s'), Js('s')]))
var.put('nm5', Js([Js('ia'), Js('a'), Js('ea'), Js('ia'), Js('ia')]))
var.put('check', Js([Js('anal'), Js('anus'), Js('arse'), Js('ass'), Js('balls'), Js('bastard'), Js('biatch'), Js('bigot'), Js('bitch'), Js('bollock'), Js('bollok'), Js('boner'), Js('boob'), Js('bugger'), Js('bum'), Js('butt'), Js('clitoris'), Js('cock'), Js('coon'), Js('crap'), Js('cunt'), Js('damn'), Js('dick'), Js('dildo'), Js('dyke'), Js('fag'), Js('feck'), Js('felching'), Js('fellate'), Js('fellatio'), Js('flange'), Js('fuck'), Js('gay'), Js('lust'), Js('goddamn'), Js('homo'), Js('jackass'), Js('jerk'), Js('jizz'), Js('knobend'), Js('labia'), Js('muff'), Js('nigga'), Js('nigger'), Js('penis'), Js('piss'), Js('poop'), Js('prick'), Js('pube'), Js('pussy'), Js('queer'), Js('scrotum'), Js('sex'), Js('shit'), Js('slut'), Js('smegma'), Js('spunk'), Js('tit'), Js('tosser'), Js('turd'), Js('twat'), Js('vagina'), Js('wank'), Js('whore'), Js('wtf')]))
pass
pass


# Add lib to the module scope
narniaFauns = var.to_python()