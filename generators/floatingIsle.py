__all__ = ['floatingIsle']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen', 'nm4', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm5', 'result'])
    var.put('nm5', Js([Js('Aeranas'), Js('Aerene'), Js('Aeria'), Js('Aeris'), Js('Aeros'), Js('Aerule'), Js('Albatross'), Js('Angel'), Js('Apex'), Js('Apogee'), Js('Ataraxia'), Js('Ataraxis'), Js('Atmos'), Js('Aura'), Js('Aurora'), Js('Avia'), Js('Avian'), Js('Avis'), Js('Azura'), Js('Azure'), Js('Azuris'), Js('Billow'), Js('Bliss'), Js('Borealis'), Js('Buoya'), Js('Bustard'), Js('Cassowary'), Js('Celes'), Js('Celeste'), Js('Cerulea'), Js('Cerulis'), Js('Cerulle'), Js('Chinook'), Js('Cirrostratus'), Js('Cirrus'), Js('Condor'), Js('Crane'), Js('Crow'), Js('Crown'), Js('Cuckoo'), Js('Cumulus'), Js('Dove'), Js('Eagle'), Js('Elysium'), Js('Empyre'), Js('Empyrea'), Js('Empyris'), Js('Falcon'), Js('Flamingo'), Js('Gale'), Js('Griffin'), Js('Gull'), Js('Halo'), Js('Halos'), Js('Harmony'), Js('Harpy'), Js('Hippogriff'), Js('Hummingbird'), Js('Imperos'), Js('Macaw'), Js('Mistral'), Js('Mistros'), Js('Murmus'), Js('Nebula'), Js('Nightingale'), Js('Nightowl'), Js('Obelisk'), Js('Owl'), Js('Ozone'), Js('Peacock'), Js('Pegasus'), Js('Pelican'), Js('Phoenix'), Js('Pigeon'), Js('Raven'), Js('Serenity'), Js('Solace'), Js('Sonas'), Js('Sonus'), Js('Sparrow'), Js('Spire'), Js('Stork'), Js('Storm'), Js('Stormy'), Js('Stratos'), Js('Stratus'), Js('Swan'), Js('Swift'), Js('Thunder'), Js('Toocan'), Js('Tranquility'), Js('Tropos'), Js('Tumul'), Js('Tumulus'), Js('Utopia'), Js('Valkyrie'), Js('Ventis'), Js('Vertex'), Js('Volance'), Js('Volantis'), Js('Volar'), Js('Volaris'), Js('Vortex'), Js('Vox'), Js('Voxis'), Js('Vulture'), Js('Windy'), Js('Zenith'), Js('Zephyr'), Js('Zephys'), Js('Zion')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nm6').get(var.get('rnd7'))))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd5')))+Js(' '))+var.get('nm6').get(var.get('rnd7'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.get('nm5').callprop('splice', var.get('rnd'), Js(1.0))
                var.put('names', ((var.get('nm5').get(var.get('rnd'))+Js(' '))+var.get('nm6').get(var.get('rnd7'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('dh'), Js('f'), Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('ph'), Js('s'), Js('sh'), Js('th'), Js('v'), Js('w')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('o'), Js('ea'), Js('ae'), Js('ia'), Js('ai'), Js('eo')]))
var.put('nm3', Js([Js('b'), Js('b'), Js('f'), Js('f'), Js('ff'), Js('g'), Js('g'), Js('h'), Js('h'), Js('j'), Js('j'), Js('l'), Js('l'), Js('ll'), Js('m'), Js('m'), Js('mm'), Js('n'), Js('n'), Js('nn'), Js('r'), Js('r'), Js('s'), Js('s'), Js('ss'), Js('th'), Js('th'), Js('v'), Js('v'), Js('b'), Js('bh'), Js('bl'), Js('bs'), Js('br'), Js('f'), Js('ff'), Js('fl'), Js('fr'), Js('g'), Js('gh'), Js('gn'), Js('gl'), Js('h'), Js('hn'), Js('hl'), Js('hm'), Js('j'), Js('l'), Js('lf'), Js('ll'), Js('lt'), Js('lc'), Js('lb'), Js('ld'), Js('lm'), Js('ln'), Js('lr'), Js('lw'), Js('m'), Js('mm'), Js('mn'), Js('mr'), Js('n'), Js('nn'), Js('ns'), Js('nth'), Js('nt'), Js('nm'), Js('nf'), Js('nph'), Js('pr'), Js('phr'), Js('r'), Js('rl'), Js('rm'), Js('rn'), Js('s'), Js('sf'), Js('sh'), Js('sp'), Js('st'), Js('sw'), Js('ss'), Js('sn'), Js('sm'), Js('th'), Js('v')]))
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('th')]))
var.put('nm6', Js([Js('Island'), Js('Enclave'), Js('Isle'), Js('Islet'), Js('Island'), Js('Isle')]))
pass
pass


# Add lib to the module scope
floatingIsle = var.to_python()