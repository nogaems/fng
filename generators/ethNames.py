__all__ = ['ethNames']

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
        var.put('names1', Js([Js('Aah'), Js('Ah'), Js('Amen'), Js('Amun'), Js('Ankh'), Js('Bek'), Js('Bith'), Js('Ebon'), Js('Hal'), Js('Hab'), Js('Hem'), Js('Hon'), Js('Is'), Js('Kam'), Js('Kar'), Js('Kan'), Js('Khep'), Js('Khuns'), Js('Mak'), Js('Mad'), Js('Manet'), Js('Meh'), Js('Mer'), Js('Mukan'), Js('Mum'), Js('Naham'), Js('Nan'), Js('Nef'), Js('Nen'), Js('Nes'), Js('Nofr'), Js('Nub'), Js('Olab'), Js('Pen'), Js('Ran'), Js('Raz'), Js('Sam'), Js('San'), Js('Sen'), Js('Shen'), Js('Shan'), Js('Tam'), Js('Ten'), Js('Tet'), Js('Therm')]))
        var.put('names2', Js([Js('agara'), Js('anath'), Js('ankhnas'), Js('arama'), Js('arta'), Js('astis'), Js('atra'), Js('ekhu'), Js('ela'), Js('emi'), Js('enen'), Js('enet'), Js('ense'), Js('epet'), Js('erit'), Js('es'), Js('ese'), Js('iah'), Js('ibah'), Js('ibeu'), Js('ika'), Js('ila'), Js('ilah'), Js('ima'), Js('ina'), Js('inah'), Js('inoe'), Js('ira'), Js('irye'), Js('isi'), Js('isis'), Js('itis'), Js('iya'), Js('iza'), Js('onee'), Js('orisis'), Js('otep'), Js('ukura'), Js('unta'), Js('ura'), Js('utaraa'), Js('utis')]))
    else:
        var.put('names1', Js([Js('Aah'), Js('Aakh'), Js('Abaal'), Js('Abay'), Js('Abdil'), Js('Abdam'), Js('Abub'), Js('Abus'), Js('Abuskh'), Js('Achen'), Js('Acher'), Js('Amen'), Js('Ankh'), Js('Apron'), Js('Baken'), Js('Bakar'), Js('Chat'), Js('Dar'), Js('Fen'), Js('Fun'), Js('Hak'), Js('Ham'), Js('Han'), Js('Har'), Js('Hek'), Js('Hor'), Js('Im'), Js('Jab'), Js('Jaf'), Js('Kam'), Js('Kak'), Js('Kef'), Js('Khab'), Js('Khaf'), Js('Khons'), Js('Man'), Js('Makal'), Js('Mem'), Js('Menk'), Js('Ment'), Js('Nar'), Js('Neb'), Js('Nekht'), Js('Osir'), Js('Osor'), Js('Pad'), Js('Phan'), Js('Phrah'), Js('Psam'), Js('Sem'), Js('Seph'), Js('Ser'), Js('Sok'), Js('Smen'), Js('Tab'), Js('Tah'), Js('Tat'), Js('Thoth'), Js('Thutm'), Js('Tosor')]))
        var.put('names2', Js([Js('aesis'), Js('ahersef'), Js('aka'), Js('akar'), Js('akaruti'), Js('aken'), Js('akhsas'), Js('amelek'), Js('amen'), Js('aphos'), Js('aphres'), Js('aphris'), Js('apis'), Js('asenb'), Js('astes'), Js('auhor'), Js('ehemto'), Js('ekhet'), Js('ekhtou'), Js('emheb'), Js('emhebi'), Js('emhet'), Js('emhotep'), Js('enaten'), Js('ennifi'), Js('entu'), Js('ephers'), Js('epthah'), Js('epthes'), Js('eramen'), Js('erermes'), Js('eres'), Js('eri'), Js('erres'), Js('ertum'), Js('eru'), Js('erumes'), Js('esseker'), Js('ihiti'), Js('iris'), Js('is'), Js('isaba'), Js('otep'), Js('oteph'), Js('oubis'), Js('ouris'), Js('ubis'), Js('umah'), Js('urmes')]))
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
ethNames = var.to_python()