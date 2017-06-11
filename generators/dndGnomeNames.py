__all__ = ['dndGnomeNames']

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
    var.get('testSwear')(var.get('nMs'))
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
var.put('nm1', Js([Js('Al'), Js('Ari'), Js('Bil'), Js('Bri'), Js('Cal'), Js('Cor'), Js('Dav'), Js('Dor'), Js('Eni'), Js('Er'), Js('Far'), Js('Fel'), Js('Ga'), Js('Gra'), Js('His'), Js('Hor'), Js('Ian'), Js('Ipa'), Js('Je'), Js('Jor'), Js('Kas'), Js('Kel'), Js('Lan'), Js('Lo'), Js('Man'), Js('Mer'), Js('Nes'), Js('Ni'), Js('Or'), Js('Oru'), Js('Pana'), Js('Po'), Js('Qua'), Js('Quo'), Js('Ras'), Js('Ron'), Js('Sa'), Js('Sal'), Js('Sin'), Js('Tan'), Js('To'), Js('Tra'), Js('Um'), Js('Uri'), Js('Val'), Js('Vor'), Js('War'), Js('Wil'), Js('Wre'), Js('Xal'), Js('Xo'), Js('Ye'), Js('Yos'), Js('Zan'), Js('Zil')]))
var.put('nm2', Js([Js('bar'), Js('ben'), Js('bis'), Js('corin'), Js('cryn'), Js('don'), Js('dri'), Js('fan'), Js('fiz'), Js('gim'), Js('grim'), Js('hik'), Js('him'), Js('ji'), Js('jin'), Js('kas'), Js('kur'), Js('len'), Js('lin'), Js('min'), Js('mop'), Js('morn'), Js('nan'), Js('ner'), Js('ni'), Js('pip'), Js('pos'), Js('rick'), Js('ros'), Js('rug'), Js('ryn'), Js('ser'), Js('ston'), Js('tix'), Js('tor'), Js('ver'), Js('vyn'), Js('win'), Js('wor'), Js('xif'), Js('xim'), Js('ybar'), Js('yur'), Js('ziver'), Js('zu')]))
var.put('nm3', Js([Js('Alu'), Js('Ari'), Js('Ban'), Js('Bree'), Js('Car'), Js('Cel'), Js('Daphi'), Js('Do'), Js('Eili'), Js('El'), Js('Fae'), Js('Fen'), Js('Fol'), Js('Gal'), Js('Gren'), Js('Hel'), Js('Hes'), Js('Ina'), Js('Iso'), Js('Jel'), Js('Jo'), Js('Klo'), Js('Kri'), Js('Lil'), Js('Lori'), Js('Min'), Js('My'), Js('Ni'), Js('Ny'), Js('Oda'), Js('Or'), Js('Phi'), Js('Pri'), Js('Qi'), Js('Que'), Js('Re'), Js('Rosi'), Js('Sa'), Js('Sel'), Js('Spi'), Js('Ta'), Js('Tifa'), Js('Tri'), Js('Ufe'), Js('Uri'), Js('Ven'), Js('Vo'), Js('Wel'), Js('Wro'), Js('Xa'), Js('Xyro'), Js('Ylo'), Js('Yo'), Js('Zani'), Js('Zin')]))
var.put('nm4', Js([Js('bi'), Js('bys'), Js('celi'), Js('ci'), Js('dira'), Js('dysa'), Js('fi'), Js('fyx'), Js('gani'), Js('gyra'), Js('hana'), Js('hani'), Js('kasys'), Js('kini'), Js('la'), Js('li'), Js('lin'), Js('lys'), Js('mila'), Js('miphi'), Js('myn'), Js('myra'), Js('na'), Js('niana'), Js('noa'), Js('nove'), Js('phina'), Js('pine'), Js('qaryn'), Js('qys'), Js('rhana'), Js('roe'), Js('sany'), Js('ssa'), Js('sys'), Js('tina'), Js('tra'), Js('wyn'), Js('wyse'), Js('xi'), Js('xis'), Js('yaris'), Js('yore'), Js('za'), Js('zyre')]))
pass
pass
pass
pass


# Add lib to the module scope
dndGnomeNames = var.to_python()