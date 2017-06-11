__all__ = ['caves']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm7').get(var.get('rnd6')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abysmal'), Js('Adamantine'), Js('Ancient'), Js('Angry'), Js('Arching'), Js('Arctic'), Js('Arid'), Js('Bare'), Js('Beholding'), Js('Bellowing'), Js('Black'), Js('Bleak'), Js('Blue'), Js('Boiling'), Js('Bottomless'), Js('Boundless'), Js('Brilliant'), Js('Bronze'), Js('Burned'), Js('Burning'), Js('Calm'), Js('Calmest'), Js('Charmed'), Js('Cheerless'), Js('Climbing'), Js('Cobalt'), Js('Cold'), Js('Collapsing'), Js('Colorless'), Js('Colossal'), Js('Coral'), Js('Crystal'), Js('Cunning'), Js('Cursed'), Js('Dancing'), Js('Dangerous'), Js('Dark'), Js('Darkest'), Js('Dead'), Js('Decayed'), Js('Decaying'), Js('Deep'), Js('Deepest'), Js('Dense'), Js('Depraved'), Js('Deserted'), Js('Desolate'), Js('Desolated'), Js('Diamond'), Js('Distant'), Js('Dread'), Js('Dreaded'), Js('Dreadful'), Js('Dreary'), Js('Dry'), Js('Eastern'), Js('Emerald'), Js('Empty'), Js('Enchanted'), Js('Enormous'), Js('Eroded'), Js('Ethereal'), Js('Ever Reaching'), Js('Everlasting'), Js('Fabled'), Js('Faraway'), Js('Farthest'), Js('Feared'), Js('Fearsome'), Js('Fiery'), Js('Flaring'), Js('Flat'), Js('Flowing'), Js('Foaming'), Js('Forbidden'), Js('Forbidding'), Js('Fractured'), Js('Frightening'), Js('Frozen'), Js('Gargantuan'), Js('Giant'), Js('Gigantic'), Js('Glassy'), Js('Gleaming'), Js('Glistening'), Js('Gloomy'), Js('Glowing'), Js('Gold'), Js('Golden'), Js('Grave'), Js('Gray'), Js('Green'), Js('Grim'), Js('Harmonious'), Js('Haunted'), Js('Heaving'), Js('Hellish'), Js('Hollow'), Js('Homeless'), Js('Hopeless'), Js('Hot'), Js('Huge'), Js('Humongous'), Js('Hungry'), Js('Immense'), Js('Infernal'), Js('Infinite'), Js('Invisible'), Js('Iron'), Js('Isolated'), Js('Jade'), Js('Jagged'), Js('Killing'), Js('Laughing'), Js('Lifeless'), Js('Light'), Js('Lightest'), Js('Living'), Js('Lonely'), Js('Lucent'), Js('Majestic'), Js('Malevolent'), Js('Malicious'), Js('Mammoth'), Js('Mesmerizing'), Js('Mighty'), Js('Mirrored'), Js('Misty'), Js('Moaning'), Js('Molten'), Js('Monotonous'), Js('Monstrous'), Js('Motionless'), Js('Mysterious'), Js('Narrow'), Js('Neverending'), Js('New'), Js('Northern'), Js('Open'), Js('Orient'), Js('Overhanging'), Js('Parched'), Js('Peaceful'), Js('Perfumed'), Js('Plain'), Js('Pleasant'), Js('Prickly'), Js('Primeval'), Js('Quiet'), Js('Raging'), Js('Red'), Js('Relentless'), Js('Remote'), Js('Restless'), Js('Rocking'), Js('Rocky'), Js('Rough'), Js('Rugged'), Js('Sad'), Js('Sandy'), Js('Sanguine'), Js('Savage'), Js('Scarlet'), Js('Scorching'), Js('Serene'), Js('Severed'), Js('Shadow'), Js('Shadowed'), Js('Shadowy'), Js('Shimmering'), Js('Silent'), Js('Silver'), Js('Sleeping'), Js('Slumbering'), Js('Slumbrous'), Js('Sly'), Js('Soundless'), Js('Southern'), Js('Spacious'), Js('Sparkling'), Js('Sterile'), Js('Stern'), Js('Straitened'), Js('Sunny'), Js('Symmetrical'), Js('Teal'), Js('Terraced'), Js('Terrestrial'), Js('Throbbing'), Js('Thundering'), Js('Tinted'), Js('Titanic'), Js('Tranquil'), Js('Treacherous'), Js('Troubled'), Js('Turbulent'), Js('Turquoise'), Js('Twisting'), Js('Ugly'), Js('Uncanny'), Js('Unfathomed'), Js('Uninviting'), Js('Unknown'), Js('Unresting'), Js('Unruffled'), Js('Unscaled'), Js('Unstable'), Js('Unwelcoming'), Js('Vast'), Js('Violent'), Js('Voiceless'), Js('Volcanic'), Js('Walled'), Js('Wasted'), Js('Wasteful'), Js('Wasting'), Js('Welcoming'), Js('Western'), Js('Whelming'), Js('Whispering'), Js('White'), Js('Wild'), Js('Windless'), Js('Windy'), Js('Withered'), Js('Wondering'), Js('Wrinkled'), Js('Yearning'), Js('Yelling'), Js('Yellow')]))
var.put('nm2', Js([Js('Cave'), Js('Cavern'), Js('Grotto'), Js('Den'), Js('Cavity'), Js('Hollow'), Js('Hollows'), Js('Caves'), Js('Caverns'), Js('Hole'), Js('Hideout'), Js('Shelter'), Js('Overhang'), Js('Sanctuary'), Js('Subterrane')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
var.put('nm7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
pass
pass


# Add lib to the module scope
caves = var.to_python()