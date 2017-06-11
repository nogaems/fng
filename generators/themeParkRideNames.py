__all__ = ['themeParkRideNames']

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
    var.registers(['nm1', 'nm4', 'nm5', 'nm3', 'nm2', 'result'])
    var.put('nm1', Js([Js('Abyss'), Js('Adventure'), Js('Aftermath'), Js('Ambition'), Js('Angel'), Js('Apparatus'), Js('Arachnid'), Js('Arch'), Js('Balance'), Js('Balloon'), Js('Baron'), Js('Basin'), Js('Loophole'), Js('Expedition'), Js('Battle'), Js('Beast'), Js('Beauty'), Js('Blade'), Js('Bluff'), Js('Bomb'), Js('Bomber'), Js('Boost'), Js('Boulder'), Js('Brass'), Js('Brass Knuckle'), Js('Bridge'), Js('Brutality'), Js('Bullet'), Js('Candle'), Js('Cannon'), Js('Canyon'), Js('Chain'), Js('Chaos'), Js('Chasm'), Js('Chimera'), Js('Cliffhanger'), Js('Comet'), Js('Commando'), Js('Condor'), Js('Cork'), Js('Count'), Js('Courage'), Js('Crook'), Js('Cross'), Js('Crown'), Js('Curse'), Js('Curtain'), Js('Curve'), Js('Daemon'), Js('Death'), Js('Delight'), Js('Demon'), Js('Desire'), Js('Devil'), Js('Diamond'), Js('Dimension'), Js('Diver'), Js('Divide'), Js('Division'), Js('Dread'), Js('Dream'), Js('Dreamscape'), Js('Earthquake'), Js('Enchantment'), Js('Enigma'), Js('Eruption'), Js('Escape'), Js('Eternity'), Js('Eventide'), Js('Evolution'), Js('Explosion'), Js('Extreme'), Js('Fall'), Js('Feather'), Js('Figure'), Js('Fire'), Js('Fireball'), Js('Flake'), Js('Flame'), Js('Flight'), Js('Flock'), Js('Fluke'), Js('Flux'), Js('Fog'), Js('Force'), Js('Fortune'), Js('Freedom'), Js('Garden'), Js('Ghost'), Js('Glass'), Js('Glutton'), Js('Gravity'), Js('Heart'), Js('Heartbeat'), Js('Hook'), Js('Horror'), Js('Hurricane'), Js('Icicle'), Js('Impulse'), Js('Island'), Js('Jewel'), Js('Judgment'), Js('Justice'), Js('Knockout'), Js('Kraken'), Js('Leopard'), Js('Mammoth'), Js('Medium'), Js('Meteor'), Js('Miracle'), Js('Mirror'), Js('Mist'), Js('Motion'), Js('Night'), Js('Nightmare'), Js('Octopus'), Js('Omen'), Js('Operation'), Js('Oracle'), Js('Panther'), Js('Phantom'), Js('Phase'), Js('Prison'), Js('Pulse'), Js('Punishment'), Js('Quake'), Js('Quicksand'), Js('Quill'), Js('Reflection'), Js('Regret'), Js('Requiem'), Js('Response'), Js('Rhythm'), Js('Riddle'), Js('Ride'), Js('River'), Js('Ruin'), Js('Serpent'), Js('Servant'), Js('Shade'), Js('Shadow'), Js('Shift'), Js('Shock'), Js('Signal'), Js('Snake'), Js('Snowflake'), Js('Sparkle'), Js('Spell'), Js('Split'), Js('Star'), Js('Stitch'), Js('Storm'), Js('Switch'), Js('Switcheroo'), Js('Thrill'), Js('Throne'), Js('Thunder'), Js('Tornado'), Js('Tower'), Js('Tremor'), Js('Trick'), Js('Twist'), Js('Twister'), Js('Typhoon'), Js('Vault'), Js('Volcano'), Js('Voyage'), Js('Wave'), Js('Wipeout'), Js('Wonder'), Js('Zephyr')]))
    var.put('nm2', Js([Js('Boat'), Js('Bungee'), Js('Coaster'), Js('Coil'), Js('Depth'), Js('Diver'), Js('Drop'), Js('Edge'), Js('Expedition'), Js('Extreme'), Js('House'), Js('Hall'), Js('Loop'), Js('Manor'), Js('Mansion'), Js('Obelisk'), Js('Palace'), Js('Pass'), Js('Passage'), Js('Pendulum'), Js('Place'), Js('Plummet'), Js('Plunge'), Js('Rapids'), Js('Release'), Js('Ride'), Js('Rider'), Js('Shot'), Js('Slide'), Js('Spire'), Js('Supreme'), Js('Swing'), Js('Tower'), Js('Tumble'), Js('Wheel')]))
    var.put('nm3', Js([Js('Acrobatics'), Js('Action'), Js('Adventure'), Js('Amazement'), Js('Autumn'), Js('Awe'), Js('Balance'), Js('Battle'), Js('Beginnings'), Js('Belief'), Js('Blood'), Js('Bones'), Js('Bravery'), Js('Bubbles'), Js('Candy'), Js('Chains'), Js('Chaos'), Js('Clarity'), Js('Clouds'), Js('Courage'), Js('Creatures'), Js('Cushions'), Js('Dance'), Js('Darkness'), Js('Death'), Js('Delight'), Js('Desire'), Js('Discovery'), Js('Doom'), Js('Dread'), Js('Dreams'), Js('Ecstacy'), Js('Eternity'), Js('Fascination'), Js('Fear'), Js('Feasts'), Js('Fire'), Js('Flame'), Js('Flukes'), Js('Fortune'), Js('Fun'), Js('Ghosts'), Js('Glass'), Js('Gluttony'), Js('Gold'), Js('Harmony'), Js('Hilarity'), Js('Horror'), Js('Ice'), Js('Impulses'), Js('Insanity'), Js('Insects'), Js('Jelly'), Js('Jokes'), Js('Juniors'), Js('Laughter'), Js('Liberty'), Js('Light'), Js('Liquid'), Js('Luck'), Js('Magic'), Js('Masks'), Js('Mayhem'), Js('Midnight'), Js('Mirrors'), Js('Motion'), Js('Nightmares'), Js('Paradise'), Js('Pillows'), Js('Pleasure'), Js('Quicksand'), Js('Rain'), Js('Reflections'), Js('Rhythm'), Js('Riddles'), Js('Scents'), Js('Science'), Js('Secrets'), Js('Shadows'), Js('Silliness'), Js('Silly'), Js('Smiles'), Js('Snow'), Js('Sparks'), Js('Speed'), Js('Spells'), Js('Spirits'), Js('Spring'), Js('Stars'), Js('Storms'), Js('Strings'), Js('Sugar'), Js('Summer'), Js('Surprises'), Js('Terror'), Js('Thrills'), Js('Thunder'), Js('Tunes'), Js('Twists'), Js('Uncertainty'), Js('Voices'), Js('Water'), Js('Webs'), Js('Whispers'), Js('Winter'), Js('Wishes'), Js('Wonders')]))
    var.put('nm4', Js([Js('Abandoned'), Js('Abstract'), Js('Ancient'), Js('Bizarre'), Js('Blind'), Js('Broken'), Js('Charmed'), Js('Colossal'), Js('Daffy'), Js('Dark'), Js('Defiant'), Js('Demonic'), Js('Dynamic'), Js('Enchanted'), Js('Enchanting'), Js('Ethereal'), Js('Euphoric'), Js('Forsaken'), Js('Frozen'), Js('Grand'), Js('Grave'), Js('Grim'), Js('Hollow'), Js('Horrific'), Js('Hungry'), Js('Jumbo'), Js('Living'), Js('Lone'), Js('Lonely'), Js('Merciless'), Js('Merry'), Js('Monster'), Js('Monstrous')]))
    var.put('nm5', Js([Js('The '), Js('')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
            if (var.get('i')<Js(2.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('names', (((var.get('nm5').get(var.get('rnd3'))+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                if (var.get('i')<Js(4.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                    var.put('names', (Js('The ')+var.get('nm1').get(var.get('rnd'))))
                    var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('names', (((Js('The ')+var.get('nm4').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                        var.get('nm4').callprop('splice', var.get('rnd'), Js(1.0))
                    else:
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm2').get(var.get('rnd2'))+Js(' of '))+var.get('nm3').get(var.get('rnd'))))
                        var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
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
themeParkRideNames = var.to_python()