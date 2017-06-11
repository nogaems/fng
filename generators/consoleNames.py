__all__ = ['consoleNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'nm2', 'result'])
    var.put('nm1', Js([Js('Aberrant'), Js('Achievement'), Js('Achiever'), Js('Adventure'), Js('Adventurer'), Js('Agent'), Js('Ambition'), Js('Assistant'), Js('Beast'), Js('Beginning'), Js('Buddy'), Js('Canvas'), Js('Challenger'), Js('Champ'), Js('Champion'), Js('Chimera'), Js('Click'), Js('Cloud'), Js('Clover'), Js('Companion'), Js('Creator'), Js('Crystal'), Js('Curiosity'), Js('Delight'), Js('Desire'), Js('Diamond'), Js('Dot'), Js('Dreamscape'), Js('Edge'), Js('Enigma'), Js('Event'), Js('Feast'), Js('Fest'), Js('Flame'), Js('Fluke'), Js('Ghost'), Js('Gift'), Js('Guest'), Js('Guide'), Js('Heart'), Js('Horn'), Js('Host'), Js('Image'), Js('Impulse'), Js('Jewel'), Js('Level Up'), Js('Light'), Js('Master'), Js('Mirage'), Js('Moment'), Js('Motion'), Js('Omen'), Js('Oracle'), Js('Particle'), Js('Phantom'), Js('Playground'), Js('Prism'), Js('Reward'), Js('Rhythm'), Js('Scene'), Js('Secret'), Js('Sense'), Js('Signal'), Js('Smile'), Js('Snowflake'), Js('Spark'), Js('Sparkle'), Js('Specter'), Js('Spell'), Js('Spirit'), Js('Sprite'), Js('Station'), Js('Taste'), Js('Tempest'), Js('Thrill'), Js('Thunder'), Js('Treat'), Js('Trick'), Js('Twist'), Js('Veil'), Js('Victory'), Js('View'), Js('Wish')]))
    var.put('nm2', Js([Js('Aberrant'), Js('Action'), Js('Adventure'), Js('Ambition'), Js('Amusement'), Js('Awe'), Js('Beginning'), Js('Boundless'), Js('Buddy'), Js('Challenge'), Js('Challenger'), Js('Champion'), Js('Chance'), Js('Child'), Js('Childhood'), Js('Chimera'), Js('Collection'), Js('Companion'), Js('Courage'), Js('Creation'), Js('Creative'), Js('Creator'), Js('Crux'), Js('Crystal'), Js('Curiosity'), Js('Desire'), Js('Dimension'), Js('Dream'), Js('Emotion'), Js('Enigma'), Js('Entertainment'), Js('Eternity'), Js('Fantasy'), Js('Fire'), Js('Force'), Js('Fortune'), Js('Freedom'), Js('Game'), Js('Golden'), Js('Grand'), Js('Harmony'), Js('Hyper'), Js('Image'), Js('Imagination'), Js('Impulse'), Js('Infinity'), Js('Liberty'), Js('Life'), Js('Light'), Js('Master'), Js('Mirage'), Js('Mystery'), Js('Oracle'), Js('Particle'), Js('Phantom'), Js('Play'), Js('Pocket'), Js('Power'), Js('Prism'), Js('Response'), Js('Retro'), Js('Rhythm'), Js('Sentient'), Js('Silver'), Js('Smile'), Js('Source'), Js('Spark'), Js('Specialist'), Js('Specter'), Js('Spell'), Js('Start'), Js('Super'), Js('Surprise'), Js('Switch'), Js('Thrill'), Js('Thunder'), Js('Treat'), Js('Vessel'), Js('Victory'), Js('Virtual'), Js('Vision'), Js('Voyage'), Js('Voyager'), Js('Wisdom'), Js('World')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('names', (Js('The ')+var.get('nm1').get(var.get('rnd'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                var.put('names', (((Js('The ')+var.get('nm2').get(var.get('rnd')))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm3', Js([Js('Box'), Js('Cast'), Js('Center'), Js('Core'), Js('Cube'), Js('Drive'), Js('Sphere'), Js('Station'), Js('System'), Js('Zone'), Js('Arcade'), Js('Box'), Js('Cade'), Js('Cast'), Js('Center'), Js('Core'), Js('Cube'), Js('Drive'), Js('Player'), Js('Sphere'), Js('Station'), Js('System'), Js('Vision'), Js('Zone')]))
pass
pass


# Add lib to the module scope
consoleNames = var.to_python()