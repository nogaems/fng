__all__ = ['inventionNames']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm4').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('Adaptable'), Js('Altered'), Js('Amplified'), Js('Analytical'), Js('Animal Powered'), Js('Aquatic'), Js('Atmospheric'), Js('Augmented'), Js('Automated'), Js('Auxiliary'), Js('Bionic'), Js('Comprehensive'), Js('Computerized'), Js('Diagnostic'), Js('Electromagnetic'), Js('Electronic'), Js('Encrypted'), Js('Enhanced'), Js('Experimatic'), Js('Experitron'), Js('Explosive'), Js('Extended'), Js('Extraordinary'), Js('Extrematic'), Js('Gizmatic'), Js('Global'), Js('Heavy'), Js('Heavy-Duty'), Js('Improved'), Js('Light'), Js('Lunar'), Js('Medical'), Js('Medium'), Js('Military'), Js('Mini'), Js('Miniature'), Js('Mobile'), Js('Modified'), Js('Multifunctional'), Js('Omni'), Js('Optimal'), Js('Optimized'), Js('Portable'), Js('Precise'), Js('Progressive'), Js('Reformed'), Js('Reinforced'), Js('Revised'), Js('Robotic'), Js('Robotized'), Js('Selfaware'), Js('Solar'), Js('Super'), Js('Superior'), Js('Surface'), Js('Synthesized'), Js('Synthetic'), Js('Systematic'), Js('Tactical'), Js('Titanium'), Js('Versatile'), Js('Volatile')]))
var.put('nm2', Js([Js('A.I.'), Js('Aid'), Js('Air'), Js('Ammo'), Js('Antidote'), Js('Antivenom'), Js('Assist'), Js('Aura'), Js('Barrier'), Js('Battle'), Js('Biopsy'), Js('Blackout'), Js('Blockade'), Js('Blood'), Js('Bomb'), Js('Bone'), Js('Broadcast'), Js('Care'), Js('Casualty'), Js('Cell'), Js('Chemical'), Js('Clay'), Js('Cloud'), Js('Code'), Js('Combat'), Js('Comfort'), Js('Construction'), Js('Cooking'), Js('Crime'), Js('Crop'), Js('Cure'), Js('Data'), Js('Defence'), Js('Disaster'), Js('Disease'), Js('Dream'), Js('Echo'), Js('Emergency'), Js('Essence'), Js('Exam'), Js('Farm'), Js('Fire'), Js('First Aid'), Js('Flame'), Js('Flood'), Js('Food'), Js('Ghost'), Js('Guidance'), Js('Hazard'), Js('Heal'), Js('Hologram'), Js('Ice'), Js('Idea'), Js('Laser'), Js('Life'), Js('Light'), Js('Load'), Js('Luggage'), Js('Lumination'), Js('Magnet'), Js('Measurement'), Js('Medicine'), Js('Message'), Js('Mimic'), Js('Mine'), Js('Mold'), Js('Moon'), Js('Motion'), Js('Mountain'), Js('Navigation'), Js('Noise'), Js('Nutrition'), Js('Obstacle'), Js('Ocean'), Js('Ore'), Js('Package'), Js('Pet'), Js('Plague'), Js('Plant'), Js('Pollution'), Js('Probe'), Js('Propulsion'), Js('Radiation'), Js('Ray'), Js('Relief'), Js('Remedy'), Js('Rescue'), Js('Road'), Js('Sample'), Js('Scan'), Js('Science'), Js('Sea'), Js('Security'), Js('Service'), Js('Shadow'), Js('Shield'), Js('Shock'), Js('Simulation'), Js('Smog'), Js('Snow'), Js('Soil'), Js('Sound'), Js('Soundwave'), Js('Spell'), Js('Spirit'), Js('Stealth'), Js('Stone'), Js('Storage'), Js('Strategy'), Js('Strife'), Js('Sun'), Js('Support'), Js('Surgeon'), Js('Survival'), Js('Termination'), Js('Tool'), Js('Toxin'), Js('Trade'), Js('Transport'), Js('Tree'), Js('Venom'), Js('View'), Js('Virus'), Js('Vitality'), Js('Warfare'), Js('Water'), Js('Weather'), Js('Wound')]))
var.put('nm3', Js([Js('Alterator'), Js('Alternator'), Js('Analytron'), Js('Analyzer'), Js('Assembler'), Js('Attractomatic'), Js('Augmentron'), Js('Automatron'), Js('Catalyzer'), Js('Circulator'), Js('Communicator'), Js('Concealer'), Js('Concealotron'), Js('Conductron'), Js('Controller'), Js('Conveyor'), Js('Decoder'), Js('Detector'), Js('Detectron'), Js('Diagnoser'), Js('Director'), Js('Disconnector'), Js('Dislocator'), Js('Disseminator'), Js('Distrubutor'), Js('Enchanter'), Js('Encrypter'), Js('Enhancomatic'), Js('Enthraller'), Js('Enticer'), Js('Evaluator'), Js('Exchangomatic'), Js('Generator'), Js('Gyrator'), Js('Incubator'), Js('Inducer'), Js('Intensitron'), Js('Jumbler'), Js('Magnetizer'), Js('Magnificator'), Js('Manipulator'), Js('Manipulsator'), Js('Maximizer'), Js('Mechanizer'), Js('Minimizer'), Js('Mobilizer'), Js('Modificator'), Js('Modulator'), Js('Monitron'), Js('Morphomatic'), Js('Mutator'), Js('Obscurator'), Js('Possessor'), Js('Processor'), Js('Pullomatic'), Js('Reanimator'), Js('Refiner'), Js('Regenerator'), Js('Rejuvenator'), Js('Relocator'), Js('Reproducer'), Js('Revealotron'), Js('Revitalizer'), Js('Scrambler'), Js('Secretor'), Js('Separatron'), Js('Telelocator'), Js('Teleporter'), Js('Transferator'), Js('Transfigurator'), Js('Transformer'), Js('Transmitter'), Js('Transmogrifier'), Js('Transmutator'), Js('Transporter'), Js('Unscrambler'), Js('Zapper')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js('Kit'), Js('Network'), Js('Network'), Js('Interface'), Js('Interface'), Js('Matrix'), Js('Tool'), Js('Engine'), Js('Gizmo'), Js('Device'), Js('MachineKit'), Js('Matrix'), Js('Tool'), Js('Engine'), Js('Apparatus'), Js('Apparatus'), Js('Device'), Js('Machine'), Js('Doodad'), Js('Widget'), Js('Thingymajig'), Js('Mechanism'), Js('Doohickey')]))
pass
pass


# Add lib to the module scope
inventionNames = var.to_python()