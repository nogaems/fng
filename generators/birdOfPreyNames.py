__all__ = ['birdOfPreyNames']

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
var.put('nm1', Js([Js('Ace'), Js('Achilles'), Js('Admiral'), Js('Ajax'), Js('Ammo'), Js('Apache'), Js('Apollo'), Js('Aquila'), Js('Arcane'), Js('Archer'), Js('Argos'), Js('Artemis'), Js('Ash'), Js('Atlas'), Js('Avalanche'), Js('Awe'), Js('Bandit'), Js('Bane'), Js('Blaze'), Js('Blight'), Js('Blitz'), Js('Blood'), Js('Bolt'), Js('Bones'), Js('Boon'), Js('Brawn'), Js('Brutus'), Js('Buck'), Js('Bullet'), Js('Bullseye'), Js('Butch'), Js('Buzz'), Js('Caine'), Js('Champ'), Js('Chaos'), Js('Chase'), Js('Cloud'), Js('Coal'), Js('Comet'), Js('Courage'), Js('Dagger'), Js('Darth'), Js('Diablo'), Js('Doom'), Js('Drake'), Js('Dread'), Js('Duke'), Js('Dusk'), Js('Dust'), Js('Echo'), Js('Eclipse'), Js('Edge'), Js('Force'), Js('Frenzy'), Js('Fury'), Js('Genghis'), Js('Ghost'), Js('Goliath'), Js('Gray'), Js('Griffin'), Js('Grim'), Js('Gunner'), Js('Hades'), Js('Hannibal'), Js('Havock'), Js('Hawke'), Js('Hawkeye'), Js('Hector'), Js('Hero'), Js('Hooch'), Js('Hulk'), Js('Hunter'), Js('Hyde'), Js('Ice'), Js('Jax'), Js('Jeckyll'), Js('Judge'), Js('Khan'), Js('Kindle'), Js('King'), Js('Lecter'), Js('Legend'), Js('Loki'), Js('Lucifer'), Js('Magnum'), Js('Maverick'), Js('Mayhem'), Js('Merlin'), Js('Midnight'), Js('Mirage'), Js('Myst'), Js('Nemesis'), Js('Neo'), Js('Nero'), Js('Nightmare'), Js('Nyx'), Js('Obsidian'), Js('Onyx'), Js('Orion'), Js('Pandora'), Js('Panther'), Js('Pepper'), Js('Phantom'), Js('Phoenix'), Js('Pride'), Js('Pyro'), Js('Rage'), Js('Rampage'), Js('Ranger'), Js('Raven'), Js('Razor'), Js('Reaper'), Js('Rebel'), Js('Ripley'), Js('Riptide'), Js('Rogue'), Js('Ryder'), Js('Sabath'), Js('Saber'), Js('Sable'), Js('Savage'), Js('Scandal'), Js('Scourge'), Js('Shade'), Js('Shadow'), Js('Shiv'), Js('Sky'), Js('Slate'), Js('Sly'), Js('Sniper'), Js('Snow'), Js('Steele'), Js('Storm'), Js('Striker'), Js('Surge'), Js('Talon'), Js('Tank'), Js('Terror'), Js('Thunder'), Js('Titan'), Js('Titanium'), Js('Torment'), Js('Triumph'), Js('Vapor'), Js('Viper'), Js('Vlad'), Js('Whisper'), Js('Wicked'), Js('Wrath'), Js('Xerxes')]))
var.put('nm2', Js([Js('Acadia'), Js('Alexis'), Js('Alibi'), Js('Amazone'), Js('Amber'), Js('Angel'), Js('Aphrodite'), Js('Arcane'), Js('Ares'), Js('Ash'), Js('Ashes'), Js('Astral'), Js('Athena'), Js('Aura'), Js('Aurora'), Js('Azure'), Js('Banshee'), Js('Blaze'), Js('Blitz'), Js('Bones'), Js('Calypso'), Js('Charity'), Js('Clemency'), Js('Cleo'), Js('Cleopatra'), Js('Codex'), Js('Dahlia'), Js('Dakota'), Js('Dawn'), Js('Diva'), Js('Ebony'), Js('Echo'), Js('Eclipse'), Js('Eve'), Js('Faith'), Js('Faye'), Js('Fire'), Js('Gidget'), Js('Ginger'), Js('Grace'), Js('Harmony'), Js('Hazel'), Js('Helena'), Js('Hope'), Js('Huntress'), Js('Ice'), Js('Ivory'), Js('Jade'), Js('Jewel'), Js('Jinx'), Js('Justice'), Js('Jynx'), Js('Karma'), Js('Labyrinth'), Js('Lady'), Js('Liberty'), Js('Love'), Js('Luna'), Js('Maiden'), Js('Maya'), Js('Medusa'), Js('Melancholy'), Js('Mercy'), Js('Midnight'), Js('Mischief'), Js('Mistress'), Js('Moone'), Js('Myst'), Js('Mystique'), Js('Nighte'), Js('Nova'), Js('Nyx'), Js('Olympia'), Js('Onyxia'), Js('Ozone'), Js('Pandora'), Js('Patience'), Js('Phoenix'), Js('Princess'), Js('Raine'), Js('Raven'), Js('Rebel'), Js('Ribbon'), Js('Ripley'), Js('Robin'), Js('Rogue'), Js('Ruby'), Js('Rune'), Js('Ruth'), Js('Sable'), Js('Sabre'), Js('Sanguine'), Js('Scarlett'), Js('Serenity'), Js('Shade'), Js('Shadow'), Js('Shaye'), Js('Siren'), Js('Skye'), Js('Snow'), Js('Storm'), Js('Termina'), Js('Truce'), Js('Twilight'), Js('Tyra'), Js('Vanity'), Js('Velvet'), Js('Victoria'), Js('Violet'), Js('Vixen'), Js('Wilde'), Js('Willow'), Js('Winter'), Js('Xena')]))
pass
pass


# Add lib to the module scope
birdOfPreyNames = var.to_python()