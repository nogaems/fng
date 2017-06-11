__all__ = ['servantNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names', 'nm1', 'nm2', 'nameGen'])
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
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abbington'), Js('Abbot'), Js('Abner'), Js('Abraham'), Js('Alastair'), Js('Albert'), Js('Albus'), Js('Alexander'), Js('Alfred'), Js('Alistair'), Js('Andrew'), Js('Angus'), Js('Anslo'), Js('Archibald'), Js('Arlington'), Js('Ashby'), Js('Ashton'), Js('Atwood'), Js('Bailey'), Js('Baines'), Js('Baldrick'), Js('Baldwin'), Js('Barkley'), Js('Barnabus'), Js('Barnaby'), Js('Barrett'), Js('Bartholomew'), Js('Baxter'), Js('Beauregard'), Js('Belvadair'), Js('Benedict'), Js('Benson'), Js('Bentley'), Js('Bernard'), Js('Bertram'), Js('Bishop'), Js('Caldwell'), Js('Carlisle'), Js('Carlton'), Js('Carstair'), Js('Carter'), Js('Cedric'), Js('Charles'), Js('Chester'), Js('Christopher'), Js('Clarence'), Js('Clark'), Js('Claud'), Js('Claude'), Js('Clement'), Js('Cornelius'), Js('Crawford'), Js('Dalton'), Js('Darby'), Js('Darcy'), Js('Dorian'), Js('Edgar'), Js('Edmun'), Js('Edmund'), Js('Edward'), Js('Edwin'), Js('Elliot'), Js('Emerson'), Js('Francis'), Js('Franklin'), Js('Geoffrey'), Js('George'), Js('Gerald'), Js('Gerard'), Js('Gideon'), Js('Giles'), Js('Godfrey'), Js('Godwin'), Js('Graham'), Js('Gregory'), Js('Hamilton'), Js('Harold'), Js('Harris'), Js('Hartley'), Js('Hastings'), Js('Henry'), Js('Herbert'), Js('Hobbes'), Js('Hobson'), Js('Horace'), Js('Hubert'), Js('Humphrey'), Js('Hymphrey'), Js('Jacob'), Js('James'), Js('Jameson'), Js('Jasper'), Js('Jeeves'), Js('Jeremy'), Js('Johnathan'), Js('Kenworth'), Js('Kingsley'), Js('Lambert'), Js('Laurance'), Js('Leighton'), Js('Lombard'), Js('Lucious'), Js('Manfred'), Js('Maxwell'), Js('Milton'), Js('Montgomery'), Js('Mortimer'), Js('Nathaniel'), Js('Nicholas'), Js('Niles'), Js('Norman'), Js('Olin'), Js('Oliver'), Js('Orson'), Js('Oswald'), Js('Palmer'), Js('Percival'), Js('Percy'), Js('Philip'), Js('Pierce'), Js('Pierre'), Js('Piers'), Js('Porter'), Js('Prescott'), Js('Preston'), Js('Quentin'), Js('Quimby'), Js('Ramsey'), Js('Randolph'), Js('Reginald'), Js('Remington'), Js('Richard'), Js('Roderick'), Js('Roger'), Js('Roland'), Js('Rupert'), Js('Sebastian'), Js('Seymour'), Js('Sinclair'), Js('Smith'), Js('Sterling'), Js('Stuart'), Js('Theobold'), Js('Theodore'), Js('Tobin'), Js('Valentine'), Js('Wallace'), Js('Walter'), Js('Watson'), Js('Wentworth'), Js('Wilfred'), Js('Wilkins'), Js('Willard'), Js('Wilson'), Js('Winston')]))
var.put('nm2', Js([Js('Abigail'), Js('Addison'), Js('Adelaide'), Js('Adeline'), Js('Alexandra'), Js('Alice'), Js('Anastasia'), Js('Angela'), Js('Angelina'), Js('Annabella'), Js('Annabelle'), Js('Anne'), Js('Annebella'), Js('Audrey'), Js('Beatrice'), Js('Belinda'), Js('Bernice'), Js('Blanche'), Js('Briana'), Js('Bridgette'), Js('Brittany'), Js('Caitlin'), Js('Camilla'), Js('Camille'), Js('Carolina'), Js('Cassandra'), Js('Cecilia'), Js('Celeste'), Js('Celia'), Js('Charity'), Js('Charlene'), Js('Charlotte'), Js('Claire'), Js('Clara'), Js('Clarissa'), Js('Clementine'), Js('Corline'), Js('Cynthia'), Js('Danielle'), Js('Daphne'), Js('Darlene'), Js('Delilah'), Js('Diana'), Js('Dora'), Js('Dorothy'), Js('Edit'), Js('Elaine'), Js('Eleanor'), Js('Eleanore'), Js('Elena'), Js('Elizabeth'), Js('Elsie'), Js('Emily'), Js('Eva'), Js('Evangeline'), Js('Eve'), Js('Evelyn'), Js('Fiona'), Js('Fleur'), Js('Florence'), Js('Francine'), Js('Genevieve'), Js('Georgina'), Js('Geraldine'), Js('Gertrude'), Js('Gloria'), Js('Grace'), Js('Gwendoline'), Js('Gwendolyn'), Js('Heather'), Js('Helen'), Js('Helena'), Js('Helene'), Js('Helga'), Js('Henrietta'), Js('Hillary'), Js('Ingrid'), Js('Isabella'), Js('Jeanette'), Js('Jessica'), Js('Johanna'), Js('Josephina'), Js('Josephine'), Js('Judith'), Js('Julia'), Js('Julianna'), Js('Julie'), Js('Juliet'), Js('June'), Js('Justine'), Js('Katherine'), Js('Kathlyn'), Js('Laura'), Js('Leah'), Js('Lillian'), Js('Lily'), Js('Lisabet'), Js('Lorelei'), Js('Louise'), Js('Lucille'), Js('Lydia'), Js('Madeline'), Js('Maisy'), Js('Margery'), Js('Marie'), Js('Marion'), Js('Martha'), Js('Mary'), Js('Mary Anne'), Js('Mary Grace'), Js('Matilda'), Js('Melanie'), Js('Meredith'), Js('Mildred'), Js('Miranda'), Js('Nadine'), Js('Naomi'), Js('Natalaia'), Js('Nicolette'), Js('Noelene'), Js('Nora'), Js('Ophelia'), Js('Penelope'), Js('Phoebe'), Js('Pippa'), Js('Portia'), Js('Priscilla'), Js('Prudence'), Js('Rose'), Js('Rosemary'), Js('Ruth'), Js('Sabrina'), Js('Samantha'), Js('Samara'), Js('Sarah'), Js('Scarlet'), Js('Selena'), Js('Selma'), Js('Serena'), Js('Shirley'), Js('Sophia'), Js('Stella'), Js('Tiffany'), Js('Valerie'), Js('Vanessa'), Js('Veronica'), Js('Victoria'), Js('Viola'), Js('Violet'), Js('Virginia'), Js('Vivian'), Js('Wendy'), Js('Wilhelmina'), Js('Zoe')]))
var.put('names', Js(''))
pass
pass


# Add lib to the module scope
servantNames = var.to_python()