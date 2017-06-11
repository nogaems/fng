__all__ = ['dndShifterNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', var.get('names2').get(var.get('rnd2')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('names', var.get('names1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Acor'), Js('Almond'), Js('Ash'), Js('Astro'), Js('Badger'), Js('Barb'), Js('Basalt'), Js('Basil'), Js('Beast'), Js('Birch'), Js('Blast'), Js('Blaze'), Js('Bluff'), Js('Bog'), Js('Boulder'), Js('Bramble'), Js('Breach'), Js('Briar'), Js('Brock'), Js('Brook'), Js('Burst'), Js('Canyon'), Js('Char'), Js('Chasm'), Js('Cinder'), Js('Claw'), Js('Cliff'), Js('Cloud'), Js('Coal'), Js('Cobalt'), Js('Cobble'), Js('Comet'), Js('Cosmo'), Js('Crag'), Js('Crater'), Js('Dash'), Js('Drake'), Js('Drift'), Js('Dune'), Js('Dusk'), Js('Dust'), Js('Echo'), Js('Fang'), Js('Flame'), Js('Flare'), Js('Flax'), Js('Flint'), Js('Flood'), Js('Foam'), Js('Fog'), Js('Forest'), Js('Fox'), Js('Frost'), Js('Frostbite'), Js('Fume'), Js('Fury'), Js('Gale'), Js('Glare'), Js('Gorge'), Js('Grime'), Js('Grit'), Js('Grove'), Js('Gulch'), Js('Gust'), Js('Kindle'), Js('Light'), Js('Lumber'), Js('Magma'), Js('Mahogany'), Js('Marsh'), Js('Mercury'), Js('Midnight'), Js('Mire'), Js('Moss'), Js('Mountain'), Js('Nebula'), Js('Newt'), Js('Nightfall'), Js('Nightshade'), Js('Nimbus'), Js('North'), Js('Nova'), Js('Nyx'), Js('Oak'), Js('Ocean'), Js('Onyx'), Js('Pitch'), Js('Pyre'), Js('Pyro'), Js('Quicksilver'), Js('Ravine'), Js('Ridge'), Js('Rift'), Js('River'), Js('Rock'), Js('Rubble'), Js('Scar'), Js('Shrub'), Js('Silver'), Js('Smoke'), Js('Soot'), Js('Spark'), Js('Spike'), Js('Spine'), Js('Steam'), Js('Steel'), Js('Stone'), Js('Storm'), Js('Surge'), Js('Talon'), Js('Thicket'), Js('Thistle'), Js('Thorn'), Js('Thunder'), Js('Tide'), Js('Tiger'), Js('Timber'), Js('Tinder'), Js('Tor'), Js('Torrent'), Js('Vapor'), Js('Vermin'), Js('Vine'), Js('Void'), Js('Wave'), Js('Willow'), Js('Wolf'), Js('Woods')]))
var.put('names2', Js([Js('Abyss'), Js('Almond'), Js('Amber'), Js('Amethyst'), Js('Anemone'), Js('Aqua'), Js('Aurora'), Js('Autumn'), Js('Birch'), Js('Bloom'), Js('Blossom'), Js('Breeze'), Js('Briar'), Js('Brook'), Js('Canyon'), Js('Chestnut'), Js('Cloud'), Js('Coral'), Js('Coyote'), Js('Crest'), Js('Cricket'), Js('Crystal'), Js('Dawn'), Js('Dew'), Js('Dewdrop'), Js('Diamond'), Js('Elm'), Js('Ember'), Js('Emerald'), Js('Evening'), Js('Feather'), Js('Fern'), Js('Flare'), Js('Floe'), Js('Flora'), Js('Floret'), Js('Flow'), Js('Fluff'), Js('Galaxy'), Js('Gem'), Js('Hail'), Js('Harley'), Js('Haze'), Js('Hazel'), Js('Horizon'), Js('Ice'), Js('Indigo'), Js('Iris'), Js('Isle'), Js('Ivy'), Js('Jade'), Js('Jasmine'), Js('Juniper'), Js('Karma'), Js('Lake'), Js('Lavender'), Js('Leaf'), Js('Lily'), Js('Luna'), Js('Magenta'), Js('Maple'), Js('Marigold'), Js('Meadow'), Js('Midnight'), Js('Mist'), Js('Moon'), Js('Moss'), Js('Nebula'), Js('Nutmeg'), Js('Ocean'), Js('Olive'), Js('Opal'), Js('Orchid'), Js('Pearl'), Js('Petal'), Js('Pine'), Js('Pinecone'), Js('Plume'), Js('Poison'), Js('Pyro'), Js('Quill'), Js('Rain'), Js('Raven'), Js('Rill'), Js('River'), Js('Robin'), Js('Rose'), Js('Rosemary'), Js('Ruby'), Js('Saffron'), Js('Sage'), Js('Sapphire'), Js('Scarlet'), Js('Shade'), Js('Silver'), Js('Sky'), Js('Snow'), Js('Snowflake'), Js('Spring'), Js('Star'), Js('Stardust'), Js('Sugar'), Js('Summer'), Js('Sun'), Js('Sunrise'), Js('Sunset'), Js('Sunshine'), Js('Swill'), Js('Thistle'), Js('Tidal'), Js('Tiger'), Js('Tinder'), Js('Topaz'), Js('Twig'), Js('Twilight'), Js('Urchin'), Js('Vapor'), Js('Violet'), Js('Whirl'), Js('Willow'), Js('Wind'), Js('Wing'), Js('Winter')]))
pass
pass


# Add lib to the module scope
dndShifterNames = var.to_python()