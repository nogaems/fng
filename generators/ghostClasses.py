__all__ = ['ghostClasses']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            var.put('names', ((((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' '))+var.get('nm3').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Class 1'), Js('Class 2'), Js('Class 3'), Js('Class 4'), Js('Class 5'), Js('Type 1'), Js('Type 2'), Js('Type 3'), Js('Type 4'), Js('Type 5'), Js('Category 1'), Js('Category 2'), Js('Category 3'), Js('Category 4'), Js('Category 5'), Js('Rank 1'), Js('Rank 2'), Js('Rank 3'), Js('Rank 4'), Js('Rank 5'), Js('Grade 1'), Js('Grade 2'), Js('Grade 3'), Js('Grade 4'), Js('Grade 5')]))
var.put('nm2', Js([Js('Aggressive'), Js('Ancient'), Js('Angry'), Js('Animalistic'), Js('Aquatic'), Js('Artificial'), Js('Beastly'), Js('Bitter'), Js('Boulder'), Js('Cataclysmic'), Js('Cheerful'), Js('Childlike'), Js('Clone'), Js('Common'), Js('Corrupted'), Js('Crazed'), Js('Cruel'), Js('Dark'), Js('Deadly'), Js('Demonic'), Js('Derange'), Js('Destructive'), Js('Diabolical'), Js('Docile'), Js('Dormant'), Js('Dumb'), Js('Echo'), Js('Electric'), Js('Energized'), Js('Energy'), Js('Envious'), Js('Evil'), Js('Familiar'), Js('Fire'), Js('Foreign'), Js('Forsaken'), Js('Foul'), Js('Frantic'), Js('Freeroaming'), Js('Frenzied'), Js('Friendly'), Js('Frost'), Js('Gentle'), Js('Grieving'), Js('Gruesome'), Js('Harmful'), Js('Harmless'), Js('Hellish'), Js('Helpful'), Js('Ignorant'), Js('Infernal'), Js('Insane'), Js('Intelligent'), Js('Invisible'), Js('Jealous'), Js('Lonely'), Js('Mad'), Js('Malevolent'), Js('Malicious'), Js('Malign'), Js('Mellow'), Js('Metal'), Js('Mild'), Js('Mirror'), Js('Mischievous'), Js('Monstrous'), Js('Mournful'), Js('Natural'), Js('Nefarious'), Js('Nuclear'), Js('Obedient'), Js('Obscene'), Js('Passive'), Js('Petrified'), Js('Petty'), Js('Playful'), Js('Pleasant'), Js('Portal'), Js('Radioactive'), Js('Rejected'), Js('Residual'), Js('Rude'), Js('Shadow'), Js('Slumbering'), Js('Sly'), Js('Solitary'), Js('Somber'), Js('Sorrow'), Js('Stinking'), Js('Teasing'), Js('Teleportation'), Js('Timelost'), Js('Toxic'), Js('Trapped'), Js('Tricky'), Js('Twin'), Js('Uncommon'), Js('Vengeful'), Js('Wandering'), Js('Wicked')]))
var.put('nm3', Js([Js('Apparition'), Js('Appearance'), Js('Banshee'), Js('Behemoth'), Js('Boogieman'), Js('Daemon'), Js('Demon'), Js('Devil'), Js('Duplicate'), Js('Entity'), Js('Ethereal'), Js('Ghost'), Js('Glob'), Js('Haunt'), Js('Metamorph'), Js('Mutation'), Js('Phantasm'), Js('Phantom'), Js('Poltergeist'), Js('Revenant'), Js('Shade'), Js('Shadow'), Js('Shifter'), Js('Specter'), Js('Spirit'), Js('Spook'), Js('Tempus'), Js('Vision'), Js('Visitor'), Js('Wraith')]))
pass
pass


# Add lib to the module scope
ghostClasses = var.to_python()