__all__ = ['robotNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'names9', 'nameGen', 'names6', 'names5', 'names8', 'names2', 'names3', 'names1', 'names7'])
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
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd0'))+Js(' '))+var.get('names2').get(var.get('rnd1')))+Js(' '))+var.get('names3').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('names', var.get('names4').get(var.get('rnd0')))
                else:
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names9').get('length'))))
                    var.put('names', ((((var.get('names5').get(var.get('rnd0'))+var.get('names6').get(var.get('rnd1')))+var.get('names7').get(var.get('rnd2')))+var.get('names8').get(var.get('rnd3')))+var.get('names9').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Adept'), Js('Advanced'), Js('Artificial'), Js('Automated'), Js('Automatic'), Js('Autonomous'), Js('Bio-Electrionic'), Js('Bionic'), Js('Compact'), Js('Computerized'), Js('Conscious'), Js('Cybernated'), Js('Cybernetic'), Js('Digital'), Js('Dynamic'), Js('Efficient'), Js('Electronic'), Js('Essential'), Js('Exceptional'), Js('Experimental'), Js('Extra-Terrestrial'), Js('Extraterrestial'), Js('Extreme'), Js('General'), Js('Generic'), Js('Global'), Js('High-Powered'), Js('Highpowered'), Js('Humanoid'), Js('Independent'), Js('Integrated'), Js('Intelligent'), Js('Main'), Js('Mechanical'), Js('Mechanized'), Js('Motorized'), Js('Neohuman'), Js('Nuclear'), Js('Perceptive'), Js('Personal'), Js('Preliminary'), Js('Primary'), Js('Prime'), Js('Primitive'), Js('Programmed'), Js('Rational'), Js('Reactive'), Js('Responsive'), Js('Robotic'), Js('Secondary'), Js('Self-Aware'), Js('Self-Regulaing'), Js('Self-Reliant'), Js('Self-Sufficient'), Js('Sensitive'), Js('Sensory'), Js('Solar'), Js('Strategic'), Js('Super'), Js('Supreme'), Js('Synchronized'), Js('Temporary'), Js('Ultimate'), Js('Unified'), Js('Universal')]))
var.put('names2', Js([Js('Air Defense'), Js('Air Safety'), Js('Airplane Control'), Js('Algorithm'), Js('Analysis'), Js('Animal Control'), Js('Animal Handling'), Js('Animal Protection'), Js('Assassination'), Js('Base Protection'), Js('Battle'), Js('Bodyguard'), Js('Bomb Disposal'), Js('Care'), Js('Caretaker'), Js('Construction'), Js('Contamination'), Js('Cultivation'), Js('Data Analyzing'), Js('Data Collection'), Js('Data Destruction'), Js('Data Protection'), Js('Decoding'), Js('Demolition'), Js('Detection'), Js('Diplomacy'), Js('Docking'), Js('Domination'), Js('Education'), Js('Emergency Repair'), Js('Emergency Response'), Js('Emergency'), Js('Emulation'), Js('Encoding'), Js('Encryption'), Js('Enforcer'), Js('Engineering'), Js('Eradication'), Js('Escort'), Js('Evacuation'), Js('Evasion'), Js('Examination'), Js('Excevation'), Js('Excretion'), Js('Expedition'), Js('Exploration'), Js('Farming'), Js('Fire Fighting'), Js('First Aid'), Js('Flora and Fauna'), Js('Garbage Disposal'), Js('Guidance'), Js('Harvesting'), Js('Home Protection'), Js('Human Control'), Js('Human Protection'), Js('Human Training'), Js('Infiltration'), Js('Info Analyzing'), Js('Info Collection'), Js('Information'), Js('Inspection'), Js('Instruction'), Js('Instructor'), Js('Invasion'), Js('Lab Partner'), Js('Laboratorium'), Js('Life Emulation'), Js('Life Protection'), Js('Life Simulation'), Js('Lifeform Detection'), Js('Management'), Js('Mapping'), Js('Medical'), Js('Mining'), Js('Network Defense'), Js('Neutralization'), Js('Nullification'), Js('Observer'), Js('Ocean Exploration'), Js('Oceanic Navigation'), Js('Operating'), Js('Operation'), Js('Peacekeeping'), Js('Personal Protection'), Js('Pilot'), Js('Piloting'), Js('Planet Defence'), Js('Planet Examination'), Js('Planet Exploration'), Js('Planet Survey'), Js('Planetary Analysis'), Js('Planetary Expedition'), Js('Probe'), Js('Processor'), Js('Protection'), Js('Recording'), Js('Regulation'), Js('Repairation'), Js('Riot Control'), Js('Robot Control'), Js('Sabotage'), Js('Safety Guard'), Js('Safety'), Js('Sanitation'), Js('Science'), Js('Servant'), Js('Shepherd'), Js('Simulation'), Js('Space Expedition'), Js('Space Exploration'), Js('Space Navigation'), Js('Spacecraft Defense'), Js('Supervision'), Js('Teaching'), Js('Termination'), Js('Terraforming'), Js('Translation'), Js('Transportation'), Js('Travel'), Js('Troubleshooting'), Js('Unit Response'), Js('Usher'), Js('Utility'), Js('Vegetation'), Js('War Domination'), Js('War Management'), Js('War'), Js('Waste Collection'), Js('Waste Disposal')]))
var.put('names3', Js([Js('Android'), Js('Automaton'), Js('Bot'), Js('Cyborg'), Js('Device'), Js('Droid'), Js('Drone'), Js('Emulator'), Js('Entity'), Js('Golem'), Js('Juggernaut'), Js('Machine'), Js('Prototype'), Js('Robot'), Js('Technician'), Js('Technology')]))
var.put('names4', Js([Js('01010010 (R in binary)'), Js('Alpha'), Js('Andromeda'), Js('Andy Roid'), Js('Anne Droid'), Js('Ash'), Js('Auto'), Js('Axel'), Js('Azerty'), Js('Beta'), Js('Bit'), Js('Bolt'), Js('Booker'), Js('Boomer'), Js('Bracer'), Js('Brainstorm'), Js('Brobot'), Js('Bult'), Js('Buttons'), Js('Cabe'), Js('Clank'), Js('Cole'), Js('Combot'), Js('Copper'), Js('Core'), Js('Corion'), Js('Corius'), Js('Crowby'), Js('Curious'), Js('Cyb'), Js('Cybel'), Js('Cyd'), Js('Cyl'), Js('Cylinder'), Js('Data'), Js('Devi'), Js('Dot'), Js('Dotty'), Js('Drillbit'), Js('Dustie'), Js('Earl'), Js('Experiment'), Js('Fiber'), Js('Gadget'), Js('Gage'), Js('Gear'), Js('Gearz'), Js('Gere'), Js('Gigabit'), Js('Golem'), Js('Greez'), Js('Grezzer'), Js('Hammer'), Js('Jet'), Js('Jin'), Js('Kitt'), Js('Knave'), Js('Led'), Js('Mace'), Js('Mach'), Js('Max'), Js('Mecha'), Js('Mechan'), Js('Mechi'), Js('Micro'), Js('Mig'), Js('Norbit'), Js('Nozzle'), Js('Otis'), Js('Plex'), Js('Plexi'), Js('Plier'), Js('Prime'), Js('Proto'), Js('Qwerty'), Js('Ranger'), Js('Ratcher'), Js('Ratchet'), Js('Rob Bitt'), Js('Rob Bott'), Js('Rob Oto'), Js('Robbie'), Js('Robert'), Js('Roberto'), Js('Rubber'), Js('Rust'), Js('Rusty'), Js('Sark'), Js('Scrap'), Js('Scrappie'), Js('Scrappy'), Js('Screwie'), Js('Scythe'), Js('Scyther'), Js('Shrimp'), Js('Silver'), Js('Skip'), Js('Socket'), Js('Sona'), Js('Spanner'), Js('Spark'), Js('Sparkle'), Js('Sparky'), Js('Spencer'), Js('Spirit'), Js('Spud'), Js('Spudnik'), Js('Sterling'), Js('Talus'), Js('Tech'), Js('Tera'), Js('Terra'), Js('Test'), Js('Tin'), Js('Tink'), Js('Tinker'), Js('Tobor'), Js('Tracker'), Js('Twobit'), Js('Wire')]))
var.put('names5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('names6', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z')]))
var.put('names7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js('')]))
var.put('names8', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('x'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('x'), Js('y'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names9', Js([Js('x'), Js('tron'), Js('roid'), Js('ator'), Js('oid'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
robotNames = var.to_python()