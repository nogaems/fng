__all__ = ['evilOrganizations']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' of '))+var.get('nm4').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aero'), Js('Anarchy'), Js('Aqua'), Js('Arachnid'), Js('Arcane'), Js('Ash'), Js('Avalon'), Js('Awe'), Js('Bane'), Js('Barrage'), Js('Black Mark'), Js('Blackout'), Js('Blank'), Js('Blaze'), Js('Blight'), Js('Bolt'), Js('Brain'), Js('Cerebro'), Js('Chaos'), Js('Chrome'), Js('Chronos'), Js('Cinder'), Js('Clone'), Js('Cloud'), Js('Collapse'), Js('Comet'), Js('Cosmos'), Js('Cringe'), Js('Curse'), Js('Dash'), Js('Death'), Js('Dire'), Js('Dismay'), Js('Dread'), Js('Dust'), Js('Dynamo'), Js('Echo'), Js('Eclipse'), Js('Ecto'), Js('Eternity'), Js('Fear'), Js('Flock'), Js('Frost'), Js('Frostburn'), Js('Funk'), Js('Furor'), Js('Fury'), Js('Gargoyle'), Js('Germ'), Js('Ghost'), Js('Grim'), Js('Grime'), Js('Hallow'), Js('Harm'), Js('Hive'), Js('Horror'), Js('Hydro'), Js('Iron'), Js('Judgment'), Js('Karma'), Js('Knockout'), Js('Legion'), Js('Libra'), Js('Lightning'), Js('Miasma'), Js('Micro'), Js('Midnight'), Js('Mime'), Js('Mirage'), Js('Mirror'), Js('Mist'), Js('Moira'), Js('Murk'), Js('Myriad'), Js('Myth'), Js('Nano'), Js('Necron'), Js('Nemesis'), Js('Nether'), Js('Nightmare'), Js('Nite'), Js('Nitro'), Js('Null'), Js('Obsidian'), Js('Onyx'), Js('Orion'), Js('Parallel'), Js('Phantom'), Js('Phobia'), Js('Poison'), Js('Psi'), Js('Psych'), Js('Pyro'), Js('Quake'), Js('Quantum'), Js('Rise'), Js('Ruin'), Js('Rust'), Js('Scorpio'), Js('Scourge'), Js('Serpent'), Js('Shade'), Js('Shadow'), Js('Shock'), Js('Shroud'), Js('Silence'), Js('Sliver'), Js('Specter'), Js('Spike'), Js('Spite'), Js('Steel'), Js('Stigma'), Js('Storm'), Js('Swarm'), Js('Syndicate'), Js('Taint'), Js('Taunt'), Js('Terror'), Js('Thunder'), Js('Torment'), Js('Toxin'), Js('Twilight'), Js('Twist'), Js('Valhalla'), Js('Veil'), Js('Venom'), Js('Virus'), Js('Visage'), Js('Void'), Js('Whisper'), Js('Wrath'), Js('Zion')]))
var.put('nm2', Js([Js('Anarchy'), Js('Arcane'), Js('Ash'), Js('Barrage'), Js('Battle'), Js('Beast'), Js('Behemoth'), Js('Blackout'), Js('Blaze'), Js('Blight'), Js('Cataclysm'), Js('Chaos'), Js('Chrome'), Js('Chrono'), Js('Cipher'), Js('Clone'), Js('Cobalt'), Js('Cosmos'), Js('Crypt'), Js('Curse'), Js('Cyber'), Js('Dead'), Js('Death'), Js('Demon'), Js('Devil'), Js('Diablo'), Js('Dire'), Js('Doom'), Js('Dragon'), Js('Dread'), Js('Echo'), Js('Elemental'), Js('Enigma'), Js('Fear'), Js('Fiend'), Js('Fire'), Js('Frost'), Js('Fury'), Js('Gargoyle'), Js('Ghost'), Js('Gloom'), Js('Grim'), Js('Hallow'), Js('Hate'), Js('Horror'), Js('Imp'), Js('Infernal'), Js('Inferno'), Js('Iron'), Js('Judgment'), Js('Justice'), Js('Karma'), Js('Knockout'), Js('Liberty'), Js('Lightning'), Js('Midnight'), Js('Millennium'), Js('Mutant'), Js('Nano'), Js('Necro'), Js('Necron'), Js('Nemesis'), Js('Nether'), Js('Nightmare'), Js('Obsidian'), Js('Odium'), Js('Onyx'), Js('Phantom'), Js('Poison'), Js('Psi'), Js('Psycho'), Js('Pyro'), Js('Quantum'), Js('Salvation'), Js('Serpent'), Js('Shadow'), Js('Shock'), Js('Silent'), Js('Sinner'), Js('Slayer'), Js('Specter'), Js('Spectral'), Js('Spite'), Js('Steel'), Js('Storm'), Js('Terror'), Js('Thunder'), Js('Torment'), Js('Toxin'), Js('Twisted'), Js('Undead'), Js('Universe'), Js('Unknown'), Js('Unseen'), Js('Vengeance'), Js('Venom'), Js('Verdict'), Js('Vile'), Js('Virus'), Js('Void'), Js('War'), Js('Warlord'), Js('Wicked')]))
var.put('nm3', Js([Js('Assembly'), Js('Brigade'), Js('Brotherhood'), Js('Clan'), Js('Company'), Js('Corps'), Js('Council'), Js('Crew'), Js('Force'), Js('Posse'), Js('Sisterhood'), Js('Squad'), Js('Tribe'), Js('Order')]))
var.put('nm4', Js([Js('Anarchy'), Js('Ash'), Js('Battle'), Js('Blaze'), Js('Blight'), Js('Chaos'), Js('Chrome'), Js('Chronos'), Js('Ciphers'), Js('Clones'), Js('Crypts'), Js('Curses'), Js('Death'), Js('Demons'), Js('Devilry'), Js('Diablo'), Js('Dire'), Js('Doom'), Js('Dragons'), Js('Dread'), Js('Echos'), Js('Elementals'), Js('Fear'), Js('Fiends'), Js('Fire'), Js('Frost'), Js('Fury'), Js('Gargoyles'), Js('Ghosts'), Js('Gloom'), Js('Grim'), Js('Hallow'), Js('Hate'), Js('Hatred'), Js('Horror'), Js('Imps'), Js('Infernos'), Js('Iron'), Js('Judgment'), Js('Justice'), Js('Karma'), Js('Liberty'), Js('Lightning'), Js('Midnight'), Js('Mutants'), Js('Nightmares'), Js('Obsidian'), Js('Odium'), Js('Onyx'), Js('Phantoms'), Js('Poison'), Js('Psychos'), Js('Pyro'), Js('Pyromaniacs'), Js('Salvation'), Js('Serpents'), Js('Shadow'), Js('Shock'), Js('Silence'), Js('Sin'), Js('Sinners'), Js('Slayers'), Js('Specters'), Js('Spite'), Js('Steel'), Js('Storm'), Js('Terror'), Js('Thunder'), Js('Thunders'), Js('Torment'), Js('Toxin'), Js('Vengeance'), Js('Venom'), Js('Verdicts'), Js('War'), Js('Warlords'), Js('the Arcane'), Js('the Beast'), Js('the Behemoth'), Js('the Cataclysm'), Js('the Cosmos'), Js('the Curse'), Js('the Dead'), Js('the Devil'), Js('the Elements'), Js('the Enigma'), Js('the Infernal'), Js('the Inferno'), Js('the Mutant'), Js('the Necro'), Js('the Nether'), Js('the Nightmare'), Js('the Phantom'), Js('the Serpent'), Js('the Shade'), Js('the Sinner'), Js('the Slayer'), Js('the Specter'), Js('the Twisted'), Js('the Undead'), Js('the Universe'), Js('the Unknown'), Js('the Unseen'), Js('the Virus'), Js('the Void'), Js('the Warlord'), Js('the Wicked')]))
pass
pass


# Add lib to the module scope
evilOrganizations = var.to_python()