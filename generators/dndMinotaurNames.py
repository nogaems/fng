__all__ = ['dndMinotaurNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameFem', 'nmSF', 'nameGen', 'nmSL', 'nmMF', 'nameMas', 'nmFF', 'nmFL', 'nmML'])
@Js
def PyJsHoisted_nameFem_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmFF').get('length'))))
    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmFL').get('length'))))
    var.put('nMs', (var.get('nmFF').get(var.get('rnd'))+var.get('nmFL').get(var.get('rnd2'))))
    var.get('testSwear')(var.get('nMs'))
PyJsHoisted_nameFem_.func_name = 'nameFem'
var.put('nameFem', PyJsHoisted_nameFem_)
@Js
def PyJsHoisted_nameMas_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    if (var.get('i')<Js(5.0)):
        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmFF').get('length'))))
        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmFL').get('length'))))
        var.put('nMs', (var.get('nmFF').get(var.get('rnd'))+var.get('nmFL').get(var.get('rnd2'))))
    else:
        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMF').get('length'))))
        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmML').get('length'))))
        var.put('nMs', (var.get('nmMF').get(var.get('rnd'))+var.get('nmML').get(var.get('rnd2'))))
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmSF').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmSL').get('length'))))
            var.put('nSr', (var.get('nmSF').get(var.get('rnd'))+var.get('nmSL').get(var.get('rnd2'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.get('nameFem')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameFem')()
            else:
                var.get('nameMas')()
                while PyJsStrictEq(var.get('nMs'),Js('')):
                    var.get('nameMas')()
            var.put('nMs', ((var.get('nMs')+Js(' '))+var.get('nSr')))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nmFF', Js([Js('Aam'), Js('Ane'), Js('Are'), Js('Ase'), Js('Duu'), Js('Em'), Js('Enti'), Js('Este'), Js('Fen'), Js('Hene'), Js('Hes'), Js('Hila'), Js('Hine'), Js('Ias'), Js('Ire'), Js('Ki'), Js('Kia'), Js('Kuo'), Js('Laan'), Js('Line'), Js('Loo'), Js('Muu'), Js('Nan'), Js('Nea'), Js('Neo'), Js('Noo'), Js('Nuo'), Js('Oen'), Js('Oes'), Js('Raas'), Js('Ras'), Js('Sees'), Js('Seo'), Js('Sina'), Js('Tee'), Js('Tes'), Js('Tia'), Js('Tina'), Js('Uova'), Js('Weo')]))
var.put('nmFL', Js([Js('dra'), Js('fin'), Js('kane'), Js('kea'), Js('la'), Js('las'), Js('len'), Js('lin'), Js('lo'), Js('mas'), Js('me'), Js('mi'), Js('min'), Js('na'), Js('nan'), Js('nas'), Js('nim'), Js('nu'), Js('pen'), Js('pe'), Js('ra'), Js('ren'), Js('res'), Js('rin'), Js('ris'), Js('ru'), Js('sen'), Js('sia'), Js('ta'), Js('ter'), Js('tin'), Js('tra'), Js('tred'), Js('tri'), Js('trin'), Js('tris'), Js('ven'), Js('vena'), Js('vera'), Js('vin')]))
var.put('nmMF', Js([Js('Ar'), Js('Are'), Js('Aste'), Js('Bjor'), Js('Car'), Js('Cod'), Js('Da'), Js('Djar'), Js('Djun'), Js('Doen'), Js('Dor'), Js('Dur'), Js('Foos'), Js('Gar'), Js('Goe'), Js('Gra'), Js('Gran'), Js('Gun'), Js('Hun'), Js('Ja'), Js('Jar'), Js('Kar'), Js('Kin'), Js('Kir'), Js('Koo'), Js('Koor'), Js('Krum'), Js('Kur'), Js('Man'), Js('Min'), Js('Mir'), Js('Noo'), Js('Pod'), Js('Rak'), Js('Te'), Js('Toon'), Js('Trak'), Js('Tur'), Js('Zam'), Js('Zun')]))
var.put('nmML', Js([Js('ban'), Js('baran'), Js('bur'), Js('dak'), Js('daran'), Js('dor'), Js('fajar'), Js('faruk'), Js('furan'), Js('gajan'), Js('garak'), Js('gur'), Js('jar'), Js('kan'), Js('kar'), Js('karat'), Js('kun'), Js('kurat'), Js('kus'), Js('manuk'), Js('maruk'), Js('nark'), Js('narun'), Js('paran'), Js('raduk'), Js('rak'), Js('rakar'), Js('ranak'), Js('rapak'), Js('ras'), Js('rat'), Js('rios'), Js('ron'), Js('rus'), Js('rut'), Js('tagar'), Js('taruk'), Js('toron'), Js('turok'), Js('tus')]))
var.put('nmSF', Js([Js('Agile'), Js('Bear'), Js('Bold'), Js('Boulder'), Js('Brave'), Js('Bright'), Js('Fearless'), Js('Fist'), Js('Glory'), Js('Goblin'), Js('Great'), Js('Heavy'), Js('Honor'), Js('Iron'), Js('Jagged'), Js('Keen'), Js('Nimble'), Js('Orc'), Js('Rock'), Js('Rugged'), Js('Sharp'), Js('Silent'), Js('Single'), Js('Steady'), Js('Steel'), Js('Stone'), Js('Storm'), Js('Stout'), Js('Strong'), Js('Swift'), Js('Thick'), Js('Thunder'), Js('Tough'), Js('Truth'), Js('Valiant'), Js('Vigil'), Js('Wolf')]))
var.put('nmSL', Js([Js('bane'), Js('body'), Js('eye'), Js('fighter'), Js('fist'), Js('fury'), Js('hand'), Js('heart'), Js('hide'), Js('hoof'), Js('horn'), Js('horns'), Js('hunter'), Js('leader'), Js('mind'), Js('pelt'), Js('roar'), Js('runner'), Js('skin'), Js('skull'), Js('slash'), Js('slayer'), Js('speaker'), Js('step'), Js('striker'), Js('vigor'), Js('walker'), Js('warrior')]))
pass
pass
pass
pass


# Add lib to the module scope
dndMinotaurNames = var.to_python()