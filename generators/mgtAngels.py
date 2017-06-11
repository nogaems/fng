__all__ = ['mgtAngels']

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
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                if (var.get('i')<Js(3.0)):
                    var.put('names', ((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('nm6').get(var.get('rnd6')))+Js(' of '))+var.get('nm7').get(var.get('rnd7'))))
                else:
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd8')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', ((((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+var.get('nm5').get(var.get('rnd5')))+Js(', '))+var.get('nm6').get(var.get('rnd6')))+Js(' of '))+var.get('nm7').get(var.get('rnd7'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', ((var.get('nm6').get(var.get('rnd'))+Js(' of '))+var.get('nm7').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                    var.put('names', ((var.get('nm8').get(var.get('rnd'))+Js(' '))+var.get('nm9').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js('b'), Js('br'), Js('d'), Js('g'), Js('h'), Js('j'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('t')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('a'), Js('e'), Js('i'), Js('a'), Js('e'), Js('i'), Js('o'), Js('u'), Js('a'), Js('e'), Js('a'), Js('e'), Js('i'), Js('au'), Js('ia'), Js('ie'), Js('io'), Js('aa')]))
var.put('nm3', Js([Js('br'), Js('c'), Js('dr'), Js('g'), Js('k'), Js('kr'), Js('kn'), Js('l'), Js('ll'), Js('ln'), Js('lm'), Js('m'), Js('my'), Js('n'), Js('nv'), Js('ny'), Js('r'), Js('rr'), Js('s'), Js('v'), Js('y'), Js('z')]))
var.put('nm4', Js([Js('c'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nr'), Js('ndr'), Js('r'), Js('rd'), Js('rn'), Js('rl'), Js('s'), Js('ss'), Js('sn'), Js('t'), Js('th'), Js('z')]))
var.put('nm5', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('h'), Js('l'), Js('n')]))
var.put('nm6', Js([Js('Angel'), Js('Cerberus'), Js('Champion'), Js('Curator'), Js('Guardian'), Js('Herald'), Js('Keeper'), Js('Magister'), Js('Reaper'), Js('Sentinel'), Js('Seraph'), Js('Shepherd'), Js('Shield'), Js('Voice')]))
var.put('nm7', Js([Js('All'), Js('Authority'), Js('Balance'), Js('Battle'), Js('Blood'), Js('Bones'), Js('Carnage'), Js('Chains'), Js('Chance'), Js('Change'), Js('Dawn'), Js('Death'), Js('Deliverance'), Js('Desire'), Js('Despair'), Js('Destruction'), Js('Discovery'), Js('Dread'), Js('Dusk'), Js('Duty'), Js('Existence'), Js('Finality'), Js('Fury'), Js('Grace'), Js('Guidance'), Js('Harmony'), Js('Health'), Js('Invention'), Js('Iron'), Js('Jubilation'), Js('Justice'), Js('Knowledge'), Js('Law'), Js('Light'), Js('Memories'), Js('Mercy'), Js('Pleasure'), Js('Power'), Js('Punishment'), Js('Purpose'), Js('Regret'), Js('Reason'), Js('Renewal'), Js('Retribution'), Js('Scales'), Js('Serenity'), Js('Servitude'), Js('Shades'), Js('Shadows'), Js('Silence'), Js('Silver'), Js('Smoke'), Js('Solitude'), Js('Sustenance'), Js('Thrills'), Js('Time'), Js('Twilight'), Js('War'), Js('Wealth'), Js('Worth'), Js('Wrath'), Js('the Blade'), Js('the Crown'), Js('the Feast'), Js('the Flame'), Js('the Flock'), Js('the Inferno'), Js('the Light'), Js('the Masses'), Js('the Morning'), Js('the Nether'), Js('the Provinces'), Js('the Realm'), Js('the Shield'), Js('the Sword'), Js('the Wild')]))
var.put('nm8', Js([Js('Adept'), Js('Aged'), Js('Agile'), Js('Ancient'), Js('Austere'), Js('Battle'), Js('Belated'), Js('Bitter'), Js('Blood'), Js('Bone'), Js('Brilliant'), Js('Careless'), Js('Chain'), Js('Colossal'), Js('Cruel'), Js('Deathless'), Js('Defiant'), Js('Delirious'), Js('Deserted'), Js('Desire'), Js('Desolation'), Js('Devoted'), Js('Diligent'), Js('Dread'), Js('Elegant'), Js('Emancipation'), Js('Enormous'), Js('Enraged'), Js('Exalted'), Js('Fallen'), Js('Flame'), Js('Flawless'), Js('Forsaken'), Js('Gargantuan'), Js('Giant'), Js('Gleaming'), Js('Glorious'), Js('Golden'), Js('Graceful'), Js('Gracious'), Js('Grand'), Js('Grim'), Js('Guardian'), Js('Harmonious'), Js('Hidden'), Js('Hollow'), Js('Illustrious'), Js('Impure'), Js('Infernal'), Js('Infinite'), Js('Juvenile'), Js('Light'), Js('Livid'), Js('Lone'), Js('Lonely'), Js('Luminous'), Js('Lustrous'), Js('Magnificent'), Js('Majestic'), Js('Merciless'), Js('Mindless'), Js('Monstrous'), Js('Mysterious'), Js('Prime'), Js('Radiant'), Js('Serene'), Js('Shady'), Js('Silent'), Js('Silver'), Js('Skeletal'), Js('Storm'), Js('Twilight'), Js('Twin'), Js('Unknown'), Js('Vengeful'), Js('Vigilant'), Js('Violent'), Js('Watchful'), Js('Whirlwind'), Js('Wicked'), Js('Wrathful'), Js('Wretched')]))
var.put('nm9', Js([Js('Angel'), Js('Cerberus'), Js('Champion'), Js('Curator'), Js('Guardian'), Js('Herald'), Js('Keeper'), Js('Reaper'), Js('Sentinel'), Js('Seraph')]))
pass
pass


# Add lib to the module scope
mgtAngels = var.to_python()