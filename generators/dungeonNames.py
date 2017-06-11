__all__ = ['dungeonNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm2', 'nm3', 'nm4', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            if (var.get('i')<Js(4.0)):
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm2').get(var.get('rnd2'))+Js(' of the '))+var.get('nm3').get(var.get('rnd3')))+Js(' '))+var.get('nm4').get(var.get('rnd4'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abandoned'), Js('Abominable'), Js('Abomination'), Js('Abysmal'), Js('Abyss'), Js('Adamantine'), Js('Adamantite'), Js('Ancient'), Js('Angry'), Js('Arcane'), Js('Arching'), Js('Arctic'), Js('Arid'), Js('Bare'), Js('Bellowing'), Js('Black'), Js('Black Forest'), Js('Black Mountain'), Js('Bleak'), Js('Bloodfall'), Js('Bloodlust'), Js('Boiling'), Js('Bottomless'), Js('Brilliant'), Js('Broken Bones'), Js('Broken Curse'), Js('Bronze'), Js('Brutal'), Js('Buried'), Js('Burned'), Js('Burning'), Js('Burning Forest'), Js('Buried'), Js('Chaos'), Js('Chaotic'), Js('Cobalt'), Js('Cold'), Js('Collapsing'), Js('Coral'), Js('Courage'), Js('Crescent Moon'), Js('Crystal'), Js('Cunning'), Js('Cursed'), Js('Damned'), Js('Dancing'), Js('Dark'), Js('Daydream'), Js('Dead'), Js('Deadly'), Js('Death Talon'), Js('Decayed'), Js('Decaying'), Js('Deep'), Js('Deepest'), Js('Deepwood'), Js('Delusion'), Js('Demonic'), Js('Depraved'), Js('Desert'), Js('Deserted'), Js('Desolate'), Js('Desolated'), Js('Destroyed'), Js('Destruction'), Js('Diamond'), Js('Dire'), Js('Distant'), Js('Dragon'), Js('Dragonclaw'), Js('Dragontooth'), Js('Dread'), Js('Dreaded'), Js('Dreadful'), Js('Dream'), Js('Dreary'), Js('Dry'), Js('Dying'), Js('Earth'), Js('Eastern'), Js('Eclipse'), Js('Emerald'), Js('Empty'), Js('Enchanted'), Js('Ender'), Js('Erased'), Js('Eternal'), Js('Eternal Agony'), Js('Eternal Rest'), Js('Ethereal'), Js('Fabled'), Js('Fallen Legion'), Js('False'), Js('Feared'), Js('Fearsome'), Js('Fire'), Js('Fire Mountain'), Js('Flowing'), Js('Foaming'), Js('Forbidden'), Js('Forgotten'), Js('Forsaken'), Js('Fractured'), Js('Frozen'), Js('Full Moon'), Js('Ghost'), Js('Glistening'), Js('Gloomy'), Js('Glowing'), Js('Goblin'), Js('Gold Mine'), Js('Grey'), Js('Grim'), Js('Grizzly'), Js('Hallucination'), Js('Haunted'), Js('Hidden'), Js('Hollow'), Js('Howling'), Js('Hungry'), Js('Illusion'), Js('Infernal'), Js('Infinite'), Js('Invisible'), Js('Iron'), Js('Iron Mine'), Js('Ironbark'), Js('Isolated'), Js('Jade'), Js('Jagged'), Js('Killing'), Js('Laughing'), Js('Laughing Skulls'), Js('Lifeless'), Js('Light'), Js('Lion Tooth'), Js('Living'), Js('Living Dead'), Js('Lonely'), Js('Lost'), Js('Lower'), Js('Lucent'), Js('Lurking Shadow'), Js('Malicious'), Js('Mesmerizing'), Js('Mighty'), Js('Mirage'), Js('Mirrored'), Js('Misty'), Js('Mithril'), Js('Mithril Mine'), Js('Moaning'), Js('Mocking'), Js('Molten'), Js('Motionless'), Js('Mourning'), Js('Murky'), Js('Mysterious'), Js('Mystic'), Js('Narrow'), Js('Nether'), Js('Neverending'), Js('Nightmare'), Js('Northern'), Js('Obliterated'), Js('Oblivion'), Js('Ogre'), Js('Oracle'), Js('Orc'), Js('Overhanging'), Js('Perfumed'), Js('Phantom'), Js('Phoenix'), Js('Prisoner'), Js('Quiet'), Js('Raging'), Js('Red'), Js('Restless'), Js('Roaring'), Js('Rocking'), Js('Rugged'), Js('Sad'), Js('Sanguine'), Js('Savage'), Js('Scarlet'), Js('Scheming'), Js('Scorching'), Js('Screaming'), Js('Secret'), Js('Serene'), Js('Shadow'), Js('Shadowed'), Js('Shadowy'), Js('Shimmering'), Js('Shrieking'), Js('Silent'), Js('Silver'), Js('Sleeping'), Js('Smoky'), Js('Smoldering'), Js('Sorrow'), Js('Southern'), Js('Specter'), Js('Spirit'), Js('Steel'), Js('Sterile'), Js('Sunken'), Js('Swamp'), Js('Terraced'), Js('Thief'), Js('Thundering'), Js('Tormented'), Js('Tranquil'), Js('Turbulent'), Js('Twilight'), Js('Twisted'), Js('Twisting'), Js('Unholy'), Js('Unknown'), Js('Unstable'), Js('Vicious'), Js('Violent'), Js('Voiceless'), Js('Voiceless Whimpers'), Js('Volcanic'), Js('Wailing'), Js('Wasted'), Js('Watching Eyes'), Js('Western'), Js('Whispering'), Js('Whispering Shadows'), Js('White'), Js('White Forest'), Js('Wicked'), Js('Wild'), Js('Wind'), Js('Windy'), Js('Winter'), Js('Withered'), Js('Wondering'), Js('Wraith'), Js('Wrath'), Js('Yawning')]))
var.put('nm2', Js([Js('Burrows'), Js('Catacombs'), Js('Caverns'), Js('Cells'), Js('Chambers'), Js('Crypt'), Js('Delves'), Js('Dungeon'), Js('Grotto'), Js('Haunt'), Js('Labyrinth'), Js('Lair'), Js('Maze'), Js('Pits'), Js('Point'), Js('Quarters'), Js('Tombs'), Js('Tunnels'), Js('Vault')]))
var.put('nm3', Js([Js('Black'), Js('White'), Js('Silver'), Js('Golden'), Js('Crystal'), Js('Fallen'), Js('Ghost'), Js('Phantom'), Js('Hidden'), Js('Secret'), Js('Hopeless'), Js('Forsaken'), Js('Gentle'), Js('Chaotic'), Js('Conquered'), Js('Burning'), Js('Poisoned'), Js('Whispering'), Js('Mourning'), Js('Crying'), Js('Lost'), Js('Infernal'), Js('Vanished'), Js('Rejected'), Js('Neglected'), Js('Shunned'), Js('Impostor'), Js('Renegade'), Js('Betrayed'), Js('Vanquished'), Js('Burning'), Js('Frozen'), Js('Destroyed'), Js('Cursed'), Js('Ancient'), Js('Obsidian'), Js('Ebon'), Js('Forbidden'), Js('Lonely'), Js('Nameless'), Js('Dark'), Js('Cold'), Js('Haunted'), Js('Forgotten'), Js('Scarlet'), Js('Shrouded'), Js('Uncanny'), Js('Unspoken'), Js('Vanishing'), Js('Nightmare'), Js('Mystic'), Js('Mythic'), Js('Enigmatic'), Js('Doomed'), Js("Death's"), Js('Spirit'), Js("Spirit's"), Js('Unknown'), Js('Shadow'), Js('Elemental'), Js('Savage'), Js('Storm'), Js('Thunder'), Js('Barbaric'), Js('Cruel'), Js('Brutal'), Js('Blooded'), Js('Ruthless'), Js('Raging'), Js('Furious'), Js('Mad'), Js('Granite'), Js('Dishonored'), Js('Perished')]))
var.put('nm4', Js([Js('Arachnid'), Js('Army'), Js('Basilisk'), Js('Bat'), Js('Bear'), Js('Cult'), Js('Desert'), Js('Dragon'), Js('Eagle'), Js('Elf'), Js('Emperor'), Js('Forest'), Js('Giant'), Js('Goblin'), Js('Guardian'), Js('Horsemen'), Js('Hound'), Js('Hunter'), Js('Jungle'), Js('King'), Js('Knight'), Js('Legion'), Js('Leopard'), Js('Lion'), Js('Mage'), Js('Marsh'), Js('Monk'), Js('Morass'), Js('Mountain'), Js('Occult'), Js('Ogre'), Js('Oracle'), Js('Orc'), Js('Paladin'), Js('Panther'), Js('Phoenix'), Js('Priest'), Js('Queen'), Js('Raven'), Js('Scorpion'), Js('Serpent'), Js('Soldier'), Js('Spider'), Js('Swamp'), Js('Tiger'), Js('Warrior'), Js('Widow'), Js('Witch'), Js('Wizard'), Js('Warlord'), Js('Wolf')]))
pass
pass


# Add lib to the module scope
dungeonNames = var.to_python()