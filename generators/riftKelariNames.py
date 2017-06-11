__all__ = ['riftKelariNames']

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
        var.put('names1', Js([Js('Ac'), Js('Ad'), Js('Adem'), Js('Adon'), Js('Adr'), Js('Ag'), Js('Agl'), Js('Ail'), Js('Air'), Js('Al'), Js('Alet'), Js('Alex'), Js('Alys'), Js('Am'), Js('An'), Js('Anas'), Js('And'), Js('Ang'), Js('Aph'), Js('Aphr'), Js('Apol'), Js('Ar'), Js('Aret'), Js('Art'), Js('As'), Js('Asp'), Js('Ath'), Js('Bar'), Js('Cal'), Js('Call'), Js('Cas'), Js('Casc'), Js('Cath'), Js('Cel'), Js('Char'), Js('Cher'), Js('Cos'), Js('Cres'), Js('Cyr'), Js('Daphn'), Js('Del'), Js('Delph'), Js('Dem'), Js('Den'), Js('Dian'), Js('Dion'), Js('Dor'), Js('Dorin'), Js('Dun'), Js('Eil'), Js('Elean'), Js('Elen'), Js('Elin'), Js('Eud'), Js('Euph'), Js('Evan'), Js('Evang'), Js('Gel'), Js('Hel'), Js('Hyac'), Js('Hyp'), Js('Ir'), Js('Is'), Js('Isad'), Js('Kal'), Js('Kol'), Js('Lar'), Js('Lyd'), Js('Mar'), Js('Mel'), Js('Nel'), Js('Ner'), Js('Nes'), Js('Nor'), Js('Ol'), Js('Olym'), Js('Oph'), Js('Pan'), Js('Pand'), Js('Phed'), Js('Phil'), Js('Ren'), Js('San'), Js('Sel'), Js('Stel'), Js('Tar'), Js('Ter'), Js('Thel'), Js('Xand'), Js('Xen'), Js('Zan'), Js('Zer')]))
        var.put('names2', Js([Js('acia'), Js('adia'), Js('agia'), Js('aina'), Js('ala'), Js('alia'), Js('anda'), Js('andia'), Js('andra'), Js('ania'), Js('antha'), Js('ara'), Js('arria'), Js('asia'), Js('atha'), Js('atia'), Js('eanor'), Js('ectra'), Js('eda'), Js('eia'), Js('ela'), Js('elia'), Js('elina'), Js('emia'), Js('emona'), Js('emone'), Js('ena'), Js('enia'), Js('ephone'), Js('erine'), Js('erise'), Js('esa'), Js('eta'), Js('etha'), Js('ethea'), Js('etina'), Js('etria'), Js('exis'), Js('ia'), Js('ice'), Js('ida'), Js('ienne'), Js('illa'), Js('ina'), Js('ine'), Js('inthe'), Js('ira'), Js('isia'), Js('isma'), Js('issa'), Js('ite'), Js('itha'), Js('iza'), Js('ocia'), Js('odite'), Js('odora'), Js('omeda'), Js('omena'), Js('ona'), Js('one'), Js('onia'), Js('onne'), Js('ora'), Js('osine'), Js('othea'), Js('othy'), Js('yllis'), Js('yne'), Js('ysa')]))
    else:
        var.put('names1', Js([Js('Ab'), Js('Abd'), Js('Abs'), Js('Absyr'), Js('Ac'), Js('Acas'), Js('Ach'), Js('Achat'), Js('Achel'), Js('Achil'), Js('Achl'), Js('Acr'), Js('Act'), Js('Ad'), Js('Adber'), Js('Adel'), Js('Adelp'), Js('Adm'), Js('Adr'), Js('Adras'), Js('Aeac'), Js('Aeg'), Js('Aegis'), Js('Aegyp'), Js('Aen'), Js('Aeol'), Js('Aes'), Js('Aescul'), Js('Aet'), Js('Ag'), Js('Agam'), Js('Agat'), Js('Ain'), Js('Aj'), Js('Ak'), Js('Al'), Js('Alcan'), Js('Alcin'), Js('Ales'), Js('Alex'), Js('Alp'), Js('Am'), Js('And'), Js('Andr'), Js('Ant'), Js('Antil'), Js('Apo'), Js('Apol'), Js('Arc'), Js('Arg'), Js('Aris'), Js('At'), Js('Bal'), Js('Bas'), Js('Baz'), Js('Bem'), Js('Bor'), Js('But'), Js('Cadm'), Js('Cap'), Js('Cas'), Js('Cast'), Js('Cel'), Js('Cep'), Js('Cerb'), Js('Cir'), Js('Col'), Js('Cor'), Js('Corid'), Js('Cro'), Js('Dam'), Js('Damar'), Js('Damas'), Js('Dar'), Js('Darr'), Js('Dem'), Js('Demet'), Js('Demod'), Js('Demor'), Js('Diom'), Js('Dion'), Js('Dn'), Js('Dor'), Js('Dun'), Js('Erasm'), Js('Erys'), Js('Eur'), Js('Gan'), Js('Gor'), Js('Greg'), Js('Grig'), Js('Hec'), Js('Hect'), Js('Hel'), Js('Her'), Js('Herc'), Js('Herm'), Js('Hes'), Js('Hom'), Js('Homer'), Js('Icar'), Js('Jul'), Js('Kor'), Js('Krat'), Js('Krik'), Js('Kyr'), Js('Lean'), Js('Leon'), Js('Lys'), Js('Maur'), Js('Morp'), Js('Nar'), Js('Nect'), Js('Nem'), Js('Ob'), Js('Obel'), Js('Or'), Js('Orp'), Js('Pal'), Js('Pat'), Js('Pen'), Js('Per'), Js('Phant'), Js('Plat'), Js('Pos'), Js('Proct'), Js('Ras'), Js('Rhod'), Js('Socr'), Js('Spyr'), Js('Stam'), Js('Tak'), Js('Thad'), Js('Ther'), Js('Trit'), Js('Vas'), Js('Xer'), Js('Zen')]))
        var.put('names2', Js([Js('acus'), Js('aemon'), Js('aeon'), Js('aethon'), Js('aeus'), Js('annos'), Js('antes'), Js('apius'), Js('areus'), Js('arios'), Js('arius'), Js('arus'), Js('asius'), Js('astos'), Js('ates'), Js('atius'), Js('aus'), Js('avros'), Js('eas'), Js('elous'), Js('emas'), Js('emus'), Js('enios'), Js('eon'), Js('eos'), Js('epios'), Js('erios'), Js('eron'), Js('eros'), Js('erus'), Js('es'), Js('etheus'), Js('etrios'), Js('etrius'), Js('etus'), Js('eus'), Js('hates'), Js('heus'), Js('hile'), Js('hos'), Js('ian'), Js('icus'), Js('idas'), Js('illes'), Js('illos'), Js('ion'), Js('is'), Js('isius'), Js('iss'), Js('issus'), Js('isthus'), Js('isto'), Js('ites'), Js('iton'), Js('ius'), Js('obus'), Js('ocles'), Js('olemus'), Js('olos'), Js('olus'), Js('onis'), Js('orgon'), Js('orior'), Js('orus'), Js('os'), Js('osios'), Js('othius'), Js('ous'), Js('ycus'), Js('ymion'), Js('yros'), Js('ysius'), Js('ystheus'), Js('ysus'), Js('ytus')]))
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
riftKelariNames = var.to_python()