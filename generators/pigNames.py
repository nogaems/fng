__all__ = ['pigNames']

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
var.put('nm1', Js([Js('Chris P. Bacon'), Js('Ace'), Js('Truffle'), Js('Trufflers'), Js('Acorn'), Js('Admiral'), Js('Snortimer'), Js('Ascot'), Js('Axel'), Js('Bacon'), Js('Badger'), Js('Bailey'), Js('Bing'), Js('Blitz'), Js('Blizz'), Js('Bowser'), Js('Boxer'), Js('Bramble'), Js('Brew'), Js('Bronco'), Js('Buddy'), Js('Bullet'), Js('Button'), Js('Buttons'), Js('Casanova'), Js('Cashew'), Js('Caveman'), Js('Chili'), Js('Chop'), Js('Choplin'), Js('Chubs'), Js('Cookie'), Js('Cotton'), Js('Crackle'), Js('Deacon'), Js('Deuce'), Js('Dipper'), Js('Dodge'), Js('Dodger'), Js('Doom'), Js('Duffy'), Js('Einswine'), Js('Fizzle'), Js('Flye'), Js('Fudge'), Js('Gizmo'), Js('Glutton'), Js('Goliath'), Js('Gorge'), Js('Gorger'), Js('Greedo'), Js('Grouch'), Js('Grumby'), Js('Gumball'), Js('Hambo'), Js('Hamilton'), Js('Hamlet'), Js('Hammer'), Js('Hammibal'), Js('Hannibal'), Js('Hawke'), Js('Hector'), Js('Hercules'), Js('Hog'), Js('Hogger'), Js('Hogzilla'), Js('Hulk'), Js('Iggy'), Js('Judge'), Js('Lad'), Js('Macho'), Js('Magnum'), Js('Magnum Pig'), Js('Marble'), Js('Mello'), Js('Mellow'), Js('Mud'), Js('Mudpie'), Js('Mudster'), Js('Nibble'), Js('Nibbler'), Js('Noodle'), Js('Norton'), Js('Nugget'), Js('Oinkers'), Js('Onyx'), Js('Oreo'), Js('Paddington'), Js('Patches'), Js('Pepper'), Js('Pie'), Js('Piggles'), Js('Pigsley'), Js('Popcorn'), Js('Porkchop'), Js('Puddle'), Js('Pudge'), Js('Rambo'), Js('Rambore'), Js('Ringo'), Js('Rosco'), Js('Rugby'), Js('Russell'), Js('Scamper'), Js('Scout'), Js('Slob'), Js('Slobber'), Js('Smokey'), Js('Smudge'), Js('Snuff'), Js('Snuffles'), Js('Stuffy'), Js('Titan'), Js('Waddle'), Js('Waddles'), Js('Wedge'), Js('Whopper'), Js('Wilburt'), Js('Wobble'), Js('Yoda')]))
var.put('nm2', Js([Js('Abby'), Js('Amber'), Js('Trufflers'), Js('Badge'), Js('Beauty'), Js('Beebee'), Js('Bell'), Js('Bella'), Js('Bertha'), Js('Betty'), Js('Blush'), Js('Brandy'), Js('Brew'), Js('Button'), Js('Buttons'), Js('Caramel'), Js('Checkers'), Js('Chili'), Js('Chips'), Js('Coco'), Js('Cookie'), Js('Coral'), Js('Cotton'), Js('Daisy'), Js('Dakota'), Js('Dawn'), Js('Dee'), Js('Deedee'), Js('Dew'), Js('Dodger'), Js('Doppler'), Js('Dot'), Js('Dots'), Js('Dottie'), Js('Dove'), Js('Duffy'), Js('Dutchess'), Js('Frazzle'), Js('Frizzle'), Js('Fuchsia'), Js('Ginger'), Js('Gorgy'), Js('Grace'), Js('Granny'), Js('Gummy'), Js('Iggy'), Js('June'), Js('Jynx'), Js('Lily'), Js('Lola'), Js('Lulu'), Js('Maggie'), Js('Maple'), Js('Marbles'), Js('Mello'), Js('Mellow'), Js('Missy'), Js('Mittens'), Js('Momma'), Js('Muckie'), Js('Nibble'), Js('Nibbles'), Js('Noodle'), Js('Noodles'), Js('Nugget'), Js('Oinkee'), Js('Olive'), Js('Opal'), Js('Orbit'), Js('Oreo'), Js('Paprika'), Js('Peaches'), Js('Pepper'), Js('Pie'), Js('Pink'), Js('Pinky'), Js('Pookie'), Js('Popcorn'), Js('Poppy'), Js('Porkette'), Js('Princess'), Js('Prudence'), Js('Pudge'), Js('Pudgy'), Js('Rose'), Js('Roseate'), Js('Rosie'), Js('Rune'), Js('Salmone'), Js('Skye'), Js('Slobs'), Js('Sludges'), Js('Slushie'), Js('Smudge'), Js('Smudges'), Js('Snoots'), Js('Snuffle'), Js('Spot'), Js('Stuffles'), Js('Sugar'), Js('Thistle'), Js('Trixie'), Js('Tulip'), Js('Twinkie'), Js('Twinkle'), Js('Ursula'), Js('Wiggle'), Js('Waddle'), Js('Waddles'), Js('Wiggles'), Js('Wobble')]))
pass
pass


# Add lib to the module scope
pigNames = var.to_python()