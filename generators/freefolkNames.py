__all__ = ['freefolkNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names8', 'names2', 'names3', 'names1', 'names7'])
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
            if (var.get('i')<Js(5.0)):
                if PyJsStrictEq(var.get('tp'),Js(1.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('names', (var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                    var.put('names', (var.get('names5').get(var.get('rnd'))+var.get('names6').get(var.get('rnd2'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(1.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('names', (var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
                    var.put('names', (var.get('names7').get(var.get('rnd'))+var.get('names8').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('An'), Js('Ar'), Js('As'), Js('Ber'), Js('Bir'), Js('Dal'), Js('Dis'), Js('Dor'), Js('El'), Js('Fer'), Js('Fjor'), Js('Fren'), Js('Gil'), Js('Gren'), Js('Grin'), Js('Har'), Js('Her'), Js('Hil'), Js('Hol'), Js('Ig'), Js('Jen'), Js('Jor'), Js('Kar'), Js('Len'), Js('Mun'), Js('Myr'), Js('Nel'), Js('Row'), Js('Svan'), Js('Val'), Js('Vel'), Js('Vig'), Js('Yg'), Js('Yn'), Js('Yr')]))
var.put('names2', Js([Js('da'), Js('dis'), Js('ga'), Js('gin'), Js('la'), Js('lie'), Js('lif'), Js('lin'), Js('lina'), Js('lis'), Js('ly'), Js('ma'), Js('milla'), Js('na'), Js('ne'), Js('nel'), Js('ness'), Js('nora'), Js('ny'), Js('ra'), Js('rey'), Js('rima'), Js('rin'), Js('rine'), Js('rit'), Js('ritte'), Js('ry'), Js('sten'), Js('thine'), Js('trud'), Js('vil'), Js('vild'), Js('wen'), Js('wyn'), Js('ya')]))
var.put('names3', Js([Js('Ama'), Js('Ane'), Js('Arne'), Js('Bre'), Js('Bri'), Js('Cami'), Js('Da'), Js('Eli'), Js('Fa'), Js('Fra'), Js('Fre'), Js('Ge'), Js('Gei'), Js('Gja'), Js('Gra'), Js('Gre'), Js('Ha'), Js('Hi'), Js('Hre'), Js('Ine'), Js('Ingi'), Js('Ka'), Js('Kri'), Js('Ma'), Js('Mi'), Js('Ne'), Js('No'), Js('Oli'), Js('Sra'), Js('Sre'), Js('Stei'), Js('Sva'), Js('Tho'), Js('Ule'), Js('Vre')]))
var.put('names4', Js([Js('borg'), Js('dis'), Js('finna'), Js('hild'), Js('lda'), Js('ldis'), Js('lena'), Js('lene'), Js('lga'), Js('lla'), Js('lly'), Js('lsa'), Js('nda'), Js('nhild'), Js('nna'), Js('nya'), Js('ra'), Js('ren'), Js('rie'), Js('rine'), Js('rit'), Js('ritte'), Js('rma'), Js('rna'), Js('rny'), Js('rthe'), Js('sa'), Js('sha'), Js('stin'), Js('the'), Js('thera'), Js('vild'), Js('wa'), Js('ya'), Js('yah')]))
var.put('names5', Js([Js('Ar'), Js('Bal'), Js('Bar'), Js('Bior'), Js('Bjor'), Js('Bol'), Js('Bran'), Js('Dar'), Js('Dor'), Js('Dryn'), Js('Fjar'), Js('Geir'), Js('Gen'), Js('Gor'), Js('Gorn'), Js('Grun'), Js('Gun'), Js('Har'), Js('Hran'), Js('Is'), Js('Jar'), Js('Jor'), Js('Lok'), Js('Mar'), Js('Mor'), Js('Nar'), Js('Nor'), Js('Or'), Js('Orn'), Js('Rag'), Js('Rog'), Js('Styr'), Js('Sur'), Js('Thor'), Js('Tor'), Js('Val'), Js('Var'), Js('Varn'), Js('Vig'), Js('Vor')]))
var.put('names6', Js([Js('ald'), Js('alder'), Js('amun'), Js('amyr'), Js('and'), Js('arr'), Js('arun'), Js('dar'), Js('del'), Js('egg'), Js('eigr'), Js('ell'), Js('grim'), Js('igar'), Js('ik'), Js('kar'), Js('laf'), Js('leck'), Js('mir'), Js('modr'), Js('mund'), Js('myr'), Js('nor'), Js('odarr'), Js('odr'), Js('old'), Js('olf'), Js('oll'), Js('or'), Js('orn'), Js('rad'), Js('ran'), Js('rand'), Js('rik'), Js('ryn'), Js('ulas'), Js('und'), Js('vir'), Js('wynd'), Js('yger')]))
var.put('names7', Js([Js('Ara'), Js('Bae'), Js('Bia'), Js('Bja'), Js('Bora'), Js('Bra'), Js('Dara'), Js('Do'), Js('Dra'), Js('Dry'), Js('Go'), Js('Gra'), Js('Gre'), Js('Gro'), Js('Hara'), Js('Hro'), Js('Jara'), Js('Jora'), Js('Olmo'), Js('Ore'), Js('Orno'), Js('Rau'), Js('Ska'), Js('Sra'), Js('Stei'), Js('Sty'), Js('Sve'), Js('Tho'), Js('Tore'), Js('Vara')]))
var.put('names8', Js([Js('dill'), Js('dir'), Js('dol'), Js('gard'), Js('geir'), Js('gir'), Js('gni'), Js('gr'), Js('grim'), Js('gvar'), Js('kmar'), Js('kul'), Js('laf'), Js('lner'), Js('mir'), Js('mun'), Js('mund'), Js('myr'), Js('narr'), Js('nir'), Js('rald'), Js('rand'), Js('regg'), Js('rigg'), Js('rik'), Js('rne'), Js('rnir'), Js('rolf'), Js('rrand'), Js('val')]))
pass
pass


# Add lib to the module scope
freefolkNames = var.to_python()