__all__ = ['lionNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ajax'), Js('Alfie'), Js('Anger'), Js('Artemis'), Js('Aslan'), Js('Astro'), Js('Axe'), Js('Bale'), Js('Bandit'), Js('Bane'), Js('Bazal'), Js('Begal'), Js('Bengo'), Js('Biscuit'), Js('Bleach'), Js('Blitz'), Js('Bones'), Js('Boots'), Js('Brownie'), Js('Bruno'), Js('Brutus'), Js('Bubba'), Js('Bubble'), Js('Buster'), Js('Butters'), Js('Catastrophe'), Js('Chance'), Js('Chase'), Js('Chester'), Js('Chewy'), Js('Chili'), Js('Clawde'), Js('Cloud'), Js('Cosmo'), Js('Cotton'), Js('Cuddles'), Js('Dash'), Js('Domino'), Js('Dova'), Js('Duke'), Js('Dusty'), Js('Echo'), Js('Fang'), Js('Fetch'), Js('Fire'), Js('Flynn'), Js('Frisky'), Js('Fury'), Js('Fyre'), Js('Ghost'), Js('Giggles'), Js('Gnaw'), Js('Grinch'), Js('Hannibal'), Js('Haze'), Js('Hector'), Js('Hooch'), Js('Indi'), Js('Jag'), Js('Khan'), Js('Kimba'), Js('Lash'), Js('Lecter'), Js('Leo'), Js('Leon'), Js('Licorice'), Js('Lightning'), Js('Lionel'), Js('Loki'), Js('Lycan'), Js('Marble'), Js('Maw'), Js('Max'), Js('Mello'), Js('Midnight'), Js('Miles'), Js('Mittens'), Js('Muffin'), Js('Nemesis'), Js('Nibble'), Js('Nibbler'), Js('Nightmare'), Js('Nightshade'), Js('Nine'), Js('Nocturn'), Js('Nova'), Js('Nugget'), Js('Onyx'), Js('Patch'), Js('Pax'), Js('Peanut'), Js('Pebble'), Js('Perseus'), Js('Phantom'), Js('Pounce'), Js('Pouncer'), Js('Puff'), Js('Pyre'), Js('Quicksilver'), Js('Rage'), Js('Raja'), Js('Rambo'), Js('Ranger'), Js('Rawr'), Js('Reaper'), Js('Render'), Js('Rock'), Js('Rocky'), Js('Scar'), Js('Scratches'), Js('Shadow'), Js('Shiv'), Js('Shrapnel'), Js('Shredder'), Js('Silver'), Js('Skip'), Js('Skittles'), Js('Skye'), Js('Sly'), Js('Smiles'), Js('Smokey'), Js('Snickers'), Js('Snow'), Js('Snowball'), Js('Snowflake'), Js('Snuggle'), Js('Sparks'), Js('Spike'), Js('Spot'), Js('Stalker'), Js('Stitch'), Js('Storm'), Js('Strike'), Js('Striker'), Js('Stripe'), Js('Stripes'), Js('Swipes'), Js('Thunder'), Js('Tickles'), Js('Tiny'), Js('Tooth'), Js('Truffle'), Js('Tygar'), Js('Tyson'), Js('Victor'), Js('Whiskers'), Js('Woods'), Js('Wrath')]))
var.put('nm2', Js([Js('Aggy'), Js('Alexi'), Js('Amber'), Js('Anger'), Js('Ashelia'), Js('Aslana'), Js('Athena'), Js('Azure'), Js('Babe'), Js('Bambino'), Js('Beauty'), Js('Belle'), Js('Biscuit'), Js('Blitze'), Js('Boots'), Js('Brownie'), Js('Bubbles'), Js('Buttercup'), Js('Cara'), Js('Cato'), Js('Chance'), Js('Cinnamon'), Js('Clawdia'), Js('Cloe'), Js('Coco'), Js('Cookie'), Js('Cosmo'), Js('Cotton'), Js('Crystal'), Js('Cupcake'), Js('Daisy'), Js('Dash'), Js('Dawn'), Js('Delilah'), Js('Dot'), Js('Dottie'), Js('Dutchess'), Js('Echo'), Js('Enigma'), Js('Enya'), Js('Eve'), Js('Faith'), Js('Fawn'), Js('Flame'), Js('Giggles'), Js('Ginny'), Js('Grace'), Js('Harley'), Js('Haze'), Js('Hazel'), Js('Hope'), Js('Huntress'), Js('Iris'), Js('Jade'), Js('Jasmine'), Js('Jinx'), Js('June'), Js('Jynx'), Js('Kara'), Js('Karma'), Js('Kat'), Js('Kate'), Js('Kathy'), Js('Kisses'), Js('Kitty'), Js('Lilly'), Js('Lola'), Js('Lucy'), Js('Lullaby'), Js('Luna'), Js('Lyla'), Js('Mae'), Js('Mango'), Js('Maya'), Js('Mello'), Js('Mila'), Js('Misty'), Js('Mocha'), Js('Muffin'), Js('Myst'), Js('Mystique'), Js('Nala'), Js('Neko'), Js('Nemo'), Js('Nibble'), Js('Nibbles'), Js('Nipsey'), Js('Nora'), Js('Nugget'), Js('Nutmeg'), Js('Oracle'), Js('Patches'), Js('Paws'), Js('Peaches'), Js('Pebble'), Js('Pebbles'), Js('Pepper'), Js('Phantom'), Js('Pickles'), Js('Precious'), Js('Princess'), Js('Puff'), Js('Roxy'), Js('Ruby'), Js('Sabrina'), Js('Sage'), Js('Sandy'), Js('Sapphire'), Js('Scratches'), Js('Selena'), Js('Serenity'), Js('Shade'), Js('Shadow'), Js('Shiba'), Js('Shinx'), Js('Smooch'), Js('Smudges'), Js('Snow'), Js('Snowball'), Js('Snowflake'), Js('Snuggles'), Js('Song'), Js('Sphinx'), Js('Spot'), Js('Stripes'), Js('Sugar'), Js('Summer'), Js('Sundance'), Js('Sweetie'), Js('Tickles'), Js('Tigress'), Js('Tiny'), Js('Toots'), Js('Trixie'), Js('Truffles'), Js('Twilight'), Js('Twinkle'), Js('Umbreon'), Js('Violet'), Js('Waffles'), Js('Whiskers'), Js('Whisper'), Js('Wiggles'), Js('Willow'), Js('Winter')]))
pass
pass


# Add lib to the module scope
lionNames = var.to_python()