__all__ = ['toolNicknames']

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
            var.put('names', (Js('The ')+var.get('nm1').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Angel Wing'), Js('Angler'), Js('Arm Buster'), Js('Automaton'), Js('Backscratcher'), Js('Band Aid'), Js('Bear Claw'), Js('Bear Paw'), Js('Bell'), Js('Belly'), Js('Big Beak'), Js('Big Blue'), Js('Big Buddy'), Js('Big Nose'), Js('Bigwig'), Js('Biter'), Js('Bodangle'), Js('Boomer'), Js('Braces'), Js('Breaker'), Js('Breather'), Js('Bridesmaid'), Js('Brute'), Js('Brute Force'), Js('Bubble'), Js('Bullet'), Js('Bullseye'), Js('Bumblebee'), Js('Burner'), Js('Buster'), Js('Butterfly'), Js('Button Hook'), Js('Buzz'), Js('Buzzer'), Js('Cage'), Js('Carrot'), Js('Cat Head'), Js('Cat Paw'), Js('Cheater'), Js('Cheese Grater'), Js('Chicken Beak'), Js('Chicken Catcher'), Js('Chipper'), Js('Choppers'), Js('Chucker'), Js('Clicker'), Js('Commander'), Js('Crusher'), Js('Cube'), Js('Dirty Bomb'), Js('Dislocator'), Js('Dismounter'), Js('Do-Goodie'), Js('Drag'), Js('Drag Bag'), Js('Dual Wing'), Js('Duck Foot'), Js('Duster'), Js('Eagle Eye'), Js('Feather'), Js('Firecrackers'), Js('Fish'), Js('Fish Head'), Js('Fixer'), Js('Fixeraller'), Js('Flasher'), Js('Flat Nose'), Js('Fluffer'), Js('Four Eyes'), Js('Friendly One'), Js('Frog'), Js('Fury'), Js('Fuse Gate'), Js('Ghost Catcher'), Js('Goat Head'), Js('Gobbler'), Js('Godzilla'), Js('Good-for-nothing'), Js('Goof'), Js('Goofy Hook'), Js('Grasshopper'), Js('Grater'), Js('Grinder'), Js('Ground Crusher'), Js('Guardian'), Js('Guts'), Js('Guzzler'), Js('Hand Press'), Js('Hand Shoe'), Js('Handler'), Js('Handy Dandy'), Js('Hard Head'), Js('Hog'), Js('Hole Digger'), Js('Hole Puncher'), Js('Hookclaw'), Js('Horn Head'), Js('Horseshoe'), Js('Icicle'), Js('Interogator'), Js('Jawbreaker'), Js('Jaybird'), Js('Jelly'), Js('Jiggle'), Js('Kicker'), Js('Killer'), Js('Knocker'), Js('Knockout'), Js('Knuckle Knocker'), Js('Leverager'), Js('Little Buddy'), Js('Little Green'), Js('Little Head'), Js('Locator'), Js('Looper'), Js('Loosener'), Js('Lumpy'), Js('Measurer'), Js('Meat Hook'), Js('Mega Laser'), Js('Mohawk'), Js('Monkey Face'), Js('Monkey Suit'), Js('Naga'), Js('Nail Clipper'), Js('Nail Uzi'), Js('Nutcracker'), Js('Old Yeller'), Js('Onion Skin'), Js('Parrot'), Js('Pawpaw'), Js('Pencil Neck'), Js('Persuader'), Js('Phaser'), Js('Picker'), Js('Pickle'), Js('Pie Knife'), Js('Pig Tails'), Js('Pignose'), Js('Pitcher'), Js('Plumber'), Js('Plumbstick'), Js('Pokey'), Js('Power Shower'), Js('Powpow'), Js('Prickle'), Js('Puffer'), Js('Pully'), Js('Puncher'), Js('Punisher'), Js('Puppy Eyes'), Js('Questioner'), Js('Rabbit Ears'), Js('Ram'), Js('Ram Head'), Js('Rambler'), Js('Rat Skin'), Js('Ratchet'), Js('Rattle'), Js('Rattle Gun'), Js('Remover'), Js('Ridge'), Js('Rocky'), Js('Rum Raddle'), Js('Saber'), Js('Sabertooth'), Js('Salsa'), Js('Scalpel'), Js('Scratcher'), Js('Screecher'), Js('Screw Loose'), Js('Scythe'), Js('Sea Shell'), Js('Seahorse'), Js('Shackles'), Js('Sharpner'), Js('Shoe String'), Js('Shover'), Js('Single Wing'), Js('Skater'), Js('Skiller'), Js('Slack Strap'), Js('Slacker'), Js('Slapper'), Js('Slipper'), Js('Sludge'), Js('Slug'), Js('Small Beak'), Js('Smasher'), Js('Smiter'), Js('Snackbox'), Js('Snake'), Js('Snapper'), Js('Snipsnap'), Js('Soft Head'), Js('Sparkler'), Js('Sparrow'), Js('Spiderleg'), Js('Spiker'), Js('Spine'), Js('Spoon'), Js('Sprocket'), Js('Spuds'), Js('Squeezer'), Js('Starfish'), Js('Stitcher'), Js('Stretcher'), Js('Stud'), Js('Stunner'), Js('Sweat Cap'), Js('Switcher'), Js('Talon'), Js('Tater'), Js('Tatertot'), Js('Terminator'), Js('Termite'), Js('Thief'), Js('Thingymabob'), Js('Tingler'), Js('Toothpick'), Js('Tracker'), Js('Trapper'), Js('Tumb Crusher'), Js('Tumb Wrench'), Js('Turner'), Js('Tweaker'), Js('Twister'), Js('Wacker'), Js('Watchamacallit'), Js('Wazoo'), Js('Wedger'), Js('Wedgies'), Js('Weeper'), Js('Weeping Bell'), Js('Wheel of Death'), Js('Whiskers'), Js('Whiskey Stick'), Js('Wiggle Stick'), Js('Wiggler'), Js('Winger'), Js('Wippersnapper'), Js('Wishywashy'), Js('Wizzer'), Js('Wonker'), Js('Woodhandle'), Js('Woodpecker'), Js('Wrapper'), Js('Zapper'), Js('Zigzag'), Js('Zipzap')]))
pass
pass


# Add lib to the module scope
toolNicknames = var.to_python()