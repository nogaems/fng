__all__ = ['martialArtDescriptions']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm14', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['rnd15', 'rnd11', 'rnd8', 'name', 'rnd14', 'name3', 'rnd2', 'br', 'name2', 'rnd5', 'rnd4', 'rnd6b', 'rnd7', 'rnd5b', 'result', 'rnd6', 'rnd13', 'rnd3', 'rnd10', 'rnd9', 'rnd12', 'rnd1'])
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    if (var.get('rnd2')<Js(3.0)):
        while (var.get('rnd3')>Js(11.0)):
            var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
        while (var.get('rnd4')>Js(19.0)):
            var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    else:
        if (var.get('rnd2')>Js(5.0)):
            while (var.get('rnd3')<Js(12.0)):
                var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
            while (var.get('rnd4')<Js(20.0)):
                var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd5b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    while PyJsStrictEq(var.get('rnd5'),var.get('rnd5b')):
        var.put('rnd5b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd6b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    while PyJsStrictEq(var.get('rnd6'),var.get('rnd6b')):
        var.put('rnd6b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length')))))
    def PyJs_LONG_0_(var=var):
        return ((((((((((((var.get('nm1').get(var.get('rnd1'))+Js(' is a '))+var.get('nm2').get(var.get('rnd2')))+Js(' martial art that focuses on '))+var.get('nm3').get(var.get('rnd3')))+Js(' your opponent '))+var.get('nm4').get(var.get('rnd4')))+Js('. The primary focus lies on both '))+var.get('nm5').get(var.get('rnd5')))+Js(' and '))+var.get('nm5').get(var.get('rnd5b')))+Js(' and it often relies on the '))+var.get('nm6').get(var.get('rnd6')))
    var.put('name', ((((PyJs_LONG_0_()+Js(' and '))+var.get('nm6').get(var.get('rnd6b')))+var.get('nm7').get(var.get('rnd7')))+Js('.')))
    def PyJs_LONG_1_(var=var):
        return ((((((((((((((Js('The biggest strength of ')+var.get('nm1').get(var.get('rnd1')))+Js(' is '))+var.get('nm8').get(var.get('rnd8')))+Js('. By '))+var.get('nm9').get(var.get('rnd9')))+Js(' the '))+var.get('nm11').get(var.get('rnd11')))+Js(' of '))+var.get('nm10').get(var.get('rnd10')))+Js(' your opponent '))+var.get('nm12').get(var.get('rnd12')))+Js(', '))+var.get('nm13').get(var.get('rnd13')))+Js('.'))
    var.put('name2', PyJs_LONG_1_())
    var.put('name3', ((((((Js('On the other hand the biggest weakness of ')+var.get('nm1').get(var.get('rnd1')))+Js(' is '))+var.get('nm14').get(var.get('rnd14')))+Js(' '))+var.get('nm15').get(var.get('rnd15')))+Js('.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(5.0)):
        try:
            pass
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Bolenoe'), Js('Chiknu'), Js('Chorea-Crava'), Js('Chu Gwiara'), Js('Chukmul'), Js('Cogre Kenku'), Js('Croonkenzu'), Js('Crucho Bistia'), Js('Deochaju'), Js('Dintingaa'), Js('Dorohla'), Js('Dunari'), Js('Eenshi'), Js('Endia'), Js('Geche Gimpia'), Js('Goupo Vuati'), Js('Grupeo Chuto'), Js('Guthwou'), Js('Hanhim'), Js('Hintihte'), Js('Injashi'), Js('Jorin'), Js('Jothe'), Js('Ju-Monbung'), Js('Kekil'), Js('Khrastao'), Js('Kukmakyu'), Js('Kutte'), Js('Lantirmai'), Js('Let Aeshia'), Js('Maihtihta'), Js('Mindihlu'), Js('Neacela'), Js('Nejaesh'), Js('Nevoo-Crinchi'), Js('Ngairmeni'), Js('Ngobambo'), Js('Nhobyai'), Js('Nhunshulo'), Js('Nogwaimbo'), Js('Nunde-Gagri'), Js('Ochku'), Js('Ostundo'), Js('Oukwom Hwum'), Js('Saambermo'), Js('Stipu Iku'), Js('Taigwambu'), Js('Tosale'), Js('Voitse'), Js('Vusi')]))
var.put('nm2', Js([Js('defensive'), Js('mostly defensive'), Js('strictly defensive'), Js('defensive and offensive'), Js('partially offensive and partially defensive'), Js('mixed'), Js('offensive'), Js('mostly offensive'), Js('strictly offensive')]))
var.put('nm3', Js([Js('disabling'), Js('disenabling'), Js('subduing'), Js('exhausting'), Js('immobilizing'), Js('incapacitating'), Js('knocking out'), Js('paralyzing'), Js('taking down'), Js('outmaneuvering'), Js('undermining'), Js('defeating'), Js('crushing'), Js('overpowering'), Js('overwhelming'), Js('overthrowing'), Js('beating'), Js('decimating'), Js('demolishing'), Js('thrashing'), Js('crippling'), Js('clobbering'), Js('steamrolling')]))
var.put('nm4', Js([Js('with a minimum expenditure of your own energy'), Js('through quick and very specific movements'), Js('by utilizing pressure points on the body'), Js("by taking advantage of every opening in your opponent's defense"), Js('by using your opponents own energy against them'), Js('through quick dodges and steadfast retaliations'), Js('by focusing on weaker parts of your opponents body'), Js('through exploiting weak and vulnerable areas of the body'), Js('by disrupting your opponents movements'), Js('by manipulating your opponents limbs at their joints'), Js('through preferably a single, fierce retaliating movement'), Js("by exploiting weakness in your opponent and using your body's own strengths"), Js('by taking advantage of the openings your opponent will leave whenever they attack'), Js('through a constant build up of momentum and disrupting the momentum of your opponent'), Js('through utilizing every available weakness in your opponents defense and body'), Js('by dodging attacks and thus both exhausting your opponent and causing an exploitable opening'), Js('through keeping an impenetrable defense and thus forcing your opponent to open one in theirs when they attack'), Js('by figuring out your opponents strengths and defending against those, forcing them to change their attack'), Js('by constantly shifting both your and your opponents center of gravity'), Js('by focusing solely on your opponents movements, figuring out their weakness and exploiting it'), Js('through a series of incredibly swift attacks'), Js('by disorienting your opponent through quick movements and disruptive attacks'), Js("by exploiting your body's strongest parts against the weakest of your opponent"), Js('by barraging your opponent with countless fierce strikes and thus forcing him to stay defensive'), Js('through fierce attacks on your opponents weaker body parts'), Js('by constantly hammering your opponent with relentless and often dirty attacks'), Js('through very precise and well timed strikes'), Js('through minimal, but relentless and very precise strikes'), Js('by exploiting sensitive points in your opponents body'), Js('by focusing all your energy into a few precise attacks'), Js('through manipulation and exploitation of your opponents weaknesses'), Js('through swift dodges, quick movements and even faster attacks'), Js('through quick and swift strikes and utilizing different centers of gravity'), Js('by using every stronger point of your body as a possible weapon'), Js('by shifting energies in your body to soften the blows you receive and strengthen the ones you hand out'), Js('by focusing entirely on maximizing your own natural strengths and minimizing your weaknesses'), Js('by patiently waiting for an opening before unleashing your power swiftly'), Js('by converting the energy and momentum of your opponent into that of your own and using it against them'), Js('through subtle body shifts to deflect your opponents attacks and create openings to retaliate'), Js("through a rapid succession of strike after strike on vital and vulnerable parts of your opponents' bodies")]))
var.put('nm5', Js([Js('agility'), Js('blocking'), Js('blocks'), Js('choke holds'), Js('deflection'), Js('elbow jabs'), Js('foot sweeps'), Js('grapples'), Js('headbutts'), Js('joint locks'), Js('kicks'), Js('knee strikes'), Js('open hand techniques'), Js('pressure points'), Js('punches'), Js('quick movements'), Js('shifts in balance'), Js('sidesteps'), Js('speed'), Js('throws')]))
var.put('nm6', Js([Js('speed'), Js('agility'), Js('reflexes'), Js('strength'), Js('stamina'), Js('endurance'), Js('flexibility'), Js('quick thinking')]))
var.put('nm7', Js([Js(' of yourself and your opponent'), Js(', or lack thereof, of your opponent'), Js(' of yourself primarily, but also of your opponent'), Js(' of yourself'), Js(' of the defender'), Js(' of the attacker'), Js(' of both the attacker and defender')]))
var.put('nm9', Js([Js('exploiting'), Js('capitalizing'), Js('manipulating'), Js('profiting from'), Js('utilizing'), Js('taking advantage of')]))
var.put('nm10', Js([Js('yourself'), Js('your challenger'), Js('both fighters')]))
var.put('nm11', Js([Js('blocks'), Js('deflections'), Js('pressure points'), Js('quick movements'), Js('shifts in balance'), Js('sidesteps'), Js('speed'), Js('shifts in the centers of gravity'), Js('sense of balance'), Js('sheer strength')]))
var.put('nm12', Js([Js('can often be caught off guard'), Js('may overextend themselves'), Js('can be thrown off balance'), Js('is likely to exhaust themselves'), Js('will likely leave an opening'), Js('tends to overexert themselves'), Js('can be driven into a position you want them to be'), Js('will have to adapt and thus leave openings'), Js('has no choice but to change their stance'), Js('tends to tire out pretty quickly'), Js('can become overconfident and leave an opening'), Js('tends to become frustrated as none of their strikes hit'), Js('is often unable to respond in time'), Js('often lacks the knowledge to respond well enough'), Js('may become infuriated or just frustrated')]))
var.put('nm13', Js([Js('making them easy to overmaster'), Js('giving you the perfect opportunities to retaliate'), Js('allowing you to become an overwhelming force'), Js('giving you the opportunity to gain the upper hand'), Js('making it easier to overcome their strengths'), Js('further giving your strengths the upper hand'), Js('which helps defend your weaknesses more'), Js('helping you stay in control of the fight'), Js('allowing you to be the dominant force in this encounter'), Js('further giving you leverage to work with'), Js('which just helps pave the road to victory'), Js('which is a huge advantage in and of itself'), Js('which puts them right where you want them to be'), Js("something you'll be able to take full advantage of"), Js('allowing you to capitalize on your biggest strengths')]))
var.put('nm14', Js([Js("a lack of ground techniques. Once you're on the ground"), Js("a lack of more circular movements. If you're up against an opponent who dances around you"), Js("that it requires a great deal of mastery. So if you're still relatively new to this style"), Js('that opposite styles tend to gain the upper hand more easily. So if facing such an opponent'), Js("that it often requires the opponent to make the first move. If you're facing an opponent that doesn't"), Js("that it requires you to react incredibly fast. So until you've training your reflexes"), Js("that there are too many different styles. So until you've mastered enough"), Js("a lack of some very crucial real life applicable skills. So if you're in a real fight"), Js('a lack of potentially lethal moves. Not a big weakness, but needed in some situations and in those cases'), Js("the illegal moves in this art are easily used and exploited by others. When your opponent doesn't fight with the same rules"), Js('that multiple opponents can become overwhelming very quickly. If you ever face 3 or more opponents'), Js('that this is a purely one on one style. When facing multiple opponents'), Js('a lack of dirty tricks that are used in real life. So whenever facing an opponent outside of sporting events'), Js('that many moves are predictable to a knowledgeable opponent. If you face an opponent who knows your tricks'), Js("a common feeling of being in control even when you might not be. When you're overconfident")]))
var.put('nm15', Js([Js("it's really difficult to gain the upper hand"), Js('the fight may already be over'), Js("you'll need more than your skills to win"), Js('you may be the one that gets caught off guard'), Js('your weaknesses may suddenly become very apparent to your opponent'), Js('you could quickly end up overpowered'), Js("it's near impossible to win"), Js('your own strengths may prove to be lacking'), Js('your strengths quickly become far less viable'), Js("you'll have to rely on a different bag of tricks"), Js('your strengths may suddenly be a weakness'), Js("it's really difficult not to leave an exploitable opening"), Js("you're no longer the one in control of the fight"), Js('your opponent will have a lot of leverage over you'), Js('all you can do is try to force your opponent into a position you can dominate from'), Js('any advantage you may have had are out of the window')]))
pass
pass


# Add lib to the module scope
martialArtDescriptions = var.to_python()