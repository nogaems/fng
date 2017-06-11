__all__ = ['weaponBladeDescriptions']

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
    var.registers(['nm19', 'nm1', 'nm11', 'nm24', 'rnd15', 'rnd18', 'rnd11', 'rnd19', 'rnd22', 'nm16', 'rnd8', 'name', 'nm23', 'name7', 'nm3', 'rnd14', 'rnd23', 'name3', 'rnd17', 'name6', 'nm2', 'rnd2', 'br', 'name2', 'nm22', 'nm14', 'nm7', 'nm10', 'nm21', 'name4', 'nm15', 'nm20', 'rnd21', 'rnd5', 'nm12', 'nm5', 'rnd4', 'rnd7', 'rnd24', 'result', 'nm6', 'rnd6', 'rnd20', 'rnd13', 'nm4', 'rnd3', 'nm8', 'name5', 'nm18', 'nm17', 'nm13', 'nm9', 'rnd10', 'rnd16', 'rnd9', 'rnd12', 'rnd1'])
    var.put('nm1', Js([Js('fairly large'), Js('fairly long'), Js('fairly short'), Js('fairly small'), Js('large'), Js('long'), Js('short'), Js('small'), Js('very long'), Js('very short')]))
    var.put('nm2', Js([Js('thick'), Js('thin'), Js('wide'), Js('narrow'), Js('slim'), Js('broad')]))
    var.put('nm3', Js([Js('straight'), Js('smooth'), Js('slightly curved'), Js('warped'), Js('curved'), Js('jagged'), Js('barbed')]))
    var.put('nm4', Js([Js('ceramic'), Js('diamond'), Js('copper'), Js('bronze'), Js('glass'), Js('ivory'), Js('silver'), Js('adamantium'), Js('crystal'), Js('folded steel'), Js('iron'), Js('mithril'), Js('obsidian'), Js('steel'), Js('titanium')]))
    var.put('nm5', Js([Js('common'), Js('dull'), Js('elegant'), Js('expensive'), Js('extravagant'), Js('extremely rare'), Js('fairly common'), Js('gilded'), Js('high quality'), Js('lavish'), Js('low-cost'), Js('ordinary'), Js('rare'), Js('regular'), Js('strange'), Js('uncommon')]))
    var.put('nm6', Js([Js('black'), Js('bronze'), Js('brown'), Js('dark brown'), Js('deep orange'), Js('emerald green'), Js('forest green'), Js('gold colored'), Js('green'), Js('grey'), Js('ivory'), Js('jade green'), Js('light brown'), Js('maroon'), Js('navy blue'), Js('onyx'), Js('red'), Js('royal blue'), Js('ruby red'), Js('sapphire blue'), Js('scarlet'), Js('white')]))
    var.put('nm7', Js([Js('bear leather'), Js('boar hide'), Js('buffalo skin'), Js('cow leather'), Js('crocodile leather'), Js('deerskin'), Js('goat leather'), Js('pig leather'), Js('ray skin'), Js('salmon leather'), Js('scaled leather'), Js('shark skin'), Js('smooth leather'), Js('snake leather'), Js('sting ray leather'), Js('wolf leather')]))
    var.put('nm8', Js([Js('One sharp edge'), Js('A single, sharp edge'), Js('With just one razor-sharp edge'), Js('Because its sharp on just one edge'), Js('With a single, sharp edge'), Js('A sharp, dual-edged blade'), Js('The sharp, dual-edged blade'), Js('Dual-edged and razor-sharp'), Js('With its sharp, dual-edged blade'), Js('Because its sharp on both its edges'), Js('A fine, sharp point'), Js('The razor-sharp point'), Js('With a point as sharp as a razor'), Js('With just a razor-sharp point'), Js('Because it only has a razor-sharp point')]))
    var.put('nm9', Js([Js("makes this weapon ideal for both blocking and slicing, your enemies won't stand a chance."), Js('makes this a perfect weapon to block attacks and slice enemies to tiny, little pieces.'), Js('makes sure this weapon is not just for hacking and slashing, but also great to block incoming attacks.'), Js('this weapon is ideal for both cleaving enemies as well as blocking their attacks.'), Js('this weapon will protect you from incoming blows while also giving you the ability to shred your enemies to pieces.'), Js('this weapon is the perfect choice for slicing and dicing while also offering you a way to effectively block attacks.'), Js('makes this weapon the best choice for both cleaving and stabbing your enemies with ferocious power.'), Js("makes this the ideal weapon if you're looking to slice, dice, stab and jab your enemies."), Js('makes this weapon the choice for any warrior looking for a versatile weapon ideal for any combat style.'), Js("this weapon will slice, dice, stab and jab your enemies and shred whatever's left of them."), Js("this weapon is the champion's choice. It'll crush your enemies with cleaving hacks and piercing stabs."), Js('this weapon makes for the best choice for those looking for power, versatility and general awesomeness.'), Js('makes this weapon ideal to pierce your enemies and turn them into a sieve.'), Js('makes this weapon a perfect choice if you wish to puncture your enemies to death with ruthless speed and precision.'), Js('makes this weapon the best choice if you want to pierce, prick, puncture and perforate your enemies.'), Js('this weapon is the ideal choice to turn your enemies into Swiss cheese. '), Js('this weapon will make sure your enemies are full of holes with deadly speed and precision.'), Js('this weapon will cause your enemies to leak from thousands of holes before they even know what happened.')]))
    var.put('nm10', Js([Js('small'), Js('thin'), Js('narrow'), Js('wide'), Js('broad'), Js('large'), Js('barbed'), Js('jagged'), Js('spiked')]))
    var.put('nm11', Js([Js('slightly curved'), Js('straight'), Js('curved'), Js('warped'), Js('twisted'), Js('curled')]))
    var.put('nm12', Js([Js("just large enough to protect the owner's fingers"), Js('just large enough to prevent it from slipping from your hands'), Js('just large enough to make sure your fingers are safe and the blade will remain firmly in your hands'), Js('just large enough to give the blade the perfect weight balance'), Js("offering just enough protection to the owner's hands, as well as adding a weight balance to the blade"), Js("offering plenty of protection to the owner's hands and thus his or her life"), Js('adding weight to the blade for a better weight balance, as well as offering hand protection during battle'), Js('creating the ideal weight balance to allow for smooth and accurate swings with this blade'), Js("adding just enough weight to make sure the blade sits firmly in the owner's hand and protecting those same hands as well"), Js("which makes sure the blade is both balanced and capable of protecting the owner's hands against any sliding sword")]))
    var.put('nm13', Js([Js('a simple'), Js('a plain'), Js('a basic'), Js('an intricate'), Js('an elaborate'), Js('a decorative'), Js('a lavish'), Js('an ornamented'), Js('an elegant'), Js('a jeweled'), Js('a gilded')]))
    var.put('nm14', Js([Js('sphere'), Js('curl'), Js('coil'), Js('twist'), Js('loop'), Js('orb'), Js('ring'), Js('cross'), Js('dragon head'), Js('lion head'), Js('bear paw'), Js('hawk beak'), Js('eye'), Js('wolf head'), Js('skull'), Js('flame'), Js('miniature sword'), Js('eagle wing'), Js('horn'), Js('bear head'), Js('lion paw'), Js('panther head'), Js('claw'), Js('tooth'), Js('crow head'), Js('fish scale'), Js('snake head'), Js('owl head'), Js('dragon tail'), Js('snake'), Js('spider')]))
    var.put('nm15', Js([Js('which is common on many weapons'), Js('which shows how ordinary this weapon is'), Js('a sign of mass production'), Js('which tells you this weapon belongs to a soldier or commoner'), Js('so this weapon is for just about anybody with the right amount of cash'), Js("this weapon clearly isn't a one of a kind"), Js('marking the house it belongs to'), Js('a clear sign this weapon belongs to a champion'), Js("this weapon wasn't created by just any blacksmith"), Js('this weapon was clearly a custom order, probably by an important figure'), Js('this is clearly a weapon not meant to be wielded by a commoner'), Js('the cost of this weapon must have been high'), Js('this weapon is clearly meant to be taken care of with dedication'), Js('a unique design for a unique weapon')]))
    var.put('nm16', Js([Js('small'), Js('fairly small'), Js('large'), Js('wide'), Js('thick'), Js('massive'), Js('fairly large')]))
    var.put('nm17', Js([Js('marked'), Js('engraved'), Js('decorated'), Js('decorated')]))
    var.put('nm18', Js([Js("the sword maker's symbol"), Js("the sword maker's signature"), Js('a quality symbol'), Js('the symbol of the house this sword belongs to'), Js('the symbol of its owner'), Js('a fairly common gem'), Js('common gems'), Js('precious gems'), Js('gilded linings'), Js('a rare gem')]))
    var.put('nm19', Js([Js('a symbol one can be proud of'), Js('a symbol of true greatness'), Js('a symbol many are jealous of'), Js('a famous symbol and rightfully so'), Js('a symbol many would kill for'), Js('an unimpressive symbol at the best of times'), Js('not the most impressive symbol to be fair'), Js("a symbol which doesn't prove much"), Js('a symbol some might be embarrassed of'), Js('a decent symbol for a decent weapon'), Js('commonness for a commonly made weapon'), Js('anything better would be a waste'), Js("nothing too impressive, but that's to be expected"), Js('but the weapon is supposed to cut after all, not look fancy'), Js("but to be fair, gems aren't what makes a weapon great"), Js('fancy decorations for a fancy sword'), Js('which is to be expected from such an elegant weapon'), Js('no expense is spared for this gorgeous weapon'), Js('fine details which prove how carefully this weapon was crafted'), Js('this weapon is clearly meant for an important figure')]))
    var.put('nm20', Js([Js('bare'), Js('simple'), Js('fairly simple'), Js('unadorned'), Js('engraved'), Js('engraved')]))
    var.put('nm21', Js([Js('No markings can be found'), Js('No decorations or engraved patterns'), Js('No markings, no decorations and no engravings'), Js('No decorations of any sorts are on it'), Js('Several runes are etched into the blade'), Js('A line of text is engraved on the blade'), Js('Seemingly strange markings are carved into the blade'), Js('Ancient symbols are engraved on the blade'), Js('Intricate decorational patterns have been carefully etched into the blade'), Js('Religious symbols have been delicately etched into the blade'), Js('Several words of power have been artistically etched into the blade'), Js("The symbol of the owner's house is engraved on the blade"), Js("The owner's name has been artistically etched into the blade"), Js("The name of the owner's house has been engraved on the blade"), Js('The name of the blade has been engraved into the blade with artistic elegance')]))
    var.put('nm22', Js([Js('. Engravings are too costly and time consuming for an ordinary weapon'), Js(', an everyday weapon needs no decorations'), Js(', engravings, marks and decorations are only for special or expensive weapons'), Js(". This weapon is meant for fighting, decorations don't make you fight better"), Js('. Engravings are too costly, but perhaps the owner can have the weapon blessed instead'), Js(', with the exception of the small scratches from battle, which are perhaps the best marks for a weapon'), Js(', any engravings could only diminish the strength of the blade'), Js('. While the hilt is as elegant as its owner, the blade has to be as strong as its owner'), Js(', the blade needs no decorations, it only needs to be strong and sharp'), Js('. A sheathed sword has a hidden blade and a sword in use will be dirty and bloody, so only the hilt needs decorations'), Js(', but the blade will surely be decorated in battle'), Js(', which is supposed to give the weapon and its owner extra strength'), Js(', which adds mystery and supposedly more power to the weapon'), Js(", which, like a blessing, is supposed to protect the weapon's owner in battle"), Js(', which only adds to the elegance of this weapon, as well as its cost'), Js(', which is supposed to contain a hidden power'), Js('. This is clearly no ordinary weapon to be used by anybody'), Js('. This weapon is clearly a priced possession owned by somebody important'), Js('. A weapon this magnificent is not meant for battle'), Js(', which further adds to the uniqueness of this valuable weapon'), Js(', which hints at the purpose, as well as the age of this elegant weapon'), Js('. This weapon must be old and incredibly valuable, who knows what it has seen'), Js(', which just shows how special this weapon truly is'), Js('. This weapon is no ordinary weapon, that much is clear'), Js('. This weapon and its master are both famous and infamous throughout the world'), Js('. This weapon is feared and admired throughout the lands and rightfully so'), Js('. You would not want to meet this blade, let alone its owner, in battle')]))
    var.put('nm23', Js([Js('only during celebrations'), Js('only during special occasions'), Js('only on rare occasions'), Js('only for ceremonial purposes'), Js('only as a bragging object'), Js('only as a decorational piece'), Js('only as a display of wealth'), Js('by royalty and the noble'), Js('only by those with vast amounts of wealth'), Js('by just about anybody'), Js('by anybody with a decent amount of money'), Js('the lower ranked guards'), Js('by the royal guard'), Js('by higher ranked guards'), Js('by champions and proven fighters'), Js('by only its creator')]))
    var.put('nm24', Js([Js('A decent weapon which serves its purpose'), Js('Whatever the purpose of its owner, this weapon will be sufficient'), Js('A respectable weapon for mostly respectable people'), Js('A great weapon for proven fighters'), Js('An excellent weapon for the defense of the country'), Js('An exceptional weapon for exceptional fighters'), Js("The capable hands of the country's greatest defenders deserve nothing less than this weapon's excellence"), Js('None deserve this weapon more than the greatest fighters of all'), Js("You'd expect nothing less from such fighters"), Js('Worn by the wealthiest among us, but not always the most deserving among us'), Js('Worn by the high and mighty as a display of status, wealth and power'), Js('An elegant and valuable weapon for mostly elegant and respectable people'), Js('Perhaps not great in battle, but definitely great at showing off wealth and power'), Js('An exceptional weapon carried by exceptional people, for better and worse'), Js('Any occasion which requires royalty also requires this weapon by their side'), Js('From royal weddings and births to cutting ribbons and slicing pie, this weapon has plenty of ceremonies to attend'), Js('A weapon this rare and magnificent is only used in the most important, royal ceremonies'), Js("This ceremonial weapon has seen king's being crowned, princes and princesses being born and kings and queens being married"), Js('While not rare and impressive enough for the most important celebrations, this weapon has seen its fair share of ceremonies')]))
    var.put('rnd1', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length')))))
    var.put('rnd2', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length')))))
    var.put('rnd3', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length')))))
    var.put('rnd4', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length')))))
    var.put('rnd5', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length')))))
    var.put('rnd6', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length')))))
    var.put('rnd7', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length')))))
    var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    if (var.get('rnd3')>Js(4.0)):
        while (var.get('rnd8')<Js(4.0)):
            var.put('rnd8', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length')))))
    if (PyJsStrictEq(var.get('rnd8'),Js(0.0)) or PyJsStrictEq(var.get('rnd8'),Js(1.0))):
        var.put('rnd9', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(2.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
    else:
        if ((var.get('rnd8')>Js(1.0)) and (var.get('rnd8')<Js(5.0))):
            var.put('rnd9', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(5.0)-Js(3.0))+Js(1.0))))+Js(3.0))))
        else:
            if (PyJsStrictEq(var.get('rnd8'),Js(5.0)) or PyJsStrictEq(var.get('rnd8'),Js(6.0))):
                var.put('rnd9', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(8.0)-Js(6.0))+Js(1.0))))+Js(6.0))))
            else:
                if ((var.get('rnd8')>Js(6.0)) and (var.get('rnd8')<Js(10.0))):
                    var.put('rnd9', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(11.0)-Js(9.0))+Js(1.0))))+Js(9.0))))
                else:
                    if (PyJsStrictEq(var.get('rnd8'),Js(10.0)) or PyJsStrictEq(var.get('rnd8'),Js(11.0))):
                        var.put('rnd9', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(14.0)-Js(12.0))+Js(1.0))))+Js(12.0))))
                    else:
                        var.put('rnd9', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(17.0)-Js(15.0))+Js(1.0))))+Js(15.0))))
    var.put('rnd10', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length')))))
    if (var.get('rnd10')<Js(2.0)):
        var.put('rnd12', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(4.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
    else:
        var.put('rnd12', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(9.0)-Js(5.0))+Js(1.0))))+Js(5.0))))
    var.put('rnd11', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length')))))
    var.put('rnd13', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length')))))
    if (var.get('rnd13')<Js(3.0)):
        var.put('rnd14', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(7.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
        var.put('rnd15', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(5.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
    else:
        var.put('rnd14', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length')))))
        var.put('rnd15', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(13.0)-Js(6.0))+Js(1.0))))+Js(6.0))))
    var.put('rnd16', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length')))))
    var.put('rnd17', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length')))))
    if (var.get('rnd17')<Js(2.0)):
        var.put('rnd18', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(4.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
    else:
        if (var.get('rnd13')<Js(3.0)):
            var.put('rnd18', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(6.0)-Js(5.0))+Js(1.0))))+Js(5.0))))
        else:
            var.put('rnd18', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(9.0)-Js(7.0))+Js(1.0))))+Js(7.0))))
    if (var.get('rnd18')<Js(4.0)):
        if (var.get('rnd13')<Js(3.0)):
            var.put('rnd19', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(9.0)-Js(5.0))+Js(1.0))))+Js(5.0))))
        else:
            var.put('rnd19', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(4.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
    else:
        if (var.get('rnd13')<Js(3.0)):
            var.put('rnd19', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(14.0)-Js(10.0))+Js(1.0))))+Js(10.0))))
        else:
            var.put('rnd19', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(19.0)-Js(15.0))+Js(1.0))))+Js(15.0))))
    var.put('rnd20', var.get('parseInt')(var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm20').get('length')))))
    if (var.get('rnd20')<Js(4.0)):
        var.put('rnd21', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(3.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
    else:
        var.put('rnd21', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(13.0)-Js(4.0))+Js(1.0))))+Js(4.0))))
    if (var.get('rnd21')<Js(4.0)):
        if (var.get('rnd13')<Js(3.0)):
            var.put('rnd22', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(6.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
        else:
            var.put('rnd22', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(10.0)-Js(7.0))+Js(1.0))))+Js(7.0))))
    else:
        if ((var.get('rnd21')<Js(12.0)) and (var.get('rnd21')>Js(3.0))):
            var.put('rnd22', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(21.0)-Js(11.0))+Js(1.0))))+Js(5.0))))
        else:
            if (var.get('rnd21')>Js(11.0)):
                var.put('rnd22', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(26.0)-Js(22.0))+Js(1.0))))+Js(22.0))))
    if (var.get('rnd22')<Js(6.0)):
        var.put('rnd23', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(11.0)-Js(9.0))+Js(1.0))))+Js(9.0))))
    else:
        if ((var.get('rnd22')<Js(11.0)) and (var.get('rnd22')>Js(5.0))):
            var.put('rnd23', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(14.0)-Js(12.0))+Js(1.0))))+Js(12.0))))
        else:
            if ((var.get('rnd22')>Js(10.0)) and (var.get('rnd22')<Js(16.0))):
                var.put('rnd23', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(3.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
            else:
                if ((var.get('rnd22')>Js(15.0)) and (var.get('rnd22')<Js(22.0))):
                    var.put('rnd23', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(8.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
                else:
                    var.put('rnd23', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(8.0)-Js(4.0))+Js(1.0))))+Js(4.0))))
    if (var.get('rnd23')<Js(3.0)):
        var.put('rnd24', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(19.0)-Js(10.0))+Js(1.0))))+Js(15.0))))
    else:
        if ((var.get('rnd23')>Js(2.0)) and (var.get('rnd23')<Js(9.0))):
            var.put('rnd24', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(14.0)-Js(10.0))+Js(1.0))))+Js(10.0))))
        else:
            if ((var.get('rnd23')>Js(8.0)) and (var.get('rnd23')<Js(12.0))):
                var.put('rnd24', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(3.0)-Js(0.0))+Js(1.0))))+Js(0.0))))
            else:
                var.put('rnd24', var.get('parseInt')((var.get('Math').callprop('floor', (var.get('Math').callprop('random')*((Js(9.0)-Js(4.0))+Js(1.0))))+Js(4.0))))
    var.put('name', ((((((((((((((Js('A ')+var.get('nm1').get(var.get('rnd1')))+Js(', '))+var.get('nm2').get(var.get('rnd2')))+Js(', '))+var.get('nm3').get(var.get('rnd3')))+Js(' blade made of '))+var.get('nm4').get(var.get('rnd4')))+Js(' is held by a grip wrapped in '))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('nm6').get(var.get('rnd6')))+Js(' '))+var.get('nm7').get(var.get('rnd7')))+Js('.')))
    var.put('name2', ((var.get('nm8').get(var.get('rnd8'))+Js(' '))+var.get('nm9').get(var.get('rnd9'))))
    var.put('name3', ((((((Js('The blade has a ')+var.get('nm10').get(var.get('rnd10')))+Js(', '))+var.get('nm11').get(var.get('rnd11')))+Js(' cross-guard, '))+var.get('nm12').get(var.get('rnd12')))+Js('.')))
    var.put('name4', ((((((Js(' The cross-guard has ')+var.get('nm13').get(var.get('rnd13')))+Js(' '))+var.get('nm14').get(var.get('rnd14')))+Js(' on each side, '))+var.get('nm15').get(var.get('rnd15')))+Js('.')))
    var.put('name5', ((((((((Js('A ')+var.get('nm16').get(var.get('rnd16')))+Js(' pommel is  '))+var.get('nm17').get(var.get('rnd17')))+Js(' with '))+var.get('nm18').get(var.get('rnd18')))+Js(', '))+var.get('nm19').get(var.get('rnd19')))+Js('.')))
    var.put('name6', (((((Js('The blade itself is ')+var.get('nm20').get(var.get('rnd20')))+Js('. '))+var.get('nm21').get(var.get('rnd21')))+var.get('nm22').get(var.get('rnd22')))+Js('.')))
    var.put('name7', ((((Js('This weapon is used ')+var.get('nm23').get(var.get('rnd23')))+Js('. '))+var.get('nm24').get(var.get('rnd24')))+Js('.')))
    var.put('br', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(7.0)):
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
weaponBladeDescriptions = var.to_python()