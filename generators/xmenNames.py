__all__ = ['xmenNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
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
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Matter Master'), Js('Skye'), Js('Conjurer'), Js('Invincible'), Js('Shift'), Js('Telescope'), Js('Wormhole'), Js('Reptile'), Js('Insect'), Js('Bullet'), Js('Venus'), Js('Puma'), Js('Lunar'), Js('Wireless'), Js('Vaccine'), Js('Perception'), Js('Springboard'), Js('Eclipse'), Js('Demon'), Js('Siren'), Js('Steelskin'), Js('Ace'), Js('Anarchy'), Js('Ape'), Js('Arachnid'), Js('Ash'), Js('Ashes'), Js('Augury'), Js('Aura'), Js('Bandit'), Js('Barrage'), Js('Bearpaw'), Js('Behemoth'), Js('Blaze'), Js('Blight'), Js('Blizzard'), Js('Bolt'), Js('Bones'), Js('Boulder'), Js('Brute'), Js('Bubble'), Js('Chaos'), Js('Chronos'), Js('Clairity'), Js('Clone'), Js('Cloud'), Js('Creature'), Js('Cryptic'), Js('Crystal'), Js('Daydream'), Js('Decay'), Js('Demon'), Js('Dice'), Js('Discharge'), Js('Disperse'), Js('Dragonfly'), Js('Dynamo'), Js('Echo'), Js('Electrode'), Js('Enigma'), Js('Fallout'), Js('Fangs'), Js('Feline'), Js('Fiend'), Js('Flint'), Js('Flow'), Js('Flux'), Js('Frost'), Js('Fury'), Js('Fuse'), Js('Gamble'), Js('Gargoyle'), Js('Ghost'), Js('Gimmick'), Js('Glutton'), Js('Granite'), Js('Grimm'), Js('Hazard'), Js('Hue'), Js('Hypnotic'), Js('Inferno'), Js('Infinity'), Js('Jackal'), Js('Jester'), Js('Katana'), Js('Knightmare'), Js('Light'), Js('Liquid'), Js('Luna'), Js('Lupine'), Js('Lupus'), Js('Mammoth'), Js('Mist'), Js('Mouse'), Js('Myth'), Js('Naught'), Js('Nightmare'), Js('Nightowl'), Js('Nightshade'), Js('Noise'), Js('Ogre'), Js('Omen'), Js('Onesize'), Js('Ooze'), Js('Optic'), Js('Oracle'), Js('Paladin'), Js('Pandemonium'), Js('Paradox'), Js('Particle'), Js('Pebble'), Js('Phonic'), Js('Phonix'), Js('Physique'), Js('Pipsqueak'), Js('Plague'), Js('Plasma'), Js('Pygmy'), Js('Pyre'), Js('Quake'), Js('Rime'), Js('Ruse'), Js('Savage'), Js('Scepter'), Js('Scout'), Js('Scramble'), Js('Seismic'), Js('Sentinel'), Js('Serenity'), Js('Serpent'), Js('Shade'), Js('Shadow'), Js('Shockwave'), Js('Sight'), Js('Siphon'), Js('Siren'), Js('Slither'), Js('Sliver'), Js('Sly'), Js('Snake'), Js('Snowflake'), Js('Solaris'), Js('Spark'), Js('Splinter'), Js('Stardust'), Js('Steel'), Js('Stretch'), Js('Swine'), Js('Switch'), Js('Thunder'), Js('Timber'), Js('Timeles'), Js('Tranquillity'), Js('Twin'), Js('Valkyrie'), Js('Vapor'), Js('Vermin'), Js('Viper'), Js('Virtue'), Js('Void'), Js('Vortex'), Js('Weasel'), Js('Whisper'), Js('Wisp'), Js('X-Ray'), Js('Yce')]))
pass
pass


# Add lib to the module scope
xmenNames = var.to_python()