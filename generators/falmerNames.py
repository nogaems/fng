__all__ = ['falmerNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names3'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['names1', 'names2', 'tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', Js([Js('Ari'), Js('Aith'), Js('Bel'), Js('Bire'), Js('Cele'), Js('Cen'), Js('El'), Js('Elle'), Js('En'), Js('Fae'), Js('Fai'), Js('Gis'), Js('Gwen'), Js('Haer'), Js('Hele'), Js('Inhe'), Js('Ime'), Js('Je'), Js('Jes'), Js('Kir'), Js('Kine'), Js('Les'), Js('Lyn'), Js('Mel'), Js('Min'), Js('Nira'), Js('Nythe'), Js('Pes'), Js('Prys'), Js('Rine'), Js('Ryn'), Js('Shi'), Js('Sina'), Js('Tera'), Js('Ter'), Js('Unhel'), Js('Uve'), Js('Ven'), Js('Vyr'), Js('Wae'), Js('Wina'), Js('Ynhe'), Js('Ys'), Js('Zhar'), Js('Zida')]))
        var.put('names2', Js([Js('bora'), Js('bysh'), Js('dhora'), Js('denyse'), Js('fani'), Js('feah'), Js('geth'), Js('greah'), Js('her'), Js('hish'), Js('kharise'), Js('kyre'), Js('lenor'), Js('lori'), Js('mhes'), Js('meril'), Js('neris'), Js('nyish'), Js('pireth'), Js('path'), Js('rae'), Js('rish'), Js('reno'), Js('ren'), Js('shan'), Js('selin'), Js('thune'), Js('tys'), Js('vhis'), Js('vena'), Js('wihn'), Js('wen'), Js('yane'), Js('yis'), Js('zhina'), Js('zis')]))
    else:
        var.put('names1', Js([Js('Are'), Js('Ath'), Js('Bal'), Js('Bir'), Js('Cele'), Js('Cen'), Js('Ed'), Js('Edhel'), Js('En'), Js('Fa'), Js('Fai'), Js('Gir'), Js('Glen'), Js('Har'), Js('Here'), Js('Idhe'), Js('Ire'), Js('Ja'), Js('Jed'), Js('Kar'), Js('Kida'), Js('Lat'), Js('Lyr'), Js('Men'), Js('Mir'), Js('Niri'), Js('Nyr'), Js('Pare'), Js('Pryn'), Js('Red'), Js('Ryn'), Js('Si'), Js('Sida'), Js('Tere'), Js('Tor'), Js('Udhel'), Js('Ure'), Js('Var'), Js('Vyr'), Js('Wai'), Js('Wiri'), Js('Ydhe'), Js('Yr'), Js('Zar'), Js('Zida')]))
        var.put('names2', Js([Js('bor'), Js('bys'), Js('dhor'), Js('danyis'), Js('faris'), Js('fiath'), Js('groth'), Js('griath'), Js('hur'), Js('his'), Js('karis'), Js('kir'), Js('lebor'), Js('lor'), Js('mhor'), Js('mitil'), Js('naris'), Js('nyis'), Js('prith'), Js('piroth'), Js('re'), Js('riath'), Js('rilor'), Js('ring'), Js('sur'), Js('sebir'), Js('thur'), Js('til'), Js('vhur'), Js('vus'), Js('with'), Js('we'), Js('yaris'), Js('yor'), Js('zhor'), Js('zius')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
            var.put('names', ((((var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1')))+Js(' '))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names3', Js([Js('An'), Js('Ag'), Js('Agar'), Js('Bin'), Js('Berel'), Js('Cryn'), Js('Caer'), Js('Den'), Js('Dane'), Js('Ere'), Js('Eme'), Js('Fin'), Js('For'), Js('Gran'), Js('Gan'), Js('Hene'), Js('Har'), Js('Irel'), Js('Ise'), Js('Kran'), Js('Kor'), Js('Lene'), Js('Lore'), Js('Mas'), Js('Mine'), Js('Nor'), Js('Nara'), Js('Or'), Js('Ore'), Js('Pan'), Js('Pris'), Js('Ran'), Js('Rone'), Js('Shan'), Js('Sin'), Js('Tor'), Js('Tin'), Js('Ure'), Js('Unar'), Js('Vran'), Js('Vor'), Js('Wan'), Js('Was'), Js('Yre'), Js('Yren'), Js('Zon'), Js('Zar')]))
var.put('names4', Js([Js('bath'), Js('borin'), Js('dwen'), Js('dras'), Js('faroth'), Js('ferys'), Js('garwen'), Js('goth'), Js('horith'), Js('han'), Js('krath'), Js('kelor'), Js('len'), Js('loth'), Js('meloth'), Js('myn'), Js('naris'), Js('noth'), Js('paris'), Js('parwen'), Js('rawyn'), Js('renoth'), Js('saroth'), Js('saris'), Js('taroth'), Js('tan'), Js('vryn'), Js('varys'), Js('wenoth'), Js('wen'), Js('yloth'), Js('yrwen'), Js('zras'), Js('zoth')]))
pass
pass


# Add lib to the module scope
falmerNames = var.to_python()