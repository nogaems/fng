__all__ = ['amphibianNames']

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
var.put('nm1', Js([Js('Alien'), Js('Arrow'), Js('Bazoo'), Js('Beaker'), Js('Belch'), Js('Belcher'), Js('Binky'), Js('Bloats'), Js('Blob'), Js('Bob'), Js('Bog'), Js('Bogs'), Js('Booger'), Js('Boogy'), Js('Bubba'), Js('Bubbles'), Js('Buffle'), Js('Buffles'), Js('Bully'), Js('Buster'), Js('Charizard'), Js('Charmander'), Js('Chubber'), Js('Chubbles'), Js('Chubbs'), Js('Chubby'), Js('Chunky'), Js('Claw'), Js('Clawde'), Js('Clawdius'), Js('Claws'), Js('Cozmo'), Js('Cricket'), Js('Croak'), Js('Croaker'), Js('Croaks'), Js('Crook'), Js('Cruncher'), Js('Crunchy'), Js('Curmet'), Js('Dart'), Js('Darts'), Js('Doc'), Js('Fatty'), Js('Fiddles'), Js('Fire'), Js('Flibbit'), Js('Flippy'), Js('Flips'), Js('Flubber'), Js('Flubs'), Js('Flye'), Js('Freak'), Js('Freckles'), Js('Frogger'), Js('Froggie'), Js('Frogzilla'), Js('Gobbles'), Js('Goble'), Js('Gobles'), Js('Godzilla'), Js('Golem'), Js('Goliath'), Js('Gooey'), Js('Grog'), Js('Hobbit'), Js('Hopkins'), Js('Hopper'), Js('Hopscotch'), Js('Hudini'), Js('Jabba'), Js('JarJar'), Js('Kermi'), Js('Kermie'), Js('Kermit'), Js('Leaps'), Js('Leapy'), Js('Mantis'), Js('Marsh'), Js('Mello'), Js('Mellow'), Js('Mog'), Js('MrSticky'), Js('Mud'), Js('Muds'), Js('Newt'), Js('Newton'), Js('Orbit'), Js('Patches'), Js('Pickle'), Js('Pickles'), Js('Pogo'), Js('Predator'), Js('Prince'), Js('Puddles'), Js('Pudge'), Js('Pug'), Js('Quibbit'), Js('Ribbit'), Js('Shmoo'), Js('Shmooch'), Js('Skippy'), Js('Skittles'), Js('Slick'), Js('Slimes'), Js('Slippy'), Js('Slub'), Js('Slug'), Js('Slugg'), Js('Sluggs'), Js('Slugs'), Js('Smeagol'), Js('Smudge'), Js('Spot'), Js('Sticky'), Js('Stinky'), Js('Stubby'), Js('Stumper'), Js('Swampie'), Js('Swamps'), Js('Thor'), Js('Toad'), Js('Weirdo'), Js('Whopper'), Js('Wiggles'), Js('Wobble'), Js('Wobbles'), Js('Yoda')]))
var.put('nm2', Js([Js('Algee'), Js('Amazone'), Js('Amazonia'), Js('Babe'), Js('Belchy'), Js('Blinks'), Js('Blinky'), Js('Bloats'), Js('Bubble'), Js('Bubbles'), Js('Buffy'), Js('Bufonia'), Js('Cherry'), Js('Chops'), Js('Chubbles'), Js('Chubby'), Js('Clawdia'), Js('Cookie'), Js('Cosmo'), Js('Cricket'), Js('Croaks'), Js('Daphne'), Js('Dirty'), Js('Faye'), Js('Fern'), Js('Fiddle'), Js('Flubby'), Js('Flye'), Js('Freakey'), Js('Freckles'), Js('Frogzilla'), Js('Fye'), Js('Fyre'), Js('Geo'), Js('Gobbles'), Js('Gooey'), Js('Hippity'), Js('Hipscotch'), Js('Hoppity'), Js('Iggy'), Js('Karma'), Js('Kirby'), Js('Kiss'), Js('Kisses'), Js('Leaps'), Js('Leapy'), Js('Lilo'), Js('Lily'), Js('Lilypad'), Js('Lips'), Js('Mello'), Js('Muddy'), Js('Muds'), Js('Mystique'), Js('Noodles'), Js('Patches'), Js('Peeps'), Js('Penelope'), Js('Pepper'), Js('Pickle'), Js('Pickles'), Js('Princess'), Js('Puds'), Js('Pugs'), Js('Pumpkin'), Js('Raisin'), Js('Ribbit'), Js('Ribbits'), Js('Sally'), Js('Shirly'), Js('Shmoo'), Js('Shmooches'), Js('Slimey'), Js('Slippy'), Js('Smiley'), Js('Smooch'), Js('Snaile'), Js('Sparkle'), Js('Sparkles'), Js('Speckles'), Js('Spot'), Js('Spots'), Js('Squee'), Js('Squiggy'), Js('Stitch'), Js('Stitches'), Js('Teeny'), Js('Tiggles'), Js('Tiny'), Js('Tootsie'), Js('Trixie'), Js('Twiggy'), Js('Twinkle'), Js('Waddle'), Js('Waddles'), Js('Wiggle'), Js('Wiggles'), Js('Wobble'), Js('Wobbles'), Js('Xena')]))
pass
pass


# Add lib to the module scope
amphibianNames = var.to_python()