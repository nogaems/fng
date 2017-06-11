__all__ = ['mutantNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen', 'namesNeutral', 'namesMale', 'namesFemale'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['names1', 'tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', var.get('namesFemale'))
    else:
        if PyJsStrictEq(var.get('tp'),Js(2.0)):
            var.put('names1', var.get('namesNeutral'))
        else:
            var.put('names1', var.get('namesMale'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('names', var.get('names1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('namesFemale', Js([Js('Absent'), Js('Adamance '), Js('Aide'), Js('Angel'), Js('Anomaly'), Js('Ash'), Js('Ashes'), Js('Aurora'), Js('Beak'), Js('Bling'), Js('Blinkey'), Js('Blossom'), Js('Bones'), Js('Books'), Js('Bookworm'), Js('Box'), Js('Boxey'), Js('Bubblegum'), Js('Bucks'), Js('Bugs'), Js('Butterfly'), Js('Cascade'), Js('Chance'), Js('Cinders'), Js('Clarity'), Js('Cloak'), Js('Cloud'), Js('Clumsy'), Js('Dancer'), Js('Darling'), Js('Daydream'), Js('Desire'), Js('Doc'), Js('Doctor'), Js('Dot'), Js('Dragonfly'), Js('Dust'), Js('Elsewhere'), Js('Ember'), Js('Enigma'), Js('Exo'), Js('Facade'), Js('Face'), Js('Faith'), Js('Feather'), Js('Feathers'), Js('Fiddles'), Js('Fix'), Js('Flower'), Js('Fluque'), Js('Fortune'), Js('Foxy'), Js('Freak'), Js('Freakshow'), Js('Freckles'), Js('Gadget'), Js('Gentle'), Js('Ghost'), Js('Gloom'), Js('Grace'), Js('Heat'), Js('Hive'), Js('Hog'), Js('Honey'), Js('Hope'), Js('Huntress'), Js('Hybrid'), Js('Hydra'), Js('Imp'), Js('Ion'), Js('Jams'), Js('Jester'), Js('Joy'), Js('Longshot'), Js('Lotus'), Js('Magma'), Js('Magpie'), Js('Mask'), Js('Mendy'), Js('Minx'), Js('Misty'), Js('Moon'), Js('Mopes'), Js('Muse'), Js('Naughty'), Js('Needle'), Js('Nemo'), Js('Nightmare'), Js('Nightowl'), Js('Nocturne'), Js('Oddity'), Js('Patch'), Js('Patches'), Js('Penance'), Js('Pepper'), Js('Petal'), Js('Pickle'), Js('Piggy'), Js('Pixy'), Js('Plasma'), Js('Prodigy'), Js('Puzzle'), Js('Puzzles'), Js('Pygmy'), Js('Raine'), Js('Random'), Js('Rascal'), Js('Riddle'), Js('Risque'), Js('Rogue'), Js('Rubble'), Js('Saber'), Js('Serpente'), Js('Silence'), Js('Silver'), Js('Siren'), Js('Skins'), Js('Skit'), Js('Skitters'), Js('Sky'), Js('Slime'), Js('Slimey'), Js('Sly'), Js('Smokes'), Js('Snail'), Js('Snout'), Js('Snow'), Js('Soot'), Js('Specter'), Js('Spikes'), Js('Spirit'), Js('Spot'), Js('Spots'), Js('Sprite'), Js('Starlight'), Js('Sunshine'), Js('Tadpole'), Js('Tags'), Js('Tattoo'), Js('Tinder'), Js('Tinkle'), Js('Tooths'), Js('Toothsey'), Js('Toots'), Js('Tootsey'), Js('Trace'), Js('Twinkle'), Js('Utopia'), Js('Vex'), Js('Vipra'), Js('Vyolet'), Js('Weeds'), Js('Whisper'), Js('Wicked'), Js('Wings'), Js('Wink'), Js('Wish'), Js('Witch'), Js('Wither'), Js('Woe'), Js('Zero')]))
var.put('namesMale', Js([Js('Absent'), Js('Adamance '), Js('Aide'), Js('Angel'), Js('Anomaly'), Js('Ash'), Js('Atlas'), Js('Beak'), Js('Beast'), Js('Bishop'), Js('Bling'), Js('Blinkey'), Js('Blob'), Js('Blood'), Js('Bolt'), Js('Bones'), Js('Books'), Js('Bookworm'), Js('Box'), Js('Bravo'), Js('Bucks'), Js('Buffalo'), Js('Bugs'), Js('Bullet'), Js('Bulletproof'), Js('Cable'), Js('Captain'), Js('Chance'), Js('Chaos'), Js('Cinders'), Js('Cloak'), Js('Cloud'), Js('Clumsy'), Js('Cobalt'), Js('Cyclops'), Js('Dagger'), Js('Dancer'), Js('Daydream'), Js('Doc'), Js('Doctor'), Js('Dragonfly'), Js('Dust'), Js('Elsewhere'), Js('Exo'), Js('Facade'), Js('Face'), Js('Fallen'), Js('Feather'), Js('Feathers'), Js('Fiddles'), Js('Fix'), Js('Flood'), Js('Fluke'), Js('Freak'), Js('Freakshow'), Js('Frenzy'), Js('Gadget'), Js('Gentle'), Js('Ghost'), Js('Glob'), Js('Gloom'), Js('Gremlin'), Js('Grub'), Js('Hawk'), Js('Heat'), Js('Hermit'), Js('Hijack'), Js('Hive'), Js('Hog'), Js('Hunter'), Js('Husk'), Js('Hybrid'), Js('Hydro'), Js('Imp'), Js('Inn'), Js('Ion'), Js('Jams'), Js('Jester'), Js('Jet'), Js('Lance'), Js('Leech'), Js('Longshot'), Js('Maggot'), Js('Magma'), Js('Marsh'), Js('Mask'), Js('Mercury'), Js('Mime'), Js('Mist'), Js('Moon'), Js('Moose'), Js('Mopes'), Js('Muzzle'), Js('Naughty'), Js('Needle'), Js('Nemo'), Js('Newman'), Js('Nightmare'), Js('Nightowl'), Js('Nocturne'), Js('Oaf'), Js('Oak'), Js('Omega'), Js('Ooze'), Js('Patch'), Js('Patches'), Js('Penance'), Js('Phantom'), Js('Pickle'), Js('Piggy'), Js('Plasma'), Js('Prodigy'), Js('Puzzle'), Js('Puzzles'), Js('Pygmy'), Js('Pyro'), Js('Rain'), Js('Random'), Js('Rascal'), Js('Rat'), Js('Riddle'), Js('Rig'), Js('Rigs'), Js('Risk'), Js('Roach'), Js('Rogue'), Js('Rubble'), Js('Saber'), Js('Scooter'), Js('Serpent'), Js('Silence'), Js('Silver'), Js('Skeleton'), Js('Sketch'), Js('Skins'), Js('Skit'), Js('Skitters'), Js('Sky'), Js('Slime'), Js('Sly'), Js('Smokes'), Js('Snail'), Js('Snout'), Js('Snow'), Js('Soot'), Js('Specter'), Js('Spike'), Js('Spikes'), Js('Spirit'), Js('Spot'), Js('Spots'), Js('Sprite'), Js('Stonewall'), Js('Striker'), Js('Tadpole'), Js('Tags'), Js('Tattoo'), Js('Thorn'), Js('Thunder'), Js('Tinder'), Js('Toad'), Js('Tooth'), Js('Triclops'), Js('Viper'), Js('Weeds'), Js('Whisper'), Js('Wicked'), Js('Wings'), Js('Wink'), Js('Wither'), Js('Worm'), Js('Zero')]))
var.put('namesNeutral', Js([Js('Absent'), Js('Adamance '), Js('Aide'), Js('Angel'), Js('Anomaly'), Js('Ash'), Js('Beak'), Js('Bling'), Js('Blinkey'), Js('Blob'), Js('Bones'), Js('Books'), Js('Bookworm'), Js('Box'), Js('Bucks'), Js('Bugs'), Js('Chance'), Js('Cinders'), Js('Cloak'), Js('Cloud'), Js('Clumsy'), Js('Cyclops'), Js('Dancer'), Js('Daydream'), Js('Desire'), Js('Doc'), Js('Doctor'), Js('Dragonfly'), Js('Dust'), Js('Elsewhere'), Js('Exo'), Js('Facade'), Js('Face'), Js('Feather'), Js('Feathers'), Js('Fiddles'), Js('Fix'), Js('Fluke'), Js('Freak'), Js('Freakshow'), Js('Frenzy'), Js('Gadget'), Js('Gentle'), Js('Ghost'), Js('Gloom'), Js('Heat'), Js('Hive'), Js('Hog'), Js('Hybrid'), Js('Imp'), Js('Ion'), Js('Jams'), Js('Jester'), Js('Leech'), Js('Longshot'), Js('Maggot'), Js('Magma'), Js('Mask'), Js('Mime'), Js('Moon'), Js('Moonshine'), Js('Moose'), Js('Mopes'), Js('Naughty'), Js('Needle'), Js('Nemo'), Js('Nightmare'), Js('Nightowl'), Js('Nocturne'), Js('Patch'), Js('Penance'), Js('Pickle'), Js('Piggy'), Js('Plasma'), Js('Prodigy'), Js('Puzzle'), Js('Puzzles'), Js('Pygmy'), Js('Random'), Js('Rascal'), Js('Riddle'), Js('Risk'), Js('Rogue'), Js('Rubble'), Js('Saber'), Js('Silence'), Js('Silver'), Js('Skins'), Js('Skit'), Js('Skitters'), Js('Sky'), Js('Slime'), Js('Sly'), Js('Smokes'), Js('Smokey'), Js('Snail'), Js('Snout'), Js('Snow'), Js('Soot'), Js('Specter'), Js('Spikes'), Js('Spirit'), Js('Spot'), Js('Spots'), Js('Sprite'), Js('Tadpole'), Js('Tags'), Js('Tattoo'), Js('Tinder'), Js('Tooth'), Js('Triclops'), Js('Weeds'), Js('Whisper'), Js('Wicked'), Js('Wings'), Js('Wink'), Js('Wither'), Js('Zero')]))
pass
pass


# Add lib to the module scope
mutantNames = var.to_python()