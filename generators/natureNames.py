__all__ = ['natureNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', var.get('nm3').get(var.get('rnd')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('Abelia'), Js('Acacia'), Js('Agate'), Js('Almond'), Js('Aloe'), Js('Alyssa'), Js('Amala'), Js('Amaranth'), Js('Amaryllis'), Js('Amber'), Js('Ambrosia'), Js('Amethyst'), Js('Anemone'), Js('Angel'), Js('Angelica'), Js('Angelice'), Js('Anise'), Js('Apple'), Js('April'), Js('Aqua'), Js('Arbor'), Js('Ari'), Js('Aria'), Js('Arum'), Js('Ash'), Js('Aspen'), Js('Aster'), Js('Aura'), Js('Aurelia'), Js('Aurora'), Js('Autumn'), Js('Ava'), Js('Avis'), Js('Aya'), Js('Azalea'), Js('Azolia'), Js('Azure'), Js('Basil'), Js('Bay'), Js('Bayou'), Js('Bee'), Js('Begonia'), Js('Belladonna'), Js('Beryl'), Js('Bird'), Js('Birdie'), Js('Blair'), Js('Blaze'), Js('Blossom'), Js('Bramble'), Js('Breeze'), Js('Breezy'), Js('Briar'), Js('Brier'), Js('Briny'), Js('Brook'), Js('Brooke'), Js('Brooks'), Js('Bryony'), Js('Bunny'), Js('Buttercup'), Js('Cadence'), Js('Calla'), Js('Camelia'), Js('Camellia'), Js('Camomile'), Js('Canary'), Js('Carina'), Js('Cascade'), Js('Cassa'), Js('Cassia'), Js('Catalina'), Js('Cayenne'), Js('Cedar'), Js('Celosia'), Js('Chandra'), Js('Cheyenne'), Js('Chrysanthe'), Js('Cinnamon'), Js('Clay'), Js('Clematis'), Js('Clementine'), Js('Cloud'), Js('Clove'), Js('Clover'), Js('Coral'), Js('Coriander'), Js('Cove'), Js('Crescent'), Js('Cricket'), Js('Crystal'), Js('Cypress'), Js('Daffodil'), Js('Dahlia'), Js('Daisy'), Js('Dakota'), Js('Dale'), Js('Danica'), Js('Danika'), Js('Daphne'), Js('Dawn'), Js('Deer'), Js('Delilah'), Js('Delta'), Js('Destiny'), Js('Dew'), Js('Dewy'), Js('Diamond'), Js('Doe'), Js('Dove'), Js('Dusk'), Js('Dusty'), Js('Ebony'), Js('Eden'), Js('Electra'), Js('Elektra'), Js('Elm'), Js('Ember'), Js('Emerald'), Js('Erica'), Js('Eve'), Js('Eytelia'), Js('Faith'), Js('Fauna'), Js('Fawn'), Js('Feather'), Js('Fen'), Js('Fennel'), Js('Fern'), Js('Fleur'), Js('Flora'), Js('Freesia'), Js('Fuchsia'), Js('Gaia'), Js('Galaxy'), Js('Gale'), Js('Galena'), Js('Garden'), Js('Garland'), Js('Garnet'), Js('Geranium'), Js('Gideon'), Js('Ginger'), Js('Glen'), Js('Glenn'), Js('Harmony'), Js('Haven'), Js('Hayley'), Js('Hazel'), Js('Heather'), Js('Hibiscus'), Js('Holly'), Js('Honey'), Js('Hyacinth'), Js('Ice'), Js('Indigo'), Js('Iris'), Js('Isle'), Js('Ivory'), Js('Ivy'), Js('Jacinth'), Js('Jade'), Js('Jasmine'), Js('Jay'), Js('Jewel'), Js('Jordan'), Js('Juniper'), Js('Kailani'), Js('Kale'), Js('Kalina'), Js('Karma'), Js('Kyla'), Js('Lake'), Js('Lale'), Js('Laleh'), Js('Lapis'), Js('Lark'), Js('Laurel'), Js('Lavender'), Js('Lazuli'), Js('Leaf'), Js('Leif'), Js('Leilani'), Js('Lelani'), Js('Lila'), Js('Lilac'), Js('Lillian'), Js('Lilly'), Js('Lily'), Js('Linden'), Js('Linnea'), Js('Lotus'), Js('Love'), Js('Lucerne'), Js('Luna'), Js('Magnolia'), Js('Mango'), Js('Maple'), Js('Mare'), Js('Marigold'), Js('Marin'), Js('Marina'), Js('Marine'), Js('Meadow'), Js('Melissa'), Js('Mesa'), Js('Mica'), Js('Mist'), Js('Misty'), Js('Moon'), Js('Myrtle'), Js('Nigella'), Js('Nova'), Js('Oak'), Js('Ocean'), Js('Oleander'), Js('Olive'), Js('Olivia'), Js('Opal'), Js('Orchard'), Js('Orchid'), Js('Oriel'), Js('Oriole'), Js('Pandora'), Js('Pansy'), Js('Peach'), Js('Peaches'), Js('Pearl'), Js('Peony'), Js('Pepper'), Js('Peridot'), Js('Petal'), Js('Petunia'), Js('Phoenix'), Js('Pine'), Js('Poppy'), Js('Posy'), Js('Primrose'), Js('Puma'), Js('Rain'), Js('Raine'), Js('Raven'), Js('Reed'), Js('Reef'), Js('Rhine'), Js('River'), Js('Roan'), Js('Robin'), Js('Rosa'), Js('Rose'), Js('Rosemary'), Js('Rosetta'), Js('Rowan'), Js('Rubia'), Js('Ruby'), Js('Rue'), Js('Ruellia'), Js('Sable'), Js('Saffron'), Js('Sage'), Js('Sahara'), Js('Sakura'), Js('Sapphire'), Js('Sassafras'), Js('Savanna'), Js('Savannah'), Js('Season'), Js('Senna'), Js('Sequoia'), Js('Shadow'), Js('Shale'), Js('Sharon'), Js('Shell'), Js('Shelly'), Js('Shore'), Js('Sienna'), Js('Sierra'), Js('Silver'), Js('Sky'), Js('Skye'), Js('Skyler'), Js('Snow'), Js('Sol'), Js('Solstice'), Js('Sorrel'), Js('Sparrow'), Js('Spring'), Js('Spruce'), Js('Star'), Js('Starling'), Js('Stella'), Js('Sterling'), Js('Storm'), Js('Stormy'), Js('Summer'), Js('Sunny'), Js('Sunshine'), Js('Swan'), Js('Sweetpea'), Js('Sycamore'), Js('Tansy'), Js('Teal'), Js('Tempest'), Js('Terra'), Js('Thyme'), Js('Tierra'), Js('Tigerlily'), Js('Topaz'), Js('Tulip'), Js('Vale'), Js('Valley'), Js('Vanilla'), Js('Vanille'), Js('Venus'), Js('Veronica'), Js('Violet'), Js('Vixen'), Js('Willow'), Js('Windy'), Js('Winter'), Js('Wren'), Js('Wynter'), Js('Yarrow'), Js('Zahra'), Js('Zinnia')]))
var.put('nm1', Js([Js('Acke'), Js('Ackerly'), Js('Ackley'), Js('Acorn'), Js('Aedan'), Js('Aegis'), Js('Aiden'), Js('Alabaster'), Js('Alan'), Js('Alder'), Js('Alfalfa'), Js('Almond'), Js('Amon'), Js('Angel'), Js('Aqua'), Js('Archer'), Js('Ari'), Js('Arum'), Js('Ash'), Js('Asher'), Js('Aspen'), Js('Aster'), Js('Austin'), Js('Avis'), Js('Axel'), Js('Azure'), Js('Badger'), Js('Balsam'), Js('Bark'), Js('Barrow'), Js('Basil'), Js('Bay'), Js('Bayou'), Js('Bear'), Js('Berry'), Js('Birch'), Js('Bird'), Js('Blair'), Js('Blaze'), Js('Blue'), Js('Bluejay'), Js('Bramble'), Js('Bran'), Js('Branch'), Js('Breeze'), Js('Briar'), Js('Brier'), Js('Brighton'), Js('Bronze'), Js('Brook'), Js('Brooke'), Js('Brooks'), Js('Buck'), Js('Cade'), Js('Calder'), Js('Canyon'), Js('Carnelian'), Js('Cayenne'), Js('Cedar'), Js('Chase'), Js('Chervil'), Js('Chester'), Js('Clay'), Js('Cliff'), Js('Cloud'), Js('Clove'), Js('Clyde'), Js('Coal'), Js('Coast'), Js('Cobalt'), Js('Colt'), Js('Copper'), Js('Coriander'), Js('Cornelian'), Js('Cotton'), Js('Cove'), Js('Crane'), Js('Crescent'), Js('Cricket'), Js('Crow'), Js('Cypress'), Js('Dakota'), Js('Dale'), Js('Danica'), Js('Danika'), Js('Dante'), Js('Dean'), Js('Deer'), Js('Delta'), Js('Dew'), Js('Dewy'), Js('Dingo'), Js('Drake'), Js('Dune'), Js('Dusk'), Js('Dusty'), Js('Eban'), Js('Edan'), Js('Elm'), Js('Ember'), Js('Everest'), Js('Falcon'), Js('Fen'), Js('Fennel'), Js('Fern'), Js('Field'), Js('Finch'), Js('Fjord'), Js('Flame'), Js('Flint'), Js('Ford'), Js('Forest'), Js('Forrest'), Js('Fox'), Js('Frost'), Js('Gale'), Js('Gibbon'), Js('Gideon'), Js('Ginger'), Js('Glen'), Js('Glenn'), Js('Glyn'), Js('Gold'), Js('Gorge'), Js('Granite'), Js('Grove'), Js('Harbor'), Js('Harvest'), Js('Haven'), Js('Hawk'), Js('Hawke'), Js('Hawthorn'), Js('Heath'), Js('Heron'), Js('Horizon'), Js('Huckleberry'), Js('Hudson'), Js('Hunter'), Js('Huntley'), Js('Hyatt'), Js('Hyde'), Js('Ice'), Js('Indigo'), Js('Jade'), Js('Jaguar'), Js('Jasper'), Js('Jay'), Js('Jericho'), Js('Jet'), Js('Jett'), Js('Jordan'), Js('Judas'), Js('Juniper'), Js('Kale'), Js('Kodiak'), Js('Kylan'), Js('Kyle'), Js('Lagoon'), Js('Lake'), Js('Land'), Js('Lando'), Js('Larch'), Js('Lark'), Js('Laurel'), Js('Lazuli'), Js('Leaf'), Js('Leif'), Js('Leo'), Js('Leon'), Js('Linden'), Js('Lion'), Js('Lynx'), Js('Mace'), Js('Macon'), Js('Mai'), Js('Mango'), Js('Mansi'), Js('Marin'), Js('Marino'), Js('Marsh'), Js('Mason'), Js('Mercury'), Js('Mica'), Js('Moor'), Js('Moth'), Js('Newt'), Js('North'), Js('Nova'), Js('Oak'), Js('Obsidian'), Js('Ocean'), Js('Oleander'), Js('Oliver'), Js('Onyx'), Js('Orchard'), Js('Orion'), Js('Pembroke'), Js('Pepper'), Js('Phoenix'), Js('Pike'), Js('Pine'), Js('Quarry'), Js('Quartz'), Js('Quest'), Js('Quill'), Js('Rain'), Js('Raine'), Js('Ram'), Js('Raven'), Js('Reed'), Js('Reef'), Js('Rhine'), Js('Ridge'), Js('Rio'), Js('River'), Js('Roan'), Js('Robin'), Js('Rock'), Js('Rowan'), Js('Rue'), Js('Ryland'), Js('Sable'), Js('Sage'), Js('Seal'), Js('Shadow'), Js('Shale'), Js('Shell'), Js('Silver'), Js('Sky'), Js('Skylark'), Js('Skyler'), Js('Slate'), Js('Snow'), Js('Sol'), Js('Sorrel'), Js('Spruce'), Js('Star'), Js('Starling'), Js('Steel'), Js('Steele'), Js('Sterling'), Js('Stone'), Js('Storm'), Js('Stormy'), Js('Sunny'), Js('Talon'), Js('Thicket'), Js('Thorn'), Js('Thyme'), Js('Tide'), Js('Tiger'), Js('Vale'), Js('Valerian'), Js('Winter'), Js('Wolf'), Js('Wolfe'), Js('Wood'), Js('Woods'), Js('Woody'), Js('Wren'), Js('Yarrow'), Js('Zinc')]))
var.put('nm3', Js([Js('Almond'), Js('Angel'), Js('Aqua'), Js('Ari'), Js('Arum'), Js('Ash'), Js('Aspen'), Js('Aster'), Js('Avis'), Js('Azure'), Js('Basil'), Js('Bay'), Js('Bayou'), Js('Bird'), Js('Blair'), Js('Blaze'), Js('Bramble'), Js('Breeze'), Js('Briar'), Js('Brier'), Js('Brook'), Js('Brooke'), Js('Brooks'), Js('Cayenne'), Js('Cedar'), Js('Clay'), Js('Cloud'), Js('Clove'), Js('Coriander'), Js('Cove'), Js('Crescent'), Js('Cricket'), Js('Cypress'), Js('Dakota'), Js('Dale'), Js('Danica'), Js('Danika'), Js('Deer'), Js('Delta'), Js('Dew'), Js('Dewy'), Js('Dusk'), Js('Dusty'), Js('Elm'), Js('Ember'), Js('Fen'), Js('Fennel'), Js('Fern'), Js('Gale'), Js('Gideon'), Js('Ginger'), Js('Glen'), Js('Glenn'), Js('Haven'), Js('Ice'), Js('Indigo'), Js('Jade'), Js('Jay'), Js('Jordan'), Js('Juniper'), Js('Kale'), Js('Lake'), Js('Lark'), Js('Laurel'), Js('Lazuli'), Js('Leaf'), Js('Leif'), Js('Linden'), Js('Mango'), Js('Marin'), Js('Mica'), Js('Nova'), Js('Oak'), Js('Ocean'), Js('Oleander'), Js('Orchard'), Js('Pepper'), Js('Phoenix'), Js('Pine'), Js('Rain'), Js('Raine'), Js('Raven'), Js('Reed'), Js('Reef'), Js('Rhine'), Js('River'), Js('Roan'), Js('Robin'), Js('Rowan'), Js('Sable'), Js('Sage'), Js('Shadow'), Js('Shale'), Js('Shell'), Js('Silver'), Js('Sky'), Js('Skyler'), Js('Snow'), Js('Sol'), Js('Sorrel'), Js('Spruce'), Js('Star'), Js('Starling'), Js('Sterling'), Js('Storm'), Js('Stormy'), Js('Sunny'), Js('Thyme'), Js('Vale'), Js('Winter'), Js('Wren'), Js('Yarrow')]))
pass
pass


# Add lib to the module scope
natureNames = var.to_python()