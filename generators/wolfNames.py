__all__ = ['wolfNames']

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
var.put('nm1', Js([Js('Ace'), Js('Akira'), Js('Alistair'), Js('Alpha'), Js('Apache'), Js('Apollo'), Js('Archer'), Js('Artemis'), Js('Astro'), Js('Athene'), Js('Atlas'), Js('Avalanche'), Js('Axis'), Js('Bandit'), Js('Bane'), Js('Baron'), Js('Beacon'), Js('Bear'), Js('Blaze'), Js('Blitz'), Js('Bolt'), Js('Bones'), Js('Boomer'), Js('Boon'), Js('Booth'), Js('Boulder'), Js('Brawn'), Js('Brick'), Js('Brock'), Js('Browne'), Js('Bruno'), Js('Brutus'), Js('Buck'), Js('Bud'), Js('Buddy'), Js('Bullet'), Js('Buster'), Js('Butch'), Js('Buzz'), Js('Caesar'), Js('Camelot'), Js('Chase'), Js('Chewy'), Js('Chronos'), Js('Cloud'), Js('Colt'), Js('Comet'), Js('Conan'), Js('Courage'), Js('Dagger'), Js('Dane'), Js('Danger'), Js('Dash'), Js('Delta'), Js('Dexter'), Js('Diablo'), Js('Digger'), Js('Drake'), Js('Duke'), Js('Dust'), Js('Dutch'), Js('Echo'), Js('Edge'), Js('Excalibur'), Js('Fang'), Js('Farkas'), Js('Flash'), Js('Frost'), Js('Fury'), Js('Ghost'), Js('Goliath'), Js('Gray'), Js('Grunt'), Js('Hannibal'), Js('Havoc'), Js('Hawke'), Js('Hawkeye'), Js('Hector'), Js('Hercules'), Js('Hooch'), Js('Hulk'), Js('Hunter'), Js('Hyde'), Js('Ice'), Js('Jaws'), Js('Jax'), Js('Jeckyll'), Js('Jethro'), Js('Judge'), Js('Kaine'), Js('Kane'), Js('Khan'), Js('Killer'), Js('King'), Js('Lad'), Js('Laika'), Js('Lecter'), Js('Lightning'), Js('Logan'), Js('Loki'), Js('Lupin'), Js('Lupus'), Js('Magnus'), Js('Mako'), Js('Mason'), Js('Maverick'), Js('Max'), Js('Maximus'), Js('Mayhem'), Js('Menace'), Js('Midnight'), Js('Miles'), Js('Murdoch'), Js('Myst'), Js('Nanook'), Js('Nero'), Js('Nightmare'), Js('Nova'), Js('Oak'), Js('Obsidian'), Js('Odin'), Js('Omega'), Js('Omen'), Js('Onyx'), Js('Orbit'), Js('Outlaw'), Js('Patriot'), Js('Phantom'), Js('Prince'), Js('Pyro'), Js('Quicksilver'), Js('Rage'), Js('Ralph'), Js('Ranger'), Js('Razor'), Js('Rebel'), Js('Rex'), Js('Rider'), Js('Riggs'), Js('Ripley'), Js('Riptide'), Js('Rogue'), Js('Rover'), Js('Scar'), Js('Scout'), Js('Shade'), Js('Shadow'), Js('Shepherd'), Js('Shredder'), Js('Silver'), Js('Skye'), Js('Slate'), Js('Sly'), Js('Smoke'), Js('Splinter'), Js('Steele'), Js('Storm'), Js('Striker'), Js('Summit'), Js('Tank'), Js('Thor'), Js('Thunder'), Js('Timber'), Js('Titan'), Js('Tooth'), Js('Trace'), Js('Trapper'), Js('Trouble'), Js('Tundra'), Js('Vapor'), Js('Whisper'), Js('Wolf')]))
var.put('nm2', Js([Js('Acadia'), Js('Aiyana'), Js('Akita'), Js('Alaska'), Js('Alexia'), Js('Alexis'), Js('Alize'), Js('Alpine'), Js('Amber'), Js('Amethyst'), Js('Angel'), Js('Ares'), Js('Ari'), Js('Aspen'), Js('Astral'), Js('Athena'), Js('Atilla'), Js('Aura'), Js('Aurora'), Js('Avril'), Js('Babe'), Js('Banshee'), Js('Beauty'), Js('Blaze'), Js('Blitz'), Js('Blitzen'), Js('Blossom'), Js('Bo'), Js('Boone'), Js('Breeze'), Js('Charm'), Js('Chronis'), Js('Clarity'), Js('Cleo'), Js('Codex'), Js('Coral'), Js('Crystal'), Js('Dakota'), Js('Dash'), Js('Dawn'), Js('Delphi'), Js('Destiny'), Js('Dharma'), Js('Diva'), Js('Dodger'), Js('Dot'), Js('Duchess'), Js('Ebony'), Js('Echo'), Js('Eclipse'), Js('Enigma'), Js('Faith'), Js('Fern'), Js('Gemini'), Js('Gia'), Js('Girl'), Js('Grace'), Js('Hailey'), Js('Heather'), Js('Heaven'), Js('Helen'), Js('Hope'), Js('Ice'), Js('Indigo'), Js('Iris'), Js('Ivory'), Js('Ivy'), Js('Jade'), Js('Jasmine'), Js('Jewel'), Js('Jinx'), Js('June'), Js('Juno'), Js('Justice'), Js('Jynx'), Js('Karma'), Js('Kenya'), Js('Lady'), Js('Laika'), Js('Levi'), Js('Lexis'), Js('Liberty'), Js('Lore'), Js('Lotus'), Js('Luna'), Js('Maple'), Js('Maxima'), Js('Meadow'), Js('Mello'), Js('Melody'), Js('Mercy'), Js('Midnight'), Js('Mona'), Js('Moone'), Js('Myst'), Js('Mysti'), Js('Mystique'), Js('Myth'), Js('Nanook'), Js('Nova'), Js('Nymph'), Js('Nyx'), Js('Omen'), Js('Onyxia'), Js('Opal'), Js('Oracle'), Js('Pandora'), Js('Paws'), Js('Pearl'), Js('Pepper'), Js('Phantom'), Js('Phoenix'), Js('Precious'), Js('Princess'), Js('Pyro'), Js('Queen'), Js('Rags'), Js('Raine'), Js('Raven'), Js('Rogue'), Js('Sable'), Js('Saffron'), Js('Sapphire'), Js('Satin'), Js('Scarlet'), Js('Shade'), Js('Shadow'), Js('Silver'), Js('Snow'), Js('Snowball'), Js('Snowflake'), Js('Solstice'), Js('Star'), Js('Twilight'), Js('Vapor'), Js('Velvet'), Js('Violet'), Js('Vixen'), Js('Whisper'), Js('Willow'), Js('Winter'), Js('Xena'), Js('Zelda')]))
pass
pass


# Add lib to the module scope
wolfNames = var.to_python()