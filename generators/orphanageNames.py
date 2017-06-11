__all__ = ['orphanageNames']

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
var.put('nm1', Js([Js('All As One'), Js('Amazing Grace'), Js('Angel Eyes'), Js("Angel's Haven"), Js("Angel's Palace"), Js('Angelwing'), Js('Apple Blossom'), Js('Arms of Love'), Js('Aurora'), Js('Big Buddies'), Js('Big Companions'), Js('Big Heart'), Js('Blossoms'), Js('Bluebird'), Js("Boy's Town"), Js('Bright Horizons'), Js('Bright Sides'), Js('Building Blocks'), Js('Bumble Bee'), Js('Butterfly'), Js('Cherish'), Js('Children of the World'), Js("Children's Garden"), Js('Comfort Zone'), Js('Companions'), Js('Cradle of Love'), Js('Cradles'), Js('Crystal Fountain'), Js('Crystal Tree'), Js('Darlings'), Js('Daybreak'), Js('Daydream'), Js('Daydreams'), Js('Destiny Gardens'), Js('Dreamland'), Js("Eagle's Nest"), Js('Early Rise'), Js('Eden'), Js('Eternal Sunshine'), Js('Family Circle'), Js('Fellowship'), Js('First Light'), Js('Fountain of Life'), Js('Fountain of Youth'), Js('Fresh Hope'), Js('Friendship'), Js('Future Happiness'), Js('Generous Lives'), Js('Genesis'), Js("Girl's Town"), Js('Grace'), Js('Grand Tree'), Js('Green Fields'), Js('Guardian Angel'), Js("Guardian's Garden"), Js('Guidance'), Js('Halo'), Js('Hand in Hand'), Js('Happy Days'), Js('Happy Hearts'), Js('Happy Hill'), Js('Happy Home'), Js('Happy Mountain'), Js('Harmony'), Js("Heaven's"), Js('Helping Hand'), Js('Helping Hands'), Js('Home of Peace'), Js('Home of the Good'), Js('Honey Drop'), Js('Hope Springs'), Js('Hope Town'), Js('Horizon'), Js('Humble Bee'), Js('Inceptions'), Js('Innocence'), Js('Junior Angel'), Js('Kids Kingdom'), Js('Kindred Hearts'), Js('Kindred Souls'), Js('Kindred Spirits'), Js('Laughing Souls'), Js('Leg Up'), Js('Legacy'), Js('Lighthouse'), Js('Lily'), Js('Lilypad'), Js('Little Angel'), Js('Little Beginnings'), Js('Little Bugs'), Js('Little Champions'), Js('Little Darlings'), Js('Little Delights'), Js('Little Dreams'), Js('Little Friends'), Js('Little Garden'), Js('Little Lamb'), Js('Little Miracles'), Js('Little Palace'), Js('Little Petals'), Js('Little River'), Js('Little Rock'), Js('Little Stars'), Js('Little Steps'), Js('Little Talents'), Js('Little Town'), Js('Little Treasures'), Js('Little Voices'), Js("Little Wanderer's"), Js('Little Whispers'), Js('Littlest Angels'), Js('Littlewood'), Js('Living Water'), Js('Lotus'), Js('Lotus Children'), Js('Lullaby'), Js('Mercy Home'), Js('Mini Miracles'), Js('Mission of Hope'), Js('Mission of Love'), Js('Morning Star'), Js('Mother Goose'), Js('New Beginnings'), Js('New Connections'), Js('New Dawn'), Js('New Haven'), Js('New Heritage'), Js('New Hope'), Js('New Horizons'), Js('New Life'), Js('New Prospects'), Js('New Vision'), Js('North Star'), Js('Nourish and Flourish'), Js('One Heart'), Js('Open Doorways'), Js('Open Heart'), Js('Over the Rainbow'), Js('Paradise'), Js('Peace Blossoms'), Js('Phoenix'), Js('Piggyback'), Js('Playground'), Js('Precious Child'), Js('Precious Gems'), Js('Precious Home'), Js('Prospects'), Js('Radiance'), Js('Radiant Futures'), Js('Rainbow Children'), Js('Rainbow Flowers'), Js('Rascals'), Js('Rays of Life'), Js('Renaissance'), Js("Robin's Nest"), Js('Rose Petals'), Js('Rugrats'), Js('Sacred Heart'), Js('Safe Harbor'), Js('Serenity'), Js('Shepherd'), Js("Shepherd's Home"), Js('Silver Oak'), Js('Skyreach'), Js('Small Miracles'), Js('Small Steps'), Js('Smiles'), Js('Starlight'), Js('Step by Step'), Js('Stepping Stones'), Js('Story Time'), Js('Strong Desires'), Js('Strong Foundations'), Js('Sugerplum'), Js('Sunflower'), Js('Sunrise'), Js('Sweet Children'), Js('Sweethearts'), Js('Tiny Toes'), Js('Tranquil Garden'), Js('Transformation'), Js('Tree of Life'), Js('Treetops'), Js('Trinity'), Js('Under the Sun'), Js('United Voices'), Js('United We Stand'), Js('Voices of Children'), Js('Warm Hearts'), Js('Warm Home'), Js('We Care'), Js('White Lilly'), Js('White Orchid'), Js('White Tulip'), Js('White Warden'), Js('White Willow'), Js('Wings of Angels'), Js('Wings of Love'), Js('Wings of Refuge'), Js('Zion')]))
var.put('nm2', Js([Js('Orphanage'), Js('Orphan Home'), Js('Home')]))
pass
pass


# Add lib to the module scope
orphanageNames = var.to_python()