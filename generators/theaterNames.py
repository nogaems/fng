__all__ = ['theaterNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Academy'), Js('Aeon'), Js('Alliance'), Js('Ambassador'), Js('Ambition'), Js('Ancestral'), Js('Angel'), Js('Animus'), Js('Apex'), Js('Apollo'), Js('Apple Blossom'), Js('Arcane'), Js('Arts'), Js('Aura'), Js('Aurora'), Js('Bamboo'), Js('Beacon'), Js('Bellevue'), Js('Bluebell'), Js('Borealis'), Js('Boulevard'), Js('Capital'), Js('Carnival'), Js('Casino'), Js('Castle'), Js('Celeste'), Js('Celestial'), Js('Century'), Js('Cerberus'), Js('Cherry Blossom'), Js('Chimera'), Js('Citadel'), Js('Classic'), Js('Climax'), Js('Cosmos'), Js('Courtyard'), Js('Crescent'), Js('Crown'), Js('Crystal'), Js('Curator'), Js('Daydream'), Js('Delight'), Js('Desire'), Js('Diamond'), Js('Dominion'), Js('Downtown'), Js('Dreamland'), Js('Eclipse'), Js('Ecstasy'), Js('Eden'), Js('Ellipse'), Js('Emerald'), Js('Eminence'), Js('Empire'), Js('Enigma'), Js('Epoch'), Js('Eternity'), Js('Euphony'), Js('Exalted'), Js('Fantasia'), Js('Fantasy'), Js('Festival'), Js('Figment'), Js('Firefly'), Js('Flux'), Js('Fortune'), Js('Frontier'), Js('Galaxy'), Js('Gilded'), Js('Globe'), Js('Golden Gate'), Js('Grand'), Js('Grand Avenue'), Js('Grand Centre'), Js('Grand Chateau'), Js('Grand Fountain'), Js('Grand Guild'), Js('Grand Palace'), Js('Grand Park'), Js('Grand River'), Js('Grand Shrine'), Js('Grandeur'), Js('Grandview'), Js('Guardian'), Js('Harmony'), Js('Heirloom'), Js('Heritage'), Js('Hippogriff'), Js('Illusion'), Js('Image'), Js('Imagination'), Js('Imagine'), Js('Imperial'), Js('Infinity'), Js('Jupiter'), Js("King's"), Js('Landmark'), Js('Legacy'), Js('Legend'), Js('Lilypad'), Js('Limelight'), Js('Lionheart'), Js('Little'), Js('Lumina'), Js('Luminous'), Js('Luminus'), Js('Lunar'), Js('Magic Lantern'), Js('Magister'), Js('Majesty'), Js('Major'), Js('Mammoth'), Js('Melody'), Js('Mercury'), Js('Meridian'), Js('Millennium'), Js('Mirage'), Js('Monolith'), Js('Monument'), Js('Moonlight'), Js('Mystery'), Js('Nebula'), Js('Nightingale'), Js('Obelisk'), Js('Obsidian'), Js('Onyx'), Js('Oracle'), Js('Orbit'), Js('Orion'), Js('Ornate'), Js('Paradise'), Js('Paragon'), Js('Paramount'), Js('Paramour'), Js('Patriot'), Js('Pavilion'), Js('Peacock'), Js('Phenomenon'), Js('Phoenix'), Js('Pilgrim'), Js('Pinnacle'), Js('Pioneer'), Js('Platinum'), Js('Pluto'), Js('Prestige'), Js('Prime'), Js('Prism'), Js('Prodigy'), Js('Pyramid'), Js('Radiance'), Js('Rainbow'), Js('Regal'), Js('Resonance'), Js('Rhinestone'), Js('Rose Petal'), Js('Rosebud'), Js('Royal'), Js('Royal Court'), Js('Royal Hall'), Js('Sapphire'), Js('Serenity'), Js('Silverlight'), Js('Snowflake'), Js('Solar'), Js('Solaris'), Js('Solstice'), Js('Songbird'), Js('Spectacle'), Js('Spirit'), Js('Spotlight'), Js('Spring Garden'), Js('Sprite'), Js('Stargaze'), Js('Starlight'), Js('Stellar'), Js('Summer Garden'), Js('Summit'), Js('Sunset'), Js('Supremacy'), Js('Swanlake'), Js('Talisman'), Js('Independence'), Js('Temple'), Js('Tiara'), Js('Titan'), Js('Tranquility'), Js('Transcendence'), Js('Treasure'), Js('Trinity'), Js('Twilight'), Js('Unison'), Js('Universe'), Js('Uptown'), Js('Utopia'), Js('Valentine'), Js('Vanilla Flower'), Js('Velvet'), Js('Vertex'), Js('Victory'), Js('Vintage'), Js('Virtue'), Js('Vision'), Js('Vortex'), Js('Warden'), Js('Watchtower'), Js('White Flare'), Js('White Orchid'), Js('Zion')]))
var.put('nm2', Js([Js('Theater'), Js('Opera House'), Js('Cinema'), Js('Assembly Hall'), Js('Amphitheater'), Js('Concert Hall'), Js('Theatre')]))
pass
pass


# Add lib to the module scope
theaterNames = var.to_python()