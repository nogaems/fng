__all__ = ['magicTrees']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    if (var.get('rnd')>Js(9.0)):
                        while (var.get('rnd3')>Js(9.0)):
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((((var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm7').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abyss'), Js('Aching'), Js('Angel'), Js("Angel's"), Js('Anxious'), Js('Aquatic'), Js('Arching'), Js('Aromatic'), Js('Assassin'), Js('Banshee'), Js('Barbed'), Js('Bitter'), Js('Black'), Js('Bleak'), Js('Blight'), Js('Blister'), Js('Blood'), Js('Blue'), Js('Bone'), Js('Boomerang'), Js('Bouncing'), Js('Bright'), Js('Bronze'), Js('Candy'), Js('Cave'), Js('Chilling'), Js('Cliff'), Js('Cold'), Js('Corrupt'), Js('Corrupted'), Js('Corrupting'), Js('Coughing'), Js('Crawling'), Js('Creeping'), Js('Dancing'), Js('Dawn'), Js('Deadly'), Js("Death's"), Js('Delicious'), Js('Demon'), Js("Demon's"), Js("Devil's"), Js('Dim'), Js('Dire'), Js('Dragon'), Js('Drifting'), Js('Drowsy'), Js('Dusk'), Js('Dwarf'), Js('Eagle'), Js('Fake'), Js('Fanged'), Js('Fatigue'), Js('Fear'), Js('Fearful'), Js('Fever'), Js('Fire'), Js('Fjord'), Js('Flying'), Js('Fragrant'), Js('Frozen'), Js('Funeral'), Js('Funky'), Js('Ghost'), Js('Giant'), Js('Glacier'), Js('Glowing'), Js('Golden'), Js('Grand'), Js('Grave'), Js('Gray'), Js('Green'), Js('Grim'), Js('Grumpy'), Js('Hammer'), Js('Happy'), Js('Harmless'), Js('Hate'), Js('Hidden'), Js('Hollow'), Js('Horned'), Js('Hot'), Js('Hovering'), Js('Humble'), Js('Ice'), Js('Imperial'), Js('Infecting'), Js('Invisible'), Js('Island'), Js('Itching'), Js('Jealous'), Js('Jester'), Js('Joyful'), Js("King's"), Js('Lethal'), Js("Life's"), Js('Lion'), Js('Love'), Js('Lunar'), Js("Mage's"), Js('Majestic'), Js('Mammoth'), Js('Marsh'), Js("Mercy's"), Js('Mimic'), Js('Mock'), Js('Mocking'), Js("Monk's"), Js('Moon'), Js('Mound'), Js('Mountain'), Js('Nasty'), Js('Naughty'), Js('Nervous'), Js('Noxious'), Js('Ocean'), Js('Orange'), Js('Ordinary'), Js('Perfumed'), Js('Pest'), Js('Phantom'), Js('Pink'), Js('Piranha'), Js('Pixy'), Js('Plague'), Js('Pleasant'), Js('Poisonous'), Js('Prancing'), Js('Putrid'), Js('Pygmy'), Js("Queen's"), Js('Quiet'), Js('Rare'), Js('Rash'), Js('Raven'), Js('Red'), Js('Regal'), Js('Restoration'), Js('River'), Js('Rotten'), Js('Royal'), Js('Sad'), Js('Salty'), Js('Sanguine'), Js('Savage'), Js('Scented'), Js('Screaming'), Js('Sentient'), Js('Serpent'), Js('Shadow'), Js('Shield'), Js('Shocking'), Js('Shrine'), Js('Shy'), Js('Silver'), Js('Skeletal'), Js('Skulking'), Js('Sleeping'), Js('Sleepy'), Js('Smelly'), Js('Smooth'), Js('Sneeze'), Js('Sneezing'), Js('Solar'), Js('Sore'), Js('Sour'), Js('Spicy'), Js('Spiky'), Js('Spirit'), Js('Spitfire'), Js('Stink'), Js('Stinking'), Js('Sugar'), Js('Sun'), Js('Sunny'), Js('Swamp'), Js('Sweet'), Js('Tall'), Js('Tangle'), Js('Tangled'), Js('Taunting'), Js('Tickle'), Js('Toxic'), Js('Twilight'), Js('Twisted'), Js('Urban'), Js('Venomous'), Js('Vision'), Js('Volcano'), Js('Walking'), Js('Warm'), Js('Weeping'), Js('Whisper'), Js('White'), Js('Whomping'), Js('Wicked'), Js('Wild'), Js('Wisdom'), Js('Wolf'), Js('Yellow')]))
var.put('nm2', Js([Js('Acacia'), Js('Alder'), Js('Ash'), Js('Aspen'), Js('Azalea'), Js('Balsa'), Js('Bamboo'), Js('Baobab'), Js('Bayonet'), Js('Beech'), Js('Birch'), Js('Box'), Js('Buckeye'), Js('Buckthorn'), Js('Bunya'), Js('Bush'), Js('Cassava'), Js('Catalpa'), Js('Cedar'), Js('Conifer'), Js('Cycad'), Js('Cypress'), Js('Elder'), Js('Elm'), Js('Eucalyptus'), Js('Fir'), Js('Hawthorn'), Js('Hazel'), Js('Hemlock'), Js('Hickory'), Js('Holly'), Js('Hornbeam'), Js('Juniper'), Js('Larch'), Js('Leaf'), Js('Locust'), Js('Magnolia'), Js('Mahogany'), Js('Mangrove'), Js('Maple'), Js('Medlar'), Js('Milkbark'), Js('Oak'), Js('Oleander'), Js('Palm'), Js('Palmetto'), Js('Persimmon'), Js('Pine'), Js('Poplar'), Js('Privet'), Js('Rhododendron'), Js('Rowan'), Js('Sequoia'), Js('Spruce'), Js('Strongbark'), Js('Sumac'), Js('Sycamore'), Js('Tree'), Js('Viburnum'), Js('Willow'), Js('Wood'), Js('Yew'), Js('Yucca')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ei'), Js('eo'), Js('ae'), Js('ai'), Js('ia'), Js('io'), Js('ua'), Js('aa'), Js('ee'), Js('oo'), Js('ou'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bl'), Js('br'), Js('ch'), Js('chr'), Js('cl'), Js('cr'), Js('dl'), Js('dr'), Js('fl'), Js('fr'), Js('fy'), Js('gl'), Js('gr'), Js('kl'), Js('kn'), Js('kr'), Js('ph'), Js('phr'), Js('pl'), Js('pr'), Js('sc'), Js('sh'), Js('shr'), Js('sl'), Js('sm'), Js('sn'), Js('sp'), Js('sr'), Js('str'), Js('th'), Js('thr'), Js('tr'), Js('vl')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ei'), Js('eo'), Js('ae'), Js('ai'), Js('ia'), Js('io'), Js('ua'), Js('aa'), Js('ee'), Js('oo'), Js('ou')]))
var.put('nm6', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('x'), Js('y'), Js('z'), Js('bb'), Js('bd'), Js('bg'), Js('bl'), Js('br'), Js('bs'), Js('cc'), Js('ch'), Js('chr'), Js('cl'), Js('cr'), Js('dd'), Js('df'), Js('dg'), Js('dl'), Js('dr'), Js('ds'), Js('dt'), Js('fd'), Js('ff'), Js('fg'), Js('fl'), Js('fm'), Js('fn'), Js('fp'), Js('fr'), Js('fy'), Js('gd'), Js('gg'), Js('ght'), Js('gl'), Js('gr'), Js('gth'), Js('hh'), Js('hl'), Js('hm'), Js('hn'), Js('hs'), Js('ht'), Js('kd'), Js('kk'), Js('kl'), Js('km'), Js('kn'), Js('kr'), Js('lb'), Js('ld'), Js('lf'), Js('lg'), Js('lk'), Js('ll'), Js('lm'), Js('ln'), Js('lp'), Js('ls'), Js('lt'), Js('ly'), Js('mb'), Js('md'), Js('mf'), Js('mk'), Js('ml'), Js('mm'), Js('mn'), Js('mp'), Js('ms'), Js('my'), Js('nc'), Js('nd'), Js('nf'), Js('ng'), Js('nk'), Js('nl'), Js('nm'), Js('nn'), Js('np'), Js('ns'), Js('nt'), Js('ny'), Js('ph'), Js('phr'), Js('pl'), Js('pp'), Js('pr'), Js('ql'), Js('qr'), Js('qs'), Js('rc'), Js('rd'), Js('rf'), Js('rg'), Js('rh'), Js('rk'), Js('rl'), Js('rm'), Js('rn'), Js('rp'), Js('rr'), Js('rs'), Js('rsh'), Js('rt'), Js('rth'), Js('rw'), Js('sb'), Js('sc'), Js('sd'), Js('sf'), Js('sg'), Js('sh'), Js('shr'), Js('sk'), Js('sl'), Js('sm'), Js('sn'), Js('sp'), Js('sr'), Js('ss'), Js('st'), Js('str'), Js('sw'), Js('sy'), Js('th'), Js('thr'), Js('tr'), Js('tt'), Js('vl'), Js('zh'), Js('zl'), Js('zr'), Js('zz')]))
var.put('nm7', Js([Js('ab'), Js('ac'), Js('acca'), Js('acia'), Js('alea'), Js('an'), Js('ander'), Js('ant'), Js('any'), Js('ar'), Js('arch'), Js('ark'), Js('ava'), Js('eaf'), Js('eam'), Js('eech'), Js('en'), Js('er'), Js('ess'), Js('et'), Js('etto'), Js('ew'), Js('eye'), Js('ifer'), Js('immon'), Js('ine'), Js('iper'), Js('irch'), Js('ock'), Js('olia'), Js('on'), Js('onet'), Js('ood'), Js('ore'), Js('orn'), Js('ory'), Js('ove'), Js('ow'), Js('uce'), Js('um'), Js('us')]))
pass
pass


# Add lib to the module scope
magicTrees = var.to_python()