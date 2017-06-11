__all__ = ['mgtCentaurs']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm5b', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            if PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5b').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('lName', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5b').get(var.get('rnd5')))+Js("'s "))+var.get('nm11').get(var.get('rnd6'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                while PyJsStrictEq(var.get('nm10').get(var.get('rnd')),var.get('nm11').get(var.get('rnd2'))):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                var.put('lName', ((var.get('nm10').get(var.get('rnd'))+Js(' '))+var.get('nm11').get(var.get('rnd2'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', (((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+Js(', '))+var.get('lName')))
                    else:
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        while PyJsStrictEq(var.get('nm9').get(var.get('rnd8')),var.get('nm8').get(var.get('rnd3'))):
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('names', (((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd8')))+var.get('nm7').get(var.get('rnd9')))+Js(', '))+var.get('lName')))
                else:
                    var.put('names', var.get('lName'))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('i')<Js(3.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('lName')))
                    else:
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        while PyJsStrictEq(var.get('nm4').get(var.get('rnd8')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('lName')))
                else:
                    var.put('names', var.get('lName'))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('c'), Js('g'), Js('j'), Js('k'), Js('r'), Js('s'), Js('v'), Js('x'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('g'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('y'), Js('z')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('n'), Js('t'), Js('v'), Js('z')]))
var.put('nm5', Js([Js('c'), Js('l'), Js('n'), Js('r'), Js('s'), Js('t'), Js('x')]))
var.put('nm5b', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('l'), Js('n'), Js('r'), Js('s'), Js('t'), Js('x')]))
var.put('nm6', Js([Js(''), Js(''), Js('c'), Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('t')]))
var.put('nm7', Js([Js('a'), Js('i'), Js('e'), Js('a'), Js('i'), Js('e'), Js('a'), Js('i'), Js('e'), Js('y'), Js('y'), Js('a'), Js('i'), Js('e'), Js('a'), Js('i'), Js('e'), Js('y'), Js('ea'), Js('ia'), Js('ua')]))
var.put('nm8', Js([Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('z')]))
var.put('nm9', Js([Js('d'), Js('f'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm10', Js([Js('Abandoned'), Js('Accursed'), Js('Adept'), Js('Adored'), Js('Aggravated'), Js('Aggressive'), Js('Agitated'), Js('Alienated'), Js('Angry'), Js('Animated'), Js('Austere'), Js('Battlefield'), Js('Blind'), Js('Boreal'), Js('Brave'), Js('Broken'), Js('Careful'), Js('Careless'), Js('Cautious'), Js('Centaur'), Js('Chief'), Js('Colossal'), Js('Composed'), Js('Corrupt'), Js('Corrupted'), Js('Crooked'), Js('Cruel'), Js('Defiant'), Js('Delirious'), Js('Determined'), Js('Devoted'), Js('Diligent'), Js('Disloyal'), Js('Dowsing'), Js('Faithful'), Js('Fearless'), Js('Feisty'), Js('Forsaken'), Js('Gifted'), Js('Graceful'), Js('Grand'), Js('Grim'), Js('Idle'), Js('Infamous'), Js('Juvenile'), Js('Kind'), Js('Kindhearted'), Js('Leaf'), Js('Loaming'), Js('Lone'), Js('Mindless'), Js('Misguided'), Js('Naive'), Js('Nervous'), Js('Nimble'), Js('Outlandish'), Js('Phantom'), Js('Possessed'), Js('Prestigious'), Js('Prime'), Js('Roaming'), Js('Serene'), Js('Shadowy'), Js('Sneaking'), Js('Sneaky'), Js('Spellbane'), Js('Spellbound'), Js('Spirit'), Js('Swift'), Js('Thunderous'), Js('Tired'), Js('Torn'), Js('Trusted'), Js('Turbulent'), Js('Twin'), Js('Unruly'), Js('Unwielding'), Js('Venerated'), Js('Vengeful'), Js('Warped'), Js('Watchful'), Js('Wicked'), Js('Wild'), Js('Wrathful'), Js('Wretched'), Js('Young')]))
var.put('nm11', Js([Js('Adept'), Js('Archer'), Js('Barbarian'), Js('Battlemaster'), Js('Binder'), Js('Brawler'), Js('Brute'), Js('Caster'), Js('Centaur'), Js('Champion'), Js('Charger'), Js('Chieftain'), Js('Courser'), Js('Crusader'), Js('Dancer'), Js('Disciple'), Js('Elder'), Js('Fanatic'), Js('Guardian'), Js('Healer'), Js('Herald'), Js('Hero'), Js('Marauder'), Js('Oracle'), Js('Outrider'), Js('Protector'), Js('Raider'), Js('Ranger'), Js('Rootbinder'), Js('Rootcaster'), Js('Rootcrasher'), Js('Safeguard'), Js('Savage'), Js('Scavenger'), Js('Scout'), Js('Scrounger'), Js('Seer'), Js('Sentinel'), Js('Shaman'), Js('Slayer'), Js('Spellcaster'), Js('Stomper'), Js('Tactician'), Js('Thunderhoof'), Js('Trailblazer'), Js('Trampler'), Js('Trapper'), Js('Trickster'), Js('Veteran'), Js('Vinecaster'), Js('Vinecrasher'), Js('Warchief'), Js('Warden'), Js('Warmage'), Js('Warmaster'), Js('Weaver')]))
pass
pass


# Add lib to the module scope
mgtCentaurs = var.to_python()