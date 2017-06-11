__all__ = ['dndShardmindNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameMas', 'nameGen'])
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
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.get('nameMas')()
            while PyJsStrictEq(var.get('nMs'),Js('')):
                var.get('nameMas')()
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Adu'), Js('Ama'), Js('Ani'), Js('Ar'), Js('Arsha'), Js('Ashi'), Js('Ashtu'), Js('Bala'), Js('Bara'), Js('Basha'), Js('Beles'), Js('Delu'), Js('Di'), Js('Dura'), Js('Duru'), Js('Enu'), Js('Eri'), Js('Eshu'), Js('Hua'), Js('Hun'), Js('Il'), Js('Ilu'), Js('Ira'), Js('Ish'), Js('Ku'), Js('Kua'), Js('Kuba'), Js('Lu'), Js('Mani'), Js('Mara'), Js('Mashi'), Js('Na'), Js('Nara'), Js('Nashi'), Js('Nu'), Js('Rua'), Js('Run'), Js('Sana'), Js('Sari'), Js('Selu'), Js('Shir'), Js('Suma'), Js('Tab'), Js('Tin'), Js('Tiru'), Js('Uba'), Js('Uku'), Js('Ura'), Js('Ut'), Js('Zaki')]))
var.put('nm2', Js([Js('ba'), Js('bam'), Js('bani'), Js('bu'), Js('ha'), Js('hara'), Js('hu'), Js('ka'), Js('ku'), Js('lazu'), Js('lua'), Js('mea'), Js('nar'), Js('nara'), Js('naram'), Js('naru'), Js('nashtu'), Js('ni'), Js('niri'), Js('nu'), Js('nua'), Js('pana'), Js('ram'), Js('ranu'), Js('rashi'), Js('raya'), Js('ri'), Js('rin'), Js('runu'), Js('shara'), Js('shari'), Js('shi'), Js('shti'), Js('shtu'), Js('shu'), Js('sunu'), Js('ta'), Js('tana'), Js('tani'), Js('tari'), Js('ti'), Js('tira'), Js('tiru'), Js('tua'), Js('tum'), Js('wia'), Js('ya'), Js('yara'), Js('yua'), Js('zu')]))
pass
pass
pass


# Add lib to the module scope
dndShardmindNames = var.to_python()