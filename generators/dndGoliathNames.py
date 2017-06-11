__all__ = ['dndGoliathNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameFem', 'nmSF', 'nameGen', 'nmSL', 'nmMF', 'nameMas', 'nmMdL', 'nmFF', 'nmFL', 'nmML', 'nmMdF'])
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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMdF').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmMdL').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmSF').get('length'))))
            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nmSL').get('length'))))
            var.put('nSr', ((((var.get('nmMdF').get(var.get('rnd'))+var.get('nmMdL').get(var.get('rnd2')))+Js(' '))+var.get('nmSF').get(var.get('rnd3')))+var.get('nmSL').get(var.get('rnd4'))))
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
var.put('nmFF', Js([Js('Age'), Js('Ane'), Js('Gau'), Js('Ge'), Js('Ina'), Js('Kau'), Js('Ke'), Js('Ki'), Js('Kuo'), Js('La'), Js('Le'), Js('Maa'), Js('Man'), Js('Mau'), Js('Me'), Js('Na'), Js('Nal'), Js('Ni'), Js('One'), Js('Ori'), Js('Paa'), Js('Pau'), Js('Pe'), Js('Tha'), Js('The'), Js('Thu'), Js('Vaa'), Js('Vau'), Js('Ve'), Js('Vu')]))
var.put('nmFL', Js([Js('gea'), Js('geo'), Js('gia'), Js('gu'), Js('kea'), Js('keo'), Js('ki'), Js('kia'), Js('kio'), Js('la'), Js('lai'), Js('lane'), Js('lea'), Js('leo'), Js('lo'), Js('lu'), Js('meo'), Js('mi'), Js('mia'), Js('ne'), Js('nea'), Js('neo'), Js('ni'), Js('nia'), Js('nu'), Js('peo'), Js('peu'), Js('pu'), Js('rea'), Js('ri'), Js('ria'), Js('the'), Js('thea'), Js('thia'), Js('thio'), Js('thu'), Js('vea'), Js('vi'), Js('via'), Js('vu')]))
var.put('nmMF', Js([Js('Ag'), Js('Apa'), Js('Au'), Js('Aug'), Js('Eg'), Js('Gau'), Js('Gea'), Js('Gha'), Js('Ili'), Js('Kana'), Js('Kava'), Js('Keo'), Js('Khu'), Js('La'), Js('Ma'), Js('Mau'), Js('Mea'), Js('Mo'), Js('Na'), Js('Neo'), Js('Pa'), Js('Pu'), Js('Tha'), Js('Thava'), Js('Tho'), Js('Va'), Js('Vau'), Js('Vega'), Js('Vi'), Js('Vo')]))
var.put('nmML', Js([Js('gak'), Js('gal'), Js('gan'), Js('gath'), Js('ghan'), Js('gith'), Js('glath'), Js('gun'), Js('kan'), Js('kein'), Js('khal'), Js('kin'), Js('kon'), Js('lath'), Js('lig'), Js('lok'), Js('mahg'), Js('mahk'), Js('mahl'), Js('mak'), Js('man'), Js('mith'), Js('mul'), Js('nak'), Js('nath'), Js('nihl'), Js('noth'), Js('path'), Js('phak'), Js('thag'), Js('thak'), Js('tham'), Js('thi'), Js('thok'), Js('veith'), Js('vek'), Js('vhal'), Js('vhik'), Js('vith'), Js('voi')]))
var.put('nmMdF', Js([Js('Adept'), Js('Bear'), Js('Brave'), Js('Bright'), Js('Dawn'), Js('Day'), Js('Deer'), Js('Dream'), Js('Flint'), Js('Fearless'), Js('Flower'), Js('Food'), Js('Fright'), Js('Goat'), Js('Hard'), Js('Hide'), Js('High'), Js('Honest'), Js('Horn'), Js('Keen'), Js('Lone'), Js('Long'), Js('Low'), Js('Lumber'), Js('Master'), Js('Mind'), Js('Mountain'), Js('Night'), Js('Rain'), Js('River'), Js('Rock'), Js('Root'), Js('Silent'), Js('Sky'), Js('Sly'), Js('Smart'), Js('Steady'), Js('Stone'), Js('Storm'), Js('Strong'), Js('Swift'), Js('Thread'), Js('Thunder'), Js('Tree'), Js('Tribe'), Js('True'), Js('Truth'), Js('Wander'), Js('Wild'), Js('Wise'), Js('Wound')]))
var.put('nmMdL', Js([Js('aid'), Js('bearer'), Js('breaker'), Js('caller'), Js('carver'), Js('chaser'), Js('climber'), Js('cook'), Js('dream'), Js('drifter'), Js('eye'), Js('finder'), Js('fist'), Js('friend'), Js('frightener'), Js('guard'), Js('hand'), Js('hauler'), Js('heart'), Js('herder'), Js('hunter'), Js('jumper'), Js('killer'), Js('lander'), Js('leader'), Js('leaper'), Js('logger'), Js('maker'), Js('mender'), Js('picker'), Js('runner'), Js('shot'), Js('smasher'), Js('speaker'), Js('stalker'), Js('striker'), Js('tanner'), Js('twister'), Js('vigor'), Js('walker'), Js('wanderer'), Js('warrior'), Js('watcher'), Js('weaver'), Js('worker')]))
var.put('nmSF', Js([Js('Agu-Ul'), Js('Agu-V'), Js('Anakal'), Js('Apuna-M'), Js('Athun'), Js('Egena-V'), Js('Egum'), Js('Elan'), Js('Ganu-M'), Js('Gathak'), Js('Gean'), Js('Inul'), Js('Kalag'), Js('Kaluk'), Js('Katho-Ol'), Js('Kolae-G'), Js('Kolak'), Js('Kulan'), Js('Kulum'), Js('Lakum'), Js('Maluk'), Js('Munak'), Js('Muthal'), Js('Nalak'), Js('Nola-K'), Js('Nugal'), Js('Nulak'), Js('Ogol'), Js('Oveth'), Js('Thenal'), Js('Thul'), Js('Thunuk'), Js('Ugun'), Js('Uthenu-K'), Js('Vaimei-L'), Js('Valu-N'), Js('Vathun'), Js('Veom'), Js('Vuma-Th'), Js('Vunak')]))
var.put('nmSL', Js([Js('aga'), Js('ageane'), Js('akane'), Js('akanu'), Js('akume'), Js('alathi'), Js('amino'), Js('amune'), Js('anathi'), Js('atake'), Js('athai'), Js('athala'), Js('atho'), Js('avea'), Js('avi'), Js('avone'), Js('eaku'), Js('ekali'), Js('elo'), Js('iaga'), Js('iago'), Js('iala'), Js('iano'), Js('igala'), Js('igane'), Js('igano'), Js('igo'), Js('igone'), Js('ileana'), Js('ithino'), Js('olake'), Js('ugate'), Js('ugoni'), Js('ukane'), Js('ukate'), Js('ukena'), Js('ulane'), Js('upine'), Js('utha'), Js('uthea')]))
pass
pass
pass
pass


# Add lib to the module scope
dndGoliathNames = var.to_python()