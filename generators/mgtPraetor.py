__all__ = ['mgtPraetor']

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
            if (var.get('i')<Js(6.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm5').get(var.get('rnd3'))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    var.put('lName', ((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3'))))
                else:
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd4')),var.get('nm5').get(var.get('rnd3'))):
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('lName', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd3'))))
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm5').get(var.get('rnd3'))):
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                if (var.get('i')<Js(3.0)):
                    var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+Js(' '))+var.get('lName')))
                else:
                    var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd4')),var.get('nm5').get(var.get('rnd3'))):
                        var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd3')))+Js(' '))+var.get('lName')))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm6').get(var.get('rnd'))+Js(' '))+var.get('nm7').get(var.get('rnd2'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm8').get(var.get('rnd'))+Js(' of '))+var.get('nm9').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('ch'), Js('d'), Js('g'), Js('j'), Js('k'), Js('kh'), Js('n'), Js('ph'), Js('q'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('eo'), Js('ia'), Js('io'), Js('ea')]))
var.put('nm3', Js([Js('d'), Js('dr'), Js('dd'), Js('g'), Js('gn'), Js('gr'), Js('gl'), Js('k'), Js('kk'), Js('kl'), Js('kn'), Js('kr'), Js('l'), Js('ll'), Js('lgl'), Js('gr'), Js('ld'), Js('ln'), Js('lr'), Js('lv'), Js('lz'), Js('lq'), Js('lqr'), Js('ldr'), Js('n'), Js('nn'), Js('nq'), Js('nqr'), Js('ng'), Js('ngr'), Js('nd'), Js('ndr'), Js('nz'), Js('nv'), Js('nl'), Js('q'), Js('qq'), Js('qr'), Js('ql'), Js('qn'), Js('r'), Js('rk'), Js('rl'), Js('rn'), Js('rv'), Js('rz'), Js('rr'), Js('rqr'), Js('rdr'), Js('rl'), Js('sh'), Js('str'), Js('sc'), Js('scl'), Js('skr'), Js('sk'), Js('t'), Js('th'), Js('tr'), Js('thr'), Js('v')]))
var.put('nm4', Js([Js('d'), Js('g'), Js('gg'), Js('k'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('q'), Js('r'), Js('rr'), Js('sh'), Js('t'), Js('tt'), Js('v'), Js('z')]))
var.put('nm5', Js([Js('d'), Js('g'), Js('k'), Js('ks'), Js('n'), Js('nd'), Js('q'), Js('rn'), Js('s'), Js('sh'), Js('sk'), Js('x'), Js('z')]))
var.put('nm6', Js([Js('Adept'), Js('Aged'), Js('Ancient'), Js('Banished'), Js('Barbed'), Js('Barrage'), Js('Bitter'), Js('Blazing'), Js('Blind'), Js('Bold'), Js('Bony'), Js('Bright'), Js('Broken'), Js('Cackling'), Js('Careless'), Js('Chaos'), Js('Cinder'), Js('Colossal'), Js('Core'), Js('Corrupt'), Js('Corrupted'), Js('Crimson'), Js('Crooked'), Js('Cruel'), Js('Crystal'), Js('Dark'), Js('Deaf'), Js('Delirious'), Js('Deserted'), Js('Ebon'), Js('Ember'), Js('Eternal'), Js('Fallen'), Js('Fearless'), Js('Feisty'), Js('Fickle'), Js('Fiery'), Js('Flame'), Js('Forge'), Js('Forked'), Js('Forsaken'), Js('Frost'), Js('Gargantuan'), Js('Grand'), Js('Grave'), Js('Grim'), Js('Grinning'), Js('Growing'), Js('Gruesome'), Js('Haunting'), Js('Haze'), Js('Hidden'), Js('Hollow'), Js('Hungering'), Js('Hungry'), Js('Idle'), Js('Infernal'), Js('Jaded'), Js('Jagged'), Js('Juvenile'), Js('Laughing'), Js('Lone'), Js('Lost'), Js('Mammoth'), Js('Mute'), Js('Nether'), Js('Noxious'), Js('Obsidian'), Js('Powerful'), Js('Primal'), Js('Prime'), Js('Pyre'), Js('Radiant'), Js('Ragged'), Js('Rash'), Js('Reckless'), Js('Sanguine'), Js('Scornful'), Js('Shade'), Js('Shadow'), Js('Shallow'), Js('Silent'), Js('Smiling'), Js('Smirking'), Js('Stark'), Js('Swift'), Js('Thunderous'), Js('Titan'), Js('Torn'), Js('Twilight'), Js('Twin'), Js('Tyrant'), Js('Unknown'), Js('Vain'), Js('Vengeful'), Js('Vicious'), Js('Villainous'), Js('Vile'), Js('Warped'), Js('Whispering'), Js('Wicked'), Js('Woeful'), Js('Wrathful'), Js('Wretched'), Js('Writhing')]))
var.put('nm7', Js([Js('Annihilator'), Js('Augur'), Js('Befouler'), Js('Being'), Js('Brute'), Js('Cenobite'), Js('Creature'), Js('Degenerate'), Js('Demolisher'), Js('Desecrator'), Js('Despoiler'), Js('Destroyer'), Js('Diviner'), Js('Fiend'), Js('Harbinger'), Js('Harvester'), Js('Herald'), Js('Infernal'), Js('Keeper'), Js('Marauder'), Js('Minion'), Js('Monster'), Js('Oracle'), Js('Overlord'), Js('Overseer'), Js('Persecutor'), Js('Praetor'), Js('Ravager'), Js('Reaper'), Js('Renegade'), Js('Savage'), Js('Scourge'), Js('Seer'), Js('Sentinel'), Js('Sentry'), Js('Soothsayer'), Js('Taskmaster'), Js('Tyrant'), Js('Warden')]))
var.put('nm8', Js([Js('Being'), Js('Brute'), Js('Creature'), Js('Fiend'), Js('Herald'), Js('Keeper'), Js('Minion'), Js('Overlord'), Js('Overseer'), Js('Praetor'), Js('Reaper'), Js('Renegade'), Js('Scourge'), Js('Seer'), Js('Tyrant'), Js('Voice'), Js('Warden')]))
var.put('nm9', Js([Js('Acrimony'), Js('Agony'), Js('Anger'), Js('Anguish'), Js('Annihilation'), Js('Anxiety'), Js('Blood'), Js('Bones'), Js('Calamity'), Js('Catastrophe'), Js('Chaos'), Js('Darkness'), Js('Death'), Js('Desolation'), Js('Despair'), Js('Destruction'), Js('Ember'), Js('Extinction'), Js('Fire'), Js('Flame'), Js('Frenzy'), Js('Furor'), Js('Fury'), Js('Gloom'), Js('Grief'), Js('Hate'), Js('Hatred'), Js('Hunger'), Js('Hysteria'), Js('Ire'), Js('Isolation'), Js('Loss'), Js('Mania'), Js('Melancholy'), Js('Misery'), Js('Misfortune'), Js('Nightmares'), Js('Obsidian'), Js('Onyx'), Js('Pain'), Js('Perdition'), Js('Pestilence'), Js('Pride'), Js('Regret'), Js('Rue'), Js('Ruin'), Js('Ruins'), Js('Shadows'), Js('Silence'), Js('Solitude'), Js('Sorrow'), Js('Thunder'), Js('Tragedy'), Js('Twilight'), Js('Umbrage'), Js('Vengeance'), Js('Venom'), Js('Woe')]))
pass
pass


# Add lib to the module scope
mgtPraetor = var.to_python()