__all__ = ['mgtElementals']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm6').get(var.get('rnd')),var.get('nm7').get(var.get('rnd2'))):
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                var.put('lName', (((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+Js(' '))+var.get('nm8').get(var.get('rnd3'))))
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5'))):
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                if (var.get('i')<Js(3.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('lName')))
                else:
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd6')),var.get('nm5').get(var.get('rnd5'))):
                        var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('lName')))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm6').get(var.get('rnd')),var.get('nm7').get(var.get('rnd2'))):
                        var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('names', (((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+Js(' '))+var.get('nm8').get(var.get('rnd3'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm9').get(var.get('rnd'))+Js(' '))+var.get('nm8').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('d'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('a'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('kl'), Js('kd'), Js('kn'), Js('km'), Js('l'), Js('ld'), Js('ll'), Js('lr'), Js('lt'), Js('lv'), Js('ln'), Js('m'), Js('mm'), Js('mr'), Js('ml'), Js('mn'), Js('n'), Js('nl'), Js('nr'), Js('nd'), Js('nt'), Js('nn'), Js('r'), Js('rd'), Js('rg'), Js('rl'), Js('rdr'), Js('rr'), Js('sn'), Js('sl'), Js('sr'), Js('sm'), Js('ss'), Js('x'), Js('z'), Js('zz'), Js('zl')]))
var.put('nm4', Js([Js('c'), Js('l'), Js('m'), Js('n'), Js('s'), Js('th'), Js('x'), Js('z')]))
var.put('nm5', Js([Js('d'), Js('g'), Js('l'), Js('n'), Js('r'), Js('s'), Js('th')]))
var.put('nm6', Js([Js('amber'), Js('ash'), Js('blaze'), Js('blood'), Js('boulder'), Js('bright'), Js('chloro'), Js('cinder'), Js('elder'), Js('fire'), Js('flame'), Js('flood'), Js('forest'), Js('frost'), Js('fuse'), Js('geyser'), Js('glare'), Js('glow'), Js('gore'), Js('green'), Js('ground'), Js('heart'), Js('hell'), Js('hollow'), Js('hydro'), Js('lava'), Js('leaf'), Js('mana'), Js('meadow'), Js('molten'), Js('moss'), Js('mourn'), Js('nether'), Js('plume'), Js('primal'), Js('pyre'), Js('pyro'), Js('rage'), Js('rock'), Js('rubble'), Js('rush'), Js('scorch'), Js('shadow'), Js('shine'), Js('shore'), Js('silver'), Js('skull'), Js('slither'), Js('smoke'), Js('snow'), Js('soot'), Js('soul'), Js('spark'), Js('spawn'), Js('spite'), Js('splinter'), Js('storm'), Js('sun'), Js('talon'), Js('terra'), Js('thunder'), Js('tide'), Js('venge'), Js('vine'), Js('war'), Js('water'), Js('whisper'), Js('wild'), Js('wind'), Js('wolf'), Js('wood')]))
var.put('nm7', Js([Js('bane'), Js('beam'), Js('bender'), Js('blaze'), Js('blight'), Js('blust'), Js('boon'), Js('born'), Js('braider'), Js('bramble'), Js('branch'), Js('brand'), Js('breaker'), Js('breeze'), Js('briar'), Js('bright'), Js('chaser'), Js('cloud'), Js('core'), Js('crag'), Js('crasher'), Js('crest'), Js('crux'), Js('dew'), Js('draft'), Js('drifter'), Js('fall'), Js('field'), Js('fiend'), Js('fire'), Js('flame'), Js('flare'), Js('flayer'), Js('flow'), Js('force'), Js('forge'), Js('fright'), Js('fury'), Js('glade'), Js('glide'), Js('growth'), Js('haze'), Js('heart'), Js('hearth'), Js('henge'), Js('horn'), Js('hulk'), Js('kin'), Js('land'), Js('lash'), Js('mare'), Js('mender'), Js('mind'), Js('morph'), Js('mulcher'), Js('muse'), Js('phant'), Js('pyre'), Js('rage'), Js('reaver'), Js('rend'), Js('roar'), Js('scar'), Js('shard'), Js('slide'), Js('spark'), Js('spitter'), Js('sprout'), Js('stoke'), Js('surge'), Js('thorn'), Js('tusk'), Js('veil'), Js('vine'), Js('walker'), Js('ward'), Js('warden'), Js('water'), Js('wend'), Js('whelk'), Js('wielder'), Js('wind'), Js('wood'), Js('wraith'), Js('writhe')]))
var.put('nm8', Js([Js('Acolyte'), Js('Ally'), Js('Ancient'), Js('Behemoth'), Js('Brood'), Js('Cerberus'), Js('Champion'), Js('Chaser'), Js('Cohort'), Js('Conservator'), Js('Consul'), Js('Custodian'), Js('Defender'), Js('Elemental'), Js('Elemental'), Js('Elemental'), Js('Elemental'), Js('Elemental'), Js('Elemental'), Js('Elemental'), Js('Elemental'), Js('Elemental'), Js('Devourer'), Js('Drifter'), Js('Effigy'), Js('Elemental'), Js('Entity'), Js('Envoy'), Js('Fiend'), Js('Figure'), Js('Force'), Js('Forger'), Js('Glider'), Js('Guardian'), Js('Hatchling'), Js('Hulk'), Js('Hunter'), Js('Icon'), Js('Incarnate'), Js('Infantry'), Js('Knight'), Js('Legate'), Js('Liege'), Js('Mage'), Js('Mongrel'), Js('Monster'), Js('Nimbus'), Js('Overseer'), Js('Paladin'), Js('Patrol'), Js('Plasma'), Js('Protector'), Js('Rager'), Js('Ravager'), Js('Ripper'), Js('Rusher'), Js('Scavenger'), Js('Scion'), Js('Scout'), Js('Sentinel'), Js('Servant'), Js('Shaman'), Js('Shambler'), Js('Shepherd'), Js('Soldier'), Js('Soul'), Js('Spirit'), Js('Stalker'), Js('Strider'), Js('Titan'), Js('Trooper'), Js('Tyrant'), Js('Walker'), Js('Wanderer'), Js('Warden'), Js('Watcher'), Js('Zealot')]))
var.put('nm9', Js([Js('Aqua'), Js('Blizzard'), Js('Blood'), Js('Bog'), Js('Boulder'), Js('Bramble'), Js('Bright'), Js('Brine'), Js('Celestial'), Js('Cinder'), Js('Cloud'), Js('Crater'), Js('Cyclone'), Js('Dawn'), Js('Dread'), Js('Dusk'), Js('Dust'), Js('Earth'), Js('Ember'), Js('Ethereal'), Js('Fiery'), Js('Fire'), Js('Flame'), Js('Fog'), Js('Forest'), Js('Forgotten'), Js('Frost'), Js('Frozen'), Js('Fungi'), Js('Fungus'), Js('Furnace'), Js('Fury'), Js('Fusion'), Js('Geyser'), Js('Glacial'), Js('Glaring'), Js('Grand'), Js('Granite'), Js('Grave'), Js('Greater'), Js('Grove'), Js('Hellfire'), Js('Hollow'), Js('Hurricane'), Js('Hydro'), Js('Igneous'), Js('Infernal'), Js('Inferno'), Js('Ingot'), Js('Labyrinth'), Js('Lagoon'), Js('Lake'), Js('Lightning'), Js('Lucent'), Js('Lucid'), Js('Maelstrom'), Js('Magma'), Js('Marsh'), Js('Maze'), Js('Meadow'), Js('Mist'), Js('Molten'), Js('Moon'), Js('Moss'), Js('Mountain'), Js('Mud'), Js('Nova'), Js('Oasis'), Js('Obsidian'), Js('Orchard'), Js('Plasma'), Js('Primal'), Js('Prime'), Js('Pyre'), Js('Pyro'), Js('Quicksilver'), Js('Rage'), Js('Rift'), Js('Rock'), Js('Root'), Js('Rotten'), Js('Rotting'), Js('Rumbling'), Js('Rust'), Js('Salt'), Js('Savage'), Js('Seething'), Js('Seismic'), Js('Smog'), Js('Smoke'), Js('Smoking'), Js('Smolder'), Js('Smoldering'), Js('Soot'), Js('Spark'), Js('Spectral'), Js('Stone'), Js('Storm'), Js('Sun'), Js('Tempest'), Js('Terra'), Js('Thorn'), Js('Thunder'), Js('Thundercloud'), Js('Tidal'), Js('Tide'), Js('Time'), Js('Torrent'), Js('Totem'), Js('Undergrowth'), Js('Vapor'), Js('Vengeful'), Js('Vine'), Js('Void'), Js('Volatile'), Js('Volcanic'), Js('Vortex'), Js('War'), Js('Water'), Js('Wave'), Js('Wayfaring'), Js('Wind'), Js('Wood')]))
pass
pass


# Add lib to the module scope
mgtElementals = var.to_python()