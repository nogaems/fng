__all__ = ['mountains']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd7')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                else:
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((((((var.get('nm3').get(var.get('rnd3'))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Adamantine'), Js('Ancient'), Js('Angry'), Js('Arctic'), Js('Arid'), Js('Bare'), Js('Barren'), Js('Beholding'), Js('Bellowing'), Js('Black'), Js('Bronze'), Js('Burning'), Js('Calm'), Js('Calmest'), Js('Charmed'), Js('Cold'), Js('Collapsing'), Js('Colorless'), Js('Colossal'), Js('Cursed'), Js('Dangerous'), Js('Dark'), Js('Darkest'), Js('Dead'), Js('Decayed'), Js('Decaying'), Js('Deserted'), Js('Desolate'), Js('Desolated'), Js('Diamond'), Js('Disintegrated'), Js('Distant'), Js('Dominating'), Js('Eastern'), Js('Empty'), Js('Enchanted'), Js('Enormous'), Js('Eroded'), Js('Ethereal'), Js('Ever Reaching'), Js('Everlasting'), Js('Fabled'), Js('Faraway'), Js('Feared'), Js('Fearsome'), Js('Flaring'), Js('Forbidden'), Js('Forested'), Js('Fractured'), Js('Frightening'), Js('Frozen'), Js('Gargantuan'), Js('Giant'), Js('Gigantic'), Js('Gloomy'), Js('Gold'), Js('Golden'), Js('Gray'), Js('Grim'), Js('Haunted'), Js('Heaven-reaching'), Js('Hollow'), Js('Homeless'), Js('Hopeless'), Js('Huge'), Js('Humongous'), Js('Hungry'), Js('Ice-crowned'), Js('Immense'), Js('Infernal'), Js('Iron'), Js('Isolated'), Js('Jagged'), Js('Laughing'), Js('Lifeless'), Js('Light'), Js('Lightest'), Js('Lonely'), Js('Mammoth'), Js('Mighty'), Js('Mirrored'), Js('Misty'), Js('Moaning'), Js('Monstrous'), Js('Moonlit'), Js('Motionless'), Js('Mysterious'), Js('Naked'), Js('Narrow'), Js('Neverending'), Js('New'), Js('Northern'), Js('Overhanging'), Js('Plain'), Js('Prickly'), Js('Quiet'), Js('Raging'), Js('Red'), Js('Relentless'), Js('Remote'), Js('Restless'), Js('Rocky'), Js('Round-topped'), Js('Rugged'), Js('Sad'), Js('Savage'), Js('Scarlet'), Js('Severed'), Js('Shadowed'), Js('Shadowy'), Js('Sharp-peaked'), Js('Shimmering'), Js('Silver'), Js('Slumbering'), Js('Snowy'), Js('Southern'), Js('Steep'), Js('Symmetrical'), Js('Terraced'), Js('Thundering'), Js('Titanic'), Js('Towering'), Js('Unresting'), Js('Unscaled'), Js('Unwelcoming'), Js('Vast'), Js('Violent'), Js('Voiceless'), Js('Volcanic'), Js('Welcoming'), Js('Western'), Js('Whispering'), Js('White'), Js('Windless'), Js('Windy'), Js('Wintry'), Js('Withered'), Js('Yelling')]))
var.put('nm2', Js([Js('Bluff'), Js('Heights'), Js('Highland'), Js('Highlands'), Js('Hill'), Js('Hills'), Js('Hillside'), Js('Mountain'), Js('Mountains'), Js('Peaks'), Js('Pinnacle'), Js('Rise'), Js('Slopes'), Js('Summit'), Js('Tips'), Js('Tops'), Js('Volcano')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
mountains = var.to_python()