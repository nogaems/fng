__all__ = ['transformersNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', var.get('nm3').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Acid'), Js('Aero'), Js('After'), Js('Air'), Js('Ape'), Js('Aqua'), Js('Armor'), Js('Astro'), Js('Auto'), Js('Avian'), Js('Back'), Js('Blow'), Js('Blue'), Js('Body'), Js('Bomb'), Js('Bone'), Js('Botani'), Js('Boulder'), Js('Brake'), Js('Break'), Js('Broad'), Js('Brush'), Js('Bulk'), Js('Bull'), Js('Bullet'), Js('Buzz'), Js('Cannon'), Js('Chain'), Js('Chrome'), Js('Cinder'), Js('Cliff'), Js('Cloud'), Js('Crack'), Js('Crank'), Js('Cross'), Js('Dark'), Js('Deep'), Js('Deft'), Js('Depth'), Js('Dino'), Js('Dirt'), Js('Dive'), Js('Doom'), Js('Double'), Js('Dread'), Js('Drop'), Js('Dune'), Js('Dust'), Js('Fang'), Js('Fiery'), Js('Fire'), Js('Fist'), Js('Flame'), Js('Flash'), Js('Flat'), Js('Flight'), Js('Fly'), Js('Free'), Js('Freeze'), Js('Frost'), Js('Gear'), Js('Gloom'), Js('Gold'), Js('Grand'), Js('Grim'), Js('Grind'), Js('Grizz'), Js('Groove'), Js('Ground'), Js('Growl'), Js('Gun'), Js('Hail'), Js('Half'), Js('Hammer'), Js('Hang'), Js('Hard'), Js('Heavy'), Js('Heli'), Js('High'), Js('Hook'), Js('Hot'), Js('Hydra'), Js('Hydrau'), Js('Hyper'), Js('Ice'), Js('Iron'), Js('Jaw'), Js('Jet'), Js('Jolt'), Js('Junk'), Js('Kick'), Js('Land'), Js('Lazer'), Js('Lead'), Js('Leo'), Js('Light'), Js('Lock'), Js('Long'), Js('Lunar'), Js('Magma'), Js('Magna'), Js('Mean'), Js('Mecha'), Js('Mega'), Js('Melt'), Js('Motor'), Js('Neutro'), Js('Night'), Js('Oil'), Js('Over'), Js('Phase'), Js('Photon'), Js('Power'), Js('Pyro'), Js('Quick'), Js('Rage'), Js('Rapid'), Js('Rat'), Js('Razor'), Js('Retro'), Js('Rhi'), Js('Rhino'), Js('Rip'), Js('Road'), Js('Roll'), Js('Rotor'), Js('Rough'), Js('Rumble'), Js('Savage'), Js('Scorch'), Js('Scrap'), Js('Sea'), Js('Shade'), Js('Shadow'), Js('Shock'), Js('Side'), Js('Silver'), Js('Sky'), Js('Slam'), Js('Slip'), Js('Smoke'), Js('Solar'), Js('Sound'), Js('Spark'), Js('Speed'), Js('Star'), Js('Steel'), Js('Stone'), Js('Storm'), Js('Strike'), Js('Sun'), Js('Swift'), Js('Thunder'), Js('Tiga'), Js('Tiger'), Js('Top'), Js('Turbo'), Js('Twin'), Js('Vice'), Js('Volt'), Js('Wide'), Js('Wild'), Js('Wind'), Js('Wolf'), Js('Wreck')]))
var.put('nm2', Js([Js('back'), Js('bang'), Js('beam'), Js('beast'), Js('bird'), Js('bite'), Js('blade'), Js('blades'), Js('blast'), Js('blaze'), Js('blight'), Js('blitz'), Js('bolt'), Js('boom'), Js('bot'), Js('brawl'), Js('brawn'), Js('burn'), Js('burner'), Js('burst'), Js('buster'), Js('button'), Js('case'), Js('cast'), Js('charge'), Js('charger'), Js('circuit'), Js('clash'), Js('claw'), Js('cloud'), Js('clutch'), Js('crack'), Js('crush'), Js('crusher'), Js('cut'), Js('cycle'), Js('dash'), Js('dealer'), Js('dive'), Js('dome'), Js('drift'), Js('drive'), Js('feather'), Js('fight'), Js('fire'), Js('fist'), Js('flash'), Js('flight'), Js('flow'), Js('foot'), Js('frame'), Js('glide'), Js('glider'), Js('glitch'), Js('guard'), Js('hammer'), Js('head'), Js('heap'), Js('hide'), Js('horn'), Js('jaw'), Js('jump'), Js('kick'), Js('kill'), Js('lane'), Js('lift'), Js('light'), Js('line'), Js('load'), Js('lock'), Js('master'), Js('mine'), Js('point'), Js('pounder'), Js('punch'), Js('quake'), Js('raid'), Js('raider'), Js('rake'), Js('raker'), Js('ray'), Js('razor'), Js('runner'), Js('scope'), Js('scrap'), Js('scraps'), Js('scream'), Js('shift'), Js('shot'), Js('side'), Js('sight'), Js('siren'), Js('slide'), Js('sling'), Js('slinger'), Js('snarl'), Js('spike'), Js('spin'), Js('splitter'), Js('spot'), Js('stalker'), Js('steel'), Js('stop'), Js('storm'), Js('streak'), Js('stream'), Js('strike'), Js('strong'), Js('stuff'), Js('sweep'), Js('switch'), Js('thing'), Js('top'), Js('track'), Js('tracks'), Js('trap'), Js('tron'), Js('twitch'), Js('viper'), Js('vortex'), Js('war'), Js('watch'), Js('wave'), Js('way'), Js('ways'), Js('wheels'), Js('whip'), Js('wing'), Js('wire'), Js('wise'), Js('works')]))
var.put('nm3', Js([Js('Abomination'), Js('Ace'), Js('Ares'), Js('Aries'), Js('Athena'), Js('Augment'), Js('Aurora'), Js('Barbarian'), Js('Barrage'), Js('Beacon'), Js('Beast'), Js('Behemoth'), Js('Blade'), Js('Blitz'), Js('Blitzkrieg'), Js('Blockaide'), Js('Brute'), Js('Cascade'), Js('Claw'), Js('Coil'), Js('Comet'), Js('Compass'), Js('Core'), Js('Creature'), Js('Critter'), Js('Crossflare'), Js('Crux'), Js('Dagger'), Js('Delirium'), Js('Ditch'), Js('Divebomb'), Js('Dread'), Js('Dynamite'), Js('Dynamo'), Js('Earthquake'), Js('Eclipse'), Js('Element'), Js('Ember'), Js('Enigma'), Js('Error'), Js('Feral'), Js('Flinch'), Js('Flow'), Js('Flutter'), Js('Flux'), Js('Freak'), Js('Fungus'), Js('Fury'), Js('Fuse'), Js('Gadget'), Js('Gleam'), Js('Grease'), Js('Growl'), Js('Harness'), Js('Havoc'), Js('Hazard'), Js('Hightop'), Js('Hitch'), Js('Honeybee'), Js('Howler'), Js('Hymn'), Js('Icicle'), Js('Inferno'), Js('Influx'), Js('Jeopardy'), Js('Landslide'), Js('Maniac'), Js('Melody'), Js('Mercy'), Js('Meteoroid'), Js('Nightlight'), Js('Oracle'), Js('Outburst'), Js('Overboard'), Js('Overflow'), Js('Overload'), Js('Paradox'), Js('Particle'), Js('Pest'), Js('Pillage'), Js('Posthaste'), Js('Prodigy'), Js('Pummel'), Js('Pursuit'), Js('Quake'), Js('Quarrel'), Js('Rabid'), Js('Racer'), Js('Rage'), Js('Remix'), Js('Requiem'), Js('Residue'), Js('Ricochet'), Js('Riot'), Js('Rodent'), Js('Rubble'), Js('Rumble'), Js('Rush'), Js('Salvo'), Js('Savage'), Js('Savvy'), Js('Scourge'), Js('Scratch'), Js('Shamble'), Js('Shift'), Js('Sidearm'), Js('Sideburns'), Js('Sidelock'), Js('Sidewire'), Js('Sky-High'), Js('Slide'), Js('Smite'), Js('Snake'), Js('Snarl'), Js('Snowdrift'), Js('Sprocket'), Js('Stampede'), Js('Starblaster'), Js('Starburst'), Js('Stormrunner'), Js('Sunblast'), Js('Sunburst'), Js('Switch'), Js('Talon'), Js('Tempest'), Js('Thrust'), Js('Thunder'), Js('Torment'), Js('Torrent'), Js('Trailfire'), Js('Trident'), Js('Turbine'), Js('Twinkle'), Js('Typhoon'), Js('Venture'), Js('Vermin'), Js('Vigor'), Js('Virtue'), Js('Volley'), Js('Voltage'), Js('Wallop'), Js('Weasel'), Js('Wheels'), Js('Whistle'), Js('Whiz'), Js('Wrangle'), Js('Wreckage'), Js('Zephyr'), Js('Zodiac')]))
pass
pass


# Add lib to the module scope
transformersNames = var.to_python()