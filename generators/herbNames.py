__all__ = ['herbNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names4', 'nameGen', 'names6', 'names5', 'names2', 'names3', 'names1', 'names7'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                if (var.get('rnd')>Js(41.0)):
                    while (var.get('rnd3')<Js(11.0)):
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('names', ((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names4').get(var.get('rnd4')))+var.get('names5').get(var.get('rnd5'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7').get('length'))))
                var.put('names', ((var.get('names6').get(var.get('rnd'))+Js(' '))+var.get('names7').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('ch'), Js('sh'), Js('ph'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('pr'), Js('str'), Js('vr'), Js('wr'), Js(''), Js('bl'), Js('cl'), Js('gl'), Js('fl'), Js('kl'), Js('pl'), Js('sl')]))
var.put('names2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('names3', Js([Js('sh'), Js('ch'), Js('ph'), Js('cr'), Js('dr'), Js('gr'), Js('str'), Js('cl'), Js('gl'), Js('kl'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bb'), Js('cc'), Js('dd'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt')]))
var.put('names4', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('eo'), Js('ia'), Js('io')]))
var.put('names5', Js([Js(' Bud'), Js(' Grain'), Js(' Grass'), Js(' Husk'), Js(' Kernel'), Js(' Leaf'), Js(' Nut'), Js(' Petal'), Js(' Root'), Js(' Shoot'), Js(' Spore'), Js(' Stalk'), Js('bacca'), Js('bi'), Js('ce'), Js('cely'), Js('cory'), Js('cress'), Js('damom'), Js('damon'), Js('der'), Js('fras'), Js('frass'), Js('fron'), Js('gane'), Js('gano'), Js('ge'), Js('gella'), Js('ger'), Js('gon'), Js('grass'), Js('jora'), Js('joram'), Js('ka'), Js('kam'), Js('kawa'), Js('lantro'), Js('lary'), Js('lery'), Js('ley'), Js('li'), Js('lic'), Js('lica'), Js('lla'), Js('lt'), Js('ltro'), Js('me'), Js('meg'), Js('meric'), Js('min'), Js('mine'), Js('misa'), Js('mom'), Js('mon'), Js('mric'), Js('namon'), Js('nder'), Js('nel'), Js('nip'), Js('nis'), Js('nise'), Js('ntro'), Js('nut'), Js('para'), Js('per'), Js('rage'), Js('ram'), Js('ran'), Js('raway'), Js('rel'), Js('rian'), Js('ric'), Js('rica'), Js('rice'), Js('rika'), Js('rise'), Js('rlic'), Js('ron'), Js('rrel'), Js('rry'), Js('rway'), Js('ry'), Js('sabi'), Js('sbi'), Js('seed'), Js('shell'), Js('shil'), Js('sia'), Js('sil'), Js('sley'), Js('so'), Js('sop'), Js('ssop'), Js('th'), Js('tro'), Js('ve'), Js('ves'), Js('vil'), Js('way'), Js('yenne')]))
var.put('names6', Js([Js('Abyss'), Js('Angel'), Js('Arctic'), Js('Ash'), Js('Assassin'), Js('Autumn'), Js('Bitter'), Js('Black'), Js('Blister'), Js('Blood'), Js('Blue'), Js('Brown'), Js('Bruise'), Js('Candy'), Js('Cave'), Js('Cavern'), Js('Cinder'), Js('Cliff'), Js('Demon'), Js('Devil'), Js('Dragon'), Js('Drake'), Js('Dream'), Js('Earth'), Js('Elephant'), Js('Ember'), Js('Emerald'), Js('Fade'), Js('Fire'), Js('Flux'), Js('Forest'), Js('Golden'), Js('Hate'), Js('Hazel'), Js('Heart'), Js('Hybernation'), Js('Ice'), Js('Ivory'), Js('Jade'), Js("King's"), Js('Knettle'), Js('Knot'), Js('Lake'), Js('Love'), Js('Mage'), Js('Mammoth'), Js('Mellow'), Js('Mercy'), Js("Monk's"), Js('Moon'), Js('Mountain'), Js('Mud'), Js('Ocean'), Js('Orange'), Js('Peace'), Js('Pearl'), Js('Pygmy'), Js("Queen's"), Js('Rain'), Js('Red'), Js('River'), Js('Ruby'), Js('Sanguine'), Js('Sapphire'), Js('Sea'), Js('Shimmer'), Js('Silk'), Js('Snowy'), Js('Sorrow'), Js('Sour'), Js('Spark'), Js('Spring'), Js('Star'), Js('Stinky'), Js('Storm'), Js('Summer'), Js('Sun'), Js('Swamp'), Js('Sweet'), Js('Thorn'), Js('Thunder'), Js('Tiger'), Js('Tundra'), Js('Venom'), Js('Viper'), Js('Void'), Js('Water'), Js('White'), Js('Wild'), Js('Winter'), Js("Witch's"), Js('Wolf'), Js('Worm'), Js('Yellow')]))
var.put('names7', Js([Js('Angelica'), Js('Anise'), Js('Aniseed'), Js('Avens'), Js('Barberry'), Js('Bark'), Js('Basil'), Js('Bay Leaf'), Js('Blossom'), Js('Borage'), Js('Caraway'), Js('Cardamom'), Js('Cassia'), Js('Catnip'), Js('Celery'), Js('Chervil'), Js('Chicory'), Js('Chives'), Js('Cilantro'), Js('Cinnamon'), Js('Clary'), Js('Clove'), Js('Coriander'), Js('Cress'), Js('Cudweed'), Js('Culantro'), Js('Cumin'), Js('Curry Leaf'), Js('Dill'), Js('Dill Seed'), Js('Fennel'), Js('Fenugreek'), Js('Flower'), Js('Galangal'), Js('Galingale'), Js('Garlic'), Js('Ginger'), Js('Grains'), Js('Grass'), Js('Herb'), Js('Hyssop'), Js('Lavender'), Js('Leaf'), Js('Leaves'), Js('Licorice'), Js('Lovage'), Js('Mace'), Js('Mallow'), Js('Marjoram'), Js('Mint'), Js('Moss'), Js('Mustard'), Js('Nigella'), Js('Nutmeg'), Js('Oregano'), Js('Paprika'), Js('Parsley'), Js('Pepper'), Js('Peppermint'), Js('Petal'), Js('Quassia'), Js('Root'), Js('Rosemary'), Js('Rue'), Js('Safflower'), Js('Saffron'), Js('Sage'), Js('Salt'), Js('Sassafras'), Js('Savory'), Js('Seed'), Js('Shiso'), Js('Sorrel'), Js('Spearmint'), Js('Spice'), Js('Sumac'), Js('Tarragon'), Js('Thyme'), Js('Turmeric'), Js('Vanilla'), Js('Bloom'), Js('Tea Leaf'), Js('Ivy'), Js('Weed'), Js('Creeper'), Js('Vine')]))
pass
pass


# Add lib to the module scope
herbNames = var.to_python()