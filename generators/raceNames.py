__all__ = ['raceNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
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
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Ace'), Js('Airjack'), Js('Apex'), Js('Babe'), Js('Baby Face'), Js('Backpain'), Js('Bandit'), Js('Baron/Baroness'), Js('Big Beat'), Js('Blackjack'), Js('Blade'), Js('Blizzard'), Js('Blondey'), Js('Blower'), Js('Blowover'), Js('Blue Devil'), Js('Bolt'), Js('Bomber'), Js('Breakout'), Js('Breeze'), Js('Brute'), Js('Brute Force'), Js('Buddy'), Js('Bullet'), Js('Bunny'), Js('Burnout'), Js('Buster'), Js('Butch'), Js('Cannonball'), Js('Carnage'), Js('Carwash'), Js('Chase'), Js('Chaser'), Js('Chopper'), Js('Clutch'), Js('Colonel'), Js('Comeback Kid'), Js('Comet'), Js('Crimson'), Js('Delta'), Js('Diesel'), Js('Digger'), Js('Dodge'), Js('Dodger'), Js('Doughnut'), Js('Drift'), Js('Drifter'), Js('Duster'), Js('Dynamite'), Js('Dynasty'), Js('Earthquake'), Js('Echelon'), Js('Enigma'), Js('Evasive'), Js('Fatality'), Js('Fearless'), Js('Fence'), Js('Fireball'), Js('Flash'), Js('Flopper'), Js('Formula Zero'), Js('Forza'), Js('Foxy'), Js('Freebird'), Js('Freestyle'), Js('Friction'), Js('Frosty'), Js('Frozenheart'), Js('Fury'), Js('General'), Js('Glacier'), Js('Gogo'), Js('Golden Kid'), Js('Goose'), Js('Gravels'), Js('Grenade'), Js('Gridline'), Js('Groovey'), Js('Hairpin'), Js('Hammer'), Js('Handsome'), Js('Happy'), Js('Havoc'), Js('Headway'), Js('Helmet Hair'), Js('Holeshot'), Js('Honker'), Js('Hotflash'), Js('Hunter/Huntress'), Js('Hurricane'), Js('Hybrid'), Js('Iceheart'), Js('Indy'), Js('Jolt'), Js('Jumper'), Js('Junior'), Js('Kamikaze'), Js('Kid'), Js('Kit'), Js('Knight'), Js('Leadfoot'), Js('Lightning'), Js('Lightning Bolt'), Js('Lightspeed'), Js('Lionheart'), Js('Little Lightning'), Js('Little Stint'), Js('Lollipop'), Js('Lucky'), Js('Mad Max'), Js('Magic Feet'), Js('Matrix'), Js('Maverick'), Js('Meatball'), Js('Momento'), Js('Mongoose'), Js('Mouse'), Js('Mr/Miss Menace'), Js('Muscles'), Js('Nemo'), Js('Newbie'), Js('Nitro'), Js('Oracle'), Js('Outlaw'), Js('Pitstop'), Js('Pocket Rocket'), Js('Prestige'), Js('Prodigy'), Js('Proto'), Js('Prototype'), Js('Quickshift'), Js('Railer'), Js('Rapido'), Js('Red'), Js('Red Devil'), Js('Redlight'), Js('Redline'), Js('Reflex'), Js('Road Runner'), Js('Rocketeer'), Js('Rodeo'), Js('Rubber'), Js('Rubberburn'), Js('Rumble'), Js('Rush'), Js('Rustle'), Js('Rusty'), Js('Salty'), Js('Sandbag'), Js('Savage'), Js('Scooter'), Js('Scorch'), Js('Scrub'), Js('Shade'), Js('Shadow'), Js('Shakey'), Js('Shortshift'), Js('Showtime'), Js('Skip'), Js('Skipper'), Js('Slingshot'), Js('Slugs'), Js('Smiley'), Js('Smokey'), Js('Smooth Ride'), Js('Snake'), Js('Spark'), Js('Speedstar'), Js('Spirit'), Js('Sprint'), Js('Spunk'), Js('Starflal'), Js('Straightline'), Js('Swifty'), Js('Swirl'), Js('T-Bone'), Js('Tandem'), Js('Tank'), Js('Tasmanian Devil'), Js('The Comeback'), Js('Thriller'), Js('Throttle'), Js('Turbo'), Js('Twitch'), Js('Typhoon'), Js('Velocity'), Js('Viper'), Js('Wheelie'), Js('Wheelspin'), Js('White Smoke'), Js('Wild Thing'), Js('Wings'), Js('Wolf'), Js('Wonderkid'), Js('Xelarate'), Js('Zero'), Js('Zero Light'), Js('Zigzag'), Js('Zoomer'), Js('Zoomzoom')]))
pass
pass


# Add lib to the module scope
raceNames = var.to_python()