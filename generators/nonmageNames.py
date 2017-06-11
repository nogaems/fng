__all__ = ['nonmageNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('A-types'), Js('Aberrants'), Js('Abnormals'), Js('Abnormies'), Js('Abnorms'), Js('Abs'), Js('Anomalies'), Js('Arcanay'), Js('Arcanil'), Js('Arcanix'), Js('Arcano'), Js('Arcanoes'), Js('Atyps'), Js('Beyonders'), Js('Blanks'), Js('Bonas'), Js('Centrics'), Js('Chimeras'), Js('Commoners'), Js('Culiars'), Js('Deviants'), Js('Eccentrics'), Js('Eccents'), Js('Extraordinaries'), Js('Extraors'), Js('Feebles'), Js('Freaks'), Js('Free'), Js('Generics'), Js('Genrics'), Js('Gens'), Js('Hollows'), Js('Humdrums'), Js('Idles'), Js('Illegits'), Js('Imps'), Js('Impures'), Js('Inerts'), Js('Irregs'), Js('Irregulars'), Js('Lawfuls'), Js('Legis'), Js('Legits'), Js('Malfors'), Js('Medians'), Js('Meras'), Js('Millers'), Js('Miscreants'), Js('Monos'), Js('Mortals'), Js('Mundanes'), Js('Munds'), Js('Mutants'), Js('Mutes'), Js('Nabracadabras'), Js('Nabras'), Js('Naturals'), Js('Naygicians'), Js('Naymagi'), Js('Nerics'), Js('Nizards'), Js('Nocana'), Js('Noccult'), Js('Nocus'), Js('Nocus Pocus'), Js('Nogician'), Js('Nomages'), Js('Nomagi'), Js('Nomalies'), Js('Nonchanters'), Js('Nonvoyants'), Js('Norcana'), Js('Norcerers'), Js('Normies'), Js('Norms'), Js('Novoyants'), Js('Oddities'), Js('Ordies'), Js('Ordinaries'), Js('Originals'), Js('Orthos'), Js('Passives'), Js('Peculiars'), Js('Propers'), Js('Reggies'), Js('Regs'), Js('Regulars'), Js('Spiritless'), Js('Standards'), Js('Standies'), Js('Strangers'), Js('Traditionals'), Js('Typicals'), Js('Typics'), Js('Unnaturals'), Js('Usuals'), Js('Vacants'), Js('Voids'), Js("Voodon't"), Js('Weirdos'), Js('Zaros')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
nonmageNames = var.to_python()