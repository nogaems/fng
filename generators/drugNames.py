__all__ = ['drugNames']

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
var.put('nm1', Js([Js('After Burner'), Js('Ammo'), Js('Angel'), Js('Anvil'), Js('Aqua'), Js('Arachnid'), Js('Ash'), Js('Barb'), Js('Blaze'), Js('Nitro'), Js('Cookie Dough'), Js('Sugar'), Js('Flour'), Js('Paste'), Js('Blitz'), Js('Haunt'), Js('Blue'), Js('Bonedust'), Js('Boogie'), Js('Boom'), Js('Bronze'), Js('Buffoon'), Js('Burnout'), Js('Buster'), Js('Cactus'), Js('Caine'), Js('Catnip'), Js('Change'), Js('Chaos'), Js('Chocolate'), Js('Chopsticks'), Js('Chow'), Js('Chrono'), Js('Claw'), Js('Coco'), Js('Comet'), Js('Crimson'), Js('Crisps'), Js('Crocodile Tears'), Js('Crow'), Js('Crush'), Js('Crypt'), Js('Daydream'), Js('Deluge'), Js("Devil's Tongue"), Js('Dew'), Js('Diamond'), Js('Doom'), Js('Dragon'), Js('Dragontail'), Js('Droplet'), Js('Dwarf'), Js('Dyno'), Js('Echo'), Js('Ecto'), Js('Enigma'), Js('Epiphany'), Js('Ether'), Js('Fairy Tale'), Js('Fate'), Js('Feather'), Js('Fizz'), Js('Fizzy Drink'), Js('Flare'), Js('Flashbang'), Js('Flinch'), Js('Fluff'), Js('Fluke'), Js('Frenzy'), Js('Frost'), Js('Fury'), Js('Gadgets'), Js('Galaxy'), Js('Gloom'), Js('Glory'), Js('Glue'), Js('Grave Dust'), Js('Green'), Js('Grunt'), Js('Hoarse'), Js('Hog'), Js('Honey'), Js('Hood'), Js('Howler'), Js('Hush'), Js('Icicles'), Js('Impact'), Js('Jade'), Js('Jetlag'), Js('Jiggy'), Js('Juice'), Js('Knockout'), Js('Lag'), Js('Leaves'), Js('Leech'), Js('Liftoff'), Js('Light Speed'), Js('Lightyear'), Js('Lizard'), Js('Luna'), Js('Lupus'), Js('Lyrics'), Js('Mane'), Js('Marbles'), Js('Mask'), Js('Merch'), Js('Miracle'), Js('Mirage'), Js('Mist'), Js('Mistress'), Js('Mithril'), Js('Moisturizer'), Js('Moon Rocks'), Js('Morbid'), Js('Morph'), Js('Mud'), Js('Musk'), Js('Muze'), Js('Myth'), Js('Nails'), Js('Necro'), Js('Nether'), Js('Nibble'), Js('Nova'), Js('Nuggets'), Js('Nuts'), Js('Onyx'), Js('Oracle'), Js('Orb'), Js('Ozone'), Js('Ozz'), Js('Phoenix'), Js('Pipes'), Js('Pixel'), Js('Powder'), Js('Quills'), Js("Rabbit's Foot"), Js('Rainbow'), Js('Rampage'), Js('Raptor'), Js('Reaper'), Js('Red'), Js('Rock Salt'), Js('Roots'), Js('Roth'), Js('Ruby'), Js('Runes'), Js('Sanguine'), Js('Sapphire'), Js('Serenity'), Js('Silver'), Js('Slush'), Js('Smut'), Js('Snowflake'), Js('Soil'), Js('Songbird'), Js('Soot'), Js('Spice'), Js('Spirit'), Js('Stake'), Js('Steel'), Js('Storm'), Js('Stripes'), Js('Sugar Cane'), Js('Sunburn'), Js('Supernova'), Js('Tails'), Js('Taint'), Js('Talon'), Js('Tears'), Js('Tease'), Js('Thimble'), Js('Third Eye'), Js('Thorn'), Js('Thunder'), Js('Titanium'), Js('Tombstone'), Js('Tranquil'), Js('Trinity'), Js('Twin'), Js('Twinkle'), Js('Twist'), Js('Twister'), Js('Typhoon'), Js('Vacuum'), Js('Vamp'), Js('Vampire Dust'), Js('Vanilla'), Js('Vapor'), Js('Venom'), Js('Vibe'), Js('Vintage'), Js('Visage'), Js('Void'), Js('Warp'), Js('Waves'), Js('Wax'), Js('Whiskers'), Js('Whisper'), Js('Wish'), Js('Wizard'), Js('Wolf'), Js('Wrath'), Js('Wrathhog'), Js('Wyvern'), Js('Xp')]))
pass
pass


# Add lib to the module scope
drugNames = var.to_python()