__all__ = ['dndGenasi']

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
    var.registers(['nm1', 'nm2', 'nm3', 'result', 'nm4'])
    var.put('nm1', Js([Js('Ablaze'), Js('Alight'), Js('Ardor'), Js('Ardour'), Js('Arson'), Js('Ash'), Js('Austral'), Js('Bake'), Js('Beacon'), Js('Blaze'), Js('Blight'), Js('Boil'), Js('Bonfire'), Js('Brand'), Js('Broil'), Js('Burn'), Js('Calcine'), Js('Candle'), Js('Cauterize'), Js('Char'), Js('Charcoal'), Js('Cinder'), Js('Coal'), Js('Combust'), Js('Conflagration'), Js('Cremate'), Js('Crisp'), Js('Dante'), Js('Dantean'), Js('Ember'), Js('Enkindle'), Js('Explosion'), Js('Fervor'), Js('Fever'), Js('Fiery'), Js('Flame'), Js('Flare'), Js('Flash'), Js('Flicker'), Js('Flux'), Js('Forge'), Js('Frizzle'), Js('Fry'), Js('Fuego'), Js('Fuel'), Js('Fume'), Js('Furnace'), Js('Glare'), Js('Gleam'), Js('Glint'), Js('Glow'), Js('Grill'), Js('Heat'), Js('Hell'), Js('Hellfire'), Js('Hot'), Js('Igneous'), Js('Ignite'), Js('Ignition'), Js('Incendiary'), Js('Incinerate'), Js('Infernal'), Js('Inferno'), Js('Kiln'), Js('Kindle'), Js('Lantern'), Js('Lava'), Js('Light'), Js('Lit'), Js('Magma'), Js('Melt'), Js('Nether'), Js('Oven'), Js('Parch'), Js('Phoenix'), Js('Piping'), Js('Pyre'), Js('Pyro'), Js('Roast'), Js('Scald'), Js('Scorch'), Js('Scoria'), Js('Sear'), Js('Seethe'), Js('Shine'), Js('Singe'), Js('Sizzle'), Js('Smoke'), Js('Smolder'), Js('Soot'), Js('Spark'), Js('Sultry'), Js('Sun'), Js('Swelter'), Js('Thermal'), Js('Thermo'), Js('Tinder'), Js('Toast'), Js('Torch'), Js('Torrid'), Js('Volcano'), Js('Warmth'), Js('Wildfire'), Js('Wither')]))
    var.put('nm2', Js([Js('Agua'), Js('Aqua'), Js('Azure'), Js('Basin'), Js('Bath'), Js('Bathe'), Js('Beck'), Js('Bore'), Js('Branch'), Js('Brine'), Js('Brook'), Js('Cleanse'), Js('Course'), Js('Creek'), Js('Current'), Js('Dabble'), Js('Damp'), Js('Deluge'), Js('Dew'), Js('Dewdrop'), Js('Douse'), Js('Downpour'), Js('Drain'), Js('Drench'), Js('Drift'), Js('Drip'), Js('Drizzle'), Js('Drop'), Js('Droplet'), Js('Drown'), Js('Eagre'), Js('Estuary'), Js('Expanse'), Js('Flood'), Js('Flow'), Js('Flux'), Js('Fog'), Js('Fountain'), Js('Geyser'), Js('Gush'), Js('Hose'), Js('Hydra'), Js('Hydrogen'), Js('Influx'), Js('Jet'), Js('Lagoon'), Js('Lake'), Js('Lakelet'), Js('Liquid'), Js('Mere'), Js('Mist'), Js('Monsoon'), Js('Neptune'), Js('Ocean'), Js('Paddle'), Js('Plash'), Js('Plunge'), Js('Pond'), Js('Pool'), Js('Precip'), Js('Puddle'), Js('Quagmire'), Js('Rain'), Js('Rill'), Js('Rinse'), Js('Ripple'), Js('River'), Js('Rivulet'), Js('Run'), Js('Runnel'), Js('Rush'), Js('Sea'), Js('Seiche'), Js('Shower'), Js('Soak'), Js('Spatter'), Js('Splash'), Js('Spout'), Js('Spring'), Js('Sprinkle'), Js('Storm'), Js('Stream'), Js('Streamlet'), Js('Surf'), Js('Surge'), Js('Swish'), Js('Tear'), Js('Teardrop'), Js('Tempest'), Js('Tidal'), Js('Tide'), Js('Torrent'), Js('Tributary'), Js('Tsunami'), Js('Typhoon'), Js('Vapor'), Js('Wash'), Js('Wave'), Js('Well'), Js('Wet')]))
    var.put('nm3', Js([Js('Adamant'), Js('Agate'), Js('Alabaster'), Js('Amethyst'), Js('Azurite'), Js('Basalt'), Js('Bedrock'), Js('Block'), Js('Boulder'), Js('Brick'), Js('Callous'), Js('Citrine'), Js('Clay'), Js('Cliff'), Js('Cobble'), Js('Cobblestone'), Js('Crag'), Js('Crystal'), Js('Dense'), Js('Diamond'), Js('Emerald'), Js('Flint'), Js('Fossil'), Js('Fossilstone'), Js('Garnet'), Js('Gem'), Js('Geo'), Js('Geode'), Js('Granite'), Js('Gravel'), Js('Grime'), Js('Ground'), Js('Hill'), Js('Hunk'), Js('Ingot'), Js('Jade'), Js('Jewel'), Js('Lapis'), Js('Lazuli'), Js('Limestone'), Js('Lodge'), Js('Lump'), Js('Malachite'), Js('Marble'), Js('Marmoreal'), Js('Mason'), Js('Masonry'), Js('Mineral'), Js('Monolith'), Js('Moonstone'), Js('Mountain'), Js('Nugget'), Js('Obsidian'), Js('Onyx'), Js('Opal'), Js('Ore'), Js('Pebble'), Js('Pellet'), Js('Peridot'), Js('Precious'), Js('Quarry'), Js('Quartz'), Js('Quartzite'), Js('Rock'), Js('Rocky'), Js('Rough'), Js('Rubble'), Js('Ruby'), Js('Rugged'), Js('Sand'), Js('Sandstone'), Js('Sapphire'), Js('Sediment'), Js('Shelf'), Js('Slab'), Js('Slate'), Js('Soapstone'), Js('Solid'), Js('Spinel'), Js('Stone'), Js('Stony'), Js('Sturdy'), Js('Terra'), Js('Tile'), Js('Topaz'), Js('Travertine'), Js('Turf'), Js('Umber'), Js('Wedge'), Js('Zircon')]))
    var.put('nm4', Js([Js('Aerate'), Js('Aerial'), Js('Air'), Js('Ascend'), Js('Atmosphere'), Js('Aura'), Js('Aviate'), Js('Azure'), Js('Blast'), Js('Blow'), Js('Breath'), Js('Breeze'), Js('Celeste'), Js('Celestial'), Js('Chinook'), Js('Cruise'), Js('Current'), Js('Cyclone'), Js('Draft'), Js('Drift'), Js('Eddy'), Js('Empyrean'), Js('Fan'), Js('Float'), Js('Flow'), Js('Flurry'), Js('Flute'), Js('Flutter'), Js('Fly'), Js('Funnel'), Js('Gale'), Js('Gasp'), Js('Glide'), Js('Gust'), Js('Heave'), Js('Heaven'), Js('Hiss'), Js('Hover'), Js('Hurricane'), Js('Lift'), Js('Mistral'), Js('Murmur'), Js('Oxygen'), Js('Ozone'), Js('Pipe'), Js('Pneumatic'), Js('Puff'), Js('Rise'), Js('Sail'), Js('Shriek'), Js('Sigh'), Js('Sky'), Js('Soar'), Js('Squall'), Js('Storm'), Js('Stratosphere'), Js('Surge'), Js('Tempest'), Js('Tornado'), Js('Troposphere'), Js('Tumult'), Js('Turbine'), Js('Turbulence'), Js('Twister'), Js('Vent'), Js('Waft'), Js('Wheeze'), Js('Whiff'), Js('Whirl'), Js('Whirlwind'), Js('Whisk'), Js('Whistle'), Js('Wind'), Js('Wing'), Js('Zephyr')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(12.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('names', var.get('nm1').get(var.get('rnd')))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('names', var.get('nm2').get(var.get('rnd')))
                    var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    if (var.get('i')<Js(9.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                        var.put('names', var.get('nm3').get(var.get('rnd')))
                        var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
                    else:
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('names', var.get('nm4').get(var.get('rnd')))
                        var.get('nm4').callprop('splice', var.get('rnd'), Js(1.0))
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
dndGenasi = var.to_python()