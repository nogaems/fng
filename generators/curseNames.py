__all__ = ['curseNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((var.get('nm3').get(var.get('rnd2'))+Js(' of '))+var.get('nm1').get(var.get('rnd'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd2')),var.get('nm2').get(var.get('rnd'))):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm2').get(var.get('rnd')))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Acrimony'), Js('Agony'), Js('Amber'), Js('Anger'), Js('Anguish'), Js('Annihilation'), Js('Anxiety'), Js('Ash'), Js('Asperity'), Js('Assault'), Js('Atonement'), Js('Bane'), Js('Blood'), Js('Bone'), Js('Bones'), Js('Brass'), Js('Catastrophe'), Js('Chains'), Js('Chaos'), Js('Coal'), Js('Crimson'), Js('Crystal'), Js('Darkness'), Js('Dawn'), Js('Death'), Js('Defeat'), Js('Depletion'), Js('Desire'), Js('Desolation'), Js('Despair'), Js('Destruction'), Js('Doom'), Js('Dusk'), Js('Dust'), Js('Earth'), Js('Ember'), Js('Exctinction'), Js('Failure'), Js('Fire'), Js('Flame'), Js('Flesh'), Js('Flies'), Js('Frenzy'), Js('Frost'), Js('Furor'), Js('Fury'), Js('Glass'), Js('Gold'), Js('Grief'), Js('Growth'), Js('Hate'), Js('Hatred'), Js('Heartache'), Js('Horns'), Js('Hysteria'), Js('Ice'), Js('Imbalance'), Js('Ire'), Js('Iron'), Js('Isolation'), Js('Lava'), Js('Lead'), Js('Light'), Js('Loss'), Js('Love'), Js('Mania'), Js('Marble'), Js('Metal'), Js('Misery'), Js('Misfortune'), Js('Nightmares'), Js('Obsidian'), Js('Onyx'), Js('Pain'), Js('Passion'), Js('Penance'), Js('Perdition'), Js('Pests'), Js('Poison'), Js('Poverty'), Js('Pride'), Js('Prison'), Js('Rage'), Js('Rain'), Js('Rats'), Js('Ruin'), Js('Runes'), Js('Sacrifice'), Js('Sand'), Js('Scales'), Js('Scents'), Js('Seclusion'), Js('Shadows'), Js('Silence'), Js('Silk'), Js('Silver'), Js('Smiles'), Js('Smoke'), Js('Snow'), Js('Solitude'), Js('Sorrow'), Js('Spasms'), Js('Stone'), Js('Storms'), Js('Teeth'), Js('Thunder'), Js('Truth'), Js('Twilight'), Js('Umbrage'), Js('Vengeance'), Js('Venom'), Js('Vermin'), Js('Woe'), Js('Wrath'), Js('the Arachnid'), Js('the Banshee'), Js('the Bat'), Js('the Blaze'), Js('the Boulder'), Js('the Cave'), Js('the Crow'), Js('the Crown'), Js('the Crypt'), Js('the Dark'), Js('the Dead'), Js('the Dragon'), Js('the Feast'), Js('the Fire'), Js('the Flame'), Js('the Flock'), Js('the Fog'), Js('the Forge'), Js('the Grave'), Js('the Griffin'), Js('the Hallowed'), Js('the Heart'), Js('the Horn'), Js('the Hydra'), Js('the Lone Wolf'), Js('the Lonely'), Js('the Mind'), Js('the Mist'), Js('the Moon'), Js('the Nightmare'), Js('the Phoenix'), Js('the Prison'), Js('the Quill'), Js('the Rat'), Js('the Reaper'), Js('the Ring'), Js('the Ruins'), Js('the Sanguine'), Js('the Seed'), Js('the Serpent'), Js('the Shade'), Js('the Shadows'), Js('the Snail'), Js('the Storm'), Js('the Stranger'), Js('the Sun'), Js('the Talon'), Js('the Titan'), Js('the Tomb'), Js('the Tyrant'), Js('the Veil'), Js('the Vermin'), Js('the Vessel'), Js('the Visitor'), Js('the Voice'), Js('the Void'), Js('the Wild'), Js('the Wraith'), Js('the Wreckage'), Js('the Wyvern'), Js('the Zephyr')]))
var.put('nm2', Js([Js('Acrimony'), Js('Aggression'), Js('Agony'), Js('Ancient'), Js('Angel'), Js('Anguish'), Js('Anxiety'), Js('Arachnid'), Js('Avian'), Js('Banshee'), Js('Bat'), Js('Blaze'), Js('Boulder'), Js('Brass'), Js('Canine'), Js('Chaos'), Js('Cold'), Js('Crazy'), Js('Creeper'), Js('Creeping'), Js('Crimson'), Js('Crippling'), Js('Crow'), Js('Crown'), Js('Crumbling'), Js('Crying'), Js('Crypt'), Js('Crystal'), Js('Dark'), Js('Deathbell'), Js('Delirium'), Js('Demon'), Js('Desolation'), Js('Devil'), Js('Dragon'), Js('Dread'), Js('Elephant'), Js('Ember'), Js('Ethereal'), Js('Fickle'), Js('Flock'), Js('Flying'), Js('Fog'), Js('Forbidden'), Js('Forest'), Js('Forge'), Js('Frenzy'), Js('Frost'), Js('Frozen'), Js('Furor'), Js('Fury'), Js('Ghast'), Js('Ghastly'), Js('Ghost'), Js('Grave'), Js('Harpy'), Js('Heartache'), Js('Hell'), Js('Hellish'), Js('Hopeless'), Js('Horn'), Js('Horror'), Js('Hydra'), Js('Hyper'), Js('Hysteria'), Js('Ice'), Js('Immobile'), Js('Impossible'), Js('Ire'), Js('Iron'), Js('Ironbark'), Js('Laughing'), Js('Lifeless'), Js('Limp'), Js('Limp Limb'), Js('Mania'), Js('Mind'), Js('Misery'), Js('Misfortune'), Js('Moon'), Js('Mortal'), Js('Necro'), Js('Nercrotic'), Js('Nightmare'), Js('Numb'), Js('Paralyzing'), Js('Penance'), Js('Perdition'), Js('Phantom'), Js('Pharaoh'), Js('Pygmy'), Js('Rabid'), Js('Restless'), Js('Rodent'), Js('Rotting'), Js('Scale'), Js('Seclusion'), Js('Serpent'), Js('Shadow'), Js('Shaking'), Js('Shivering'), Js('Silence'), Js('Silent'), Js('Sinister'), Js('Smiling'), Js('Spirit'), Js('Stiffening'), Js('Stoneskin'), Js('Storm'), Js('Strange'), Js('Stranger'), Js('Sun'), Js('Swamp'), Js('Terror'), Js('Thorn'), Js('Thunder'), Js('Tomb'), Js('Twilight'), Js('Undead'), Js('Vengeance'), Js('Venom'), Js('Volatile'), Js('Wandering'), Js('Wicked'), Js('Wraith'), Js('Zombie')]))
var.put('nm3', Js([Js('Curse'), Js('Bane'), Js('Jinx'), Js('Hex'), Js('Vex'), Js('Cure'), Js('Curse'), Js('Curse'), Js('Curse'), Js('Curse'), Js('Curse')]))
pass
pass


# Add lib to the module scope
curseNames = var.to_python()