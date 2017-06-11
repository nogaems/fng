__all__ = ['cyberPunknames']

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
    var.put('nm1', Js([Js('Acid'), Js('Aero'), Js('Agile'), Js('Alco'), Js('Alter'), Js('Answer'), Js('Ant'), Js('Arch'), Js('Art'), Js('Aspect'), Js('Audience'), Js('Aura'), Js('Aurora'), Js('Awe'), Js('Badge'), Js('Bait'), Js('Bandage'), Js('Bank'), Js('Banks'), Js('Bargain'), Js('Barrage'), Js('Basis'), Js('Bat'), Js('Beam'), Js('Beast'), Js('Beauty'), Js('Bee'), Js('Beetle'), Js('Bell'), Js('Bells'), Js('Bird'), Js('Blade'), Js('Blank'), Js('Block'), Js('Blunder'), Js('Bold'), Js('Bolt'), Js('Bomb'), Js('Bone'), Js('Bones'), Js('Bonus'), Js('Books'), Js('Boost'), Js('Boot'), Js('Boots'), Js('Brash'), Js('Brass'), Js('Brave'), Js('Bribe'), Js('Brick'), Js('Bright'), Js('Brush'), Js('Cable'), Js('Canine'), Js('Canvas'), Js('Cash'), Js('Catch'), Js('Cause'), Js('Cell'), Js('Cent'), Js('Chain'), Js('Chalk'), Js('Chance'), Js('Change'), Js('Chaos'), Js('Charge'), Js('Chart'), Js('Cheat'), Js('Checkmate'), Js('Click'), Js('Clock'), Js('Clocks'), Js('Cloud'), Js('Coarse'), Js('Coil'), Js('Collar'), Js('Complex'), Js('Console'), Js('Crash'), Js('Craven'), Js('Cross'), Js('Crumbs'), Js('Cycle'), Js('Dapper'), Js('Dare'), Js('Data'), Js('Deal'), Js('Design'), Js('Detail'), Js('Dish'), Js('Disk'), Js('Double'), Js('Dynamic'), Js('Dynamo'), Js('Edge'), Js('Ego'), Js('Elite'), Js('Eternity'), Js('Fearless'), Js('Feature'), Js('Feedback'), Js('Fickle'), Js('Fix'), Js('Flaky'), Js('Fluke'), Js('Friction'), Js('Frost'), Js('Gain'), Js('Game'), Js('Gear'), Js('Gene'), Js('Ghost'), Js('Gift'), Js('Glove'), Js('Grave'), Js('Grim'), Js('Habit'), Js('Hack'), Js('Hacks'), Js('Heat'), Js('Hide'), Js('Hollow'), Js('Hook'), Js('Ice'), Js('Impulse'), Js('Ink'), Js('Iron'), Js('Jumbo'), Js('Junior'), Js('Law'), Js('Light'), Js('Link'), Js('Lock'), Js('Luck'), Js('Mammoth'), Js('Math'), Js('Maths'), Js('Mellow'), Js('Memory'), Js('Mirror'), Js('Mouse'), Js('Nemo'), Js('Night'), Js('Nightowl'), Js('Nimble'), Js('Noise'), Js('Note'), Js('Nova'), Js('Number'), Js('Omen'), Js('Owl'), Js('Panther'), Js('Parcel'), Js('Path'), Js('Pathfinder'), Js('Patriot'), Js('Phase'), Js('Piece'), Js('Pitch'), Js('Poison'), Js('Prime'), Js('Print'), Js('Prompt'), Js('Push'), Js('Quote'), Js('Range'), Js('Rebel'), Js('Requiem'), Js('Riddle'), Js('Risk'), Js('Route'), Js('Sable'), Js('Scene'), Js('Score'), Js('Session'), Js('Shade'), Js('Shallow'), Js('Shift'), Js('Shiny'), Js('Signal'), Js('Silver'), Js('Slice'), Js('Slide'), Js('Spark'), Js('Spring'), Js('Status'), Js('Stitch'), Js('Stranger'), Js('Stretch'), Js('Survey'), Js('Switch'), Js('Thrill'), Js('Trick'), Js('Tune'), Js('Unit'), Js('Venom'), Js('Virus'), Js('Ward'), Js('Wicked'), Js('Wish'), Js('Zen'), Js('Zero'), Js('Zigzag'), Js('Zone')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
            var.put('names', var.get('nm1').get(var.get('rnd')))
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
cyberPunknames = var.to_python()