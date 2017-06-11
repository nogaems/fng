__all__ = ['politicalPartyNames']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Advanced'), Js('Collective'), Js('Common'), Js('Constitutional'), Js('Contemporary'), Js('Eastern'), Js('Extremist'), Js('Fanatical'), Js('Federal'), Js('First'), Js('Free'), Js('Global'), Js('Independent'), Js('Industrial'), Js('International'), Js('Lawful'), Js('Leading'), Js('Liberal'), Js('Moderate'), Js('Modern'), Js('National'), Js('Neo'), Js('New'), Js('Northern'), Js('Organized'), Js('Patriotic'), Js('Peaceful'), Js("People's"), Js('Permanent'), Js('Prime'), Js('Progressive'), Js('Radical'), Js('Rational'), Js('Revolutionary'), Js('Social'), Js('Southern'), Js('Sovereign'), Js('Traditional'), Js('Unconditional'), Js('Undivided'), Js('Unified'), Js('United'), Js('Universal'), Js('Vocal'), Js('Western'), Js('World'), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('Abolition'), Js('Action'), Js('Administration'), Js('Advancement'), Js('Affinity'), Js('Agrarian'), Js('Alliance'), Js('Amendment'), Js('Animal'), Js('Appreciation'), Js('Autocrat'), Js('Choice'), Js('Citizens'), Js('Civic'), Js('Civil Rights'), Js('Coalition'), Js('Communion'), Js('Communist'), Js('Community'), Js('Compromise'), Js('Conservative'), Js('Constitution'), Js('Defiance'), Js('Democratic'), Js('Denizen'), Js('Diligence'), Js('Earth'), Js('Egalitarian'), Js('Egalitarianism'), Js('Egalitarion'), Js('Emancipation'), Js('Enterprise'), Js('Equality'), Js('Equilibrium'), Js('Evaluation'), Js('Evolution'), Js('Family'), Js('Fascist'), Js('Fatherland'), Js('Federation'), Js('Formation'), Js('Freedom'), Js('Future'), Js('Green'), Js('Homeland'), Js('Honesty'), Js('Household'), Js('Humanitarian'), Js('Identity'), Js('Immunity'), Js('Impartiality'), Js('Independence'), Js('Industry'), Js('Integrity'), Js('Isolation'), Js('Justice'), Js('Labor'), Js('Law'), Js('Left'), Js('Left Wing'), Js('Legislation'), Js('Liberation'), Js('Libertarian'), Js('Liberty'), Js('Life'), Js('Loyalist'), Js('Monarchist'), Js('Motherland'), Js('Nation'), Js('Nationalist'), Js('Nature'), Js('Operation'), Js('Opportunity'), Js('Pacifism'), Js('Pacifist'), Js('Parliamentary'), Js('Patriot'), Js('Peace'), Js('People'), Js('Preservation'), Js('Privilege'), Js('Probation'), Js('Progress'), Js('Progression'), Js('Prohibition'), Js('Proposition'), Js('Prosperity'), Js('Protection'), Js('Reconciliation'), Js('Red'), Js('Reformation'), Js('Regulation'), Js('Rehabilitation'), Js('Renovation'), Js('Republican'), Js('Resistance'), Js('Respect'), Js('Right'), Js('Right Wing'), Js('Science'), Js('Segregation'), Js('Separation'), Js('Separatist'), Js('Socialist'), Js('Solidarity'), Js('State'), Js('Taxpayer'), Js('Theocratic'), Js('Transformation'), Js('Trust'), Js('Uniformity'), Js('Unionist'), Js('Unity'), Js('Voice'), Js('Voter'), Js('Welfare'), Js('Workers'), Js('Working Class')]))
var.put('nm3', Js([Js('Party'), Js('League'), Js('Movement'), Js('Group'), Js('Union'), Js('Coalition'), Js('Party'), Js('Party')]))
pass
pass


# Add lib to the module scope
politicalPartyNames = var.to_python()