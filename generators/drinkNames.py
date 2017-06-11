__all__ = ['drinkNames']

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
    var.registers(['names1', 'names2', 'result'])
    var.put('names1', Js([Js('Ale'), Js('Brandy'), Js('Tea'), Js('Tea'), Js('Sherry'), Js('Brew'), Js('Cappuchino'), Js('Cider'), Js('Coffee'), Js('Cognac'), Js('Dark Ale'), Js('Dark Beer'), Js('Drink'), Js('Espresso'), Js('Gin'), Js('Java'), Js('Lager'), Js('Light Ale'), Js('Light Beer'), Js('Mead'), Js('Mocha'), Js('Red Wine'), Js('Rum'), Js('Sake'), Js('Tea'), Js('Tonic'), Js('Vodka'), Js('Whiskey'), Js('White Wine'), Js('Wine'), Js('Almond'), Js('Amazing'), Js('Ancient'), Js('Angel'), Js('Angelic'), Js('Apple'), Js('Apricot'), Js('Arctic'), Js('Aromatic'), Js('Autumn'), Js('Avocado'), Js('Balanced'), Js('Banana'), Js('Basil'), Js('Bay Leaf'), Js('Beautiful'), Js('Beetroot'), Js('Black'), Js('Blue'), Js('Blueberry'), Js('Boiled'), Js('Brilliant'), Js('Brown'), Js('Brutal'), Js('Burning'), Js('Calm'), Js('Capital'), Js('Caramel'), Js('Catnip'), Js('Cherry'), Js('Cherry Blossom'), Js('Chestnut'), Js('Chilled'), Js('Chilli'), Js('Cinnamon'), Js('Clouded'), Js('Cloudy'), Js('Coconut'), Js('Cool'), Js('Coriander'), Js('Cosmic'), Js('Cranberry'), Js('Crazy'), Js('Crimson'), Js('Cucumber'), Js('Demon'), Js('Demonic'), Js('Dire'), Js('Eastern'), Js('Easy'), Js('Electric'), Js('Elemental'), Js('Evil'), Js('Extreme'), Js('Fainting'), Js('Fallen'), Js('Fancy'), Js('Fantasy'), Js('Fast'), Js('Final'), Js('First'), Js('Flaming'), Js('Flower'), Js('Flying'), Js('Forest'), Js('Fresh'), Js('Frosted'), Js('Frozen'), Js('Fruity'), Js('Garlic'), Js('Gentle'), Js('Ginger'), Js('Gingerroot'), Js('Gleaming'), Js('Glowing'), Js('Grape'), Js('Grapefruit'), Js('Green'), Js('Hazelnut'), Js('High'), Js('Holy'), Js('Honest'), Js('Honey'), Js('Hot'), Js('Hushed'), Js('Icy'), Js('Imaginary'), Js('Incredible'), Js('Infinite'), Js('Innocent'), Js('Insane'), Js('Insanity'), Js('Jasmine'), Js('Kiwi'), Js('Lavender'), Js('Lavish'), Js('Lemon'), Js('Lemonade'), Js('Lemongrass'), Js('Lemony'), Js('Lime'), Js('Low'), Js('Lucky'), Js('Mad'), Js('Mango'), Js('Melon'), Js('Mild'), Js('Milk'), Js('Milky'), Js('Mint'), Js('Minty'), Js('Molten'), Js('Mountain'), Js('Mystic'), Js('Nasty'), Js('Nimble'), Js('Noble'), Js('Northern'), Js('Noxious'), Js('Numb'), Js('Nutmeg'), Js('Nutty'), Js('Oak'), Js('Oaken'), Js('Oblivious'), Js('Obvious'), Js('Orange'), Js('Oregano'), Js('Palm'), Js('Paranoid'), Js('Passion Fruit'), Js('Peacan'), Js('Peanut'), Js('Pear'), Js('Peppermint'), Js('Perfect'), Js('Pineapple'), Js('Pink'), Js('Potato'), Js('Precious'), Js('Pure'), Js('Rainbow'), Js('Red'), Js('River'), Js('Rose'), Js('Rose Petal'), Js('Rosemary'), Js('Rotten'), Js('Rough'), Js('Rude'), Js('Rushed'), Js('Saffron'), Js("Salt 'n Pepper"), Js('Salty'), Js('Sanguine'), Js('Savage'), Js('Scented'), Js('Secret'), Js('Silent'), Js('Smooth'), Js('Southern'), Js('Spearmint'), Js('Spiced'), Js('Spicy'), Js('Spirit'), Js('Spring'), Js('Stale'), Js('Steamy'), Js('Sticky'), Js('Strawberry'), Js('Sugar'), Js('Sugary'), Js('Summer'), Js('Surprised'), Js('Sweet'), Js('Tarragon'), Js('Thyme'), Js('Tiny'), Js('Tomato'), Js('Tropic'), Js('Tropical'), Js('Twisting'), Js('Ultimate'), Js('Unholy'), Js('Universal'), Js('Unlucky'), Js('Vanilla'), Js('Vanillabean'), Js('Vibrant'), Js('Warm'), Js('Wasabi'), Js('Watermelon'), Js('Western'), Js('Wet'), Js('Whimsical'), Js('Whipped'), Js('White'), Js('Wicked'), Js('Wild'), Js('Willow'), Js('Winged'), Js('Winter'), Js('Wonderful'), Js('Wonderous'), Js('Yellow')]))
    var.put('names2', Js([Js('Ale'), Js('Brandy'), Js('Tea'), Js('Tea'), Js('Sherry'), Js('Brew'), Js('Cappuchino'), Js('Cider'), Js('Coffee'), Js('Cognac'), Js('Dark Ale'), Js('Dark Beer'), Js('Drink'), Js('Espresso'), Js('Gin'), Js('Java'), Js('Lager'), Js('Light Ale'), Js('Light Beer'), Js('Mead'), Js('Mocha'), Js('Red Wine'), Js('Rum'), Js('Sake'), Js('Tea'), Js('Tonic'), Js('Vodka'), Js('Whiskey'), Js('White Wine'), Js('Wine'), Js('Amigo'), Js('Arrow'), Js('Ball'), Js('Barrage'), Js('Bear'), Js('Blast'), Js('Blaze'), Js('Bliss'), Js('Blitz'), Js('Blizzard'), Js('Blood'), Js('Blossom'), Js('Bolt'), Js('Bomb'), Js('Breeze'), Js('Bruiser'), Js('Bubble'), Js('Bull'), Js('Burst'), Js('Buzzer'), Js('Cooler'), Js('Crash'), Js('Critter'), Js('Crush'), Js('Crusher'), Js('Crystal'), Js('Delight'), Js('Dog'), Js('Double'), Js('Drop'), Js('Duke'), Js('Dutchess'), Js('Earthquake'), Js('Eclipse'), Js('Eight'), Js('Enigma'), Js('Eye'), Js('Five'), Js('Flash'), Js('Fluff'), Js('Fluffy'), Js('Four'), Js('Freedom'), Js('Fury'), Js('Giant'), Js('Gloom'), Js('Grog'), Js('Heaven'), Js('Hell'), Js('Hopper'), Js('Horn'), Js('Horror'), Js('Hound'), Js('Howler'), Js('Infusion'), Js('Jam'), Js('Joke'), Js('Joker'), Js('Joy'), Js('Killer'), Js('Kiss'), Js('Kisses'), Js('Knight'), Js('Lady'), Js('Lagoon'), Js('Light'), Js('Lion'), Js('Lord'), Js('Lotus'), Js('Lover'), Js('Major'), Js('Minor'), Js('Mix'), Js('Monsoon'), Js('Moonshine'), Js('Mud'), Js('Murder'), Js('Nectar'), Js('Night'), Js('Nightfall'), Js('Orb'), Js('Paradise'), Js('Paralyzer'), Js('Parody'), Js('Passion'), Js('Pearl'), Js('Pecker'), Js('Petal'), Js('Phantom'), Js('Plus'), Js('Pop'), Js('Puff'), Js('Punch'), Js('Rage'), Js('Riddle'), Js('Roar'), Js('Rumble'), Js('Rush'), Js('Score'), Js('Scream'), Js('Seven'), Js('Shadow'), Js('Shield'), Js('Shot'), Js('Shrub'), Js('Silence'), Js('Sip'), Js('Six'), Js('Sizzle'), Js('Slammer'), Js('Slap'), Js('Slapper'), Js('Sling'), Js('Slingshot'), Js('Slush'), Js('Smash'), Js('Smooch'), Js('Snake'), Js('Snowball'), Js('Sour'), Js('Special'), Js('Squeeze'), Js('Stardust'), Js('Starlight'), Js('Stinger'), Js('Storm'), Js('Striker'), Js('Sunrise'), Js('Sunset'), Js('Surge'), Js('Talon'), Js('Teaser'), Js('Temper'), Js('Tempest'), Js('Thrill'), Js('Thriller'), Js('Thunder'), Js('Ticker'), Js('Tickle'), Js('Tonic'), Js('Tornado'), Js('Torrent'), Js('Touch'), Js('Tremor'), Js('Twilight'), Js('Twister'), Js('Velour'), Js('Velvet'), Js('Vengeance'), Js('Volcano'), Js('Volley'), Js('Wacker'), Js('Walk'), Js('Walker'), Js('Wave'), Js('Whisper'), Js('Whistle'), Js('Wink'), Js('Wonder'), Js('Zombie')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            if (var.get('rnd')<Js(30.0)):
                while (var.get('rnd2')<Js(30.0)):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', ((var.get('names1').get(var.get('rnd'))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
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
drinkNames = var.to_python()