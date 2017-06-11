__all__ = ['colorNames']

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
            var.put('names', ((var.get('nm2').get(var.get('rnd2'))+Js(' '))+var.get('nm1').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Almond'), Js('Amaranth'), Js('Amber'), Js('Amethyst'), Js('Aquamarine'), Js('Auburn'), Js('Azure'), Js('Beige'), Js('Black'), Js('Blond'), Js('Blue'), Js('Bone'), Js('Brass'), Js('Bronze'), Js('Brown'), Js('Cerulean'), Js('Cherry'), Js('Chrome'), Js('Coal'), Js('Cobalt'), Js('Coffee'), Js('Coral'), Js('Cream'), Js('Crimson'), Js('Cyan'), Js('Ebony'), Js('Emerald'), Js('Fuchsia'), Js('Gold'), Js('Green'), Js('Grey'), Js('Indigo'), Js('Ivory'), Js('Jade'), Js('Jasmine'), Js('Jasper'), Js('Khaki'), Js('Lava'), Js('Lavender'), Js('Lemon'), Js('Chocolate'), Js('Lilac'), Js('Magenta'), Js('Malachite'), Js('Maroon'), Js('Mauve'), Js('Moss'), Js('Obsidian'), Js('Onyx'), Js('Orange'), Js('Peach'), Js('Pink'), Js('Purple'), Js('Red'), Js('Rose'), Js('Ruby'), Js('Saffron'), Js('Sand'), Js('Sanguine'), Js('Sapphire'), Js('Satin'), Js('Scarlet'), Js('Sienna'), Js('Silver'), Js('Tan'), Js('Teal'), Js('Turquoise'), Js('Ultramarine'), Js('Umber'), Js('Vanilla'), Js('Velvet'), Js('Vermilion'), Js('Violet'), Js('White'), Js('Yellow')]))
var.put('nm2', Js([Js('Abstract'), Js('Abyss'), Js('Abyssal'), Js('Aged'), Js('Ageless'), Js('Airy'), Js('Alien'), Js('Ancient'), Js('Angelic'), Js('Antique'), Js('Archaic'), Js('Arctic'), Js('Argent'), Js('Aristocratic'), Js('Ashy'), Js('Astral'), Js('August'), Js('Aura'), Js('Aurora'), Js('Autumn'), Js('Baby'), Js('Big'), Js('Bland'), Js('Blazing'), Js('Bleached'), Js('Bleak'), Js('Blemished'), Js('Bloated'), Js('Blossom'), Js('Botanic'), Js('Bouncy'), Js('Bright'), Js('Brilliant'), Js('Burned'), Js('Burning'), Js('Burnished'), Js('Caribbean'), Js('Castle'), Js('Celestial'), Js('Charged'), Js('Charming'), Js('Charred'), Js('Classic'), Js('Classy'), Js('Clear'), Js('Cloudy'), Js('Coarse'), Js('Common'), Js('Cool'), Js('Corrupt'), Js('Cosmic'), Js('Crazed'), Js('Crazy'), Js('Cyber'), Js('Dark'), Js('Dawn'), Js('Dazzling'), Js('Deep'), Js('Delicate'), Js('Deluxe'), Js('Dignified'), Js('Dim'), Js('Distorted'), Js('Divine'), Js('Dreary'), Js('Dull'), Js('Dusk'), Js('Dynamic'), Js('Eerie'), Js('Electric'), Js('Empyral'), Js('Enchanting'), Js('Eternal'), Js('Exciting'), Js('Experimental'), Js('Faded'), Js('Faint'), Js('Field'), Js('Fierce'), Js('Fiery'), Js('Flamboyant'), Js('Flaming'), Js('Flawless'), Js('Floral'), Js('Fluid'), Js('Forest'), Js('Freaky'), Js('Fresh'), Js('Frigid'), Js('Frosty'), Js('Frozen'), Js('Fuzzy'), Js('Galactic'), Js('Garden'), Js('Generic'), Js('Generous'), Js('Gentle'), Js('Ghastly'), Js('Ghostly'), Js('Giant'), Js('Glamorous'), Js('Glistening'), Js('Gloomy'), Js('Glorious'), Js('Glossy'), Js('Glowing'), Js('Grim'), Js('Groovy'), Js('Happy'), Js('Harsh'), Js('Harvest'), Js('Herbal'), Js('Hot'), Js('Illuminated'), Js('Immortal'), Js('Imperial'), Js('Imposing'), Js('Intense'), Js('Irresistible'), Js('Joyful'), Js('Jungle'), Js('Lavish'), Js('Light'), Js('Livid'), Js('Loud'), Js('Loving'), Js('Low'), Js('Lucent'), Js('Lucid'), Js('Luminous'), Js('Lush'), Js('Lustrous'), Js('Luxurious'), Js('Magic'), Js('Magical'), Js('Majestic'), Js('Marsh'), Js('Mechanical'), Js('Medieval'), Js('Medium'), Js('Mellow'), Js('Metallic'), Js('Midnight'), Js('Mild'), Js('Misty'), Js('Moderate'), Js('Modern'), Js('Modest'), Js('Monster'), Js('Moonlit'), Js('Mountain'), Js('Murky'), Js('Mystery'), Js('Mystical'), Js('Mythic'), Js('Noble'), Js('Noisy'), Js('Obscure'), Js('Old'), Js('Old-Fashioned'), Js('Ordinary'), Js('Pale'), Js('Paradise'), Js('Parched'), Js('Pastel'), Js('Pasture'), Js('Peaceful'), Js('Pleasant'), Js('Polar'), Js('Polished'), Js('Precious'), Js('Premium'), Js('Primitive'), Js('Proud'), Js('Psychedelic'), Js('Putrid'), Js('Radiant'), Js('Regal'), Js('Rich'), Js('Rigid'), Js('Rough'), Js('Royal'), Js('Rusty'), Js('Seductive'), Js('Shadow'), Js('Silky'), Js('Smooth'), Js('Smoldering'), Js('Soft'), Js('Somber'), Js('Sonic'), Js('Sovereign'), Js('Spectral'), Js('Spicy'), Js('Spring'), Js('Steamy'), Js('Strong'), Js('Sublime'), Js('Summer'), Js('Sunlit'), Js('Sunrise'), Js('Sunset'), Js('Superior'), Js('Supernatural'), Js('Supreme'), Js('Swamp'), Js('Sweet'), Js('Tacky'), Js('Tempting'), Js('Tender'), Js('Timeless'), Js('Tired'), Js('Tranquil'), Js('Tropical'), Js('Twilight'), Js('Undead'), Js('Unsullied'), Js('Vague'), Js('Vampiric'), Js('Vineyard'), Js('Vintage'), Js('Violent'), Js('Virtual'), Js('Vivid'), Js('Volatile'), Js('Washed Out'), Js('Wild'), Js('Wilderness'), Js('Winter'), Js('Youthful')]))
pass
pass


# Add lib to the module scope
colorNames = var.to_python()