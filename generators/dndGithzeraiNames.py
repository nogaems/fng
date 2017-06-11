__all__ = ['dndGithzeraiNames']

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
var.put('nm1', Js([Js('Am'), Js('Ar'), Js('Ara'), Js('Aza'), Js('Bar'), Js('Bra'), Js('Bru'), Js('Da'), Js('Dar'), Js('Dor'), Js('Dra'), Js('Dro'), Js('Du'), Js('Fa'), Js('Far'), Js('Fer'), Js('Gra'), Js('Gran'), Js('Gre'), Js('Gro'), Js('Gru'), Js('Hu'), Js('Ka'), Js('Kar'), Js('Kha'), Js('Kra'), Js('Kro'), Js('Ma'), Js('Mu'), Js('Na'), Js('Nar'), Js('Nu'), Js('Ra'), Js('Ran'), Js('Rin'), Js('Ru'), Js('Sha'), Js('Shra'), Js('Sra'), Js('Zra')]))
var.put('nm2', Js([Js('d'), Js('dak'), Js('gh'), Js('k'), Js('kahr'), Js('kar'), Js('khar'), Js('kk'), Js('lag'), Js('llak'), Js('mag'), Js('mak'), Js('nag'), Js('rag'), Js('rak'), Js('ram'), Js('rath'), Js('rek'), Js('rg'), Js('rm'), Js('rth'), Js('ruk'), Js('th'), Js('tig'), Js('zag'), Js('zak'), Js('zar'), Js('zeg'), Js('zirg'), Js('zth')]))
var.put('nm3', Js([Js('Ad'), Js('Alm'), Js('Arw'), Js('Ash'), Js('Dah'), Js('Dhar'), Js('Dolm'), Js('Dran'), Js('Ell'), Js('Erzh'), Js('Esz'), Js('Ezh'), Js('Grel'), Js('Halm'), Js('Han'), Js('Harn'), Js('Heln'), Js('Ihr'), Js('Iln'), Js('Imm'), Js('Iz'), Js('Kan'), Js('Kharm'), Js('Khaz'), Js('Krez'), Js('Laz'), Js('Lez'), Js('Lhash'), Js('Magd'), Js('Marm'), Js('Nagr'), Js('Nah'), Js('Nalm'), Js('Rasz'), Js('Rez'), Js('Sham'), Js('Sharm'), Js('Shund'), Js('Um'), Js('Uw')]))
var.put('nm4', Js([Js('a'), Js('ah'), Js('aka'), Js('al'), Js('arah'), Js('arin'), Js('aya'), Js('ayah'), Js('eah'), Js('eka'), Js('el'), Js('ela'), Js('elna'), Js('elya'), Js('elzal'), Js('ena'), Js('enah'), Js('era'), Js('erah'), Js('eya'), Js('ihn'), Js('ila'), Js('ilzin'), Js('in'), Js('ina'), Js('ira'), Js('iza'), Js('mina'), Js('ya'), Js('yara')]))
pass
pass
pass
pass


# Add lib to the module scope
dndGithzeraiNames = var.to_python()