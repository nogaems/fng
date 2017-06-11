__all__ = ['spaceColony']

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
var.put('nm1', Js([Js('Aegis'), Js('Aeon'), Js('Aeris'), Js('Babylon'), Js('Aeternitas'), Js('Aether'), Js('Alliance'), Js('Alpha'), Js('Amazone'), Js('Ancestor'), Js('Anemone'), Js('Angel'), Js('Anomaly'), Js('Apollo'), Js('Arcadia'), Js('Arcadis'), Js('Arch'), Js('Architect'), Js('Ark'), Js('Artemis'), Js('Asphodel'), Js('Asteria'), Js('Astraeus'), Js('Athena'), Js('Atlas'), Js('Atmos'), Js('Aura'), Js('Aurora'), Js('Awe'), Js('Azura'), Js('Azure'), Js('Baldur'), Js('Beacon'), Js('Blue Moon'), Js('Borealis'), Js('Burrow'), Js('Caelestis'), Js('Canaan'), Js('Century'), Js('Chrono'), Js('Chronos'), Js('Crescent'), Js('Curator'), Js('Curiosity'), Js('Data'), Js('Dawn'), Js('Daydream'), Js('Demeter'), Js('Dogma'), Js('Dream'), Js('Dune'), Js('Ecstacys'), Js('Eir'), Js('Elyse'), Js('Elysium'), Js('Empyrea'), Js('Ender'), Js('Enigma'), Js('Eos'), Js('Epiphany'), Js('Epitome'), Js('Erebus'), Js('Escort'), Js('Eternis'), Js('Eternity'), Js('Exposure'), Js('Fable'), Js('Father'), Js('Fauna'), Js('Felicity'), Js('Flora'), Js('Fortuna'), Js('Frontier'), Js('Gaia'), Js('Galaxy'), Js('Genesis'), Js('Genius'), Js('Glory'), Js('Guardian'), Js('Halo'), Js('Heirloom'), Js('Helios'), Js('Hemera'), Js('Hera'), Js('Heritage'), Js('Hermes'), Js('Horus'), Js('Hymn'), Js('Hyperion'), Js('Hypnos'), Js('Ignis'), Js('Illume'), Js('Inception'), Js('Infinity'), Js('Isis'), Js('Janus'), Js('Juno'), Js('Legacy'), Js('Liberty'), Js('Lore'), Js('Lucent'), Js('Lumina'), Js('Luminous'), Js('Luna'), Js('Lunis'), Js('Magni'), Js('Mammoth'), Js('Mani'), Js('Marvel'), Js('Memento'), Js('Minerva'), Js('Miracle'), Js('Mother'), Js('Muse'), Js('Mystery'), Js('Mythos'), Js('Nebula'), Js('Nemesis'), Js('Nemo'), Js('Neo'), Js('Nero'), Js('Nimbus'), Js('Nott'), Js('Nova'), Js('Novis'), Js('Nox'), Js('Nyx'), Js('Odyssey'), Js('Olympus'), Js('Omega'), Js('Oracle'), Js('Orbital'), Js('Origin'), Js('Orphan'), Js('Osiris'), Js('Outlander'), Js('Parable'), Js('Paradox'), Js('Paragon'), Js('Pedigree'), Js('Phantasm'), Js('Phantom'), Js('Phenomenon'), Js('Phoenix'), Js('Pilgrim'), Js('Pioneer'), Js('Prism'), Js('Prodigy'), Js('Prometheus'), Js('Prophecy'), Js('Proto'), Js('Radiance'), Js('Rebus'), Js('Relic'), Js('Revelation'), Js('Reverie'), Js('Rogue'), Js('Rune'), Js('Saga'), Js('Sancus'), Js('Scout'), Js('Selene'), Js('Serenity'), Js('Settler'), Js('Shangris'), Js('Shepherd'), Js('Shu'), Js('Sol'), Js('Solas'), Js('Spectacle'), Js('Specter'), Js('Spectrum'), Js('Spire'), Js('Symbolica'), Js('Tartarus'), Js('Terminus'), Js('Terra'), Js('Terran'), Js('Terraria'), Js('Themis'), Js('Tiberius'), Js('Titan'), Js('Titanus'), Js('Torus'), Js('Tranquility'), Js('Trivia'), Js('Utopis'), Js('Valhalla'), Js('Vanguard'), Js('Vanquish'), Js('Vesta'), Js('Vestige'), Js('Victoria'), Js('Virtue'), Js('Visage'), Js('Voyage'), Js('Vulcan'), Js('Warden'), Js('Yggdrasil'), Js('Zeus'), Js('Zion')]))
var.put('nm2', Js([Js(''), Js('Colony'), Js('Station'), Js('Colony'), Js('Station'), Js('Base'), Js('Terminal'), Js('')]))
pass
pass


# Add lib to the module scope
spaceColony = var.to_python()