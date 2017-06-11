__all__ = ['tribeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen', 'names3'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('names', (((((Js('The ')+var.get('names1').get(var.get('rnd')))+Js(' '))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Ancient'), Js('Angry'), Js('Arcane'), Js('Arctic'), Js('Berserk'), Js('Big'), Js('Bitter'), Js('Black'), Js('Blessed'), Js('Blind'), Js('Blue'), Js('Brave'), Js('Bright'), Js('Broken'), Js('Bronze'), Js('Brown'), Js('Burned'), Js('Clay'), Js('Cold'), Js('Crazy'), Js('Crimson'), Js('Cruel'), Js('Dark'), Js('Dead'), Js('Diamond'), Js('Dirty'), Js('Ebon'), Js('Eternal'), Js('Evil'), Js('Falling'), Js('False'), Js('First'), Js('Free'), Js('Frozen'), Js('Gentle'), Js('Giant'), Js('Gifted'), Js('Golden'), Js('Grave'), Js('Gray'), Js('Green'), Js('Grim'), Js('Half'), Js('Hard'), Js('Hell'), Js('Hidden'), Js('High'), Js('Impure'), Js('Infamous'), Js('Invincible'), Js('Iron'), Js('Large'), Js('Last'), Js('Light'), Js('Lost'), Js('Loyal'), Js('Magic'), Js('Master'), Js('Mean'), Js('Middle'), Js('Miracle'), Js('Misty'), Js('Molten'), Js('Murky'), Js('Mute'), Js('Night'), Js('Nightmare'), Js('Original'), Js('Pale'), Js('Poison'), Js('Prime'), Js('Pure'), Js('Quiet'), Js('Rabid'), Js('Rapid'), Js('Reckless'), Js('Red'), Js('Risen'), Js('Rising'), Js('Rude'), Js('Salty'), Js('Sapphire'), Js('Savage'), Js('Shadow'), Js('Silent'), Js('Silver'), Js('Small'), Js('Smelly'), Js('Standing'), Js('Steel'), Js('Stone'), Js('Strong'), Js('Swift'), Js('True'), Js('Twilight'), Js('Twin'), Js('Undead'), Js('Vicious'), Js('White'), Js('Yellow')]))
var.put('names2', Js([Js('Ancestor'), Js('Angel'), Js('Ant'), Js('Arrow'), Js('Ash'), Js('Aura'), Js('Axe'), Js('Bat'), Js('Bear'), Js('Bison'), Js('Bone'), Js('Bones'), Js('Boulder'), Js('Bow'), Js('Brothers'), Js('Cave'), Js('Claw'), Js('Cloak'), Js('Coyote'), Js('Crow'), Js('Crown'), Js('Dagger'), Js('Demon'), Js('Dragon'), Js('Eagle'), Js('Ear'), Js('Earth'), Js('Ember'), Js('Eye'), Js('Feet'), Js('Finger'), Js('Fire'), Js('Fish'), Js('Fist'), Js('Foot'), Js('Forest'), Js('Fox'), Js('Fury'), Js('Ghost'), Js('Giant'), Js('God'), Js('Hammer'), Js('Hand'), Js('Hawk'), Js('Heaven'), Js('Hill'), Js('Hounds'), Js('Hunt'), Js('Island'), Js('Lake'), Js('Lightning'), Js('Lion'), Js('Mage'), Js('Mammoth'), Js('Moon'), Js('Mountain'), Js('Mouth'), Js('Oracle'), Js('Owl'), Js('Paw'), Js('Phantom'), Js('Phoenix'), Js('Rage'), Js('Raven'), Js('Ribbon'), Js('River'), Js('Rock'), Js('Sand'), Js('Scar'), Js('Scorpion'), Js('Sea'), Js('Seer'), Js('Shark'), Js('Shield'), Js('Sisters'), Js('Skeleton'), Js('Skull'), Js('Snake'), Js('Snow'), Js('Spear'), Js('Spider'), Js('Spirit'), Js('Stag'), Js('Stalker'), Js('Star'), Js('Storm'), Js('Sun'), Js('Swamp'), Js('Sword'), Js('Thunder'), Js('Titan'), Js('Tooth'), Js('Tower'), Js('Watch'), Js('Water'), Js('Whisper'), Js('Wing'), Js('Witch'), Js('Wolf'), Js('Woods')]))
var.put('names3', Js([Js('Tribe'), Js('Kin'), Js('Clan'), Js('Warriors'), Js('Children'), Js('Caste'), Js('Horde'), Js('Tribe')]))
pass
pass


# Add lib to the module scope
tribeNames = var.to_python()