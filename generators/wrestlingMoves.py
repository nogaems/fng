__all__ = ['wrestlingMoves']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
            var.put('names', var.get('names1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Abdominal Tight Grip'), Js('Alligator Grip'), Js('Alligator Leglock'), Js('Alligator Spinebuster'), Js('Anaconda Death Grip'), Js('Anaconda Headlock'), Js('Anaconda Tight Grip'), Js('Angel Wings'), Js('Atomic Bomb Elbow Drop'), Js('Backstab Elbow Slam'), Js('Bald Eagle Freedom Dive'), Js('Barrel Roll'), Js('Battering Ram Headbutt'), Js('Bearhug Headlock'), Js('Bearhug Life Squeezer'), Js('Bionic Backhand Chop'), Js('Bionic Elbow Slam'), Js('Bone Buster'), Js('Boomerang Armbreaker'), Js('Boulderfist Facebreaker'), Js('Boulderfist Nightmare Slam'), Js('Boulderfist Spinebuster'), Js('Bulldog Bite Armbreaker'), Js('Butterfly Body Grip'), Js('Cannonball Backbreaker'), Js('Catapult Leg Sweep'), Js('Charging Bizon Gutbuster'), Js('Charging Bizon Headbutt'), Js('Charging Bizon Rib Breaker'), Js('Charging Bizon Takedown'), Js('Charging Bull Headbutt'), Js('Chickenwing Armlock'), Js('Chopping Block'), Js('Cobra Bite'), Js('Corkscrew Leg Drop'), Js('Crab Claw Shoulder Grip'), Js('Crucifixion'), Js('Death From Above'), Js('Dire Wolf Bite'), Js('Diving Knee Bomb'), Js('Diving Knee Hammers'), Js('Diving Whale'), Js('Double Knee Backbreaker'), Js('Double Knee Dive Bomb'), Js('Double Legged Takedown'), Js('Dragon Claw'), Js('Dragon Punch'), Js('Dragon Tail Elbow Slam'), Js('Dragonbreath Face Twister'), Js('Dragonfire Body Slam'), Js('Dragontail Legsweep'), Js('Dragontail Whip'), Js('Dragonwing Body Slam'), Js('Eagle Dive'), Js('Elbow Barrage'), Js('Electric Armlock'), Js('Elevated Elbow Smash'), Js('Elevated Gutbuster'), Js('Elevated Muscle Buster'), Js('Explosive Leg Drop'), Js('Facebreaker Elbow Dive'), Js('Facebreaker Elbow Smash'), Js('Firework Neckbreaker'), Js('Fists of Fury'), Js('Flight of the Phoenix '), Js('Flying Chokeslam'), Js('Flying Knee Smash'), Js('Flying Legs Takedown'), Js('Flying Nightmare Kick '), Js('Full Body Avalanche'), Js('Full Body Earthquake'), Js('Full Body Powerbomb'), Js('Giant Deathswing'), Js('Giant Panda Body Lock'), Js('Giant Panda Body Slam'), Js('Gorilla Shoulder Swing'), Js('Gorilla Slam Forearm Drop'), Js('Gorilla Slam Jawbreaker'), Js('Gorilla Stomp'), Js('Grizzly Bear Death Choke'), Js('Grizzly Bear Death Grip'), Js('Guillotine Neckbreaker'), Js('Gutbuster Knee Smash'), Js('Hammerhead Backbreaker'), Js('Hammerhead Knock Out'), Js('Hangman Body Lock'), Js('Hangman Hold'), Js('High Speed Body Slam'), Js('Hippo Headlock'), Js('Hippopotamus Body Slam'), Js('Horserider Tight Grip'), Js('Hurricane Arm Dive'), Js('Hurricane Fists'), Js('Hurricane Powerslam'), Js('Imminent Death Heart Punch'), Js('Imploding Body Grip'), Js('Inverted Facebuster'), Js('Inverted Pilediver'), Js('Iron Fists Bombardment'), Js('Ironfist Jawbreaker'), Js('Ironfury Cannonball'), Js('Jackhammer Backbreaker'), Js('Jackhammer Headbutt'), Js('Knuckle Buster'), Js('Leaping Frog Body Slam'), Js('Leaping Frog Headbutt'), Js('Leaping Frog Take Down'), Js('Leaping Frog Takedown'), Js('Lifting Body Slam'), Js('Lightning Fist'), Js('Lion Roar Body Slam'), Js('Lunar Assault'), Js('Mad Monkey Overhead Chop'), Js('Mad Monkey Shoulderbreaker'), Js('Mammoth Stom Spinebreaker'), Js('Mammoth Stome Facebreaker'), Js('Mammoth Stomp'), Js('Mammoth Stomp Facebreaker'), Js('Monkey Madness'), Js('Mountain Goat Headbutt'), Js('Mountain Goat Takedown'), Js('Neck Twister'), Js('Octopus Body Stretch'), Js('Octopus Choke Hold'), Js('Octopus Grip'), Js('Orbital Shoulder Throw'), Js('Overhead Body Slam'), Js('Overhead Body Throw'), Js('Overshoulder Discus Throw'), Js('Paralyzing Palm Strike'), Js('Pentagram Headlock'), Js('Pitbull Tight Grip'), Js('Polar Bear Body Slam'), Js('Polar Bear Death Chop'), Js('Polar Bear Headlock'), Js('Praying Mantis'), Js('Raginb Bull Headbutt'), Js('Ramming Speed Gutbuster'), Js('Rebound Headbutt'), Js('Recoil Armbreaker'), Js('Rhino Charge Gutbuster'), Js('Rhino Charge Headbutt'), Js('Rhino Charge Rib Breaker'), Js('Rocketeer Elbow Drop'), Js('Rocketeer Powerbomb'), Js('Scorpion Sting'), Js('Serpent Sting Forehand Chop'), Js('Shooting Star Body Slam'), Js('Shooting Star Elbow Dive'), Js('Shooting Star Spinning Kick'), Js('Shoulder Dive Backbreaker'), Js('Shoulder Slam Gutbuster'), Js('Shoulder Slam Neckbreaker'), Js('Skull Cracker'), Js('Sleeper Headlock'), Js('Sleeping Chokehold'), Js('Sleeping Giant Body Lock'), Js('Sleeping Giant Death Choke'), Js('Sleeping Headbutt'), Js('Sleeping Time Chokegrip'), Js('Slingshot Elbow Buster'), Js('Smiling Facelock'), Js('Snapping Turtle Armbreaker'), Js('Spinning Crane Leg Kick'), Js('Spinning Crane Neckbuster'), Js('Spinning Crane Spinebuster'), Js('Spinning Legsweep Takedown'), Js('Spinning Toe Legsweep'), Js('Staggering Horse Leg Kick'), Js('Starfish Armlock'), Js('Starfish Body Lock'), Js('Starfish Leglock'), Js('Straitjacket Jawlock'), Js('Stubborn Mule Leg Kick'), Js('Stubborn Mule Stomach Kick'), Js('Submission Chokehold'), Js('Super Nova Body Bomb'), Js('Superkick Slingshot'), Js('Sweeping Leg Shin Breaker'), Js('The Beggar Lock'), Js('The Boomerang'), Js('The Guillotine'), Js('The Jawbreaker'), Js('The Slingshot'), Js('The Whirlwind'), Js('Thrusting Spear Elbow Dive'), Js('Thunderbird Elbow Dive'), Js('Thunderbird Elbow Smash'), Js('Thunderbird Powerbomb'), Js('Thunderbord Knee Dive'), Js('Thunderstorm Leg Drop'), Js('Tiger Claw Back Chop'), Js('Tigerjaw Shoulderlock'), Js('Tightgrip Headlock'), Js('Torpedo Knee Buster'), Js('Total Eclipe Body Slam'), Js('Turtle Bite Chinlock'), Js('Turtle Bite Choke Hold'), Js('Two-Handed Gutbuster'), Js('Two-Handed Rib Breaker')]))
pass
pass


# Add lib to the module scope
wrestlingMoves = var.to_python()