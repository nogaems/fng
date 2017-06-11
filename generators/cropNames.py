__all__ = ['cropNames']

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
            if (var.get('i')<Js(2.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                var.put('names', (((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names5').get(var.get('rnd4'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    if (var.get('rnd3')>Js(9.0)):
                        while (var.get('rnd5')>Js(9.0)):
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length'))))
                    var.put('names', (((((var.get('names1').get(var.get('rnd'))+var.get('names2').get(var.get('rnd2')))+var.get('names3').get(var.get('rnd3')))+var.get('names4').get(var.get('rnd4')))+var.get('names3').get(var.get('rnd5')))+var.get('names5').get(var.get('rnd6'))))
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
var.put('names1', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('names2', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('str'), Js('tr'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('kl'), Js('pl'), Js('sl'), Js('ch'), Js('ph'), Js('sh')]))
var.put('names3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ao'), Js('ee'), Js('oo'), Js('io'), Js('eo'), Js('ou')]))
var.put('names4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('z'), Js('br'), Js('cr'), Js('dr'), Js('fr'), Js('gr'), Js('kr'), Js('pr'), Js('str'), Js('tr'), Js('bl'), Js('cl'), Js('fl'), Js('gl'), Js('kl'), Js('pl'), Js('sl'), Js('ch'), Js('ph'), Js('sh'), Js('bb'), Js('cc'), Js('dd'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt')]))
var.put('names5', Js([Js(' Berry'), Js(' Root'), Js(' Fruit'), Js(' Grass'), Js(' Wheat'), Js(' Seed'), Js(' Pea'), Js(' Nut'), Js(' Pepper'), Js(' Flower'), Js(' Bean'), Js('bage'), Js('bber'), Js('ber'), Js('ble'), Js('ca'), Js('can'), Js('cane'), Js('cao'), Js('ce'), Js('ch'), Js('chin'), Js('chio'), Js('cra'), Js('der'), Js('dis'), Js('drin'), Js('ds'), Js('flower'), Js('gar'), Js('ger'), Js('go'), Js('gus'), Js('kin'), Js('la'), Js('lar'), Js('le'), Js('ley'), Js('lic'), Js('lion'), Js('live'), Js('lla'), Js('llar'), Js('llion'), Js('lon'), Js('lone'), Js('mat'), Js('mber'), Js('me'), Js('meg'), Js('mel'), Js('melo'), Js('men'), Js('min'), Js('mon'), Js('mond'), Js('mp'), Js('na'), Js('nach'), Js('nder'), Js('ne'), Js('nel'), Js('nell'), Js('nelo'), Js('nger'), Js('ngin'), Js('ngo'), Js('ni'), Js('nip'), Js('nna'), Js('nnel'), Js('nola'), Js('nt'), Js('ntin'), Js('nto'), Js('nut'), Js('pe'), Js('per'), Js('phe'), Js('pper'), Js('ra'), Js('rab'), Js('rey'), Js('rgus'), Js('riak'), Js('rin'), Js('rine'), Js('rli'), Js('rlin'), Js('rn'), Js('rom'), Js('rot'), Js('rry'), Js('ry'), Js('sam'), Js('same'), Js('save'), Js('seed'), Js('sh'), Js('sil'), Js('sley'), Js('ss'), Js('star'), Js('ster'), Js('tarin'), Js('te'), Js('terd'), Js('tine'), Js('to'), Js('tro'), Js('ts'), Js('tus'), Js('va'), Js('ve'), Js('ver'), Js('x'), Js('ya'), Js('yoca'), Js('yot'), Js('ze')]))
var.put('names6', Js([Js('Abyss'), Js('Angel'), Js('Arctic'), Js('Arrow'), Js('Ash'), Js('Autumn'), Js('Bitter'), Js('Black'), Js('Blister'), Js('Blood'), Js('Blue'), Js('Broad'), Js('Brown'), Js('Bruise'), Js('Candy'), Js('Cave'), Js('Cavern'), Js('Cinder'), Js('Cliff'), Js('Demon'), Js('Devil'), Js('Dragon'), Js('Drake'), Js('Dream'), Js('Earth'), Js('Ember'), Js('Emerald'), Js('Fade'), Js('Fire'), Js('Flux'), Js('Forest'), Js('Golden'), Js('Ground'), Js('Guinea'), Js('Hate'), Js('Hazel'), Js('Heart'), Js('Hybernation'), Js('Hybrid'), Js('Ice'), Js('Ivory'), Js('Jade'), Js("King's"), Js('Knot'), Js('Lake'), Js('Love'), Js('Mage'), Js('Mammoth'), Js('Mellow'), Js('Mercy'), Js('Moon'), Js('Mountain'), Js('Mud'), Js('Ocean'), Js('Peace'), Js('Pygmy'), Js('Rain'), Js('Red'), Js('River'), Js('Ruby'), Js('Sanguine'), Js('Sapphire'), Js('Sea'), Js('Shimmer'), Js('Silk'), Js('Snowy'), Js('Sorrow'), Js('Sour'), Js('Spring'), Js('Star'), Js('Stinky'), Js('Storm'), Js('Summer'), Js('Sun'), Js('Swamp'), Js('Sweet'), Js('Thorn'), Js('Thunder'), Js('Tiger'), Js('Tundra'), Js('Venom'), Js('Viper'), Js('Void'), Js('Water'), Js('White'), Js('Wild'), Js('Winter'), Js('Wolf'), Js('Worm'), Js('Yellow')]))
var.put('names7', Js([Js('Almond'), Js('Apple'), Js('Asparagus'), Js('Banana'), Js('Barley'), Js('Basil'), Js('Beans'), Js('Beets'), Js('Broccoli'), Js('Cabbage'), Js('Cacao'), Js('Cane'), Js('Canola'), Js('Cardamom'), Js('Carrot'), Js('Cassava'), Js('Cauliflower'), Js('Celeriac'), Js('Celery'), Js('Chayote'), Js('Cherry'), Js('Chili'), Js('Cilantro'), Js('Clementine'), Js('Clover'), Js('Coconut'), Js('Coffee'), Js('Collard'), Js('Corn'), Js('Cotton'), Js('Cress'), Js('Cucumber'), Js('Date'), Js('Dill'), Js('Fennel'), Js('Fig'), Js('Flax'), Js('Garlic'), Js('Ginger'), Js('Grape'), Js('Grass'), Js('Guava'), Js('Hemp'), Js('Henna'), Js('Hop'), Js('Jasmine'), Js('Jute'), Js('Kale'), Js('Kohlrabi'), Js('Lavender'), Js('Leek'), Js('Lemon'), Js('Lettuce'), Js('Lime'), Js('Mace'), Js('Maize'), Js('Mandarin'), Js('Mango'), Js('Melon'), Js('Mint'), Js('Mushroom'), Js('Mustard'), Js('Nectarine'), Js('Nutmeg'), Js('Nuts'), Js('Oats'), Js('Okra'), Js('Olive'), Js('Onion'), Js('Papaya'), Js('Parsley'), Js('Parsnip'), Js('Pea'), Js('Peach'), Js('Peanut'), Js('Pear'), Js('Pecan'), Js('Pepper'), Js('Pistachio'), Js('Plum'), Js('Pomelo'), Js('Potato'), Js('Prune'), Js('Pumpkin'), Js('Radish'), Js('Rice'), Js('Root'), Js('Rubber'), Js('Rye'), Js('Safflower'), Js('Scallion'), Js('Seeds'), Js('Sesame'), Js('Soy'), Js('Spinach'), Js('Sprouts'), Js('Squash'), Js('Sugar'), Js('Tangerine'), Js('Tapioca'), Js('Tea'), Js('Tomato'), Js('Turnip'), Js('Vanilla'), Js('Wheat'), Js('Yam'), Js('Zucchini')]))
pass
pass


# Add lib to the module scope
cropNames = var.to_python()