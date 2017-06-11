__all__ = ['heistNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('10,000 Mile'), Js('Acrobatics'), Js('Aerial'), Js('Alpha'), Js('Anarchy'), Js('Angel'), Js('Animal'), Js('Annihilation'), Js('Apex'), Js('Aquatic'), Js('Assassination'), Js('Asset'), Js('Avian'), Js('Backfire'), Js('Baited'), Js('Balance'), Js('Bankrupt'), Js('Basket Case'), Js('Benign'), Js('Black Diamond'), Js('Blind'), Js('Blood Diamond'), Js('Bloody'), Js('Blunder'), Js('Bogus'), Js('Bread'), Js('Breadcrumb'), Js('Breakdown'), Js('Bribery'), Js('Bulldozer'), Js('Bully'), Js('Business'), Js('Butcher'), Js('CEO'), Js('Cannibal'), Js('Champion'), Js('Chaos'), Js('Charade'), Js("Child's Play"), Js('Cipher'), Js('Civil'), Js('Clown'), Js('Clumsy'), Js('Copycat'), Js('Corpse'), Js('Corruption'), Js('Counterfeit'), Js('Crooked'), Js('Decimation'), Js('Demolition'), Js('Demon'), Js('Desperation'), Js('Dilemma'), Js('Diplomat'), Js('Dirty'), Js('Disaster'), Js('Diversion'), Js('Divine'), Js('Dread'), Js('Duped'), Js('Duplicate'), Js('Earthquake'), Js('Echo'), Js('Enigma'), Js('Epitome'), Js('Equality'), Js('Escort'), Js('Ethereal'), Js('Evanescence'), Js('Evaporation'), Js('Evil Incarnate'), Js('Extermination'), Js('Fake Out'), Js('False'), Js('Family'), Js('Feral'), Js('Fire'), Js('Floating'), Js('Flood'), Js('Fluke'), Js('Flying'), Js("Fool's"), Js("Fool's Errand"), Js('Foolproof'), Js('Forsaken'), Js('Framed'), Js('Fruitcake'), Js('Fury'), Js('Gambit'), Js('Genocide'), Js('Getaway'), Js('Ghost'), Js('Gopher'), Js('Grave'), Js('Grease'), Js('Great Food'), Js('Grim'), Js('Grim Reaper'), Js('Guardian'), Js('Gunpowder'), Js('Hallowed'), Js('Happy'), Js('Harrier'), Js('Hollow'), Js('Homicide'), Js('Honeycomb'), Js('Honorable'), Js('Hostage'), Js('Hummiliation'), Js('Hurricane'), Js('Hysteria'), Js('Ignition'), Js('Illusion'), Js('Imaginary'), Js('Inferno'), Js('Insanity'), Js('Insider'), Js('Intimidation'), Js('Investment'), Js('Ire'), Js('Junior'), Js('Killing'), Js('Labyrinth'), Js('Landmine'), Js('Laughing'), Js('Lethal'), Js('Lightning'), Js('Limbo'), Js('Liquid'), Js('Lookalike'), Js('Lottery'), Js('Lucky'), Js('Lunatic'), Js('Mad'), Js('Magician'), Js('Maniac'), Js('Martyr'), Js('Masked'), Js('Massacre'), Js('Medieval'), Js('Meteor'), Js('Midnight'), Js('Mile High'), Js('Mime'), Js('Mirror'), Js('Misdirection'), Js('Mobile'), Js('Mock'), Js('Mole'), Js('Mulligan'), Js('Mystery'), Js('Naked'), Js('Neglect'), Js('Neighbor'), Js('Noble'), Js('Noon'), Js('Obliteration'), Js('Oblivion'), Js('Omega'), Js('Paragon'), Js('Parallel'), Js('Pawn'), Js('Perfect'), Js('Phantom Thief'), Js('Picnic'), Js('Plague'), Js('Poison'), Js('Polite'), Js('Premium'), Js('Prime'), Js('Prototype'), Js('Pseudo'), Js('Psycho'), Js('Punishment'), Js('Rampage'), Js('Red Herring'), Js('Refund'), Js('Repeat'), Js('Replica'), Js('Reverse'), Js('Riddle'), Js('Robin Hood'), Js('Rookie'), Js('Ruthless'), Js('Sacrificial'), Js('Savage'), Js('Scapegoat'), Js('Seduction'), Js('Senior'), Js('Sentinel'), Js('Shepherd'), Js('Shock and Awe'), Js('Slayer'), Js('Sleaze'), Js('Smoke Screen'), Js('Smoke and Mirrors'), Js('Smooth'), Js('Smut'), Js('Stained'), Js('Sugarcoated'), Js('Sullied'), Js('Switcheroo'), Js('Termination'), Js('Terror'), Js('Textbook'), Js('Thunder'), Js('Titan'), Js('Torture'), Js('Treasure'), Js('Twin'), Js('Tyrant'), Js('Undead'), Js('Underdog'), Js('Vanishing'), Js('Venom'), Js('Vigilante'), Js('Void'), Js('Voodoo'), Js('Walking Dead'), Js('Warden'), Js('Watchdog'), Js('Wild Goose'), Js('Witchcraft'), Js('Worthless'), Js('Zero'), Js('Zombie')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('Heist'), Js('Sting'), Js('Robbery'), Js('Heist'), Js('Robbery'), Js('Heist')]))
pass
pass


# Add lib to the module scope
heistNames = var.to_python()