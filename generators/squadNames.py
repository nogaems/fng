__all__ = ['squadNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('names', (((Js('The ')+var.get('names1').get(var.get('rnd')))+Js(' '))+var.get('names6').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(6.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('names', (Js('The ')+var.get('names2').get(var.get('rnd'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('names', ((((var.get('names3').get(var.get('rnd'))+Js(' '))+var.get('names4').get(var.get('rnd2')))+Js(' '))+var.get('names5').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Alpha'), Js('Angel'), Js('Annihilation'), Js('Apache'), Js('Arachnid'), Js('Ash'), Js('Bane'), Js('Recon'), Js('Assault'), Js('Banshee'), Js('Barrage'), Js('Beast'), Js('Behemoth'), Js('Black Skull'), Js('Blast'), Js('Blitz'), Js('Bravo'), Js('Burning'), Js('Carnage'), Js('Cobra'), Js('Coyote'), Js('Crisis'), Js('Cyclone'), Js('Daemon'), Js('Danger'), Js('Demon'), Js('Disaster'), Js('Dragon'), Js('Electric'), Js('Elimination'), Js('Enigma'), Js('Ethereal'), Js('Extinction'), Js('Feral'), Js('Fiery'), Js('Fire'), Js('Firebolt'), Js('Flux'), Js('Frozen'), Js('Ghost'), Js('Grindstone'), Js('Guardian'), Js('Havoc'), Js('Hazard'), Js('Honor'), Js('Hurricane'), Js('Ice'), Js('Jackal'), Js('Jester'), Js('Leopard'), Js('Lightning'), Js('Lion'), Js('Mammoth'), Js('Marvel'), Js('Miracle'), Js('Mirage'), Js('Monster'), Js('Mutant'), Js('Nemesis'), Js('Nightmare'), Js('Omega'), Js('Oracle'), Js('Padlock'), Js('Panther'), Js('Phantom'), Js('Phoenix'), Js('Plague'), Js('Prodigy'), Js('Rage'), Js('Raid'), Js('Rattle'), Js('Ravage'), Js('Red Demon'), Js('Riot'), Js('Rogue'), Js('Rubble'), Js('Rumble'), Js('Scourge'), Js('Serpent'), Js('Shadow'), Js('Shatter'), Js('Silent'), Js('Silver'), Js('Skirmish'), Js('Spider'), Js('Spirit'), Js('Stampede'), Js('Storm'), Js('Surge'), Js('Thunder'), Js('Tiger'), Js('Titan'), Js('Turtle'), Js('Viper'), Js('Void'), Js('Whisper'), Js('White Skull'), Js('White Wolf'), Js('Wild'), Js('Wipe Out'), Js('Wolf'), Js('Wreckage')]))
var.put('names2', Js([Js('Freaks'), Js('Alphas'), Js('Angels'), Js('Silver Angels'), Js('Hellhounds'), Js('Thunderbirds'), Js('Vikings'), Js('Arachnids'), Js('Ashes'), Js('Banshees'), Js('Beasts'), Js('Behemoths'), Js('Black Skulls'), Js('Cobras'), Js('Coyotes'), Js('Cyclones'), Js('Daemons'), Js('Demons'), Js('Dragons'), Js('Enigmas'), Js('Ethereals'), Js('Ferals'), Js('Firebolts'), Js('Ghosts'), Js('Guardians'), Js('Hurricanes'), Js('Jackals'), Js('Jesters'), Js('Leopards'), Js('Lightning Bolts'), Js('Lions'), Js('Mammoths'), Js('Marvels'), Js('Miracles'), Js('Monsters'), Js('Mutants'), Js('Nightmares'), Js('Omegas'), Js('Oracles'), Js('Padlocks'), Js('Panthers'), Js('Black Panthers'), Js('Silver Banshees'), Js('Phantoms'), Js('Phoenixes'), Js('Prodigies'), Js('Red Demons'), Js('Rogues'), Js('Serpents'), Js('Shadows'), Js('Spiders'), Js('Spirits'), Js('Stormwalkers'), Js('Rolling Thunders'), Js('Tigers'), Js('Titans'), Js('Turtles'), Js('Vipers'), Js('Whispers'), Js('White Skulls'), Js('White Wolves'), Js('Wolves'), Js('Barbarians'), Js('Wildlings'), Js('Black Masks'), Js('All Blacks'), Js('Fiends'), Js('War Turtles'), Js('Mongrels'), Js('Spooks'), Js('Silence'), Js('Scepters'), Js('Strikers'), Js('Lone Wolves'), Js('Black Angels'), Js('Black Vipers'), Js('Black Mambas'), Js('Silver Wolves'), Js('White Tigers'), Js('Black Lions'), Js('Silver Lions'), Js('Black Bulls'), Js('Invisible'), Js('Disguised'), Js('Mysteries'), Js('Coverts'), Js('Goliaths'), Js('Black Cats'), Js('Daggers'), Js('Blades'), Js('Eagles'), Js('Falcons'), Js('Hornets'), Js('Red Devils'), Js('Saints'), Js('Stripes'), Js('Hammers'), Js('Wasps'), Js('Red Dragons'), Js('Black Dragons'), Js('Braves'), Js('Golden Tigers'), Js('Knights'), Js('Street Dogs'), Js('Sharks'), Js('Scorpions'), Js('Flames'), Js('Mambas'), Js('Shields'), Js('Jaguars'), Js('Nightowls'), Js('Clockworks'), Js('Valkyries')]))
var.put('names3', Js([Js('Advanced'), Js('Classified'), Js('Covert'), Js('Crisis'), Js('Disaster'), Js('Emergency'), Js('Extreme'), Js('Incident'), Js('Pressure'), Js('Situational'), Js('Special'), Js('Specialized'), Js('Standby'), Js('Stategic'), Js('Tactical'), Js('Trauma')]))
var.put('names4', Js([Js('Airborne'), Js('Assault'), Js('Assemble'), Js('Combat'), Js('Command'), Js('Control'), Js('Evaluation'), Js('Counter'), Js('Engage'), Js('Force'), Js('Intelligence'), Js('Liberation'), Js('Maintenance'), Js('Management'), Js('Mobilization'), Js('Operation'), Js('Organization'), Js('Pursuit'), Js('Reinforce'), Js('Reconnaisance'), Js('Relief'), Js('Rescue'), Js('Response'), Js('Retaliation'), Js('Salvage'), Js('Service'), Js('Support'), Js('Task'), Js('Tracking'), Js('Training'), Js('Weapons')]))
var.put('names5', Js([Js('Crew'), Js('Division'), Js('Squad'), Js('Squadron'), Js('Team'), Js('Unit')]))
var.put('names6', Js([Js('Crew'), Js('Squad'), Js('Squadron')]))
pass
pass


# Add lib to the module scope
squadNames = var.to_python()