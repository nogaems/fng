__all__ = ['volcanoNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names8', 'names2', 'names3', 'names1', 'names7'])
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
                var.put('name', (Js('Mount ')+var.get('names1').get(var.get('rnd'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
                    var.put('name', (((Js('The ')+var.get('names2').get(var.get('rnd')))+Js(' '))+var.get('names8').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('name', (((((Js('Mount ')+var.get('names3').get(var.get('rnd')))+var.get('names4').get(var.get('rnd2')))+var.get('names5').get(var.get('rnd3')))+var.get('names6').get(var.get('rnd4')))+var.get('names7').get(var.get('rnd5'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Acrimony'), Js('Agony'), Js('Anguish'), Js('Animus'), Js('Apathy'), Js('Ashcloud'), Js('Ashenfield'), Js('Ashstorm'), Js('Bane'), Js('Barrage'), Js('Bedrock'), Js('Blackcloud'), Js('Blackfuse'), Js('Blackout'), Js('Blackpeak'), Js('Blackrock'), Js('Blastfury'), Js('Boulderblast'), Js('Boulderclash'), Js('Boulderpeak'), Js('Boulderrain'), Js('Boulderscream'), Js('Bouldersmash'), Js('Bravery'), Js('Calamity'), Js('Cataclysm'), Js('Charcoal'), Js('Death'), Js('Deluge'), Js('Destiny'), Js('Destruction'), Js('Diablo'), Js('Doom'), Js('Downfall'), Js('Ebon'), Js('Ebony'), Js('Eclipse'), Js('Empathy'), Js('Envy'), Js('Equilibrium'), Js('Equity'), Js('Ferocity'), Js('Fireburst'), Js('Flux'), Js('Fortune'), Js('Frenzy'), Js('Furor'), Js('Fury'), Js('Harmony'), Js('Hate'), Js('Hatred'), Js('Heinous'), Js('Hellion'), Js('Horror'), Js('Immolate'), Js('Infamy'), Js('Injury'), Js('Ire'), Js('Judgment'), Js('Karma'), Js('Limbo'), Js('Maleficent'), Js('Malice'), Js('Malicious'), Js('Mercy'), Js('Misery'), Js('Moltencore'), Js('Moltenfury'), Js('Moltenrock'), Js('Mystery'), Js('Necrosis'), Js('Nefarious'), Js('Nightfall'), Js('Obidian'), Js('Oblivion'), Js('Obscurity'), Js('Odium'), Js('Onyx'), Js('Paradise'), Js('Parity'), Js('Passion'), Js('Penance'), Js('Rage'), Js('Rampage'), Js('Rancor'), Js('Rapture'), Js('Repose'), Js('Rockfury'), Js('Rubblefield'), Js('Ruin'), Js('Sacrifice'), Js('Savagery'), Js('Serenity'), Js('Severity'), Js('Sin'), Js('Sorrow'), Js('Spite'), Js('Stasis'), Js('Storm'), Js('Stormpeak'), Js('Temper'), Js('Terminator'), Js('Terror'), Js('Thunder'), Js('Thundercloud'), Js('Thunderhowl'), Js('Thunderrage'), Js('Thunderrock'), Js('Thunderscream'), Js('Torment'), Js('Tragedy'), Js('Tranquility'), Js('Twilight'), Js('Umbrage'), Js('Unity'), Js('Vengeance'), Js('Vicious'), Js('Violence'), Js('Void'), Js('Woe'), Js('Wrath'), Js('Wrath of God')]))
var.put('names2', Js([Js('Aching'), Js('Angry'), Js('Ashen'), Js('Barrage'), Js('Bellowing'), Js('Blazing'), Js('Blistering'), Js('Boiling'), Js('Bombarding'), Js('Booming'), Js('Burning'), Js('Bursting'), Js('Carbon'), Js('Charcoal'), Js('Charring'), Js('Cinder'), Js('Clouded'), Js('Collapsing'), Js('Combusting'), Js('Consuming'), Js('Crashing'), Js('Crimson'), Js('Crumbling'), Js('Crying'), Js('Deafening'), Js('Demon'), Js('Devil'), Js('Devouring'), Js('Diablo'), Js('Dormant'), Js('Dozing'), Js('Dreaming'), Js('Drowsy'), Js('Drumming'), Js('Dynamic'), Js('Ebon'), Js('Ember'), Js('Eruptive'), Js('Exhausted'), Js('Exploding'), Js('Explosive'), Js('Fading'), Js('Fever'), Js('Fiery'), Js('Flaming'), Js('Flowing'), Js('Forsaken'), Js('Fuming'), Js('Furious'), Js('Gleaming'), Js('Glowing'), Js('God'), Js('Growing'), Js('Hellfire'), Js('Hellgate'), Js('Hellish'), Js('Hibernating'), Js('Howling'), Js('Inert'), Js('Inferno'), Js('Kindling'), Js('Latent'), Js('Liquid'), Js('Living'), Js('Maroon'), Js('Mellow'), Js('Mighty'), Js('Moaning'), Js('Molten'), Js('Monster'), Js('Mourning'), Js('Moving'), Js('Nefarious'), Js('Nether'), Js('Obscured'), Js('Obsidian'), Js('Onyx'), Js('Parching'), Js('Rabid'), Js('Raging'), Js('Rampant'), Js('Resting'), Js('Roaring'), Js('Roasting'), Js('Running'), Js('Sanguine'), Js('Scalding'), Js('Scarlet'), Js('Scorching'), Js('Screaming'), Js('Searing'), Js('Shadow'), Js('Shattered'), Js('Sizzling'), Js('Slag'), Js('Sleeping'), Js('Sluggish'), Js('Slumbering'), Js('Smoking'), Js('Smoldering'), Js('Snoring'), Js('Sobbing'), Js('Somber'), Js('Steaming'), Js('Storm'), Js('Thunder'), Js('Thundering'), Js('Titan'), Js('Turbulent'), Js('Vanishing'), Js('Vermilion'), Js('Vibrant'), Js('Vicious'), Js('Violent'), Js('Wasted'), Js('Wasteland'), Js('Weeping')]))
var.put('names3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('names5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('names7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
var.put('names8', Js([Js('Mountain'), Js('Mountains'), Js('Summit'), Js('Peaks'), Js('Precipice'), Js('Heights'), Js('Apex'), Js('Vertex'), Js('Pinnacle')]))
pass
pass


# Add lib to the module scope
volcanoNames = var.to_python()