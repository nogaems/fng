__all__ = ['warriorNicknames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('The Animal'), Js('The Anomaly'), Js('The Anvil'), Js('The Army'), Js('The Axe'), Js('The Barbarian'), Js('The Bear'), Js('The Bearclaw'), Js('The Beast'), Js('The Behemoth'), Js('The Blade'), Js('The Bloodlust'), Js('The Bloody'), Js('The Boar'), Js('The Boulder'), Js('The Boulderfist'), Js('The Brute'), Js('The Bull'), Js('The Butcher'), Js('The Challenger'), Js('The Champion'), Js('The Cobra'), Js('The Colossal'), Js('The Colossus'), Js('The Conqueror'), Js('The Corrupter'), Js('The Coyote'), Js('The Crooked'), Js('The Crow'), Js('The Cruel'), Js('The Cunning'), Js('The Cursed'), Js('The Dagger'), Js('The Danger'), Js('The Deceiver'), Js('The Defiant'), Js('The Delirious'), Js('The Demigod'), Js('The Demon'), Js('The Deserter'), Js('The Destroyer'), Js('The Devil'), Js('The Dire'), Js('The Dire Bear'), Js('The Dire One'), Js('The Dire Wolf'), Js('The Dog'), Js('The Dragon'), Js('The Dragonheart'), Js('The Drake'), Js('The Dread'), Js('The Edge'), Js('The Enigma'), Js('The Eternal Hunger'), Js('The Exalted'), Js('The Executioner'), Js('The Exile'), Js('The Fang'), Js('The Fearless'), Js('The Feisty'), Js('The Feral'), Js('The Fiend'), Js('The Fierce'), Js('The Fire'), Js('The Firestarter'), Js('The Flame'), Js('The Flurry'), Js('The Forsaken'), Js('The Freak'), Js('The Fury'), Js('The Ghost'), Js('The Giant'), Js('The Giantslayer'), Js('The Gold One'), Js('The Grave'), Js('The Gravedigger'), Js('The Gravekeeper'), Js('The Grim'), Js('The Grotesque'), Js('The Guardian'), Js('The Hallowed'), Js('The Hammer'), Js('The Hawk'), Js('The Heartless'), Js('The Hog'), Js('The Hollow'), Js('The Honorbound'), Js('The Honorless'), Js('The Horror'), Js('The Hound'), Js('The Hunger'), Js('The Hungry'), Js('The Hunter'), Js('The Hurricane'), Js('The Impure'), Js('The Insane'), Js('The Invincible'), Js('The Ironclad'), Js('The Ironfist'), Js('The Jackal'), Js('The Jester'), Js('The Legionnaire'), Js('The Limp'), Js('The Lion'), Js('The Lionheart'), Js('The Lone Wolf'), Js('The Magnificent'), Js('The Mammoth'), Js('The Maneater'), Js('The Maniac'), Js('The Marked'), Js('The Marked One'), Js('The Martyr'), Js('The Menace'), Js('The Merciful'), Js('The Miracle'), Js('The Monster'), Js('The Mountain'), Js('The Mutant'), Js('The Mute'), Js('The Nightmare'), Js('The Nightowl'), Js('The Noble'), Js('The Nobody'), Js('The Observer'), Js('The Owl'), Js('The Ox'), Js('The Paragon'), Js('The Patient'), Js('The Phantom'), Js('The Phoenix'), Js('The Prince'), Js('The Prodigy'), Js('The Pyro'), Js('The Rabid'), Js('The Raven'), Js('The Rebel'), Js('The Reckless'), Js('The Rider'), Js('The Rogue'), Js('The Sadist'), Js('The Sadistic'), Js('The Savage'), Js('The Scar'), Js('The Scarred One'), Js('The Sentinel'), Js('The Serpent'), Js('The Shadow'), Js('The Shady'), Js('The Shepherd'), Js('The Silencer'), Js('The Silent'), Js('The Silver One'), Js('The Skeleton'), Js('The Slayer'), Js('The Sleeper'), Js('The Spider'), Js('The Spook'), Js('The Storm'), Js('The Surgeon'), Js('The Swine'), Js('The Temper'), Js('The Tempest'), Js('The Terror'), Js('The Thief'), Js('The Thirst'), Js('The Thug'), Js('The Thunder'), Js('The Titan'), Js('The Tower'), Js('The Traitor'), Js('The Tyrant'), Js('The Undying'), Js('The Valiant'), Js('The Vengeful'), Js('The Venom Tongue'), Js('The Vermin'), Js('The Vicious'), Js('The Viper'), Js('The Vulture'), Js('The Whisper'), Js('The Widow Maker'), Js('The Wild'), Js('The Wildling'), Js('The Wolf'), Js('The Wonder'), Js('The Wyrm')]))
var.put('nm2', Js([Js('Battle'), Js('Bear'), Js('Blood'), Js('Bone'), Js('Boulder'), Js('Bright'), Js('Dark'), Js('Dead'), Js('Death'), Js('Demon'), Js('Doom'), Js('Dragon'), Js('Ember'), Js('Fire'), Js('Fist'), Js('Frost'), Js('Fuse'), Js('Giant'), Js('Gold'), Js('Gore'), Js('Grand'), Js('Great'), Js('Hell'), Js('Iron'), Js('Light'), Js('Mammoth'), Js('Molten'), Js('Night'), Js('Phoenix'), Js('Proud'), Js('Rage'), Js('Raven'), Js('Red'), Js('Rock'), Js('Rumble'), Js('Shadow'), Js('Sharp'), Js('Shield'), Js('Silent'), Js('Silver'), Js('Single'), Js('Skull'), Js('Spirit'), Js('Steel'), Js('Stone'), Js('Storm'), Js('Stout'), Js('Strong'), Js('Swift'), Js('Thunder'), Js('True'), Js('Void'), Js('War'), Js('Wild'), Js('Wolf')]))
var.put('nm3', Js([Js('bane'), Js('blade'), Js('blood'), Js('blow'), Js('bolt'), Js('bow'), Js('breaker'), Js('brow'), Js('chaser'), Js('claw'), Js('cleaver'), Js('crest'), Js('cut'), Js('eye'), Js('fang'), Js('fist'), Js('flayer'), Js('fury'), Js('gaze'), Js('grim'), Js('grimace'), Js('grip'), Js('hair'), Js('hallow'), Js('hammer'), Js('hand'), Js('head'), Js('heart'), Js('helm'), Js('hide'), Js('mane'), Js('mantle'), Js('might'), Js('pelt'), Js('rage'), Js('roar'), Js('scar'), Js('scream'), Js('shade'), Js('shadow'), Js('shield'), Js('shout'), Js('snarl'), Js('song'), Js('sorrow'), Js('stare'), Js('stride'), Js('strike'), Js('sword'), Js('sworn'), Js('talon'), Js('thorn'), Js('tongue'), Js('visage')]))
var.put('nm4', Js([Js(''), Js(''), Js(' ')]))
pass
pass


# Add lib to the module scope
warriorNicknames = var.to_python()