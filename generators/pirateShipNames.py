__all__ = ['pirateShipNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(type, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'type':type}, var)
    var.registers(['tp', 'result', 'type'])
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('Adventure'), Js('Anger of the'), Js('Angry'), Js('Barbaric'), Js('Bearded'), Js('Black'), Js('Blasted'), Js('Crimson'), Js('Sanguine'), Js('Blind'), Js('Bloodthirsty'), Js('Bloody'), Js('Broken'), Js('Buccaneers'), Js('Burning'), Js('Cacophonous'), Js('Captains'), Js('Corrupted'), Js('Cruel'), Js('Cry'), Js('Cry of the'), Js('Curse of the'), Js('Cursed'), Js('Damnation of the'), Js('Damned'), Js('Davy Jones'), Js('Death of'), Js('Deceit of'), Js('Deceitful'), Js('Devils'), Js('Dirty'), Js('Discourteous'), Js('Silent'), Js('Disgrace of the'), Js('Disgraced'), Js('Disgraceful'), Js('Dishonorable'), Js('Disrespectful'), Js('Dragons'), Js('Drunken'), Js('Elusive'), Js('Evil'), Js('Fall of'), Js('Fearful'), Js('Fearful Grail of'), Js('Festering'), Js('Filthy'), Js('Flying'), Js('Fortune'), Js('Foul Serpent of'), Js('Gold'), Js('Golden'), Js('Good'), Js('Greed of the'), Js('Greedy'), Js('Grief of the'), Js('Hades'), Js('Happy'), Js('Hateful'), Js('Hell-born'), Js('Hellish'), Js('Homicidal'), Js('Horrid'), Js('Howl of the'), Js('Howling'), Js('Howling '), Js('Impolite'), Js('Killers'), Js('Liberty'), Js('Little'), Js('Loyal'), Js('Lust of the'), Js('Mad'), Js('Grand'), Js('Madness of the'), Js('Mangy'), Js('Mayflower'), Js('Most'), Js('Murderers'), Js('Murderous'), Js("Mermaid's"), Js("Neptune's"), Js('New'), Js('Last'), Js('Night'), Js('Nights'), Js('Oceans'), Js('Pillaging'), Js('Pirates'), Js('Plundering'), Js('Poison'), Js('Poisoned'), Js('Poisonous'), Js("Poseidon's"), Js('Pride of the'), Js('Privateers'), Js('Rancid'), Js('Red'), Js('Revenge'), Js('Rising'), Js('Rude'), Js('Sadness of the'), Js('Savage'), Js('Scurvy'), Js('Sea'), Js('Seas'), Js('Shadows of the'), Js('Snap'), Js('Speedy'), Js('Sudden'), Js('Uncultured'), Js('Vicious'), Js('Victory'), Js('Vile'), Js('White')]))
var.put('nm2', Js([Js('Anger'), Js('Abandoned'), Js('Scorn'), Js('Tainted'), Js('Atlantis'), Js('Captain'), Js('Caribbean'), Js('Corruption'), Js('Corsair'), Js('Coward'), Js('Curse'), Js('Cutlass'), Js('Dagger'), Js('Damnation'), Js('Damned'), Js('Death'), Js('Deceit'), Js('Delight'), Js('Delivery'), Js('Demon'), Js('Disgrace'), Js('Doom'), Js('Doubloon'), Js('Dragon'), Js('Eel'), Js('Executioner'), Js('Executioners'), Js('Fall'), Js('Fear'), Js('Fortune'), Js('Galley'), Js('Ghost'), Js('Gold'), Js('Grail'), Js('Hades'), Js('Hangman'), Js('Hind'), Js('Horror'), Js('Howl'), Js('Insanity'), Js('James'), Js('Jewel'), Js('Killer'), Js('Killers'), Js('King'), Js('Knave'), Js('Lightning'), Js('Lust'), Js('Manta'), Js('Minnow'), Js('Tide'), Js('Murderer'), Js('Murderers'), Js('Night'), Js('North'), Js('Pearl'), Js('Pillager'), Js('Pirate'), Js('Plague'), Js('Plunder'), Js('Plunderer'), Js('Plunderers'), Js('Princess'), Js('Privateer'), Js('Raider'), Js('Rambler'), Js('Ranger'), Js('Return'), Js('Revenge'), Js('Saber'), Js('Scream'), Js('Sea'), Js('Seas'), Js('Marauders'), Js('Swashbucklers'), Js('Rovers'), Js('Sea Rovers'), Js('Buccaneers'), Js('Rose'), Js('Rift'), Js('Deceit'), Js('Secret'), Js('Serpent'), Js('Servant'), Js('Servants'), Js('Seven Seas'), Js('Shark'), Js('Slave'), Js('Squid'), Js('Storm'), Js('Strumpet'), Js('Sun'), Js('Terror'), Js('Tortuga'), Js('Treasure'), Js('Trinity'), Js('Wolf')]))
pass
pass


# Add lib to the module scope
pirateShipNames = var.to_python()