__all__ = ['gameEngine']

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
var.put('nm1', Js([Js('Adventure'), Js('Aeon'), Js('Affinity'), Js('Alchemy'), Js('Alliance'), Js('Alloy'), Js('Ambience'), Js('Amigo'), Js('Anomaly'), Js('Apex'), Js('Aptitude'), Js('Arcane'), Js('Arch'), Js('Architect'), Js('Artisan'), Js('Aspect'), Js('Atom'), Js('Aura'), Js('Aurora'), Js('Banshee'), Js('Beacon'), Js('Beast'), Js('Behemoth'), Js('Bionics'), Js('Bonfire'), Js('Buddy'), Js('Builder'), Js('Bullet'), Js('Canvas'), Js('Capture'), Js('Champion'), Js('Chaos'), Js('Chief'), Js('Chivalry'), Js('Cinder'), Js('Clairvoyant'), Js('Climax'), Js('Clone'), Js('Companion'), Js('Composer'), Js('Construction'), Js('Core'), Js('Courage'), Js('Creative'), Js('Creature'), Js('Crescent'), Js('Crow'), Js('Crux'), Js('Crystal'), Js('Curio'), Js('Cyborg'), Js('Daemon'), Js('Dawn'), Js('Daydream'), Js('Deity'), Js('Destiny'), Js('Device'), Js('Diamond'), Js('Divine'), Js('Domain'), Js('Dominion'), Js('Dream'), Js('Dungeon'), Js('Dwarf'), Js('Dynamo'), Js('Ebony'), Js('Ecstasy'), Js('Effigy'), Js('Ego'), Js('Elysium'), Js('Ember'), Js('Emblem'), Js('Empire'), Js('Enigma'), Js('Enterprise'), Js('Eos'), Js('Epitome'), Js('Epoch'), Js('Era'), Js('Essence'), Js('Eternity'), Js('Executive'), Js('Fable'), Js('Fairy'), Js('Fantasy'), Js('Farseer'), Js('Fay'), Js('Ferocity'), Js('Figment'), Js('Firework'), Js('Flair'), Js('Flare'), Js('Flexile'), Js('Flow'), Js('Fluid'), Js('Flux'), Js('Forged'), Js('Forger'), Js('Formula'), Js('Fortune'), Js('Frame'), Js('Framework'), Js('Fury'), Js('Fusion'), Js('Galaxy'), Js('Gargoyle'), Js('Generation'), Js('Genesis'), Js('Genie'), Js('Genius'), Js('Globe'), Js('Gold'), Js('Gorgon'), Js('Hallow'), Js('Harmony'), Js('Havoc'), Js('Hazard'), Js('Heirloom'), Js('Heist'), Js('Hex'), Js('Hieroglyph'), Js('Hymn'), Js('Hysteria'), Js('Identity'), Js('Idol'), Js('Illusion'), Js('Imagination'), Js('Imagine'), Js('Immortal'), Js('Inception'), Js('Infinity'), Js('Innovation'), Js('Insight'), Js('Inspire'), Js('Invention'), Js('Ivory'), Js('Jaeger'), Js('Javelin'), Js('Journey'), Js('Joy'), Js('Karma'), Js('Kindred'), Js('Kinetics'), Js('Kobold'), Js('Legacy'), Js('Legend'), Js('Legion'), Js('Leviathan'), Js('Liberty'), Js('Lich'), Js('Lighthouse'), Js('Locomotion'), Js('Lore'), Js('Lucid'), Js('Luminous'), Js('Magma'), Js('Mania'), Js('Maniac'), Js('Martial'), Js('Mason'), Js('Mayhem'), Js('Medusa'), Js('Memento'), Js('Mercenary'), Js('Merry'), Js('Mobius'), Js('Muse'), Js('Myriad'), Js('Mystery'), Js('Mystic'), Js('Myth'), Js('Nebula'), Js('Nephilim'), Js('Nimble'), Js('Nimbus'), Js('Oasis'), Js('Obelisk'), Js('Obsidian'), Js('Odyssey'), Js('Omega'), Js('Oracle'), Js('Origin'), Js('Parable'), Js('Paradox'), Js('Paragon'), Js('Particle'), Js('Pegasus'), Js('Peril'), Js('Phantom'), Js('Phoenix'), Js('Physique'), Js('Pinnacle'), Js('Pixel'), Js('Pixie'), Js('Platinum'), Js('Playful'), Js('Primal'), Js('Prime'), Js('Prodigy'), Js('Prophecy'), Js('Prospect'), Js('Prosperity'), Js('Protocol'), Js('Psyche'), Js('Psychic'), Js('Pursuit'), Js('Quest'), Js('Queue'), Js('Quickfire'), Js('Rage'), Js('Rainbow'), Js('Rapture'), Js('Raze'), Js('Rebel'), Js('Relic'), Js('Renaissance'), Js('Revolution'), Js('Ritual'), Js('Root'), Js('Rune'), Js('Saga'), Js('Sanctuary'), Js('Sanctum'), Js('Savage'), Js('Scope'), Js('Scythe'), Js('Searchlight'), Js('Serenity'), Js('Shade'), Js('Shadow'), Js('Shapeshifter'), Js('Shrine'), Js('Sidekick'), Js('Siege'), Js('Silence'), Js('Singularity'), Js('Siren'), Js('Sonic'), Js('Source'), Js('Sparkle'), Js('Specter'), Js('Sphinx'), Js('Spiral'), Js('Spirit'), Js('Sprite'), Js('Stage'), Js('Steel'), Js('Storm'), Js('Supremacy'), Js('Synthesis'), Js('Temper'), Js('Tempest'), Js('Terminus'), Js('Terra'), Js('Thauma'), Js('Tranquillity'), Js('Transcendence'), Js('Turbulence'), Js('Twist'), Js('Unity'), Js('Universe'), Js('Valiance'), Js('Vault'), Js('Venture'), Js('Vertex'), Js('Vigor'), Js('Virtuality'), Js('Virtue'), Js('Virtuoso'), Js('Vision'), Js('Void'), Js('Vortex'), Js('Voyage'), Js('Whiz'), Js('World'), Js('Zenith'), Js('Zion'), Js('Zodiac')]))
var.put('nm2', Js([Js('Creative Engine'), Js('Creator'), Js('Engine'), Js('Frameworks'), Js('Game Engine'), Js('Physics Engine'), Js('Studio'), Js('Tools'), Js('Toolset'), Js('Engine'), Js('Engine')]))
pass
pass


# Add lib to the module scope
gameEngine = var.to_python()