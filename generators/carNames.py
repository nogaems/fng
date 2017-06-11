__all__ = ['carNames']

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
var.put('nm1', Js([Js('Blast'), Js('Hollo'), Js('Wolf'), Js('Fang'), Js('Eagle'), Js('Blade'), Js('Adventure'), Js('Aeon'), Js('Alabaster'), Js('Albatross'), Js('Apex'), Js('Astral'), Js('Augury'), Js('Aura'), Js('Aurora'), Js('Avalanche'), Js('Baron'), Js('Barrage'), Js('Basilisk'), Js('Behemoth'), Js('Blaze'), Js('Blend'), Js('Bliss'), Js('Blitz'), Js('Blizzard'), Js('Bolt'), Js('Buffalo'), Js('Bullet'), Js('Capital'), Js('Catalyst'), Js('Celestial'), Js('Centaur'), Js('Centurion'), Js('Charm'), Js('Chase'), Js('Climax'), Js('Cobra'), Js('Conqueror'), Js('Corsair'), Js('Cosmos'), Js('Crest'), Js('Crown'), Js('Crusader'), Js('Crux'), Js('Curiosity'), Js('Dawn'), Js('Daydream'), Js('Deputy'), Js('Desire'), Js('Dominion'), Js('Dragon'), Js('Dusk'), Js('Dynamics'), Js('Dynamo'), Js('Elysium'), Js('Eminance'), Js('Empire'), Js('Empyrean'), Js('Encounter'), Js('Enigma'), Js('Eon'), Js('Eos'), Js('Epiphany'), Js('Epitome'), Js('Escape'), Js('Essence'), Js('Eternity'), Js('Ethereal'), Js('Evolution'), Js('Excursion'), Js('Expedition'), Js('Falcon'), Js('Ferocity'), Js('Fire'), Js('Flow'), Js('Flux'), Js('Formula'), Js('Fragment'), Js('Freedom'), Js('Gallop'), Js('Grit'), Js('Guardian'), Js('Guerilla'), Js('Harmony'), Js('Heirloom'), Js('Hero'), Js('Hydra'), Js('Icon'), Js('Inception'), Js('Inferno'), Js('Inquiry'), Js('Instinct'), Js('Intro'), Js('Ivory'), Js('Jazz'), Js('Legacy'), Js('Legend'), Js('Liberty'), Js('Lightning'), Js('Lioness'), Js('Magic'), Js('Majesty'), Js('Mammoth'), Js('Marvel'), Js('Mastery'), Js('Meridian'), Js('Method'), Js('Might'), Js('Millenium'), Js('Mirage'), Js('Momentum'), Js('Moonlight'), Js('Morale'), Js('Motion'), Js('Motive'), Js('Mystery'), Js('Mythic'), Js('Nebula'), Js('Nimbus'), Js('Obsidian'), Js('Olympian'), Js('Onyx'), Js('Oracle'), Js('Orbit'), Js('Origin'), Js('Paladin'), Js('Paradox'), Js('Paragon'), Js('Parallel'), Js('Passion'), Js('Patron'), Js('Phantom'), Js('Phenomenom'), Js('Pinnacle'), Js('Portrait'), Js('Presence'), Js('Prestige'), Js('Prime'), Js('Prodigy'), Js('Prophecy'), Js('Prospect'), Js('Pulse'), Js('Purity'), Js('Pyre'), Js('Quest'), Js('Quicksilver'), Js('Radiance'), Js('Ranger'), Js('Raven'), Js('Reach'), Js('Realm'), Js('Reflect'), Js('Renegade'), Js('Resolve'), Js('Revelation'), Js('Roamer'), Js('Rune'), Js('Sanctuary'), Js('Scorpion'), Js('Scout'), Js('Serpent'), Js('Shadow'), Js('Silver'), Js('Sliver'), Js('Specter'), Js('Spire'), Js('Spirit'), Js('Spotlight'), Js('Sprite'), Js('Stardust'), Js('Starlight'), Js('Storm'), Js('Striker'), Js('Supremacy'), Js('Surge'), Js('Symbol'), Js('Tarragon'), Js('Temper'), Js('Temperament'), Js('Tempest'), Js('Thriller'), Js('Thunder'), Js('Tigress'), Js('Titan'), Js('Tracer'), Js('Tradition'), Js('Trailblazer'), Js('Treasure'), Js('Triumph'), Js('Twister'), Js('Umbra'), Js('Union'), Js('Universe'), Js('Utopia'), Js('Vagabond'), Js('Vanish'), Js('Vertex'), Js('Vigor'), Js('Vindicator'), Js('Viper'), Js('Virtue'), Js('Vision'), Js('Vortex'), Js('Voyage'), Js('Vulture'), Js('Warrior'), Js('Whim'), Js('Whirlpool'), Js('Wish'), Js('Zeal')]))
pass
pass


# Add lib to the module scope
carNames = var.to_python()