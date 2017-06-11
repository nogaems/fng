__all__ = ['mgtAvatars']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd6', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd7', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                if (var.get('i')<Js(3.0)):
                    var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+Js(', '))+var.get('nm5').get(var.get('rnd6')))+Js(' of '))+var.get('nm6').get(var.get('rnd7'))))
                else:
                    var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd9', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd8')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd8', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', (((((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd8')))+var.get('nm2').get(var.get('rnd9')))+Js(', '))+var.get('nm5').get(var.get('rnd6')))+Js(' of '))+var.get('nm6').get(var.get('rnd7'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', ((var.get('nm5').get(var.get('rnd'))+Js(' of '))+var.get('nm6').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', ((var.get('nm7').get(var.get('rnd'))+Js(' '))+var.get('nm8').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('c'), Js('f'), Js('g'), Js('k'), Js('n'), Js('ph'), Js('s'), Js('th'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('a'), Js('e'), Js('o'), Js('i'), Js('i'), Js('u')]))
var.put('nm3', Js([Js('d'), Js('g'), Js('h'), Js('j'), Js('n'), Js('r'), Js('s'), Js('t'), Js('y'), Js('z')]))
var.put('nm4', Js([Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('r'), Js('v')]))
var.put('nm5', Js([Js('Animus'), Js('Avatar'), Js('Child'), Js('Daughter'), Js('Deity'), Js('Demigos'), Js('Deus'), Js('Divinity'), Js('Dominus'), Js('Essence'), Js('Hand'), Js('Heir'), Js('Heiress'), Js('Herald'), Js('Keeper'), Js('Nobilis'), Js('Overbeing'), Js('Oversoul'), Js('Progeny'), Js('Scion'), Js('Soul')]))
var.put('nm6', Js([Js('Adjustment'), Js('Advice'), Js('Amusement'), Js('Anger'), Js('Autumn'), Js('Awe'), Js('Balance'), Js('Battle'), Js('Birth'), Js('Blades'), Js('Blood'), Js('Brilliance'), Js('Calamity'), Js('Carnage'), Js('Chaos'), Js('Clarity'), Js('Compassion'), Js('Courage'), Js('Death'), Js('Deceit'), Js('Dedication'), Js('Delight'), Js('Desire'), Js('Despair'), Js('Destruction'), Js('Discord'), Js('Dreams'), Js('Elegance'), Js('Envy'), Js('Fascination'), Js('Fealty'), Js('Fear'), Js('Frailty'), Js('Freedom'), Js('Fury'), Js('Generosity'), Js('Grace'), Js('Grief'), Js('Hate'), Js('Hatred'), Js('Havoc'), Js('Honesty'), Js('Honor'), Js('Hope'), Js('Humility'), Js('Humor'), Js('Insanity'), Js('Intelligence'), Js('Justice'), Js('Knowledge'), Js('Laughter'), Js('Liberty'), Js('Life'), Js('Loss'), Js('Loyalty'), Js('Luck'), Js('Memories'), Js('Might'), Js('Misery'), Js('Omens'), Js('Pain'), Js('Perseverance'), Js('Piety'), Js('Power'), Js('Pride'), Js('Prophecies'), Js('Redemption'), Js('Revenge'), Js('Sanity'), Js('Shadows'), Js('Slaughter'), Js('Solitude'), Js('Sorrow'), Js('Spring'), Js('Strength'), Js('Summer'), Js('Thrills'), Js('Tolerance'), Js('Tranquility'), Js('Truth'), Js('Uncertainty'), Js('Vengeance'), Js('Victory'), Js('Wealth'), Js('Will'), Js('Winter'), Js('Wisdom'), Js('Wit'), Js('Woe'), Js('Wrath'), Js('the Mighty'), Js('the Resolute'), Js('the Stout')]))
var.put('nm7', Js([Js('Abandoned'), Js('Aethereal'), Js('Aggravating'), Js('Ancient'), Js('Anguished'), Js('Animated'), Js('Arrogant'), Js('Austere'), Js('Bitter'), Js('Blind'), Js('Bright'), Js('Brilliant'), Js('Broken'), Js('Careless'), Js('Colossal'), Js('Condemned'), Js('Corrupt'), Js('Crooked'), Js('Cruel'), Js('Defiant'), Js('Delirious'), Js('Deserted'), Js('Devoted'), Js('Diligent'), Js('Dismal'), Js('Divine'), Js('Doubtless'), Js('Ebon'), Js('Elated'), Js('Elegant'), Js('Exalted'), Js('False'), Js('Fearless'), Js('Fell'), Js('Fickle'), Js('Flawless'), Js('Forlorn'), Js('Forsaken'), Js('Funereal'), Js('Glorious'), Js('Golden'), Js('Gracious'), Js('Grand'), Js('Greedy'), Js('Grim'), Js('Guilty'), Js('Hallowed'), Js('Harmonious'), Js('Heedless'), Js('Hidden'), Js('Hollow'), Js('Humble'), Js('Hungering'), Js('Hungry'), Js('Illustrious'), Js('Impure'), Js('Infernal'), Js('Jaded'), Js('Living'), Js('Lone'), Js('Lonely'), Js('Luminate'), Js('Misguided'), Js('Molten'), Js('Nameless'), Js('Obsidian'), Js('Prime'), Js('Pristine'), Js('Pure'), Js('Reckless'), Js('Revered'), Js('Sanguine'), Js('Scornful'), Js('Selfish'), Js('Sepulchral'), Js('Serene'), Js('Shameless'), Js('Silent'), Js('Swift'), Js('Timeless'), Js('Torn'), Js('Transcendent'), Js('Truthful'), Js('Twin'), Js('Unbreakable'), Js('Undefeated'), Js('Unseen'), Js('Unwielding'), Js('Venerated'), Js('Vengeful'), Js('Vigilant'), Js('Warped'), Js('Wicked'), Js('Wise'), Js('Wrathful'), Js('Wretched')]))
var.put('nm8', Js([Js('Animus'), Js('Avatar'), Js('Champion'), Js('Deity'), Js('Demigod'), Js('Deus'), Js('Dominus'), Js('God'), Js('Herald'), Js('Incarnation'), Js('Keeper'), Js('One'), Js('Primordial'), Js('Scion'), Js('Shadow'), Js('Shepherd'), Js('Soul'), Js('Spiritkeeper')]))
pass
pass


# Add lib to the module scope
mgtAvatars = var.to_python()