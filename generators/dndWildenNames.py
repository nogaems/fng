__all__ = ['dndWildenNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nmMFf', 'nameFem', 'nameGen', 'nmMSl', 'nmMSf', 'nameMas', 'nmMFl', 'nmFF', 'nmFL'])
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
        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMFf').get('length'))))
        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMFl').get('length'))))
        var.put('nMs', (var.get('nmMFf').get(var.get('rnd'))+var.get('nmMFl').get(var.get('rnd2'))))
    else:
        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMSf').get('length'))))
        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMSl').get('length'))))
        var.put('nMs', (var.get('nmMSf').get(var.get('rnd'))+var.get('nmMSl').get(var.get('rnd2'))))
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
var.put('nmMFf', Js([Js('Ban'), Js('Bar'), Js('Dal'), Js('Dam'), Js('Dun'), Js('Dur'), Js('Fas'), Js('Fin'), Js('Kan'), Js('Kin'), Js('Kor'), Js('Lan'), Js('Lim'), Js('Lon'), Js('Man'), Js('Mar'), Js('Mas'), Js('Mid'), Js('Mor'), Js('Mur'), Js('Nam'), Js('Nor'), Js('Rad'), Js('Ran'), Js('Ras'), Js('Rod'), Js('San'), Js('Sin'), Js('Tor'), Js('Tum')]))
var.put('nmMFl', Js([Js('darras'), Js('darris'), Js('dommar'), Js('donnir'), Js('durrun'), Js('farran'), Js('fidden'), Js('garron'), Js('kammin'), Js('karran'), Js('lammir'), Js('larrin'), Js('mannor'), Js('marden'), Js('mennar'), Js('mennor'), Js('mindin'), Js('mirron'), Js('morrin'), Js('murrin'), Js('norren'), Js('norten'), Js('rammas'), Js('sammas'), Js('sannim'), Js('sarrin'), Js('sarris'), Js('sorran'), Js('tarrin'), Js('torrin')]))
var.put('nmMSf', Js([Js('Barrun'), Js('Burrin'), Js('Darras'), Js('Farran'), Js('Farrin'), Js('Fidden'), Js('Garrin'), Js('Harren'), Js('Harrun'), Js('Karrat'), Js('Karren'), Js('Ketten'), Js('Korrin'), Js('Larras'), Js('Lommir'), Js('Lorrin'), Js('Marrad'), Js('Mirren'), Js('Mirrun'), Js('Morrin'), Js('Parran'), Js('Purren'), Js('Tarris'), Js('Torren'), Js('Torrim'), Js('Turrus'), Js('Venner'), Js('Vunnar'), Js('Zakkan'), Js('Zarrak')]))
var.put('nmMSl', Js([Js('bar'), Js('bor'), Js('bun'), Js('das'), Js('din'), Js('dun'), Js('dur'), Js('fas'), Js('fum'), Js('gar'), Js('gun'), Js('kas'), Js('kin'), Js('las'), Js('lis'), Js('mar'), Js('mas'), Js('min'), Js('mur'), Js('nas'), Js('nim'), Js('nor'), Js('pan'), Js('rak'), Js('ras'), Js('tor'), Js('tur'), Js('zad'), Js('zim'), Js('zor')]))
var.put('nmFF', Js([Js('Allin'), Js('Ashin'), Js('Bunn'), Js('Dann'), Js('Darn'), Js('Diss'), Js('Enn'), Js('Eril'), Js('Fenn'), Js('Fert'), Js('Firr'), Js('Fiss'), Js('Genn'), Js('Grin'), Js('Kalk'), Js('Kenn'), Js('Kers'), Js('Krin'), Js('Lerm'), Js('Less'), Js('Linn'), Js('Lorr'), Js('Minn'), Js('Mirt'), Js('Mist'), Js('Nem'), Js('Niss'), Js('Shall'), Js('Shan'), Js('Shenn'), Js('Tarr'), Js('Taz'), Js('Tell'), Js('Tin'), Js('Tirr'), Js('Tris'), Js('Wenn'), Js('Zar'), Js('Zaz'), Js('Zell')]))
var.put('nmFL', Js([Js('ahai'), Js('akei'), Js('alin'), Js('amai'), Js('anai'), Js('annar'), Js('annas'), Js('arris'), Js('arrel'), Js('arresh'), Js('artish'), Js('asha'), Js('atish'), Js('elbis'), Js('embin'), Js('enna'), Js('ennash'), Js('entah'), Js('eris'), Js('erla'), Js('erlis'), Js('imai'), Js('imbel'), Js('imei'), Js('immesh'), Js('inah'), Js('inash'), Js('inda'), Js('inna'), Js('innem'), Js('irrah'), Js('ishai'), Js('issa'), Js('itas'), Js('onnes'), Js('onteh'), Js('orda'), Js('oren'), Js('oris'), Js('orren')]))
pass
pass
pass
pass


# Add lib to the module scope
dndWildenNames = var.to_python()