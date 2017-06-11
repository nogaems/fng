__all__ = ['casinoNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'nm4', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Aegis'), Js('Aeon'), Js('Aeros'), Js('Allure'), Js('Ambrosia'), Js('Amethyst'), Js('Anemone'), Js('Apex'), Js('Arch'), Js('Archway'), Js('Aria'), Js('Aristocrat'), Js('Aura'), Js('Aurora'), Js('Avian'), Js('Azalea'), Js('Basilica'), Js('Bastille'), Js('Belvedere'), Js('Bird of Paradise'), Js('Blossom'), Js('Borealis'), Js('Boulevard'), Js('Cadence'), Js('Calypso'), Js('Cardinal'), Js('Carriage'), Js('Celesta'), Js('Century'), Js('Chalice'), Js('Chariot'), Js('Clover'), Js('Coronal'), Js('Creek'), Js('Crescendo'), Js('Crown'), Js('Cub'), Js('Curtain'), Js('Cushion'), Js('Delta'), Js('Diamond'), Js('Dove'), Js('Dream'), Js('Dune'), Js('Echo'), Js('Eclipse'), Js('Element'), Js('Elephant'), Js('Elixir'), Js('Ellipsis'), Js('Elysian'), Js('Elysium'), Js('Emerald'), Js('Equinox'), Js('Euphoria'), Js('Excelsior'), Js('Felicity'), Js('Flame'), Js('Fountain'), Js('Gala'), Js('Gate'), Js('Glacier'), Js('Globe'), Js('Gold Nugget'), Js('Grand Plaza'), Js('Greyhound'), Js('Halo'), Js('Harmony'), Js('Helix'), Js('Horseshoe'), Js('Hyacinth'), Js('Iris'), Js('Labyrinth'), Js('Lady Fortune'), Js('Leviathan'), Js('Liberty'), Js('Lion'), Js('Luminos'), Js('Luna'), Js('Majesty'), Js('Marble'), Js('Matrix'), Js('Medallion'), Js('Melody'), Js('Meridian'), Js('Millenium'), Js('Mint'), Js('Mithril'), Js('Mountain'), Js('Myriad'), Js('Mystery'), Js('Mystique'), Js('Nightowl'), Js('Nimbus'), Js('Nova'), Js('Nugget'), Js('Oasis'), Js('Obelisk'), Js('Oleander'), Js('Orchid'), Js('Palm'), Js('Paradise'), Js('Phantom'), Js('Pinnacle'), Js('Plaza'), Js('Plume'), Js('Prism'), Js('Quill'), Js('Reef'), Js('Rhythm'), Js('Robin'), Js('Rose'), Js('Sable'), Js('Sapphire'), Js('Scarlet'), Js('Scepter'), Js('Serenade'), Js('Serendipity'), Js('Serenity'), Js('Sierra'), Js('Siren'), Js('Snowflake'), Js('Solas'), Js('Solstice'), Js('Spa'), Js('Spire'), Js('Spirit'), Js('Spring'), Js('Stallion'), Js('Star'), Js('Talisman'), Js('Tempest'), Js('Tiara'), Js('Tigress'), Js('Trillium'), Js('Valley'), Js('Vertex'), Js('Victory'), Js('Voyage'), Js('Wolfhound'), Js('Zenith'), Js('Zephyr')]))
    var.put('nm2', Js([Js('Aerial'), Js('Alabaster'), Js('Amber'), Js('Amethyst'), Js('Aqua'), Js('Astral'), Js('Atlantic'), Js('Aurelian'), Js('Azuline'), Js('Azure'), Js('Cardinal'), Js('Carmine'), Js('Celestial'), Js('Cerulean'), Js('Coral'), Js('Crimson'), Js('Crown'), Js('Crystal'), Js('Diamond'), Js('Eastern'), Js('Ebon'), Js('Ember'), Js('Emerald'), Js('Exalted'), Js('Gilded'), Js('Gold'), Js('Golden'), Js('Grand'), Js('Granite'), Js('Halcyon'), Js('Indigo'), Js('Ivory'), Js('Jade'), Js('King'), Js('Lavender'), Js('Light'), Js('Lucky'), Js('Lunar'), Js('Malachite'), Js('Marble'), Js('Marina'), Js('Maroon'), Js('Noble'), Js('Northern'), Js('Obsidian'), Js('Onyx'), Js('Pacific'), Js('Paradise'), Js('Porcelain'), Js('Regal'), Js('Royal'), Js('Ruby'), Js('Sable'), Js('Saffron'), Js('Sanguine'), Js('Sapphire'), Js('Scarlet'), Js('Silk'), Js('Silver'), Js('Solar'), Js('Southern'), Js('Supreme'), Js('Twin'), Js('Velour'), Js('Velvet'), Js('Verdigris'), Js('Vermilion'), Js('Violet'), Js('Viridian'), Js('Western'), Js('White')]))
    var.put('nm3', Js([Js('Aegis'), Js('Aeon'), Js('Allure'), Js('Anemone'), Js('Angel'), Js('Arc'), Js('Arch'), Js('Archway'), Js('Aura'), Js('Aurora'), Js('Avian'), Js('Bastille'), Js('Blossom'), Js('Borealis'), Js('Boulevard'), Js('Carriage'), Js('Chalice'), Js('Chariot'), Js('Citadel'), Js('Cloak'), Js('Cloud'), Js('Clover'), Js('Court'), Js('Creek'), Js('Crown'), Js('Cub'), Js('Curtain'), Js('Cushion'), Js('Diamond'), Js('Dome'), Js('Dove'), Js('Dream'), Js('Dune'), Js('Element'), Js('Elephant'), Js('Dawn'), Js('Chandelier'), Js('Panther'), Js('Griffin'), Js('Flame'), Js('Flower'), Js('Fountain'), Js('Garden'), Js('Gardens'), Js('Gate'), Js('Globe'), Js('Greyhound'), Js('Halo'), Js('Heirloom'), Js('Helix'), Js('Horseshoe'), Js('Hyacinth'), Js('Iris'), Js('Jewel'), Js('Labyrinth'), Js('Leviathan'), Js('Lion'), Js('Majesty'), Js('Mantle'), Js('Medallion'), Js('Mountain'), Js('Mystery'), Js('Nebula'), Js('Nimbus'), Js('Nugget'), Js('Oasis'), Js('Obelisk'), Js('Oleander'), Js('Orb'), Js('Orchid'), Js('Palm'), Js('Petal'), Js('Phoenix'), Js('Plume'), Js('Prism'), Js('Pyramid'), Js('Quill'), Js('Reef'), Js('Ribbon'), Js('Rose'), Js('Sabre'), Js('Scepter'), Js('Shield'), Js('Shrine'), Js('Sierra'), Js('Siren'), Js('Snowflake'), Js('Peacock'), Js('Solstice'), Js('Spa'), Js('Spire'), Js('Stallion'), Js('Star'), Js('Talisman'), Js('Tempest'), Js('Tiara'), Js('Tigress'), Js('Trillium'), Js('Trinket'), Js('Valley'), Js('Wolfhound'), Js('Zenith'), Js('Zephyr')]))
    var.put('nm4', Js([Js(''), Js(' Casino')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((Js('The ')+var.get('nm1').get(var.get('rnd')))+var.get('nm4').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((((Js('The ')+var.get('nm2').get(var.get('rnd')))+Js(' '))+var.get('nm3').get(var.get('rnd2')))+Js(' Casino')))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
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
casinoNames = var.to_python()