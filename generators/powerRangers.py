__all__ = ['powerRangers']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'nm3', 'result'])
    var.put('nm1', Js([Js('Action'), Js('Ancient'), Js('Angel'), Js('Angelic'), Js('Animal'), Js('Animorph'), Js('Aqua'), Js('Arachnid'), Js('Arch'), Js('Arctic'), Js('Aspect'), Js('Balance'), Js('Battle'), Js('Beast'), Js('Beastly'), Js('Berserker'), Js('Brass'), Js('Canine'), Js('Chain'), Js('Challenger'), Js('Champion'), Js('Chaos'), Js('Chemical'), Js('Chrono'), Js('Cloud'), Js('Corrupted'), Js('Corruption'), Js('Courage'), Js('Covert'), Js('Crown'), Js('Cryo'), Js('Dark'), Js('Diamond'), Js('Digital'), Js('Division'), Js('Dream'), Js('Dual'), Js('Dynamic'), Js('Electric'), Js('Elite'), Js('Enchanted'), Js('Ethereal'), Js('Fearless'), Js('Feline'), Js('Force'), Js('Former'), Js('Forsaken'), Js('Freedom'), Js('Future'), Js('Ghost'), Js('Giant'), Js('Glorious'), Js('Grand'), Js('Grave'), Js('Great'), Js('Grim'), Js('Hidden'), Js('Hollow'), Js('Honorable'), Js('Ice'), Js('Infernal'), Js('Infinite'), Js('Infinity'), Js('Invincible'), Js('Jewel'), Js('Junior'), Js('Justice'), Js('Juvenile'), Js('Liberty'), Js('Lizard'), Js('Lone'), Js('Mad'), Js('Magic'), Js('Majestic'), Js('Mammoth'), Js('Masked'), Js('Metal'), Js('Meteor'), Js('Midnight'), Js('Mighty'), Js('Mini'), Js('Monster'), Js('Monstrous'), Js('Mysterious'), Js('Mystery'), Js('Mythic'), Js('Mythical'), Js('Night'), Js('Nightmare'), Js('Nova'), Js('Obsidian'), Js('Peace'), Js('Phantom'), Js('Poison'), Js('Prime'), Js('Pyro'), Js('Radiant'), Js('Radical'), Js('Rebel'), Js('Reckless'), Js('Redemption'), Js('Secret'), Js('Serpent'), Js('Shadow'), Js('Silent'), Js('Snow'), Js('Spirit'), Js('Storm'), Js('Supernova'), Js('Thunder'), Js('True'), Js('Twin'), Js('Ultimate'), Js('Ultra'), Js('Unsung'), Js('Vagabond'), Js('Venom'), Js('Wicked'), Js('Wild'), Js('Winged')]))
    var.put('nm2', Js([Js('Ancient'), Js('Angel'), Js('Aqua'), Js('Arachnid'), Js('Arch'), Js('Arctic'), Js('Battle'), Js('Beast'), Js('Beastly'), Js('Berserk'), Js('Blind'), Js('Boulder'), Js('Canine'), Js('Chain'), Js('Chaos'), Js('Covert'), Js('Dark'), Js('Death'), Js('Dino'), Js('Dragon'), Js('Dread'), Js('Dream'), Js('Dual'), Js('Extreme'), Js('Fearless'), Js('Feline'), Js('Fierce'), Js('Fire'), Js('Flame'), Js('Flawless'), Js('Free'), Js('Freedom'), Js('Ghost'), Js('Golden'), Js('Grand'), Js('Grave'), Js('Great'), Js('Grim'), Js('Heavy'), Js('Hidden'), Js('High'), Js('Hollow'), Js('Ice'), Js('Infinite'), Js('Iron'), Js('Joint'), Js('Jungle'), Js('Liberty'), Js('Life'), Js('Light'), Js('Livid'), Js('Lunar'), Js('Mad'), Js('Mass'), Js('Metal'), Js('Mighty'), Js('Monster'), Js('Moon'), Js('Mystery'), Js('Mythic'), Js('Night'), Js('Nightmare'), Js('Ninja'), Js('Omen'), Js('Phantom'), Js('Phase'), Js('Phoenix'), Js('Poison'), Js('Primal'), Js('Prime'), Js('Radiant'), Js('Reckless'), Js('Rush'), Js('Secret'), Js('Serpent'), Js('Serpentine'), Js('Shadow'), Js('Silent'), Js('Silver'), Js('Smoke'), Js('Snow'), Js('Solar'), Js('Stark'), Js('Stone'), Js('Storm'), Js('Sun'), Js('Surprise'), Js('Swift'), Js('Terror'), Js('Time'), Js('Turbo'), Js('Twin'), Js('Ultra'), Js('Venom'), Js('Virus'), Js('Void'), Js('Water'), Js('Wild'), Js('World')]))
    var.put('nm3', Js([Js('Aspect'), Js('Charge'), Js('Crew'), Js('Edge'), Js('Force'), Js('Fury'), Js('Heart'), Js('Mark'), Js('Mask'), Js('Path'), Js('Point'), Js('Power'), Js('Rush'), Js('Spark'), Js('Spirit'), Js('Steel'), Js('Strike'), Js('Wrath')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('names', (var.get('nm1').get(var.get('rnd'))+Js(' Rangers')))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                var.put('names', (((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2')))+Js(' Rangers')))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
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
powerRangers = var.to_python()