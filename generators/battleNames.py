__all__ = ['battleNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['names4', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7', 'result'])
    var.put('names1', Js([Js('Battle'), Js('Assault'), Js('Battle'), Js('Battle'), Js('Attack'), Js('War'), Js('War'), Js('Siege')]))
    var.put('names2', Js([Js('Advisors'), Js('Allies'), Js('Ancients'), Js('Attrition'), Js('Bad Omen'), Js('Beliefs'), Js('Bent Truths'), Js('Betrayal'), Js('Blind Justice'), Js('Bloodthirst'), Js('Bows'), Js('Broken Bones'), Js('Broken Dreams'), Js('Broken Homes'), Js('Broken Laws'), Js('Broken Love'), Js('Broken Minds'), Js('Broken Mountains'), Js('Broken Pacts'), Js('Broken Wills'), Js('Brothers'), Js('Burning Fields'), Js('Burning Lands'), Js('Burning Plains'), Js('Camouflage'), Js('Chemistry'), Js('Chiefs'), Js('Corrupted Lands'), Js('Corrupted Minds'), Js('Courage'), Js('Covert Actions'), Js('Cowards'), Js('Craftsmen'), Js("Death's Fall"), Js("Death's Rise"), Js('Deception'), Js('Delirium'), Js('Devotion'), Js('Dictators'), Js('Differences'), Js('Dishonesty'), Js('Equality'), Js('Eternal Bombardments'), Js('Eternal Fires'), Js('Eternal Hunger'), Js('Eternal Regrets'), Js('Eternal Suffering'), Js('Executioners'), Js('Exploding Mountains'), Js('Faiths'), Js('Fallen Angels'), Js('False Promises'), Js('False Prophets'), Js('Fear'), Js('Final Rests'), Js('Fools'), Js('Freedom'), Js('Frozen Fires'), Js('Frozen Lakes'), Js('Glimmering Hope'), Js('Glorious Conquests'), Js('Gold'), Js('Hallow Hill'), Js('Heaven'), Js('Hell'), Js('Heroes'), Js('High Tide'), Js('Horrors'), Js('Ignorance'), Js('Imbalance'), Js('Impending Doom'), Js('Independence'), Js('Insanity'), Js('Integrity'), Js('Iron'), Js('Ivory'), Js('Justice'), Js('Kings Betrayal'), Js('Kings Glory'), Js('Kings Hill'), Js('Kings Mountain'), Js('Last Resorts'), Js('Last Rites'), Js('Liberty'), Js('Lost Brothers'), Js('Lost Faiths'), Js('Lost Friends'), Js('Lost Security'), Js('Lost Sons'), Js('Lost Souls'), Js('Loyalties'), Js('Lust'), Js('Mad Bulls'), Js('Mad Kings'), Js('Mad Minds'), Js('Maidens'), Js('Mercy'), Js('Naive Trust'), Js('Nature'), Js("Nature's Protectors"), Js('New Allies'), Js('New Hope'), Js('New Orphans'), Js('Nightmares'), Js('Open Seas'), Js('Pawns'), Js('Pests'), Js('Plagued Fires'), Js('Poisoned Crops'), Js('Poisoned Minds'), Js('Purification'), Js('Rats'), Js('Red Waters'), Js('Regrets'), Js('Resources'), Js('Scimitars'), Js('Secrets'), Js('Silence'), Js('Smoking Homes'), Js('Sons'), Js('Spears'), Js('Spies'), Js('Starvation'), Js('Steel'), Js('Storms'), Js('Strong Desires'), Js('Tenacity'), Js('Terror'), Js('Titans'), Js('Total Destruction'), Js('Total Domination'), Js('Treason'), Js('Tribulation'), Js('Trust'), Js('Truth'), Js('Tycoons'), Js('Tyrants'), Js('Unforseen Victory'), Js('Unsung Heroes'), Js('Utopia'), Js('Vengeance'), Js('Vile Actions'), Js('Vile Men'), Js('White Mountain'), Js('Widow Makers'), Js('Widows'), Js('Wits'), Js('the Ancestors'), Js('the Apocalypse'), Js('the Atlantic'), Js('the Betrayed'), Js('the Black Scar'), Js('the Blood River'), Js('the Broken Mountain'), Js('the Burning Forest'), Js('the Burning Sea'), Js('the Chanceless'), Js('the Curse'), Js('the Dark'), Js('the Dead Sea'), Js('the Dieing Forest'), Js('the Drained Sea'), Js('the Dry Sea'), Js('the Dunes'), Js('the Eclipse'), Js('the Endless Storm'), Js('the Eternal Day'), Js('the Eternal Night'), Js('the Falling Sky'), Js('the False King'), Js('the False Prophet'), Js('the Fiery Lake'), Js('the Frozen Harbor'), Js('the Frozen Ocean'), Js('the High Seas'), Js('the Homeless'), Js('the Infested'), Js('the Last Stand'), Js('the Light'), Js('the Molten Mountain'), Js('the Night'), Js('the Nomads'), Js('the Occult'), Js('the Oppressor'), Js('the Peaks'), Js('the People'), Js('the Plague'), Js('the Planet'), Js('the Rebellion'), Js('the Red Mountain'), Js('the Retreating Ocean'), Js('the Righteous'), Js('the Risen'), Js('the River Bank'), Js('the Scorching Lands'), Js('the Scourge'), Js('the Shores'), Js('the Towers'), Js('the True King'), Js('the True Prophet'), Js('the Void')]))
    var.put('names3', Js([Js('b'), Js('br'), Js('bl'), Js('c'), Js('cl'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('fl'), Js('g'), Js('gr'), Js('gl'), Js('gn'), Js('h'), Js('j'), Js('k'), Js('kr'), Js('kl'), Js('kn'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('pl'), Js('q'), Js('qr'), Js('ql'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('str'), Js('sl'), Js('t'), Js('tr'), Js('tl'), Js('v'), Js('vl'), Js('vr'), Js('w'), Js('wr'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('names4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
    var.put('names5', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('z'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('names6', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('y')]))
    var.put('names7', Js([Js('b'), Js('d'), Js('g'), Js('gh'), Js('h'), Js('hr'), Js('hs'), Js('ht'), Js('hst'), Js('hsh'), Js('hn'), Js('hm'), Js('hl'), Js('hz'), Js('hx'), Js('hq'), Js('k'), Js('ks'), Js('kx'), Js('l'), Js('ll'), Js('lk'), Js('ln'), Js('lm'), Js('lz'), Js('lp'), Js('lt'), Js('ls'), Js('lst'), Js('lf'), Js('m'), Js('mn'), Js('mm'), Js('mt'), Js('ms'), Js('n'), Js('nn'), Js('nt'), Js('ns'), Js('p'), Js('ps'), Js('pt'), Js('ph'), Js('q'), Js('r'), Js('rs'), Js('rt'), Js('rst'), Js('rq'), Js('rk'), Js('rc'), Js('rf'), Js('rb'), Js('rd'), Js('s'), Js('st'), Js('ss'), Js('sh'), Js('sk'), Js('sp'), Js('t'), Js('th'), Js('ts'), Js('w'), Js('wth'), Js('x'), Js('z')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', ((var.get('names1').get(var.get('rnd'))+Js(' of '))+var.get('names2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('names', ((((var.get('names1').get(var.get('rnd'))+Js(' of '))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3')))+var.get('names7').get(var.get('rnd4'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('names', ((((((var.get('names1').get(var.get('rnd'))+Js(' of '))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3')))+var.get('names5').get(var.get('rnd4')))+var.get('names6').get(var.get('rnd5')))+var.get('names7').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
battleNames = var.to_python()