__all__ = ['stadiumNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Accord'), Js('Adamant'), Js('Aegis'), Js('Aerie'), Js('Affinity'), Js('Alabaster'), Js('Alliance'), Js('Ancestor'), Js('Angel'), Js('Angel Wing'), Js('Animus'), Js('Anniversary'), Js('Anomaly'), Js('Apex'), Js('Arch'), Js('Aria'), Js('Arrowhead'), Js('Aurelian'), Js('Aureole'), Js('Aurora'), Js('Azure'), Js('Bamboo'), Js('Bauble'), Js('Beacon'), Js('Bell'), Js('Bird Nest'), Js('Blessing'), Js('Blossom'), Js('Blue Moon'), Js('Borealis'), Js('Burrow'), Js('Canvas'), Js('Cardinal'), Js('Celebration'), Js('Celestial'), Js('Central'), Js('Century'), Js('Ceremony'), Js('Champion'), Js('Cherub'), Js('Chimera'), Js('Chronicle'), Js('Cinder'), Js('Cipher'), Js('Cloud'), Js('Clover'), Js('Coalition'), Js('Community'), Js('Compass'), Js('Connection'), Js('Conquest'), Js('Convex'), Js('Core'), Js('Corona'), Js('Cosmos'), Js('Courage'), Js('Crescent'), Js('Crimson'), Js('Crown'), Js('Crux'), Js('Crystal'), Js('Curator'), Js('Dawn'), Js('Daydream'), Js('Delight'), Js('Den'), Js('Destination'), Js('Destiny'), Js('Diamond'), Js('Diorama'), Js('Discovery'), Js('Dominion'), Js('Dream'), Js('Ebon'), Js('Echo'), Js('Eclipse'), Js('Element'), Js('Ember'), Js('Emerald'), Js('Enclave'), Js('Eos'), Js('Epiphany'), Js('Epitome'), Js('Epoch'), Js('Essence'), Js('Eternity'), Js('Euphony'), Js('Exhibition'), Js('Expedition'), Js('Expo'), Js('Faith'), Js('Fate'), Js('Floret'), Js('Fortune'), Js('Founders'), Js('Fragment'), Js('Full Moon'), Js('Fusion'), Js('Galaxy'), Js('Gateway'), Js('Gemstone'), Js('Genie'), Js('Gilded'), Js('Gold'), Js('Gold Nugget'), Js('Grace'), Js('Grand'), Js('Grand Arc'), Js('Griffon'), Js('Halo'), Js('Harmony'), Js('Heart'), Js('Heirloom'), Js('Helix'), Js('Herald'), Js('Heritage'), Js('Hero'), Js('Homage'), Js('Honor'), Js('Horizon'), Js('Horoscope'), Js('Hourglass'), Js('Hunter'), Js('Huntress'), Js('Illusion'), Js('Imagination'), Js('Immortal'), Js('Impulse'), Js('Independence'), Js('Infinity'), Js('Iron'), Js('Ivory'), Js('Jade'), Js('Jubilee'), Js('Kindred Souls'), Js('Lantern'), Js('Legacy'), Js('Liberty'), Js('Locomotion'), Js('Lotus'), Js('Lucent'), Js('Lunar'), Js('Lyric'), Js('Marble'), Js('Marquis'), Js('Marvel'), Js('Matron'), Js('Meadow'), Js('Melody'), Js('Memorial'), Js('Metronome'), Js('Millennium'), Js('Miracle'), Js('Mirage'), Js('Mirror'), Js('Monolith'), Js('Moonlight'), Js('Mosaic'), Js('Muse'), Js('Myriad'), Js('Nebula'), Js('Night'), Js('Nimbus'), Js('Obelisk'), Js('Obsidian'), Js('Oculus'), Js('Omen'), Js('Onyx'), Js('Oracle'), Js('Orbit'), Js('Orchard'), Js('Ornament'), Js('Oval'), Js('Palace'), Js('Panorama'), Js('Panther'), Js('Parade'), Js('Paragon'), Js('Parallel'), Js('Particle'), Js('Patron'), Js('Pendulum'), Js('Phantom'), Js('Phenomenon'), Js('Phoenix'), Js('Pinnacle'), Js('Pioneer'), Js('Portal'), Js('Prestige'), Js('Pride'), Js('Prime'), Js('Prism'), Js('Prodigy'), Js('Promise'), Js('Prophecy'), Js('Prospect'), Js('Pure Heart'), Js('Purity'), Js('Quest'), Js('Rainbow'), Js('Renaissance'), Js('Revelation'), Js('Reverie'), Js('Rex'), Js('Rhythm'), Js('Riverside'), Js('Rose'), Js('Royal'), Js('Ruby'), Js('Saffron'), Js('Sanctum'), Js('Sapphire'), Js('Sensation'), Js('Seraph'), Js('Serenity'), Js('Silver'), Js('Snowflake'), Js('Solar'), Js('Solstice'), Js('Songbird'), Js('Soul'), Js('Spectacle'), Js('Spectrum'), Js('Speculum'), Js('Sphere'), Js('Spirit'), Js('Sprite'), Js('Starlight'), Js('Stasis'), Js('Stratosphere'), Js('Sunset'), Js('Supreme'), Js('Symphony'), Js('Synthesis'), Js('Tableau'), Js('Timeless'), Js('Tribute'), Js('Trinity'), Js('Triumph'), Js('Trust'), Js('Tulip'), Js('Twilight'), Js('Twin'), Js('Unity'), Js('Universe'), Js('Valley'), Js('Valor'), Js('Velvet'), Js('Venture'), Js('Vertex'), Js('Victory'), Js('Visage'), Js('Vision'), Js('Vista'), Js('Vortex'), Js('Voyage'), Js('White Stag'), Js('Willow'), Js('Wish'), Js('Zion'), Js('Zodiac')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('Stadium'), Js('Bowl'), Js('Park'), Js('Arena'), Js('Centre'), Js('Ring'), Js('Field'), Js('Ground')]))
pass
pass


# Add lib to the module scope
stadiumNames = var.to_python()