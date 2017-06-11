__all__ = ['throneOfGlassNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm19', 'nm1', 'nm11', 'nm12', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm16', 'nm18', 'nm14', 'nm17', 'nm3', 'nm13', 'nm7', 'nm9', 'nm10', 'nm2', 'nm15', 'nm6'])
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
            if PyJsStrictEq((var.get('i')%Js(2.0)),Js(0.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm18').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                while PyJsStrictEq(var.get('nm18').get(var.get('rnd')),var.get('nm19').get(var.get('rnd2'))):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm19').get('length'))))
                var.put('lName', (var.get('nm18').get(var.get('rnd'))+var.get('nm19').get(var.get('rnd2'))))
            else:
                if PyJsStrictEq((var.get('i')%Js(3.0)),Js(0.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('lName', ((((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm12').get(var.get('rnd4')))+var.get('nm13').get(var.get('rnd5')))+var.get('nm14').get(var.get('rnd6')))+var.get('nm15').get(var.get('rnd7'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm11').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm12').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm13').get('length'))))
                    var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm14').get('length'))))
                    var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm15').get('length'))))
                    var.put('lName', ((((var.get('nm11').get(var.get('rnd'))+var.get('nm12').get(var.get('rnd2')))+var.get('nm13').get(var.get('rnd3')))+var.get('nm14').get(var.get('rnd4')))+var.get('nm15').get(var.get('rnd5'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm17').get('length'))))
                    var.put('names', ((var.get('nm17').get(var.get('rnd'))+Js(' '))+var.get('lName')))
                else:
                    if (var.get('i')<Js(6.0)):
                        if (var.get('rnd')<Js(5.0)):
                            while (var.get('rnd5')<Js(10.0)):
                                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm10').get('length'))))
                        var.put('names', ((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm10').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                        var.put('names', ((((((((var.get('nm6').get(var.get('rnd'))+var.get('nm7').get(var.get('rnd2')))+var.get('nm8').get(var.get('rnd3')))+var.get('nm7').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd6')))+var.get('nm7').get(var.get('rnd7')))+var.get('nm10').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                if (var.get('i')<Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm16').get('length'))))
                    var.put('names', ((var.get('nm16').get(var.get('rnd'))+Js(' '))+var.get('lName')))
                else:
                    if (var.get('i')<Js(6.0)):
                        var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
                    else:
                        var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd6')))+var.get('nm2').get(var.get('rnd7')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('lName')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('ch'), Js('d'), Js('g'), Js('l'), Js('m'), Js('r'), Js('s'), Js('t'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('a'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('a'), Js('ai'), Js('ae'), Js('io'), Js('ia'), Js('ao')]))
var.put('nm3', Js([Js('b'), Js('br'), Js('d'), Js('dr'), Js('g'), Js('l'), Js('ld'), Js('lv'), Js('m'), Js('r'), Js('v'), Js('w')]))
var.put('nm4', Js([Js('b'), Js('d'), Js('g'), Js('l'), Js('m'), Js('r'), Js('v'), Js('w')]))
var.put('nm5', Js([Js('l'), Js('ll'), Js('n'), Js('nn'), Js('s')]))
var.put('nm6', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('c'), Js('f'), Js('h'), Js('k'), Js('l'), Js('m'), Js('n'), Js('s'), Js('y')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('e'), Js('i'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('e'), Js('i'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('e'), Js('i'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('e'), Js('i'), Js('e'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('e'), Js('i'), Js('e'), Js('ae'), Js('ae'), Js('ia'), Js('ea'), Js('ai')]))
var.put('nm8', Js([Js('d'), Js('f'), Js('h'), Js('l'), Js('ln'), Js('lt'), Js('m'), Js('n'), Js('nd'), Js('nr'), Js('r'), Js('s'), Js('st'), Js('sr'), Js('th')]))
var.put('nm9', Js([Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s')]))
var.put('nm10', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('ll'), Js('n'), Js('nn'), Js('s')]))
var.put('nm11', Js([Js('f'), Js('g'), Js('h'), Js('l'), Js('r'), Js('s')]))
var.put('nm12', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm13', Js([Js('ch'), Js('d'), Js('g'), Js('l'), Js('ll'), Js('mp'), Js('n'), Js('nd'), Js('nt'), Js('r'), Js('rd'), Js('s'), Js('ss'), Js('tg'), Js('th'), Js('v')]))
var.put('nm14', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('iu'), Js('ie'), Js('ia')]))
var.put('nm15', Js([Js('l'), Js('n'), Js('q'), Js('r'), Js('rd'), Js('rn'), Js('s')]))
var.put('nm16', Js([Js('Aaron'), Js('Abraham'), Js('Adam'), Js('Adrian'), Js('Aidan'), Js('Aiden'), Js('Alan'), Js('Alec'), Js('Alejandro'), Js('Alex'), Js('Alexander'), Js('Alexis'), Js('Allen'), Js('Andre'), Js('Andres'), Js('Andrew'), Js('Angel'), Js('Anthony'), Js('Antonio'), Js('Ashton'), Js('Austin'), Js('Ayden'), Js('Benjamin'), Js('Blake'), Js('Braden'), Js('Bradley'), Js('Brady'), Js('Brandon'), Js('Brayden'), Js('Brendan'), Js('Brent'), Js('Brett'), Js('Brian'), Js('Brody'), Js('Bryan'), Js('Bryce'), Js('Bryson'), Js('Caden'), Js('Caleb'), Js('Calvin'), Js('Cameron'), Js('Carlos'), Js('Carson'), Js('Carter'), Js('Casey'), Js('Cesar'), Js('Chad'), Js('Charles'), Js('Chase'), Js('Christian'), Js('Christopher'), Js('Clayton'), Js('Cody'), Js('Colby'), Js('Cole'), Js('Colin'), Js('Collin'), Js('Colton'), Js('Conner'), Js('Connor'), Js('Cooper'), Js('Corey'), Js('Cory'), Js('Craig'), Js('Cristian'), Js('Curtis'), Js('Dakota'), Js('Dalton'), Js('Damian'), Js('Daniel'), Js('Darius'), Js('David'), Js('Dennis'), Js('Derek'), Js('Derrick'), Js('Devin'), Js('Devon'), Js('Diego'), Js('Dillon'), Js('Dominic'), Js('Donald'), Js('Donovan'), Js('Douglas'), Js('Drew'), Js('Dustin'), Js('Dylan'), Js('Edgar'), Js('Eduardo'), Js('Edward'), Js('Edwin'), Js('Eli'), Js('Elias'), Js('Elijah'), Js('Emmanuel'), Js('Eric'), Js('Erick'), Js('Erik'), Js('Ethan'), Js('Evan'), Js('Fernando'), Js('Francisco'), Js('Frank'), Js('Gabriel'), Js('Gage'), Js('Garrett'), Js('Gary'), Js('Gavin'), Js('George'), Js('Giovanni'), Js('Grant'), Js('Gregory'), Js('Hayden'), Js('Hector'), Js('Henry'), Js('Hunter'), Js('Ian'), Js('Isaac'), Js('Isaiah'), Js('Ivan'), Js('Jack'), Js('Jackson'), Js('Jacob'), Js('Jaden'), Js('Jake'), Js('Jalen'), Js('James'), Js('Jared'), Js('Jason'), Js('Javier'), Js('Jayden'), Js('Jeffrey'), Js('Jeremiah'), Js('Jeremy'), Js('Jerry'), Js('Jesse'), Js('Jesus'), Js('Joel'), Js('John'), Js('Johnathan'), Js('Johnny'), Js('Jonah'), Js('Jonathan'), Js('Jonathon'), Js('Jordan'), Js('Jorge'), Js('Jose'), Js('Joseph'), Js('Joshua'), Js('Josiah'), Js('Juan'), Js('Julian'), Js('Justin'), Js('Kaden'), Js('Kaleb'), Js('Keith'), Js('Kenneth'), Js('Kevin'), Js('Kyle'), Js('Landon'), Js('Larry'), Js('Leonardo'), Js('Levi'), Js('Liam'), Js('Logan'), Js('Lucas'), Js('Luis'), Js('Luke'), Js('Malachi'), Js('Malik'), Js('Manuel'), Js('Marco'), Js('Marcus'), Js('Mario'), Js('Mark'), Js('Martin'), Js('Mason'), Js('Mathew'), Js('Matthew'), Js('Max'), Js('Maxwell'), Js('Micah'), Js('Michael'), Js('Miguel'), Js('Mitchell'), Js('Nathan'), Js('Nathaniel'), Js('Nicholas'), Js('Nicolas'), Js('Noah'), Js('Nolan'), Js('Oliver'), Js('Omar'), Js('Oscar'), Js('Owen'), Js('Parker'), Js('Patrick'), Js('Paul'), Js('Pedro'), Js('Peter'), Js('Peyton'), Js('Philip'), Js('Phillip'), Js('Preston'), Js('Randy'), Js('Raymond'), Js('Ricardo'), Js('Richard'), Js('Riley'), Js('Robert'), Js('Roberto'), Js('Ronald'), Js('Ruben'), Js('Ryan'), Js('Samuel'), Js('Scott'), Js('Sean'), Js('Sebastian'), Js('Sergio'), Js('Seth'), Js('Shane'), Js('Shawn'), Js('Spencer'), Js('Stephen'), Js('Steven'), Js('Tanner'), Js('Taylor'), Js('Thomas'), Js('Timothy'), Js('Tony'), Js('Travis'), Js('Trenton'), Js('Trevor'), Js('Tristan'), Js('Troy'), Js('Tyler'), Js('Victor'), Js('Vincent'), Js('Wesley'), Js('William'), Js('Wyatt'), Js('Xavier'), Js('Zachary')]))
var.put('nm17', Js([Js('Aaliyah'), Js('Abby'), Js('Abigail'), Js('Addison'), Js('Adriana'), Js('Adrianna'), Js('Alana'), Js('Alejandra'), Js('Alexa'), Js('Alexandra'), Js('Alexandria'), Js('Alexia'), Js('Alexis'), Js('Alicia'), Js('Alison'), Js('Allison'), Js('Alondra'), Js('Alyssa'), Js('Amanda'), Js('Amber'), Js('Amelia'), Js('Amy'), Js('Ana'), Js('Andrea'), Js('Angel'), Js('Angela'), Js('Angelica'), Js('Angelina'), Js('Anna'), Js('April'), Js('Ariana'), Js('Arianna'), Js('Ariel'), Js('Ashlee'), Js('Ashley'), Js('Ashlyn'), Js('Aubrey'), Js('Audrey'), Js('Autumn'), Js('Ava'), Js('Avery'), Js('Bailey'), Js('Bethany'), Js('Bianca'), Js('Brandi'), Js('Brandy'), Js('Breanna'), Js('Brenda'), Js('Briana'), Js('Brianna'), Js('Brittany'), Js('Brittney'), Js('Brooke'), Js('Brooklyn'), Js('Caitlin'), Js('Caitlyn'), Js('Camila'), Js('Carly'), Js('Caroline'), Js('Casey'), Js('Cassandra'), Js('Cassidy'), Js('Catherine'), Js('Charlotte'), Js('Chelsea'), Js('Chelsey'), Js('Cheyenne'), Js('Chloe'), Js('Christina'), Js('Christine'), Js('Cindy'), Js('Claire'), Js('Claudia'), Js('Courtney'), Js('Crystal'), Js('Cynthia'), Js('Daisy'), Js('Dana'), Js('Daniela'), Js('Danielle'), Js('Deanna'), Js('Delaney'), Js('Desiree'), Js('Destiny'), Js('Diamond'), Js('Diana'), Js('Dominique'), Js('Elizabeth'), Js('Ella'), Js('Ellie'), Js('Emily'), Js('Emma'), Js('Erica'), Js('Erika'), Js('Erin'), Js('Eva'), Js('Evelyn'), Js('Faith'), Js('Felicia'), Js('Gabriela'), Js('Gabriella'), Js('Gabrielle'), Js('Genesis'), Js('Gianna'), Js('Gina'), Js('Giselle'), Js('Grace'), Js('Gracie'), Js('Hailey'), Js('Haley'), Js('Hannah'), Js('Hayley'), Js('Heather'), Js('Holly'), Js('Hope'), Js('Isabel'), Js('Isabella'), Js('Isabelle'), Js('Jacqueline'), Js('Jada'), Js('Jade'), Js('Jamie'), Js('Jasmin'), Js('Jasmine'), Js('Jayla'), Js('Jazmin'), Js('Jenna'), Js('Jennifer'), Js('Jessica'), Js('Jillian'), Js('Joanna'), Js('Jocelyn'), Js('Jordan'), Js('Jordyn'), Js('Julia'), Js('Juliana'), Js('Julie'), Js('Kaitlin'), Js('Kaitlyn'), Js('Kara'), Js('Karen'), Js('Karina'), Js('Kate'), Js('Katelyn'), Js('Katherine'), Js('Kathleen'), Js('Kathryn'), Js('Katie'), Js('Katrina'), Js('Kayla'), Js('Kaylee'), Js('Kelly'), Js('Kelsey'), Js('Kendall'), Js('Kendra'), Js('Kennedy'), Js('Kiara'), Js('Kimberly'), Js('Kirsten'), Js('Krista'), Js('Kristen'), Js('Kristin'), Js('Kristina'), Js('Krystal'), Js('Kylee'), Js('Kylie'), Js('Laura'), Js('Lauren'), Js('Layla'), Js('Leah'), Js('Leslie'), Js('Liliana'), Js('Lillian'), Js('Lilly'), Js('Lily'), Js('Lindsay'), Js('Lindsey'), Js('Lisa'), Js('Lucy'), Js('Lydia'), Js('Mackenzie'), Js('Madeline'), Js('Madelyn'), Js('Madison'), Js('Makayla'), Js('Makenzie'), Js('Mallory'), Js('Margaret'), Js('Maria'), Js('Mariah'), Js('Marisa'), Js('Marissa'), Js('Mary'), Js('Maya'), Js('Mckenzie'), Js('Meagan'), Js('Megan'), Js('Meghan'), Js('Melanie'), Js('Melissa'), Js('Mercedes'), Js('Mia'), Js('Michaela'), Js('Michelle'), Js('Mikayla'), Js('Miranda'), Js('Molly'), Js('Monica'), Js('Monique'), Js('Morgan'), Js('Mya'), Js('Nancy'), Js('Naomi'), Js('Natalia'), Js('Natalie'), Js('Natasha'), Js('Nevaeh'), Js('Nicole'), Js('Olivia'), Js('Paige'), Js('Patricia'), Js('Payton'), Js('Peyton'), Js('Rachael'), Js('Rachel'), Js('Raven'), Js('Reagan'), Js('Rebecca'), Js('Rebekah'), Js('Riley'), Js('Ruby'), Js('Rylee'), Js('Sabrina'), Js('Sadie'), Js('Samantha'), Js('Sandra'), Js('Sara'), Js('Sarah'), Js('Savannah'), Js('Selena'), Js('Serenity'), Js('Shannon'), Js('Shelby'), Js('Sierra'), Js('Skylar'), Js('Sofia'), Js('Sophia'), Js('Sophie'), Js('Stephanie'), Js('Summer'), Js('Sydney'), Js('Tara'), Js('Taylor'), Js('Tiffany'), Js('Trinity'), Js('Valeria'), Js('Valerie'), Js('Vanessa'), Js('Veronica'), Js('Victoria'), Js('Whitney'), Js('Yesenia'), Js('Zoe'), Js('Zoey')]))
var.put('nm18', Js([Js('Amber'), Js('Ash'), Js('Autumn'), Js('Black'), Js('Blaze'), Js('Blue'), Js('Boulder'), Js('Bright'), Js('Bronze'), Js('Cask'), Js('Cinder'), Js('Clean'), Js('Clear'), Js('Cliff'), Js('Cloud'), Js('Col'), Js('Com'), Js('Coven'), Js('Crag'), Js('Crest'), Js('Dark'), Js('Dawn'), Js('Day'), Js('Dust'), Js('Ember'), Js('Even'), Js('Far'), Js('Fern'), Js('Flat'), Js('Flin'), Js('For'), Js('Fore'), Js('Forest'), Js('Free'), Js('Full'), Js('Fuse'), Js('Glow'), Js('Gol'), Js('Grand'), Js('Gray'), Js('Great'), Js('Green'), Js('Har'), Js('Hard'), Js('Heart'), Js('Hel'), Js('Hell'), Js('Hi'), Js('High'), Js('Hill'), Js('Ice'), Js('Iron'), Js('Keen'), Js('Li'), Js('Light'), Js('Lone'), Js('Long'), Js('Low'), Js('Mil'), Js('Mour'), Js('Nigh'), Js('Night'), Js('Orb'), Js('Pale'), Js('Pine'), Js('Plain'), Js('Pride'), Js('Proud'), Js('Rough'), Js('Shade'), Js('Shadow'), Js('Silent'), Js('Silver'), Js('Snow'), Js('Soft'), Js('Spring'), Js('Star'), Js('Still'), Js('Stone'), Js('Storm'), Js('Stout'), Js('Strong'), Js('Summer'), Js('Thunder'), Js('True'), Js('Whit'), Js('White'), Js('Wild'), Js('Wind'), Js('Winter'), Js('Wise'), Js('Wolf'), Js('Wood'), Js('Young')]))
var.put('nm19', Js([Js('ash'), Js('bane'), Js('beak'), Js('beam'), Js('beard'), Js('bend'), Js('bind'), Js('bluff'), Js('bough'), Js('bow'), Js('brace'), Js('branch'), Js('brand'), Js('brew'), Js('brook'), Js('brooke'), Js('brow'), Js('cloud'), Js('crag'), Js('creek'), Js('crest'), Js('dew'), Js('down'), Js('fall'), Js('fallow'), Js('flaw'), Js('flow'), Js('force'), Js('forge'), Js('gaze'), Js('glade'), Js('glory'), Js('glow'), Js('grove'), Js('guard'), Js('heart'), Js('light'), Js('mane'), Js('mantle'), Js('maw'), Js('more'), Js('mourn'), Js('ridge'), Js('river'), Js('rock'), Js('root'), Js('run'), Js('shadow'), Js('shine'), Js('snow'), Js('song'), Js('sorrow'), Js('spark'), Js('spire'), Js('star'), Js('stone'), Js('stream'), Js('stride'), Js('swallow'), Js('talon'), Js('thorn'), Js('thorne'), Js('tide'), Js('vale'), Js('valor'), Js('ward'), Js('watch'), Js('water'), Js('whisper'), Js('willow'), Js('wind'), Js('wing'), Js('wood'), Js('woods')]))
pass
pass


# Add lib to the module scope
throneOfGlassNames = var.to_python()