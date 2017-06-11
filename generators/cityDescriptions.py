__all__ = ['cityDescriptions']

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
    var.registers(['nm1', 'nm11', 'rnd18', 'rnd15', 'rnd11', 'nm16', 'rnd8', 'name', 'rnd18b', 'nm3', 'rnd14', 'name3', 'rnd17', 'nm2', 'rnd2', 'br', 'name2', 'nm14', 'nm7', 'nm10', 'name4', 'nm15', 'rnd5', 'nm12', 'nm5', 'rnd4', 'nm8c', 'rnd7', 'result', 'nm6', 'rnd6', 'rnd8c', 'rnd13', 'nm4', 'rnd3', 'nm18', 'rnd17b', 'nm17', 'nm13', 'rnd17c', 'nm9', 'rnd10', 'rnd16', 'rnd18c', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('along the banks of a mighty river'), Js('along the banks of modest rivers'), Js('along the banks of a gentle river'), Js('along the banks of a crystal clear river'), Js('along the banks of a labyrinth of rivers'), Js('atop the crowns of majestic hills'), Js('atop gentle hills'), Js('atop emerald hills of grass'), Js('atop quiet and serene hills'), Js('atop robust hills'), Js('at the base of a mighty mountain'), Js('in the shadow of an enormous mountain'), Js('on the sunny side of a gentle mountain'), Js('at the base of a rugged mountain'), Js('at the base of a modest mountain'), Js('in the center of a giant forest'), Js('in a large glade of a mighty forest'), Js('at the edge of a lush forest'), Js('at the edge of a dense, tall forest'), Js('among the towering trees of a huge forest'), Js('atop a breathtaking fjord'), Js('atop a towering fjord'), Js('atop the rugged walls of a fjord'), Js('atop the steep facade of a mighty fjord'), Js('atop the rocky heights of a fjord'), Js('amidst the green grasses of a gentle field'), Js('amidst the windy fields of gentle grasslands'), Js('amidst the swaying grasses of a windy meadow'), Js('amidst the dry grasses of a simple savanna'), Js('amidst the lush grasses of an evergreen pasture'), Js('amidst the ivory fields of snow'), Js('amidst the gentle snows of a pristine tundra'), Js('amidst the crisp snows of a silver taiga'), Js('amidst the frozen lands of a bitter expanse'), Js('amidst the bleak fields of snow'), Js('at the edge of a mighty swamp'), Js('in the center of an expansive swamp'), Js('at the borders of a murky swamp'), Js('amidst the murky waters of an enormous swamp'), Js('around the mushy waters of a traitorous swamp'), Js('at the base of a mighty volcano'), Js('in the shadow of a dormant volcano'), Js('at the base of a traitorous volcano'), Js('in the shadow of a rugged volcano'), Js('at the base of a potentially active volcano'), Js('on the banks of a large natural harbor'), Js('on the banks of a carefully crafted harbor'), Js('on the banks of a modest natural harbor'), Js('on the banks of a man-made harbor'), Js('on the banks of a delicate natural harbor'), Js('amidst the flora of a mighty jungle'), Js('at the edge of a lush jungle'), Js('at the center of a dangerous jungle'), Js('at the border of a traitorous jungle'), Js('at the center of a gorgeous jungle'), Js('at the center of a delicate island'), Js('amidst a large, rugged island'), Js('on a simple island'), Js('at the edge of an enormous island'), Js('at the center of a relatively small island'), Js('at the edge of a desert'), Js('amidst the sands of a mighty desert'), Js('around an oasis in the middle of a desert'), Js('in the middle of a scorching desert'), Js('in a seemingly endless desert')]))
    var.put('nm2', Js([Js('Southport'), Js('Highfront'), Js('Shroudmoor'), Js('Freyport'), Js('Westborough'), Js('Dawnburgh'), Js('Oldwood'), Js('Stonewick'), Js('Freyford'), Js('Blackmere'), Js('Rosemore'), Js('Amberhill'), Js('Evermere'), Js('Sunhold'), Js('Ebonwick'), Js('Ravenside'), Js('Riverburn'), Js('Embercrest'), Js('Whiteburn'), Js('Oxglen'), Js('Madhollow'), Js('Ironford'), Js('Earthwall'), Js('Claybourne'), Js('Shimmergarde'), Js('Earthbury'), Js('Fayglen'), Js('Craghorn'), Js('Bellburn'), Js('Kilbrook')]))
    var.put('nm3', Js([Js('a true modern'), Js('a modest'), Js('a historic'), Js('an evergrowing'), Js('an architectural'), Js('a technological'), Js('an extraordinary'), Js('a gorgeous'), Js('an ancient'), Js('a classic'), Js('a contemporary'), Js('a state-of-the-art'), Js('a fully modernized'), Js('a future oriented'), Js('a leading-edge')]))
    var.put('nm4', Js([Js('metropolis'), Js('marvel'), Js('wonder'), Js('city'), Js('phenomenon'), Js('sight'), Js('curiosity'), Js('display of wonder'), Js('urban phenomenon'), Js('trade center')]))
    var.put('nm5', Js([Js('beauty'), Js('wonder'), Js('uniqueness'), Js('appearance'), Js('allure'), Js('grace'), Js('elegance'), Js('charm')]))
    var.put('nm6', Js([Js('snowy mountains'), Js('mighty mountains'), Js('tall mountains'), Js('a gentle mountain'), Js('a majestic mountain'), Js('lush forests'), Js('majestic forests'), Js('grand forests'), Js('several waterfalls'), Js('monumental waterfalls'), Js('cascading waterfalls'), Js('a dorment volcano'), Js('a smoldering volcano'), Js('a fuming volcano'), Js('lush fields of grass'), Js('green, fertile fields'), Js('rich, luscious fields'), Js('gentle hills'), Js('an abundance of hills'), Js('modest hills'), Js('clear blue skies'), Js('pristine skies'), Js('everclear skies')]))
    var.put('nm7', Js([Js('resources'), Js('riches'), Js('trade resources'), Js('materials'), Js('climate')]))
    var.put('nm8c', Js([Js('riddled'), Js('packed'), Js('crowded'), Js('sprinkled'), Js('scattered'), Js('littered'), Js('growing'), Js('spreading')]))
    var.put('nm9', Js([Js('tall'), Js('impressive'), Js('modest'), Js('towering'), Js('soaring'), Js('giant'), Js('stylish'), Js('elaborate'), Js('various'), Js('distinct'), Js('unique'), Js('peculiar'), Js('similar'), Js('luxurious'), Js('elegant'), Js('impressive')]))
    var.put('nm10', Js([Js('a new one seems to pop up every other week'), Js('many have clearly been built within the last decade'), Js('many show their age and a rich history'), Js('a lot of them seem to have evolved throughout the ages'), Js('more seem to be on their way'), Js('they look astonishingly beautiful all together'), Js('they each represent the many different aspects of the city'), Js('they clearly show what they represent to the city itself'), Js("they've been designed to adorn the city and each other"), Js('they have aspects which represent their past, present and future'), Js('each was more impressive than the next'), Js('while modern now, their history still shined through'), Js('their history seemed to shine more now than ever'), Js('each seems to evolve with the times without losing their history'), Js('they all seem to be in perfect unison despite being different'), Js('they seem to be continuously evolving as new additions are added even now'), Js('there is no place on earth with anything like this'), Js('even from afar they manage to display their beauty'), Js('their beauty is only matched by each other'), Js('they seem to be reaching higher and higher each year')]))
    var.put('nm11', Js([Js('Business is booming'), Js('Life is great'), Js('Culture is rising'), Js('The quality of life is high'), Js('Technology is thriving'), Js('Trade is at an all time high'), Js('Recreation is impeccable'), Js('Education is superb'), Js('Parks and gardens are flourishing'), Js('Health and services are faultless'), Js("Daily life isn't too stressful"), Js('Science and development is flourishing'), Js('Employment is tremendous')]))
    var.put('nm12', Js([Js('Various cultures'), Js('New cultures'), Js('Many new cultures'), Js('A few new cultures'), Js('Countless cultures'), Js('Many different cultures')]))
    var.put('nm13', Js([Js('the architecture'), Js('education'), Js("the city's development"), Js('business'), Js("the city's history"), Js('education'), Js('trade and relations'), Js('international relations'), Js("the city's people"), Js("the city's cuisine")]))
    var.put('nm14', Js([Js('few differences'), Js('plain, ordinary people'), Js('little diversity'), Js('no variation'), Js('monotony'), Js('little contrast'), Js('few cultures'), Js('predictability')]))
    var.put('nm15', Js([Js('a large melting pot'), Js('a fusion of everything'), Js('a new culture of variety'), Js('a multicultural hub'), Js('an amalgamation of differences')]))
    var.put('nm16', Js([Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js('10'), Js('11'), Js('12'), Js('13'), Js('14')]))
    var.put('nm17', Js([Js('restaurants'), Js('bars'), Js('clubs'), Js('coffeehouses'), Js('bistros'), Js('bakeries'), Js('concession stands'), Js('diners'), Js('food carts'), Js('take-outs'), Js('sandwich bars'), Js('cafés'), Js('ethnic restaurants'), Js('gastropubs'), Js('theme restaurants')]))
    var.put('nm18', Js([Js('art galleries'), Js('one of the many parks'), Js('nature'), Js('the national park'), Js('sightseeing'), Js('libraries'), Js('water sports'), Js('adventure sports'), Js('sport activities'), Js('concerts'), Js('musical activities'), Js('musea'), Js('tours'), Js('city exploring'), Js('dance'), Js('theaters'), Js('arcades'), Js('clubs'), Js('an amusement park'), Js('aerobics'), Js('photography')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    if (var.get('rnd1')>Js(59.0)):
        while (var.get('rnd6')<Js(20.0)):
            var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    if (var.get('rnd6')>Js(19.0)):
        var.put('rnd7', Js(4.0))
    if (var.get('rnd6')<Js(5.0)):
        var.put('nm8b', Js(' mountains '))
    else:
        if ((var.get('rnd6')>Js(4.0)) and (var.get('rnd6')<Js(8.0))):
            var.put('nm8b', Js(' forests '))
        else:
            if ((var.get('rnd6')>Js(7.0)) and (var.get('rnd6')<Js(11.0))):
                var.put('nm8b', Js(' waterfalls '))
            else:
                if ((var.get('rnd6')>Js(10.0)) and (var.get('rnd6')<Js(14.0))):
                    var.put('nm8b', Js(' volcanoes '))
                else:
                    if ((var.get('rnd6')>Js(13.0)) and (var.get('rnd6')<Js(17.0))):
                        var.put('nm8b', Js(' fields '))
                    else:
                        if ((var.get('rnd6')>Js(16.0)) and (var.get('rnd6')<Js(20.0))):
                            var.put('nm8b', Js(' hills '))
                        else:
                            var.put('nm8b', Js(' skies '))
    var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    var.put('rnd8c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8c').get('length')))))
    var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length')))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
    var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
    var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length')))))
    var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    var.put('rnd17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd17b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    while PyJsStrictEq(var.get('rnd17'),var.get('rnd17b')):
        var.put('rnd17b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd17c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    while (PyJsStrictEq(var.get('rnd17'),var.get('rnd17c')) or PyJsStrictEq(var.get('rnd17b'),var.get('rnd17c'))):
        var.put('rnd17c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    var.put('rnd18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd18b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd18c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    while PyJsStrictEq(var.get('rnd18'),var.get('rnd18b')):
        var.put('rnd18b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    var.put('rnd18c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    while (PyJsStrictEq(var.get('rnd17'),var.get('rnd18c')) or PyJsStrictEq(var.get('rnd18b'),var.get('rnd18c'))):
        var.put('rnd18c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length')))))
    def PyJs_LONG_0_(var=var):
        return ((((((((((((Js('The city of ')+var.get('nm2').get(var.get('rnd2')))+Js(' was built '))+var.get('nm1').get(var.get('rnd1')))+Js(' and is truly '))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm4').get(var.get('rnd4')))+Js('. Its '))+var.get('nm5').get(var.get('rnd5')))+Js(' is matched by the backdrop of '))+var.get('nm6').get(var.get('rnd6')))+Js(' which have helped shape the city to what it is today.'))
    var.put('name', PyJs_LONG_0_())
    var.put('name2', ((((((Js('The ')+var.get('nm7').get(var.get('rnd7')))+Js(' these '))+var.get('nm8b'))+Js(' brought were of great importance, but they were also influential when it came to architectural designs as the vast majority of buildings '))+var.get('nm8').get(var.get('rnd8')))+Js('.')))
    def PyJs_LONG_1_(var=var):
        return ((((((((((((Js('The skyline is ')+var.get('nm8c').get(var.get('rnd8c')))+Js(' with '))+var.get('nm9').get(var.get('rnd9')))+Js(' skyscrapers and '))+var.get('nm10').get(var.get('rnd10')))+Js('. '))+var.get('nm11').get(var.get('rnd11')))+Js(' in '))+var.get('nm2').get(var.get('rnd2')))+Js(' and it has attracted a lot of attention. '))+var.get('nm12').get(var.get('rnd12')))+Js(' have left their mark not just on '))
    var.put('name3', ((((((((PyJs_LONG_1_()+var.get('nm13').get(var.get('rnd13')))+Js(", but also upon the city's identity. What historically was a city of "))+var.get('nm14').get(var.get('rnd14')))+Js(' has grown into '))+var.get('nm15').get(var.get('rnd15')))+Js(" and it's this that unites the "))+var.get('nm16').get(var.get('rnd16')))+Js(' million people to this day.')))
    def PyJs_LONG_2_(var=var):
        return (((((((((Js("It's this multicultural identity that has truly left its mark. Hundreds of ")+var.get('nm17').get(var.get('rnd17')))+Js(', '))+var.get('nm17').get(var.get('rnd17b')))+Js(' and '))+var.get('nm17').get(var.get('rnd17c')))+Js(' offer a plethora of culinary choices and those who feel hungry for something else can enjoy '))+var.get('nm18').get(var.get('rnd18')))+Js(', '))+var.get('nm18').get(var.get('rnd18b')))
    var.put('name4', (((PyJs_LONG_2_()+Js(', '))+var.get('nm18').get(var.get('rnd18c')))+Js(' or one of the many other recreational venues.')))
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
pass
pass


# Add lib to the module scope
cityDescriptions = var.to_python()