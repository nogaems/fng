__all__ = ['mgtDjinn']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(3.0)):
                    var.put('names', ((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm7').get(var.get('rnd6'))))
                else:
                    if (var.get('i')<Js(5.0)):
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        while PyJsStrictEq(var.get('nm4').get(var.get('rnd8')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm7').get(var.get('rnd6'))))
                    else:
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        var.put('rnd11', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                        while PyJsStrictEq(var.get('nm4').get(var.get('rnd8')),var.get('nm3').get(var.get('rnd3'))):
                            var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                        while (PyJsStrictEq(var.get('nm5').get(var.get('rnd10')),var.get('nm3').get(var.get('rnd3'))) or PyJsStrictEq(var.get('nm5').get(var.get('rnd10')),var.get('nm4').get(var.get('rnd8')))):
                            var.put('rnd10', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                        def PyJs_LONG_0_(var=var):
                            return var.put('names', ((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm5').get(var.get('rnd10')))+var.get('nm2').get(var.get('rnd11')))+var.get('nm5').get(var.get('rnd5')))+Js(' '))+var.get('nm7').get(var.get('rnd6'))))
                        PyJs_LONG_0_()
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((var.get('nm7').get(var.get('rnd'))+Js(' of '))+var.get('nm8').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((var.get('nm9').get(var.get('rnd'))+Js(' '))+var.get('nm7').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js('b'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('m'), Js('r'), Js('s'), Js('v'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('g'), Js('h'), Js('k'), Js('j'), Js('l'), Js('m'), Js('n'), Js('nth'), Js('r'), Js('rh'), Js('s'), Js('t'), Js('z')]))
var.put('nm4', Js([Js('g'), Js('m'), Js('mg'), Js('nd'), Js('r'), Js('rg'), Js('s'), Js('v'), Js('z')]))
var.put('nm5', Js([Js('g'), Js('k'), Js('j'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t'), Js('z')]))
var.put('nm6', Js([Js('b'), Js('c'), Js('d'), Js('m'), Js('r')]))
var.put('nm7', Js([Js('Djinn'), Js('Loremaster'), Js('Weaver'), Js('Sage'), Js('Djinn'), Js('Djinn'), Js('Djinn'), Js('Djinn'), Js('Djinn'), Js('Djinn'), Js('Master'), Js('Mahatma'), Js('Savant')]))
var.put('nm8', Js([Js('Amusement'), Js('Autumn'), Js('Balance'), Js('Chance'), Js('Chances'), Js('Change'), Js('Competition'), Js('Deceit'), Js('Deception'), Js('Desire'), Js('Destinations'), Js('Destinies'), Js('Favors'), Js('Fear'), Js('Fire'), Js('Flames'), Js('Flight'), Js('Frost'), Js('Games'), Js('Harmony'), Js('Humor'), Js('Ice'), Js('Illumination'), Js('Invention'), Js('Jewels'), Js('Knowledge'), Js('Laughs'), Js('Laughter'), Js('Lies'), Js('Light'), Js('Magic'), Js('Music'), Js('Passages'), Js('Play'), Js('Pleasure'), Js('Purpose'), Js('Questions'), Js('Requests'), Js('Rewards'), Js('Riddles'), Js('Servitude'), Js('Slavery'), Js('Smiles'), Js('Smoke'), Js('Smoke and Mirrors'), Js('Snow'), Js('Solitude'), Js('Spirits'), Js('Spring'), Js('Summer'), Js('Surprises'), Js('Thoughts'), Js('Thrills'), Js('Thunder'), Js('Time'), Js('Truth'), Js('Vacation'), Js('Voyages'), Js('Water'), Js('Wind'), Js('Winter'), Js('Wisdom'), Js('Wishes'), Js('the Air'), Js('the Clouds'), Js('the Destiny'), Js('the Forest'), Js('the Labyrinth'), Js('the Lamp'), Js('the Maze'), Js('the Mountain'), Js('the Realm'), Js('the Sea'), Js('the Senses'), Js('the Sky'), Js('the Swamp'), Js('the Voyage'), Js('the Weather'), Js('the World')]))
var.put('nm9', Js([Js('Aerial'), Js('Aura'), Js('Aurora'), Js('Autumn'), Js('Avian'), Js('Balance'), Js('Borealis'), Js('Brine'), Js('Chance'), Js('Competition'), Js('Cyclone'), Js('Deception'), Js('Desire'), Js('Destiny'), Js('Dew'), Js('Favor'), Js('Fire'), Js('Flame'), Js('Flight'), Js('Frost'), Js('Gale'), Js('Game'), Js('Gust'), Js('Harmony'), Js('Hellion'), Js('Ice'), Js('Illumination'), Js('Invention'), Js('Jewel'), Js('Knowledge'), Js('Laughter'), Js('Light'), Js('Music'), Js('Nebula'), Js('Ozone'), Js('Passage'), Js('Pleasure'), Js('Riddle'), Js('Servitude'), Js('Smiles'), Js('Smoke'), Js('Snow'), Js('Solitude'), Js('Spirits'), Js('Spring'), Js('Storm'), Js('Summer'), Js('Surprise'), Js('Thrill'), Js('Thunder'), Js('Time'), Js('Truth'), Js('Vapor'), Js('Voyage'), Js('Water'), Js('Wind'), Js('Winter'), Js('Wisdom'), Js('Zephyr')]))
pass
pass


# Add lib to the module scope
mgtDjinn = var.to_python()