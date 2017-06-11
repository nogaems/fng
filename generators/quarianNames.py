__all__ = ['quarianNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen', 'names6', 'names5', 'names8', 'names2', 'names7'])
@Js
def PyJsHoisted_nameGen_(gender, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'gender':gender}, var)
    var.registers(['names4', 'tp', 'names3', 'names1', 'result', 'gender'])
    var.put('tp', var.get('gender'))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('names1', Js([Js('K'), Js('G'), Js('C'), Js('F'), Js('H'), Js('J'), Js('L'), Js('M'), Js('N'), Js('R'), Js('S'), Js('V'), Js('W'), Js('Y'), Js('Z'), Js('C'), Js('F'), Js('H'), Js('J'), Js('L'), Js('M'), Js('N'), Js('R'), Js('S'), Js('V'), Js('W'), Js('Y'), Js('Z')]))
        var.put('names3', Js([Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('l'), Js('n'), Js('nn'), Js('mm'), Js('tor'), Js('to'), Js('sin'), Js('lo')]))
        var.put('names4', Js([Js('')]))
    else:
        var.put('names1', Js([Js('C'), Js('F'), Js('H'), Js('J'), Js('L'), Js('M'), Js('N'), Js('R'), Js('S'), Js('Sh'), Js('W'), Js('Y'), Js('Z')]))
        var.put('names3', Js([Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('l'), Js('n'), Js('nn'), Js('mm')]))
        var.put('names4', Js([Js('a'), Js('e'), Js('u'), Js('i'), Js('o'), Js('a')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
            var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
            var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length'))))
            def PyJs_LONG_0_(var=var):
                return ((((((((((((var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1')))+var.get('names3').get(var.get('rnd2')))+var.get('names4').get(var.get('rnd3')))+Js("'"))+var.get('names5').get(var.get('rnd4')))+var.get('names2').get(var.get('rnd5')))+var.get('names6').get(var.get('rnd6')))+Js(' '))+var.get('names7').get(var.get('rnd7')))+Js(' '))+var.get('names5').get(var.get('rnd8')))+var.get('names2').get(var.get('rnd9')))
            var.put('names', (PyJs_LONG_0_()+var.get('names8').get(var.get('rnd10'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('aa'), Js('ee'), Js('ae')]))
var.put('names5', Js([Js('C'), Js('F'), Js('H'), Js('G'), Js('J'), Js('L'), Js('M'), Js('N'), Js('R'), Js('S'), Js('Sh'), Js('V'), Js('T'), Js('W'), Js('X'), Js('Y'), Js('Z')]))
var.put('names6', Js([Js('dal'), Js('dda'), Js('dor'), Js('fal'), Js('fin'), Js('for'), Js('gar'), Js('l'), Js('la'), Js('lan'), Js('las'), Js('lin'), Js('ll'), Js('llo'), Js('lon'), Js('lun'), Js('m'), Js('ma'), Js('man'), Js('mas'), Js('me'), Js('min'), Js('mis'), Js('mm'), Js('mma'), Js('mor'), Js('mos'), Js('mun'), Js('n'), Js('nar'), Js('nis'), Js('nn'), Js('nna'), Js('r'), Js('ra'), Js('rah'), Js('ram'), Js('ras'), Js('ris'), Js('rol'), Js('rrel'), Js('rul'), Js('s'), Js('sa'), Js('sal'), Js('sar'), Js('ss'), Js('sul'), Js('zh'), Js('zu')]))
var.put('names7', Js([Js('nar'), Js('vas')]))
var.put('names8', Js([Js('bra'), Js('ca'), Js('chol'), Js('darum'), Js('din'), Js('dir'), Js('dolor'), Js('dor'), Js('doruk'), Js('firn'), Js('fis'), Js('gro'), Js('hala'), Js('hok'), Js('ji'), Js('jol'), Js('ko'), Js('kor'), Js('kra'), Js('larm'), Js('lazi'), Js('leya'), Js('ma'), Js('morn'), Js('nbay'), Js('nil'), Js('nna'), Js('pal'), Js('pan'), Js('ra'), Js('rah'), Js('raka'), Js('ram'), Js('rark'), Js('reh'), Js('ron'), Js('sost'), Js('talir'), Js('vo'), Js('vum'), Js('wa'), Js('wal'), Js('wan'), Js('wib'), Js('worp'), Js('yya'), Js('zal'), Js('zay'), Js('zorn'), Js('zzor')]))
pass
pass


# Add lib to the module scope
quarianNames = var.to_python()