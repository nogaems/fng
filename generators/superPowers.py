__all__ = ['superPowers']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
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
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('360-degree vision'), Js('Abacomancy'), Js('Absorb Electricty'), Js('Absorb Energy'), Js('Absorb Life Forces'), Js('Absorb Matter'), Js('Absorb Organisms'), Js('Absorb Powers'), Js('Absorb Pyschic Energy'), Js('Absorb Solar Energy'), Js('Absorb and Enhance Animal Powers'), Js('Absorb/Copy Memories'), Js('Absorb/Copy Skills/Knowledge'), Js('Accelerated Evolution'), Js('Accelerated Regeneration'), Js('Acidic Breat'), Js('Acidic Spit'), Js('Acidic Touch'), Js('Adhere to Walls and Ceilings'), Js('Age Manipulation'), Js('Alter Muscles'), Js('Alter Organisms'), Js('Alter Reality'), Js('Alter Size'), Js('Amalgamation'), Js('Anatomical Liberation'), Js('Animal Communication'), Js('Animate Objects'), Js('Animated Hair'), Js('Antimatter Manipulation'), Js('Ash Secretion'), Js('Astral Imprisonment'), Js('Astral Projection'), Js('Astral Trapping'), Js('Astral Vision'), Js('Aura Manipulation'), Js('Aura Vision'), Js('Balance Manipulation'), Js('Barbed Tail'), Js('Beacon Emission'), Js('Blade Weapon Mastery'), Js('Blood Relation Detection'), Js('Body Exchange'), Js('Calmness Projection'), Js('Chakra Manipulation'), Js('Chameleon Skin'), Js('Chaos Magic'), Js('Chi Manipulation'), Js('Chronolock'), Js('Claircognizance'), Js('Clairvoyance'), Js('Cloud Manipulation'), Js('Color Manipulation'), Js('Communicate with the dead'), Js('Concussion Beams'), Js('Contol Fungi'), Js('Control Animals'), Js('Control Birds'), Js('Control Earth'), Js('Control Fire'), Js('Control Glass'), Js('Control Gravity'), Js('Control Ice'), Js('Control Insects'), Js('Control Light'), Js('Control Lightning'), Js('Control Machines'), Js('Control Magnetic Forces'), Js('Control Mammals'), Js('Control Microwaves'), Js('Control Minerals'), Js('Control Pheromones'), Js('Control Plants'), Js('Control Radiation'), Js('Control Reptiles'), Js('Control Rodents/Small Animals'), Js('Control Sand'), Js('Control Shadows'), Js('Control Sound'), Js('Control Temperature'), Js('Control Time'), Js('Control Water'), Js('Control Wind'), Js('Control Wood'), Js('Control the Dead'), Js('Control the Elements'), Js('Control the Weather'), Js('Copy Powers (of others)'), Js('Create Illusions'), Js('Create Portals'), Js('Create Wormholes'), Js('Cross-dimensional awareness'), Js('Crystal Skin'), Js('Cyborg Body Part Replacements'), Js('Cyclone Spinning'), Js('Dark Matter Manipulation'), Js('Dawn Enhanced Strength'), Js('Day Inducement'), Js('Death Vision'), Js('Dehydration'), Js('Density Control'), Js('Deoxygenation'), Js('Dermal Armor'), Js('Destruction Magic'), Js('Detach and Regenerate Limbs'), Js('Diamond Skin'), Js('Digital Form'), Js('Disease Invulnerability'), Js('Disintegrate Matter'), Js('Disintegrate Objects'), Js('Disintegrate Organisms'), Js('Disorientating Pheromones'), Js('Divination'), Js('Dowsing'), Js('Dream Manipulation'), Js('Druid Magic'), Js('Dual Minds'), Js('Dusk Enhanced Strength'), Js('Eagle Eyesight'), Js('Echolocation'), Js('Ecological Empathy'), Js('Elasticity'), Js('Electric Body'), Js('Electric Feet'), Js('Electric Fingers'), Js('Electric Hands'), Js('Electric Invulnerability'), Js('Electric Skin'), Js('Electric Transportation'), Js('Electromagnetic Pulses'), Js('Elemental Magic'), Js('Elephant Skin'), Js('Empathy'), Js('Energy Blasts'), Js('Energy Constructs'), Js('Energy Conversion'), Js('Enhanced Acrobatics'), Js('Enhanced Awareness'), Js('Enhanced Camouflage'), Js('Enhanced Craftmanship'), Js('Enhanced Dexterity'), Js('Enhanced Jaw Strength'), Js('Enhanced Lock-picking'), Js('Enhanced Lung Capacity'), Js('Enhanced Marksmanship'), Js('Enhanced Memory'), Js('Enhanced Seductive Skills'), Js('Enhanced Senses'), Js('Enhanced Skeleton'), Js('Enhanced Stealth'), Js('Enhanced Thievery'), Js('Enhanced Tracking Skills'), Js('Escape Artist'), Js('Evocation'), Js('Extra Eye with Psychic Powers'), Js('Fatigue Immunity'), Js('Fear Projection'), Js('Feral Mind'), Js('Fingernail Claws'), Js('Fire Breath'), Js('Fire Invulnerability'), Js('Fire Touch'), Js('Fire Vision'), Js('Flight'), Js('Forcefields'), Js('Freeze Breath'), Js('Freeze Touch'), Js('Freeze Vision'), Js('Frost Invulnerability'), Js('Generate Earthquakes'), Js('Generate Energy Constructs'), Js('Generate Energy Life Forms'), Js('Generate Energy Weapons'), Js('Generate Light Bursts'), Js('Generate Powerful Dusts'), Js('Generate Volatile Constructs'), Js('Healing Powers'), Js('Heat Vision'), Js('Hive Organism'), Js('Holographic Projection'), Js('Hope Projection'), Js('Hydrokinetic'), Js('Hyper Breath'), Js('Hypnotism'), Js('Illusion Magic'), Js('Immobility'), Js('Immortality'), Js('Induced Sedation'), Js('Ink Secretion'), Js('Interdimensional Travel'), Js('Invisibility'), Js('Irresistable Charm'), Js('Jactitation'), Js('Jet Propulsion'), Js('Laser Eyes'), Js('Laser Vision'), Js('Levitation'), Js('Life Vision'), Js('Life-force Manipulation'), Js('Lifespan Vision'), Js('Liquid Skin'), Js('Liquify'), Js('Living Anomaly'), Js('Lunar Enhanced Strength'), Js('Machine Communication'), Js('Magnetic Body'), Js('Magnetic Fingers'), Js('Magnetic Hands'), Js('Manipulate Mass'), Js('Manipulate Molecules'), Js('Martial Arts Mastery'), Js('Matter Liquification'), Js('Memory Manipulation'), Js('Mental Projection'), Js('Merging Powers'), Js('Metamorphosis'), Js('Miasma Breathing'), Js('Micromorphing'), Js('Microscopic Vision'), Js('Mind Control'), Js('Mind Exchange'), Js('Mindblast'), Js('Molten Metal Skin'), Js('Morphable Body'), Js('Morphing Bone Armor'), Js('Morphing Bones'), Js('Musical Empathy'), Js('Nail Manipulation'), Js('Nerve Manipulation'), Js('Neuropsychology'), Js('Night Inducement'), Js('Night Vision'), Js('Nothingness Manipulation'), Js('Nullification'), Js('Offspring Detection'), Js('Oil Secretion'), Js('Omnilock'), Js('Omnipathy'), Js('Omnipresence'), Js('Omniscience'), Js('Organ Enhancement'), Js('Organ Removal'), Js('Oxygen Generation'), Js('Paralyzing Powers'), Js('Pathifery'), Js('Phasing'), Js('Planet Manipulation'), Js('Plant-like Body'), Js('Plasma Blasts'), Js('Poison Invulnerability'), Js('Possession'), Js('Power Bestowal'), Js('Power Disabling'), Js('Powerful Twins (Stronger Together)'), Js('Precognition'), Js('Prehensile Tongue'), Js('Premonitions'), Js('Pressure Manipulation'), Js('Projected Mind Illusions'), Js('Projected Thermography'), Js('Psionic Blast'), Js('Psychic Blasts'), Js('Psychic Illusions'), Js('Psychic Persuasion'), Js('Psychic Shield'), Js('Psychic Weapons'), Js('Psychometry'), Js('Quantum Locking'), Js('Quantum Trapping'), Js('Radio Beams'), Js('Radioactive Invulnerability'), Js('Radioactive Touch'), Js('Randomized Powers/Strengths'), Js('Rebirth'), Js('Regenerating Skin'), Js('Release Spirit from Body'), Js('Reptilian Skin'), Js('Resistance to Temperatures'), Js('Restoration Magic'), Js('Resurrection'), Js('Retractable Barbs'), Js('Retractable Claws'), Js('Retractable Horns'), Js('Retractable Nails'), Js('Retractable Pincers'), Js('Retractable Sharp Teeth'), Js('Retrocognition'), Js('Reverse Time'), Js('Revive the Dead'), Js('Rock Skin'), Js('Rot Organic Matter'), Js('Rubber Skin'), Js('Scald Generation'), Js('Scramble Radio Frequencies'), Js('Season Manipulation'), Js('Seismokinesis'), Js('Self Detonation'), Js('Self Duplication'), Js('Self Evolution'), Js('Self Resurrection'), Js('Self-Spawning'), Js('Self-Sustenance'), Js('Self-Transmutation'), Js('Sense Chi'), Js('Sense Danger'), Js('Sense Disabling'), Js('Sense Emotions'), Js('Sense Energy'), Js('Sense Fear'), Js('Sense Lies'), Js('Sense Life-forces'), Js('Sense Organisms'), Js('Sense People'), Js('Sense Powers'), Js('Shamanism'), Js('Shapeshifting'), Js('Siren Song'), Js('Slow Time'), Js('Slowed Aging'), Js('Smoke Secretion'), Js('Social Cloaking'), Js('Solar Enhanced Strength'), Js('Sonic Scream'), Js('Steel Skin'), Js('Stench Generation'), Js('Stone Skin'), Js('Strong Tail'), Js('Summon Organisms'), Js('Summoning'), Js('Super Agility'), Js('Super Balance'), Js('Super Climbing'), Js('Super Durability'), Js('Super Intelligence'), Js('Super Leaping'), Js('Super Luck/Control Luck'), Js('Super Reflexes'), Js('Super Speed'), Js('Super Stamina'), Js('Super Strength'), Js('Survive without oxygen'), Js('Technopathy'), Js('Telekinesis'), Js('Telekinetic Invulnerability'), Js('Telepathic Resistance/Immunity'), Js('Telepathy'), Js('Teleportation'), Js('Telescopic Vision'), Js('Temporal Duplication'), Js('Tentacles'), Js('Terrain Manipulation'), Js('Thorned Skin'), Js('Time Travel'), Js('Toxic Breath'), Js('Toxic Spit'), Js('Toxic Touch'), Js('Tracking Evasion'), Js('Transform into a gas state'), Js('Transmutation'), Js('Transmute Elements'), Js('Transmute Minerals'), Js('Twilight Enhanced Strength'), Js('Twilight Manipulation'), Js('Two Brains and Personalities'), Js('Two extra arms with super strength'), Js('Ultraviolet Vision'), Js('Universal Irreversability'), Js('Unstoppable Momentum'), Js('Vacuum Adaptation'), Js('Vampirism'), Js('Venom Breath'), Js('Venom Invulnerability'), Js('Venom Spit'), Js('Venom/Toxin Immunity'), Js('Vertigo Manipulation'), Js('Vibration Emission'), Js('Vibration Manipulation'), Js('View Infrared'), Js('Vocivery'), Js('Voice Manipulation'), Js('Void Manipulation'), Js('Vortex Breath'), Js('Water Breathing'), Js('Weapon Mastery'), Js('Web Secretion'), Js('Weight Manipulation'), Js('Wing Manifestation'), Js('Wish Granting'), Js('X-ray vision'), Js('Yin-Yang Manipulation')]))
pass
pass


# Add lib to the module scope
superPowers = var.to_python()