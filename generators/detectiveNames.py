__all__ = ['detectiveNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            else:
                if PyJsStrictEq(var.get('tp'),Js(2.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((var.get('nm4').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ace'), Js('Adam'), Js('Adrian'), Js('Alec'), Js('Alex'), Js('Andrew'), Js('Arthur'), Js('Barry'), Js('Bill'), Js('Brad'), Js('Braden'), Js('Brian'), Js('Bruce'), Js('Carl'), Js('Chad'), Js('Charles'), Js('Chris'), Js('Clive'), Js('Conan'), Js('Conor'), Js('Craig'), Js('Dale'), Js('Dan'), Js('Darryl'), Js('Dave'), Js('David'), Js('Denzel'), Js('Derek'), Js('Don'), Js('Donald'), Js('Drake'), Js('Dwayne'), Js('Ed'), Js('Edgar'), Js('Ethan'), Js('Frank'), Js('Fred'), Js('Gavin'), Js('George'), Js('Glenn'), Js('Gordon'), Js('Graham'), Js('Grant'), Js('Greg'), Js('Gus'), Js('Hal'), Js('Hank'), Js('Harold'), Js('Harris'), Js('Harry'), Js('Hector'), Js('Henry'), Js('Jack'), Js('Jacob'), Js('Jake'), Js('James'), Js('Jason'), Js('Jim'), Js('Joe'), Js('Jon'), Js('Kurt'), Js('Lance'), Js('Larry'), Js('Lars'), Js('Leo'), Js('Logan'), Js('Lou'), Js('Luke'), Js('Marcus'), Js('Martin'), Js('Marvin'), Js('Matt'), Js('Max'), Js('Michael'), Js('Mike'), Js('Miles'), Js('Moe'), Js('Morgan'), Js('Nic'), Js('Oscar'), Js('Owen'), Js('Oz'), Js('Paul'), Js('Pete'), Js('Peter'), Js('Phil'), Js('Pierce'), Js('Ray'), Js('Raymond'), Js('Rex'), Js('Rick'), Js('Rob'), Js('Robert'), Js('Roger'), Js('Russ'), Js('Russell'), Js('Ryan'), Js('Sam'), Js('Samuel'), Js('Saul'), Js('Scott'), Js('Sean'), Js('Seth'), Js('Shawn'), Js('Sid'), Js('Stan'), Js('Stephen'), Js('Steven'), Js('Terry'), Js('Thomas'), Js('Tom'), Js('Tony'), Js('Trevor'), Js('Victor'), Js('Vince'), Js('Walter'), Js('Wayne'), Js('Will'), Js('William'), Js('Zac'), Js('Zack')]))
var.put('nm2', Js([Js('Abby'), Js('Adriana'), Js('Agnes'), Js('Alex'), Js('Alice'), Js('Amber'), Js('Angela'), Js('Ann'), Js('Annabel'), Js('Anne'), Js('Arya'), Js('Audra'), Js('Aurora'), Js('Avril'), Js('Barbara'), Js('Beth'), Js('Brenda'), Js('Bridget'), Js('Brittany'), Js('Brooke'), Js('Brynn'), Js('Caitlin'), Js('Carolyn'), Js('Cassie'), Js('Catlyn'), Js('Charlotte'), Js('Christie'), Js('Clare'), Js('Cleo'), Js('Debra'), Js('Diana'), Js('Dianne'), Js('Edit'), Js('Eleanor'), Js('Elizabeth'), Js('Ellen'), Js('Ellie'), Js('Elza'), Js('Emma'), Js('Erika'), Js('Erin'), Js('Eve'), Js('Fiona'), Js('Fran'), Js('Grace'), Js('Gwen'), Js('Hanna'), Js('Hazel'), Js('Helen'), Js('Hilda'), Js('Irene'), Js('Iris'), Js('Jaime'), Js('Jane'), Js('Janis'), Js('Jean'), Js('Jenna'), Js('Jennifer'), Js('Jessica'), Js('Jill'), Js('Jo'), Js('Joan'), Js('Joanne'), Js('Judith'), Js('Julia'), Js('June'), Js('Karen'), Js('Kat'), Js('Kate'), Js('Kim'), Js('Lara'), Js('Laura'), Js('Lauren'), Js('Lillian'), Js('Lois'), Js('Lucy'), Js('Marilyn'), Js('Marion'), Js('Mary'), Js('Meg'), Js('Megan'), Js('Meryl'), Js('Michelle'), Js('Myra'), Js('Nadia'), Js('Natalie'), Js('Nicole'), Js('Nikki'), Js('Nora'), Js('Pam'), Js('Paula'), Js('Rachel'), Js('Renee'), Js('Robin'), Js('Rose'), Js('Roxanne'), Js('Ruth'), Js('Sage'), Js('Sam'), Js('Sandra'), Js('Sarah'), Js('Serena'), Js('Sharon'), Js('Skye'), Js('Stella'), Js('Sue'), Js('Susan'), Js('Tess'), Js('Vera'), Js('Vicky'), Js('Vivian'), Js('Ziva')]))
var.put('nm3', Js([Js('Abbott'), Js('Ace'), Js('Adams'), Js('Alexander'), Js('Anderson'), Js('Archer'), Js('Armstrong'), Js('Ashton'), Js('Bates'), Js('Bishop'), Js('Booth'), Js('Brady'), Js('Briggs'), Js('Brown'), Js('Burn'), Js('Burnham'), Js('Burns'), Js('Caine'), Js('Campbell'), Js('Carter'), Js('Carver'), Js('Chase'), Js('Clark'), Js('Clarkson'), Js('Cole'), Js('Collins'), Js('Cooper'), Js('Cox'), Js('Cross'), Js('Daniels'), Js('Darwin'), Js('Davidson'), Js('Davis'), Js('Dawson'), Js('Dixon'), Js('Donovan'), Js('Dukes'), Js('Duncan'), Js('Eckart'), Js('Finn'), Js('Ford'), Js('Foreman'), Js('Fox'), Js('Freeman'), Js('Frost'), Js('Gibbs'), Js('Gibson'), Js('Gold'), Js('Granger'), Js('Graves'), Js('Grey'), Js('Gunn'), Js('Hackman'), Js('Hammer'), Js('Harris'), Js('Hastings'), Js('Hawkes'), Js('Hayes'), Js('Heath'), Js('Higgins'), Js('Hill'), Js('Horn'), Js('Hunter'), Js('Jackson'), Js('Johnson'), Js('Jones'), Js('Jordan'), Js('Kane'), Js('King'), Js('Knight'), Js('Knott'), Js('Lambert'), Js('Law'), Js('Lawson'), Js('Lawton'), Js('Lawyer'), Js('Lee'), Js('Lincoln'), Js('Locke'), Js('MacLeod'), Js('Marshall'), Js('Mason'), Js('Matthews'), Js('Maxwell'), Js('Moore'), Js('Morgan'), Js('Morris'), Js('Murray'), Js('Newton'), Js('Nicholson'), Js('Nixon'), Js('Nolan'), Js('Palmer'), Js('Parker'), Js('Prescott'), Js('Price'), Js('Quinn'), Js('Reagan'), Js('Robinson'), Js('Roth'), Js('Sanders'), Js('Sawyer'), Js('Seals'), Js('Sharpe'), Js('Shepherd'), Js('Shields'), Js('Simons'), Js('Skinner'), Js('Smith'), Js('Snow'), Js('Spade'), Js('Steel'), Js('Stone'), Js('Sullivan'), Js('Tanner'), Js('Taylor'), Js('Thorn'), Js('Walker'), Js('Ward'), Js('Watson'), Js('West'), Js('White'), Js('Williams'), Js('Winder'), Js('Wolfe'), Js('Woods'), Js('Woolf'), Js('Wright'), Js('Zeal')]))
var.put('nm4', Js([Js('Aaren'), Js('Addison'), Js('Aidan'), Js('Ainsley'), Js('Alex'), Js('Angel'), Js('Arin'), Js('Ash'), Js('Ashton'), Js('Avery'), Js('Bailey'), Js('Blair'), Js('Blake'), Js('Blythe'), Js('Brett'), Js('Brook'), Js('Cameron'), Js('Casey'), Js('Cass'), Js('Charlie'), Js('Chris'), Js('Cory'), Js('Dakota'), Js('Danny'), Js('Daryl'), Js('Drew'), Js('Dylan'), Js('Eli'), Js('Emerson'), Js('Gale'), Js('Harley'), Js('Harper'), Js('Hayden'), Js('Jackie'), Js('Jaden'), Js('Jaiden'), Js('Jamie'), Js('Jay'), Js('Jesse'), Js('Jo'), Js('Jordan'), Js('Jules'), Js('Kasey'), Js('Kerry'), Js('Lane'), Js('Lee'), Js('Logan'), Js('Lynn'), Js('Marley'), Js('Mell'), Js('Merle'), Js('Mo'), Js('Morgan'), Js('Nat'), Js('Quinn'), Js('Raegan'), Js('Reese'), Js('Riley'), Js('River'), Js('Robin'), Js('Rowan'), Js('Sam'), Js('Shannon'), Js('Shawn'), Js('Skyler'), Js('Stevie'), Js('Sydney'), Js('Tanner'), Js('Taylor'), Js('Tristan'), Js('Tyler'), Js('Val'), Js('Vic'), Js('Wil')]))
pass
pass


# Add lib to the module scope
detectiveNames = var.to_python()