__all__ = ['mountainclans']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names4', 'names2', 'nameGen', 'names3'])
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
            if (var.get('tp')==Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('names', (var.get('names3').get(var.get('rnd'))+var.get('names4').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', (var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('A'), Js('Agga'), Js('Ara'), Js('Ardo'), Js('Ba'), Js('Bo'), Js('Bra'), Js('Bro'), Js('Da'), Js('Do'), Js('Dra'), Js('Dro'), Js('Ga'), Js('Gro'), Js('Gru'), Js('Gu'), Js('Ho'), Js('Hra'), Js('Hro'), Js('Hu'), Js('Ja'), Js('Jara'), Js('Jo'), Js('Jora'), Js('Ka'), Js('Kra'), Js('Kri'), Js('Kru'), Js('Sha'), Js('Sra'), Js('Sru'), Js('Sta'), Js('Tho'), Js('Ti'), Js('Tra'), Js('Tro'), Js('U'), Js('Uma'), Js('Ura'), Js('Uri')]))
var.put('names2', Js([Js('dar'), Js('dog'), Js('dor'), Js('drag'), Js('gah'), Js('gga'), Js('ggan'), Js('ggor'), Js('gir'), Js('gra'), Js('kha'), Js('khan'), Js('khar'), Js('kkan'), Js('kor'), Js('laf'), Js('lf'), Js('llag'), Js('log'), Js('lor'), Js('mar'), Js('mhor'), Js('mman'), Js('mor'), Js('nar'), Js('nnag'), Js('nog'), Js('nthor'), Js('rak'), Js('rlag'), Js('rrag'), Js('rras'), Js('tar'), Js('ther'), Js('thor'), Js('ttag'), Js('vas'), Js('vor'), Js('vrak'), Js('vvar')]))
var.put('names3', Js([Js('Bi'), Js('Bra'), Js('Bre'), Js('Bu'), Js('Cha'), Js('Che'), Js('Cru'), Js('Cwe'), Js('Da'), Js('De'), Js('Dre'), Js('Dri'), Js('Fa'), Js('Fe'), Js('Fra'), Js('Fri'), Js('Ge'), Js('Gi'), Js('Gre'), Js('Gri'), Js('Gwe'), Js('Ma'), Js('Mhe'), Js('Mi'), Js('Pha'), Js('Phu'), Js('Pre'), Js('Pru'), Js('Ra'), Js('Re'), Js('Ri'), Js('Ru'), Js('Sha'), Js('Sre'), Js('Sta'), Js('Ste'), Js('Ta'), Js('Tra'), Js('Tre'), Js('Tri')]))
var.put('names4', Js([Js('cei'), Js('cha'), Js('chal'), Js('ffis'), Js('ggi'), Js('ggin'), Js('ggis'), Js('hell'), Js('his'), Js('hynn'), Js('ka'), Js('kinn'), Js('kis'), Js('lenn'), Js('lla'), Js('llis'), Js('ma'), Js('miy'), Js('mmi'), Js('nell'), Js('nna'), Js('nni'), Js('ress'), Js('rra'), Js('rris'), Js('senne'), Js('sha'), Js('ssi'), Js('tish'), Js('tta'), Js('twyn'), Js('va'), Js('vara'), Js('vell'), Js('wenn'), Js('wyn'), Js('wys'), Js('ya'), Js('yas'), Js('yenn')]))
pass
pass


# Add lib to the module scope
mountainclans = var.to_python()