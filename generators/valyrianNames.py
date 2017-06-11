__all__ = ['valyrianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('names', ((((var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2')))+Js(' '))+var.get('names5').get(var.get('rnd3')))+var.get('names6').get(var.get('rnd4'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+Js(' '))+var.get('names5').get(var.get('rnd3')))+var.get('names6').get(var.get('rnd4'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Ae'), Js('Aega'), Js('Aera'), Js('Aery'), Js('Bae'), Js('Baese'), Js('Balae'), Js('Dae'), Js('Daema'), Js('Daera'), Js('Gae'), Js('Gahae'), Js('Galae'), Js('Garae'), Js('Jacae'), Js('Jae'), Js('Jaehae'), Js('Jaere'), Js('Lae'), Js('Lucae'), Js('Ma'), Js('Mae'), Js('Maeha'), Js('Malae'), Js('Mata'), Js('Rae'), Js('Ragae'), Js('Rahae'), Js('Rhae'), Js('Tae'), Js('Taece'), Js('Tahae'), Js('Talae'), Js('Tyrae'), Js('Va'), Js('Vae'), Js('Vahae'), Js('Vi'), Js('Vise'), Js('Yrae')]))
var.put('names2', Js([Js('dar'), Js('dor'), Js('gar'), Js('garon'), Js('garys'), Js('gel'), Js('gon'), Js('gor'), Js('lar'), Js('larr'), Js('larys'), Js('lon'), Js('lor'), Js('lyx'), Js('mar'), Js('marr'), Js('marys'), Js('mion'), Js('mon'), Js('mond'), Js('mor'), Js('morys'), Js('myx'), Js('nar'), Js('narr'), Js('nor'), Js('nys'), Js('nyx'), Js('raenar'), Js('rion'), Js('ron'), Js('rys'), Js('var'), Js('von'), Js('vor')]))
var.put('names3', Js([Js('Aene'), Js('Aere'), Js('Alae'), Js('Aly'), Js('Bae'), Js('Bhae'), Js('Ba'), Js('Dae'), Js('Daene'), Js('Delae'), Js('Elae'), Js('Erae'), Js('Hae'), Js('Haele'), Js('He'), Js('Jae'), Js('Jaela'), Js('Jelae'), Js('Mae'), Js('Maele'), Js('Malae'), Js('Manae'), Js('Nae'), Js('Naela'), Js('Naere'), Js('Nelae'), Js('Nesae'), Js('Raene'), Js('Relae'), Js('Renae'), Js('Rhae'), Js('Rhaene'), Js('Sae'), Js('Saela'), Js('Saene'), Js('Saere'), Js('Selae'), Js('Vae'), Js('Vhae'), Js('Vyse')]))
var.put('names4', Js([Js('hna'), Js('hra'), Js('hrys'), Js('hnae'), Js('hra'), Js('la'), Js('lys'), Js('lla'), Js('lyra'), Js('mys'), Js('mala'), Js('mera'), Js('na'), Js('nla'), Js('nera'), Js('nna'), Js('nya'), Js('nyra'), Js('nys'), Js('ra'), Js('rla'), Js('rya'), Js('rys'), Js('ssa'), Js('sanne'), Js('sella'), Js('sa'), Js('sys')]))
var.put('names5', Js([Js('Aer'), Js('Ag'), Js('Ar'), Js('Bael'), Js('Bar'), Js('Ber'), Js('Caen'), Js('Cal'), Js('Cel'), Js('Daer'), Js('Dal'), Js('Dor'), Js('Gael'), Js('Gal'), Js('Gon'), Js('Laen'), Js('Laer'), Js('Len'), Js('Maen'), Js('Mal'), Js('Mel'), Js('Nael'), Js('Nar'), Js('Noh'), Js('Qar'), Js('Qoh'), Js('Rael'), Js('Raen'), Js('Rah'), Js('Taen'), Js('Tael'), Js('Tar'), Js('Vael'), Js('Val'), Js('Vel')]))
var.put('names6', Js([Js('aellis'), Js('aelor'), Js('aenor'), Js('aeris'), Js('aleos'), Js('anyon'), Js('areon'), Js('daerys'), Js('eneos'), Js('ennis'), Js('eris'), Js('gaeron'), Js('garis'), Js('gyreon'), Js('iar'), Js('inarys'), Js('itheos'), Js('laeris'), Js('laeron'), Js('larys'), Js('maereon'), Js('naeros'), Js('nalys'), Js('nareon'), Js('naris'), Js('raenos'), Js('ralis'), Js('reos'), Js('talor'), Js('talos'), Js('taris'), Js('theon'), Js('theos'), Js('tigar'), Js('yreos')]))
pass
pass


# Add lib to the module scope
valyrianNames = var.to_python()