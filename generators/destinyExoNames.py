__all__ = ['destinyExoNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('Ashes'), Js('Ace'), Js('Anarchy'), Js('Anger'), Js('Apparition'), Js('Arch'), Js('Ash'), Js('Aura'), Js('Band'), Js('Bandit'), Js('Banshee'), Js('Barbarian'), Js('Barrage'), Js('Beam'), Js('Beast'), Js('Behemoth'), Js('Bite'), Js('Blade'), Js('Blaze'), Js('Blight'), Js('Blow'), Js('Bolt'), Js('Bones'), Js('Boulder'), Js('Brass'), Js('Brute'), Js('Burn'), Js('Cast'), Js('Cavalier'), Js('Chain'), Js('Champ'), Js('Chance'), Js('Chaos'), Js('Cherub'), Js('Cloud'), Js('Crack'), Js('Critter'), Js('Crook'), Js('Crow'), Js('Crux'), Js('Daemon'), Js('Death'), Js('Demon'), Js('Design'), Js('Desire'), Js('Devil'), Js('Diablo'), Js('Dice'), Js('Dragon'), Js('Dragonfly'), Js('Dusk'), Js('Dust'), Js('Echo'), Js('Eclipse'), Js('Edge'), Js('End'), Js('Enigma'), Js('Fang'), Js('Fiend'), Js('Fire'), Js('Flame'), Js('Flint'), Js('Flow'), Js('Flux'), Js('Force'), Js('Fragment'), Js('Freak'), Js('Frost'), Js('Fury'), Js('Fuse'), Js('Gargoyle'), Js('Gem'), Js('Ghost'), Js('Giant'), Js('Glutton'), Js('Goliath'), Js('Grim'), Js('Guide'), Js('Hazard'), Js('Heart'), Js('Hellion'), Js('Hook'), Js('Horn'), Js('Horror'), Js('Hound'), Js('Ice'), Js('Imp'), Js('Impulse'), Js('Iron'), Js('Jackal'), Js('Jester'), Js('Jewel'), Js('Judge'), Js('Knife'), Js('Knight'), Js('Leviathan'), Js('Limbo'), Js('Mammoth'), Js('Maniac'), Js('Martyr'), Js('Mask'), Js('Merit'), Js('Mime'), Js('Mind'), Js('Mist'), Js('Monster'), Js('Motion'), Js('Myth'), Js('Naught'), Js('Needle'), Js('Night'), Js('Ogre'), Js('Omen'), Js('Oracle'), Js('Owl'), Js('Paladin'), Js('Paradox'), Js('Paragon'), Js('Pest'), Js('Phantom'), Js('Phoenix'), Js('Plasma'), Js('Purpose'), Js('Pyre'), Js('Quake'), Js('Quiver'), Js('Rain'), Js('Rat'), Js('Ray'), Js('Revenant'), Js('Riddle'), Js('Rime'), Js('Robin'), Js('Rogue'), Js('Ruse'), Js('Saint'), Js('Salt'), Js('Sand'), Js('Savage'), Js('Scale'), Js('Scout'), Js('Secret'), Js('Sentinel'), Js('Seraph'), Js('Serenity'), Js('Serpent'), Js('Shade'), Js('Shadow'), Js('Shift'), Js('Shock'), Js('Shockwave'), Js('Silver'), Js('Siren'), Js('Sky'), Js('Slip'), Js('Slither'), Js('Sliver'), Js('Sly'), Js('Snake'), Js('Snow'), Js('Song'), Js('Soul'), Js('Specter'), Js('Sphinx'), Js('Spider'), Js('Splinter'), Js('Sprite'), Js('Steel'), Js('Stitch'), Js('Storm'), Js('Summer'), Js('Surprise'), Js('Switch'), Js('Taint'), Js('Temper'), Js('Templar'), Js('Thunder'), Js('Titan'), Js('Toad'), Js('Touch'), Js('Trick'), Js('Twist'), Js('Umbra'), Js('Vamp'), Js('Varmint'), Js('Veil'), Js('Vermin'), Js('Villain'), Js('Viper'), Js('Virtue'), Js('Vision'), Js('Void'), Js('Vortex'), Js('Wave'), Js('Weasel'), Js('Whip'), Js('Whisper'), Js('Winter'), Js('Wraith'), Js('Zealot')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*Js(50.0))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js('-'))+var.get('rnd2')))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
destinyExoNames = var.to_python()