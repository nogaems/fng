__all__ = ['daedricNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('rnd3')<Js(46.0)):
                    while (var.get('rnd4')>Js(5.0)):
                        var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    if (var.get('rnd3')<Js(46.0)):
                        while (var.get('rnd4')>Js(5.0)):
                            var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                    var.put('names', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('names', var.get('nm11').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('b'), Js('br'), Js('c'), Js('cr'), Js('ch'), Js('d'), Js('dr'), Js('g'), Js('gr'), Js('j'), Js('k'), Js('kr'), Js('kn'), Js('km'), Js('p'), Js('pr'), Js('q'), Js('qr'), Js('r'), Js('st'), Js('str'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js('zr'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('au'), Js('ou'), Js('ei'), Js('uy'), Js('oe'), Js('ua'), Js('ue'), Js('uo'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('j'), Js('k'), Js('l'), Js('m'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('km'), Js('pr'), Js('qr'), Js('st'), Js('tr'), Js('xx'), Js('g'), Js("q'"), Js("k'"), Js('rr'), Js("r'"), Js("t'"), Js('tt'), Js('vv'), Js("v'"), Js("x'"), Js("z'"), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('ag'), Js('ah'), Js('al'), Js('ala'), Js('alag'), Js('ath'), Js('bal'), Js('cath'), Js('cius'), Js('cus'), Js('dea'), Js('dia'), Js('hala'), Js('icus'), Js('ina'), Js('ine'), Js('ira'), Js('ite'), Js('lag'), Js('maeus'), Js('mina'), Js('nal'), Js('nes'), Js('oth'), Js('rath'), Js('roth'), Js('unes'), Js('ura'), Js('us'), Js('vus'), Js('yite')]))
var.put('nm6', Js([Js('b'), Js('bl'), Js('c'), Js('cl'), Js('ch'), Js('d'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gl'), Js('gn'), Js('h'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pl'), Js('ph'), Js('q'), Js('ql'), Js('s'), Js('st'), Js('sl'), Js('t'), Js('v'), Js('vl'), Js('w'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('ae'), Js('ea'), Js('eo'), Js('oe'), Js('ie'), Js('ue'), Js('ua'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm8', Js([Js('b'), Js('c'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('w'), Js('bb'), Js('bl'), Js('ff'), Js('fl'), Js('gl'), Js('gn'), Js('hh'), Js('hs'), Js('hl'), Js('hn'), Js('hm'), Js('ks'), Js('ll'), Js('lh'), Js('kh'), Js('bh'), Js('ch'), Js('dh'), Js('lm'), Js('ln'), Js('lf'), Js('mm'), Js('mn'), Js('ms'), Js('nn'), Js('ns'), Js('p'), Js('ph'), Js('ps'), Js('rf'), Js('ss'), Js('st'), Js('sh'), Js('th'), Js('ts'), Js("s'"), Js("l'"), Js("n'"), Js("m'"), Js("f'"), Js("h'")]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm10', Js([Js('ag'), Js('ah'), Js('al'), Js('ala'), Js('alag'), Js('ath'), Js('bal'), Js('cath'), Js('cius'), Js('cus'), Js('dea'), Js('dia'), Js('hala'), Js('icus'), Js('ina'), Js('ine'), Js('ira'), Js('ite'), Js('lag'), Js('maeus'), Js('mina'), Js('nal'), Js('nes'), Js('oth'), Js('rath'), Js('roth'), Js('unes'), Js('ura'), Js('us'), Js('vus'), Js('yite')]))
var.put('nm11', Js([Js('Insomnia'), Js('Lunacy'), Js('Luna'), Js('Mania'), Js('Phobia'), Js('Luna'), Js('Solar'), Js('Dementia'), Js('Hysteria'), Js('Delirium'), Js('Pedigree'), Js('Bane'), Js('Anathema'), Js('Grace'), Js('Hope'), Js('Malison'), Js('Misery'), Js('Blight'), Js('Poison'), Js('Venom'), Js('Calamity'), Js('Malificent'), Js('Sinister'), Js('Grim'), Js('Gloom'), Js('Dire'), Js('Malign'), Js('Malefic'), Js('Joy'), Js('Nova'), Js('Misty'), Js('Dusk'), Js('Dawn'), Js('Twilight'), Js('Rogue'), Js('Ominous'), Js('Vile'), Js('Nefarious'), Js('Melancholy'), Js('Saturnine'), Js('Solemn'), Js('Glum'), Js('Austere'), Js('Morose'), Js('Surly'), Js('Brusque'), Js('Gruff'), Js('Demise'), Js('Necrosis'), Js('Silence'), Js('Enigma'), Js('Virulence'), Js('Spite'), Js('Malign'), Js('Storm'), Js('Serene'), Js('Harmony'), Js('Strife'), Js('Striker'), Js('Sloth'), Js('Drowsy'), Js('Supine'), Js('Laggard')]))
pass
pass


# Add lib to the module scope
daedricNames = var.to_python()