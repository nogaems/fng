__all__ = ['myLittlePony']

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
    var.registers(['names2', 'type', 'tp', 'names3', 'names1', 'result'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', Js([Js('Blueberry'), Js('Twinkletoes'), Js('Starfish'), Js('Nettlekiss'), Js('Hazelblossom'), Js('Dazzleflash'), Js('Buttercup'), Js('Bubblegum'), Js('Cherry Blossom'), Js('Snowflake'), Js('Water Lilly'), Js('Twinkle Star'), Js('Saffron'), Js('Pumpkin'), Js('Cinnamon Twirl'), Js('Sweetie Pie'), Js('Cutie Pie'), Js('Celeste'), Js('Rose Petal'), Js('Sugar Song'), Js('Honey Bee'), Js('Scarlet'), Js('Obsidia'), Js('Lollipop'), Js('Sparkle'), Js('Dahlia'), Js('Lucy Light'), Js('Lavender'), Js('Orchid Jewel'), Js('Sapphire'), Js('Sapphire Swing'), Js('Scarlet Harmony'), Js('Sapphire Sunlight'), Js('Lunar Candy'), Js('Midnight Harmony'), Js('Violet Glow'), Js('Velvet Love'), Js('Sapphire Daisy'), Js('Fluffy Candy'), Js('Fluffy Star'), Js('Rainbow Dawn'), Js('Pearl Petunia'), Js('Caramel Candy'), Js('Velvet Kisses'), Js('Ruby Aurora'), Js('Dew Drop'), Js('Solar Kisses'), Js('Ivy Jewel'), Js('Emerald Aura'), Js('Violet Sparkle'), Js('Violet Rain'), Js('Strawberry Fashion'), Js('Ivory Fire'), Js('Shadow Flower'), Js('Delilah Dusk'), Js('Velvet Cupcake'), Js('Star Eyes'), Js('Celestial Song'), Js('Celestial Snowflake'), Js('Snowy Blossom'), Js('Azure Moon'), Js('Azure Shadow'), Js('Mythic Diamond'), Js('Sapphire Flower'), Js('Lunar Flower'), Js('Sapphire Moonlight'), Js('Aqua Lilly'), Js('Lillypad Love'), Js('Lila Love'), Js('Emerald Snow'), Js('Sugar Spice'), Js('Chocolate Harmony'), Js('Electric Harmony'), Js('Ebony Moon'), Js('River Breeze'), Js('Ebony Breeze'), Js('Crystal Rose'), Js('Diamond Blossom'), Js('Ice Blossom'), Js('Phantasia'), Js('Starry Night'), Js('Moon Petal'), Js('Emerald Dream'), Js('Sandy Shadow'), Js('Ivory Charm'), Js('Lucky Star'), Js('Lucky Lucy'), Js('Ocean Breeze'), Js('Cherry Berry'), Js('Caramel Smooch'), Js('Caramel Kisses'), Js('Amethyst Rose'), Js('Lunar Love'), Js('Scarlet Shadow'), Js('Mythic Fashion'), Js('Little Harmony'), Js('Little Snowflake'), Js('Starry Diamond'), Js('Starry Swirl'), Js('Nightlight Nourish'), Js('Honey Cake'), Js('Amber Night'), Js('Amber Gem'), Js('Flawless Gem'), Js('Twilight Snowflake'), Js('Fluffy Wings')]))
        var.put('names2', Js([Js('Amber'), Js('Amethyst'), Js('Aqua'), Js('Azure'), Js('Caramel'), Js('Celestial'), Js('Cherry'), Js('Chocolate'), Js('Cinnamon'), Js('Crystal'), Js('Cutie'), Js('Delilah'), Js('Dew'), Js('Diamond'), Js('Ebony'), Js('Electric'), Js('Emerald'), Js('Flawless'), Js('Fluffy'), Js('Honey'), Js('Ice'), Js('Ivory'), Js('Ivy'), Js('Lila'), Js('Lillypad'), Js('Little'), Js('Lucky'), Js('Lucy'), Js('Lunar'), Js('Midnight'), Js('Moon'), Js('Mythic'), Js('Nightlight'), Js('Ocean'), Js('Orchid'), Js('Pearl'), Js('Rainbow'), Js('River'), Js('Rose'), Js('Ruby'), Js('Sandy'), Js('Sapphire'), Js('Scarlet'), Js('Shadow'), Js('Snowy'), Js('Solar'), Js('Star'), Js('Starry'), Js('Strawberry'), Js('Sugar'), Js('Sweetie'), Js('Twilight'), Js('Twinkle'), Js('Velvet'), Js('Violet'), Js('Water')]))
        var.put('names3', Js([Js('Aura'), Js('Aurora'), Js('Bee'), Js('Berry'), Js('Blossom'), Js('Breeze'), Js('Cake'), Js('Candy'), Js('Charm'), Js('Cupcake'), Js('Daisy'), Js('Dawn'), Js('Diamond'), Js('Dream'), Js('Drop'), Js('Dusk'), Js('Eyes'), Js('Fashion'), Js('Fire'), Js('Flower'), Js('Gem'), Js('Glow'), Js('Harmony'), Js('Jewel'), Js('Kisses'), Js('Light'), Js('Lilly'), Js('Love'), Js('Moon'), Js('Moonlight'), Js('Night'), Js('Nourish'), Js('Petal'), Js('Petunia'), Js('Pie'), Js('Rain'), Js('Rose'), Js('Shadow'), Js('Smooch'), Js('Snow'), Js('Snowflake'), Js('Song'), Js('Sparkle'), Js('Spice'), Js('Star'), Js('Sunlight'), Js('Swing'), Js('Swirl'), Js('Twirl'), Js('Wings')]))
    else:
        if PyJsStrictEq(var.get('tp'),Js(2.0)):
            var.put('names1', Js([Js('Blueberry'), Js('Twinkletoes'), Js('Starfish'), Js('Nettlekiss'), Js('Hazelblossom'), Js('Dazzleflash'), Js('Anomaly'), Js('Applesauce'), Js('Blitz'), Js('Blue Blanket'), Js('Brushed Light'), Js('Buttons'), Js('Cheery Leap'), Js('Coco-Nut'), Js('Cookie Dough'), Js('Cupcake'), Js('Dancing Star'), Js('Dark Heart'), Js('Dark Style'), Js('Dark Vision'), Js('Fancy Hooves'), Js('Firefly'), Js('Flawless Beat'), Js('Frost Wing'), Js('Frostblossom'), Js('Frozen Hoof'), Js('Fruitcake'), Js('Full Moon'), Js('Golden Moon'), Js('Justice'), Js('Lightning Star'), Js('Liquorice'), Js('Little Hoof'), Js('Little Note'), Js('Looney'), Js('Lucky'), Js('Lucky Prize'), Js('Lucky Shadow'), Js('Lucky Star'), Js('Lunar Dash'), Js('Lunar Fury'), Js('Magic Tinker'), Js('Marble Mystery'), Js('Midnight Gem'), Js('Midnight Meteor'), Js('Midnight Might'), Js('Midnight Sapphire'), Js('Midnight Solo'), Js('Midnight Sparkle'), Js('Midnight Star'), Js('Moondance'), Js('Moondust'), Js('Moonshadow'), Js('Morning Haste'), Js('Mystic Manes'), Js('Mythic Wish'), Js('Ocean Breeze'), Js('Oddity'), Js('Pebbles'), Js('Peppermint Spice'), Js('Popcorn'), Js('Quirk Smirk'), Js('Rainbow Gadget'), Js('Rapid Shadow'), Js('Rocking Star'), Js('Sapphire Moonlight'), Js('Sapphire Sparkle'), Js('Scarlet Scar'), Js('Shadow Charm'), Js('Shadow Eyes'), Js('Shadow Fang'), Js('Shadow Hoof'), Js('Shining Star'), Js('Shooting Star'), Js('Shuffle Step'), Js('Silent Step'), Js('Silver Manes'), Js('Silver Shadow'), Js('Silver Song'), Js('Silver Stream'), Js('Silver Sunset'), Js('Silver Sunshine'), Js('Sky Chaser'), Js('Sky Star'), Js('Smooch'), Js('Smooth Shadow'), Js('Sneezy'), Js('Snow Star'), Js('Star Eyes'), Js('Starburst'), Js('Stone Steps'), Js('Straight Arrow'), Js('Sugar Cube'), Js('Sugardash'), Js('Sunrise'), Js('Sunshine'), Js('Sunshine Shy'), Js('Sweet Tooth'), Js('Swift Mist'), Js('Tiny'), Js('Tiny Thimble'), Js('Tiny Tumbler'), Js('Twinkle Toes'), Js('Wiggles'), Js('Winternight'), Js('Wintersong')]))
            var.put('names2', Js([Js('Blue'), Js('Brushed'), Js('Cheery'), Js('Cookie'), Js('Dancing'), Js('Dark'), Js('Fancy'), Js('Flawless'), Js('Frost'), Js('Frozen'), Js('Full'), Js('Golden'), Js('Lightning'), Js('Little'), Js('Lucky'), Js('Lunar'), Js('Magic'), Js('Marble'), Js('Midnight'), Js('Morning'), Js('Mystic'), Js('Mythic'), Js('Ocean'), Js('Peppermint'), Js('Quirk'), Js('Rainbow'), Js('Rapid'), Js('Rocking'), Js('Sapphire'), Js('Scarlet'), Js('Shadow'), Js('Shining'), Js('Shooting'), Js('Shuffle'), Js('Silent'), Js('Silver'), Js('Sky'), Js('Smooth'), Js('Snow'), Js('Star'), Js('Stone'), Js('Straight'), Js('Sugar'), Js('Sunshine'), Js('Sweet'), Js('Swift'), Js('Tiny'), Js('Twinkle')]))
            var.put('names3', Js([Js('Arrow'), Js('Beat'), Js('Blanket'), Js('Breeze'), Js('Charm'), Js('Chaser'), Js('Cube'), Js('Dash'), Js('Dough'), Js('Eyes'), Js('Fang'), Js('Fury'), Js('Gadget'), Js('Gem'), Js('Haste'), Js('Heart'), Js('Hoof'), Js('Hooves'), Js('Leap'), Js('Light'), Js('Manes'), Js('Meteor'), Js('Might'), Js('Mist'), Js('Moon'), Js('Moonlight'), Js('Mystery'), Js('Note'), Js('Prize'), Js('Sapphire'), Js('Scar'), Js('Shadow'), Js('Shy'), Js('Smirk'), Js('Solo'), Js('Song'), Js('Sparkle'), Js('Spice'), Js('Star'), Js('Step'), Js('Steps'), Js('Stream'), Js('Style'), Js('Sunset'), Js('Sunshine'), Js('Thimble'), Js('Tinker'), Js('Toes'), Js('Tooth'), Js('Tumbler'), Js('Vision'), Js('Wing'), Js('Wish')]))
        else:
            var.put('names1', Js([Js('Blueberry'), Js('Twinkletoes'), Js('Starfish'), Js('Nettlekiss'), Js('Hazelblossom'), Js('Dazzleflash'), Js('Apple Specter'), Js('Applesauce'), Js('Arctic Breeze'), Js('Astral Thunder'), Js('Berry White'), Js('Big B'), Js('Blaze'), Js('Bouncer'), Js('Brisk Bronco'), Js('Bulky Buster'), Js('Caramel Crunch'), Js('Cloud Sweeper'), Js('Cobalt'), Js('Coco-Nut'), Js('Colt Feet'), Js('Colt Ice'), Js('Comet Flash'), Js('Crimson Mask'), Js('Crimson Moon'), Js('Crimson Vision'), Js('Dapper Dash'), Js('Dapper Force'), Js('Dark Meadow'), Js('Dark Snow'), Js('Dark Specter'), Js('Duke Bristle'), Js('Duke Starlight'), Js('Duke Venture'), Js('Emerald Mask'), Js('Fancy Hooves'), Js('Flawless Victory'), Js('Golden Flash'), Js('Ivory Spark'), Js('Jackpot Star'), Js('Jade Jester'), Js('Last Legacy'), Js('Little Snow'), Js('Lost Legacy'), Js('Marble Mark'), Js('Master Facade'), Js('Master Metal'), Js('Maverick'), Js('Midnight Hero'), Js('Mister Bristle'), Js('Mister Dare'), Js('Moonlight Hunter'), Js('Moonshadow Colt'), Js('Moonshadow Sprint'), Js('Moonstone Mustang'), Js('Mythic Haze'), Js('Night Twister'), Js('Nimble Force'), Js('Onyx'), Js('Onyx Armor'), Js('Onyx Bolt'), Js('Onyx Justice'), Js('Onyx Star'), Js('Platinum Night'), Js('Prince Prickle'), Js('Raggedy Randy'), Js('Rapid Shadow'), Js('Rocky Road'), Js('Sapphire Spirit'), Js('Sapphire Twister'), Js('Shadow Mark'), Js('Shining Star'), Js('Silver Mane'), Js('Silver Shine'), Js('Silver Spirit'), Js('Silver Whiskers'), Js('Sky Chaser'), Js('Sky Scraper'), Js('Smoky'), Js('Soaring Surfer'), Js('Solar Comet'), Js('Star Chaser'), Js('Star Whistle'), Js('Steel Mustang'), Js('Steel Stud'), Js('Straight Arrow'), Js('Sundance'), Js('Sunrise Storm'), Js('Sweet Sorbet'), Js('Swift Bolt'), Js('Tango'), Js('Thunder Bolt'), Js('Thunder Charge'), Js('Thunder Colt'), Js('Thunder Spark'), Js('Thunder Tail'), Js('Thunder Wing'), Js('Thunderhoof'), Js('Tiny Thunder'), Js('Twilight Thunder'), Js('Velvet Chaser'), Js('Wild Ace'), Js('Wild Strikes'), Js('Winter Gust'), Js('Yellow Rock')]))
            var.put('names2', Js([Js('Apple'), Js('Arctic'), Js('Astral'), Js('Berry'), Js('Brisk'), Js('Bulky'), Js('Caramel'), Js('Cloud'), Js('Colt'), Js('Comet'), Js('Crimson'), Js('Dapper'), Js('Dark'), Js('Duke'), Js('Emerald'), Js('Fancy'), Js('Flawless'), Js('Golden'), Js('Ivory'), Js('Jackpot'), Js('Jade'), Js('Little'), Js('Marble'), Js('Master'), Js('Midnight'), Js('Mister'), Js('Moonlight'), Js('Moonshadow'), Js('Moonstone'), Js('Mythic'), Js('Night'), Js('Nimble'), Js('Onyx'), Js('Platinum'), Js('Prince'), Js('Rapid'), Js('Rocky'), Js('Sapphire'), Js('Shadow'), Js('Shining'), Js('Silver'), Js('Sky'), Js('Solar'), Js('Star'), Js('Steel'), Js('Straight'), Js('Sunrise'), Js('Sweet'), Js('Swift'), Js('Thunder'), Js('Tiny'), Js('Twilight'), Js('Velvet'), Js('Wild'), Js('Winter'), Js('Yellow')]))
            var.put('names3', Js([Js('Ace'), Js('Armor'), Js('Arrow'), Js('Bolt'), Js('Breeze'), Js('Bristle'), Js('Bronco'), Js('Buster'), Js('Charge'), Js('Chaser'), Js('Colt'), Js('Comet'), Js('Crunch'), Js('Dare'), Js('Dash'), Js('Facade'), Js('Feet'), Js('Flash'), Js('Force'), Js('Gust'), Js('Haze'), Js('Hero'), Js('Hooves'), Js('Hunter'), Js('Ice'), Js('Jester'), Js('Justice'), Js('Mane'), Js('Mark'), Js('Mask'), Js('Meadow'), Js('Metal'), Js('Moon'), Js('Mustang'), Js('Night'), Js('Prickle'), Js('Road'), Js('Rock'), Js('Shadow'), Js('Shine'), Js('Snow'), Js('Sorbet'), Js('Spark'), Js('Specter'), Js('Spirit'), Js('Sprint'), Js('Star'), Js('Starlight'), Js('Storm'), Js('Strikes'), Js('Sweeper'), Js('Tail'), Js('Thunder'), Js('Twister'), Js('Venture'), Js('Victory'), Js('Vision'), Js('Whiskers'), Js('Whistle'), Js('White'), Js('Wing')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('names', var.get('names1').get(var.get('rnd0')))
            else:
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', ((var.get('names2').get(var.get('rnd0'))+Js(' '))+var.get('names3').get(var.get('rnd1'))))
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
myLittlePony = var.to_python()