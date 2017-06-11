__all__ = ['plazaNames']

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
var.put('nm1', Js([Js('Accolade'), Js('Accomplishment'), Js('Achievement'), Js('Adventure'), Js('Ancestor'), Js('Animus'), Js('Anniversary'), Js('Apex'), Js('Art'), Js('Augury'), Js('Azure'), Js('Blue Moon'), Js('Capitol'), Js('Castle Square'), Js('Cathedral'), Js('Celebration'), Js('Central'), Js('Century'), Js('Ceremony'), Js('Cerulean'), Js("Champions'"), Js('Cherry Blossom'), Js('City Hall'), Js('Civic'), Js('Clover'), Js('Coconut'), Js('Commemoration'), Js('Community'), Js('Conquest'), Js('Crescent'), Js('Crystal'), Js('Daydream'), Js('Delicacy'), Js('Democracy'), Js('Desire'), Js('Devotion'), Js('Diamond'), Js('Discovery'), Js('Divinity'), Js('Dream'), Js('Dreamer'), Js('Duty'), Js('Effigy'), Js('Elegance'), Js('Elemental'), Js('Elysium'), Js('Emerald'), Js('Enchantment'), Js('Epiphany'), Js('Eternity'), Js('Euphony'), Js('Execution'), Js('Exploration'), Js('Fantasy'), Js('Festival'), Js('Firefly'), Js('Fortitude'), Js('Fortune'), Js("Founders'"), Js('Freedom'), Js('Galaxy'), Js('Gemstone'), Js('Glory'), Js('Golden'), Js('Good Omen'), Js('Grand'), Js('Grand Fountain'), Js('Grand Gala'), Js('Grand Harbor'), Js('Grand Market'), Js('Grand Meadow'), Js('Grand Palace'), Js('Grand Sanctum'), Js('Grand Splendor'), Js('Grand Treasure'), Js('Grapevine'), Js('Harbinger'), Js('Harmony'), Js("Heart's"), Js("Heaven's"), Js("Heroes'"), Js('History'), Js('Homage'), Js('Honor'), Js('Hope'), Js('Icewater'), Js('Illumination'), Js('Illusion'), Js('Independence'), Js('Infinity'), Js('Innocence'), Js('Innovation'), Js('Inspiration'), Js('Ivory'), Js('Jubilee'), Js('Justice'), Js('King'), Js('Kinship'), Js('Legion'), Js('Lemontree'), Js('Liberation'), Js('Liberty'), Js('Light'), Js('Lilypad'), Js('Love'), Js("Lovers'"), Js('Loyalty'), Js('Luminus'), Js('Lunar'), Js('Luxury'), Js('Magic'), Js('Majesty'), Js('Marble'), Js('Market'), Js('Marriage'), Js('Marvel'), Js('Melody'), Js('Memorial'), Js('Memory'), Js('Millennium'), Js('Miracle'), Js('Mirage'), Js('Monolith'), Js('Monument'), Js('Moonlight'), Js('Muse'), Js('Myriad'), Js('Mystic'), Js("Nature's"), Js('Nebula'), Js('New Haven'), Js('New Hope'), Js('Obelisk'), Js('Observation'), Js('Obsidian'), Js('Old Town'), Js('Opulence'), Js('Oracle'), Js('Orchard'), Js('Orchestra'), Js('Palm Leaf'), Js('Paradise'), Js('Paragon'), Js('Paramount'), Js('Passion'), Js('Peace Blossom'), Js('Peace Garden'), Js('Peacock'), Js('Pearl'), Js("People's"), Js('Perseverance'), Js('Phantasm'), Js('Phenomenon'), Js('Phoenix'), Js('Pilgrimage'), Js('Pinnacle'), Js('Pioneer'), Js('Pleasantview'), Js('Preservation'), Js('Prism'), Js('Prodigy'), Js('Promise'), Js('Prophecy'), Js('Prosperity'), Js('Public'), Js('Pyramid'), Js('Rainbow'), Js('Rebirth'), Js('Reflection'), Js('Refuge'), Js('Renaissance'), Js('Republic'), Js('Resonance'), Js('Revelation'), Js('Rose Petal'), Js('Royalty'), Js('Ruby'), Js('Sanctuary'), Js('Sanguine'), Js('Sapphire'), Js('Seduction'), Js('Sensation'), Js('Serenity'), Js("Settlers'"), Js('Silk'), Js('Silver'), Js('Silver Moon'), Js('Silver Oak'), Js('Silver Shrine'), Js('Sky'), Js('Snowflake'), Js('Solar'), Js('Songbird'), Js('Spring Gardens'), Js('Starlight'), Js('Statue'), Js('Summer Gardens'), Js('Supremacy'), Js('Sweet Delight'), Js('Sweetheart'), Js('Symphony'), Js('Temple'), Js('Tenacity'), Js('Timeless'), Js('Town Hall'), Js('Tranquility'), Js('Tribulation'), Js('Tribute'), Js('Trinity'), Js('Triumph'), Js('Trophy'), Js('Truth'), Js('Umbrella'), Js('Union'), Js('Unity'), Js('Universe'), Js('University'), Js('Utopia'), Js('Valiance'), Js('Velvet'), Js('Veneration'), Js('Venture'), Js('Vertex'), Js('Victory'), Js('Vigor'), Js('Vineyard'), Js('Virtue'), Js('Visionary'), Js('White Blossom'), Js('White Willow'), Js('Wishmaster'), Js('Wonder'), Js('Yesteryear'), Js('Zion')]))
var.put('nm2', Js([Js('Plaza'), Js('Square')]))
pass
pass


# Add lib to the module scope
plazaNames = var.to_python()