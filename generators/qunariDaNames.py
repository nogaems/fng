__all__ = ['qunariDaNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['namesFamily', 'nameGen', 'namesFemale2', 'namesMale', 'namesFemale'])
@Js
def PyJsHoisted_nameGen_(namesMale, namesFamily, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'namesMale':namesMale, 'namesFamily':namesFamily}, var)
    var.registers(['names1', 'names2', 'result', 'namesMale', 'namesFamily'])
    var.put('names1', var.get('namesMale'))
    var.put('names2', var.get('namesFamily'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
            var.put('names', (var.get('names1').get(var.get('rnd0'))+var.get('names2').get(var.get('rnd1'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('namesFemale', Js([Js('As'), Js('Bah'), Js('Bir'), Js('Birs'), Js('Can'), Js('Dem'), Js('Fad'), Js('Giz'), Js('Hat'), Js('Kar'), Js('Kard'), Js('Kub'), Js('Kubr'), Js('Kut'), Js('Mel'), Js('Naz'), Js('Nazl'), Js('Nih'), Js('Or'), Js('Ork'), Js('Oz'), Js('Ozen'), Js('Ras'), Js('San'), Js('Say'), Js('Sem'), Js('Ser'), Js('Sol'), Js('Solm'), Js('Sum'), Js('Tam'), Js('Tamg'), Js('Tur'), Js('Turn'), Js('Yas'), Js('Yasem'), Js('Yen'), Js('Yon')]))
var.put('namesFemale2', Js([Js('a'), Js('aan'), Js('al'), Js('am'), Js('an'), Js('anem'), Js('ar'), Js('asan'), Js('ay'), Js('ayar'), Js('az'), Js('azik'), Js('azli'), Js('e'), Js('ek'), Js('elek'), Js('elen'), Js('em'), Js('emin'), Js('en'), Js('ena'), Js('ener'), Js('enli'), Js('er'), Js('era'), Js('et'), Js('ice'), Js('ide'), Js('ie'), Js('iha'), Js('ihan'), Js('ik'), Js('in'), Js('onal'), Js('ul'), Js('umer')]))
var.put('namesMale', Js([Js('Ak'), Js('Akin'), Js('Akor'), Js('Al'), Js('Ar'), Js('Aris'), Js('Arm'), Js('Arv'), Js('As'), Js('Ask'), Js('Askh'), Js('Asl'), Js('Bas'), Js('Bast'), Js('Bur'), Js('Dur'), Js('Gun'), Js('Gund'), Js('Gur'), Js('Gurh'), Js('Jar'), Js('Jarv'), Js('Kan'), Js('Ket'), Js('Kub'), Js('Mar'), Js('Met'), Js('Naz'), Js('Ok'), Js('Okan'), Js('Or'), Js('Orn'), Js('Oz'), Js('Ozk'), Js('Sal'), Js('Sen'), Js('S'), Js('St'), Js('Tam'), Js('Ten'), Js('Yag'), Js('Yagm')]))
var.put('namesFamily', Js([Js('aarad'), Js('aari'), Js('aas'), Js('aca'), Js('ad'), Js('ak'), Js('alit'), Js('amay'), Js('an'), Js('anat'), Js('aner'), Js('ant'), Js('arad'), Js('ari'), Js('as'), Js('at'), Js('ay'), Js('azim'), Js('ehan'), Js('ek'), Js('en'), Js('enol'), Js('er'), Js('ilay'), Js('im'), Js('iner'), Js('ishok'), Js('it'), Js('ogan'), Js('ojan'), Js('ok'), Js('ol'), Js('oren'), Js('ri'), Js('ug'), Js('ul'), Js('urak'), Js('urhan'), Js('utlu')]))
pass
pass


# Add lib to the module scope
qunariDaNames = var.to_python()