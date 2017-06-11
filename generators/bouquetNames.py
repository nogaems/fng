__all__ = ['bouquetNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
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
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Amber Admiration'), Js('Amber Adoration'), Js('Amber Amazement'), Js('Amber Amour'), Js('Amber Awe'), Js('Amour'), Js('Angelwing'), Js('Autumn Harvest'), Js('Autumn Morning'), Js('Be Mine'), Js('Be My Valentine'), Js('Beautiful Blossoms'), Js('Beauty'), Js('Best Wishes'), Js('Blessed Blossoms'), Js('Blissful Blossoms'), Js('Blooming Blues'), Js('Blushing Blossoms'), Js('Brilliance'), Js('Caribbean Breeze'), Js('Caribbean Scents'), Js('Celebration Time'), Js('Celebrations'), Js('Cherry Blossom Cherish'), Js('Cherry Blossoms'), Js('Chocolate Love'), Js('Colorful Spring'), Js('Colorful Summer'), Js('Congratulations'), Js('Cool Blue'), Js('Country Garden'), Js('Country Meadow'), Js('Country Scents'), Js('Crimson Crests'), Js('Crystal Chrysanthemums'), Js('Crystal Coral'), Js('Crystal Curiosity'), Js('Dahlia Dominance'), Js('Daydreams'), Js('Diamond Darlings'), Js('Diamond Devotion'), Js('Dots of Love'), Js('Dreamland'), Js('Easy Green'), Js('Elegant Amber'), Js('Emerald Elegance'), Js('Eternal Emerald'), Js('Eternal Summer'), Js('Exalted Emerald'), Js('Fall in Love'), Js('Fancy Floral'), Js('Fancy Fruits'), Js('Fascination'), Js('Fiery Red'), Js('First Date'), Js('First Impression'), Js('Floral Fantasy'), Js('Flowers of Love'), Js('For Mom'), Js('Forest Fantasy'), Js('Forest Flavor'), Js('Forest Fresh'), Js('Forever Spring'), Js('Friendship'), Js('Fruits of Love'), Js('Fruits of Spring'), Js('Fruits of Summer'), Js('Fruits of the Fields'), Js('Fruits of the Forest'), Js('Garden Secrets'), Js('Golden Times'), Js('Grandeur'), Js('Happiness'), Js('Harmony'), Js('Hidden Garden'), Js('Holly Harmony'), Js('Home Sweet Home'), Js('I Miss You'), Js('I Missed You'), Js("It's a Boy"), Js("It's a Girl"), Js('Jade Joy'), Js('Joy'), Js('Just For You'), Js('Just Peachy'), Js('Lavender Love'), Js('Lavish Luster'), Js('Lily Love'), Js('Love Blossoms'), Js('Love is ..'), Js('Lullaby'), Js('Lust'), Js('Lustrous Leaves'), Js('Magnolia Magnificence'), Js('Majesty'), Js('Marvels'), Js('Mellow Yellow'), Js('Midnight Magic'), Js('Midsummer Night'), Js('Misty Magic'), Js('Morning Dew'), Js('Morning Magic'), Js('Motherly Love'), Js('My Valentine'), Js('Oriental Love'), Js('Oriental Scents'), Js('Oriental Wonders'), Js('Ornate Orchids'), Js('Passion'), Js('Pastel Passion'), Js('Peace of Mind'), Js('Peachy Passion'), Js('Peachy Peace'), Js('Petal Parade'), Js('Petal Party'), Js('Phenomenon'), Js('Pink Passion'), Js('Pink Perfection'), Js('Pretty In Pink'), Js('Pretty Passion'), Js('Pretty Petals'), Js('Pretty in Pink'), Js('Purple Paramour'), Js('Radiance'), Js('Rainbow Connection'), Js('Rainbow of Love'), Js('Red Romance'), Js('Regal Roses'), Js('Rose Radiance'), Js('Ruby Christmas'), Js('Ruby Radiance'), Js('Sapphire Scents'), Js('Sapphire Splendor'), Js('Sapphire Style'), Js('Sapphire Sweethearts'), Js('Scented Dream'), Js('Scented Love'), Js('Scents of Heaven'), Js('Scents of the Rainforest'), Js('Serenity'), Js('Snow White'), Js('Spectacles'), Js('Spring Balance'), Js('Spring Beauty'), Js('Spring Breeze'), Js('Spring Delight'), Js('Spring Dreams'), Js('Spring Fresh'), Js('Spring Garden'), Js('Spring Glory'), Js('Spring Glow'), Js('Spring Luster'), Js('Spring Magic'), Js('Spring Meadow'), Js('Spring Miracles'), Js('Spring Morning'), Js('Spring Scents'), Js('Spring Sights'), Js('Spring Surprise'), Js('Spring Vibes'), Js('Spring Whispers'), Js('Spring to Summer'), Js("Spring's First"), Js('Stylish Spring'), Js('Summer Balance'), Js('Summer Bells'), Js('Summer Breeze'), Js('Summer Dreams'), Js('Summer Evening'), Js('Summer Glory'), Js('Summer Glow'), Js('Summer Harvest'), Js('Summer Hush'), Js('Summer Love'), Js('Summer Loving'), Js('Summer Magic'), Js('Summer Majesty'), Js('Summer Meadow'), Js('Summer Miracles'), Js('Summer Morning'), Js('Summer Phenomenon'), Js('Summer Pleasures'), Js('Summer Sensations'), Js('Summer Shine'), Js('Summer Sights'), Js('Summer Spectacles'), Js('Summer Splendor'), Js('Summer Style'), Js('Summer Sun'), Js('Summer Surprise'), Js('Summer Warmth'), Js('Summer to Autumn'), Js("Summer's First"), Js("Summer's Grace"), Js('Sunshine'), Js('Surprise'), Js('Sweet Honey'), Js('Sweetheart'), Js('Tender Tulips'), Js('Thank You'), Js('Thank You Very Much'), Js('Thinking of You'), Js('Tranquility'), Js('Tropical Breeze'), Js('Tropical Scents'), Js('Tropical Summer'), Js('Valley Fruits'), Js('Valley Scents'), Js('Velvet Fascination'), Js('Velvet Valley'), Js('Velvet Violet'), Js('Wedding Bells'), Js('Welcome Back'), Js('White Wonders'), Js('Winter Bells'), Js('Winter Glow'), Js('Winter Magic'), Js('Winter Marvel'), Js('Winter Phenomenon'), Js('Winter Sensations'), Js('Winter Spectacles'), Js('Winter Vibes'), Js('Winter Whispers'), Js('Winter White'), Js('Winter Wonders'), Js('Winter to Spring'), Js("Winter's Grace"), Js('Yellow Fever'), Js('You and I'), Js("You're My Angel"), Js("You're the one")]))
pass
pass


# Add lib to the module scope
bouquetNames = var.to_python()