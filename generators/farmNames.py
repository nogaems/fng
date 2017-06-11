__all__ = ['farmNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', ((var.get('names1').get(var.get('rnd0'))+Js(' '))+var.get('names2').get(var.get('rnd1'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Almond'), Js('Angry Beaver'), Js('Apple Blossom'), Js('Applewood'), Js('Bear Creek'), Js('Beechnut'), Js('Berry Crest'), Js('Berry Ridge'), Js('Big Bear'), Js('Big Oak'), Js("Bird's Nest"), Js('Birds of Paradise'), Js('Bitterroot'), Js('Bittersweet'), Js('Black Dog'), Js('Black Hallow'), Js('Black Hawk'), Js('Black Oak'), Js('Black Raven'), Js('Blackmeadow'), Js('Blackwater'), Js('Blazing Pitchfork'), Js('Blue Moon'), Js('Blue River'), Js('Blueberry'), Js('Blueberry Basket'), Js('Bluebird'), Js('Bluestone'), Js('Borealis'), Js('Boulder Valley'), Js('Breezy Hills'), Js('Broken Arrow'), Js('Broken Cart'), Js('Buffalo Hill'), Js("Bull's Eye"), Js('Bumble Bee'), Js('Burning Sands'), Js('Cabinwood'), Js('Canyon Crest'), Js('Canyon Crossing'), Js('Chariot'), Js('Cherry Blossom'), Js('Chestnut Grove'), Js('Chicken Egg'), Js('Cowboy'), Js('Cranberry'), Js('Crescent Canyon'), Js('Crescent Moon'), Js('Critter Craze'), Js('Crooked Creek'), Js('Crossroad'), Js('Crown Meadow'), Js('Dandelion'), Js('Day Break'), Js('Deer Cove'), Js('Desert Cliffs'), Js('Desert Fox'), Js('Diamond Creek'), Js('Dogwood'), Js('Dragon Hill'), Js('Dragontooth'), Js('Dreamworks'), Js('Eagle Eye'), Js('Eagle Hill'), Js("Eagle's Nest"), Js('Eaglecrest'), Js('Eastwood'), Js('Echo Valley'), Js('Elysian'), Js('End of the World'), Js('Evening Star'), Js('Evergreen'), Js('Fairview'), Js('Firebranch'), Js('Flower Valley'), Js('Flying Pig'), Js('Foxtail'), Js('Freedom'), Js('Fresh Fountain'), Js('Furball'), Js('Gem Stone'), Js('Gilded Woods'), Js('Gold Creek'), Js('Gold Mine'), Js('Golden Hill'), Js('Good Day'), Js('Good Times'), Js('Goose Creek'), Js('Goose Feather'), Js('Grand Mountain'), Js('Grand River'), Js('Grand View'), Js('Grasshopper'), Js('Grassy Knoll'), Js('Green Haven'), Js('Green Meadows'), Js('Green River'), Js('Grizzly Bear'), Js('Happy'), Js('Happy Horse'), Js('Happy Trails'), Js('Hard Rock'), Js('Haywire'), Js('Hazelnut'), Js('Hazelwood'), Js('Healthy Horse'), Js('Heartsong'), Js('Hee Haw'), Js('Hidden Creek'), Js('Hidden Hill'), Js('High Hill'), Js('High Valey'), Js('Highland'), Js('Hollow Hill'), Js('Hollow Point'), Js('Hollybrook'), Js('Honey'), Js('Honey Bee'), Js('Honey Comb'), Js('Horseshoe'), Js('Iron Hill'), Js('Itty Bitty'), Js('Jolly Green'), Js('Jolly Oak'), Js('Laughing Oak'), Js('Little'), Js('Little Acorn'), Js('Little Critters'), Js('Little Feet'), Js('Little Foot'), Js('Little Lamb'), Js('Little Paws'), Js('Little Wolf'), Js('Lock, Stock & Barrel'), Js('Lone Oak'), Js('Lone Pine'), Js('Lone Wolf'), Js('Lucky'), Js('Lucky Paws'), Js('Lucky Star'), Js('Mad River'), Js('Maple Leaf'), Js('Maple Springs'), Js('Maple Valley'), Js('Maplewood'), Js('Meadowbrooke'), Js('Meadowcove'), Js('Meadowgrove'), Js('Meadowland'), Js('Melody'), Js('Mistwood'), Js('Misty Grove'), Js('Misty River'), Js('Moonlight'), Js('Moonshadow'), Js('Moonshine'), Js('Mooseridge'), Js('Morning Glory'), Js('Morning Star'), Js('Mossy Boulder'), Js('Mossy Cobble'), Js('Mossy Oak'), Js('Mossy Pine'), Js('Mossy Rock'), Js('Mountain Ridge'), Js('Mountain Shadow'), Js('Mountain View'), Js('Mountainridge'), Js('Mustang'), Js('Mystic Hills'), Js('New Dawn'), Js('New Hope'), Js('New Morning'), Js('New Spring'), Js('Nightfall'), Js('Nightingale'), Js('Nightowl'), Js('Northwind'), Js('Oak Ridge'), Js('Oak Springs'), Js('Oak Valley'), Js('Oak Wood'), Js('Oakey Dokey'), Js('Oasis'), Js('Old Stone'), Js('Old Town'), Js('Owlfeather'), Js('Paradise'), Js('Peach Tree'), Js('Pegasus'), Js('Phoenix'), Js('Piece of Heaven'), Js('Pine'), Js('Pine Hollow'), Js('Pine Springs'), Js('Pine Valley'), Js('Pinecone Grove'), Js('Pinewood'), Js('Pitchfork'), Js('Pleasant Knoll'), Js('Pleasant View'), Js('Poison Ivy'), Js('Prairie'), Js('Prairie Hills'), Js('Precious Stone'), Js('Pumpkin Patch'), Js('Quarter Mile'), Js('Rainbow'), Js('Rainbow Hill'), Js('Rainbow Ridge'), Js('Rattlesnake'), Js('Ravenwood'), Js('Rebirth'), Js('Red Dog'), Js('Red Mountain'), Js('Red Pine'), Js('Red River'), Js('Red Robin'), Js('Rise and Shine'), Js('River Hallow'), Js('Riverrock'), Js('Riverview'), Js('Roadrunner'), Js('Robinwood'), Js('Rock Bottom'), Js('Rolling Hills'), Js('Rolling Moss'), Js('Rolling Oak'), Js('Rolling Stone'), Js('Rooster'), Js('Rose Petal'), Js('Rosebush'), Js('Rosewood'), Js('Rusty Bucket'), Js('Serenity'), Js('Setting Sun'), Js('Shadow Ridge'), Js('Shady Oaks'), Js('Shooting Star'), Js('Silver Tree'), Js('Silverbell'), Js('Silversage'), Js('Sleeping Hills'), Js('Sleepy Hollow'), Js('Small Paws'), Js('Small Wonders'), Js('Small World'), Js('Southwind'), Js('Spring Blossom'), Js('Spring Fountain'), Js('Stallion'), Js('Starwood'), Js('Stone Valley'), Js('Straight Arrow'), Js('Strawberry Mountain'), Js('Strawberry Valley'), Js('Sunset'), Js('Sunshine'), Js('Swan Lake'), Js('Sweet Dreams'), Js('Talking Tree'), Js('Talking Trees'), Js('Tall Oaks'), Js('Thistleberry'), Js('Thunder Mountain'), Js('Thunder Valley'), Js('Tranquility'), Js('Tumbleweed'), Js('Turning Point'), Js('Twisted Pine'), Js('Two Pines'), Js('Virgin Valley'), Js('Walnut Grove'), Js('Waterfall'), Js('Weeping Willow'), Js('Westwood'), Js('Whispering Willow'), Js('Whisperwind'), Js('White Oak'), Js('White Stag'), Js('White Willow'), Js('Whitewater'), Js('Wild Horse'), Js('Wildflower'), Js('Willow Creek'), Js('Willowbranch'), Js('Windswept'), Js('Windy Oaks'), Js('Windy Willows'), Js('Yew Valley')]))
var.put('names2', Js([Js('Acres'), Js('Estate'), Js('Farm'), Js('Farms'), Js('Range'), Js('Farmstead'), Js('Fields'), Js('Gardens'), Js('Grange'), Js('Lands'), Js('Meadow'), Js('Nursery'), Js('Orchard'), Js('Pastures'), Js('Ranch'), Js('Vineyard')]))
pass
pass


# Add lib to the module scope
farmNames = var.to_python()