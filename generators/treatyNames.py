__all__ = ['treatyNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('names', (Js('Treaty of ')+var.get('names1').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Abdication'), Js('Abuse'), Js('Amalgamation'), Js('Ambitions'), Js('Anarchy'), Js('Angels'), Js('Ashes'), Js('Assassinations'), Js('Autarchy'), Js('Autonomy'), Js('Awakening'), Js('Backdoors'), Js('Backstabs'), Js('Betrayal'), Js('Blackmail'), Js('Blessings'), Js('Bliss'), Js('Blood'), Js('Bloodshed'), Js('Blunders'), Js('Bowing'), Js('Broken Armies'), Js('Broken Souls'), Js('Brutalities'), Js('Burning Flags'), Js('Carnage'), Js('Certain Demise'), Js('Certain Doom'), Js('Charity'), Js('Clean Hands'), Js('Cleansing Rains'), Js('Coalitions'), Js('Comraes'), Js('Condemnation'), Js('Control'), Js('Corruption'), Js('Covert Affairs'), Js('Cowards'), Js('Crooks'), Js('Damnation'), Js('Darkness'), Js('Death'), Js('Deaths'), Js('Deceit'), Js('Deception'), Js('Defamation'), Js('Delusion'), Js('Demands'), Js('Democracy'), Js('Denial'), Js('Desire'), Js('Destruction'), Js('Devotion'), Js('Dilemmas'), Js('Disgrace'), Js('Disguises'), Js('Dishonor'), Js('Disloyalty'), Js('Disorder'), Js('Disruption'), Js('Disunion'), Js('Domination'), Js('Duality'), Js('Duplicity'), Js('Duty'), Js('Eradication'), Js('Essence'), Js('Evaded War'), Js('Executions'), Js('Exiles'), Js('Expansion'), Js('Extermination'), Js('Extortion'), Js('Faith'), Js('Favor'), Js('Flying Colors'), Js('Fortune'), Js('Fraud'), Js('Freedom'), Js('Fusions'), Js('Gluttony'), Js('Greed'), Js('Growth'), Js('Guilt'), Js('Harmony'), Js('Heart'), Js('Heaven'), Js('Hidden Goals'), Js('Hoaxes'), Js('Honesty'), Js('Honor'), Js('Hope'), Js('Humiliation'), Js('Humility'), Js('Hypocrisy'), Js('Ignorance'), Js('Illusions'), Js('Impostors'), Js('Independence'), Js('Individuality'), Js('Innocent Victims'), Js('Innocents'), Js('Integrity'), Js('Intelligence'), Js('Interruption'), Js('Justice'), Js('Kindness'), Js('Law'), Js('Legitimacy'), Js('Liberty'), Js('Lies'), Js('Life'), Js('Loyalty'), Js('Luxury'), Js('Magic'), Js('Malignance'), Js('Martial Law'), Js('Mergers'), Js('Miracles'), Js('Mistakes'), Js('Mysteries'), Js('Mystics'), Js('Necrosis'), Js('Neglect'), Js('New Hope'), Js('Nothing'), Js('Obedience'), Js('Obscurity'), Js('Oppression'), Js('Oversights'), Js('Passivism'), Js('Patriots'), Js('Perfection'), Js('Persecution'), Js('Pressure'), Js('Privacy'), Js('Promises'), Js('Promotions'), Js('Prosperity'), Js('Protection'), Js('Public Order'), Js('Public Unrest'), Js('Purity'), Js('Rebirth'), Js('Recovery'), Js('Reincarnation'), Js('Rejuvenation'), Js('Reparation'), Js('Resignation'), Js('Respect'), Js('Restoration'), Js('Resurgence'), Js('Revelations'), Js('Revival'), Js('Riches'), Js('Righteousness'), Js('Sanctification'), Js('Sanctions'), Js('Scams'), Js('Scarred Lands'), Js('Secrets'), Js('Security'), Js('Separation'), Js('Severance'), Js('Shams'), Js('Shrouded Lies'), Js('Shrouded Truths'), Js('Silence'), Js('Slander'), Js('Slavery'), Js('Slaves'), Js('Solutions'), Js('Sovereignty'), Js('Stagnation'), Js('Submission'), Js('Subterfuge'), Js('Support'), Js('Surrender'), Js('Survival'), Js('Terminality'), Js('The Bastard'), Js('The Brotherhood'), Js('The Burning City'), Js('The Curse'), Js('The Dictator'), Js('The False King'), Js('The Forest'), Js('The Forsaken'), Js('The Greater Good'), Js('The Grim Reaper'), Js('The Impasse'), Js('The Iron Hand'), Js('The Lands'), Js('The Light'), Js('The Massacre'), Js('The Meek'), Js('The Mountains'), Js('The Occult'), Js('The Oracle'), Js('The Pure'), Js('The Silver Angel'), Js('The Trojan Horse'), Js('The True King'), Js('Theft'), Js('Thieves'), Js('Torment'), Js('Torture'), Js('Traitors'), Js('Treachery'), Js('Triumph'), Js('Truth'), Js('Unanimity'), Js('Unification'), Js('Unions'), Js('Unison'), Js('Utopia'), Js('Vetos'), Js('Victims'), Js('Victory'), Js('Vigor'), Js('Virtues'), Js('Vitality'), Js('Wealth'), Js('Wellfare'), Js('Wonder')]))
pass
pass


# Add lib to the module scope
treatyNames = var.to_python()