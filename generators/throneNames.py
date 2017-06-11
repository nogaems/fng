__all__ = ['throneNames']

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
            var.put('names', ((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' Throne')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Adamant'), Js('Angel'), Js('Animal'), Js('Apocalypse'), Js('Arachnid'), Js('Arcane'), Js('Arch'), Js('Ashen'), Js('Aura'), Js('Barbarian'), Js('Barbaric'), Js('Barbed'), Js('Beastly'), Js('Behemoth'), Js('Bleak'), Js('Blood'), Js('Bloodied'), Js('Bone'), Js('Brilliant'), Js('Broken'), Js('Burning'), Js('Burnt'), Js('Butcher'), Js('Chaos'), Js('Cold'), Js('Corpse'), Js('Corrupt'), Js('Covert'), Js('Crescent'), Js('Crimson'), Js('Crumbled'), Js('Crushed'), Js('Crystal'), Js('Cursed'), Js('Dead'), Js('Deceiver'), Js('Demon'), Js('Deranged'), Js('Desert'), Js('Destiny'), Js('Devil'), Js('Diabolic'), Js('Diamond'), Js('Dire'), Js('Dishonored'), Js('Dragon'), Js('Dragonfire'), Js('Dread'), Js('Dream'), Js('Drunk'), Js('Ebon'), Js('Elemental'), Js('Elite'), Js('Ember'), Js('Eternal'), Js('Evil'), Js('Exalted'), Js('Exile'), Js('False'), Js('Feeble'), Js('Fire'), Js('Flower'), Js('Forlorn'), Js('Forsaken'), Js('Frozen'), Js('Funereal'), Js('Gentle'), Js('Ghost'), Js('Giant'), Js('Gilded'), Js('Glass'), Js('Glistening'), Js('Glowing'), Js('God'), Js('Graceful'), Js('Grand'), Js('Granite'), Js('Grave'), Js('Great'), Js('Green'), Js('Grim'), Js('Heavenly'), Js('Hell'), Js('Hellish'), Js('High'), Js('Holy'), Js('Horror'), Js('Hostile'), Js('Ice'), Js('Illusion'), Js('Impish'), Js('Impure'), Js('Industrious'), Js('Infernal'), Js('Insane'), Js('Iron'), Js('Isolated'), Js('Ivory'), Js('Jade'), Js('Legendary'), Js('Lich'), Js('Light'), Js('Lightning'), Js('Lizard'), Js('Lonely'), Js('Loyal'), Js('Lucky'), Js('Lunar'), Js('Mad'), Js('Magic'), Js('Magma'), Js('Malicious'), Js('Marsh'), Js('Master'), Js('Midnight'), Js('Mighty'), Js('Mindless'), Js('Mithril'), Js('Molten'), Js('Monster'), Js('Mountain'), Js('Mourning'), Js('Muddy'), Js('Mutant'), Js('Mute'), Js('Mystic'), Js('Necro'), Js('Nefarious'), Js('Nightmare'), Js('Noble'), Js('Obscure'), Js('Obsidian'), Js('Occult'), Js('Ocean'), Js('Onyx'), Js('Outcast'), Js('Paragon'), Js('Peasant'), Js('Phantom'), Js('Phoenix'), Js('Placid'), Js('Plague'), Js('Primal'), Js('Prime'), Js('Prophecy'), Js('Psycho'), Js('Puppet'), Js('Rabid'), Js('Ragged'), Js('Rainbow'), Js('Reaper'), Js('Regal'), Js('Renegade'), Js('Rose'), Js('Rotten'), Js('Royal'), Js('Ruined'), Js('Rune'), Js('Sable'), Js('Sanguine'), Js('Sapphire'), Js('Savage'), Js('Serpent'), Js('Shadow'), Js('Shielded'), Js('Silent'), Js('Sinister'), Js('Sinner'), Js('Skull'), Js('Sleeping'), Js('Smoldering'), Js('Snow'), Js('Solar'), Js('Sorrow'), Js('Soul'), Js('Spider'), Js('Spine'), Js('Spirit'), Js('Spiteful'), Js('Steel'), Js('Storm'), Js('Strife'), Js('Sullen'), Js('Supreme'), Js('Surface'), Js('Talon'), Js('Terror'), Js('Thorn'), Js('Thunder'), Js('Timeless'), Js('Titan'), Js('Torment'), Js('Traitor'), Js('Tranquil'), Js('Twilight'), Js('Undead'), Js('Unholy'), Js('Venom'), Js('Vile'), Js('Violet'), Js('Volcanic'), Js('Warlord'), Js('Water'), Js('Wayward'), Js('Welfare'), Js('Wicked'), Js('Widow'), Js('Wild'), Js('Winged'), Js('Wooden'), Js('Zodiac')]))
pass
pass


# Add lib to the module scope
throneNames = var.to_python()