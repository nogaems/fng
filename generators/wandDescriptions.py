__all__ = ['wandDescriptions']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm11', 'rnd11', 'nm12b', 'rnd8', 'name', 'rnd1b', 'nm3', 'name3', 'nm2', 'br', 'name2', 'nm7', 'nm10', 'nm12', 'nm12a', 'rnd2a', 'rnd4', 'rnd7', 'result', 'nm6', 'rnd6', 'rnd2b', 'nm4', 'rnd10a', 'rnd3', 'nm8', 'rnd1a', 'nm9', 'rnd10', 'rnd9', 'rnd12'])
    var.put('nm1', Js([Js('Acacia Wood'), Js('Alder Wood'), Js('Ash Wood'), Js('Aspen Wood'), Js('Baobab Wood'), Js('Basswood'), Js('Baywood'), Js('Beech Wood'), Js('Birch Wood'), Js('Bitterwood'), Js('Blackthorn Wood'), Js('Blackwood'), Js('Buckeye Wood'), Js('Cedar Wood'), Js('Cherry Wood'), Js('Chestnut Wood'), Js('Cycad Wood'), Js('Cypress Wood'), Js('Dogwood'), Js('Ebony Wood'), Js('Elder Wood'), Js('Elm Wood'), Js('Fiddlewood'), Js('Fir Wood'), Js('Firethorn Wood'), Js('Flame Tree Wood'), Js('Hackberry Wood'), Js('Hawthorn Wood'), Js('Hazel Wood'), Js('Hazelnut Wood'), Js('Hemlock Wood'), Js('Hickory Wood'), Js('Holly Wood'), Js('Hornbeam Wood'), Js('Inkwood'), Js('Ironbark Wood'), Js('Ironwood'), Js('Ivy Wood'), Js('Juniper Wood'), Js('Kingwood'), Js('Lancewood'), Js('Larch Wood'), Js('Laurel Wood'), Js('Magnolia Wood'), Js('Mahogany Wood'), Js('Maidenwood'), Js('Mangrove Wood'), Js('Maple Wood'), Js('Medlar Wood'), Js('Oak Wood'), Js('Oleander Wood'), Js('Palm Wood'), Js('Pawpaw Wood'), Js('Pear Wood'), Js('Pine Wood'), Js('Poisonwood'), Js('Poplar Wood'), Js('Redbud Wood'), Js('Redwood'), Js('Reed Wood'), Js('Rosewood'), Js('Rowan Wood'), Js('Sandalwood'), Js('Senna Wood'), Js('Sequoia Wood'), Js('Spruce Wood'), Js('Strongbark Wood'), Js('Sycamore Wood'), Js('Toadwood'), Js('Vine Wood'), Js('Walnut Wood'), Js('Willow Wood'), Js('Yew Wood'), Js('Yucca Wood')]))
    var.put('nm2', Js([Js('heavily favors those with a talent for conjuring'), Js('heavily favors those with a talent for dueling'), Js('heavily favors those with a talent for the most powerful magics'), Js('heavily favors those with an affinity for spoken magics'), Js('heavily favors those without even an inkling of an interest in the darker arts'), Js('heavily prefers owners with an affinity for enchantments'), Js('heavily prefers those prone to temptations'), Js('heavily prefers those who are naturally lucky'), Js('heavily prefers those who can resist strong temptations'), Js('heavily prefers those with a burdened past'), Js('heavily prefers those with a loving heart'), Js('mostly prefers those who are heavily in tune with nature'), Js('mostly seeks out those who tend to make the right choice'), Js('often favors protectors and guardians'), Js('often favors those with a talent for healing spells'), Js('often needs an owner with a strong sense of justice'), Js('often prefers an owner with a lot of intuition and instinct'), Js('often prefers the more mysterious owner'), Js('often prefers those with strong family roots'), Js('often seeks out those who are faint of heart'), Js('often seeks out those who are timid or shy'), Js('often seeks out those who will serve a greater purpose'), Js('often seeks out those with a talent for non-verbal magic'), Js('often seeks out those with an interest in transfigurations'), Js('often seeks out travelers and adventurers'), Js('strongly favors an insecure owner'), Js('strongly favors slow learners'), Js('strongly favors those who love to make others smile'), Js('strongly favors those with a lot of pride'), Js('strongly favors those with a talent for mind magic'), Js('strongly prefers the more clumsy owner'), Js('strongly prefers those with a pure heart'), Js('strongly prefers those with a talent for destruction'), Js('strongly prefers those with a wandering mind'), Js('strongly seeks out quick learners'), Js('tend to seek out the well-respected'), Js('tends to favor bookworms'), Js('tends to favor the outcasts, loners and misfits'), Js('tends to favor those interested in the darker arts'), Js('tends to favor those who are energetic'), Js('tends to favor those who love and crave destruction'), Js('tends to favor those who tend to make mistakes'), Js('tends to favor those with a competitive heart'), Js('tends to favor those with a kind heart'), Js('tends to favor those with incredible destinies'), Js('tends to favor those with the darkest hearts and minds'), Js('tends to favor those with the potential to be incredibly powerful'), Js('tends to prefer an owner with big dreams'), Js('tends to prefer quick thinkers as an owner'), Js('tends to prefer those who are destined for a long, successful life'), Js('tends to prefer those with a heart of gold'), Js('tends to prefer those with a vicious mind'), Js('tends to prefer those with an affinity for water'), Js('tends to prefer those with strength and agility'), Js('tends to seek out those with a sharp mind'), Js('tends to seek out those with a talent for defensive spells'), Js('tends to seek out those with an affinity for magical creatures'), Js('usually favors those who have been around death'), Js('usually favors those who think outside of the box'), Js('usually favors those with a brave heart'), Js('usually favors those with a love of all creatures'), Js('usually favors those with a strong sense of righteousness'), Js('usually favors troublemakers'), Js('usually prefer those who lack any magical talent'), Js('usually prefers a rich owner'), Js('usually prefers a very social owner'), Js('usually prefers leader types'), Js('usually prefers public speakers and (future) public figures'), Js('usually prefers those bound by honor and integrity'), Js('usually prefers those who tend to follow instead of lead'), Js('usually prefers those with a dark heart'), Js('usually seeks out those who are bold and daring'), Js('usually seeks out those with a loyal heart'), Js('usually seeks out those with a mischievous mind'), Js('usually seeks out those with selfish magical needs')]))
    var.put('nm3', Js([Js('with a talent for conjuring'), Js('with a talent for dueling'), Js('with a talent for the most powerful magics'), Js('with an affinity for spoken magics'), Js('without even an inkling of an interest in the darker arts'), Js('with an affinity for enchantments'), Js('prone to temptations'), Js("who's naturally lucky"), Js('who can resist strong temptations'), Js('with a burdened past'), Js('with a loving heart'), Js("who's heavily in tune with nature"), Js('who tends to make the right choice'), Js('protective and loving'), Js('with a talent for healing spells'), Js('with a strong sense of justice'), Js('with a lot of intuition and instinct'), Js('mysterious'), Js('with strong family roots'), Js("who's faint of heart"), Js("who's timid or shy"), Js('who will serve a greater purpose'), Js('with a talent for non-verbal magic'), Js('with an interest in transfigurations'), Js('with a great sense of adventure'), Js("who's insecure"), Js('who tends to be a slow learner'), Js('who loves to make others smile'), Js('with a lot of pride'), Js('with a talent for mind magic'), Js('clumsy, but who tries hard'), Js('with a pure heart'), Js('with a talent for destruction'), Js('with a wandering mind'), Js('who learns quickly'), Js('well-respected'), Js('with a quick mind'), Js("who's often considered an outcast"), Js('interested in the darker arts'), Js("who's energetic"), Js('who loves and craves destruction'), Js('who tends to make mistakes'), Js('with a competitive heart'), Js('with a kind heart'), Js('with an incredible destiny'), Js('with the darkest heart and mind'), Js('with the potential to be incredibly powerful'), Js('with big dreams'), Js('who loves to study'), Js("who's destined for a long, successful life"), Js('with a heart of gold'), Js('with a vicious mind'), Js('with an affinity for water'), Js('with strength and agility'), Js('with a sharp mind'), Js('with a talent for defensive spells'), Js('with an affinity for magical creatures'), Js('who has been around death'), Js('who thinks outside of the box'), Js('with a brave heart'), Js('with a love of all creatures'), Js('with a strong sense of righteousness'), Js('who tends to get in trouble a lot'), Js('who lacks any magical talent'), Js('rich or powerful'), Js('social and likable'), Js('with the potential to be a great leader'), Js('with the potential to be an important public figure'), Js('bound by honor and integrity'), Js('who tends to follow instead of lead'), Js('with a dark heart'), Js("who's bold and daring"), Js('with a loyal heart'), Js('with a mischievous mind'), Js('with selfish magical needs')]))
    var.put('nm4', Js([Js('1 core'), Js('2 cores'), Js('3 cores')]))
    var.put('nm6', Js([Js('aids the learning process of magic spells'), Js('aids with casting spells at greater speeds'), Js('aids with the process of conjuring'), Js("can increase the power of spells immensely, but it requires a strong bond with it's owner"), Js('enhances defensive magic spells'), Js('enhances destructive magic spells'), Js("enhances either dark or light spells based on the owner's heart and refuses to cast the other"), Js('enhances healing spells'), Js('enhances mischievous magic spells, but can be mischievous itself'), Js('enhances natural magic spells'), Js("enhances the inherent magic of the wand's wood"), Js("enhances the owner's adaptability in combat"), Js("enhances the owner's courage, especially in dire situations"), Js("enhances the owner's intelligence"), Js("enhances the owner's intuition and instincts"), Js("enhances the owner's strongest characteristic"), Js('enhances the power of dark spells'), Js('enhances the power of invisibility spells'), Js('enhances the power of light spells'), Js('enhances the power of spells, but refuses to aid with destructive spells'), Js('enhances the power of transmutation spells'), Js('enhances whichever aspect its owner needs the most at a specific time'), Js('greatly aids in the process of learning non-verbal versions of many spells'), Js("greatly enhances the owner's senses during duels and battle"), Js('greatly increases magic transmission'), Js('greatly increases the power of spells, but tends to slow the casting speed'), Js('has the ability to calm its owner in dire situations'), Js("helps mitigate the owner's biggest weakness"), Js('increases the bond between owner and wand'), Js('increases the strength of summoning spells'), Js('lacks power in many aspects, except when protection is involved in some way'), Js('only slightly enhances spellpower'), Js("provides a decent all round boost to the owner's abilities"), Js('slightly increases magic transmission'), Js('strengthens the wand and protects against magical damage'), Js('tends to add explosiveness in various forms to spells')]))
    var.put('nm7', Js([Js('enhance'), Js('control'), Js('boost'), Js('constrain'), Js('regulate'), Js('augment'), Js('magnify'), Js('amplify')]))
    var.put('nm8', Js([Js('9 inches/23 cm'), Js('10 inches/25 cm'), Js('11 inches/28 cm'), Js('12 inches/30 cm'), Js('13 inches/33 cm'), Js('14 inches/36 cm'), Js('15 inches/38 cm')]))
    var.put('nm9', Js([Js('has an overall ordinary look'), Js('has intricate carvings on its handle'), Js('has intricate carvings all over'), Js('has a fairly plain look'), Js('has a well crafted look'), Js('has a classy look'), Js('has a gilded handle'), Js('was clearly made by a professional'), Js('has a beautifully crafted look'), Js('has an antique look'), Js('has an elegant look to it'), Js('has a refined look to it'), Js('has a luxurious look to it')]))
    var.put('nm10', Js([Js('very common'), Js('quite common'), Js('common'), Js('quite ordinary'), Js('not very common'), Js('quite rare'), Js('very rare'), Js('incredibily rare')]))
    var.put('nm11', Js([Js('does add to the overall cost of the wand'), Js('increases the production cost of the wand'), Js("means the wand won't be one of the cheaper types"), Js('increases the price of the wand')]))
    var.put('nm12', Js([Js('pricey wand'), Js('wand priced in the high-ranges'), Js('wand exclusively for the rich or fortunate'), Js('fancy wand for an extravagant price'), Js('very valuable wand')]))
    var.put('nm12a', Js(' and '))
    var.put('nm12b', Js(' as well, '))
    var.put('rnd1a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd1b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    while PyJsStrictEq(var.get('rnd1a'),var.get('rnd1b')):
        var.put('rnd1b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd2b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    while PyJsStrictEq(var.get('rnd2a'),var.get('rnd2b')):
        var.put('rnd2b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    if PyJsStrictEq(var.get('rnd4'),Js(0.0)):
        var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
        var.put('name2b', ((((Js('A core of ')+var.get('nm5').get(var.get('rnd5')))+Js(' which '))+var.get('nm6').get(var.get('rnd6')))+Js('.')))
    else:
        if PyJsStrictEq(var.get('rnd4'),Js(1.0)):
            var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            var.put('rnd5b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            var.put('name2b', ((((((((((Js('A core of ')+var.get('nm5').get(var.get('rnd5')))+Js(' which '))+var.get('nm6').get(var.get('rnd6')))+Js(' and '))+var.get('nm5').get(var.get('rnd5b')))+Js(' is added to '))+var.get('nm7').get(var.get('rnd7')))+Js(' the power of the '))+var.get('nm5').get(var.get('rnd5')))+Js(' core.')))
        else:
            var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            var.put('rnd5b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            var.put('rnd5c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
            var.put('rnd6b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
            def PyJs_LONG_0_(var=var):
                return (((((((((((((Js('A core of ')+var.get('nm5').get(var.get('rnd5')))+Js(' which '))+var.get('nm6').get(var.get('rnd6')))+Js(' and '))+var.get('nm5').get(var.get('rnd5b')))+Js(' is added to '))+var.get('nm7').get(var.get('rnd7')))+Js(' the power of the '))+var.get('nm5').get(var.get('rnd5')))+Js(' core. Finally, a core of '))+var.get('nm5').get(var.get('rnd5c')))+Js(' is added in small amounts to '))+var.get('nm6').get(var.get('rnd6b')))
            var.put('name2b', (PyJs_LONG_0_()+Js('.')))
    var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    if (var.get('rnd10')<Js(4.0)):
        var.put('nm11', Js([Js('reduces the overall cost a fair bit'), Js('lowers the price of the wand'), Js("means the price of the wand won't be too high"), Js('helps reduce the production cost of the wand')]))
    var.put('rnd10a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    if (var.get('rnd10a')<Js(4.0)):
        if (var.get('rnd10')<Js(4.0)):
            var.put('nm12a', Js(' and '))
            var.put('nm12', Js([Js('very cheap wand'), Js('wand priced in the lower range'), Js('wand available to all'), Js('cheap, but reliable type of wand'), Js('fairly cheap wand')]))
            var.put('nm12b', Js(' as well, '))
        else:
            var.put('nm12a', Js(', however '))
            var.put('nm12', Js([Js('wand priced in the mid-ranges'), Js('great wand for a decent price'), Js('perfect wand for a soft price'), Js('reasonably inexpensive wand')]))
            var.put('nm12b', Js(', '))
    else:
        if (var.get('rnd10')<Js(4.0)):
            var.put('nm12a', Js(', however, '))
            var.put('nm12', Js([Js('wand priced in the mid-ranges'), Js('great wand for a decent price'), Js('perfect wand for a soft price'), Js('reasonably inexpensive wand')]))
            var.put('nm12b', Js(', '))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    def PyJs_LONG_1_(var=var):
        return (((((((((((Js('This wand is made out of ')+var.get('nm1').get(var.get('rnd1a')))+Js(', which '))+var.get('nm2').get(var.get('rnd2a')))+Js('. The handle is made out of '))+var.get('nm1').get(var.get('rnd1b')))+Js(', which in turn '))+var.get('nm2').get(var.get('rnd2b')))+Js('. However, the combination of this strand of '))+var.get('nm1').get(var.get('rnd1a')))+Js(' and '))+var.get('nm1').get(var.get('rnd1b')))
    var.put('name', (((PyJs_LONG_1_()+Js(' means the wand will seek out somebody '))+var.get('nm3').get(var.get('rnd3')))+Js('.')))
    var.put('name2', (((Js('A wand usually has 1 or 2 cores, but some have 3, this wand has ')+var.get('nm4').get(var.get('rnd4')))+Js('. '))+var.get('name2b')))
    def PyJs_LONG_2_(var=var):
        return (((((((((((((Js('The wand measures ')+var.get('nm8').get(var.get('rnd8')))+Js(' and '))+var.get('nm9').get(var.get('rnd9')))+Js('. The particular strand of '))+var.get('nm1').get(var.get('rnd1a')))+Js(' used in this wand is '))+var.get('nm10').get(var.get('rnd10')))+Js(', which '))+var.get('nm11').get(var.get('rnd11')))+var.get('nm12a'))+var.get('nm5').get(var.get('rnd5')))+Js(' is '))+var.get('nm10').get(var.get('rnd10a')))
    var.put('name3', ((((PyJs_LONG_2_()+var.get('nm12b'))+Js(' resulting in a '))+var.get('nm12').get(var.get('rnd12')))+Js('.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(4.0)):
        try:
            pass
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
wandDescriptions = var.to_python()