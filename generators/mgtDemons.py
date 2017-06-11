__all__ = ['mgtDemons']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                while PyJsStrictEq(var.get('nm6').get(var.get('rnd')),var.get('nm7').get(var.get('rnd2'))):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('lName', (((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+Js(' '))+var.get('nm8').get(var.get('rnd3'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                while PyJsStrictEq(var.get('nm9').get(var.get('rnd')),var.get('nm8').get(var.get('rnd2'))):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('lName', ((var.get('nm9').get(var.get('rnd'))+Js(' '))+var.get('nm8').get(var.get('rnd2'))))
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5'))):
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                if (var.get('i')<Js(3.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('lName')))
                else:
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('lName')))
            else:
                var.put('names', var.get('lName'))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('c'), Js('g'), Js('k'), Js('m'), Js('l'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('y'), Js('t'), Js('th'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('yo'), Js('ei'), Js('ai'), Js('iu'), Js('aa')]))
var.put('nm3', Js([Js('d'), Js('f'), Js('g'), Js('k'), Js('m'), Js('r'), Js('sh'), Js('th'), Js('x'), Js('z'), Js('d'), Js('f'), Js('g'), Js('k'), Js('m'), Js('r'), Js('sh'), Js('th'), Js('x'), Js('z'), Js('d'), Js('dd'), Js('dr'), Js("d'c"), Js('f'), Js("f'g"), Js('g'), Js('gr'), Js('gn'), Js('gd'), Js('k'), Js('kd'), Js("k'k"), Js('kr'), Js('kk'), Js('kz'), Js("k'z"), Js('lf'), Js("l'k"), Js('lg'), Js("l'g"), Js("l'd"), Js('ld'), Js('lr'), Js("l'c"), Js('lc'), Js('lt'), Js("l't"), Js('m'), Js('mm'), Js('r'), Js("r'z"), Js('rz'), Js('rr'), Js('rg'), Js('rs'), Js("r's"), Js('rm'), Js('shr'), Js('sh'), Js('sr'), Js('th'), Js('x'), Js('z'), Js('zr'), Js('zh'), Js("z'l"), Js("z'g")]))
var.put('nm4', Js([Js('d'), Js('g'), Js('l'), Js('ld'), Js('lg'), Js('ll'), Js('m'), Js('n'), Js('ng'), Js('nd'), Js('nn'), Js('ph'), Js('r'), Js('rr'), Js('s'), Js('ss'), Js('sh'), Js('ts')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js('c'), Js('d'), Js('hl'), Js('l'), Js('n'), Js('r'), Js('s'), Js('x')]))
var.put('nm6', Js([Js('abyss'), Js('ache'), Js('ash'), Js('blaze'), Js('blood'), Js('cinder'), Js('crypt'), Js('dark'), Js('dead'), Js('death'), Js('doom'), Js('dust'), Js('ember'), Js('fire'), Js('flame'), Js('gloom'), Js('gore'), Js('grave'), Js('grief'), Js('grim'), Js('haze'), Js('hell'), Js('hollow'), Js('mind'), Js('nether'), Js('night'), Js('pain'), Js('pit'), Js('pyre'), Js('rue'), Js('ruin'), Js('shadow'), Js('skull'), Js('soot'), Js('sore'), Js('sorrow'), Js('soul'), Js('tomb'), Js('vault'), Js('woe')]))
var.put('nm7', Js([Js('bane'), Js('basher'), Js('bellow'), Js('binder'), Js('blade'), Js('blaze'), Js('blight'), Js('born'), Js('brand'), Js('breaker'), Js('bringer'), Js('cage'), Js('carver'), Js('claw'), Js('cleaver'), Js('cloak'), Js('cloaked'), Js('crest'), Js('dealer'), Js('drifter'), Js('fall'), Js('fang'), Js('flayer'), Js('forge'), Js('forged'), Js('fury'), Js('gaze'), Js('gift'), Js('heart'), Js('horn'), Js('lash'), Js('mane'), Js('maul'), Js('maw'), Js('more'), Js('mourn'), Js('rage'), Js('reaper'), Js('reaver'), Js('rider'), Js('ridge'), Js('ripper'), Js('scar'), Js('shard'), Js('slayer'), Js('spine'), Js('stalk'), Js('stalker'), Js('stride'), Js('strike'), Js('striker'), Js('surge'), Js('sworn'), Js('wing'), Js('wracker'), Js('wreck'), Js('wrecker')]))
var.put('nm8', Js([Js('Overlord'), Js('Pitlord'), Js('Persecutor'), Js('Archdemon'), Js('Demon'), Js('Archfiend'), Js('Archlord'), Js('Overlord'), Js('Pitlord'), Js('Persecutor'), Js('Archdemon'), Js('Demon'), Js('Archfiend'), Js('Archlord'), Js('Annihilator'), Js('Archdemon'), Js('Archfiend'), Js('Archlord'), Js('Beast'), Js('Befouler'), Js('Defiler'), Js('Demolisher'), Js('Demon'), Js('Demonlord'), Js('Desecrator'), Js('Despoiler'), Js('Destroyer'), Js('Devourer'), Js('Eradicator'), Js('Exterminator'), Js('Fiend'), Js('Harvester'), Js('Hellion'), Js('Herald'), Js('Hunter'), Js('Infernal'), Js('Lord'), Js('Marauder'), Js('Minion'), Js('Monster'), Js('Overlord'), Js('Overseer'), Js('Persecutor'), Js('Perverter'), Js('Pilferer'), Js('Pitlord'), Js('Ravager'), Js('Reaper'), Js('Renegade'), Js('Scourge'), Js('Servant'), Js('Slaughterer'), Js('Spawn'), Js('Stalker'), Js('Taskmaster'), Js('Tyrant'), Js('Violator')]))
var.put('nm9', Js([Js('Abhorrent'), Js('Abyssal'), Js('Aggravated'), Js('Ancient'), Js('Angry'), Js('Anguish'), Js('Anguished'), Js('Bellowing'), Js('Bitter'), Js('Bone'), Js('Bony'), Js('Broken'), Js('Burly'), Js('Cackling'), Js('Chaos'), Js('Colossal'), Js('Corrupt'), Js('Corrupted'), Js('Crooked'), Js('Cruel'), Js('Crypt'), Js('Damned'), Js('Dangerous'), Js('Dark'), Js('Deadly'), Js('Defiant'), Js('Delirious'), Js('Diligent'), Js('Dire'), Js('Disgusting'), Js('Dismal'), Js('Dread'), Js('Dreary'), Js('Enormous'), Js('Enraged'), Js('Evil'), Js('Fallen'), Js('Fearless'), Js('Ferocious'), Js('Filthy'), Js('Forceful'), Js('Forsaken'), Js('Frightening'), Js('Fury'), Js('Gargantuan'), Js('Gleeful'), Js('Grand'), Js('Grave'), Js('Greedy'), Js('Grim'), Js('Grinning'), Js('Gross'), Js('Grotesque'), Js('Gruesome'), Js('Haunting'), Js('Havoc'), Js('Heavy'), Js('Hollow'), Js('Horrible'), Js('Hungry'), Js('Indulgent'), Js('Infernal'), Js('Jaded'), Js('Jagged'), Js('Laughing'), Js('Lumbering'), Js('Mad'), Js('Mindless'), Js('Miserable'), Js('Misery'), Js('Monstrous'), Js('Noxious'), Js('Outlandish'), Js('Perverted'), Js('Powerful'), Js('Prime'), Js('Rage'), Js('Reckless'), Js('Renegade'), Js('Repulsive'), Js('Skeletal'), Js('Stark'), Js('Thunderous'), Js('Tomb'), Js('Torment'), Js('Tormented'), Js('Twilight'), Js('Twin'), Js('Vengeful'), Js('Vicious'), Js('Villainous'), Js('Violent'), Js('Wicked'), Js('Wild'), Js('Winged'), Js('Wrathful'), Js('Wretched')]))
pass
pass


# Add lib to the module scope
mgtDemons = var.to_python()