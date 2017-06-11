__all__ = ['mgtEldrazi']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('lName', ((var.get('nm6').get(var.get('rnd'))+Js(' '))+var.get('nm7').get(var.get('rnd2'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('lName', ((var.get('nm7').get(var.get('rnd'))+Js(' of '))+var.get('nm8').get(var.get('rnd2'))))
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5'))):
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                if (var.get('i')<Js(3.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('lName')))
                else:
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm5').get(var.get('rnd5'))):
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('lName')))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm6').get(var.get('rnd'))+Js(' '))+var.get('nm7').get(var.get('rnd2'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm7').get(var.get('rnd'))+Js(' of '))+var.get('nm8').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('m'), Js('n'), Js('r'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('j'), Js('k'), Js('l'), Js('lm'), Js('ln'), Js('lr'), Js('ll'), Js('ld'), Js('m'), Js('mr'), Js('ml'), Js('mk'), Js('mr'), Js('md'), Js('mm'), Js('mn'), Js('n'), Js('ng'), Js('nd'), Js('nl'), Js('nk'), Js('nr'), Js('nn'), Js('rl'), Js('rn'), Js('rm'), Js('rz'), Js('rr'), Js('r'), Js('s'), Js('sl'), Js('sr'), Js('z'), Js('zg'), Js('zr')]))
var.put('nm4', Js([Js('c'), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('t')]))
var.put('nm5', Js([Js('d'), Js('g'), Js('l'), Js('k')]))
var.put('nm6', Js([Js('Abandoned'), Js('Acidic'), Js('Advanced'), Js('Aged'), Js('Aggressive'), Js('Anguished'), Js('Arid'), Js('Barrage'), Js('Bitter'), Js('Bleak'), Js('Blight'), Js('Blind'), Js('Blinding'), Js('Broken'), Js('Brood'), Js('Bulky'), Js('Bumpy'), Js('Careless'), Js('Catacomb'), Js('Chittering'), Js('Colossal'), Js('Corrupt'), Js('Corrupted'), Js('Crypt'), Js('Cryptic'), Js('Culling'), Js('Deaf'), Js('Deathless'), Js('Defiant'), Js('Delirious'), Js('Dimensional'), Js('Disfigured'), Js('Distended'), Js('Dread'), Js('Dreary'), Js('Droopy'), Js('Dust'), Js('Elder'), Js('Endless'), Js('Energetic'), Js('Essence'), Js('Eternal'), Js('Eyeless'), Js('Fathom'), Js('Fibrous'), Js('Fickle'), Js('Forked'), Js('Forsaken'), Js('Fragrant'), Js('Gaseous'), Js('Glistening'), Js('Gloomy'), Js('Glossy'), Js('Grave'), Js('Gravity'), Js('Great'), Js('Grim'), Js('Grubby'), Js('Gruesome'), Js('Haunting'), Js('Havoc'), Js('Hidden'), Js('Hideous'), Js('Hollow'), Js('Howling'), Js('Hungry'), Js('Icky'), Js('Impish'), Js('Incubator'), Js('Juicy'), Js('Lone'), Js('Lumpy'), Js('Matter'), Js('Measly'), Js('Mind'), Js('Mindless'), Js('Mist'), Js('Monstrous'), Js('Murk'), Js('Mushy'), Js('Nest'), Js('Nettle'), Js('Nightmare'), Js('Noxious'), Js('Oblivion'), Js('Pale'), Js('Paltry'), Js('Parched'), Js('Prickly'), Js('Prie'), Js('Pungent'), Js('Puny'), Js('Putrid'), Js('Ragged'), Js('Reckless'), Js('Repulsive'), Js('Robust'), Js('Rotten'), Js('Ruin'), Js('Ruination'), Js('Salvage'), Js('Scrawny'), Js('Silent'), Js('Sinuous'), Js('Sky'), Js('Slaughter'), Js('Sludge'), Js('Smothering'), Js('Squiggly'), Js('Stalking'), Js('Swift'), Js('Thought'), Js('Tide'), Js('Tomb'), Js('Vexing'), Js('Vicious'), Js('Vile'), Js('Violent'), Js('Void'), Js('Warped'), Js('Wicked'), Js('Wrathful'), Js('Wretched'), Js('Writhing')]))
var.put('nm7', Js([Js('Abolisher'), Js('Abomination'), Js('Aggregate'), Js('Attendant'), Js('Bane'), Js('Behemoth'), Js('Breaker'), Js('Butcher'), Js('Carver'), Js('Conduit'), Js('Crawler'), Js('Cruiser'), Js('Crusher'), Js('Defiler'), Js('Depleter'), Js('Despoiler'), Js('Devastator'), Js('Displacer'), Js('Drifter'), Js('Drone'), Js('Eldrazi'), Js('Entangler'), Js('Feeder'), Js('Fiend'), Js('Forerunner'), Js('Grafter'), Js('Gryff'), Js('Harvester'), Js('Hatcher'), Js('Herald'), Js('Herder'), Js('Host'), Js('Hulk'), Js('Hunter'), Js('Immobilizer'), Js('Infiltrator'), Js('Intruder'), Js('Invader'), Js('Lurker'), Js('Marauder'), Js('Maw'), Js('Mimic'), Js('Monitor'), Js('Monster'), Js('Negator'), Js('Oracle'), Js('Pathfinder'), Js('Predator'), Js('Prophet'), Js('Rager'), Js('Raker'), Js('Razer'), Js('Reclaimer'), Js('Redeemer'), Js('Reshaper'), Js('Sage'), Js('Scion'), Js('Scourer'), Js('Scourge'), Js('Scout'), Js('Scuttler'), Js('Seer'), Js('Sentinel'), Js('Shaper'), Js('Shrieker'), Js('Sifter'), Js('Skimmer'), Js('Skitterer'), Js('Smasher'), Js('Sower'), Js('Spawn'), Js('Spawner'), Js('Stalker'), Js('Strangler'), Js('Strider'), Js('Summoner'), Js('Titan'), Js('Twin'), Js('Tyrant'), Js('Walker'), Js('Warden'), Js('Watcher'), Js('Winnower')]))
var.put('nm8', Js([Js('Anarchy'), Js('Armies'), Js('Atrophy'), Js('Barbarism'), Js('Blitz'), Js('Blood'), Js('Bloodbaths'), Js('Bloodshed'), Js('Bones'), Js('Butchery'), Js('Carnage'), Js('Chaos'), Js('Death'), Js('Decay'), Js('Demolition'), Js('Depravity'), Js('Destruction'), Js('Devastation'), Js('Discord'), Js('Dismay'), Js('Dread'), Js('Entropy'), Js('Extermination'), Js('Extinction'), Js('Fear'), Js('Flesh'), Js('Gore'), Js('Havoc'), Js('Horror'), Js('Legions'), Js('Malice'), Js('Massacres'), Js('Nightmares'), Js('Plasma'), Js('Ruin'), Js('Ruination'), Js('Sadism'), Js('Savagery'), Js('Silence'), Js('Sinew'), Js('Skulls'), Js('Slaughter'), Js('Spite'), Js('Subjugation'), Js('Terror'), Js('Torment'), Js('Turmoil'), Js('Venom'), Js('Voids'), Js('Wreckages'), Js('the End'), Js('the Hollow'), Js('the Void'), Js('the Wastes')]))
pass
pass


# Add lib to the module scope
mgtEldrazi = var.to_python()