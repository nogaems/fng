__all__ = ['fruitNames']

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
var.put('names5', Js([Js(' Fruit'), Js(' Nut'), Js(' Root'), Js(' Shoot'), Js('baco'), Js('bage'), Js('bana'), Js('bola'), Js('bosu'), Js('cado'), Js('can'), Js('ccoli'), Js('chee'), Js('chini'), Js('choke'), Js('cket'), Js('cona'), Js('cory'), Js('cot'), Js('cress'), Js('curi'), Js('damia'), Js('darin'), Js('dilla'), Js('dine'), Js('dish'), Js('dnut'), Js('flower'), Js('fruit'), Js('gette'), Js('guaro'), Js('gus'), Js('jube'), Js('kin'), Js('kra'), Js('ku'), Js('lal'), Js('lasan'), Js('le'), Js('lery'), Js('lini'), Js('lly'), Js('lon'), Js('loupe'), Js('mansi'), Js('mato'), Js('mber'), Js('mbi'), Js('mble'), Js('me'), Js('melo'), Js('mia'), Js('mmon'), Js('mon'), Js('mond'), Js('mquat'), Js('na'), Js('nach'), Js('nana'), Js('nate'), Js('nce'), Js('nda'), Js('ndu'), Js('ne'), Js('nge'), Js('nger'), Js('ngo'), Js('nip'), Js('ntine'), Js('nut'), Js('paw'), Js('paya'), Js('pe'), Js('per'), Js('ple'), Js('quat'), Js('quila'), Js('rac'), Js('ragus'), Js('rana'), Js('rang'), Js('rant'), Js('ranth'), Js('rd'), Js('rel'), Js('riac'), Js('rian'), Js('ricot'), Js('riman'), Js('rin'), Js('rind'), Js('rine'), Js('rlan'), Js('ro'), Js('rola'), Js('rra'), Js('rrot'), Js('rry'), Js('rula'), Js('san'), Js('shew'), Js('snip'), Js('tain'), Js('tato'), Js('taya'), Js('te'), Js('til'), Js('tillo'), Js('tine'), Js('to'), Js('tron'), Js('tuce'), Js('va'), Js('ve'), Js('ves'), Js('wan'), Js('wesh'), Js('wi'), Js('ya'), Js('yote')]))
var.put('names6', Js([Js('Abyss'), Js('Angel'), Js('Arctic'), Js('Ash'), Js('Autumn'), Js('Baby'), Js('Beach'), Js('Bitter'), Js('Bittersweet'), Js('Black'), Js('Blood'), Js('Blue'), Js('Bronze'), Js('Brown'), Js('Bush'), Js('Candy'), Js('Cave'), Js('Cavern'), Js('Cinder'), Js('Cliff'), Js('Crimson'), Js('Daydream'), Js('Demon'), Js('Desert'), Js('Dessert'), Js('Devil'), Js('Dew'), Js('Dragon'), Js('Drake'), Js('Dream'), Js('Earth'), Js('Eastern'), Js('Elder'), Js('Elephant'), Js('Ember'), Js('Fade'), Js('False'), Js('Fire'), Js('Flowered'), Js('Flux'), Js('Forest'), Js('Golden'), Js('Green'), Js('Ground'), Js('Hairless'), Js('Hairy'), Js('Hard'), Js('Hate'), Js('Hazel'), Js('Heart'), Js('Ice'), Js('Island'), Js('Lake'), Js('Love'), Js('Mage'), Js('Mammoth'), Js('Mellow'), Js('Mimic'), Js('Miracle'), Js('Mist'), Js('Mock'), Js('Monster'), Js('Moon'), Js('Mountain'), Js('Mud'), Js('Mutant'), Js('Mystery'), Js('Mystical'), Js('Native'), Js('Night'), Js('Nightmare'), Js('Northern'), Js('Ocean'), Js('Peace'), Js('Pigmy'), Js('Pygmy'), Js('Rain'), Js('Red'), Js('River'), Js('Rose'), Js('Salty'), Js('Sanguine'), Js('Sea'), Js('Shimmer'), Js('Silk'), Js('Silver'), Js('Smelly'), Js('Soft'), Js('Sorrow'), Js('Sour'), Js('Southern'), Js('Spring'), Js('Star'), Js('Storm'), Js('Summer'), Js('Sun'), Js('Swamp'), Js('Sweet'), Js('Thorn'), Js('Thorny'), Js('Thunder'), Js('Tiger'), Js('Tropical'), Js('Tundra'), Js('Violet'), Js('Void'), Js('Water'), Js('Western'), Js('White'), Js('Wild'), Js('Winter'), Js('Wonder'), Js('Wood'), Js('Yellow'), Js('Young')]))
var.put('names7', Js([Js('Acerola'), Js('Almond'), Js('Amaranth'), Js('Apple'), Js('Apricot'), Js('Artichoke'), Js('Asparagus'), Js('Avocado'), Js('Babaco'), Js('Bacuri'), Js('Bael'), Js('Banana'), Js('Bean'), Js('Berry'), Js('Bilimbi'), Js('Bolwarra'), Js('Boquila'), Js('Bramble'), Js('Breadnut'), Js('Broccoli'), Js('Broccolini'), Js('Cabbage'), Js('Calamansi'), Js('Cantaloupe'), Js('Carambola'), Js('Carrot'), Js('Cashew'), Js('Cauliflower'), Js('Cawesh'), Js('Celeriac'), Js('Celery'), Js('Celtuce'), Js('Ceriman'), Js('Chayote'), Js('Cherry'), Js('Chestnut'), Js('Chicory'), Js('Chives'), Js('Choy'), Js('Citron'), Js('Clementine'), Js('Cocona'), Js('Coconut'), Js('Courgette'), Js('Cucumber'), Js('Currant'), Js('Date'), Js('Dill'), Js('Duku'), Js('Durian'), Js('Fig'), Js('Fruit'), Js('Ginger'), Js('Gourd'), Js('Granadilla'), Js('Grape'), Js('Grapefruit'), Js('Guanabana'), Js('Guarana'), Js('Guava'), Js('Hazelnut'), Js('Jujube'), Js('Kabosu'), Js('Kale'), Js('Kiwi'), Js('Korlan'), Js('Kumquat'), Js('Laurel'), Js('Leek'), Js('Lemon'), Js('Lentil'), Js('Lettuce'), Js('Lillypilly'), Js('Lime'), Js('Loquat'), Js('Lychee'), Js('Macadamia'), Js('Mandarin'), Js('Mango'), Js('Mangosteen'), Js('Marang'), Js('Marula'), Js('Melon'), Js('Morinda'), Js('Mundu'), Js('Muscadine'), Js('Nectarine'), Js('Okra'), Js('Olive'), Js('Onion'), Js('Orange'), Js('Papaya'), Js('Paracress'), Js('Parsnip'), Js('Pawpaw'), Js('Pea'), Js('Peach'), Js('Pear'), Js('Pecan'), Js('Pepper'), Js('Persimmon'), Js('Pitaya'), Js('Plantain'), Js('Plum'), Js('Pomegranate'), Js('Pomelo'), Js('Pommerac'), Js('Potato'), Js('Prune'), Js('Pulasan'), Js('Pumpkin'), Js('Quince'), Js('Radish'), Js('Rocket'), Js('Root'), Js('Rowan'), Js('Saguaro'), Js('Salal'), Js('Spinach'), Js('Sprout'), Js('Squash'), Js('Tamarind'), Js('Tangerine'), Js('Tomatillo'), Js('Tomato'), Js('Turnip'), Js('Walnut'), Js('Yam'), Js('Zucchini')]))
pass
pass


# Add lib to the module scope
fruitNames = var.to_python()