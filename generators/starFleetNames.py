__all__ = ['starFleetNames']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abyss'), Js('Alliance'), Js('Anarchist'), Js('Angel'), Js('Annihilation'), Js('Arachnid'), Js('Archangel'), Js('Assassination'), Js('Astral'), Js('August'), Js('Aurora'), Js('Babylon'), Js('Ballistics'), Js('Bane'), Js('Banshee'), Js('Bastion'), Js('Blaze'), Js('Bombardment'), Js('Bulldozer'), Js('Bulwark'), Js('Buster'), Js('Cardinal'), Js('Carnage'), Js('Cataclysm'), Js('Celestial'), Js('Cerberus'), Js('Champion'), Js('Chaos'), Js('Citadel'), Js('Climax'), Js('Coalition'), Js('Cobra'), Js('Colonial'), Js('Concord'), Js('Confederacy'), Js('Confederation'), Js('Crimson'), Js('Crossbone'), Js('Crucifix'), Js('Crucifixion'), Js('Curator'), Js('Custodian'), Js('Daemon'), Js('Dawn'), Js('Death'), Js('Defiance'), Js('Deluge'), Js('Demolition'), Js('Demon'), Js('Destiny'), Js('Devil'), Js('Diabolical'), Js('Dimension'), Js('Divine'), Js('Doom'), Js('Dread'), Js('Ebon'), Js('Eidolon'), Js('Elimination'), Js('Enigma'), Js('Eos'), Js('Eradication'), Js('Eternal'), Js('Ethereal'), Js('Exalted'), Js('Execution'), Js('Exile'), Js('Expansion'), Js('Expedition'), Js('Extermination'), Js('Extinction'), Js('Federation'), Js('Fire'), Js('Forsaken'), Js('Frenzy'), Js('Fury'), Js('Fusillade'), Js('Genie'), Js('Ghost'), Js('Glory'), Js('Grand'), Js('Guardian'), Js('Guerrilla'), Js('Hallowed'), Js('Havoc'), Js('Hell'), Js('Heresy'), Js('Hollow'), Js('Honor'), Js('Horde'), Js('Horror'), Js('Howler'), Js('Hunter'), Js('Huntress'), Js('Hurricane'), Js('Immolation'), Js('Immortal'), Js('Imperial'), Js('Infernal'), Js('Inferno'), Js('Infinity'), Js('Innovation'), Js('Insurgent'), Js('Judge'), Js('Judgment'), Js('Justice'), Js('Legend'), Js('Legion'), Js('Lightning'), Js('Lightyear'), Js('Limbo'), Js('Martyr'), Js('Matriarch'), Js('Mayhem'), Js('Miracle'), Js('Moira'), Js('Myriad'), Js('Mythic'), Js('Neo'), Js('Nether'), Js('Nova'), Js('Obisidian'), Js('Obliteration'), Js('Onyx'), Js('Oracle'), Js('Overlord'), Js('Overseer'), Js('Paladin'), Js('Patriarch'), Js('Phantom'), Js('Phoenix'), Js('Pinnacle'), Js('Plague'), Js('Prestige'), Js('Primal'), Js('Prime'), Js('Prodigy'), Js('Prophecy'), Js('Purgatory'), Js('Purity'), Js('Radical'), Js('Ravage'), Js('Raven'), Js('Rebel'), Js('Renegade'), Js('Republic'), Js('Revelation'), Js('Revenant'), Js('Revolution'), Js('Rogue'), Js('Royal'), Js('Ruthless'), Js('Sacred'), Js('Sanguine'), Js('Scourge'), Js('Sentinel'), Js('Sentry'), Js('Separatist'), Js('Seraph'), Js('Serpent'), Js('Shade'), Js('Shadow'), Js('Shepherd'), Js('Sinister'), Js('Sinner'), Js('Specter'), Js('Spirit'), Js('Stalker'), Js('Star'), Js('Star Alliance'), Js('Star League'), Js('Star Shield'), Js('Star Treaty'), Js('Stealth'), Js('Storm'), Js('Sundry'), Js('Supernova'), Js('Supreme'), Js('Syndicate'), Js('Tempest'), Js('Terminal'), Js('Terror'), Js('Thunder'), Js('Titan'), Js('Torment'), Js('Treasure'), Js('Triumph'), Js('Union'), Js('Unity'), Js('Valliance'), Js('Valor'), Js('Vanquisher'), Js('Velvet'), Js('Venom'), Js('Viper'), Js('Void'), Js('Warden'), Js('Wraith'), Js('Wreckage'), Js('Zion')]))
var.put('nm2', Js([Js('Armada'), Js('Attack Force'), Js('Corps'), Js('Defense Force'), Js('Division'), Js('Fleet'), Js('Flotilla'), Js('Force'), Js('Military'), Js('Navy'), Js('Space Corps'), Js('Space Force'), Js('Space Navy'), Js('Space Service'), Js('Squadron'), Js('Star Division'), Js('Star Forces'), Js('Vanguard')]))
pass
pass


# Add lib to the module scope
starFleetNames = var.to_python()