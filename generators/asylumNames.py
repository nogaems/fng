__all__ = ['asylumNames']

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
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Angel Peaks'), Js('Angelic Gardens'), Js('Angelic Heights'), Js('Angelwings'), Js('Angelwood'), Js('Aurora Grove'), Js('Aurora Heights'), Js('Aurora Valley'), Js('Azure Heights'), Js('Azure Lake'), Js('Azure Valley'), Js('Beacon Point'), Js('Bellevue'), Js('Bliss Meadows'), Js('Blissful Heights'), Js('Blooming Fields'), Js('Blossoms'), Js('Blue Laguna'), Js('Blue River'), Js('Celestial Gardens'), Js('Celestial Heights'), Js('Cerulean Gardens'), Js('Cerulean Lake'), Js('Charity'), Js('Cherry Blossom'), Js('Clearwater'), Js('Cloudy Heights'), Js('Dawn Garden'), Js('Dawn Grove'), Js('Dawn Valley'), Js('Dayspring'), Js('Dragonfly Lake'), Js('Dream Forest'), Js('Dream Garden'), Js('Edgewater'), Js('Emerald Grove'), Js('Emerald Mountain'), Js('Eternal Gardens'), Js('Eternity Meadows'), Js('Evergreen Forest'), Js('Evergreen Valley'), Js('Felicity Gardens'), Js('Firefly Meadows'), Js('Firefly Waters'), Js('Flower Valley'), Js('Flowerfield'), Js('Flowerhill'), Js('Forest Vale'), Js('Fountain Vale'), Js('Fresh Meadows'), Js('Garden Springs'), Js('Genesis'), Js('Golden Halo'), Js('Golden Vale'), Js('Good Samaritan'), Js('Grand Meadow'), Js('Grand Oasis'), Js('Grand Valley'), Js('Great Garden'), Js('Green Valley'), Js('Grove Garden'), Js('Guardian Angel'), Js('Harmony'), Js('Harmony Heights'), Js('Harmony Lake'), Js('Harmony Meadows'), Js('Harmony Mountains'), Js('Harmony Valley'), Js('High Garden'), Js('Highland Garden'), Js('Holy Oak'), Js('Hope Garden'), Js('Hope Valley'), Js('Horizon'), Js('Hummingbird Garden'), Js('Koi Pond'), Js('Lakeside'), Js('Lilypad'), Js('Lilypad Meadows'), Js('Lilypad Water'), Js('Little Feather'), Js('Little Peak'), Js('Littlerock'), Js('Love Garden'), Js('Maple Grove'), Js('Mapleleaf'), Js('Meadow Isle'), Js('Mirror Lake'), Js('Misty Meadow'), Js('Misty Vale'), Js('Moonlight'), Js('Moonlight Meadows'), Js('Morningrise'), Js('Morningtide'), Js('Moss Forest'), Js('New Blessings'), Js('New Eden'), Js('New Horizon'), Js('Nirvana Heights'), Js('Noble Gardens'), Js('Noble Vale'), Js('Oak Meadow'), Js('Oak Valley'), Js('Olympus'), Js('Paradise Garden'), Js('Paradise Meadows'), Js('Paragon Heights'), Js('Paragon Valley'), Js('Peace Meadows'), Js('Peace Vale'), Js('Peace Valley'), Js('Pearl Garden'), Js('Pearly Lake'), Js('Pine River'), Js('Pine Valley'), Js('Rainbow Meadow'), Js('Renaissance'), Js('Repose Meadows'), Js('Riverside'), Js('Rose Garden'), Js('Rose Petal'), Js('Rosemary'), Js('Rosewood'), Js('Sacred Heart'), Js('Sacred Heights'), Js('Sage Forest'), Js('Sanctuary Gardens'), Js('Sanctuary Meadows'), Js('Sapphire Valley'), Js('Satin Gardens'), Js('Serenity'), Js('Serenity Falls'), Js('Serenity Grove'), Js('Serenity Heights'), Js('Serenity Lake'), Js('Serenity Peaks'), Js('Silence Lake'), Js('Silk Meadow'), Js('Silk River'), Js('Silver Birch'), Js('Silver Oak'), Js('Silverwing'), Js('Silverwood'), Js('Smooth Meadows'), Js('Smooth Valley'), Js('Snow Gardens'), Js('Snow Valley'), Js('Snowfall Valley'), Js('Snowflake'), Js('Soft Gardens'), Js('Soft Meadows'), Js('Solitude Gardens'), Js('Solitude Heights'), Js('Spirit Fields'), Js('Spirit Meadows'), Js('Spring Blossom'), Js('Spring Forest'), Js('Spring Garden'), Js('Spring Grove'), Js('Spring Horizon'), Js('Spring Pond'), Js('Springfield'), Js('Sprite Gardens'), Js('Sprite Valley'), Js('Starfall Lake'), Js('Starlight'), Js('Stillwater'), Js('Summer Gardens'), Js('Summerhill'), Js('Sunrise'), Js('Sunrise Grove'), Js('Sunrise Valley'), Js('Swan Lake'), Js('Swan River'), Js('Tranquil Falls'), Js('Tranquil Heights'), Js('Tranquil Peaks'), Js('Tranquil River'), Js('Tranquil Summit'), Js('Tranquil Valley'), Js('Tranquility Lake'), Js('Trinity Heights'), Js('Tulip Gardens'), Js('Twin Lakes'), Js('Twin Rivers'), Js('Velvet Gardens'), Js('Waterfall Gardens'), Js('Waterfall Meadow'), Js('Waterfall Valley'), Js('West Valley'), Js('Westwood'), Js('Whisperwood'), Js('White Dove'), Js('White Feather'), Js('White Mountain'), Js('White Valley'), Js('White Willow'), Js('White Wing'), Js('White Wings'), Js('Wildflower'), Js('Willow Vale'), Js('Willow Waters')]))
var.put('nm2', Js([Js('Asylum'), Js('Mental Institution'), Js('Sanatorium'), Js('Psychiatric Hospital'), Js('Mental Hospital'), Js('Psychiatric Institution'), Js('Mental Asylum')]))
pass
pass


# Add lib to the module scope
asylumNames = var.to_python()