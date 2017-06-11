__all__ = ['cafeNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names4', 'names2', 'nameGen', 'names3'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['names', 'result'])
    var.put('names', Js([]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.get('names').put(var.get('i'), ((var.get('names4').get(var.get('rnd0'))+Js(' '))+var.get('names3').get(var.get('rnd1'))))
            else:
                var.put('rnd0', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.get('names').put(var.get('i'), ((((var.get('names1').get(var.get('rnd0'))+Js(' '))+var.get('names2').get(var.get('rnd1')))+Js(' '))+var.get('names3').get(var.get('rnd2'))))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Ancient'), Js('Antique'), Js('Bad'), Js('Big'), Js('Black'), Js('Blonde'), Js('Cinnamon'), Js('Cocao'), Js('Cool'), Js('Daily'), Js('Dark'), Js('Delish'), Js('Divine'), Js('Ebony'), Js('Fatty'), Js('Featherly'), Js('Firefly'), Js('Flaming'), Js('Fluffy'), Js('Flying'), Js('Frozen'), Js('Funky'), Js('Gecko'), Js('Generous'), Js('Gentle'), Js('Ginger'), Js('Green'), Js('Handy'), Js('Happy'), Js('Hard'), Js('Harmony'), Js('Hava'), Js('Havana'), Js('Hazel'), Js('Hazelnut'), Js('Hidden'), Js('Homey'), Js('Hospitable'), Js('Hot'), Js('Incredible'), Js('Indulging'), Js('Ivory'), Js('Jasmine'), Js('Jazz'), Js('Jolly'), Js('Last'), Js('Light'), Js('Little'), Js('Little Big'), Js('Mad'), Js('Marble'), Js('Mellow'), Js('Melting'), Js('Merry'), Js('Midnight'), Js('Mini'), Js('Misty'), Js('Natural'), Js('New'), Js('Noble'), Js('Nutty'), Js('Oceanic'), Js('Old'), Js('Olive'), Js('Palm'), Js('Panama'), Js('Paragon'), Js('Peaceful'), Js('Pleasant'), Js('Pleasure'), Js('Precious'), Js('Quiet'), Js('Rainforest'), Js('Rapid'), Js('Regular'), Js('Rich'), Js('Salty'), Js('Sandy'), Js('Secret'), Js('Silent'), Js('Silk'), Js('Smooth'), Js('Soft'), Js('Strange'), Js('Sunny'), Js('Sweet'), Js('Swift'), Js('Tasty'), Js('Timeless'), Js('Tranquil'), Js('Twinkling'), Js('Unique'), Js('Universal'), Js('Unusual'), Js('Urban'), Js('Vanilla'), Js('Welcoming'), Js('Wet'), Js('Whispering'), Js('White')]))
var.put('names2', Js([Js('Baker'), Js('Balcony'), Js('Beach'), Js('Bean'), Js('Beans'), Js('Bites'), Js('Bliss'), Js('Blossom'), Js('Blue'), Js('Boulder'), Js('Break'), Js('Breeze'), Js('Brew'), Js('Brews'), Js('Cabin'), Js('Chocolate'), Js('Cook'), Js('Cottage'), Js('Crumble'), Js('Crumbs'), Js('Cup'), Js('Deli'), Js('Delight'), Js('Delights'), Js('Distraction'), Js('Drinks'), Js('Drop'), Js('Earth'), Js('Echo'), Js('Eden'), Js('Enigma'), Js('Express'), Js('Fest'), Js('Festival'), Js('Flower'), Js('Forest'), Js('Fountain'), Js('Fruits'), Js('Gallery'), Js('Garden'), Js('Gardens'), Js('Glee'), Js('Grind'), Js('Groove'), Js('Harvest'), Js('Hat'), Js('Hatter'), Js('Haven'), Js('Heaven'), Js('Ingredients'), Js('Interlude'), Js('Java'), Js('Joy'), Js('Leaf'), Js('Lodge'), Js('Lounge'), Js('Magnolia'), Js('Marina'), Js('Mirror'), Js('Monocle'), Js('Moon'), Js('Nibble'), Js('Oasis'), Js('Panini'), Js('Patio'), Js('Pearl'), Js('Petal'), Js('Picnic'), Js('Planet'), Js('Plaza'), Js('Puzzle'), Js('Question'), Js('Questions'), Js('Rest'), Js('Retreat'), Js('Rock'), Js('Rose'), Js('Satisfaction'), Js('Shack'), Js('Shrine'), Js('Sip'), Js('Snack'), Js('Spring'), Js('Station'), Js('Tales'), Js('Teapot'), Js('Tease'), Js('Temptation'), Js('Temptations'), Js('Terrace'), Js('Time'), Js('Tower'), Js('Treasure'), Js('Treasures'), Js('Treat'), Js('Treats'), Js('Tulip'), Js('Utopia'), Js('Waterfall'), Js('Waters'), Js('Waves')]))
var.put('names3', Js([Js('Cafe'), Js('Tearoom'), Js('Bistro'), Js('Barista'), Js('Coffee'), Js('Room'), Js('Coffee Shop'), Js('Joint'), Js('Lunchroom'), Js('Coffee Bar'), Js('Cafeteria'), Js('Cafe'), Js('Cafe'), Js('Diner'), Js('Espresso Bar')]))
var.put('names4', Js([Js('Bacon & Eggs'), Js('Bean & Gone'), Js('Bean Bag'), Js('Bean Drinking'), Js('Bean Me Up'), Js('Bean There'), Js('Beans & Barley'), Js('Big Mugs'), Js('Bizz Buzz'), Js('Bread & Butter'), Js('Brew & Chew'), Js('Brew Crew'), Js('Brew Ha Ha'), Js('Brew for You'), Js('Brewed Awakening'), Js('Busy Bean'), Js('Cocoa Connection'), Js('Come & Go'), Js('Common Grounds'), Js('Cool Beans'), Js('Daily Grind'), Js('Ding Dong'), Js('Drive Brew'), Js('Early Rise'), Js('Eats & Treats'), Js('Espresso Lane'), Js('Express-O'), Js('Fire & Ice'), Js('Fresh Roast'), Js('Go & Get It'), Js('Grind House'), Js('Grinders'), Js('Ground Up'), Js('Hallowed Grounds'), Js('Havana Java'), Js('Here & There'), Js('High & Mighty'), Js('Hot & Cold'), Js('Hot & Steamy'), Js('Hot Shots'), Js('Impresso Espresso'), Js('In & Out'), Js('Incredible Edibles'), Js('Java Junction'), Js('Java Nice Day'), Js('Java the Hut'), Js('Javawocky'), Js('Joe & Go'), Js('Jumping Bean'), Js('Jumpstart'), Js('Knock On Wood'), Js('Last Drop'), Js('Late Latte'), Js('Lava Java'), Js('Lemon & Lime'), Js('Lettuce Retreat'), Js('Liquid Heaven'), Js('Moment of Peace'), Js('Mug Shot'), Js('Naughty & Nice'), Js('Near & Far'), Js('Needle & Thread'), Js('Peaches & Cream'), Js('Pestle & Mortar'), Js('Q & A'), Js('Quick & Easy'), Js('Rest & Relaxation'), Js('Rise & Grind'), Js('Rise & Shine'), Js('Roasted Bean'), Js('Roasters'), Js('Salt & Pepper'), Js('See You Latte'), Js('Short & Steamy'), Js('Silky & Smooth'), Js('Slice of Life'), Js('Splitting Beans'), Js('Steamy Bean'), Js('Steamy Indulgences'), Js('Sugar & Spice'), Js('Sweet & Savory'), Js('Tall, Dark and Coffee'), Js('Tea Time'), Js('Thanks a Latte'), Js('Thinking Cup'), Js('This & That'), Js('Tongue & Cheek'), Js('Trembling Cup'), Js('Tutty Fruity'), Js('Urban Grind'), Js('Vice & Virtue'), Js('Wake Up'), Js('Wakey Wakey'), Js('Whole Latte Love'), Js('Wide Awake'), Js('Yin & Yang'), Js('Yours & Mine'), Js('Yum Yum'), Js('Yummy Tummy'), Js('Zig Zag')]))
pass
pass


# Add lib to the module scope
cafeNames = var.to_python()