__all__ = ['hpGoblinNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ad'), Js('Ag'), Js('Al'), Js('Ar'), Js('Ban'), Js('Bar'), Js('Bog'), Js('Brag'), Js('Brod'), Js('Brun'), Js('Bug'), Js('Ear'), Js('Eg'), Js('Er'), Js('Far'), Js('Fil'), Js('Frad'), Js('Fur'), Js('Gar'), Js('Gor'), Js('Grag'), Js('Gran'), Js('Grin'), Js('Gruk'), Js('Gug'), Js('Gur'), Js('Kar'), Js('Kog'), Js('Krag'), Js('Krug'), Js('Kur'), Js('Lag'), Js('Lar'), Js('Lug'), Js('Lur'), Js('Nad'), Js('Nag'), Js('Nur'), Js('Rag'), Js('Ran'), Js('Rod'), Js('Rog'), Js('Ug'), Js('Ul'), Js('Ur')]))
var.put('nm2', Js([Js('git'), Js('gok'), Js('gor'), Js('gott'), Js('gras'), Js('grat'), Js('grot'), Js('guff'), Js('gus'), Js('guss'), Js('kar'), Js('kit'), Js('knas'), Js('knus'), Js('koff'), Js('kor'), Js('kras'), Js('krat'), Js('krus'), Js('kus'), Js('laff'), Js('last'), Js('lig'), Js('lirg'), Js('lok'), Js('lor'), Js('luff'), Js('luk'), Js('lus'), Js('naff'), Js('nar'), Js('nast'), Js('nok'), Js('not'), Js('nott'), Js('nuff'), Js('nuk'), Js('nus'), Js('raff'), Js('ragg'), Js('rak'), Js('rast'), Js('rat'), Js('rig'), Js('rod')]))
pass
pass


# Add lib to the module scope
hpGoblinNames = var.to_python()