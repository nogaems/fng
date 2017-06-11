__all__ = ['fancyClothes']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['ns9', 'nm1', 'nm11', 'rnd18', 'rnd15', 'rnd19', 'rnd11', 'nm16', 'rnd8', 'name', 'ns2', 'ns5', 'nm3', 'ns16', 'ns6', 'rnd14', 'ns7', 'ns15', 'rnd17', 'name3', 'nm2', 'rnd2', 'ns19', 'ns11', 'rnd21b', 'br', 'type', 'name2', 'ns18', 'nm14', 'ns1', 'tp', 'nm7', 'nm10', 'name4', 'ns17', 'nm15', 'ns21', 'rnd5', 'nm12', 'nm5', 'ns12', 'ns14', 'rnd4', 'ns10', 'rnd7', 'ns20', 'result', 'rnd21a', 'nm6', 'rnd6', 'rnd20', 'rnd13', 'ns4', 'ns13', 'nm4', 'rnd3', 'nm8', 'name5', 'nm17', 'nm13', 'nm9', 'rnd10', 'rnd16', 'rnd9', 'rnd12', 'rnd1', 'ns3'])
    var.put('tp', var.get('type'))
    var.put('nm1', Js([Js('covers her shoulders halfway'), Js('covers her shoulders entirely'), Js('covers her shoulders almost fully'), Js('covers her shoulders only barely with 2 spaghetti straps'), Js('leaves the top of her shoulders uncovered, but does cover the sides'), Js('leaves her shoulders mostly uncovered'), Js("leaves her shoulders uncovered, instead it's supported around her neck"), Js('covers just one of her shoulders, leaves the other uncovered'), Js('covers only a small portion of her shoulders')]))
    var.put('nm2', Js([Js('an elegant'), Js('a graceful'), Js('a stylish'), Js('a delicate'), Js('a simple'), Js('a modest'), Js('a fancy'), Js('a beautiful'), Js('a tasteful')]))
    var.put('nm3', Js([Js('Queen Anne neckline'), Js('court neckline'), Js('cowl neckline'), Js('draped neckline'), Js('halter neckline'), Js('jewel neckline'), Js('keyhole neckline'), Js('plunging neckline'), Js('round neckline'), Js('scoop neckline'), Js('semi-sweetheart neckline'), Js('square neckline'), Js('sweetheart neckline'), Js('v-neck')]))
    var.put('nm4', Js([Js('tight'), Js('snug'), Js('close'), Js('loose'), Js('comfortable'), Js('relaxed')]))
    var.put('nm5', Js([Js('accentuates her breasts, but it does so in an elegant manner'), Js('puts the focus on her breasts, but in a graceful manner'), Js('emphasizes her breasts in an elegant and dignified manner'), Js('highlights her breasts, but it does so in a refined and modest manner'), Js('helps to accentuate her breasts without making it look tacky'), Js('makes the dress look sleek and elegant'), Js('adds to the grace and elegance of the dress'), Js('gives the dress a classy and polished look'), Js('makes the dress look smart and stylish'), Js('is meant to draw attention to her breasts, but in a graceful and elegant manner'), Js('removes the focus from her breasts, but without making it look sloppy'), Js('covers up her breasts, but does so without making it look awkward or messy'), Js('helps remove some of the unwanted attention on her breasts, but does so by still looking elegant'), Js('makes the dress look comfortable, yet elegant and stylish'), Js('gives the dress a relaxed, yet graceful look'), Js('makes the dress both enjoyable to wear and look at')]))
    var.put('nm6', Js([Js('have been left uncovered'), Js('are completely uncovered'), Js('are only covered at her shoulders'), Js('have been covered to only just below her shoulders'), Js('have been covered only halfway down'), Js('have been covered to just above her elbows'), Js('have been covered to just below her elbows'), Js('have been covered to about her elbows'), Js('have been covered fully'), Js('have been covered to just above her wrists'), Js('have been covered all the way down to her wrists'), Js('have been covered completely')]))
    var.put('nm7', Js([Js('A good choice too, as her skin and the color of the dress form a perfect combination'), Js("Which is a good thing too, her silky skin isn't something you want to cover up"), Js('A choice which adds to the elegance and grace of the dress'), Js('Which not only helps accentuate her gorgeous skin, it also keeps the focus on other parts of the dress'), Js('The sleeves broaden towards the bottom and playfully accentuate her skin'), Js('The sleeves are a loose fit and, in a way, help put focus on her soft skin'), Js('The sleeves start out loose and tighten towards the bottom where they form a perfect match with the color of her skin'), Js('The sleeves are simply, yet elegant. A perfect combination of grace and style'), Js('The sleeves broaden towards the bottom, allowing for bracelets to be visible'), Js('The sleeves are a loose fit from top to bottom, giving the dress a slightly casual look'), Js('The sleeves start out loose and tighten towards the bottom where they wrap graceful around her wrists'), Js('The sleeves are a tight, but comfortable fit from top to bottom, allowing for enough movement while still looking stylish')]))
    var.put('nm8', Js([Js('narrow'), Js('thin'), Js('broad'), Js('wide')]))
    var.put('nm9', Js([Js('loose fit'), Js('comfortable fit'), Js('slim fit'), Js('tight fit')]))
    var.put('nm10', Js([Js("It's not decorated with anything in order to create a graceful, flowing look"), Js("It's left simple, elegant and undecorated, creating a look that flows from top to bottom"), Js('A bow has been wrapped around her waist and positioned slightly to one side'), Js('A bow has been wrapped around her and rests gently on her belly'), Js('A bow has been wrapped around her and rests gentle on her lower back'), Js('A small, elegant belt helps accentuate her waist without being too much'), Js('A cloth ribbon has been wrapped around her and tied in the front'), Js('A cloth ribbon has been wrapped around her and is tied on one side'), Js('A large belt helps accentuate her waist in a stylish manner'), Js('A small, stylish belt is all that is needed as a perfect adornment'), Js('An elastic band within the dress perfectly accentuates her waist and breaks up the dress nicely')]))
    var.put('nm11', Js([Js('widens and has multiple symmetric layers from top to bottom'), Js('widens and has several asymmetric layers from top to bottom'), Js('widens and has multiple symmetric layers towards the bottom'), Js('widens and has multiple diagonal layers from top to bottom'), Js('widens and has several asymmetric layers towards the bottom'), Js('widens into a ball gown-like style dress'), Js('widens and forms a round, balloon-style dress'), Js('widens and has a princess dress style'), Js('widens and has a sundress style'), Js('widens and has a trapeze style'), Js('widens slightly and has a pleat style'), Js('widens and has a box pleated style'), Js('widens every so slightly and has an accordion style'), Js('widens and has a ruffle style from top to bottom'), Js('widens and has a ruffle style towards the bottom'), Js('widens and has a gypsy dress style'), Js('widens and has a symmetric draped style'), Js('widens and has an asymmetric draped style'), Js('widens and has a tiered style'), Js('widens and has a bell style'), Js('widens and has a gathered style'), Js('fits snug around her and has a draped style'), Js('fits snug around her and has a flounded style at the bottom'), Js('fits snug around her and has a suit skirt style'), Js('fits snug around her and has a pleated style'), Js('fits snug around her and has a mermaid style'), Js('fits snug around her and has a pencil style'), Js('fits snug around her and has a tulip style'), Js('fits snug around her and has a tube style'), Js('fits snug around her and has a sarong style'), Js('fits snug around her and has a sundress style'), Js('fits snug around her and has a straight style'), Js('fits snug around her and has a fish tail style'), Js('fits snug around her and has a wrap style'), Js('fits snug around her and has an accordion style')]))
    var.put('nm12', Js([Js('to just below her knees'), Js('to just above her knees'), Js('all the way down to her feet'), Js('all the way down, almost covering her feet'), Js('to just above her ankles'), Js('to well above her ankles'), Js('all the way down to the ground')]))
    var.put('nm13', Js([Js('the same length all around'), Js('the same length all around'), Js('the same length all around'), Js('the same length all around'), Js('the same length all around'), Js('the same length all around'), Js('slightly longer in the back'), Js('slightly longer at the sides'), Js('slightly longer at the sides and back of the dress'), Js('longer in the back'), Js('longer at the sides'), Js('longer at the sides and back of the dress')]))
    var.put('nm14', Js([Js('kitten heels'), Js('stilettos'), Js('slingbacks'), Js('pumps'), Js('ballerina flats'), Js('open toes'), Js('t-straps'), Js('ankle straps'), Js('cone heels'), Js('Mary Janes'), Js('scarpins'), Js('peep toes'), Js('platforms'), Js('wedges')]))
    var.put('nm15', Js([Js('which matches the dress perfectly'), Js('an ideal match for this dress'), Js('which further adds elegance and class'), Js('which goes hand in hand with this dress'), Js('which adds simplicity and elegance'), Js('a perfect choice in combination with this dress'), Js("they're simple, but radiate grace and refinement"), Js('a strange, yet seemingly perfect choice'), Js("no other shoe would've matched this dress better"), Js('gorgeous on their own, an ideal match in combination with the dress ')]))
    var.put('nm16', Js([Js('a simple, but stylish necklace'), Js('an intricately designed necklace'), Js('a gorgeous necklace'), Js('a subtle necklace'), Js('an ornate necklace'), Js('a lavish necklace'), Js('a simple, but stylish hat'), Js('a small, elegant hat'), Js('a gorgeous wide hat'), Js('a bow in her hair')]))
    var.put('nm17', Js([Js('one simple, but elegant bracelet'), Js('an ornate bracelet'), Js('an embroidered bracelet'), Js('an opulent bracelet'), Js('several lavish bracelets'), Js('several elegant bracelets'), Js('several jeweled bracelets'), Js('several gilded bracelets'), Js('small jeweled earrings'), Js('large jeweled earrings'), Js('small, stylish earrings'), Js('large, stylish earrings')]))
    var.put('ns1', Js([Js('simple shirt'), Js('clean shirt'), Js('smooth shirt'), Js('plain shirt'), Js('standard shirt')]))
    var.put('ns2', Js([Js('left it unbuttoned at the top for a more casual look'), Js("buttoned it up fully to support the elegant tie he's wearing"), Js("buttoned it up fully to support the graceful bow tie he's wearing")]))
    var.put('ns3', Js([Js('stylish'), Js('classy'), Js('trendy'), Js('chic'), Js('sleek')]))
    var.put('ns4', Js([Js('3'), Js('4'), Js('5'), Js('6'), Js('7')]))
    var.put('ns5', Js([Js("deep v-line, which causes the vest to remain hidden when the suit's jacket is buttoned up"), Js("narrow v-line, which allows for the top to remain visible even when the suit's jacket is buttoned up"), Js("very narrow v-line, which allows for a large portion of the top to remain visible, even if the suit's jacket is buttoned up"), Js("fairly deep v-line, which causes the vest to line up perfectly with the jacket's v-line when it's button up"), Js("fairly deep v-line, it's just narrow enough for the top to remain visible, adding another layer to the overal look of the suit")]))
    var.put('ns6', Js([Js('is a perfectly tailored fit for him'), Js('fits him like a glove, a tailored glove'), Js('perfectly wraps around his body'), Js("was clearly made for him, it's a perfect fit")]))
    var.put('ns7', Js([Js("It's a solid color without a pattern which radiates finesse"), Js('It has a subtle pinstripe pattern which gives the suit an elegant look'), Js('It has a smooth chalk stripe pattern which gives the suit a refined look'), Js('It has an intricate rope strike pattern which makes it look stylish and graceful'), Js('It has an elegant windowpane pattern which radiates confidence'), Js('It has an intricate, but subtle plaid pattern, giving the suit a stylish casual look'), Js('It has an elaborate houndstooth pattern which gives the suit a sporty, yet stylish look'), Js('It has a tight herringbone pattern which gives the suit a more formal and elegant look'), Js('It has a wide herringbone pattern which gives the suit a classy and graceful look'), Js('It has an elaborate checked plaid pattern which gives the suit a fancy affluent look'), Js('It has a simple, but elegant blanket plaid pattern, giving the suit a dignified and elegant look')]))
    var.put('ns9', Js([Js('3'), Js('4'), Js('5'), Js('6')]))
    var.put('ns10', Js([Js('single breasted'), Js('double breasted')]))
    var.put('ns11', Js([Js("are all buttoned up, it's the only right way to wear it"), Js('are all buttoned up, he wants to look stylish after all'), Js('are all buttoned up, giving him a sophisticated look'), Js('are all buttoned up, a stylish and elegant choice'), Js("are all buttoned up, it's the best way to wear a jacket like this after all"), Js('are all buttoned up with the exception of one, a playful touch to a classy look'), Js('are all buttoned up with the exception of one, it adds a casual touch to an elegant look'), Js('are all buttoned up with the exception of one, a subtle touch of nonchalance which works perfectly'), Js('are all buttoned up with the exception of one, it gives the suit a bit of both worlds, casual and stylish'), Js('are all buttoned up with the exception of one, a subtle but very effective touch of informality'), Js("have been left unbuttoned, it's a casual look which still manages to look classy"), Js("have been left unbuttoned, he's clearly going for a more casual look, but at the same time he looks elegant as well"), Js('have been left unbuttoned, he wants to appear well dressed while still looking casual and it works'), Js('have been left unbuttoned, this suit is meant to be worn this way. Casual, yet graceful at the same time'), Js("have been left unbuttoned, buttoned up would've made the overall look too fancy for his taste")]))
    var.put('ns12', Js([Js('the same length all around'), Js('the same length all around'), Js('slightly longer at the back'), Js('longer at the back'), Js('the same length all around')]))
    var.put('ns13', Js([Js('no vent'), Js('a vent at the back'), Js('vents at either side')]))
    var.put('ns14', Js([Js("there's a pocket on either side"), Js("there's a single pocket on one side"), Js('there are two pockets on one side and one pocket on the other'), Js('there are two pockets on either side'), Js("there's a pocket on either side")]))
    var.put('ns15', Js([Js('which contains a stylish pocket square'), Js('which has been left empty'), Js('which contains a stylish pocket square'), Js('which has been left empty'), Js('which contains a pocket watch'), Js('which holds his sunglasses')]))
    var.put('ns16', Js([Js('copy the style of the jacket, both in color and pattern'), Js('copy the style of the jacket, both in color and pattern'), Js('copy the style of the jacket, both in color and pattern'), Js('have the same pattern as the jacket, but a different, complementary color'), Js('have the same color as the jacket, but a slightly different pattern'), Js('have a different style than the jacket, but they complement each other perfectly')]))
    var.put('ns17', Js([Js("they're a perfect match for his"), Js('they perfectly complement his'), Js('they make an ideal combination with his'), Js('they create a perfect balance with his')]))
    var.put('ns18', Js([Js('a stylish'), Js('a lavish'), Js('an elegant'), Js('a classy'), Js('a modest'), Js('a sharp'), Js('a fancy'), Js('a chich'), Js('a handsome'), Js('a graceful')]))
    var.put('ns19', Js([Js('brogue derbies'), Js('brogue monkstraps'), Js('brogue oxfords'), Js('cap toe balmorals'), Js('cap toe monkstraps'), Js('cap toe oxfords'), Js('fullstrap loafers'), Js('horsebit loafers'), Js('longwing bluchers'), Js('medallian cap toe oxfords'), Js('moc toe penny loafers'), Js('penny loafers'), Js('perf toe balmorals'), Js('plain toe bluchers'), Js('plain toe derbies'), Js('plain toe monkstraps'), Js('plain toe oxfords'), Js('shortwing bluchers'), Js('spectator oxfords'), Js('split toe bluchers'), Js('split toe derbies'), Js('wholecut oxfords')]))
    var.put('ns20', Js([Js('an elegant'), Js('a stylish'), Js('a sleek'), Js('a trendy'), Js('a fancy'), Js('a luxurious'), Js('a graceful'), Js('a refined'), Js('a modest'), Js('a classic')]))
    var.put('ns21', Js([Js('gloves'), Js('cuff links'), Js('a hat'), Js('a watch'), Js('a tie clip'), Js('a scarf'), Js('a brooch')]))
    if PyJsStrictEq(var.get('tp'),Js(1.0)):
        var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns1').get('length')))))
        var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns2').get('length')))))
        var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns3').get('length')))))
        var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns4').get('length')))))
        var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns5').get('length')))))
        var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns6').get('length')))))
        var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns7').get('length')))))
        var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns9').get('length')))))
        var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns10').get('length')))))
        var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns11').get('length')))))
        if PyJsStrictEq(var.get('rnd10'),Js(1.0)):
            while (var.get('rnd11')>Js(9.0)):
                var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns11').get('length')))))
        var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns12').get('length')))))
        var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns13').get('length')))))
        var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns14').get('length')))))
        var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns15').get('length')))))
        var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns16').get('length')))))
        var.put('rnd17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns17').get('length')))))
        var.put('rnd18', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns18').get('length')))))
        var.put('rnd19', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns19').get('length')))))
        var.put('rnd20', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns20').get('length')))))
        var.put('rnd21a', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns21').get('length')))))
        var.put('rnd21b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns21').get('length')))))
        while PyJsStrictEq(var.get('rnd21a'),var.get('rnd21b')):
            var.put('rnd21b', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('ns21').get('length')))))
        var.put('name', ((((((((((Js("He's wearing a ")+var.get('ns1').get(var.get('rnd1')))+Js(' and '))+var.get('ns2').get(var.get('rnd2')))+Js(". On top of the shirt he's wearing a "))+var.get('ns3').get(var.get('rnd3')))+Js(' vest with '))+var.get('ns4').get(var.get('rnd4')))+Js(' buttons, it has a '))+var.get('ns5').get(var.get('rnd5')))+Js('.')))
        var.put('name2', ((((((((((Js('The jacket ')+var.get('ns6').get(var.get('rnd6')))+Js('. '))+var.get('ns7').get(var.get('rnd7')))+Js('. The '))+var.get('ns9').get(var.get('rnd9')))+Js(' buttons of his '))+var.get('ns10').get(var.get('rnd10')))+Js(' jacket '))+var.get('ns11').get(var.get('rnd11')))+Js('.')))
        var.put('name3', ((((((((Js('The jacket is ')+var.get('ns12').get(var.get('rnd12')))+Js(', it has '))+var.get('ns13').get(var.get('rnd13')))+Js(', '))+var.get('ns14').get(var.get('rnd14')))+Js(" and there's a breast pocket "))+var.get('ns15').get(var.get('rnd15')))+Js('.')))
        var.put('name4', ((((((((Js("He's wearing pants which ")+var.get('ns16').get(var.get('rnd16')))+Js(' and '))+var.get('ns17').get(var.get('rnd17')))+Js(" shoes. He's wearing "))+var.get('ns18').get(var.get('rnd18')))+Js(' pair of '))+var.get('ns19').get(var.get('rnd19')))+Js('.')))
        var.put('name5', ((((((Js("To top it all off he's wearing ")+var.get('ns20').get(var.get('rnd20')))+Js(' belt, which can be accompanied by '))+var.get('ns21').get(var.get('rnd21a')))+Js(' and '))+var.get('ns21').get(var.get('rnd21b')))+Js('.')))
        var.put('br', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<Js(6.0)):
            try:
                pass
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        pass
        var.put('result', Js([]))
        return var.get('result')
    else:
        var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
        var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
        var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
        var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
        var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
        if (var.get('rnd4')>Js(2.0)):
            while (var.get('rnd5')<Js(10.0)):
                var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
        var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
        var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
        if (var.get('rnd6')<Js(4.0)):
            while (var.get('rnd7')>Js(3.0)):
                var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
        else:
            if (var.get('rnd6')<Js(8.0)):
                while ((var.get('rnd7')<Js(4.0)) or (var.get('rnd7')>Js(7.0))):
                    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
            else:
                if (var.get('rnd6')>Js(7.0)):
                    while (var.get('rnd7')<Js(8.0)):
                        var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
        var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
        var.put('rnd9', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length')))))
        var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
        var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
        var.put('rnd12', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length')))))
        var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
        var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
        var.put('rnd15', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length')))))
        var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
        var.put('rnd17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
        var.put('name', ((((((((((Js('The dress ')+var.get('nm1').get(var.get('rnd1')))+Js(' and flows down into '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3')))+Js(". It's a "))+var.get('nm4').get(var.get('rnd4')))+Js(' fit which '))+var.get('nm5').get(var.get('rnd5')))+Js('.')))
        var.put('name2', ((((Js('Her arms ')+var.get('nm6').get(var.get('rnd6')))+Js('. '))+var.get('nm7').get(var.get('rnd7')))+Js('.')))
        var.put('name3', ((((((Js("The dress' waist is ")+var.get('nm8').get(var.get('rnd8')))+Js(", but it's a "))+var.get('nm9').get(var.get('rnd9')))+Js('. '))+var.get('nm10').get(var.get('rnd10')))+Js('.')))
        var.put('name4', ((((((Js('Below the waist the dress ')+var.get('nm11').get(var.get('rnd11')))+Js('. The dress reaches '))+var.get('nm12').get(var.get('rnd12')))+Js(' and is '))+var.get('nm13').get(var.get('rnd13')))+Js('.')))
        var.put('name5', ((((((((Js("She's wearing ")+var.get('nm14').get(var.get('rnd14')))+Js(', '))+var.get('nm15').get(var.get('rnd15')))+Js(". To top it all off she's wearing "))+var.get('nm16').get(var.get('rnd16')))+Js(' and '))+var.get('nm17').get(var.get('rnd17')))+Js('.')))
        var.put('br', Js([]))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<Js(6.0)):
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
fancyClothes = var.to_python()