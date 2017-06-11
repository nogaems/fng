__all__ = ['dndDevaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nameFem', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nameMas', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameFem_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
    while (PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm6').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm8').get(var.get('rnd3')),var.get('nm11').get(var.get('rnd5')))):
        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
    if (var.get('i')<Js(6.0)):
        var.put('nMs', ((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm11').get(var.get('rnd5'))))
    else:
        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
        while (PyJsStrictEq(var.get('nm10').get(var.get('rnd6')),var.get('nm11').get(var.get('rnd5'))) or PyJsStrictEq(var.get('nm10').get(var.get('rnd6')),var.get('nm8').get(var.get('rnd3')))):
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
        var.put('nMs', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm9').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd6')))+var.get('nm9').get(var.get('rnd7')))+var.get('nm11').get(var.get('rnd5'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameFem_.func_name = 'nameFem'
var.put('nameFem', PyJsHoisted_nameFem_)
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
    while (PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))) or PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm5').get(var.get('rnd5')))):
        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
    var.put('nMs', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm4').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameMas_.func_name = 'nameMas'
var.put('nameMas', PyJsHoisted_nameMas_)
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.get('nameFem')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameFem')()
            else:
                var.get('nameMas')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameMas')()
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ad'), Js('Ans'), Js('Ars'), Js('Ay'), Js('Bav'), Js('Ber'), Js('Dar'), Js('Eb'), Js('Ely'), Js('Er'), Js('Ery'), Js('Gal'), Js('Gam'), Js('Gar'), Js('Hiy'), Js('Iann'), Js('Ker'), Js('Mah'), Js('Mahr'), Js('Man'), Js('Mar'), Js('Math'), Js('Mor'), Js('Nat'), Js('Neh'), Js('Ner'), Js('Ob'), Js('Or'), Js('Rah'), Js('Ron'), Js('Sam'), Js('Sav'), Js('Ser'), Js('Sor'), Js('Tar'), Js('Tav'), Js('Vat'), Js('Ver'), Js('Zach'), Js('Zay')]))
var.put('nm2', Js([Js('ab'), Js('ach'), Js('ad'), Js('ahk'), Js('ahm'), Js('ahn'), Js('ahr'), Js('ak'), Js('al'), Js('am'), Js('an'), Js('ar'), Js('as'), Js('ath'), Js('eb'), Js('ech'), Js('ed'), Js('ehr'), Js('ek'), Js('el'), Js('em'), Js('en'), Js('er'), Js('es'), Js('iah'), Js('ihm'), Js('ihn'), Js('im'), Js('in'), Js('ir'), Js('is')]))
var.put('nm3', Js([Js('Ab'), Js('Ad'), Js('An'), Js('Ar'), Js('Ash'), Js('Chan'), Js('Dan'), Js('Dar'), Js('Dav'), Js('Din'), Js('Elk'), Js('Eran'), Js('Eys'), Js('Han'), Js('Hav'), Js('Hen'), Js('Idr'), Js('Is'), Js('Jan'), Js('Jen'), Js('Kal'), Js('Kan'), Js('Kay'), Js('Len'), Js('Lih'), Js('Mah'), Js('Mar'), Js('Nal'), Js('Nav'), Js('Nom'), Js('Paz'), Js('Rav'), Js('Ren'), Js('Riy'), Js('Sad'), Js('Shar'), Js('Sir'), Js('Tar'), Js('Tel'), Js('Tir')]))
var.put('nm4', Js([Js('a'), Js('ael'), Js('aen'), Js('ah'), Js('ahne'), Js('ana'), Js('anaeh'), Js('anael'), Js('anah'), Js('ane'), Js('anel'), Js('aniah'), Js('ara'), Js('araeh'), Js('are'), Js('ariah'), Js('ea'), Js('ehl'), Js('ek'), Js('el'), Js('ele'), Js('elle'), Js('era'), Js('ey'), Js('eya'), Js('i'), Js('ia'), Js('iah'), Js('im'), Js('ima')]))
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('h'), Js('k'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('ia'), Js('ie'), Js('ea'), Js('ei')]))
var.put('nm3', Js([Js('b'), Js('ch'), Js('d'), Js('h'), Js('hr'), Js('l'), Js('ly'), Js('m'), Js('n'), Js('nn'), Js('ns'), Js('r'), Js('rs'), Js('ry'), Js('t'), Js('th'), Js('v'), Js('y')]))
var.put('nm4', Js([Js('a'), Js('e'), Js('i')]))
var.put('nm5', Js([Js('b'), Js('ch'), Js('d'), Js('h'), Js('hk'), Js('hm'), Js('hn'), Js('hr'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('th')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('ch'), Js('d'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('sh'), Js('t'), Js('th')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i')]))
var.put('nm8', Js([Js('b'), Js('d'), Js('dr'), Js('h'), Js('l'), Js('lk'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('v'), Js('y'), Js('ys'), Js('z')]))
var.put('nm9', Js([Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('ia'), Js('ae'), Js('ea')]))
var.put('nm10', Js([Js('hn'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('r'), Js('y')]))
var.put('nm11', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('h'), Js('hl'), Js('k'), Js('l'), Js('l'), Js('n'), Js('n'), Js('m'), Js('m')]))
pass
pass
pass
pass


# Add lib to the module scope
dndDevaNames = var.to_python()