__all__ = ['weaponAbilities']

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
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
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
var.put('nm1', Js([Js('Absolving'), Js('Ambush'), Js('Ancestral'), Js('Annihilation'), Js('Beastly'), Js('Behemoth'), Js('Betrayal'), Js('Blackout'), Js('Blazing'), Js('Bleeding'), Js('Blessed'), Js('Blind'), Js('Blinding'), Js('Blocking'), Js('Branding'), Js('Brutal'), Js('Burning'), Js('Burst'), Js('Carving'), Js('Cataclysmic'), Js('Chain'), Js('Cleaving'), Js('Colossal'), Js('Combo'), Js('Combustion'), Js('Commanding'), Js('Confusion'), Js('Corrosive'), Js('Corrupting'), Js('Corruption'), Js('Counter'), Js('Crackling'), Js('Crippling'), Js('Critical'), Js('Cruel'), Js('Crumbling'), Js('Cunning'), Js('Darkness'), Js('Dazzling'), Js('Defiled'), Js('Defiling'), Js('Demon'), Js('Destruction'), Js('Detonation'), Js('Disabling'), Js('Dishonor'), Js('Dismembering'), Js('Disrupting'), Js('Disruption'), Js('Dissecting'), Js('Dissection'), Js('Distracting'), Js('Divided'), Js('Divine'), Js('Division'), Js('Dizzying'), Js('Doom'), Js('Elusive'), Js('Enveloping'), Js('Eternal'), Js('False'), Js('Fatal'), Js('Fire'), Js('Fissure'), Js('Flame'), Js('Focusing'), Js('Fracture'), Js('Freezing'), Js('Frenzied'), Js('Frenzy'), Js('Fury'), Js('Gloom'), Js('Gore'), Js('Grave'), Js('Hemorrhaging'), Js('Holy'), Js('Honor'), Js('Howling'), Js('Hungering'), Js('Igniting'), Js('Ignition'), Js('Immobilizing'), Js('Immortal'), Js('Incinerating'), Js('Incineration'), Js('Infinity'), Js('Insanity'), Js('Interrupting'), Js('Judgment'), Js('Justice'), Js('Karma'), Js('Knockout'), Js('Lacerating'), Js('Lava'), Js('Legacy'), Js('Lightning'), Js('Mad'), Js('Mammoth'), Js('Melting'), Js('Mighty'), Js('Mirror'), Js('Molten'), Js('Mortal'), Js('Mutilation'), Js('Needle'), Js('Nimble'), Js('Overpowering'), Js('Paralyzing'), Js('Perforating'), Js('Perforation'), Js('Perpetual'), Js('Phantom'), Js('Piercing'), Js('Poison'), Js('Power'), Js('Primal'), Js('Provoking'), Js('Puncturing'), Js('Purging'), Js('Rampage'), Js('Reckless'), Js('Relentless'), Js('Righteous'), Js('Rogue'), Js('Rupturing'), Js('Ruthless'), Js('Sacrificial'), Js('Savage'), Js('Searing'), Js('Shadow'), Js('Shattering'), Js('Shocking'), Js('Shrouded'), Js('Singing'), Js('Sinister'), Js('Sliding'), Js('Smoldering'), Js('Splinter'), Js('Stealth'), Js('Stinging'), Js('Subtle'), Js('Summoning'), Js('Sundering'), Js('Sweeping'), Js('Terminal'), Js('Thunder'), Js('Titan'), Js('Titanic'), Js('Trance'), Js('Trick'), Js('Turbulent'), Js('Twin'), Js('Ultimatum'), Js('Unholy'), Js('Vampiric'), Js('Vanishing'), Js('Venom'), Js('Vital'), Js('Volley'), Js('Whirling'), Js('Whirlwind'), Js('Whispering'), Js('Wild')]))
var.put('nm2', Js([Js('Strike'), Js('Shot'), Js('Burst'), Js('Crash'), Js('Force'), Js('Thrust'), Js('Bash'), Js('Slash'), Js('Slice'), Js('Gash'), Js('Rip'), Js('Smash'), Js('Blow'), Js('Slam'), Js('Cleave'), Js('Strikes'), Js('Strike'), Js('Strike'), Js('Shot')]))
var.put('nm3', Js([Js('Absolve'), Js('Ambush'), Js('Amputate'), Js('Annihilation'), Js('Backbite'), Js('Backstab'), Js('Bait'), Js('Barrage'), Js('Battery'), Js('Betrayal'), Js('Bite'), Js('Blackout'), Js('Blockade'), Js('Bloodlust'), Js('Bombardment'), Js('Bone Crusher'), Js('Bonedust'), Js('Brand'), Js('Brutality'), Js('Bunker Buster'), Js('Burst'), Js('Calamity'), Js('Carve'), Js('Cauterize'), Js('Char'), Js('Cheat'), Js('Chomp'), Js('Chop'), Js('Chopchop'), Js('Cleave'), Js('Clobber'), Js('Cloud Burst'), Js('Combo Breaker'), Js('Combust'), Js('Conflagrate'), Js('Corrupt'), Js('Crack'), Js('Crackle'), Js('Cripple'), Js('Cruelty'), Js('Crumble'), Js('Crunch'), Js('Dance'), Js('Dark Descent'), Js('Decapitate'), Js('Decoy'), Js('Defiance'), Js('Defile'), Js('Destruction'), Js('Detonate'), Js('Devastate'), Js('Disable'), Js('Disassemble'), Js('Disjoin'), Js('Dismember'), Js('Disperse'), Js('Disrupt'), Js('Dissect'), Js('Dissever'), Js('Dissolve'), Js('Distract'), Js('Divide'), Js('Divine Division'), Js('Double-Cross'), Js('Eclipse'), Js('Energize'), Js('Energy Drain'), Js('Entangle'), Js('Envenom'), Js('Evaporate'), Js('Eviscerate'), Js('Execute'), Js('Exorcism'), Js('Fade'), Js('Feint'), Js('Ferocity'), Js('Fissure'), Js('Flare'), Js('Flurry'), Js('Fracture'), Js('Fragment'), Js('Freeze'), Js('Frenzy'), Js('Fury'), Js('Garrote'), Js('Gash'), Js('Gore'), Js('Gouge'), Js('Hamstring'), Js('Hemorrhage'), Js('Howl'), Js('Hunger'), Js('Ignite'), Js('Immobilize'), Js('Impale'), Js('Incinerate'), Js('Interruption'), Js('Jab'), Js('Jitter'), Js('Knockout'), Js('Lacerate'), Js('Lash'), Js('Life Drain'), Js('Lightning Flash'), Js('Lightspeed'), Js('Liquefy'), Js('Maim'), Js('Mangle'), Js('Melt'), Js('Mince'), Js('Mind Disrupt'), Js('Mortify'), Js('Muster'), Js('Mutilate'), Js('Myriad'), Js('Needle Rain'), Js('Nova'), Js('Overload'), Js('Overpower'), Js('Paralyze'), Js('Perforate'), Js('Pierce'), Js('Plunge'), Js('Pummel'), Js('Puncture'), Js('Purge'), Js('Rampage'), Js('Ravish'), Js('Reap'), Js('Rebuke'), Js('Rend'), Js('Riposte'), Js('Rive'), Js('Roar'), Js('Rupture'), Js('Savagery'), Js('Seize'), Js('Sever'), Js('Shatter'), Js('Shiv'), Js('Shiver'), Js('Shock'), Js('Shove'), Js('Shriek'), Js('Skewer'), Js('Skiver'), Js("Slice 'n Dice"), Js('Slide'), Js('Smash'), Js('Smother'), Js('Snap'), Js('Snapshot'), Js('Snare'), Js('Soul Drain'), Js('Spite'), Js('Splinter'), Js('Split'), Js('Split Second'), Js('Sting'), Js('Sully'), Js('Summon'), Js('Sunder'), Js('Surge'), Js('Sweep'), Js('Tear'), Js('Tempest'), Js('Terminus'), Js("Titan's Favor"), Js('Trance'), Js('Turbulence'), Js('Unleash'), Js('Vanish'), Js('Wail'), Js('Warstrike'), Js('Weaken'), Js('Weaken Mind'), Js('Whip'), Js('Whirlwind'), Js('Wither'), Js('Wrath')]))
pass
pass


# Add lib to the module scope
weaponAbilities = var.to_python()