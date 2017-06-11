__all__ = ['ninjaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names5', 'names2', 'names3', 'names1'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', (((Js('The ')+var.get('names1').get(var.get('rnd')))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                if (var.get('i')<Js(8.0)):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('names', (var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2'))))
                else:
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('names', ((var.get('names3').get(var.get('rnd'))+Js(' '))+var.get('names5').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Agile'), Js('Black'), Js('Blue'), Js('Bronze'), Js('Cloaked'), Js('Crimson'), Js('Crouching'), Js('Dark'), Js('Deadly'), Js('Elegant'), Js('Falling'), Js('Fast'), Js('Floating'), Js('Flying'), Js('Ghost'), Js('Golden'), Js('Graceful'), Js('Hidden'), Js('Hollow'), Js('Invisible'), Js('Iron'), Js('Jade'), Js('Light'), Js('Masked'), Js('Muffled'), Js('Muzzled'), Js('Mysterious'), Js('Mystic'), Js('Nimble'), Js('Phantom'), Js('Quick'), Js('Quiet'), Js('Rapid'), Js('Red'), Js('Ruby'), Js('Sanguine'), Js('Sapphire'), Js('Scarlet'), Js('Serpent'), Js('Shrouded'), Js('Silent'), Js('Silver'), Js('Slender'), Js('Smiling'), Js('Smooth'), Js('Snake'), Js('Soothing'), Js('Steel'), Js('Still'), Js('Swift'), Js('Thin'), Js('Tranquil'), Js('Unheard'), Js('Unknown'), Js('Unmoving'), Js('Unseen'), Js('Veiled'), Js('White'), Js('Winged'), Js('Wise')]))
var.put('names2', Js([Js('Angel'), Js('Assassin'), Js('Avalanche'), Js('Basilisk'), Js('Beast'), Js('Blaze'), Js('Breath'), Js('Cat'), Js('Child'), Js('Cipher'), Js('Crane'), Js('Dagger'), Js('Death'), Js('Demise'), Js('Demon'), Js('Devil'), Js('Dragon'), Js('Drake'), Js('Dream'), Js('Echo'), Js('Enigma'), Js('Eye'), Js('Eyes'), Js('Figure'), Js('Fire'), Js('Flame'), Js('Ghost'), Js('Grin'), Js('Hawk'), Js('Hunter'), Js('Illusion'), Js('Image'), Js('Jackal'), Js('Knife'), Js('Laugh'), Js('Lion'), Js('Lotus'), Js('Mamba'), Js('Mark'), Js('Mask'), Js('Master'), Js('Mime'), Js('Mimic'), Js('Mind'), Js('Mirage'), Js('Moon'), Js('Mute'), Js('Oracle'), Js('Paradox'), Js('Phantom'), Js('Phoenix'), Js('Player'), Js('Rain'), Js('Ranger'), Js('Raven'), Js('Reflection'), Js('Rock'), Js('Rover'), Js('Saber'), Js('Samaritan'), Js('Scar'), Js('Scorpion'), Js('Scythe'), Js('Secret'), Js('Serpent'), Js('Shade'), Js('Shadow'), Js('Silence'), Js('Smile'), Js('Smirk'), Js('Smoke'), Js('Snake'), Js('Snow'), Js('Soldier'), Js('Spider'), Js('Stalker'), Js('Star'), Js('Striker'), Js('Sword'), Js('Thunder'), Js('Tiger'), Js('Viper'), Js('Vision'), Js('Wanderer'), Js('Warden'), Js('Watcher'), Js('Whisper'), Js('Wind'), Js('Wolf'), Js('Wrath')]))
var.put('names3', Js([Js('Black'), Js('Blood'), Js('Bullet'), Js('Crimson'), Js('Dark'), Js('Dead'), Js('Death'), Js('Dream'), Js('Ghost'), Js('Golden'), Js('Hollow'), Js('Iron'), Js('Jade'), Js('Kill'), Js('Lethal'), Js('Light'), Js('Lightning'), Js('Phantom'), Js('Quick'), Js('Rabid'), Js('Rapid'), Js('Red'), Js('Scarlet'), Js('Silent'), Js('Silver'), Js('Snow'), Js('Steel'), Js('Still'), Js('Swift'), Js('Thunder')]))
var.put('names4', Js([Js('bang'), Js('bash'), Js('beat'), Js('blade'), Js('claw'), Js('crash'), Js('eye'), Js('eyes'), Js('fall'), Js('flake'), Js('flash'), Js('flow'), Js('kill'), Js('lock'), Js('mark'), Js('moon'), Js('saw'), Js('scar'), Js('shade'), Js('shadow'), Js('shiv'), Js('shot'), Js('sign'), Js('slinger'), Js('stain'), Js('strike'), Js('streak'), Js('strikes'), Js('stroke'), Js('tooth')]))
var.put('names5', Js([Js('Bang'), Js('Bash'), Js('Beat'), Js('Blade'), Js('Claw'), Js('Crash'), Js('Eye'), Js('Eyes'), Js('Fall'), Js('Flake'), Js('Flash'), Js('Flow'), Js('Kill'), Js('Lock'), Js('Mark'), Js('Moon'), Js('Saw'), Js('Scar'), Js('Shade'), Js('Shadow'), Js('Shiv'), Js('Shot'), Js('Sign'), Js('Slinger'), Js('Stain'), Js('Strike'), Js('Streak'), Js('Strikes'), Js('Stroke'), Js('Tooth')]))
pass
pass


# Add lib to the module scope
ninjaNames = var.to_python()