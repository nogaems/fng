__all__ = ['dndElfNames']

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
var.put('nm1', Js([Js('Ad'), Js('Ae'), Js('Bal'), Js('Bei'), Js('Car'), Js('Cra'), Js('Dae'), Js('Dor'), Js('El'), Js('Ela'), Js('Er'), Js('Far'), Js('Fen'), Js('Gen'), Js('Glyn'), Js('Hei'), Js('Her'), Js('Ian'), Js('Ili'), Js('Kea'), Js('Kel'), Js('Leo'), Js('Lu'), Js('Mira'), Js('Mor'), Js('Nae'), Js('Nor'), Js('Olo'), Js('Oma'), Js('Pa'), Js('Per'), Js('Pet'), Js('Qi'), Js('Qin'), Js('Ralo'), Js('Ro'), Js('Sar'), Js('Syl'), Js('The'), Js('Tra'), Js('Ume'), Js('Uri'), Js('Va'), Js('Vir'), Js('Waes'), Js('Wran'), Js('Yel'), Js('Yin'), Js('Zin'), Js('Zum')]))
var.put('nm2', Js([Js('balar'), Js('beros'), Js('can'), Js('ceran'), Js('dan'), Js('dithas'), Js('faren'), Js('fir'), Js('geiros'), Js('golor'), Js('hice'), Js('horn'), Js('jeon'), Js('jor'), Js('kas'), Js('kian'), Js('lamin'), Js('lar'), Js('len'), Js('maer'), Js('maris'), Js('menor'), Js('myar'), Js('nan'), Js('neiros'), Js('nelis'), Js('norin'), Js('peiros'), Js('petor'), Js('qen'), Js('quinal'), Js('ran'), Js('ren'), Js('ric'), Js('ris'), Js('ro'), Js('salor'), Js('sandoral'), Js('toris'), Js('tumal'), Js('valur'), Js('ven'), Js('warin'), Js('wraek'), Js('xalim'), Js('xidor'), Js('yarus'), Js('ydark'), Js('zeiros'), Js('zumin')]))
var.put('nm3', Js([Js('Ad'), Js('Ara'), Js('Bi'), Js('Bry'), Js('Cai'), Js('Chae'), Js('Da'), Js('Dae'), Js('Eil'), Js('En'), Js('Fa'), Js('Fae'), Js('Gil'), Js('Gre'), Js('Hele'), Js('Hola'), Js('Iar'), Js('Ina'), Js('Jo'), Js('Key'), Js('Kris'), Js('Lia'), Js('Lora'), Js('Mag'), Js('Mia'), Js('Neri'), Js('Ola'), Js('Ori'), Js('Phi'), Js('Pres'), Js('Qi'), Js('Qui'), Js('Rava'), Js('Rey'), Js('Sha'), Js('Syl'), Js('Tor'), Js('Tris'), Js('Ula'), Js('Uri'), Js('Val'), Js('Ven'), Js('Wyn'), Js('Wysa'), Js('Xil'), Js('Xyr'), Js('Yes'), Js('Ylla'), Js('Zin'), Js('Zyl')]))
var.put('nm4', Js([Js('banise'), Js('bella'), Js('caryn'), Js('cyne'), Js('di'), Js('dove'), Js('fiel'), Js('fina'), Js('gella'), Js('gwyn'), Js('hana'), Js('harice'), Js('jyre'), Js('kalyn'), Js('krana'), Js('lana'), Js('lee'), Js('leth'), Js('lynn'), Js('moira'), Js('mys'), Js('na'), Js('nala'), Js('phine'), Js('phyra'), Js('qirelle'), Js('ra'), Js('ralei'), Js('rel'), Js('rie'), Js('rieth'), Js('rona'), Js('rora'), Js('roris'), Js('satra'), Js('stina'), Js('sys'), Js('thana'), Js('thyra'), Js('tris'), Js('varis'), Js('vyre'), Js('wenys'), Js('wynn'), Js('xina'), Js('xisys'), Js('ynore'), Js('yra'), Js('zana'), Js('zorwyn')]))
pass
pass
pass
pass


# Add lib to the module scope
dndElfNames = var.to_python()