__all__ = ['dndHalflingNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameFem', 'nm4', 'nameGen', 'nm3', 'nameMas', 'nm2'])
@Js
def PyJsHoisted_nameFem_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
    var.put('nMs', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
PyJsHoisted_nameFem_.func_name = 'nameFem'
var.put('nameFem', PyJsHoisted_nameFem_)
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
    var.put('nMs', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
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
var.put('nm1', Js([Js('An'), Js('Ar'), Js('Bar'), Js('Bel'), Js('Con'), Js('Cor'), Js('Dan'), Js('Dav'), Js('El'), Js('Er'), Js('Fal'), Js('Fin'), Js('Flyn'), Js('Gar'), Js('Go'), Js('Hal'), Js('Hor'), Js('Ido'), Js('Ira'), Js('Jan'), Js('Jo'), Js('Kas'), Js('Kor'), Js('La'), Js('Lin'), Js('Mar'), Js('Mer'), Js('Ne'), Js('Nor'), Js('Ori'), Js('Os'), Js('Pan'), Js('Per'), Js('Pim'), Js('Quin'), Js('Quo'), Js('Ri'), Js('Ric'), Js('San'), Js('Shar'), Js('Tar'), Js('Te'), Js('Ul'), Js('Uri'), Js('Val'), Js('Vin'), Js('Wen'), Js('Wil'), Js('Xan'), Js('Xo'), Js('Yar'), Js('Yen'), Js('Zal'), Js('Zen')]))
var.put('nm2', Js([Js('ace'), Js('amin'), Js('bin'), Js('bul'), Js('dak'), Js('dal'), Js('der'), Js('don'), Js('emin'), Js('eon'), Js('fer'), Js('fire'), Js('gin'), Js('hace'), Js('horn'), Js('kas'), Js('kin'), Js('lan'), Js('los'), Js('min'), Js('mo'), Js('nad'), Js('nan'), Js('ner'), Js('orin'), Js('os'), Js('pher'), Js('pos'), Js('ras'), Js('ret'), Js('ric'), Js('rich'), Js('rin'), Js('ry'), Js('ser'), Js('sire'), Js('ster'), Js('ton'), Js('tran'), Js('umo'), Js('ver'), Js('vias'), Js('von'), Js('wan'), Js('wrick'), Js('yas'), Js('yver'), Js('zin'), Js('zor'), Js('zu')]))
var.put('nm3', Js([Js('An'), Js('Ari'), Js('Bel'), Js('Bre'), Js('Cal'), Js('Chen'), Js('Dar'), Js('Dia'), Js('Ei'), Js('Eo'), Js('Eli'), Js('Era'), Js('Fay'), Js('Fen'), Js('Fro'), Js('Gel'), Js('Gra'), Js('Ha'), Js('Hil'), Js('Ida'), Js('Isa'), Js('Jay'), Js('Jil'), Js('Kel'), Js('Kith'), Js('Le'), Js('Lid'), Js('Mae'), Js('Mal'), Js('Mar'), Js('Ne'), Js('Ned'), Js('Odi'), Js('Ora'), Js('Pae'), Js('Pru'), Js('Qi'), Js('Qu'), Js('Ri'), Js('Ros'), Js('Sa'), Js('Shae'), Js('Syl'), Js('Tham'), Js('Ther'), Js('Tryn'), Js('Una'), Js('Uvi'), Js('Va'), Js('Ver'), Js('Wel'), Js('Wi'), Js('Xan'), Js('Xi'), Js('Yes'), Js('Yo'), Js('Zef'), Js('Zen')]))
var.put('nm4', Js([Js('alyn'), Js('ara'), Js('brix'), Js('byn'), Js('caryn'), Js('cey'), Js('da'), Js('dove'), Js('drey'), Js('elle'), Js('eni'), Js('fice'), Js('fira'), Js('grace'), Js('gwen'), Js('haly'), Js('jen'), Js('kath'), Js('kis'), Js('leigh'), Js('la'), Js('lie'), Js('lile'), Js('lienne'), Js('lyse'), Js('mia'), Js('mita'), Js('ne'), Js('na'), Js('ni'), Js('nys'), Js('ola'), Js('ora'), Js('phina'), Js('prys'), Js('rana'), Js('ree'), Js('ri'), Js('ris'), Js('sica'), Js('sira'), Js('sys'), Js('tina'), Js('trix'), Js('ula'), Js('vira'), Js('vyre'), Js('wyn'), Js('wyse'), Js('yola'), Js('yra'), Js('zana'), Js('zira')]))
pass
pass
pass
pass


# Add lib to the module scope
dndHalflingNames = var.to_python()