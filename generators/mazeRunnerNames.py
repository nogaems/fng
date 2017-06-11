__all__ = ['mazeRunnerNames']

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
    var.registers(['nm1', 'nm2', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Abu'), Js('Ahm'), Js('Al'), Js('Albert'), Js('Albis'), Js('Alby'), Js('Aldo'), Js('Alex'), Js('Alexander'), Js('Alf'), Js('Alfred'), Js('Andre'), Js('Antony'), Js('Arb'), Js('Archi'), Js('Aris'), Js('Arnold'), Js('Art'), Js('Arthur'), Js('August'), Js('Augustus'), Js('Bell'), Js('Ben'), Js('Benji'), Js('Bernard'), Js('Bernie'), Js('Bert'), Js('Bill'), Js('Billy'), Js('Boyle'), Js('Brian'), Js('Buns'), Js('Bunsen'), Js('Carl'), Js('Carson'), Js('Cav'), Js('Caven'), Js('Charles'), Js('Charlie'), Js('Chris'), Js('Christian'), Js('Clarence'), Js('Clark'), Js('Claude'), Js('Cloud'), Js('Clyde'), Js('Coper'), Js('Dalton'), Js('Dave'), Js('David'), Js('Davy'), Js('Ed'), Js('Eddie'), Js('Edwin'), Js('Ernest'), Js('Erwin'), Js('Farad'), Js('Ford'), Js('Francis'), Js('Frank'), Js('Franklin'), Js('Fred'), Js('Freddie'), Js('Frederick'), Js('Gale'), Js('George'), Js('Georgey'), Js('Gibbs'), Js('Glenn'), Js('Graham'), Js('Gray'), Js('Greg'), Js('Harold'), Js('Harvey'), Js('Hawk'), Js('Henry'), Js('Hodgkin'), Js('Hooke'), Js('Hops'), Js('Hubble'), Js('Hubs'), Js('Isaac'), Js('Isic'), Js('Ivan'), Js('Jack'), Js('James'), Js('Jamie'), Js('John'), Js('Johnie'), Js('Jules'), Js('Julian'), Js('Karl'), Js('Ken'), Js('Leo'), Js('Leonard'), Js('Locke'), Js('Luis'), Js('Luther'), Js('Marcello'), Js('Mario'), Js('Max'), Js('Mendel'), Js('Mich'), Js('Michael'), Js('Mike'), Js('Mikey'), Js('Mitchell'), Js('Morgan'), Js('Murray'), Js('Neil'), Js('Newt'), Js('Nick'), Js('Nobel'), Js('Nobs'), Js('Otto'), Js('Paul'), Js('Percy'), Js('Pete'), Js('Peter'), Js('Quimby'), Js('Raman'), Js('Ramon'), Js('Ramsay'), Js('Randy'), Js('Rob'), Js('Robbie'), Js('Robert'), Js('Ron'), Js('Ronald'), Js('Ross'), Js('Russ'), Js('Russel'), Js('Sal'), Js('Sheldon'), Js('Shin'), Js('Siggie'), Js('Simon'), Js('Smith'), Js('Stephen'), Js('Steven'), Js('Sven'), Js('Teller'), Js('Theo'), Js('Theodor'), Js('Thom'), Js('Thomas'), Js('Thommie'), Js('Tim'), Js('Timmy'), Js('Timothy'), Js('Tom'), Js('Tommie'), Js('Tyson'), Js('Vince'), Js('Volt'), Js('Wallace'), Js('Wallie'), Js('Wally'), Js('Walt'), Js('Walter'), Js('Watson'), Js('Wilhelm'), Js('Will'), Js('Willard'), Js('Willia'), Js('Wolf')]))
    var.put('nm2', Js([Js('Ada'), Js('Aga'), Js('Age'), Js('Aggie'), Js('Agnes'), Js('Alex'), Js('Alexis'), Js('Alva'), Js('Ana'), Js('Anaxi'), Js('Andie'), Js('Andrea'), Js('Angel'), Js('Anni'), Js('Ava'), Js('Avi'), Js('Babs'), Js('Barba'), Js('Barbara'), Js('Barbs'), Js('Bea'), Js('Beatrix'), Js('Beckie'), Js('Belle'), Js('Beth'), Js('Bethe'), Js('Binet'), Js('Birdie'), Js('Blaise'), Js('Bri'), Js('Bria'), Js('Carla'), Js('Carol'), Js('Celsie'), Js('Charlie'), Js('Christy'), Js('Clarence'), Js('Cori'), Js('Dana'), Js('Diana'), Js('Dorothy'), Js('Eliza'), Js('Elizabeth'), Js('Elli'), Js('Em'), Js('Emile'), Js('Emmy'), Js('Eva'), Js('Evangeline'), Js('Gale'), Js('Georgie'), Js('Gertrude'), Js('Gerty'), Js('Gibbs'), Js('Grace'), Js('Gracy'), Js('Haley'), Js('Halley'), Js('Hally'), Js('Harriet'), Js('Illy'), Js('Inge'), Js('Irene'), Js('Iva'), Js('Jackie'), Js('Jane'), Js('Jean'), Js('Jenny'), Js('Joce'), Js('Jocelyn'), Js('Joyce'), Js('Kat'), Js('Kath'), Js('Katharine'), Js('Kristi'), Js('Lace'), Js('Lea'), Js('Lela'), Js('Leona'), Js('Libby'), Js('Lina'), Js('Lisa'), Js('Lise'), Js('Louise'), Js('Love'), Js('Lucy'), Js('Lye'), Js('Lynn'), Js('Mae'), Js('Maria'), Js('Marie'), Js('Mary'), Js('May'), Js('Michel'), Js('Moli'), Js('Nea'), Js('Neila'), Js('Nikol'), Js('Nikola'), Js('Noa'), Js('Nobs'), Js('Pascal'), Js('Paula'), Js('Pearl'), Js('Rachel'), Js('Rene'), Js('Renee'), Js('Rita'), Js('Rosalin'), Js('Ruth'), Js('Sally'), Js('Shelly'), Js('Sherri'), Js('Sherry'), Js('Siggy'), Js('Simone'), Js('Sommer'), Js('Steph'), Js('Stephanie'), Js('Thabita'), Js('Thea'), Js('Theador'), Js('Theodore'), Js('Theresa'), Js('Torri'), Js('Trix'), Js('Trixie'), Js('Willy'), Js('Zora')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
pass
pass


# Add lib to the module scope
mazeRunnerNames = var.to_python()