__all__ = ['sportNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'nm3', 'result', 'nm4'])
    var.put('nm1', Js([Js('Acro'), Js('Adven'), Js('Aero'), Js('Air'), Js('Alpha'), Js('Ama'), Js('Anar'), Js('Ani'), Js('Aqua'), Js('Asteroi'), Js('Auto'), Js('Azu'), Js('Bad'), Js('Bala'), Js('Bea'), Js('Bia'), Js('Biath'), Js('Blitz'), Js('Brawl'), Js('Bungee'), Js('Chaos'), Js('Chrono'), Js('Clash'), Js('Comb'), Js('Comet'), Js('Corner'), Js('Crash'), Js('Cri'), Js('Cross'), Js('Cryo'), Js('Cy'), Js('Cyclo'), Js('Death'), Js('Deca'), Js('Demo'), Js('Demoli'), Js('Dino'), Js('Diplo'), Js('Dirt'), Js('Dis'), Js('Disc'), Js('Dog'), Js('Domi'), Js('Domina'), Js('Draft'), Js('Drag'), Js('Drago'), Js('Dri'), Js('Drift'), Js('Dril'), Js('Dual'), Js('Duo'), Js('Electri'), Js('Endu'), Js('Equi'), Js('Fien'), Js('Fluke'), Js('Fore'), Js('Free'), Js('Frost'), Js('Fur'), Js('Fury'), Js('Fuse'), Js('Geo'), Js('Giga'), Js('Gli'), Js('Glue'), Js('Grav'), Js('Grim'), Js('Gut'), Js('Gutter'), Js('Hi'), Js('Hollow'), Js('Hover'), Js('Hy'), Js('Hybri'), Js('Hypo'), Js('Ice'), Js('Immu'), Js('Indi'), Js('Infini'), Js('Inter'), Js('Kil'), Js('Laser'), Js('Lim'), Js('Lo'), Js('Mara'), Js('Mash'), Js('Matri'), Js('Maze'), Js('Mer'), Js('Meta'), Js('Mind'), Js('Mini'), Js('Mix'), Js('Mod'), Js('Mono'), Js('Mud'), Js('Neo'), Js('Nether'), Js('Nova'), Js('Omega'), Js('Orient'), Js('Pandemo'), Js('Para'), Js('Persi'), Js('Pitch'), Js('Pod'), Js('Prime'), Js('Pro'), Js('Psy'), Js('Pyra'), Js('Pyre'), Js('Pyro'), Js('Quad'), Js('Quadri'), Js('Quantum'), Js('Race'), Js('Rando'), Js('Resi'), Js('Reso'), Js('Rever'), Js('Ring'), Js('Ro'), Js('Roa'), Js('Rock'), Js('Rum'), Js('Sam'), Js('Scu'), Js('Scuf'), Js('Seg'), Js('Siege'), Js('Skele'), Js('Skir'), Js('Soar'), Js('Speed'), Js('Sti'), Js('Storm'), Js('Strate'), Js('Strato'), Js('Sub'), Js('Sur'), Js('Swor'), Js('Sym'), Js('Sys'), Js('Tag'), Js('Tele'), Js('Terri'), Js('Terror'), Js('Thunder'), Js('Tira'), Js('Tiro'), Js('Titan'), Js('Trampo'), Js('Tria'), Js('Triad'), Js('Trini'), Js('Tug'), Js('Tum'), Js('Ulti'), Js('Ultra'), Js('Uni'), Js('Venti'), Js('Vertex'), Js('Verti'), Js('Virti'), Js('Vitali'), Js('Void'), Js('Wall'), Js('War'), Js('Wel'), Js('Wheel'), Js('Wish'), Js('Wub'), Js('Zephy')]))
    var.put('nm2', Js([Js('ball'), Js('base'), Js('bat'), Js('batics'), Js('boarding'), Js('chase'), Js('course'), Js('cross'), Js('crosse'), Js('cycling'), Js('derby'), Js('dive'), Js('diving'), Js('draft'), Js('game'), Js('glide'), Js('go'), Js('goal'), Js('hoop'), Js('line'), Js('ling'), Js('mix'), Js('net'), Js('play'), Js('pool'), Js('race'), Js('raid'), Js('rally'), Js('relay'), Js('sail'), Js('slam'), Js('style'), Js('surf'), Js('surfing'), Js('tag'), Js('ton'), Js('tour'), Js('trial'), Js('vault'), Js('volley')]))
    var.put('nm3', Js([Js('Adventure'), Js('Aero'), Js('Aqua'), Js('Astral'), Js('Auto'), Js('Balance'), Js('Barrel'), Js('Battle'), Js('Beast'), Js('Big'), Js('Blind'), Js('Blitz'), Js('Bone'), Js('Bumper'), Js('Bungee'), Js('Capture'), Js('Chrono'), Js('Comet'), Js('Command'), Js('Corner'), Js('Crazy'), Js('Cross'), Js('Crush'), Js('Cryo'), Js('Cushion'), Js('Death'), Js('Decoy'), Js('Demolition'), Js('Dimension'), Js('Domination'), Js('Doom'), Js('Double'), Js('Dragon'), Js('Drone'), Js('Drop'), Js('Drum'), Js('Duel'), Js('Dynamic'), Js('Ember'), Js('Endurance'), Js('Escape'), Js('Eternity'), Js('Extreme'), Js('Field'), Js('Final'), Js('Floor'), Js('Fluster'), Js('Free'), Js('Freefall'), Js('Freestyle'), Js('Fury'), Js('Galaxy'), Js('Gate'), Js('Geo'), Js('Glider'), Js('Glove'), Js('Grand'), Js('Gravity'), Js('Grim'), Js('Hammer'), Js('High'), Js('Hound'), Js('Hurdle'), Js('Hurricane'), Js('Hyper'), Js('Ice'), Js('Illusion'), Js('Immortal'), Js('Infinity'), Js('Invasion'), Js('Iron'), Js('Jump'), Js('Laser'), Js('Leopard'), Js('Light'), Js('Low'), Js('Lunar'), Js('Maneuver'), Js('Martial'), Js('Maze'), Js('Mini'), Js('Mountain'), Js('Mud'), Js('Mystery'), Js('Nemo'), Js('Neo'), Js('Neuro'), Js('Night'), Js('Nimble'), Js('Nova'), Js('Obstacle'), Js('Oracle'), Js('Over'), Js('Paragon'), Js('Parallel'), Js('Pitch'), Js('Platform'), Js('Pod'), Js('Power'), Js('Primal'), Js('Prime'), Js('Pyre'), Js('Pyro'), Js('Quantum'), Js('Rally'), Js('Realm'), Js('Resolution'), Js('Retro'), Js('River'), Js('Roller'), Js('Row'), Js('Scrub'), Js('Serial'), Js('Shuffle'), Js('Silent'), Js('Sky'), Js('Smash'), Js('Snag'), Js('Snail'), Js('Snare'), Js('Snow'), Js('Soft'), Js('Solar'), Js('Sonic'), Js('Speed'), Js('Sprint'), Js('Stamina'), Js('Star'), Js('Stasis'), Js('Stealth'), Js('Stick'), Js('Sticky'), Js('Still'), Js('Storm'), Js('Strike'), Js('Stunt'), Js('Super'), Js('Swamp'), Js('Sync'), Js('Tag'), Js('Target'), Js('Terra'), Js('Tetra'), Js('Thunder'), Js('Time'), Js('Torpedo'), Js('Touch'), Js('Trial'), Js('Trick'), Js('Trigger'), Js('Tumble'), Js('Twister'), Js('Typhoon'), Js('Ultra'), Js('Universe'), Js('Vertex'), Js('Vertigo'), Js('Vision'), Js('Vortex'), Js('Wall'), Js('War'), Js('Water'), Js('Whack'), Js('Wheel'), Js('Zero-G'), Js('Zigzag')]))
    var.put('nm4', Js([Js('Acrobatics'), Js('Attack'), Js('Ball'), Js('Base'), Js('Boarding'), Js('Chase'), Js('Combined'), Js('Course'), Js('Cross'), Js('Cycling'), Js('Derby'), Js('Dive'), Js('Diving'), Js('Draft'), Js('Game'), Js('Gliding'), Js('Goal'), Js('Hurl'), Js('Mix'), Js('Pitch'), Js('Play'), Js('Race'), Js('Raid'), Js('Rally'), Js('Relay'), Js('Ring'), Js('Rings'), Js('Rules'), Js('Sailing'), Js('Slam'), Js('Smash'), Js('Style'), Js('Surfing'), Js('Tag'), Js('Tour'), Js('Trial'), Js('Volley'), Js('War')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
                var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm4').callprop('splice', var.get('rnd2'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
sportNames = var.to_python()