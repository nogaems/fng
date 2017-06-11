__all__ = ['heroNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2', 'nm6'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(4.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(8.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', ((((var.get('nm3').get(var.get('rnd'))+Js(' '))+var.get('nm4').get(var.get('rnd2')))+Js(' '))+var.get('nm5').get(var.get('rnd3'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('names', var.get('nm6').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('The Accidental'), Js('The Ancient'), Js('The Aqua'), Js('The Awesome'), Js('The Black'), Js('The Blue'), Js('The Brass'), Js('The Brave'), Js('The Broad'), Js('The Broken'), Js('The Bronze'), Js('The Calm'), Js('The Clever'), Js('The Cold'), Js('The Colossal'), Js('The Confident'), Js('The Cool'), Js('The Copper'), Js('The Crimson'), Js('The Dapper'), Js('The Dark'), Js('The Defiant'), Js('The Dramatic'), Js('The Eager'), Js('The Earth'), Js('The Earthen'), Js('The Electric'), Js('The Electron'), Js('The Elegant'), Js('The Ethereal'), Js('The Fabulous'), Js('The Famous'), Js('The Fancy'), Js('The Fantastic'), Js('The Fast'), Js('The Fearless'), Js('The Fiery'), Js('The Fire'), Js('The Galactic'), Js('The Gentle'), Js('The Giant'), Js('The Gigantic'), Js('The Glorious'), Js('The Godly'), Js('The Golden'), Js('The Good'), Js('The Gorgeous'), Js('The Gray'), Js('The Green'), Js('The Heavenly'), Js('The Heavy'), Js('The Honorable'), Js('The Hot'), Js('The Huge'), Js('The Hypnotic'), Js('The Ice'), Js('The Impossible'), Js('The Incredible'), Js('The Infamous'), Js('The Intelligent'), Js('The Iron'), Js('The Jade'), Js('The Jolly'), Js('The Kind'), Js('The Light'), Js('The Long'), Js('The Lucky'), Js('The Macho'), Js('The Magical'), Js('The Magnificent'), Js('The Majestic'), Js('The Mammoth'), Js('The Marked'), Js('The Marvelous'), Js('The Merciful'), Js('The Mighty'), Js('The Misty'), Js('The Mysterious'), Js('The Nifty'), Js('The Nimble'), Js('The Nuclear'), Js('The Old'), Js('The Orange'), Js('The Outrageous'), Js('The Pink'), Js('The Proud'), Js('The Purple'), Js('The Quantum'), Js('The Quick'), Js('The Quiet'), Js('The Rapid'), Js('The Red'), Js('The Righteous'), Js('The Royal'), Js('The Scarlet'), Js('The Silver'), Js('The Smooth'), Js('The Spectacular'), Js('The Steel'), Js('The Storm'), Js('The Swift'), Js('The Terrific'), Js('The Thunder'), Js('The Vengeful'), Js('The Voiceless'), Js('The Wacky'), Js('The Water'), Js('The Whispering'), Js('The White'), Js('The Wise'), Js('The Yellow')]))
var.put('nm2', Js([Js('Robin'), Js('Owl'), Js('Vulture'), Js('Condor'), Js('Falcon'), Js('Merlin'), Js('Eagle'), Js('Hawk'), Js('Swan'), Js('Ibis'), Js('Crane'), Js('Snipe'), Js('Macaw'), Js('Amazon'), Js('Nighthawk'), Js('Nightowl'), Js('Monarch'), Js('Lord'), Js('Crow'), Js('Raven'), Js('Swallow'), Js('Starling'), Js('Sparrow'), Js('Ant'), Js('Antman'), Js('Wasp'), Js('Phoenix'), Js('Waspman'), Js('Grasshopper'), Js('Cricket'), Js('Beetle'), Js('Assassin'), Js('Mantis'), Js('Mothman'), Js('Moth'), Js('Termite'), Js('Dragonfly'), Js('Elephantman'), Js('Wolf'), Js('Wolfman'), Js('Bat'), Js('Rhino'), Js('Rhinoceros'), Js('Cat'), Js('Catman'), Js('Lynx'), Js('Gorilla'), Js('Leopard'), Js('Armadillo'), Js('Bear'), Js('Tiger'), Js('Lion'), Js('Fox'), Js('Raccoon'), Js('Ox'), Js('Oxman'), Js('Puma'), Js('Panther'), Js('Wolverine'), Js('Cheetah'), Js('Mongoose'), Js('Jackal'), Js('Hornet'), Js('Warrior'), Js('Fighter'), Js('Angel'), Js('Devil'), Js('Guardian'), Js('Protector'), Js('Champion'), Js('Defender'), Js('Saviour'), Js('Guard'), Js('Watcher'), Js('Slayer'), Js('Killer'), Js('Soldier'), Js('Marksman'), Js('Sniper'), Js('Commando'), Js('Gunner'), Js('Mercenary'), Js('Scout'), Js('Veteran'), Js('Sentinel'), Js('Shepherd'), Js('Warden'), Js('Keeper'), Js('Watchman'), Js('Magician'), Js('Charmer'), Js('Conjurer'), Js('Enchanter'), Js('Genius'), Js('Illusionist'), Js('Prophet'), Js('Seer'), Js('Shaman'), Js('Siren'), Js('Wizard'), Js('Mage'), Js('Master'), Js('Mastermind'), Js('Prodigy'), Js('Sage'), Js('Wonder'), Js('Wonderman'), Js('Whiz'), Js('Spectacle'), Js('Duke'), Js('Baron'), Js('Prince'), Js('Shield'), Js('Sword'), Js('Dagger'), Js('Trident'), Js('Knuckles'), Js('Daggers'), Js('Swordsman'), Js('Scimitar'), Js('Katana'), Js('Axeman'), Js('Scepter'), Js('Hammer'), Js('Gladiator'), Js('Shadow'), Js('Shade'), Js('Gloom'), Js('Spy'), Js('Agent'), Js('Detective'), Js('Mole'), Js('Leader'), Js('Vindicator'), Js('Captain'), Js('Chief'), Js('Doctor'), Js('General'), Js('Smasher'), Js('Spirit'), Js('Scorpion'), Js('Spider')]))
var.put('nm3', Js([Js('Doctor'), Js('Captain'), Js('Doctor'), Js('Captain'), Js('Lord'), Js('Professor'), Js('Professor'), Js('Mister'), Js('Commander'), Js('Master'), Js('Agent'), Js('Master'), Js('Agent'), Js('Chief'), Js('Warden'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm4', Js([Js('Red'), Js('Blue'), Js('Green'), Js('Yellow'), Js('Purple'), Js('Pink'), Js('Gray'), Js('Dark'), Js('Light'), Js('Orange'), Js('Galactic'), Js('Black'), Js('White'), Js('Clever'), Js('Famous'), Js('Infamous'), Js('Brave'), Js('Calm'), Js('Gentle'), Js('Proud'), Js('Dapper'), Js('Eager'), Js('Jolly'), Js('Broad'), Js('Brass'), Js('Copper'), Js('Golden'), Js('Silver'), Js('Bronze'), Js('Iron'), Js('Steel'), Js('Huge'), Js('Mammoth'), Js('Gigantic'), Js('Colossal'), Js('Quiet'), Js('Thundering'), Js('Whispering'), Js('Ancient'), Js('Fast'), Js('Fancy'), Js('Magnificent'), Js('Mysterious'), Js('Old'), Js('Long'), Js('Rapid'), Js('Swift'), Js('Quick'), Js('Broken'), Js('Cold'), Js('Cool'), Js('Hot'), Js('Heavy'), Js('Light'), Js('Good'), Js('Eager'), Js('Fiery'), Js('Elegent'), Js('Electric'), Js('Defiant'), Js('Brave'), Js('Accidental'), Js('Ethereal'), Js('Dramatic'), Js('Awesome'), Js('Impossible'), Js('Incredible'), Js('Intelligent'), Js('Heavenly'), Js('Honorable'), Js('Huge'), Js('Hypnotic'), Js('Gentle'), Js('Giant'), Js('Glorious'), Js('Godly'), Js('Gorgeous'), Js('Fabulous'), Js('Fancy'), Js('Fantastic'), Js('Fearless'), Js('Kind'), Js('Lucky'), Js('Macho'), Js('Magical'), Js('Majestic'), Js('Marked'), Js('Marvelous'), Js('Mighty'), Js('Messy'), Js('Merciful'), Js('Misty'), Js('Nifty'), Js('Nimble'), Js('Outrageous'), Js('Confident'), Js('Rapid'), Js('Righteous'), Js('Royal'), Js('Terrific'), Js('Smooth'), Js('Spectacular'), Js('Wacky'), Js('Wise'), Js('Vengeful'), Js('Voiceless'), Js('Unarmed'), Js('Armed'), Js('Nuclear'), Js('Scarlet'), Js('Quantum'), Js('Electron'), Js('Crimson'), Js('Fire'), Js('Ice'), Js('Earth'), Js('Earthen'), Js('Water'), Js('Aqua'), Js('Storm'), Js('Thunder')]))
var.put('nm5', Js([Js('Masquerade'), Js('Robin'), Js('Owl'), Js('Vulture'), Js('Condor'), Js('Falcon'), Js('Merlin'), Js('Eagle'), Js('Hawk'), Js('Swan'), Js('Ibis'), Js('Phoenix'), Js('Crane'), Js('Snipe'), Js('Macaw'), Js('Amazon'), Js('Nighthawk'), Js('Nightowl'), Js('Monarch'), Js('Lord'), Js('Crow'), Js('Raven'), Js('Swallow'), Js('Starling'), Js('Sparrow'), Js('Ant'), Js('Antman'), Js('Wasp'), Js('Waspman'), Js('Grasshopper'), Js('Cricket'), Js('Beetle'), Js('Assassin'), Js('Mantis'), Js('Mothman'), Js('Moth'), Js('Termite'), Js('Dragonfly'), Js('Elephantman'), Js('Wolf'), Js('Wolfman'), Js('Bat'), Js('Rhino'), Js('Rhinoceros'), Js('Cat'), Js('Catman'), Js('Lynx'), Js('Gorilla'), Js('Leopard'), Js('Armadillo'), Js('Bear'), Js('Tiger'), Js('Lion'), Js('Fox'), Js('Raccoon'), Js('Ox'), Js('Oxman'), Js('Puma'), Js('Panther'), Js('Wolverine'), Js('Cheetah'), Js('Mongoose'), Js('Jackal'), Js('Hornet'), Js('Warrior'), Js('Fighter'), Js('Angel'), Js('Devil'), Js('Guardian'), Js('Protector'), Js('Champion'), Js('Defender'), Js('Saviour'), Js('Watcher'), Js('Slayer'), Js('Killer'), Js('Sentinel'), Js('Shepherd'), Js('Magician'), Js('Charmer'), Js('Conjurer'), Js('Enchanter'), Js('Genius'), Js('Illusionist'), Js('Prophet'), Js('Mastermind'), Js('Prodigy'), Js('Sage'), Js('Wonder'), Js('Spectacle'), Js('Shield'), Js('Sword'), Js('Dagger'), Js('Trident'), Js('Knuckles'), Js('Daggers'), Js('Swordsman'), Js('Scimitar'), Js('Katana'), Js('Axeman'), Js('Scepter'), Js('Hammer'), Js('Shadow'), Js('Shade'), Js('Gloom'), Js('Mole'), Js('Smasher'), Js('Spirit'), Js('Scorpion'), Js('Spider')]))
var.put('nm6', Js([Js('Frost'), Js('Golden Hope'), Js('Hope'), Js('Elemental'), Js('Impossible Girl'), Js('Griffin'), Js('Tecton'), Js('Captain Atomic'), Js('Titanio'), Js('Solar Flare'), Js('Alley Cat'), Js('Snow Storm'), Js('Absolute Zero'), Js('The Great Defender'), Js('Timeline'), Js('Skylar Storm'), Js('Optimo'), Js('Remix'), Js('Citadel'), Js('Alpha Dog'), Js('Brain Matter'), Js('Dark Warrior'), Js('The Crusher'), Js('Owl'), Js('Incognito'), Js('Gray Granite'), Js('Gamma'), Js('Spark Plug'), Js('Silver Shield'), Js('Quiver'), Js('Smoke'), Js('Captain Quake'), Js('Icicle'), Js('Metanite'), Js('Blaze'), Js('Fantasia'), Js('Phantasm'), Js('Sparks'), Js('Ace'), Js('Amethyst Heart'), Js('Animalia'), Js('Armed'), Js('Black Bat'), Js('Black Cat'), Js('Black Knight'), Js('Black Phoenix'), Js('Black Star'), Js('Blitzfire'), Js('Boler'), Js('Bolt'), Js('Brass Bison'), Js('Bright Shadow'), Js('Broken Watchman'), Js('Choicemaker'), Js('Cleanser'), Js('Crazy Eight'), Js('Creature'), Js('Criss Cross'), Js('Dark Flame'), Js('Dark Omen'), Js('Dark Titan'), Js('Dazzler'), Js('Deadnite'), Js('Death Roach'), Js('Doctor Chronos'), Js('Doctor Dynasty'), Js('Doctor Juggernaut'), Js('Doctor Titanium'), Js('Dragon Boy'), Js('Dragon Spectre'), Js('Dragonloom'), Js('Dragontooth'), Js('Electric Arrow'), Js('Eltrocus'), Js('Ethereal Phoenix'), Js('Ethereal Titan'), Js('Fallen Pheonix'), Js('Fiery Falcon'), Js('Firebird'), Js('Freefall'), Js('Frozenstar'), Js('Galactic Gargoyle'), Js('Gecko'), Js('Griffin'), Js('Heavy Step'), Js('Helon'), Js('Heloth'), Js('Hopewing'), Js('Ice Raven'), Js('Iron Archer'), Js('Iron Assassin'), Js('Jade Stranger'), Js('King Scorp'), Js('Mad Manta'), Js('Makeshift'), Js('Marked Stranger'), Js('Master Defiance'), Js('Mighty Mamba'), Js('Mister Penance'), Js('Mister X'), Js('Mister Y'), Js('Misty Manta'), Js('Moon Halo'), Js('Moonshadow'), Js('Nightbolt'), Js('Nightleaf'), Js('Nightquake'), Js('Nightwave'), Js('Orothos'), Js('Osa'), Js('Peacebringer'), Js('Phantom'), Js('Phantom Archer'), Js('Phantom Kid'), Js('Phantom Spectre'), Js('Phoen-X'), Js('Quantum Colossus'), Js('Quantum Commander'), Js('Razor'), Js('Red Heart'), Js('Rosethorn'), Js('Saber'), Js('Saberleaf'), Js('Sage'), Js('Savior'), Js('Scarlet Feathers'), Js('Scarlet Horse'), Js('Scarlet King'), Js('Scarlet Sentinel'), Js('Shaden'), Js('Shadow'), Js('Shadowleaf'), Js('Shadowstar'), Js('Silver Goliath'), Js('Silver Shepherd'), Js('Silver Wolf'), Js('Snow Raven'), Js('Spitfire'), Js('Spur'), Js('Star Sentinel'), Js('Starbright'), Js('Stareye'), Js('Starlight'), Js('Starry Night'), Js('Sunspot'), Js('Switcher'), Js('The Hunter'), Js('The Last One'), Js('Thornhead'), Js('Thunder Hawk'), Js('Thunderclap'), Js('Thundering Whisper'), Js('Venom'), Js('Venombite'), Js('Voiceless Stranger'), Js('Wi-Fire'), Js('Wild Tornado'), Js('Wildfire'), Js('Wildflame'), Js('Karma')]))
pass
pass


# Add lib to the module scope
heroNames = var.to_python()