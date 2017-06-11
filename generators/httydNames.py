__all__ = ['httydNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', var.get('nm3').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Adder'), Js('Alder'), Js('Arrow'), Js('Bewilder'), Js('Blaze'), Js('Blubber'), Js('Bone'), Js('Bull'), Js('Burro'), Js('Change'), Js('Cloud'), Js('Crooked'), Js('Dark'), Js('Dawn'), Js('Day'), Js('Dead'), Js('Death'), Js('Desert'), Js('Doom'), Js('Dragon'), Js('Dread'), Js('Dream'), Js('Dull'), Js('Dusk'), Js('Elder'), Js('Eternal'), Js('Fire'), Js('Flame'), Js('Flapper'), Js('Flutter'), Js('Forever'), Js('Frost'), Js('Fury'), Js('Ghost'), Js('Gloom'), Js('Glow'), Js('Gore'), Js('Great'), Js('Grim'), Js('Ground'), Js('Hallow'), Js('Hell'), Js('Hollow'), Js('Hook'), Js('Hypno'), Js('Inferno'), Js('Light'), Js('Little'), Js('Mild'), Js('Mud'), Js('Night'), Js('Rage'), Js('Razor'), Js('Rocket'), Js('Rumble'), Js('Sand'), Js('Sea'), Js('Shadow'), Js('Shiver'), Js('Shock'), Js('Silver'), Js('Snow'), Js('Song'), Js('Speed'), Js('Storm'), Js('Swift'), Js('Sword'), Js('Talon'), Js('Terror'), Js('Thunder'), Js('Torch'), Js('Tranquil'), Js('Tumble'), Js('Venom'), Js('Whirl'), Js('Wild')]))
var.put('nm2', Js([Js('back'), Js('beast'), Js('belly'), Js('breath'), Js('claw'), Js('cutter'), Js('drum'), Js('eye'), Js('eyes'), Js('fang'), Js('flight'), Js('glider'), Js('grunt'), Js('horn'), Js('hunter'), Js('jaw'), Js('jumper'), Js('nose'), Js('paw'), Js('ripper'), Js('roar'), Js('smasher'), Js('song'), Js('striker'), Js('tail'), Js('tongue'), Js('tooth'), Js('twister'), Js('whip'), Js('wing')]))
var.put('nm3', Js([Js('Awe'), Js('Bait'), Js('Bead'), Js('Bellow'), Js('Bigby'), Js('Blare'), Js('Blue'), Js('Bluster'), Js('Bolt'), Js('Bones'), Js('Boom'), Js('Boulder'), Js('Burst'), Js('Buster'), Js('Chase'), Js('Chinook'), Js('Cobble'), Js('Cower'), Js('Crackle'), Js('Crest'), Js('Crimson'), Js('Crisscross'), Js('Crumb'), Js('Curly'), Js('Dart'), Js('Dash'), Js('Dire'), Js('Ditch'), Js('Dodge'), Js('Dozer'), Js('Dread'), Js('Dribble'), Js('Drifter'), Js('Drool'), Js('Droplet'), Js('Dusty'), Js('Echo'), Js('Eclipse'), Js('Enigma'), Js('Fawn'), Js('Fay'), Js('Feather'), Js('Feint'), Js('Flare'), Js('Flash'), Js('Flinch'), Js('Flo'), Js('Fluff'), Js('Flurry'), Js('Gale'), Js('Ghast'), Js('Ghost'), Js('Glider'), Js('Glimmer'), Js('Glint'), Js('Glum'), Js('Gnaw'), Js('Gobbles'), Js('Goof'), Js('Gravel'), Js('Grim'), Js('Grime'), Js('Grouch'), Js('Grumpy'), Js('Grunt'), Js('Gust'), Js('Haze'), Js('Helix'), Js('Hogger'), Js('Honey'), Js('Hue'), Js('Itchy'), Js('Jitters'), Js('Juke'), Js('Knot'), Js('Looper'), Js('Magma'), Js('Manes'), Js('Muds'), Js('Munchy'), Js('Muzzle'), Js('Needle'), Js('Nibble'), Js('Night'), Js('Nimbles'), Js('Nip'), Js('Nozzle'), Js('Paradox'), Js('Pebble'), Js('Phanom'), Js('Pickle'), Js('Pinch'), Js('Pitch'), Js('Plume'), Js('Plummet'), Js('Prickle'), Js('Puds'), Js('Pugs'), Js('Quill'), Js('Rainbow'), Js('Riddle'), Js('Rumble'), Js('Saliva'), Js('Sally'), Js('Sapphire'), Js('Scruffy'), Js('Scuddle'), Js('Shade'), Js('Shadow'), Js('Shay'), Js('Shuffle'), Js('Sidestep'), Js('Skip'), Js('Sky'), Js('Skyler'), Js('Slobber'), Js('Slush'), Js('Smudge'), Js('Snare'), Js('Sneak'), Js('Snookum'), Js('Snout'), Js('Snowflake'), Js('Soot'), Js('Sparkle'), Js('Spice'), Js('Squall'), Js('Squeak'), Js('Sting'), Js('Storm'), Js('Subs'), Js('Surge'), Js('Surly'), Js('Swifty'), Js('Tails'), Js('Thorn'), Js('Thunder'), Js('Tickles'), Js('Tingle'), Js('Trace'), Js('Tremble'), Js('Tumble'), Js('Twilight'), Js('Twinkle'), Js('Twist'), Js('Twister'), Js('Typhoon'), Js('Umbra'), Js('Veil'), Js('Whallop'), Js('Whammy'), Js('Wiggle'), Js('Wriggle'), Js('Zap'), Js('Zigzag'), Js('Zip')]))
pass
pass


# Add lib to the module scope
httydNames = var.to_python()