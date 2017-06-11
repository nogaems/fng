__all__ = ['dndWarforged']

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
    var.put('nm1', Js([Js('Abider'), Js('Achiever'), Js('Actor'), Js('Adapter'), Js('Adviser'), Js('Aegis'), Js('Agent'), Js('Animal'), Js('Apparatus'), Js('Armament'), Js('Artist'), Js('Audience'), Js('Author'), Js('Awakener'), Js('Basher'), Js('Bastion'), Js('Battler'), Js('Bear'), Js('Beast'), Js('Beauty'), Js('Beetle'), Js('Bender'), Js('Binder'), Js('Blade'), Js('Book'), Js('Booster'), Js('Boot'), Js('Bouncer'), Js('Brain'), Js('Brander'), Js('Brawler'), Js('Breaker'), Js('Bringer'), Js('Browser'), Js('Bruiser'), Js('Buffet'), Js('Bug'), Js('Builder'), Js('Bulwark'), Js('Calmer'), Js('Candle'), Js('Cannon'), Js('Carer'), Js('Carriage'), Js('Carrier'), Js('Cart'), Js('Carver'), Js('Case'), Js('Caster'), Js('Catcher'), Js('Chain'), Js('Chains'), Js('Challenger'), Js('Champion'), Js('Chaperon'), Js('Charger'), Js('Chaser'), Js('Chopper'), Js('Claymore'), Js('Cleaver'), Js('Climber'), Js('Clock'), Js('Club'), Js('Clubber'), Js('Coil'), Js('Commander'), Js('Controller'), Js('Cook'), Js('Counter'), Js('Creator'), Js('Creature'), Js('Creese'), Js('Crew'), Js('Croaker'), Js('Crow'), Js('Crumbler'), Js('Crusher'), Js('Curator'), Js('Curtana'), Js('Custodian'), Js('Cutlas'), Js('Cutlass'), Js('Cutter'), Js('Dagger'), Js('Data'), Js('Dealer'), Js('Decipherer'), Js('Defender'), Js('Definer'), Js('Delver'), Js('Designer'), Js('Destroyer'), Js('Diagnoser'), Js('Director'), Js('Dirk'), Js('Diver'), Js('Doctor'), Js('Dozer'), Js('Dreamer'), Js('Drifter'), Js('Driver'), Js('Drone'), Js('Echo'), Js('Edge'), Js('Enchanter'), Js('Epee'), Js('Eraser'), Js('Estoc'), Js('Etcher'), Js('Examiner'), Js('Expert'), Js('Falchion'), Js('Familiar'), Js('Fighter'), Js('Figure'), Js('Fire'), Js('Five'), Js('Flail'), Js('Flame'), Js('Fluke'), Js('Foil'), Js('Follower'), Js('Forger'), Js('Four'), Js('Friend'), Js('Fumbler'), Js('Gasher'), Js('Gauger'), Js('Ghost'), Js('Giant'), Js('Gift'), Js('Glaive'), Js('Glancer'), Js('Griller'), Js('Grunter'), Js('Guardian'), Js('Guest'), Js('Guide'), Js('Hacker'), Js('Hammer'), Js('Handler'), Js('Heart'), Js('Help'), Js('Hook'), Js('Horn'), Js('Host'), Js('Hummer'), Js('Hunter'), Js('Image'), Js('Inspector'), Js('Iron'), Js('Judge'), Js('Junior'), Js('Jury'), Js('Katana'), Js('Kid'), Js('Killer'), Js('Knife'), Js('Knocker'), Js('Kris'), Js('Launcher'), Js('Leaper'), Js('Lifter'), Js('Lock'), Js('Locket'), Js('Lurker'), Js('Mace'), Js('Machine'), Js('Mark'), Js('Marker'), Js('Mask'), Js('Masker'), Js('Mauler'), Js('Melter'), Js('Menace'), Js('Mentor'), Js('Merger'), Js('Metal'), Js('Mime'), Js('Mistake'), Js('Model'), Js('Molder'), Js('Murderer'), Js('Nameless'), Js('Needle'), Js('Nemo'), Js('Novice'), Js('Nurse'), Js('Observer'), Js('Officer'), Js('Ogler'), Js('One'), Js('Ornament'), Js('Painter'), Js('Passenger'), Js('Patient'), Js('Patriot'), Js('Pierce'), Js('Pilot'), Js('Pious'), Js('Player'), Js('Porter'), Js('Preacher'), Js('Pretender'), Js('Prize'), Js('Probe'), Js('Protector'), Js('Prowler'), Js('Punisher'), Js('Query'), Js('Ravager'), Js('Reader'), Js('Reckoner'), Js('Relic'), Js('Render'), Js('Rescuer'), Js('Responder'), Js('Reviewer'), Js('Rider'), Js('Rune'), Js('Saber'), Js('Sabre'), Js('Safeguard'), Js('Salvager'), Js('Saviour'), Js('Scimitar'), Js('Scorcher'), Js('Scratcher'), Js('Scrubber'), Js('Searcher'), Js('Security'), Js('Seeker'), Js('Senior'), Js('Senser'), Js('Sentinel'), Js('Sentry'), Js('Servant'), Js('Shaper'), Js('Shepherd'), Js('Shield'), Js('Shielder'), Js('Shredder'), Js('Slasher'), Js('Slicer'), Js('Smasher'), Js('Smiter'), Js('Snooper'), Js('Spark'), Js('Sparkle'), Js('Special'), Js('Spirit'), Js('Sprinter'), Js('Sprite'), Js('Squasher'), Js('Stalker'), Js('Status'), Js('Steel'), Js('Steeple'), Js('Stick'), Js('Sticks'), Js('Stitcher'), Js('Striker'), Js('Student'), Js('Stumbler'), Js('Subject'), Js('Suit'), Js('Sunderer'), Js('Supporter'), Js('Surveyor'), Js('Sword'), Js('Tackler'), Js('Taunter'), Js('Teacher'), Js('Teaser'), Js('Tempter'), Js('Tester'), Js('Thief'), Js('Thinker'), Js('Three'), Js('Thunder'), Js('Tinkerer'), Js('Titan'), Js('Toad'), Js('Toledo'), Js('Tutor'), Js('Twister'), Js('Two'), Js('Undoer'), Js('Unit'), Js('Unmaker'), Js('Unsung'), Js('Vessel'), Js('Victor'), Js('Visitor'), Js('Voice'), Js('Walker'), Js('Ward'), Js('Warden'), Js('Watcher'), Js('Whisperer'), Js('Wielder'), Js('Winker'), Js('Winner'), Js('Wonderer'), Js('Wrestler'), Js('Zealot'), Js('Zero')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('names', var.get('nm1').get(var.get('rnd')))
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
dndWarforged = var.to_python()