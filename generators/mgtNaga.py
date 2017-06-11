__all__ = ['mgtNaga']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
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
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('lName', (((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4'))))
            else:
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm4').get(var.get('rnd5'))):
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('lName', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6'))))
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                if (var.get('i')<Js(3.0)):
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+Js(' '))+var.get('lName')))
                else:
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm2').get(var.get('rnd6')))+Js(' '))+var.get('lName')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((var.get('lName')+Js(' '))+var.get('nm5').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('g'), Js('h'), Js('j'), Js('kh'), Js('n'), Js('r'), Js('s'), Js('t'), Js('th'), Js('y'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('g'), Js('k'), Js('l'), Js('n'), Js('r'), Js('s'), Js('t'), Js('d'), Js('g'), Js('k'), Js('l'), Js('n'), Js('r'), Js('s'), Js('t'), Js('d'), Js('dd'), Js('dr'), Js('g'), Js('gg'), Js('gr'), Js('gl'), Js('gn'), Js('gd'), Js('k'), Js('kk'), Js('kl'), Js('kn'), Js('kd'), Js('kdr'), Js('kr'), Js('l'), Js('ll'), Js('lk'), Js('ld'), Js('lg'), Js('ldr'), Js('lgr'), Js('lkr'), Js('n'), Js('nn'), Js('nd'), Js('ndr'), Js('ng'), Js('ngr'), Js('r'), Js('rr'), Js('rh'), Js('rn'), Js('s'), Js('sh'), Js('shr'), Js('sr'), Js('shn'), Js('sn'), Js('t'), Js('thn'), Js('thr'), Js('tr')]))
var.put('nm4', Js([Js('d'), Js('g'), Js('k'), Js('l'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm5', Js([Js('Archer'), Js('Assassin'), Js('Augur'), Js('Bonekeeper'), Js('Brute'), Js('Butcher'), Js('Champion'), Js('Clairvoyant'), Js('Conqueror'), Js('Conscript'), Js('Deceiver'), Js('Defender'), Js('Defiant'), Js('Diviner'), Js('Drowner'), Js('Enforcer'), Js('Executioner'), Js('Fiend'), Js('Flayer'), Js('Guerrilla'), Js('Insurgent'), Js('Keeper'), Js('Mutineer'), Js('Oracle'), Js('Ranger'), Js('Rebel'), Js('Renegade'), Js('Resistance'), Js('Savage'), Js('Scout'), Js('Seer'), Js('Shepherd'), Js('Skullkeeper'), Js('Slayer'), Js('Soothsayer'), Js('Spell-Eater'), Js('Spellcaster'), Js('Spellcatcher'), Js('Spellsnatcher'), Js('Spy'), Js('Strangler'), Js('Subjugator'), Js('Swindler'), Js('Tyrant'), Js('Vandal'), Js('Vanquisher'), Js('Victor'), Js('Vigilante'), Js('Vindicator'), Js('Vizier'), Js('Wanderer'), Js('Warrior')]))
pass
pass


# Add lib to the module scope
mgtNaga = var.to_python()