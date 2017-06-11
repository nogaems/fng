__all__ = ['attackOnTitan']

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
    var.put('nm1', Js([Js('Aberrant'), Js('Absurd'), Js('Acrobatic'), Js('Adamant'), Js('Adapting'), Js('Advanced'), Js('Advancing'), Js('Aged'), Js('Aggressive'), Js('Agile'), Js('Altering'), Js('Anchored'), Js('Ancient'), Js('Angelic'), Js('Angler'), Js('Animal'), Js('Aquatic'), Js('Awoken'), Js('Barbarian'), Js('Barraging'), Js('Battle'), Js('Berserker'), Js('Besieging'), Js('Blade'), Js('Blazing'), Js('Blind'), Js('Blinding'), Js('Blond'), Js('Blood'), Js('Bone'), Js('Bony'), Js('Boosting'), Js('Brass'), Js('Brawling'), Js('Building'), Js('Burning'), Js('Burrowing'), Js('Cackling'), Js('Careless'), Js('Chain'), Js('Champion'), Js('Chaos'), Js('Charging'), Js('Chuckling'), Js('Clawing'), Js('Clever'), Js('Climbing'), Js('Commanding'), Js('Conquering'), Js('Crawling'), Js('Crazy'), Js('Creature'), Js('Crooked'), Js('Cruel'), Js('Crying'), Js('Dancing'), Js('Darkness'), Js('Dashing'), Js('Defiant'), Js('Delirious'), Js('Destroyer'), Js('Dimpled'), Js('Disappearing'), Js('Dodging'), Js('Dread'), Js('Dribbling'), Js('Drunk'), Js('Earthquake'), Js('Echoing'), Js('Elderly'), Js('Elite'), Js('Enormous'), Js('Enraged'), Js('Evading'), Js('Excited'), Js('Feigning'), Js('Feline'), Js('Fierce'), Js('Fire'), Js('Flailing'), Js('Flame'), Js('Frog'), Js('Frogleap'), Js('Fuming'), Js('Furry'), Js('Fuzzy'), Js('Game'), Js('Gargantuan'), Js('Ghost'), Js('Gigantic'), Js('Giggling'), Js('Golden'), Js('Grappling'), Js('Grim'), Js('Grimacing'), Js('Grinning'), Js('Grotesque'), Js('Growling'), Js('Guardian'), Js('Hammer'), Js('Hardening'), Js('Head-Butting'), Js('Heavy'), Js('Herald'), Js('Hideous'), Js('Hiding'), Js('Hissing'), Js('Hook'), Js('Horror'), Js('Howling'), Js('Igniting'), Js('Infernal'), Js('Inhaling'), Js('Intelligent'), Js('Iron'), Js('Junior'), Js('Juvenile'), Js('Lanky'), Js('Laughing'), Js('Leader'), Js('Leading'), Js('Learning'), Js('Light'), Js('Lightning'), Js('Luminous'), Js('Lunging'), Js('Marked'), Js('Masked'), Js('Massive'), Js('Mentor'), Js('Metal'), Js('Mimic'), Js('Miming'), Js('Miniature'), Js('Monkey'), Js('Mumbling'), Js('Night'), Js('Nightmare'), Js('Nimble'), Js('Nocturnal'), Js('Omen'), Js('Parroting'), Js('Patrolling'), Js('Phantom'), Js('Pouncing'), Js('Prime'), Js('Protecting'), Js('Prowling'), Js('Punishing'), Js('Quick'), Js('Rabid'), Js('Raging'), Js('Rain'), Js('Rainstorm'), Js('Rapid'), Js('Resting'), Js('Roaring'), Js('Roasting'), Js('Rummaging'), Js('Running'), Js('Rushing'), Js('Shepherd'), Js('Shield'), Js('Shielded'), Js('Shielding'), Js('Shrieking'), Js('Silver'), Js('Sizzling'), Js('Skeletal'), Js('Slinging'), Js('Slingshot'), Js('Smoking'), Js('Smouldering'), Js('Sneaking'), Js('Speedy'), Js('Sprinting'), Js('Squealing'), Js('Stalking'), Js('Staring'), Js('Storm'), Js('Strange'), Js('Swift'), Js('Tackling'), Js('Thinking'), Js('Thundering'), Js('Tracing'), Js('Tracking'), Js('Trained'), Js('Trap'), Js('Trapping'), Js('Tremor'), Js('Vengeful'), Js('Vicious'), Js('Volatile'), Js('Volcano'), Js('Vomitting'), Js('Whistling'), Js('Wicked'), Js('Winking'), Js('Wise')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('names', (var.get('nm1').get(var.get('rnd'))+Js(' Titan')))
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
attackOnTitan = var.to_python()