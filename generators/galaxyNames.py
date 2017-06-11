__all__ = ['galaxyNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
                else:
                    if (var.get('i')<Js(8.0)):
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2'))))
                    else:
                        if (var.get('i')<Js(9.0)):
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('names', (((((var.get('nm5').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+Js('-'))+var.get('nm6').get(var.get('rnd3')))+var.get('nm6').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5'))))
                        else:
                            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                            var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                            var.put('names', ((((((var.get('nm5').get(var.get('rnd'))+var.get('nm5').get(var.get('rnd2')))+var.get('nm5').get(var.get('rnd3')))+Js(' '))+var.get('nm6').get(var.get('rnd4')))+var.get('nm6').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd5'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Alpha'), Js('Apus'), Js('Aquila'), Js('Ara'), Js('Beta'), Js('Canis'), Js('Carina'), Js('Comae'), Js('Corona'), Js('Crux'), Js('Delta'), Js('Draco'), Js('Epsilon'), Js('Gamma'), Js('Lambda'), Js('Lyra'), Js('Nemo'), Js('Omega'), Js('Omicron'), Js('Pavo'), Js('Proxima'), Js('Sagitta'), Js('Serpens'), Js('Sigma'), Js('Theta'), Js('Upsilon'), Js('Ursa'), Js('Vela'), Js('Virgo'), Js('Zeta'), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('Acallaris'), Js('Achelois'), Js('Adastreia'), Js('Aegialeus'), Js('Aegimius'), Js('Alatheia'), Js('Alcyoneus'), Js('Aldebaran'), Js('Amphiaraus'), Js('Anadeia'), Js('Andromeda'), Js('Aquarii'), Js('Arcturus'), Js('Aristaeus'), Js('Asteria'), Js('Asteropaios'), Js('Astraeus'), Js('Aurigae'), Js('Boreas'), Js('Borysthenis'), Js('Calesius'), Js('Capella'), Js('Cassiopeia'), Js('Centauri'), Js('Centaurus'), Js('Chronos'), Js('Cymopoleia'), Js('Dioscuri'), Js('Draconis'), Js('Eioneus'), Js('Eridani'), Js('Eridanus'), Js('Eubuleus'), Js('Euphorion'), Js('Eusebeia'), Js('Euthenia'), Js('Hemithea'), Js('Hyperbius'), Js('Hyperes'), Js('Hyperion'), Js('Icarius'), Js('Ichnaea'), Js('Ilioneus'), Js('Kentaurus'), Js('Leporis'), Js('Librae'), Js('Lyrae'), Js('Majoris'), Js('Miriandynus'), Js('Myrmidon'), Js('Nebula'), Js('Nemesis'), Js('Odysseus'), Js('Ophiuchi'), Js('Orion'), Js('Orionis'), Js('Orithyia'), Js('Palioxis'), Js('Peleus'), Js('Perileos'), Js('Perseus'), Js('Phoroneus'), Js('Polystratus'), Js('Porphyrion'), Js('Proioxis'), Js('Sagittarius'), Js('Sirius'), Js('Solymus'), Js('Zagreus'), Js('Zephyrus')]))
var.put('nm3', Js([Js('Abyss'), Js('Acorn'), Js('Arrowhead'), Js('Banana'), Js('Beansprout'), Js('Beanstalk'), Js('Bell'), Js('Blue Ribbon'), Js('Blueberry'), Js('Bottleneck'), Js('Bowl'), Js("Bull's Eye"), Js('Bullet'), Js('Butterfly'), Js("Cat's Ear"), Js("Cat's Eye"), Js('Catterpillar'), Js('Cherry'), Js('Chickpea'), Js('Clover'), Js('Coconut'), Js('Comet'), Js('Crescent'), Js("Crow's Feet"), Js('Crown'), Js('Dandelion'), Js('Diamond'), Js('Dragontooth'), Js('Droplet'), Js('Eagle Claw'), Js('Eggshell'), Js('Exploding'), Js('Eyebrow'), Js('Eyelash'), Js('Falling'), Js('Feather'), Js('Fern Leaf'), Js('Fingerprint'), Js('Fisheye'), Js('Fishscale'), Js('Flame'), Js('Football'), Js('Grain'), Js('Halo'), Js('Heart'), Js('Horseshoe'), Js('Hurricane'), Js('Icicle'), Js('Iris'), Js('Jellyfish'), Js('Kettle'), Js('Leaf'), Js('Lemon'), Js('Lightbulb'), Js('Lilypad'), Js("Lion's Mane"), Js("Lion's Tail"), Js('Maelstrom'), Js('Meridian'), Js('Mosaic'), Js('Mouse'), Js('Octopus'), Js('Oculus'), Js('Onion'), Js('Owl Head'), Js('Pear'), Js('Pepper'), Js("Pig's Tail"), Js('Pinecone'), Js('Ponytail'), Js('Potato'), Js('Red Ribbon'), Js('Rippled'), Js('Rose Petal'), Js('Sawblade'), Js('Seashell'), Js('Serpent'), Js("Serpent's Eye"), Js('Sharkfin'), Js('Sharktooth'), Js('Shield'), Js('Shooting Star'), Js('Snail Shell'), Js('Snowflake'), Js('Soap Bubble'), Js('Sparrow'), Js('Spearpoint'), Js('Spiderleg'), Js('Spiderweb'), Js('Spiral'), Js('Starfish'), Js('Strawberry'), Js('Teacup'), Js('Tiara'), Js('Tiger Paw'), Js('Tree Root'), Js('Tree Trunk'), Js('Turtle Shell'), Js('Vortex'), Js('Wave'), Js("Whale's Tail"), Js('Zodiac')]))
var.put('nm4', Js([Js('Nebula'), Js('Galaxy'), Js('Cloud'), Js('Star System')]))
var.put('nm5', Js([Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('X'), Js('Y'), Js('Z'), Js('')]))
var.put('nm6', Js([Js('0'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js('')]))
pass
pass


# Add lib to the module scope
galaxyNames = var.to_python()