__all__ = ['mathosianNames']

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
    var.registers(['names1', 'names2', 'tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', Js([Js('Ad'), Js('Adel'), Js('Ag'), Js('Agn'), Js('Al'), Js('Am'), Js('Amal'), Js('And'), Js('Ang'), Js('Bar'), Js('Bern'), Js('Birg'), Js('Brun'), Js('Car'), Js('Cec'), Js('Cel'), Js('Christ'), Js('Char'), Js('Cor'), Js('Clar'), Js('Dan'), Js('Den'), Js('Dor'), Js('Ed'), Js('El'), Js('Elf'), Js('Elis'), Js('Els'), Js('Em'), Js('Emil'), Js('Er'), Js('Es'), Js('Est'), Js('Flor'), Js('Fel'), Js('Frid'), Js('Gabr'), Js('Gen'), Js('Gertr'), Js('Gret'), Js('Gund'), Js('Hann'), Js('Heid'), Js('Helg'), Js('Herm'), Js('Hild'), Js('Ing'), Js('Isab'), Js('Jan'), Js('Johann'), Js('Jul'), Js('Kar'), Js('Kat'), Js('Kath'), Js('Lar'), Js('Lill'), Js('Lin'), Js('Madel'), Js('Marg'), Js('Marl'), Js('Mel'), Js('Mon'), Js('Nat'), Js('Nic'), Js('Petr'), Js('Ren'), Js('Ros'), Js('Sabr'), Js('Saman'), Js('Ser'), Js('Seraph'), Js('Sof'), Js('Soph'), Js('Sus'), Js('Ther'), Js('Urs'), Js('Val'), Js('Valer'), Js('Ver'), Js('Veron'), Js('Yv')]))
        var.put('names2', Js([Js('a'), Js('adette'), Js('alena'), Js('alie'), Js('anda'), Js('andra'), Js('anie'), Js('anna'), Js('anze'), Js('ara'), Js('arete'), Js('arie'), Js('arina'), Js('ascha'), Js('atha'), Js('auke'), Js('ea'), Js('eanor'), Js('een'), Js('efine'), Js('egard'), Js('ekka'), Js('ele'), Js('eli'), Js('elin'), Js('eline'), Js('eliy'), Js('ella'), Js('elle'), Js('elore'), Js('ena'), Js('enie'), Js('esia'), Js('eth'), Js('ette'), Js('eva'), Js('ia'), Js('iane'), Js('ice'), Js('icia'), Js('ie'), Js('iela'), Js('ienne'), Js('ies'), Js('ika'), Js('ilde'), Js('ilia'), Js('ily'), Js('ina'), Js('ind'), Js('ine'), Js('ion'), Js('issa'), Js('istel'), Js('istin'), Js('itha'), Js('ivia'), Js('izia'), Js('olin'), Js('oline'), Js('onia'), Js('onora'), Js('ora'), Js('ore'), Js('othea'), Js('otte'), Js('ucie'), Js('udis'), Js('ula'), Js('urga'), Js('usta')]))
    else:
        var.put('names1', Js([Js('Aar'), Js('Ab'), Js('Abr'), Js('Ach'), Js('Ad'), Js('Adr'), Js('Alb'), Js('Ant'), Js('Aug'), Js('Bast'), Js('Ben'), Js('Bern'), Js('Clem'), Js('Den'), Js('Diet'), Js('Dom'), Js('Eb'), Js('Eber'), Js('Eck'), Js('Ed'), Js('Edm'), Js('Em'), Js('Emm'), Js('Er'), Js('Erh'), Js('Erw'), Js('Fab'), Js('Fer'), Js('Ferd'), Js('Gab'), Js('Ger'), Js('Gerw'), Js('Gun'), Js('Gunt'), Js('Har'), Js('Hil'), Js('Joh'), Js('Jos'), Js('Kar'), Js('Kas'), Js('Kon'), Js('Len'), Js('Mag'), Js('Man'), Js('Mar'), Js('Mark'), Js('Mik'), Js('Nic'), Js('Pat'), Js('Patr'), Js('Rein'), Js('Rob'), Js('Ron'), Js('Rud'), Js('Sam'), Js('Stef'), Js('Thom'), Js('Tob'), Js('Vict'), Js('Wal'), Js('Wolf')]))
        var.put('names2', Js([Js('ald'), Js('am'), Js('amin'), Js('an'), Js('and'), Js('ang'), Js('ank'), Js('ann'), Js('annes'), Js('antin'), Js('ar'), Js('ard'), Js('art'), Js('aus'), Js('echt'), Js('ed'), Js('egor'), Js('elar'), Js('emar'), Js('end'), Js('ens'), Js('ent'), Js('eph'), Js('erhard'), Js('ert'), Js('etan'), Js('ian'), Js('ias'), Js('ich'), Js('ick'), Js('ict'), Js('ied'), Js('iel'), Js('ilian'), Js('ill'), Js('ilus'), Js('in'), Js('inic'), Js('ix'), Js('oah'), Js('ob'), Js('of'), Js('olas'), Js('old'), Js('olf'), Js('oman'), Js('on'), Js('uard'), Js('uin'), Js('und'), Js('ur'), Js('ut')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', (var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2'))))
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
mathosianNames = var.to_python()