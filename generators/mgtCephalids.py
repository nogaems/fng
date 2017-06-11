__all__ = ['mgtCephalids']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                while PyJsStrictEq(var.get('nm2').get(var.get('rnd2')),var.get('nm4').get(var.get('rnd4'))):
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                while PyJsStrictEq(var.get('nm5').get(var.get('rnd6')),var.get('nm4').get(var.get('rnd4'))):
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+Js(', '))+var.get('nm6').get(var.get('rnd7')))+Js(' '))+var.get('nm7').get(var.get('rnd8'))))
            else:
                var.put('names', ((var.get('nm6').get(var.get('rnd7'))+Js(' '))+var.get('nm7').get(var.get('rnd8'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('o'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('b'), Js('d'), Js('g'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v')]))
var.put('nm3', Js([Js('a'), Js('o'), Js('a'), Js('o'), Js('a'), Js('o'), Js('a'), Js('o'), Js('a'), Js('o'), Js('u'), Js('e'), Js('i')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('dh'), Js('g'), Js('kh'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('s'), Js('ss'), Js('sh'), Js('t'), Js('th'), Js('tt'), Js('v'), Js('w'), Js('z'), Js('zh')]))
var.put('nm5', Js([Js('d'), Js('l'), Js('m'), Js('n'), Js('t'), Js('th')]))
var.put('nm6', Js([Js('Abandoned'), Js('Acclaimed'), Js('Aggressive'), Js('Agitated'), Js('Ambitious'), Js('Ancient'), Js('Bitter'), Js('Bold'), Js('Broken'), Js('Callous'), Js('Careless'), Js('Cautious'), Js('Corrupt'), Js('Corrupted'), Js('Crooked'), Js('Cruel'), Js('Dangerous'), Js('Defiant'), Js('Delirious'), Js('Deserted'), Js('Devoted'), Js('Diligent'), Js('Discrete'), Js('Dreary'), Js('Eager'), Js('Enraged'), Js('Evil'), Js('Fearless'), Js('Fickle'), Js('Forsaken'), Js('Frightening'), Js('Grand'), Js('Grave'), Js('Grim'), Js('Gruesome'), Js('Haunting'), Js('Hideous'), Js('Husky'), Js('Infernal'), Js('Juvenile'), Js('Keen'), Js('Livid'), Js('Loathsome'), Js('Lone'), Js('Lost'), Js('Lumbering'), Js('Mad'), Js('Mindless'), Js('Monstrous'), Js('Nasty'), Js('Needy'), Js('Noxious'), Js('Obedient'), Js('Petty'), Js('Powerful'), Js('Prime'), Js('Ragged'), Js('Rash'), Js('Reckless'), Js('Somber'), Js('Spiteful'), Js('Trifling'), Js('Turbulent'), Js('Unfit'), Js('Useless'), Js('Vicious'), Js('Villainous'), Js('Violent'), Js('Weak'), Js('Wicked'), Js('Wild'), Js('Woeful'), Js('Wrathful'), Js('Wretched'), Js('Zealous')]))
var.put('nm7', Js([Js('Agent'), Js('Aristocrat'), Js('Broker'), Js('Bully'), Js('Chandler'), Js('Charmer'), Js('Conjurer'), Js('Dealer'), Js('Defacer'), Js('Diviner'), Js('Escort'), Js('Explorer'), Js('Guard'), Js('Guardian'), Js('Illusionist'), Js('Informer'), Js('Lookout'), Js('Looter'), Js('Mage'), Js('Marauder'), Js('Mediator'), Js('Merchant'), Js('Monger'), Js('Negotiator'), Js('Noble'), Js('Operative'), Js('Oppressor'), Js('Outrider'), Js('Overlord'), Js('Overseer'), Js('Patrician'), Js('Patrol'), Js('Pillager'), Js('Pioneer'), Js('Plunderer'), Js('Ravager'), Js('Recruiter'), Js('Retailer'), Js('Sage'), Js('Scout'), Js('Sentinel'), Js('Sneak'), Js('Soothsayer'), Js('Spellbinder'), Js('Spoiler'), Js('Spy'), Js('Taskmaster'), Js('Trader'), Js('Tyrant'), Js('Vandal'), Js('Vanguard'), Js('Vendor'), Js('Watcher')]))
pass
pass


# Add lib to the module scope
mgtCephalids = var.to_python()