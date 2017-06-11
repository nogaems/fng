__all__ = ['cityNicknames']

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
    var.put('nm1', Js([Js('Alcohol'), Js('Ancient'), Js('Angelic'), Js('Angry'), Js('Art'), Js('Autumn'), Js('Awkward'), Js('Barren'), Js('Beast'), Js('Big'), Js('Bird'), Js('Bleak'), Js('Blissful'), Js('Blossom'), Js('Blushing'), Js('Bold'), Js('Book'), Js('Brave'), Js('Bright'), Js('Brilliant'), Js('Broken'), Js('Bronze'), Js('Burning'), Js('Butterfly'), Js('Careful'), Js('Careless'), Js('Cat'), Js('Chameleon'), Js('Champion'), Js('Chaotic'), Js('Charming'), Js('Cheery'), Js('Cherry'), Js('Classic'), Js('Cloudy'), Js('Cold'), Js('College'), Js('Colorful'), Js('Copper'), Js('Corrupt'), Js('Crazy'), Js('Crime'), Js('Crimson'), Js('Crisp'), Js('Crossroad'), Js('Crowded'), Js('Crown'), Js('Cruel'), Js('Crystal'), Js('Culture'), Js('Dark'), Js('Darling'), Js('Dead'), Js('Defiant'), Js('Delightful'), Js('Democratic'), Js('Digital'), Js('Dirty'), Js('Discrete'), Js('Dog'), Js('Dream'), Js('Dreaming'), Js('Dry'), Js('Earnest'), Js('Ebon'), Js('Elderly'), Js('Electric'), Js('Elegant'), Js('Emerald'), Js('Empty'), Js('Enchanted'), Js('Enchanting'), Js('Enduring'), Js('Esteemed'), Js('Eternal'), Js('Evergreen'), Js('Exalted'), Js('Excited'), Js('Exotic'), Js('Expert'), Js('Faint'), Js('Fair'), Js('False'), Js('Fantastic'), Js('Fantasy'), Js('Farming'), Js('Fashion'), Js('Fearless'), Js('Fish'), Js('Flag'), Js('Flawless'), Js('Floating'), Js('Flower'), Js('Fog'), Js('Forbidden'), Js('Forsaken'), Js('Fortune'), Js('Fountain'), Js('Free'), Js('Fresh'), Js('Frozen'), Js('Fruit'), Js('Funny'), Js('Future'), Js('Garden'), Js('Gateway'), Js('Gem'), Js('Generous'), Js('Gentle'), Js('Ghost'), Js('Giant'), Js('Gifted'), Js('Giving'), Js('Glass'), Js('Glorious'), Js('Golden'), Js('Good'), Js('Graceful'), Js('Grand'), Js('Granite'), Js('Great'), Js('Greedy'), Js('Green'), Js('Griffin'), Js('Grim'), Js('Half'), Js('Happy'), Js('Harbor'), Js('Health'), Js('Hearty'), Js('Herb'), Js('Hill'), Js('Hollow'), Js('Holy'), Js('Honest'), Js('Honor'), Js('Hungry'), Js('Idle'), Js('Illusion'), Js('Imperial'), Js('Infinite'), Js('Innocent'), Js('Intelligent'), Js('Invincible'), Js('Iron'), Js('Ivory'), Js('Jade'), Js('Jaded'), Js('Jewel'), Js('Jewelry'), Js('Junior'), Js('Justice'), Js('Kind'), Js('Lasting'), Js('Lawful'), Js('Lazy'), Js('Light'), Js('Lily'), Js('Literature'), Js('Little'), Js('Little Big'), Js('Lonely'), Js('Long'), Js('Lovable'), Js('Love'), Js('Loyal'), Js('Lucky'), Js('Mad'), Js('Magic'), Js('Majestic'), Js('Marble'), Js('Marsh'), Js('Massive'), Js('Mellow'), Js('Merry'), Js('Mighty'), Js('Minor'), Js('Misty'), Js('Model'), Js('Modest'), Js('Molten'), Js('Money'), Js('Moon'), Js('Mountain'), Js('Music'), Js('Mysterious'), Js('Mystery'), Js('Mystic'), Js('Mythical'), Js('Narrow'), Js('Nature'), Js('New'), Js('Oasis'), Js('Obsidian'), Js('Onyx'), Js('Orchard'), Js('Orchid'), Js('Ordinary'), Js('Ornate'), Js('Parallel'), Js('Peace'), Js('Pearl'), Js("People's"), Js('Perfume'), Js('Perfumed'), Js('Pet'), Js('Petal'), Js('Phantom'), Js('Phoenix'), Js('Pink'), Js('Plastic'), Js('Pleasant'), Js('Poetry'), Js('Polite'), Js('Precious'), Js('Prime'), Js('Pristine'), Js('Proud'), Js('Quiet'), Js('Rainbow'), Js('Red'), Js('Remote'), Js('River'), Js('Rocky'), Js('Rose'), Js('Round'), Js('Royal'), Js('Ruby'), Js('Rumbling'), Js('Safe'), Js('Sapphire'), Js('Scented'), Js('Serene'), Js('Shadow'), Js('Shallow'), Js('Shimmering'), Js('Shy'), Js('Silent'), Js('Silver'), Js('Sin'), Js('Sleeping'), Js('Sleepwalking'), Js('Smoke'), Js('Smooth'), Js('Song'), Js('Spice'), Js('Spicy'), Js('Spirit'), Js('Spring'), Js('Square'), Js('Star'), Js('Steel'), Js('Storm'), Js('Stormy'), Js('Strange'), Js('Strawberry'), Js('Style'), Js('Stylish'), Js('Summer'), Js('Sunny'), Js('Super'), Js('Tasty'), Js('Tender'), Js('Terrible'), Js('Thunder'), Js('Tinted'), Js('Tiny'), Js('Tired'), Js('Tragedy'), Js('Tranquil'), Js('Tree'), Js('Trembling'), Js('True'), Js('Trusty'), Js('Turbulent'), Js('Twin'), Js('Unholy'), Js('Uniform'), Js('United'), Js('Unlucky'), Js('Upbeat'), Js('Velvet'), Js('Vermin'), Js('Vibrant'), Js('Violet'), Js('Vision'), Js('Vivid'), Js('Warm'), Js('Water'), Js('Welcome'), Js('Wet'), Js('White'), Js('Wicked'), Js('Wild'), Js('Windy'), Js('Winter'), Js('Wise'), Js('Wonder'), Js('Wooden'), Js('Worn'), Js('Young')]))
    var.put('nm2', Js([Js('Alcohol'), Js('Amusement'), Js('Ancients'), Js('Angels'), Js('Animals'), Js('Antiquity'), Js('Art'), Js('Autumn'), Js('Beasts'), Js('Birds'), Js('Bliss'), Js('Blossoms'), Js('Books'), Js('Bravery'), Js('Bronze'), Js('Butterflies'), Js('Cats'), Js('Celebration'), Js('Champions'), Js('Chaos'), Js('Charm'), Js('Class'), Js('Clouds'), Js('Cold'), Js('Colors'), Js('Comforts'), Js('Competition'), Js('Copper'), Js('Crime'), Js('Crimson'), Js('Crowds'), Js('Crowns'), Js('Crystal'), Js('Crystals'), Js('Culture'), Js('Daydreams'), Js('Delights'), Js('Dirt'), Js('Dogs'), Js('Dreamers'), Js('Dreams'), Js('Drinks'), Js('Ebon'), Js('Elegance'), Js('Emeralds'), Js('Enchantments'), Js('Excellence'), Js('Fantasy'), Js('Farms'), Js('Fashion'), Js('Flowers'), Js('Fog'), Js('Food'), Js('Fortitude'), Js('Fortune'), Js('Fountains'), Js('Fruits'), Js('Futures'), Js('Games'), Js('Gardens'), Js('Gates'), Js('Gems'), Js('Ghosts'), Js('Giants'), Js('Gifts'), Js('Glass'), Js('Gluttony'), Js('Gold'), Js('Grace'), Js('Grandure'), Js('Granite'), Js('Greed'), Js('Green'), Js('Happiness'), Js('Harmony'), Js('Health'), Js('History'), Js('Honesty'), Js('Honor'), Js('Hunger'), Js('Illusions'), Js('Infinity'), Js('Innocence'), Js('Insects'), Js('Iron'), Js('Ivory'), Js('Jade'), Js('Jewelry'), Js('Jewels'), Js('Joy'), Js('Justice'), Js('Laws'), Js('Lights'), Js('Lilies'), Js('Literature'), Js('Love'), Js('Loyalty'), Js('Luck'), Js('Luxury'), Js('Magic'), Js('Marble'), Js('Marvel'), Js('Merit'), Js('Might'), Js('Mist'), Js('Modesty'), Js('Money'), Js('Mountains'), Js('Music'), Js('Mystery'), Js('Myths'), Js('Nature'), Js('Obsidian'), Js('Onyx'), Js('Orchards'), Js('Orchids'), Js('Peace'), Js('Perfume'), Js('Petals'), Js('Plastic'), Js('Pleasure'), Js('Poems'), Js('Poetry'), Js('Pride'), Js('Rainbows'), Js('Riddles'), Js('Rivers'), Js('Roses'), Js('Royalty'), Js('Rubies'), Js('Sapphires'), Js('Scents'), Js('Serenity'), Js('Shadows'), Js('Silence'), Js('Silver'), Js('Sins'), Js('Sleep'), Js('Smoke'), Js('Solitude'), Js('Songs'), Js('Souls'), Js('Spice'), Js('Spirit'), Js('Spirits'), Js('Spring'), Js('Stars'), Js('Steel'), Js('Storms'), Js('Style'), Js('Summer'), Js('Tastes'), Js('Thrills'), Js('Thunder'), Js('Tragedy'), Js('Tranquility'), Js('Trees'), Js('Trust'), Js('Unity'), Js('Values'), Js('Vermin'), Js('Virtues'), Js('Visions'), Js('Water'), Js('Waterfalls'), Js('Welcomes'), Js('Winds'), Js('Wisdom'), Js('Wonders'), Js('Wood'), Js('Yesteryear'), Js('Zest')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (Js('The City of ')+var.get('nm2').get(var.get('rnd'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' City')))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
cityNicknames = var.to_python()