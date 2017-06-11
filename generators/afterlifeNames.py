__all__ = ['afterlifeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm6'])
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
            if (var.get('tp')!=Js(1.0)):
                if (var.get('i')<Js(5.0)):
                    var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('name', ((((var.get('nm1').get(var.get('rnd0'))+var.get('nm2').get(var.get('rnd1')))+var.get('nm3').get(var.get('rnd2')))+var.get('nm4').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('name', (((Js('The ')+var.get('nm6').get(var.get('rnd')))+Js(' '))+var.get('nm7').get(var.get('rnd2'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(1.0)):
                    if (var.get('i')<Js(5.0)):
                        var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                        var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                        var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                        var.put('name', ((((var.get('nm8').get(var.get('rnd0'))+var.get('nm9').get(var.get('rnd1')))+var.get('nm10').get(var.get('rnd2')))+var.get('nm11').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4'))))
                    else:
                        var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                        var.put('name', (((Js('The ')+var.get('nm13').get(var.get('rnd')))+Js(' '))+var.get('nm14').get(var.get('rnd2'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm2', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('v'), Js('w'), Js('y'), Js('z'), Js('ch'), Js('sh'), Js('ph')]))
var.put('nm3', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('io'), Js('ae'), Js('eo')]))
var.put('nm4', Js([Js('g'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('bea'), Js('bis'), Js('bo'), Js('dah'), Js('del'), Js('den'), Js('dia'), Js('dore'), Js('dows'), Js('fey'), Js('gan'), Js('gish'), Js('gren'), Js('hala'), Js('hana'), Js('hel'), Js('hina'), Js('kala'), Js('kira'), Js('la'), Js('lara'), Js('laris'), Js('las'), Js('lear'), Js('less'), Js('lia'), Js('lis'), Js('lore'), Js('mani'), Js('mer'), Js('mia'), Js('mora'), Js('mu'), Js('muria'), Js('mus'), Js('naha'), Js('nahar'), Js('nara'), Js('nas'), Js('nase'), Js('nee'), Js('neer'), Js('nemo'), Js('nera'), Js('nero'), Js('ney'), Js('neya'), Js('nis'), Js('nor'), Js('nora'), Js('now'), Js('noya'), Js('nya'), Js('nyss'), Js('phae'), Js('phis'), Js('pyre'), Js('ra'), Js('raya'), Js('sira'), Js('sium'), Js('soah'), Js('sone'), Js('sora'), Js('tia'), Js('tira'), Js('tory'), Js('tu'), Js('vana'), Js('ven'), Js('vyre'), Js('wan'), Js('wen'), Js('wyn'), Js('zo')]))
var.put('nm6', Js([Js('Aerial'), Js('Ageless'), Js('Angelic'), Js('Argent'), Js('Astral'), Js('Azure'), Js('Beatific'), Js('Blessed'), Js('Blissful'), Js('Bright'), Js('Celestial'), Js('Cerulean'), Js('Champion'), Js('Chosen'), Js('Cloud'), Js('Cosmic'), Js('Divine'), Js('Dream'), Js('Elysian'), Js('Emerald'), Js('Empyreal'), Js('Empyrean'), Js('Eternal'), Js('Ethereal'), Js('Euphoric'), Js('Exalted'), Js('Glorious'), Js('Grand'), Js('Green'), Js('Hallowed'), Js('Happy'), Js('Harmonic'), Js('Heavenly'), Js('Hero'), Js('Holy'), Js('Hunting'), Js('Immortal'), Js('Infinite'), Js('Ivory'), Js('Jade'), Js('Light'), Js('Miracle'), Js('Olympian'), Js('Paradise'), Js('Pearly'), Js('Perpetual'), Js('Prime'), Js('Promised'), Js('Proven'), Js('Rainbow'), Js('Sapphire'), Js('Seraphic'), Js('Silver'), Js('Sky'), Js('Spirit'), Js('Spring'), Js('Sublime'), Js('Summer'), Js('Timeless'), Js('Utopia'), Js('Warrior'), Js('Wonder')]))
var.put('nm7', Js([Js('Domain'), Js('Empire'), Js('Field'), Js('Fields'), Js('Forest'), Js('Forests'), Js('Garden'), Js('Gardens'), Js('Ground'), Js('Grounds'), Js('Haven'), Js('Heaven'), Js('Heavens'), Js('Home'), Js('Kingdom'), Js('Land'), Js('Lands'), Js('Meadow'), Js('Meadows'), Js('Oasis'), Js('Pasture'), Js('Pastures'), Js('Plane'), Js('Planes'), Js('Realm'), Js('Sanctuary'), Js('Sanctum'), Js('World')]))
var.put('nm8', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm9', Js([Js('b'), Js('c'), Js('d'), Js('f'), Js('g'), Js('h'), Js('j'), Js('k'), Js('m'), Js('n'), Js('p'), Js('q'), Js('r'), Js('s'), Js('t'), Js('v'), Js('x'), Js('y'), Js('z'), Js('ch'), Js('sh'), Js('br'), Js('cr'), Js('dr'), Js('gr'), Js('kr'), Js('pr'), Js('str'), Js('tr'), Js('vr')]))
var.put('nm10', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('ea'), Js('ou'), Js('ua'), Js('iu')]))
var.put('nm11', Js([Js('n'), Js('r'), Js('s'), Js('g'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm12', Js([Js("'dem"), Js("'qar"), Js("'qira"), Js("'xin"), Js("'ziha"), Js('bax'), Js('byss'), Js('dahn'), Js('dell'), Js('dess'), Js('dis'), Js('doze'), Js('dues'), Js('gara'), Js('garn'), Js('gash'), Js('gor'), Js('grinn'), Js('hara'), Js('hull'), Js('huza'), Js('jura'), Js('kax'), Js('kaz'), Js('khan'), Js('kiru'), Js('kura'), Js('mas'), Js('mez'), Js('mixar'), Js('morta'), Js('muria'), Js('mus'), Js('muy'), Js('nahar'), Js('naq'), Js('naza'), Js('naze'), Js('nery'), Js('nex'), Js('nin'), Js('nixa'), Js('niza'), Js('no'), Js('nur'), Js('nura'), Js('ny'), Js('paqar'), Js('pax'), Js('pyre'), Js('qa'), Js('qore'), Js('qu'), Js('qur'), Js('ra'), Js('rax'), Js('siux'), Js('six'), Js('sour'), Js('sura'), Js('thor'), Js('tix'), Js('turan'), Js('vara'), Js('vax'), Js('vye'), Js('wax'), Js('wren'), Js('wyn'), Js('xan'), Js('zar'), Js('zo'), Js('zora'), Js('zya'), Js('zyss')]))
var.put('nm13', Js([Js('Abominable'), Js('Agony'), Js('Anguish'), Js('Ashen'), Js('Battle'), Js('Blasted'), Js('Bleak'), Js('Blind'), Js('Burning'), Js('Carnage'), Js('Conflict'), Js('Crimson'), Js('Dark'), Js('Dead'), Js('Delirium'), Js('Demon'), Js('Demonic'), Js('Devil'), Js('Diabolic'), Js('Dire'), Js('Dread'), Js('Ebon'), Js('Fever'), Js('Flaming'), Js('Foul'), Js('Frenzy'), Js('Gallow'), Js('Gloom'), Js('Grave'), Js('Gray'), Js('Grim'), Js('Horror'), Js('Infernal'), Js('Killing'), Js('Mad'), Js('Manic'), Js('Misery'), Js('Misty'), Js('Nether'), Js('Obsidian'), Js('Onyx'), Js('Penance'), Js('Plague'), Js('Punishment'), Js('Retribution'), Js('Rotten'), Js('Sanguine'), Js('Scarlet'), Js('Scourge'), Js('Shadow'), Js('Silent'), Js('Sinister'), Js('Skeletal'), Js('Slave'), Js('Somber'), Js('Sorrow'), Js('Struggle'), Js('Terror'), Js('Torment'), Js('Torture'), Js('Vicious'), Js('Vile'), Js('Wayward'), Js('Wicked')]))
var.put('nm14', Js([Js('Domain'), Js('Empire'), Js('Field'), Js('Fields'), Js('Ground'), Js('Grounds'), Js('Kingdom'), Js('Land'), Js('Lands'), Js('Pasture'), Js('Pastures'), Js('Plane'), Js('Planes'), Js('Realm'), Js('World')]))
pass
pass


# Add lib to the module scope
afterlifeNames = var.to_python()