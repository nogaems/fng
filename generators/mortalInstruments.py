__all__ = ['mortalInstruments']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
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
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
            var.put('nl', (var.get('nm4').get(var.get('rnd2'))+var.get('nm5').get(var.get('rnd3'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nl')))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nl')))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nl')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Aaron'), Js('Adam'), Js('Aidan'), Js('Aiden'), Js('Alex'), Js('Alexander'), Js('Alfie'), Js('Andrew'), Js('Anthony'), Js('Archie'), Js('Arthur'), Js('Ashton'), Js('Bailey'), Js('Ben'), Js('Benjamin'), Js('Billy'), Js('Blake'), Js('Bobby'), Js('Bradley'), Js('Brandon'), Js('Caleb'), Js('Callum'), Js('Cameron'), Js('Charles'), Js('Charlie'), Js('Christopher'), Js('Cody'), Js('Connor'), Js('Corey'), Js('Daniel'), Js('David'), Js('Declan'), Js('Dexter'), Js('Dominic'), Js('Dylan'), Js('Edward'), Js('Elliot'), Js('Ellis'), Js('Ethan'), Js('Evan'), Js('Ewan'), Js('Finlay'), Js('Finley'), Js('Frankie'), Js('Freddie'), Js('Frederick'), Js('Gabriel'), Js('George'), Js('Harley'), Js('Harrison'), Js('Harry'), Js('Harvey'), Js('Hayden'), Js('Henry'), Js('Isaac'), Js('Jack'), Js('Jackson'), Js('Jacob'), Js('Jake'), Js('James'), Js('Jamie'), Js('Jay'), Js('Jayden'), Js('Jenson'), Js('Joe'), Js('Joel'), Js('John'), Js('Jonathan'), Js('Jordan'), Js('Joseph'), Js('Josh'), Js('Joshua'), Js('Jude'), Js('Kai'), Js('Kayden'), Js('Kian'), Js('Kieran'), Js('Kyle'), Js('Leo'), Js('Leon'), Js('Lewis'), Js('Liam'), Js('Logan'), Js('Louie'), Js('Louis'), Js('Luca'), Js('Lucas'), Js('Luke'), Js('Mason'), Js('Matthew'), Js('Max'), Js('Michael'), Js('Morgan'), Js('Nathan'), Js('Nicholas'), Js('Noah'), Js('Oliver'), Js('Ollie'), Js('Oscar'), Js('Owen'), Js('Patrick'), Js('Peter'), Js('Reece'), Js('Reuben'), Js('Rhys'), Js('Riley'), Js('Robert'), Js('Rory'), Js('Ryan'), Js('Sam'), Js('Samuel'), Js('Scott'), Js('Sean'), Js('Sebastian'), Js('Spencer'), Js('Stanley'), Js('Taylor'), Js('Theo'), Js('Thomas'), Js('Toby'), Js('Tom'), Js('Tommy'), Js('Tyler'), Js('William'), Js('Zac'), Js('Zachary'), Js('Zak')]))
var.put('nm2', Js([Js('Abbie'), Js('Abby'), Js('Abigail'), Js('Aimee'), Js('Alexandra'), Js('Alice'), Js('Alicia'), Js('Alisha'), Js('Amber'), Js('Amelia'), Js('Amelie'), Js('Amy'), Js('Anna'), Js('Ava'), Js('Bella'), Js('Bethany'), Js('Brooke'), Js('Caitlin'), Js('Cerys'), Js('Charlie'), Js('Charlotte'), Js('Chelsea'), Js('Chloe'), Js('Courtney'), Js('Daisy'), Js('Danielle'), Js('Demi'), Js('Eleanor'), Js('Eliza'), Js('Elizabeth'), Js('Ella'), Js('Ellie'), Js('Eloise'), Js('Elsie'), Js('Emilia'), Js('Emily'), Js('Emma'), Js('Erin'), Js('Esme'), Js('Eva'), Js('Eve'), Js('Evelyn'), Js('Evie'), Js('Faith'), Js('Freya'), Js('Georgia'), Js('Georgina'), Js('Grace'), Js('Gracie'), Js('Hannah'), Js('Harriet'), Js('Heidi'), Js('Hollie'), Js('Holly'), Js('Imogen'), Js('Isabel'), Js('Isabella'), Js('Isabelle'), Js('Isla'), Js('Isobel'), Js('Jade'), Js('Jasmine'), Js('Jennifer'), Js('Jessica'), Js('Jodie'), Js('Julia'), Js('Kate'), Js('Katherine'), Js('Katie'), Js('Kayla'), Js('Kayleigh'), Js('Keira'), Js('Lacey'), Js('Lara'), Js('Laura'), Js('Lauren'), Js('Layla'), Js('Leah'), Js('Lexi'), Js('Lexie'), Js('Libby'), Js('Lilly'), Js('Lily'), Js('Lola'), Js('Louise'), Js('Lucy'), Js('Lydia'), Js('Maddison'), Js('Madeleine'), Js('Madison'), Js('Maisie'), Js('Maisy'), Js('Maria'), Js('Martha'), Js('Matilda'), Js('Maya'), Js('Megan'), Js('Melissa'), Js('Mia'), Js('Millie'), Js('Mollie'), Js('Molly'), Js('Morgan'), Js('Mya'), Js('Naomi'), Js('Natasha'), Js('Niamh'), Js('Nicole'), Js('Olivia'), Js('Paige'), Js('Phoebe'), Js('Poppy'), Js('Rachel'), Js('Rebecca'), Js('Rose'), Js('Rosie'), Js('Ruby'), Js('Samantha'), Js('Sara'), Js('Sarah'), Js('Scarlett'), Js('Shannon'), Js('Sienna'), Js('Skye'), Js('Sofia'), Js('Sophia'), Js('Sophie'), Js('Summer'), Js('Tegan'), Js('Tia'), Js('Tilly'), Js('Victoria'), Js('Willow'), Js('Yasmin'), Js('Zara'), Js('Zoe')]))
var.put('nm3', Js([Js('Aaren'), Js('Addison'), Js('Aiden'), Js('Alex'), Js('Alexis'), Js('Ali'), Js('Angel'), Js('Ash'), Js('Ashley'), Js('Ashton'), Js('Aubrey'), Js('Avery'), Js('Bailey'), Js('Bennie'), Js('Bev'), Js('Billie'), Js('Billy'), Js('Blair'), Js('Blake'), Js('Bret'), Js('Brett'), Js('Brice'), Js('Brook'), Js('Brynn'), Js('Caden'), Js('Cameron'), Js('Carmen'), Js('Carol'), Js('Casey'), Js('Charlie'), Js('Chris'), Js('Clem'), Js('Cory'), Js('Dane'), Js('Danni'), Js('Danny'), Js('Denny'), Js('Drew'), Js('Eli'), Js('Elliot'), Js('Emerson'), Js('Erin'), Js('Fran'), Js('Frankie'), Js('Franky'), Js('Gabby'), Js('Gabe'), Js('Gail'), Js('Gale'), Js('Gene'), Js('Glen'), Js('Glenn'), Js('Haiden'), Js('Harley'), Js('Harper'), Js('Hayden'), Js('Jackie'), Js('Jaden'), Js('Jaime'), Js('Jamie'), Js('Jess'), Js('Jesse'), Js('Jessie'), Js('Jo'), Js('Jody'), Js('Jordan'), Js('Jude'), Js('Justice'), Js('Kai'), Js('Kerry'), Js('Kiran'), Js('Kit'), Js('Kris'), Js('Lane'), Js('Lee'), Js('Leigh'), Js('Lesley'), Js('Leslie'), Js('Logan'), Js('Lynn'), Js('Maddox'), Js('Marley'), Js('Mason'), Js('Mel'), Js('Mell'), Js('Morgan'), Js('Nicky'), Js('Noel'), Js('Phoenix'), Js('Quinn'), Js('Ray'), Js('Raylee'), Js('Reed'), Js('Reggie'), Js('Rene'), Js('Riley'), Js('River'), Js('Robin'), Js('Rory'), Js('Rowan'), Js('Rudy'), Js('Ryan'), Js('Sam'), Js('Sammy'), Js('Shay'), Js('Sidney'), Js('Silver'), Js('Skye'), Js('Skylar'), Js('Skyler'), Js('Steff'), Js('Tanner'), Js('Taylor'), Js('Terry'), Js('Tyler'), Js('Val'), Js('Vic'), Js('Will'), Js('Willy')]))
var.put('nm4', Js([Js('Alder'), Js('Amber'), Js('Ash'), Js('Autumn'), Js('Beau'), Js('Belle'), Js('Black'), Js('Bran'), Js('Bright'), Js('Cart'), Js('Clear'), Js('Cliff'), Js('Cloud'), Js('Cold'), Js('Common'), Js('Coven'), Js('Crag'), Js('Dawn'), Js('Deep'), Js('Dew'), Js('Distant'), Js('Dream'), Js('Dusk'), Js('Earth'), Js('Elder'), Js('Ember'), Js('Even'), Js('Fair'), Js('Far'), Js('Feather'), Js('Fern'), Js('Fire'), Js('Flame'), Js('Flat'), Js('Forest'), Js('Free'), Js('Full'), Js('Glad'), Js('Glory'), Js('Gold'), Js('Grand'), Js('Gray'), Js('Great'), Js('Hard'), Js('Haven'), Js('Hay'), Js('Heart'), Js('Heavy'), Js('High'), Js('Hill'), Js('Honor'), Js('Humble'), Js('Keen'), Js('Kings'), Js('Light'), Js('Lone'), Js('Long'), Js('Low'), Js('Meadow'), Js('Merry'), Js('Mid'), Js('Mild'), Js('Moon'), Js('Morning'), Js('Night'), Js('Noble'), Js('Pen'), Js('Plain'), Js('Pont'), Js('Pride'), Js('Proud'), Js('Rain'), Js('Raven'), Js('Regal'), Js('River'), Js('Rose'), Js('Sage'), Js('Shadow'), Js('Sharp'), Js('Shield'), Js('Silent'), Js('Silver'), Js('Simple'), Js('Single'), Js('Sky'), Js('Snow'), Js('Soft'), Js('Spirit'), Js('Spring'), Js('Star'), Js('Stark'), Js('Stern'), Js('Still'), Js('Stout'), Js('Strong'), Js('Summer'), Js('Sun'), Js('Swift'), Js('Tall'), Js('Town'), Js('Tree'), Js('True'), Js('Way'), Js('Whisper'), Js('Whit'), Js('White'), Js('Wild'), Js('Wind'), Js('Winter'), Js('Wise'), Js('Wolf'), Js('Wood'), Js('Young')]))
var.put('nm5', Js([Js('bane'), Js('beam'), Js('bloom'), Js('blossom'), Js('bluff'), Js('born'), Js('bough'), Js('bow'), Js('braid'), Js('branch'), Js('brand'), Js('breath'), Js('breeze'), Js('brook'), Js('brow'), Js('child'), Js('creek'), Js('crest'), Js('cross'), Js('dale'), Js('dew'), Js('down'), Js('draft'), Js('dream'), Js('fall'), Js('flare'), Js('flaw'), Js('fleur'), Js('flow'), Js('flower'), Js('force'), Js('ford'), Js('gaze'), Js('gem'), Js('glade'), Js('gleam'), Js('glide'), Js('grove'), Js('guard'), Js('hallow'), Js('heart'), Js('hood'), Js('keep'), Js('lace'), Js('land'), Js('law'), Js('less'), Js('man'), Js('mark'), Js('mercy'), Js('might'), Js('mill'), Js('more'), Js('peace'), Js('ridge'), Js('root'), Js('run'), Js('scar'), Js('send'), Js('shade'), Js('sky'), Js('smith'), Js('soar'), Js('song'), Js('spark'), Js('stern'), Js('stone'), Js('stride'), Js('sun'), Js('surge'), Js('sworn'), Js('thorn'), Js('tide'), Js('tower'), Js('tree'), Js('vale'), Js('ward'), Js('water'), Js('weather'), Js('weaver'), Js('well'), Js('whirl'), Js('wind'), Js('winds'), Js('wine'), Js('wing'), Js('winter'), Js('wood'), Js('woods'), Js('wright')]))
pass
pass


# Add lib to the module scope
mortalInstruments = var.to_python()