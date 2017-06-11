__all__ = ['steampunkCities']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aera'), Js('Aero'), Js('Aether'), Js('Alder'), Js('Arc'), Js('Arca'), Js('Ash'), Js('Astro'), Js('Automa'), Js('Bacca'), Js('Baro'), Js('Beak'), Js('Bel'), Js('Bell'), Js('Bene'), Js('Bibbing'), Js('Black'), Js('Blag'), Js('Bobbing'), Js('Bol'), Js('Bone'), Js('Brass'), Js('Broad'), Js('Buckle'), Js('Can'), Js('Cant'), Js('Caper'), Js('Char'), Js('Chaun'), Js('Chisel'), Js('Chro'), Js('Chrono'), Js('Cinder'), Js('Cine'), Js('Coal'), Js('Cog'), Js('Cokum'), Js('Cooper'), Js('Cove'), Js('Cover'), Js('Crank'), Js('Crow'), Js('Dapple'), Js('Dark'), Js('Dawn'), Js('Deca'), Js('Dillo'), Js('Dipper'), Js('Diri'), Js('Dirigi'), Js('Dobbin'), Js('Drag'), Js('Dread'), Js('Dub'), Js('Duc'), Js('Duffer'), Js('Dumplin'), Js('Dusk'), Js('Dyna'), Js('Ebon'), Js('Ember'), Js('Ether'), Js('Flam'), Js('Flush'), Js('Fogle'), Js('Gaff'), Js('Gallie'), Js('Gammon'), Js('Gatter'), Js('Gear'), Js('Gearing'), Js('Gegor'), Js('Giz'), Js('Gizmo'), Js('Glim'), Js('Glimmer'), Js('Glimming'), Js('Glock'), Js('Goggle'), Js('Gouge'), Js('Grap'), Js('Graven'), Js('Gray'), Js('Grim'), Js('Grime'), Js('Grub'), Js('Heat'), Js('Heather'), Js('Heli'), Js('Hob'), Js('Hobble'), Js('Ichor'), Js('Iron'), Js('Ivor'), Js('Ivory'), Js('Jemmy'), Js('Jugger'), Js('Kanur'), Js('Ken'), Js('Kenning'), Js('Kennuck'), Js('Kife'), Js('Kine'), Js('Kino'), Js('Knap'), Js('Labo'), Js('Lag'), Js('Leaden'), Js('Leg'), Js('Lever'), Js('Lill'), Js('Lug'), Js('Lugger'), Js('Lushing'), Js('Mag'), Js('Meck'), Js('Mecking'), Js('Mel'), Js('Mill'), Js('Milling'), Js('Min'), Js('Mizzle'), Js('Muffle'), Js('Mumper'), Js('Murk'), Js('Nedding'), Js('Nether'), Js('Nobble'), Js('Nom'), Js('Nox'), Js('Nubbik'), Js('Obsidi'), Js('Onyx'), Js('Padding'), Js('Pall'), Js('Para'), Js('Peri'), Js('Pitch'), Js('Plu'), Js('Pneu'), Js('Poly'), Js('Pradding'), Js('Prater'), Js('Prong'), Js('Rack'), Js('Racket'), Js('Rain'), Js('Raven'), Js('Reaming'), Js('Reeb'), Js('Rig'), Js('Rip'), Js('Riven'), Js('Rook'), Js('Rooker'), Js('Rozzer'), Js('Ruffle'), Js('Scal'), Js('Scran'), Js('Scuttle'), Js('Sere'), Js('Shevi'), Js('Skip'), Js('Skipper'), Js('Skipping'), Js('Slate'), Js('Sloe'), Js('Slum'), Js('Snell'), Js('Snow'), Js('Snoz'), Js('Soot'), Js('Speeler'), Js('Spindle'), Js('Steam'), Js('Steel'), Js('Swart'), Js('Swelling'), Js('Tatting'), Js('Terra'), Js('Tine'), Js('Tinker'), Js('Titfer'), Js('Toff'), Js('Toffing'), Js('Tol'), Js('Tooler'), Js('Toper'), Js('Topping'), Js('Twirl'), Js('Tyro'), Js('Umber'), Js('Van'), Js('Velo'), Js('Veloci'), Js('Vex'), Js('Voli'), Js('Vox'), Js('Wheal'), Js('Whealing')]))
var.put('nm2', Js([Js('barrow'), Js('borough'), Js('bourne'), Js('burg'), Js('burgh'), Js('burn'), Js('bury'), Js('cairn'), Js('dale'), Js('denn'), Js('drift'), Js('edge'), Js('fall'), Js('fell'), Js('ford'), Js('fort'), Js('garde'), Js('gate'), Js('glen'), Js('guard'), Js('gue'), Js('haben'), Js('hagen'), Js('hallow'), Js('ham'), Js('haven'), Js('helm'), Js('hold'), Js('hollow'), Js('mere'), Js('mire'), Js('moor'), Js('more'), Js('mourne'), Js('point'), Js('port'), Js('rath'), Js('stead'), Js('stein'), Js('storm'), Js('sturm'), Js('thain'), Js('ton'), Js('town'), Js('vale'), Js('wall'), Js('wallow'), Js('ward'), Js('watch'), Js('worth')]))
pass
pass


# Add lib to the module scope
steampunkCities = var.to_python()