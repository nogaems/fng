__all__ = ['clothingBrands']

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
    var.registers(['nm1', 'nm2', 'result'])
    var.put('nm1', Js([Js('Ace'), Js('Adore'), Js('Aeon'), Js('Allure'), Js('Ambience'), Js('Amity'), Js('Amour'), Js('Anchor'), Js('Angel'), Js('Angelwings'), Js('Anomaly'), Js('Apex'), Js('Aqua'), Js('Aqua Pura'), Js('Arcane'), Js('Ardor'), Js('Aristocrat'), Js('Arrow'), Js('Artiste'), Js('August'), Js('Aura'), Js('Aurelian'), Js('Aurora'), Js('Aurora Borealis'), Js('Awe'), Js('Azure'), Js('Beacon'), Js('Beast'), Js('Black Widow'), Js('Bliss'), Js('Blitz'), Js('Blizzard'), Js('Blossoms'), Js('Blue Flamingo'), Js('Blues'), Js('Borealis'), Js('Caesura'), Js('Capital'), Js('Castle'), Js('Charade'), Js('Charisma'), Js('Cherish'), Js('Chronicle'), Js('Comet'), Js('Countess'), Js('Crystal'), Js('Cupid'), Js('Dawn'), Js('Daydream'), Js('Dazzle'), Js('Delicacy'), Js('Delight'), Js('Desire'), Js('Eagle Eye'), Js('Ebony'), Js('Eccentricity'), Js('Eccentrics'), Js('Echo'), Js('Eclipse'), Js('Ecstasy'), Js('Edict'), Js('Elan Vital'), Js('Elite'), Js('Elysium'), Js('Emerald'), Js('Eminence'), Js('Emperor'), Js('Empress'), Js('Enchanted'), Js('Enigma'), Js('Enterprise'), Js('Entity'), Js('Entrance'), Js('Eos'), Js('Epilogue'), Js('Epoch'), Js('Escape'), Js('Esprit'), Js('Essence'), Js('Estate'), Js('Eternal Youth'), Js('Eternity'), Js('Ethereal'), Js('Euphoria'), Js('Fable'), Js('Facet'), Js('Fairy Dust'), Js('Fanatics'), Js('Fata Morgana'), Js('Fay'), Js('Felicity'), Js('Figments'), Js('Firefly'), Js('Flair'), Js('Flame'), Js('Flare'), Js('Flow'), Js('Flow Motion'), Js('Fluke'), Js('Flux'), Js('Forte'), Js('Fusion'), Js('Galaxy'), Js('Gemstone'), Js('Gift'), Js('Glamour'), Js('Glimmer'), Js('Grace'), Js('Grand Slam'), Js('Grandeur'), Js('Groove'), Js('Halcyon'), Js('Heirloom'), Js('Helix'), Js('Heritage'), Js('Honor'), Js('Hush'), Js('Illume'), Js('Impulse'), Js('Intrepid'), Js('Ivory'), Js('Joy'), Js('Jubilee'), Js('Lacuna'), Js('Lagoon'), Js('Legacy'), Js('Legend'), Js('Leisure'), Js('Leviathan'), Js('Liberty'), Js('Lily'), Js('Loco Motion'), Js('Lore'), Js('Lullaby'), Js('Luminos'), Js('Majesty'), Js('Memo'), Js('Merry'), Js("Mind's Eye"), Js('Miracle'), Js('Mirage'), Js('Monolith'), Js('Muse'), Js('Mystery'), Js('Mythic'), Js('Mythos'), Js('Noble'), Js('Nova'), Js('Oasis'), Js('Obelisk'), Js('Obsidian'), Js('Oddity'), Js('Onyx'), Js('Opal Essence'), Js('Oracle'), Js('Orchid'), Js('Palace'), Js('Paradise'), Js('Paradox'), Js('Paragon'), Js('Parallel'), Js('Paramour'), Js('Patron'), Js('Peacock'), Js('Petal'), Js('Petal Rose'), Js('Phenomenon'), Js('Pinnacle'), Js('Pizzazz'), Js('Pompon'), Js('Prestige'), Js('Prime'), Js('Primrose'), Js('Prodigy'), Js('Prophecy'), Js('Psyche'), Js('Pyramid'), Js('Pyre'), Js('Question Mark'), Js('Radiance'), Js('Rara Avis'), Js('Reflection'), Js('Reign'), Js('Relish'), Js('Repose'), Js('Retrospectacle'), Js('Revelation'), Js('Reverse'), Js('Saga'), Js('Sanctuary'), Js('Sapphire'), Js('Scandal'), Js('Scents'), Js('Sensations'), Js('Serenity'), Js('Shadow'), Js('Shooting Star'), Js('Snowflake'), Js('Solace'), Js('Solitude'), Js('Solstice'), Js('Spark'), Js('Sparkle'), Js('Spectacle'), Js('Spellbound'), Js('Spire'), Js('Spirit'), Js('Sprite'), Js('Starlight'), Js('Stasis'), Js('Strut'), Js('Suave'), Js('Summit'), Js('Swagger'), Js('Swashbuckle'), Js('Tempest'), Js('Temptation'), Js('Tranquility'), Js('Tribute'), Js('Triumph'), Js('Urbane'), Js('Valentine'), Js('Venture'), Js('Vice'), Js('Virtue'), Js('Vision'), Js('Vortex'), Js('White Wolf'), Js('Willow'), Js('Yen'), Js('Yin'), Js('Zeal'), Js('Zenith'), Js('Zigzag'), Js('Zion')]))
    var.put('nm2', Js([Js('Design'), Js('Designs'), Js('Apparel'), Js('Gear'), Js('Couture'), Js('Clothing Company'), Js('Clothing'), Js('Accessories'), Js('Fashion'), Js('Clothing'), Js('Clothes'), Js('Collective'), Js('Collection'), Js('Company')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            if (var.get('i')<Js(3.0)):
                var.put('names', var.get('nm1').get(var.get('rnd')))
            else:
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
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
clothingBrands = var.to_python()