__all__ = ['hospitalNames']

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
var.put('nm1', Js([Js('Alliance'), Js('Amity'), Js('Angelstone'), Js('Angelvale'), Js('Angelwing'), Js('Angelwood'), Js('Animas'), Js('Archangel'), Js('Bayhealth'), Js('Bayview'), Js('Beacon'), Js('Bellevue'), Js('Bellflower'), Js('Big Heart'), Js('Big River'), Js('Blessings'), Js('Blossom'), Js('Blossom Valley'), Js('Blossomvale'), Js('Broadwater'), Js('Castle'), Js('Charity'), Js('Cherry Blossom'), Js('Citrus'), Js('Clearview'), Js('Clearwater Lake'), Js('Clearwater Valley'), Js('Clemency'), Js('Crossroads'), Js('Desert Springs'), Js('Diamond Grove'), Js('East Valley'), Js('Eden'), Js('Edgewater'), Js('Evergreen'), Js('Fairbanks'), Js('Fairmont'), Js('Fairview'), Js('Featherfall'), Js('Flowerhill'), Js('Forest Health'), Js('Forest View'), Js('Fortuna'), Js('Fortune'), Js('Fountain Valley'), Js('Freeman'), Js('Garden City'), Js('Garden Grove'), Js('Genesis'), Js('Golden Oak'), Js('Golden Valley'), Js('Goldriver'), Js('Goldvalley'), Js('Good Samaritan'), Js('Grace'), Js('Grand Garden'), Js('Grand Meadow'), Js('Grand Mountain'), Js('Grand Oak'), Js('Grand Plains'), Js('Grand River'), Js('Grand University'), Js('Grand Valley'), Js('Grand View'), Js('Grand Willow'), Js('Grandview'), Js('Great Plains'), Js('Great River'), Js('Green Country'), Js('Green Hill'), Js('Greengrass'), Js('Greenlawn'), Js('Greenwood'), Js('Griffin'), Js('Guardian'), Js('Hallmark'), Js('Harmony'), Js('Harmony Grove'), Js('Healthbridge'), Js('Healthstone'), Js('Heart Center'), Js('Heartland'), Js('Heartstone'), Js('Highland'), Js('Highlands'), Js('Hill Crest'), Js('Hillsdale'), Js('Honor'), Js('Honor Grave'), Js('Hope Garden'), Js('Hope Haven'), Js('Hope Valley'), Js('Hopedale'), Js('Hopevale'), Js('Horizon'), Js('Hot Springs'), Js('Hyacinth'), Js('Jade Forest'), Js('Kindred'), Js('Kindred Soul'), Js('Laguna'), Js('Lakeland'), Js('Lakeside'), Js('Lakewood'), Js('Lifecare'), Js('Light Beacon'), Js('Lilypad'), Js('Lilypad Gardens'), Js('Little River'), Js('Love'), Js('Lowland'), Js('Lullaby'), Js('Magnolia'), Js('Maple Grove'), Js('Maple Valley'), Js('Marine'), Js('Meadowview'), Js('Memorial'), Js('Mercy'), Js('Mercy Vale'), Js('Mineral'), Js('Morningside'), Js('Mountain View'), Js('New Eden'), Js('New Horizons'), Js('Noble'), Js('North Star'), Js('Northshore'), Js('Oak Crest'), Js('Oak Valley'), Js('Oakdale'), Js('Oasis'), Js('Olympus'), Js('Orange Garden'), Js('Overlook'), Js('Paradise Grove'), Js('Paradise Valley'), Js('Parkview'), Js('Peace Forest'), Js('Peace River'), Js('Peak View'), Js('Pearl River'), Js('Petunia'), Js('Phoenix'), Js('Pine Rest'), Js('Pine Valley'), Js('Pinevale'), Js('Pinevalley'), Js('Pioneer'), Js('Primary'), Js('Principal'), Js('Progress'), Js('Promise'), Js('Rainbow'), Js('Repose'), Js('Ridgeview'), Js('Riverside'), Js('Riverview'), Js('Rose'), Js('Rose Gardens'), Js('Rose Petal'), Js('Rose Valley'), Js('Rosemary'), Js('Rosewood'), Js('Ruby Valley'), Js('Sacred Heart'), Js('Samaritan'), Js('Sapphire Lake'), Js('Serenity'), Js('Silver Birch'), Js('Silver Boulder'), Js('Silver Gardens'), Js('Silver Hill'), Js('Silver Lake'), Js('Silver Oak'), Js('Silver Pine'), Js('Silver Wing'), Js('Silverstone'), Js('Silverwood'), Js('Snowflake'), Js('Southshore'), Js('Specialty'), Js('Spring Forest'), Js('Spring Fountain'), Js('Spring Grove'), Js('Spring Harbor'), Js('Spring Hill'), Js('Spring River'), Js('Springfield'), Js('Springhill'), Js('Stillwater'), Js('Summer Springs'), Js('Summerfield'), Js('Summerhill'), Js('Summerstone'), Js('Summit'), Js('Swan River'), Js('Swanlake'), Js('Tranquil Valley'), Js('Tranquility'), Js('Trinity'), Js('Tulip'), Js('Twin Lakes'), Js('Twin Mountains'), Js('Union'), Js('United'), Js('Valley Health'), Js('Wellness'), Js('West Valley'), Js('Westview'), Js('White Blossom'), Js('White Feather'), Js('White Mountain'), Js('White Petal'), Js('White River'), Js('White Willow'), Js('White Wing'), Js('Wildflower'), Js('Willow Gardens'), Js('Woodland')]))
var.put('nm2', Js([Js('Clinic'), Js('Community Hospital'), Js('General Hospital'), Js('Hospital'), Js('Hospital Center'), Js('Medical Center'), Js('Medical Clinic')]))
pass
pass


# Add lib to the module scope
hospitalNames = var.to_python()