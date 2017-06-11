__all__ = ['creatureDescriptions']

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
    var.registers(['names15', 'random21b', 'random0', 'random26', 'names5', 'names27', 'names2', 'names23b', 'random4a', 'name', 'names4a', 'names23', 'name7', 'names7a', 'names21', 'random5', 'name3', 'name6', 'names7c', 'random11', 'names7d', 'names20', 'random24', 'names28', 'names7b', 'names24', 'name2', 'random10', 'names14', 'names11', 'names18', 'random7c', 'random8', 'random20', 'names17', 'names25', 'random7d', 'name4', 'names11a', 'random3', 'random17', 'random21a', 'random25', 'random6', 'names9', 'random7b', 'names13', 'names8', 'names16', 'random27', 'names4c', 'names4b', 'names3', 'names12', 'names1', 'random9', 'random18', 'names22', 'random23', 'result', 'names26', 'random2', 'random7a', 'random12', 'random15a', 'random22', 'names6', 'names10', 'random4c', 'random19', 'random14', 'random1', 'random16', 'name5', 'random28', 'names0', 'names19', 'random13', 'random7e', 'random15b', 'random4b'])
    var.put('names0', Js([Js(' and rare'), Js(' and incredibily rare'), Js(' and nearly extinct'), Js(', but common'), Js(', but very common'), Js(' and uncommon'), Js(' and seldom seen'), Js(', but extremely common'), Js(', but fairly common'), Js(', but often seen')]))
    var.put('names1', Js([Js('adorable'), Js('amazing'), Js('amusing'), Js('astonishing'), Js('beautiful'), Js('bizarre'), Js('captivating'), Js('charming'), Js('clever'), Js('curious'), Js('delightful'), Js('fierce'), Js('funny'), Js('incredible'), Js('lovely'), Js('odd'), Js('special'), Js('strange'), Js('unusual'), Js('weird')]))
    var.put('names2', Js([Js('mammal'), Js('aquatic mammal'), Js('amphibian'), Js('reptile'), Js('fish'), Js('invertebrate'), Js('bird')]))
    var.put('names3', Js([Js(' bear'), Js(' cat'), Js(' cow'), Js(' deer'), Js(' dog'), Js('n elephant'), Js(' fox'), Js(' goat'), Js(' hippo'), Js(' horse'), Js(' human'), Js(' leopard'), Js(' lion'), Js(' mouse'), Js(' pig'), Js(' rabbit'), Js(' rat'), Js(' rhino'), Js(' tiger'), Js(' wolf')]))
    var.put('names4a', Js([Js('two legs and two arms'), Js('two legs and four arms'), Js('four legs'), Js('six legs'), Js('two legs and two arms'), Js('four legs'), Js('six legs'), Js('four legs and two arms'), Js('four legs and two arms')]))
    var.put('names4b', Js([Js('')]))
    var.put('names4c', Js([Js(', but they have no tail'), Js(', but they have no tail'), Js(', but they have no tail'), Js(', but they have no tail'), Js(', but they have no tail'), Js(', but they have no tail'), Js(' and a long, curling tail'), Js(' and a long, fluffy tail'), Js(' and a long, muscular tail'), Js(' and a long, ribbon-like tail'), Js(' and a long, strong and agile tail'), Js(' and a long, strong tail'), Js(' and a long, thick tail'), Js(' and a long, thin tail'), Js(' and a long, weak tail'), Js(' and a short, curly tail'), Js(' and a short, fluffy tail'), Js(' and a short, muscular tail'), Js(' and a short, strong tail'), Js(' and a short, stubby tail'), Js(' and a short, thick tail'), Js(' and a short, thin tail'), Js(' and a short, weak tail'), Js(' and a thick, flat tail'), Js(' and remnants of what was once a tail')]))
    var.put('names5', Js([Js('soft, but strong skin'), Js('thick, strong skin'), Js('soft, delicate skin'), Js('thick, rough skin'), Js('thin, rough skin'), Js('thin, delicate skin'), Js('thick, smooth skin'), Js('soft, smooth skin'), Js('thin, but strong skin'), Js('thick, but delicate skin')]))
    var.put('names6', Js([Js('covered in thick, soft fur'), Js('covered in thick, coarse fur'), Js('covered in thin, soft fur'), Js('covered in thin, coarse fur'), Js('covered in thick, fluffy fur'), Js('covered in thin, fluffy fur'), Js('covered in short, soft fur'), Js('covered in long, soft fur'), Js('covered in long, fluffy fur'), Js('covered in short, fluffy fur'), Js('covered in short, coarse hairs'), Js('covered in short, soft hairs'), Js('covered in long, coarse hairs'), Js('covered in long, soft hairs'), Js('covered in thick, soft hairs'), Js('covered in thick, coarse hairs'), Js('covered in thin, soft hairs'), Js('covered in thin, coarse hairs')]))
    var.put('names7a', Js([Js('black'), Js('blue'), Js('bronze'), Js('brown'), Js('gold'), Js('grey'), Js('orange'), Js('pink'), Js('purple'), Js('red'), Js('silver'), Js('white'), Js('yellow'), Js('dark blue'), Js('dark bronze'), Js('dark brown'), Js('dark gold'), Js('dark grey'), Js('dark orange'), Js('dark pink'), Js('dark purple'), Js('dark red'), Js('dark silver'), Js('dark yellow'), Js('light blue'), Js('light bronze'), Js('light brown'), Js('light gold'), Js('light grey'), Js('light orange'), Js('light pink'), Js('light purple'), Js('light red'), Js('light silver'), Js('light yellow')]))
    var.put('names7b', Js([Js(', black'), Js(', blue'), Js(', bronze'), Js(', brown'), Js(', gold'), Js(', grey'), Js(', orange'), Js(', pink'), Js(', purple'), Js(', red'), Js(', silver'), Js(', white'), Js(', yellow'), Js(', dark blue'), Js(', dark bronze'), Js(', dark brown'), Js(', dark gold'), Js(', dark grey'), Js(', dark orange'), Js(', dark pink'), Js(', dark purple'), Js(', dark red'), Js(', dark silver'), Js(', dark yellow'), Js(', light blue'), Js(', light bronze'), Js(', light brown'), Js(', light gold'), Js(', light grey'), Js(', light orange'), Js(', light pink'), Js(', light purple'), Js(', light red'), Js(', light silver'), Js(', light yellow'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('names7c', Js([Js(', black'), Js(', blue'), Js(', bronze'), Js(', brown'), Js(', gold'), Js(', grey'), Js(', orange'), Js(', pink'), Js(', purple'), Js(', red'), Js(', silver'), Js(', white'), Js(', yellow'), Js(', dark blue'), Js(', dark bronze'), Js(', dark brown'), Js(', dark gold'), Js(', dark grey'), Js(', dark orange'), Js(', dark pink'), Js(', dark purple'), Js(', dark red'), Js(', dark silver'), Js(', dark yellow'), Js(', light blue'), Js(', light bronze'), Js(', light brown'), Js(', light gold'), Js(', light grey'), Js(', light orange'), Js(', light pink'), Js(', light purple'), Js(', light red'), Js(', light silver'), Js(', light yellow'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
    var.put('names7d', Js([Js(' or black'), Js(' or blue'), Js(' or bronze'), Js(' or brown'), Js(' or gold'), Js(' or grey'), Js(' or orange'), Js(' or pink'), Js(' or purple'), Js(' or red'), Js(' or silver'), Js(' or white'), Js(' or yellow'), Js(' or dark blue'), Js(' or dark bronze'), Js(' or dark brown'), Js(' or dark gold'), Js(' or dark grey'), Js(' or dark orange'), Js(' or dark pink'), Js(' or dark purple'), Js(' or dark red'), Js(' or dark silver'), Js(' or dark yellow'), Js(' or light blue'), Js(' or light bronze'), Js(' or light brown'), Js(' or light gold'), Js(' or light grey'), Js(' or light orange'), Js(' or light pink'), Js(' or light purple'), Js(' or light red'), Js(' or light silver'), Js(' or light yellow')]))
    var.put('names8', Js([Js('barren areas'), Js('cold areas'), Js('darker areas'), Js('forested areas'), Js('frozen areas'), Js('high areas'), Js('hot areas'), Js('humid areas'), Js('low areas'), Js('marshy areas'), Js('moist areas'), Js('mountainous areas'), Js('open areas'), Js('quiet areas'), Js('rainy areas'), Js('snowy areas'), Js('temperate areas'), Js('warm areas'), Js('wet areas'), Js('wintry areas')]))
    var.put('names9', Js([Js('common'), Js('extremely common'), Js('extremely rare'), Js('fairly common'), Js('fairly rare'), Js('quite common'), Js('quite rare'), Js('rare'), Js('relatively common'), Js('relatively rare')]))
    var.put('names10', Js([Js('herbivores'), Js('carnivores'), Js('omnivores')]))
    var.put('names11', Js([Js('relatively small'), Js('relatively large'), Js('fairly small'), Js('fairly large'), Js('small, long'), Js('large, long'), Js('small, thin'), Js('large, wide'), Js('small, narrow'), Js('long, narrow')]))
    var.put('names11a', Js('mouths, their teeth'))
    var.put('names12', Js([Js('long'), Js('short'), Js('wide'), Js('narrow'), Js('rough')]))
    var.put('names13', Js([Js('grasses'), Js('berries'), Js('fruits'), Js('nuts'), Js('flowers'), Js('plants'), Js('leaves'), Js('insects'), Js('fish'), Js('smaller creatures'), Js('larger creatures'), Js('mushrooms'), Js('creatures')]))
    var.put('names14', Js([Js('nocturnal'), Js('diurnal'), Js('crepuscular')]))
    var.put('names15', Js([Js('sight'), Js('sense of smell'), Js('hearing'), Js('taste buds'), Js('extra sense')]))
    var.put('names16', Js([Js('large, round eyes'), Js('thin, narrow eyes'), Js('small, slanted eyes'), Js('small, round eyes'), Js('small, beady eyes'), Js('small, elliptic eyes'), Js('large, elliptic eyes'), Js('large, slanted eyes'), Js('odd, but interesting eyes'), Js('gorgeous eyes')]))
    var.put('names17', Js([Js('not that great'), Js('not very reliable'), Js('not impressive'), Js('a bit poor'), Js('not too great'), Js('lacking'), Js('underdeveloped'), Js('relatively poor')]))
    var.put('names18', Js([Js('huge noses'), Js('small noses'), Js('wide noses'), Js('long noses'), Js('enormous noses'), Js('thin noses'), Js('an almost hidden nose'), Js('a lack of a visible nose'), Js('tiny noses'), Js('narrow noses')]))
    var.put('names19', Js([Js('enormous ears'), Js('huge, flappy ears'), Js('huge, hanging ears'), Js('large, bended ears'), Js('large, hanging ears'), Js('large, round ears'), Js('large, standing ears'), Js('long, pointy ears'), Js('short, flappy ears'), Js('short, pointy ears'), Js('small, bended ears'), Js('small, hanging ears'), Js('small, round ears'), Js('small, standing ears'), Js('tiny, almost hidden ears')]))
    var.put('names20', Js([Js('relatively small'), Js('relatively large'), Js('fairly small'), Js('fairly large'), Js('small and long'), Js('large and long'), Js('small and thin'), Js('large and wide'), Js('small and narrow'), Js('long and narrow')]))
    var.put('names21', Js([Js('extremely high pitched'), Js('very high pitched'), Js('high pitched'), Js('fairly high pitched'), Js('relatively high pitched'), Js('relatively low pitched'), Js('fairly low pitched'), Js('low pitched'), Js('very low pitched'), Js('extremely low pitched')]))
    var.put('names22', Js([Js('extremely large'), Js('extremely limited'), Js('fairly limited'), Js('fairly small'), Js('fairly wide'), Js('huge'), Js('large'), Js('limited'), Js('small'), Js('very limited'), Js('very small'), Js('wide')]))
    var.put('names23', Js([Js('aggressive'), Js('bold'), Js('fairly violent'), Js('invasive'), Js('quite forceful'), Js('quite frenzied'), Js('quite intrusive'), Js('quite nervous'), Js('very aggressive'), Js('very violent'), Js('very peaceful'), Js('calm'), Js('fairly calm'), Js('very calm'), Js('very gentle'), Js('very timid'), Js('quite timid'), Js('timid'), Js('mild mannered'), Js('gentle')]))
    var.put('names23b', Js(', but '))
    var.put('names24', Js([Js("they're very territorial."), Js('they get very territorial.'), Js('they heavily defend their personal space.'), Js("they'll fiercely defend their territory."), Js("they're quite territorial."), Js("they'll defend their territory strongly."), Js('their territory is well defended.'), Js('they can get quite territorial.'), Js("they're territorial in terms of personal space."), Js('their personal space is fiercely defended.'), Js("they're not very territorial."), Js("they're not territorial at all."), Js("they won't defend their territory much."), Js('they tend to let their territory be taken be stronger creatures.'), Js("they're not one to defend their territory."), Js("they're not keen on defending their personal space."), Js("they minimize conflict and thus aren't very territorial."), Js('they have no real territory and wish to avoid conflicts.'), Js('they travel a lot and thus have no real territory nor urges to defend it.'), Js('their nomadic lifestyle has made them placid in terms of defending territory.')]))
    var.put('names25', Js([Js('once a year'), Js('twice a year'), Js('once every two years'), Js('once every 18 months'), Js('once every three years'), Js('twice to three times a year'), Js('once or twice a year'), Js('once every nine to ten months'), Js('once every five years'), Js('once every four years')]))
    var.put('names26', Js([Js('mate and bond with a single partner for life'), Js('mate with just 1 partner for life'), Js('mate and bond with a select few partners for life'), Js('mate and bond with one or two partners throughout life'), Js('mate with multiple partners throughout life'), Js('mate with one or two partners throughout life'), Js('mate with a select few partners throughout life'), Js('mate with a specificly selected partner for life'), Js('mate with a select group of partners for life'), Js('mate with a select few partners for life')]))
    var.put('names27', Js([Js('long lifepans'), Js('incredibily long lifespans'), Js('very long lifespans'), Js('fairly long lifespans'), Js('short lifespans'), Js('fairly short lifespans'), Js('very short lifespans'), Js('unfortunately short lifespans')]))
    var.put('names28', Js([Js('is to be expected.'), Js("isn't too surprising."), Js('is only normal.'), Js("isn't out of the ordinary."), Js("isn't extraordinary."), Js('is quite common among other species as well.')]))
    var.put('random0', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names0').get('length')))))
    var.put('random1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length')))))
    var.put('random2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length')))))
    if PyJsStrictEq(var.get('random2'),Js(1.0)):
        def PyJs_LONG_0_(var=var):
            return var.put('names3', Js([Js(' seal'), Js(' dolphin'), Js('n orca'), Js(' minke whale'), Js(' blue whale'), Js(' fin whale'), Js(' humpback whale'), Js(' great white shark'), Js(' narwhal'), Js(' reef shark'), Js(' manta ray'), Js(' tuna'), Js(' squid'), Js(' salmon'), Js(' carp'), Js(' trout'), Js(' piranha'), Js(' goldfish'), Js(' bass'), Js('n eel'), Js(' catfish'), Js(' pike'), Js(' small shark'), Js(' parrotfish'), Js(' young tuna')]))
        PyJs_LONG_0_()
        def PyJs_LONG_1_(var=var):
            return var.put('names4a', Js([Js('two large flippers'), Js('two small flippers'), Js('two large flippers'), Js('two small flippers'), Js('four large flippers'), Js('four small flippers'), Js('two strong side fins'), Js('four strong side fins'), Js('two side fins'), Js('four side fins'), Js('two large side fins'), Js('four large side fins'), Js('two powerful side fins'), Js('four powerful side fins'), Js('two huge side fins'), Js('four huge side fins')]))
        PyJs_LONG_1_()
        def PyJs_LONG_2_(var=var):
            return var.put('names4b', Js([Js(', a huge dorsal fin'), Js(', a small dorsal fin'), Js(', a thick, long dorsal fin'), Js(', a thin, long dorsal fin'), Js(', a wide, sail-like dorsal fin'), Js(', a ribbon-like dorsal fin'), Js(', a long, ribbon-like dorsal fin'), Js(', a short, ribbon-like dorsal fin'), Js(', a huge, sail-like dorsal fin'), Js(', a short, strong dorsal fin'), Js(', a long, strong dorsal fin'), Js(', a short, pointy dorsal fin'), Js(', a long, pointy dorsal fin'), Js(', a long, streamlined dorsal fin'), Js(', a short, streamlined dorsal fin')]))
        PyJs_LONG_2_()
        def PyJs_LONG_3_(var=var):
            return var.put('names4c', Js([Js(' and a huge, powerful tail'), Js(' and a huge, muscular tail'), Js(' and a large, muscular tail'), Js(' and a large, powerful tail'), Js(' and a short, muscular tail'), Js(' and a long, powerful tail'), Js(' and a short, powerful tail'), Js(' and a long, muscular tail'), Js(' and a huge, powerful tail'), Js(' and a huge, muscular tail'), Js(' and a large, muscular tail'), Js(' and a large, powerful tail'), Js(' and a short, muscular tail'), Js(' and a long, powerful tail'), Js(' and a short, powerful tail'), Js(' and a long, muscular tail')]))
        PyJs_LONG_3_()
        var.put('names6', Js([Js('')]))
        var.put('names8', Js([Js('deep waters'), Js('relatively shallow waters'), Js('coastal areas'), Js('the depths of the ocean'), Js('the depths of the seas'), Js('large lakes'), Js('rivers'), Js('large rivers'), Js('lakes'), Js('the entire ocean as they migrate')]))
        var.put('names19', Js([Js('virtually no visible ears'), Js('no visible ears'), Js('pretty much no visible ears'), Js('short, flappy ears'), Js('short, pointy ears'), Js('small, bended ears'), Js('small, hanging ears'), Js('small, round ears'), Js('small, standing ears'), Js('tiny, almost hidden ears')]))
    else:
        if PyJsStrictEq(var.get('random2'),Js(2.0)):
            var.put('names3', Js([Js(' toad'), Js(' tree frog'), Js(' salamander'), Js('n anaconda'), Js('n earthworm'), Js(' gecko'), Js(' chameleon'), Js(' newt'), Js(' frog'), Js(' cobra'), Js(' komodo dragon'), Js(' viper'), Js(' coral snake'), Js(' python'), Js(' Chinese giant salamander')]))
            var.put('names4a', Js([Js('four legs'), Js('four legs and two arms'), Js('no legs or arms, like a snake'), Js('six legs'), Js('two legs and two arms')]))
            def PyJs_LONG_4_(var=var):
                return var.put('names4c', Js([Js(', but they have no tail'), Js(' and a huge, powerful tail'), Js(' and a long, muscular tail'), Js(' and a long, powerful tail'), Js(' and a long, strong and agile tail'), Js(' and a long, strong tail'), Js(' and a long, thick tail'), Js(' and a long, thin tail'), Js(' and a long, useless tail'), Js(' and a long, weak tail'), Js(' and a short, muscular tail'), Js(' and a short, powerful tail'), Js(' and a short, strong tail'), Js(' and a short, stubby tail'), Js(' and a short, thick tail'), Js(' and a short, thin tail'), Js(' and a short, useless tail'), Js(' and a short, weak tail'), Js(' and a thick, powerful tail'), Js(' and remnants of what was once a tail')]))
            PyJs_LONG_4_()
            var.put('names6', Js([Js(' covered in a thin layer of mucous,'), Js(' covered in a thick layer of mucous,'), Js(' covered in a very thin layer of mucous,'), Js(' covered in a very thick layer of mucous,'), Js(' covered lightly in mucous,'), Js(' covered in nothing but small scales,'), Js(' covered in nothing but large scales,'), Js(', '), Js(', '), Js(', ')]))
            var.put('names19', Js([Js('virtually no visible ears'), Js('no visible ears'), Js('pretty much no visible ears'), Js('short, pointy ears'), Js('small, bended ears'), Js('small, hanging ears'), Js('small, round ears'), Js('small, standing ears'), Js('tiny, almost hidden ears')]))
            var.put('names25', Js([Js('once a year'), Js('twice a year'), Js('once every two years'), Js('once every 18 months'), Js('once every three years'), Js('twice to three times a year'), Js('once or twice a year'), Js('once every three to four months'), Js('four times a year'), Js('three times a year')]))
        else:
            if PyJsStrictEq(var.get('random2'),Js(3.0)):
                var.put('names3', Js([Js(' boa'), Js(' chameleon'), Js(' cobra'), Js(' crocodile'), Js(' diplodocus'), Js(' frog'), Js(' gecko'), Js(' komodo dragon'), Js(' newt'), Js(' python'), Js(' salamander'), Js(' sea turtle'), Js(' stegosaurus'), Js(' t-rex'), Js(' tortoise'), Js(' triceratops'), Js(' velociraptor'), Js(' viper'), Js('n alligator'), Js('n anaconda')]))
                var.put('names4a', Js([Js('four legs'), Js('four legs and two arms'), Js('no legs or arms, like a snake'), Js('six legs'), Js('two legs and two arms')]))
                def PyJs_LONG_5_(var=var):
                    return var.put('names4c', Js([Js(', but they have no tail'), Js(' and a huge, powerful tail'), Js(' and a long, muscular tail'), Js(' and a long, powerful tail'), Js(' and a long, strong and agile tail'), Js(' and a long, strong tail'), Js(' and a long, thick tail'), Js(' and a long, thin tail'), Js(' and a long, useless tail'), Js(' and a long, weak tail'), Js(' and a short, muscular tail'), Js(' and a short, powerful tail'), Js(' and a short, strong tail'), Js(' and a short, stubby tail'), Js(' and a short, thick tail'), Js(' and a short, thin tail'), Js(' and a short, useless tail'), Js(' and a short, weak tail'), Js(' and a thick, powerful tail'), Js(' and remnants of what was once a tail')]))
                PyJs_LONG_5_()
                def PyJs_LONG_6_(var=var):
                    return var.put('names6', Js([Js(' covered in thin, coarse scales,'), Js(' covered in large, coarse scales,'), Js(' covered in large, smooth scales,'), Js(' covered in large, strong scales,'), Js(' covered in small, coarse scales,'), Js(' covered in small, smooth scales,'), Js(' covered in small, strong scales,'), Js(' covered in strong, hard scales,'), Js(' covered in thick, coarse scales,'), Js(' covered in thick, strong scales,')]))
                PyJs_LONG_6_()
                var.put('names8', Js([Js('barren areas'), Js('darker areas'), Js('forested areas'), Js('high areas'), Js('hot areas'), Js('humid areas'), Js('low areas'), Js('marshy areas'), Js('moist areas'), Js('mountainous areas'), Js('open areas'), Js('quiet areas'), Js('rainy areas'), Js('temperate areas'), Js('warm areas'), Js('wet areas')]))
                var.put('names18', Js([Js('small noses'), Js('wide noses'), Js('long noses'), Js('thin noses'), Js('almost hidden noses'), Js('lack of a visible nose'), Js('tiny noses'), Js('narrow noses')]))
                var.put('names19', Js([Js('virtually no visible ears'), Js('no visible ears'), Js('pretty much no visible ears'), Js('short, pointy ears'), Js('small, bended ears'), Js('small, hanging ears'), Js('small, round ears'), Js('small, standing ears'), Js('tiny, almost hidden ears')]))
                var.put('names25', Js([Js('once a year'), Js('twice a year'), Js('once every two years'), Js('once every 18 months'), Js('once every three years'), Js('twice to three times a year'), Js('once or twice a year'), Js('once every three to four months'), Js('four times a year'), Js('three times a year')]))
            else:
                if PyJsStrictEq(var.get('random2'),Js(4.0)):
                    def PyJs_LONG_7_(var=var):
                        return var.put('names3', Js([Js(' seal'), Js(' dolphin'), Js('n orca'), Js(' minke whale'), Js(' blue whale'), Js(' fin whale'), Js(' humpback whale'), Js(' great white shark'), Js(' narwhal'), Js(' reef shark'), Js(' manta ray'), Js(' tuna'), Js(' squid'), Js(' salmon'), Js(' carp'), Js(' trout'), Js(' piranha'), Js(' goldfish'), Js(' bass'), Js('n eel'), Js(' catfish'), Js(' pike'), Js(' small shark'), Js(' parrotfish'), Js(' young tuna'), Js(' pufferfish'), Js(' clownfish'), Js(' triggerfish'), Js(' guppy'), Js(' discus fish'), Js(' lionfish')]))
                    PyJs_LONG_7_()
                    var.put('names4a', Js([Js('two strong side fins'), Js('four strong side fins'), Js('two side fins'), Js('four side fins'), Js('two large side fins'), Js('four large side fins'), Js('two powerful side fins'), Js('four powerful side fins'), Js('two huge side fins'), Js('four huge side fins')]))
                    def PyJs_LONG_8_(var=var):
                        return var.put('names4b', Js([Js(', a huge dorsal fin'), Js(', a small dorsal fin'), Js(', a thick, long dorsal fin'), Js(', a thin, long dorsal fin'), Js(', a wide, sail-like dorsal fin'), Js(', a ribbon-like dorsal fin'), Js(', a long, ribbon-like dorsal fin'), Js(', a short, ribbon-like dorsal fin'), Js(', a huge, sail-like dorsal fin'), Js(', a short, strong dorsal fin'), Js(', a long, strong dorsal fin'), Js(', a short, pointy dorsal fin'), Js(', a long, pointy dorsal fin'), Js(', a long, streamlined dorsal fin'), Js(', a short, streamlined dorsal fin')]))
                    PyJs_LONG_8_()
                    def PyJs_LONG_9_(var=var):
                        return var.put('names4c', Js([Js(' and a huge, powerful tail and small anal fin'), Js(' and a huge, muscular tail and small anal fin'), Js(' and a large, muscular tail and small anal fin'), Js(' and a large, powerful tail and small anal fin'), Js(' and a short, muscular tail and small anal fin'), Js(' and a long, powerful tail and small anal fin'), Js(' and a short, powerful tail and small anal fin'), Js(' and a long, muscular tail and small anal fin'), Js(' and a huge, powerful tail and small anal fin'), Js(' and a huge, muscular tail and long anal fin'), Js(' and a large, muscular tail and long anal fin'), Js(' and a large, powerful tail and long anal fin'), Js(' and a short, muscular tail and long anal fin'), Js(' and a long, powerful tail and long anal fin'), Js(' and a short, powerful tail and long anal fin'), Js(' and a long, muscular tail and long anal fin')]))
                    PyJs_LONG_9_()
                    def PyJs_LONG_10_(var=var):
                        return var.put('names6', Js([Js(' covered in thin, coarse scales,'), Js(' covered in large, coarse scales,'), Js(' covered in large, smooth scales,'), Js(' covered in large, strong scales,'), Js(' covered in small, coarse scales,'), Js(' covered in small, smooth scales,'), Js(' covered in small, strong scales,'), Js(' covered in strong, hard scales,'), Js(' covered in thick, coarse scales,'), Js(' covered in thick, strong scales,')]))
                    PyJs_LONG_10_()
                    var.put('names8', Js([Js('deep waters'), Js('relatively shallow waters'), Js('coastal areas'), Js('the depths of the ocean'), Js('the depths of the seas'), Js('large lakes'), Js('rivers'), Js('large rivers'), Js('lakes'), Js('the entire ocean as they migrate')]))
                    var.put('names11a', Js('mouths'))
                    var.put('names18', Js([Js('small noses'), Js('wide noses'), Js('long noses'), Js('thin noses'), Js('almost hidden noses'), Js('lack of a visible nose'), Js('tiny noses'), Js('narrow noses')]))
                    var.put('names19', Js([Js('virtually no visible ears'), Js('no visible ears'), Js('pretty much no visible ears'), Js('tiny, almost hidden ears')]))
                    var.put('names25', Js([Js('once a year'), Js('twice a year'), Js('once every two years'), Js('once every 18 months'), Js('once every three years'), Js('twice to three times a year'), Js('once or twice a year'), Js('once every three to four months'), Js('four times a year'), Js('three times a year')]))
                else:
                    if PyJsStrictEq(var.get('random2'),Js(5.0)):
                        var.put('names3', Js([Js(' lobster'), Js(' hermite crab'), Js(' king crab'), Js(' squid'), Js(' mosquito'), Js(' fly'), Js(' fruitfly'), Js('n octopus'), Js(' bee'), Js(' wasp'), Js(' shrimp'), Js(' crayfish'), Js(' flea'), Js(' prawn'), Js(' giant squid')]))
                        def PyJs_LONG_11_(var=var):
                            return var.put('names4a', Js([Js('eight legs'), Js('eight tentacles'), Js('four clawed arms, four legs'), Js('four legs'), Js('four tentacles, four legs'), Js('four tentacles, six legs'), Js('four tentacles, two clawed arms'), Js('four tentacles, two legs'), Js('four winged arms, four legs'), Js('four winged arms, six legs'), Js('four winged arms, two legs'), Js('four wings, four legs'), Js('four wings, six legs'), Js('four wings, two legs'), Js('six legs'), Js('six tentacles'), Js('two clawed arms, four legs'), Js('two clawed arms, six legs'), Js('two clawed arms, two legs'), Js('two legs, two arms'), Js('two tentacles, four legs'), Js('two tentacles, six legs'), Js('two tentacles, two clawed arms'), Js('two tentacles, two legs'), Js('two winged arms, four legs'), Js('two winged arms, six legs'), Js('two winged arms, two legs'), Js('two wings, four legs'), Js('two wings, six legs'), Js('two wings, two legs')]))
                        PyJs_LONG_11_()
                        def PyJs_LONG_12_(var=var):
                            return var.put('names4c', Js([Js(', but they have no tail'), Js(' and a huge, powerful tail'), Js(' and a long, muscular tail'), Js(' and a long, powerful tail'), Js(' and a long, strong and agile tail'), Js(' and a long, strong tail'), Js(' and a long, thick tail'), Js(' and a long, thin tail'), Js(' and a long, useless tail'), Js(' and a long, weak tail'), Js(' and a short, muscular tail'), Js(' and a short, powerful tail'), Js(' and a short, strong tail'), Js(' and a short, stubby tail'), Js(' and a short, thick tail'), Js(' and a short, thin tail'), Js(' and a short, useless tail'), Js(' and a short, weak tail'), Js(' and a thick, powerful tail'), Js(' and remnants of what was once a tail')]))
                        PyJs_LONG_12_()
                        def PyJs_LONG_13_(var=var):
                            return var.put('names5', Js([Js('soft, but strong skin'), Js('thick, strong skin'), Js('soft, delicate skin'), Js('thick, rough skin'), Js('thin, rough skin'), Js('thin, delicate skin'), Js('thick, smooth skin'), Js('soft, smooth skin'), Js('thin, but strong skin'), Js('thick, but delicate skin'), Js('stong, armored skin'), Js('thick, armored skin'), Js('soft, armored skin'), Js('thinly armored skin'), Js('hard, armored skin')]))
                        PyJs_LONG_13_()
                        var.put('names6', Js([Js('')]))
                        var.put('names11a', Js('mouths'))
                        var.put('names25', Js([Js('once a year'), Js('twice a year'), Js('once every two years'), Js('once every 18 months'), Js('once every three years'), Js('twice to three times a year'), Js('once or twice a year'), Js('once every three to four months'), Js('four times a year'), Js('three times a year')]))
                    else:
                        if PyJsStrictEq(var.get('random2'),Js(6.0)):
                            var.put('names3', Js([Js('n albatross'), Js(' chicken'), Js(' cockatoo'), Js(' condor'), Js(' crane'), Js(' crow'), Js(' dove'), Js(' duck'), Js('n eagle'), Js(' falcon'), Js(' flamingo'), Js(' kiwi'), Js('n owl'), Js(' macaw'), Js('n ostrich'), Js(' peacock'), Js(' pelican'), Js(' penguin'), Js(' pigeon'), Js(' raven'), Js(' robin'), Js(' sparrow'), Js(' swan'), Js(' swift'), Js(' vulture')]))
                            var.put('names4a', Js([Js('two huge wings'), Js('four huge wings'), Js('two huge, powerful wings'), Js('four huge, powerful wings'), Js('two huge and two smaller wings'), Js('two enormous wings'), Js('four enormous wings'), Js('two large and four smaller wings'), Js('four smaller wings'), Js('two smaller wings')]))
                            var.put('names4b', Js([Js(', two strong, clawed legs'), Js(', two small, clawed legs'), Js(', four strong, clawed legs'), Js(', four small, clawed legs'), Js(', two strong legs'), Js(', four strong legs'), Js(', two small legs'), Js(', four small legs'), Js(', two thin, long legs'), Js(', two long, strong legs, ')]))
                            var.put('names4c', Js([Js(' and a huge tail'), Js(' and a huge, wide tail'), Js(' and a huge, powerful tail'), Js(' and a long, powerful tail'), Js(' and a long, elegant tail'), Js(' and a short, elegant tail'), Js(' and a short, powerful tail'), Js(' and a wide, powerful tail'), Js(' and a wide, elegant tail'), Js(' and a short tail')]))
                            def PyJs_LONG_14_(var=var):
                                return var.put('names6', Js([Js(' covered in large feathers,'), Js(' covered in short feathers,'), Js(' covered in thick feathers,'), Js(' covered in thin feathers,'), Js(' covered in small, narrow feathers,'), Js(' covered in large, narrow feathers,'), Js(' covered in large, thin feathers,'), Js(' covered in large, wide feathers,'), Js(' covered in long, thin feathers,'), Js(' covered in long, wide feathers,'), Js(' covered in short, thin feathers,'), Js(' covered in short, wide feathers,'), Js(' covered in small feathers,'), Js(' covered in small, thin feathers,'), Js(' covered in small, wide feathers,')]))
                            PyJs_LONG_14_()
                            var.put('names11', Js([Js('')]))
                            var.put('names11a', Js('beaks'))
                            var.put('names18', Js([Js('long beaks'), Js('sharp beaks'), Js('thin beaks'), Js('short beaks'), Js('huge beaks'), Js('enormous beaks'), Js('wide beaks'), Js('thin, sharp beaks'), Js('long, sharp beaks'), Js('long, pointy beaks'), Js('short, pointy beaks'), Js('huge, pointy beaks'), Js('huge, sharp beaks'), Js('short, sharp beaks'), Js('thin, pointy beaks')]))
                            var.put('names19', Js([Js('virtually no visible ears'), Js('no visible ears'), Js('pretty much no visible ears'), Js('tiny, almost hidden ears')]))
    var.put('random3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length')))))
    var.put('random4a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4a').get('length')))))
    var.put('random4b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4b').get('length')))))
    var.put('random4c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names4c').get('length')))))
    var.put('random5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names5').get('length')))))
    var.put('random6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names6').get('length')))))
    var.put('random7a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7a').get('length')))))
    var.put('random7b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7b').get('length')))))
    while PyJsStrictEq(var.get('random7b'),var.get('random7a')):
        var.put('random2b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7b').get('length')))))
    var.put('random7c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7c').get('length')))))
    while (PyJsStrictEq(var.get('random7c'),var.get('random7a')) or PyJsStrictEq(var.get('random7c'),var.get('random7b'))):
        var.put('random7c', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7c').get('length')))))
    var.put('random7d', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7c').get('length')))))
    while ((PyJsStrictEq(var.get('random7d'),var.get('random7a')) or PyJsStrictEq(var.get('random7d'),var.get('random7b'))) or PyJsStrictEq(var.get('random7d'),var.get('random7c'))):
        var.put('random7d', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7c').get('length')))))
    var.put('random7e', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7d').get('length')))))
    while (((PyJsStrictEq(var.get('random7e'),var.get('random7a')) or PyJsStrictEq(var.get('random7e'),var.get('random7b'))) or PyJsStrictEq(var.get('random7e'),var.get('random7c'))) or PyJsStrictEq(var.get('random7e'),var.get('random7d'))):
        var.put('random7e', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names7d').get('length')))))
    var.put('random8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names8').get('length')))))
    var.put('random9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names9').get('length')))))
    var.put('random10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names10').get('length')))))
    if PyJsStrictEq(var.get('random10'),Js(0.0)):
        if (PyJsStrictEq(var.get('random2'),Js(1.0)) or PyJsStrictEq(var.get('random2'),Js(4.0))):
            var.put('names13', Js([Js('plants'), Js('soft corals'), Js('hard corals')]))
        else:
            var.put('names13', Js([Js('grasses'), Js('berries'), Js('fruits'), Js('nuts'), Js('flowers'), Js('plants'), Js('leaves'), Js('mushrooms')]))
    else:
        if PyJsStrictEq(var.get('random10'),Js(1.0)):
            if (PyJsStrictEq(var.get('random2'),Js(1.0)) or PyJsStrictEq(var.get('random2'),Js(4.0))):
                var.put('names13', Js([Js('fish'), Js('smaller creatures'), Js('larger creatures'), Js('creatures'), Js('crustaceans')]))
            else:
                var.put('names13', Js([Js('insects'), Js('fish'), Js('smaller creatures'), Js('larger creatures'), Js('creatures')]))
        else:
            if PyJsStrictEq(var.get('random10'),Js(2.0)):
                if (PyJsStrictEq(var.get('random2'),Js(1.0)) or PyJsStrictEq(var.get('random2'),Js(4.0))):
                    var.put('names13', Js([Js('fish'), Js('smaller creatures'), Js('larger creatures'), Js('creatures'), Js('crustaceans'), Js('plants'), Js('soft corals'), Js('hard corals')]))
    var.put('random11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names11').get('length')))))
    var.put('random12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names12').get('length')))))
    var.put('random13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names13').get('length')))))
    var.put('random14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names14').get('length')))))
    var.put('random15a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names15').get('length')))))
    var.put('random15b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names15').get('length')))))
    while PyJsStrictEq(var.get('random15b'),var.get('random15a')):
        var.put('random15b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names15').get('length')))))
    var.put('random16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names16').get('length')))))
    var.put('random17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names17').get('length')))))
    var.put('random18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names18').get('length')))))
    var.put('random19', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names19').get('length')))))
    var.put('random20', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names20').get('length')))))
    var.put('name4', Js(''))
    var.put('name5', Js(''))
    if (PyJsStrictNeq(var.get('random15a'),Js(0.0)) and PyJsStrictNeq(var.get('random15b'),Js(0.0))):
        var.put('name4', ((((((((((Js("They're ")+var.get('names14').get(var.get('random14')))+Js(' and rely on their '))+var.get('names15').get(var.get('random15a')))+Js(' and '))+var.get('names15').get(var.get('random15b')))+Js(' to get around. They do have '))+var.get('names16').get(var.get('random16')))+Js(', but their sight is '))+var.get('names17').get(var.get('random17')))+Js('.')))
        var.put('name5', ((((((Js('They have ')+var.get('names18').get(var.get('random18')))+Js(' and '))+var.get('names19').get(var.get('random19')))+Js('. Their heads are '))+var.get('names20').get(var.get('random20')))+Js(' in comparison to their bodies.')))
    else:
        if (PyJsStrictNeq(var.get('random15a'),Js(1.0)) and PyJsStrictNeq(var.get('random15b'),Js(1.0))):
            var.put('name4', ((((((((((Js("They're ")+var.get('names14').get(var.get('random14')))+Js(' and rely on their '))+var.get('names15').get(var.get('random15a')))+Js(' and '))+var.get('names15').get(var.get('random15b')))+Js(' to get around. They do have '))+var.get('names18').get(var.get('random18')))+Js(', but their sense of smell is '))+var.get('names17').get(var.get('random17')))+Js('.')))
            var.put('name5', ((((((Js('They have ')+var.get('names16').get(var.get('random16')))+Js(' and '))+var.get('names19').get(var.get('random19')))+Js('. Their heads are '))+var.get('names20').get(var.get('random20')))+Js(' in comparison to their bodies.')))
        else:
            if (PyJsStrictNeq(var.get('random15a'),Js(2.0)) and PyJsStrictNeq(var.get('random15b'),Js(2.0))):
                var.put('name4', ((((((((((Js("They're ")+var.get('names14').get(var.get('random14')))+Js(' and rely on their '))+var.get('names15').get(var.get('random15a')))+Js(' and '))+var.get('names15').get(var.get('random15b')))+Js(' to get around. They do have '))+var.get('names19').get(var.get('random19')))+Js(', but their hearing is '))+var.get('names17').get(var.get('random17')))+Js('.')))
                var.put('name5', ((((((Js('They have ')+var.get('names18').get(var.get('random18')))+Js(' and '))+var.get('names16').get(var.get('random16')))+Js('. Their heads are '))+var.get('names20').get(var.get('random20')))+Js(' in comparison to their bodies.')))
            else:
                if (PyJsStrictNeq(var.get('random15a'),Js(3.0)) and PyJsStrictNeq(var.get('random15b'),Js(3.0))):
                    var.put('name4', ((((((((Js("They're ")+var.get('names14').get(var.get('random14')))+Js(' and rely on their '))+var.get('names15').get(var.get('random15a')))+Js(' and '))+var.get('names15').get(var.get('random15b')))+Js(' to get around. However, their taste buds are '))+var.get('names17').get(var.get('random17')))+Js('.')))
                    var.put('name5', ((((((((Js('They have ')+var.get('names16').get(var.get('random16')))+Js(', '))+var.get('names18').get(var.get('random18')))+Js(' and '))+var.get('names19').get(var.get('random19')))+Js('. Their heads are '))+var.get('names20').get(var.get('random20')))+Js(' in comparison to their bodies.')))
                else:
                    if (PyJsStrictNeq(var.get('random15a'),Js(4.0)) and PyJsStrictNeq(var.get('random15b'),Js(4.0))):
                        var.put('name4', ((((((((Js("They're ")+var.get('names14').get(var.get('random14')))+Js(' and rely on their '))+var.get('names15').get(var.get('random15a')))+Js(' and '))+var.get('names15').get(var.get('random15b')))+Js(' to get around. However, their other senses are '))+var.get('names17').get(var.get('random17')))+Js('.')))
                        var.put('name5', ((((((((Js('They have ')+var.get('names16').get(var.get('random16')))+Js(', '))+var.get('names18').get(var.get('random18')))+Js(' and '))+var.get('names19').get(var.get('random19')))+Js('. Their heads are '))+var.get('names20').get(var.get('random20')))+Js(' in comparison to their bodies.')))
    var.put('random21a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names21').get('length')))))
    var.put('random21b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names21').get('length')))))
    while PyJsStrictEq(var.get('random21b'),var.get('random21a')):
        var.put('random21b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names21').get('length')))))
    var.put('random22', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names22').get('length')))))
    var.put('random23', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names23').get('length')))))
    var.put('random24', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names24').get('length')))))
    if (((var.get('random23')<Js(10.0)) and (var.get('random24')<Js(10.0))) or ((var.get('random23')>Js(9.0)) and (var.get('random24')>Js(9.0)))):
        var.put('names23b', Js(' and '))
    var.put('random25', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names25').get('length')))))
    var.put('random26', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names26').get('length')))))
    var.put('random27', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names27').get('length')))))
    if ((var.get('random27')<Js(4.0)) and (var.get('names26')<Js(4.0))):
        var.put('names28', Js([Js('is quite surprising.'), Js('is just amazing.'), Js('is beautiful in its own right.'), Js('is something special indeed.'), Js('is astonishing.')]))
    var.put('random28', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names28').get('length')))))
    def PyJs_LONG_15_(var=var):
        return ((((((((((Js('This ')+var.get('names1').get(var.get('random1')))+var.get('names0').get(var.get('random0')))+Js(' creature is a type of '))+var.get('names2').get(var.get('random2')))+Js(". It's about the size of a"))+var.get('names3').get(var.get('random3')))+Js(', has '))+var.get('names4a').get(var.get('random4a')))+var.get('names4b').get(var.get('random4b')))+var.get('names4c').get(var.get('random4c')))
    var.put('name', (PyJs_LONG_15_()+Js('.')))
    def PyJs_LONG_16_(var=var):
        return ((((((((((Js('They have a ')+var.get('names5').get(var.get('random5')))+Js(' '))+var.get('names6').get(var.get('random6')))+Js(' which is usually either '))+var.get('names7a').get(var.get('random7a')))+var.get('names7b').get(var.get('random7b')))+var.get('names7c').get(var.get('random7c')))+var.get('names7c').get(var.get('random7d')))+var.get('names7d').get(var.get('random7e')))+Js(' or a combination of these colors.'))
    var.put('name2', PyJs_LONG_16_())
    def PyJs_LONG_17_(var=var):
        return (((((((((((((Js('They live in ')+var.get('names8').get(var.get('random8')))+Js(' and are '))+var.get('names9').get(var.get('random9')))+Js(". They're "))+var.get('names10').get(var.get('random10')))+Js(' and their '))+var.get('names11').get(var.get('random11')))+Js(' '))+var.get('names11a'))+Js(' and '))+var.get('names12').get(var.get('random12')))+Js(' tongue are ideal for eating '))+var.get('names13').get(var.get('random13')))
    var.put('name3', (PyJs_LONG_17_()+Js('.')))
    var.put('name6', ((((((Js('They make sounds ranging from ')+var.get('names21').get(var.get('random21a')))+Js(' to '))+var.get('names21').get(var.get('random21b')))+Js(' and have a '))+var.get('names22').get(var.get('random22')))+Js(' range of sounds they make to indicate discoveries, dangers and otherwise communicate with each other.')))
    def PyJs_LONG_18_(var=var):
        return (((((((((((Js('These creatures are ')+var.get('names23').get(var.get('random23')))+var.get('names23b'))+var.get('names24').get(var.get('random24')))+Js(' They mate '))+var.get('names25').get(var.get('random25')))+Js(' and they '))+var.get('names26').get(var.get('random26')))+Js('. Which, with their '))+var.get('names27').get(var.get('random27')))+Js(', '))+var.get('names28').get(var.get('random28')))
    var.put('name7', PyJs_LONG_18_())
    pass
    pass
    var.put('result', Js([]))
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
creatureDescriptions = var.to_python()