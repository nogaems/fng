__all__ = ['haloSanShyuumNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                if (var.get('rnd')<Js(7.0)):
                    while (var.get('rnd3')<Js(7.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                if (var.get('rnd')>Js(6.0)):
                    while (var.get('rnd3')<Js(6.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm4').get(var.get('rnd4')))+var.get('nm2').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd6')))+var.get('nm6').get(var.get('rnd7'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('names', ((var.get('nm7').get(var.get('rnd'))+Js(' of '))+var.get('nm8').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('o'), Js('a'), Js('u')]))
var.put('nm3', Js([Js('b'), Js('c'), Js('d'), Js('g'), Js('k'), Js('p'), Js('t'), Js('rd'), Js('rb'), Js('rc'), Js('rd'), Js('rg'), Js('rk'), Js('rp'), Js('rt')]))
var.put('nm4', Js([Js('b'), Js('br'), Js('c'), Js('cr'), Js('d'), Js('dr'), Js('f'), Js('fr'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('pr'), Js('r'), Js('s'), Js('sr'), Js('t'), Js('tr'), Js('v'), Js('vr'), Js('w'), Js('z'), Js('mr'), Js('kr')]))
var.put('nm5', Js([Js('b'), Js('bt'), Js('c'), Js('ct'), Js('d'), Js('f'), Js('ft'), Js('h'), Js('k'), Js('kt'), Js('l'), Js('m'), Js('mnt'), Js('mt'), Js('n'), Js('nb'), Js('nc'), Js('nct'), Js('nd'), Js('nf'), Js('nft'), Js('nst'), Js('nt'), Js('p'), Js('pt'), Js('r'), Js('rc'), Js('rnt'), Js('rt'), Js('s'), Js('sc'), Js('st'), Js('t'), Js('w'), Js('wt'), Js('z'), Js('zc'), Js('zt')]))
var.put('nm6', Js([Js('o'), Js('a'), Js('u'), Js(''), Js('')]))
var.put('nm7', Js([Js('Prophet'), Js('Minister'), Js('High Prophet')]))
var.put('nm8', Js([Js('Absolution'), Js('Analysis'), Js('Atonement'), Js('Attrition'), Js('Audacity'), Js('Aversion'), Js('Boldness'), Js('Bravery'), Js('Candor'), Js('Caution'), Js('Censure'), Js('Charity'), Js('Civility'), Js('Clemency'), Js('Commitment'), Js('Compassion'), Js('Confidence'), Js('Conscience'), Js('Conservancy'), Js('Constraint'), Js('Contrition'), Js('Control'), Js('Conviction'), Js('Courage'), Js('Courtesy'), Js('Creed'), Js('Decency'), Js('Defiance'), Js('Dignity'), Js('Disdain'), Js('Doubt'), Js('Duty'), Js('Elegance'), Js('Empathy'), Js('Endurance'), Js('Esteem'), Js('Etiology'), Js('Fairness'), Js('Favor'), Js('Fervor'), Js('Forbearance'), Js('Fortitude'), Js('Gallantry'), Js('Generosity'), Js('Goodwill'), Js('Grace'), Js('Honesty'), Js('Honor'), Js('Inhibition'), Js('Inquisition'), Js('Insolence'), Js('Integrity'), Js('Interrogation'), Js('Intrepidity'), Js('Investigation'), Js('Kindness'), Js('Legitimacy'), Js('Lenience'), Js('Mercy'), Js('Moderation'), Js('Nobility'), Js('Objection'), Js('Obligation'), Js('Patience'), Js('Penance'), Js('Penitence'), Js('Pity'), Js('Principles'), Js('Protection'), Js('Protest'), Js('Prowess'), Js('Qualm'), Js('Recognition'), Js('Regret'), Js('Reliance'), Js('Remorse'), Js('Repentance'), Js('Resilience'), Js('Resistance'), Js('Restraint'), Js('Restriction'), Js('Reverence'), Js('Salvation'), Js('Saving'), Js('Silence'), Js('Sincerity'), Js('Sorrow'), Js('Stewardship'), Js('Strength'), Js('Suffering'), Js('Supposition'), Js('Sympathy'), Js('Tenacity'), Js('Tolerance'), Js('Trust'), Js('Truth'), Js('Valiance'), Js('Veracity'), Js('Vigor'), Js('Virtue')]))
pass
pass


# Add lib to the module scope
haloSanShyuumNames = var.to_python()