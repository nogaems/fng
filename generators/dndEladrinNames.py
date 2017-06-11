__all__ = ['dndEladrinNames']

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
var.put('nm1', Js([Js('Ara'), Js('Aran'), Js('Ber'), Js('Bran'), Js('Cor'), Js('Cru'), Js('Da'), Js('Daye'), Js('Elro'), Js('Ere'), Js('Far'), Js('Fyla'), Js('Gal'), Js('Galin'), Js('Ha'), Js('Hor'), Js('Im'), Js('Ira'), Js('Ja'), Js('Jor'), Js('Kru'), Js('Kuo'), Js('Lan'), Js('Lic'), Js('Mar'), Js('Min'), Js('Nal'), Js('Nark'), Js('Ola'), Js('Otir'), Js('Pae'), Js('Pan'), Js('Qua'), Js('Quo'), Js('Rel'), Js('Riar'), Js('Sarn'), Js('Sove'), Js('Tav'), Js('Trin'), Js('Uri'), Js('Veth'), Js('Vic'), Js('Wal'), Js('Wrug'), Js('Xan'), Js('Yan'), Js('Yor'), Js('Zen'), Js('Zor')]))
var.put('nm2', Js([Js('aris'), Js('aster'), Js('baver'), Js('bin'), Js('card'), Js('corin'), Js('dan'), Js('darai'), Js('dartis'), Js('don'), Js('emin'), Js('erta'), Js('fis'), Js('fros'), Js('geon'), Js('grephor'), Js('heros'), Js('horn'), Js('ikul'), Js('iver'), Js('kris'), Js('kul'), Js('lias'), Js('liss'), Js('mendi'), Js('meral'), Js('mil'), Js('morn'), Js('neiros'), Js('nis'), Js('okas'), Js('oros'), Js('peiros'), Js('prath'), Js('ratra'), Js('reth'), Js('rian'), Js('rion'), Js('sirak'), Js('ster'), Js('thas'), Js('tihr'), Js('torin'), Js('urian'), Js('uvir'), Js('van'), Js('vis'), Js('wirn'), Js('worn'), Js('xeral'), Js('xis'), Js('ykos'), Js('yth'), Js('zeiros'), Js('zion')]))
var.put('nm3', Js([Js('Al'), Js('An'), Js('Anas'), Js('Be'), Js('Bri'), Js('Cae'), Js('Cyl'), Js('Dris'), Js('Dur'), Js('Eil'), Js('Ena'), Js('Fae'), Js('Fan'), Js('Gru'), Js('Gyl'), Js('Hen'), Js('Hyl'), Js('Illa'), Js('Ire'), Js('Jar'), Js('Jelen'), Js('Kai'), Js('Kora'), Js('Les'), Js('Lyv'), Js('Mag'), Js('Me'), Js('Nai'), Js('Neri'), Js('Ol'), Js('Ori'), Js('Pi'), Js('Prys'), Js('Qi'), Js('Que'), Js('Ri'), Js('Rol'), Js('Sa'), Js('Sha'), Js('Thei'), Js('Tri'), Js('Ul'), Js('Ura'), Js('Va'), Js('Vela'), Js('Wes'), Js('Wre'), Js('Xyr'), Js('Ylla'), Js('Zen')]))
var.put('nm4', Js([Js('bis'), Js('bynn'), Js('cahne'), Js('caryn'), Js('celle'), Js('cena'), Js('diel'), Js('dys'), Js('faera'), Js('fyra'), Js('glyn'), Js('grys'), Js('hanna'), Js('hyssa'), Js('kiries'), Js('kyrath'), Js('lenae'), Js('lenna'), Js('lyn'), Js('lynna'), Js('meiv'), Js('miris'), Js('mynis'), Js('nairra'), Js('neth'), Js('parys'), Js('prana'), Js('qirith'), Js('qis'), Js('raste'), Js('rastra'), Js('riele'), Js('rynna'), Js('sanna'), Js('shana'), Js('sys'), Js('thaea'), Js('tora'), Js('trianna'), Js('vara'), Js('viryn'), Js('vyre'), Js('wena'), Js('wyse'), Js('xana'), Js('xis'), Js('yana'), Js('yeira'), Js('zane'), Js('zora')]))
pass
pass
pass
pass


# Add lib to the module scope
dndEladrinNames = var.to_python()