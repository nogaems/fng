__all__ = ['mgtGorgon']

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
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd3', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                while PyJsStrictEq(var.get('nm3').get(var.get('rnd3')),var.get('nm1').get(var.get('rnd'))):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('rnd4', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('rnd7', ((var.get('Math').callprop('random')*var.get('nm6').get('length'))|Js(0.0)))
                if (var.get('i')<Js(3.0)):
                    var.put('names', (((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm5').get(var.get('rnd4')))+Js(' the '))+var.get('nm6').get(var.get('rnd7'))))
                else:
                    var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    while PyJsStrictEq(var.get('nm4').get(var.get('rnd5')),var.get('nm3').get(var.get('rnd3'))):
                        var.put('rnd5', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                    var.put('rnd6', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('names', (((((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd6')))+var.get('nm4').get(var.get('rnd5')))+var.get('nm5').get(var.get('rnd4')))+Js(' the '))+var.get('nm6').get(var.get('rnd7'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm8').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm7').get(var.get('rnd'))+Js(' of '))+var.get('nm8').get(var.get('rnd2'))))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm9').get('length'))|Js(0.0)))
                    var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm7').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm9').get(var.get('rnd'))+Js(' '))+var.get('nm7').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('d'), Js('f'), Js('h'), Js('l'), Js('m'), Js('n'), Js('s'), Js('v'), Js('w'), Js('z')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('i'), Js('o'), Js('y')]))
var.put('nm3', Js([Js('c'), Js('g'), Js('h'), Js('l'), Js('ll'), Js('m'), Js('n'), Js('nn'), Js('s'), Js('th'), Js('z')]))
var.put('nm4', Js([Js('l'), Js('ll'), Js('n'), Js('r'), Js('s'), Js('sh')]))
var.put('nm5', Js([Js('a'), Js('e'), Js('a'), Js('e'), Js('i'), Js('i'), Js('ia'), Js('ea'), Js('ae')]))
var.put('nm6', Js([Js('Abandoned'), Js('Aggressive'), Js('Agonized'), Js('Ancient'), Js('Angry'), Js('Arid'), Js('Barbarous'), Js('Bitter'), Js('Blind'), Js('Broken'), Js('Brutal'), Js('Calculated'), Js('Callous'), Js('Careless'), Js('Cold'), Js('Corrupt'), Js('Corrupted'), Js('Crazy'), Js('Crone'), Js('Crooked'), Js('Cruel'), Js('Dead'), Js('Defiant'), Js('Delirious'), Js('Deserted'), Js('Dire'), Js('Dreadful'), Js('Dreary'), Js('Evil'), Js('False'), Js('Feral'), Js('Fickle'), Js('Fierce'), Js('Forked'), Js('Forsaken'), Js('Foul'), Js('Grave'), Js('Greedy'), Js('Grim'), Js('Gross'), Js('Grotesque'), Js('Gruesome'), Js('Hag'), Js('Harsh'), Js('Hateful'), Js('Haunting'), Js('Heartless'), Js('Heinous'), Js('Hollow'), Js('Impure'), Js('Infernal'), Js('Insane'), Js('Insidious'), Js('Jaded'), Js('Loathsome'), Js('Mad'), Js('Maleficent'), Js('Malevolent'), Js('Malicious'), Js('Merciless'), Js('Needy'), Js('Nefarious'), Js('Noxious'), Js('Pitiless'), Js('Rash'), Js('Reckless'), Js('Relentless'), Js('Ruthless'), Js('Sadistic'), Js('Savage'), Js('Shady'), Js('Shallow'), Js('Skeletal'), Js('Spiteful'), Js('Swift'), Js('Toxic'), Js('Unrelenting'), Js('Vicious'), Js('Vile'), Js('Villain'), Js('Villainous'), Js('Vindictive'), Js('Violent'), Js('Warped'), Js('Wicked'), Js('Wild'), Js('Wrathful'), Js('Wretched')]))
var.put('nm7', Js([Js('Archetype'), Js('Sage'), Js('Gorgon'), Js('Medusa'), Js('Mender'), Js('Reaper'), Js('Sister'), Js('Binder'), Js('Sentinel'), Js('Curator'), Js('Custodian'), Js('Overseer'), Js('Warden'), Js('Shepherd'), Js('Keeper'), Js('Guard'), Js('Attendant'), Js('Caretaker'), Js('Conservator'), Js('Sentry'), Js('Steward'), Js('Warden'), Js('Gorgon'), Js('Gorgon'), Js('Gorgon'), Js('Gorgon'), Js('Gorgon'), Js('Medusa'), Js('Medusa'), Js('Vixen'), Js('Sorceress')]))
var.put('nm8', Js([Js('Relics'), Js('Souvenirs'), Js('Keepsakes'), Js('Boulder Beings'), Js('Busts'), Js('Carnage'), Js('Carving'), Js('Certitude'), Js('Corruption'), Js('Crystallization'), Js('Despair'), Js('Destruction'), Js('Dust'), Js('Effigies'), Js('Ends'), Js('Eternal Rest'), Js('Figures'), Js('Finality'), Js('Fossilization'), Js('Foundations'), Js('Granite'), Js('Granite Trophies'), Js('Living Fossils'), Js('Living Ornaments'), Js('Living Statues'), Js('Marble'), Js('Marble Memories'), Js('Memorials'), Js('Ornaments'), Js('Petrification'), Js('Rubble'), Js('Ruins'), Js('Sculpting'), Js('Sculptures'), Js('Solid Ends'), Js('Solid Sleep'), Js('Solidification'), Js('Statues'), Js('Stiffening'), Js('Stone'), Js('Stone Cemeteries'), Js('Stone Creatures'), Js('Stone Death'), Js('Stone Desire'), Js('Stone Flesh'), Js('Stone Images'), Js('Stone Memorials'), Js('Stone Servants'), Js('Stone Skin'), Js('Stone Surprise'), Js('Stone Trophies'), Js('Stonework'), Js('the Basin'), Js('the Cavern'), Js('the Field of Statues'), Js('the Forest'), Js('the Granite Territory'), Js('the Isle'), Js('the Lake'), Js('the Marsh'), Js('the Meadows'), Js('the Mountain'), Js('the Ruins'), Js('the Statue Army'), Js('the Statue Shore'), Js('the Stone Army'), Js('the Stone Cemetery'), Js('the Stone Cold Heart'), Js('the Stone Garden'), Js('the Stone Lake'), Js('the Stone Playground'), Js('the Swamp'), Js('the Wilds')]))
var.put('nm9', Js([Js('Aged'), Js('Ancient'), Js('Angry'), Js('Attentive'), Js('Austere'), Js('Beautiful'), Js('Bitter'), Js('Blind'), Js('Bold'), Js('Careless'), Js('Cheerful'), Js('Cold'), Js('Composed'), Js('Corrupt'), Js('Corrupted'), Js('Crooked'), Js('Cruel'), Js('Defiant'), Js('Disfigured'), Js('Envious'), Js('Evil'), Js('Exotic'), Js('False'), Js('Fearless'), Js('Feisty'), Js('Forsaken'), Js('Fragrant'), Js('Glaring'), Js('Gleeful'), Js('Grave'), Js('Grim'), Js('Grotesque'), Js('Hidden'), Js('Hollow'), Js('Hungry'), Js('Idle'), Js('Infamous'), Js('Infernal'), Js('Insidious'), Js('Jaded'), Js('Juvenile'), Js('Lone'), Js('Lonely'), Js('Lost'), Js('Mad'), Js('Masked'), Js('Mysterious'), Js('Needy'), Js('Noxious'), Js('Petty'), Js('Playful'), Js('Prime'), Js('Radiant'), Js('Scornful'), Js('Selfish'), Js('Shady'), Js('Silent'), Js('Somber'), Js('Sore'), Js('Spiteful'), Js('Swift'), Js('Tired'), Js('Tragic'), Js('Twilight'), Js('Twin'), Js('Unknown'), Js('Vengeful'), Js('Vicious'), Js('Violent'), Js('Warped'), Js('Wicked'), Js('Wrathful'), Js('Wretched')]))
pass
pass


# Add lib to the module scope
mgtGorgon = var.to_python()