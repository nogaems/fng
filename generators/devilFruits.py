__all__ = ['devilFruits']

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
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js([Js('Ame'), Js('Rain')]), Js([Js('Arashi'), Js('Storm')]), Js([Js('Ari'), Js('Ant')]), Js([Js('Baku'), Js('Bomb (Bakudan)')]), Js([Js('Bijon'), Js('Vision')]), Js([Js('Buta'), Js('Pig')]), Js([Js('Chika'), Js('Underground')]), Js([Js('Chikara'), Js('Strength')]), Js([Js('Dōbu'), Js('Animal (Dōbutsu)')]), Js([Js('Eki'), Js('Liquid (Ekitai)')]), Js([Js('Gama'), Js('Toad')]), Js([Js('Gasu'), Js('Gas')]), Js([Js('Gin'), Js('Silver')]), Js([Js('Hāto'), Js('Heart')]), Js([Js('Ha'), Js('Blade')]), Js([Js('Ha'), Js('Tooth')]), Js([Js('Haga'), Js('Steel (Hagane)')]), Js([Js('Hana'), Js('Flower')]), Js([Js('Hansha'), Js('Reflex')]), Js([Js('Hebi'), Js('Snake')]), Js([Js('Heikō'), Js('Equilibrium/Balance')]), Js([Js('Hensō'), Js('Disguise')]), Js([Js('Hi'), Js('Day')]), Js([Js('Hi'), Js('Fire')]), Js([Js('Hika'), Js('Light (Hikari)')]), Js([Js('Himi'), Js('Secret (Himitsu)')]), Js([Js('Himo'), Js('Cord')]), Js([Js('Hokori'), Js('Dust')]), Js([Js('Hyō'), Js('Leopard')]), Js([Js('Ika'), Js('Squid')]), Js([Js('Ikari'), Js('Anger')]), Js([Js('Iki'), Js('Breath')]), Js([Js('Iki'), Js('Creature (Ikimono)')]), Js([Js('Inku'), Js('Ink')]), Js([Js('Inu'), Js('Dog')]), Js([Js('Itami'), Js('Pain')]), Js([Js('Iwa'), Js('Rock')]), Js([Js('Jigo'), Js('Hell (Jigoku)')]), Js([Js('Jikan'), Js('Time')]), Js([Js('Kōri'), Js('Ice')]), Js([Js('Kūki'), Js('Air')]), Js([Js('Kaba'), Js('Hippopotamus')]), Js([Js('Kabu'), Js('Beetle (Kabutomushi)')]), Js([Js('Kaeru'), Js('Frog')]), Js([Js('Kage'), Js('Shadow')]), Js([Js('Kagi'), Js('Key')]), Js([Js('Kaku'), Js('Cactus (Kakutasu)')]), Js([Js('Kaori'), Js('Scent')]), Js([Js('Kara'), Js('Crow (Karasu)')]), Js([Js('Kaze'), Js('Wind')]), Js([Js('Kemo'), Js('Beast (Kemono)')]), Js([Js('Kemuri'), Js('Smoke')]), Js([Js('Kesshō'), Js('Crystal')]), Js([Js('Ketsue'), Js('Blood (Ketsueki)')]), Js([Js('Ki'), Js('Tree')]), Js([Js('Kibō'), Js('Wish')]), Js([Js('Kiba'), Js('Fang')]), Js([Js('Kin'), Js('Gold')]), Js([Js('Kugi'), Js('Spike')]), Js([Js('Kuma'), Js('Bear')]), Js([Js('Kumo'), Js('Cloud')]), Js([Js('Kumo'), Js('Spider')]), Js([Js('Kusari'), Js('Chain')]), Js([Js('Kyo'), Js('Giant (Kyojin)')]), Js([Js('Kyojin'), Js('Giant')]), Js([Js('Maindo'), Js('Mind')]), Js([Js('Mame'), Js('Bean')]), Js([Js('Me'), Js('Eye')]), Js([Js('Mizu'), Js('Water')]), Js([Js('Mushi'), Js('Insect')]), Js([Js('Nō'), Js('Brain')]), Js([Js('Nama'), Js('Lead (Namari)')]), Js([Js('Nawa'), Js('Rope')]), Js([Js('Neko'), Js('Cat')]), Js([Js('Netsu'), Js('Heat')]), Js([Js('Nezu'), Js('Rat/Mouse (Nezumi)')]), Js([Js('Ningyō'), Js('Doll')]), Js([Js('Odo'), Js('Surprise (Odoroki)')]), Js([Js('Onsei'), Js('Voice')]), Js([Js('Osore'), Js('Fear')]), Js([Js('Oto'), Js('Sound')]), Js([Js('Ryū'), Js('Dragon')]), Js([Js('Saru'), Js('Monkey')]), Js([Js('Seishin'), Js('Spirit')]), Js([Js('Shi'), Js('Death')]), Js([Js('Shi'), Js('Lion (Shishi)')]), Js([Js('Shimo'), Js('Frost')]), Js([Js('Shinpi'), Js('Mystery')]), Js([Js('Shita'), Js('Tongue')]), Js([Js('Shoku'), Js('Appetite (Shokuyoku)')]), Js([Js('Sokudo'), Js('Speed')]), Js([Js('Sora'), Js('Sky')]), Js([Js('Suji'), Js('Muscle')]), Js([Js('Suna'), Js('Sand')]), Js([Js('Taihō'), Js('Cannon')]), Js([Js('Taiyō'), Js('Sun')]), Js([Js('Taka'), Js('Hawk')]), Js([Js('Tako'), Js('Octopus')]), Js([Js('Tamai'), Js('Boulder (Tamaishi)')]), Js([Js('Tatsu'), Js('Dragon')]), Js([Js('Ten'), Js('Heaven (Tengoku)')]), Js([Js('Tenki'), Js('Weather')]), Js([Js('Tetsu'), Js('Iron')]), Js([Js('Tobu'), Js('Fly')]), Js([Js('Tora'), Js('Tiger')]), Js([Js('Tori'), Js('Bird')]), Js([Js('Tsuba'), Js('Wing (Tsubasa)')]), Js([Js('Tsuchi'), Js('Earth/Ground')]), Js([Js('Tsuki'), Js('Moon')]), Js([Js('Uma'), Js('Horse')]), Js([Js('Un'), Js('Luck')]), Js([Js('Uta'), Js('Song')]), Js([Js('Yūrei'), Js('Ghost')]), Js([Js('Yoku'), Js('Desire (Yokubō)')]), Js([Js('Yoro'), Js('Pleasure (Yourokobi)')]), Js([Js('Yoru'), Js('Night')]), Js([Js('Yu'), Js('Hot Water')]), Js([Js('Yuge'), Js('Steam')]), Js([Js('Yuki'), Js('Snow')]), Js([Js('Zō'), Js('Elephant')])]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', (((((var.get('nm1').get(var.get('rnd')).get('0')+Js(' '))+var.get('nm1').get(var.get('rnd')).get('0'))+Js(' no Mi ('))+var.get('nm1').get(var.get('rnd')).get('1'))+Js(')')))
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
devilFruits = var.to_python()