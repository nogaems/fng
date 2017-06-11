__all__ = ['skyCities']

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
    var.registers(['nm5', 'nm8', 'nm7', 'nm9', 'nm10', 'result'])
    var.put('nm7', Js([Js('Aer'), Js('Aera'), Js('Aere'), Js('Aeri'), Js('Air'), Js('Ar'), Js('Aro'), Js('Atmo'), Js('Avi'), Js('Avia'), Js('Avis'), Js('Azu'), Js('Brey'), Js('Cele'), Js('Celes'), Js('Chi'), Js('Chinoo'), Js('Cir'), Js('Circo'), Js('Clo'), Js('Clod'), Js('Clou'), Js('Cloud'), Js('Cyclo'), Js('Empear'), Js('Exa'), Js('Exalo'), Js('Flur'), Js('Gal'), Js('Gale'), Js('Hali'), Js('Halo'), Js('Huri'), Js('Huric'), Js('Impe'), Js('Imper'), Js('Mis'), Js('Mur'), Js('Oxy'), Js('Ozo'), Js('Sky'), Js('Skye'), Js('Son'), Js('Sona'), Js('Soni'), Js('Stra'), Js('Tempe'), Js('Tempes'), Js('Tro'), Js('Tropo'), Js('Tum'), Js('Tumu'), Js('Tumul'), Js('Ven'), Js('Venti'), Js('Vol'), Js('Vola'), Js('Vox'), Js('Xy'), Js('Zeph'), Js('Zephy')]))
    var.put('nm8', Js([Js('polis'), Js('more'), Js('bay'), Js('bell'), Js('bury'), Js('cairn'), Js('call'), Js('crest'), Js('cross'), Js('drift'), Js('ham'), Js('helm'), Js('hold'), Js('holde'), Js('mere'), Js('mire'), Js('mond'), Js('moor'), Js('more'), Js('rest'), Js('run'), Js('wich'), Js('star'), Js('storm'), Js('strand'), Js('summit'), Js('tide'), Js('wallow'), Js('ward'), Js('watch'), Js('well')]))
    var.put('nm9', Js([Js('Aera'), Js('Aeranas'), Js('Aeria'), Js('Aeris'), Js('Aeros'), Js('Ara'), Js('Aros'), Js('Atmos'), Js('Auris'), Js('Aurora'), Js('Avia'), Js('Avian'), Js('Avis'), Js('Azur'), Js('Azura'), Js('Azuros'), Js('Borealis'), Js('Breyze'), Js('Celes'), Js('Cerul'), Js('Cerulea'), Js('Cerulis'), Js('Cerulle'), Js('Cerullis'), Js('Chinook'), Js('Circos'), Js('Cirrus'), Js('Clode'), Js('Empearal'), Js('Ether'), Js('Ethis'), Js('Ethos'), Js('Exalos'), Js('Flurris'), Js('Gale'), Js('Gayle'), Js('Halitos'), Js('Halitus'), Js('Halo'), Js('Halos'), Js('Helios'), Js('Horizon'), Js('Huricus'), Js('Imperos'), Js('Mistral'), Js('Mulus'), Js('Murmus'), Js('Nimbus'), Js('Orion'), Js('Oxyn'), Js('Ozon'), Js('Sonas'), Js('Sonis'), Js('Sono'), Js('Sonus'), Js('Spheris'), Js('Spheros'), Js('Stratos'), Js('Tempeste'), Js('Tempestus'), Js('Tropos'), Js('Tumul'), Js('Tumulus'), Js('Ventis'), Js('Volance'), Js('Volaris'), Js('Vox'), Js('Voxis'), Js('Welkis'), Js('Xygen'), Js('Zephyr'), Js('Zephys'), Js('Zures'), Js('Zuros')]))
    var.put('nm10', Js([Js('New '), Js('Nova '), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('nm5', Js([Js('Aeranas'), Js('Aerene'), Js('Aeria'), Js('Aeris'), Js('Aeros'), Js('Aerule'), Js('Albatross'), Js('Angel'), Js('Apex'), Js('Apogee'), Js('Ataraxia'), Js('Ataraxis'), Js('Atmos'), Js('Aura'), Js('Aurora'), Js('Avia'), Js('Avian'), Js('Avis'), Js('Azura'), Js('Azure'), Js('Azuris'), Js('Billow'), Js('Bliss'), Js('Borealis'), Js('Buoya'), Js('Bustard'), Js('Cassowary'), Js('Celes'), Js('Celeste'), Js('Cerulea'), Js('Cerulis'), Js('Cerulle'), Js('Chinook'), Js('Cirrostratus'), Js('Cirrus'), Js('Condor'), Js('Crane'), Js('Crow'), Js('Crown'), Js('Cuckoo'), Js('Cumulus'), Js('Dove'), Js('Eagle'), Js('Elysium'), Js('Empyre'), Js('Empyrea'), Js('Empyris'), Js('Falcon'), Js('Flamingo'), Js('Gale'), Js('Griffin'), Js('Gull'), Js('Halo'), Js('Halos'), Js('Harmony'), Js('Harpy'), Js('Hippogriff'), Js('Hummingbird'), Js('Imperos'), Js('Macaw'), Js('Mistral'), Js('Mistros'), Js('Murmus'), Js('Nebula'), Js('Nightingale'), Js('Nightowl'), Js('Obelisk'), Js('Owl'), Js('Ozone'), Js('Peacock'), Js('Pegasus'), Js('Pelican'), Js('Phoenix'), Js('Pigeon'), Js('Raven'), Js('Serenity'), Js('Solace'), Js('Sonas'), Js('Sonus'), Js('Sparrow'), Js('Spire'), Js('Stork'), Js('Storm'), Js('Stormy'), Js('Stratos'), Js('Stratus'), Js('Swan'), Js('Swift'), Js('Thunder'), Js('Toocan'), Js('Tranquility'), Js('Tropos'), Js('Tumul'), Js('Tumulus'), Js('Utopia'), Js('Valkyrie'), Js('Ventis'), Js('Vertex'), Js('Volance'), Js('Volantis'), Js('Volar'), Js('Volaris'), Js('Vortex'), Js('Vox'), Js('Voxis'), Js('Vulture'), Js('Windy'), Js('Zenith'), Js('Zephyr'), Js('Zephys'), Js('Zion')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(3.0)):
                    var.put('names', (((((Js('The city of ')+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', (((((((Js('The city of ')+var.get('nm1').get(var.get('rnd')))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm3').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm4').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', (var.get('nm7').get(var.get('rnd'))+var.get('nm8').get(var.get('rnd2'))))
                    var.get('nm7').callprop('splice', var.get('rnd'), Js(1.0))
                    var.get('nm8').callprop('splice', var.get('rnd2'), Js(1.0))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', (var.get('nm10').get(var.get('rnd2'))+var.get('nm9').get(var.get('rnd'))))
                    var.get('nm9').callprop('splice', var.get('rnd'), Js(1.0))
                    var.get('nm10').callprop('splice', var.get('rnd2'), Js(1.0))
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
var.put('nm4', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('sh'), Js('ph'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('th')]))
pass
pass


# Add lib to the module scope
skyCities = var.to_python()