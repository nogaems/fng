__all__ = ['seaCreatureNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd'))+var.get('nm2').get(var.get('rnd2')))+var.get('nm3').get(var.get('rnd3')))+var.get('nm2').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', (((((Js('The ')+var.get('nm5').get(var.get('rnd')))+Js(' '))+var.get('nm6').get(var.get('rnd2')))+Js(' '))+var.get('nm7').get(var.get('rnd3'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                    var.put('names', var.get('nm8').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('B'), Js('Bl'), Js('Cr'), Js('Ch'), Js('G'), Js('Gl'), Js('Gr'), Js('H'), Js('J'), Js('K'), Js('Kr'), Js('L'), Js('M'), Js('S'), Js('Sc'), Js('Tr'), Js('Z')]))
var.put('nm2', Js([Js('o'), Js('a'), Js('a'), Js('o'), Js('e'), Js('i'), Js('u'), Js('y')]))
var.put('nm3', Js([Js('bd'), Js('bs'), Js('dr'), Js('gl'), Js('gn'), Js('gm'), Js('gr'), Js('k'), Js('kr'), Js('kl'), Js('ll'), Js('nd'), Js('nr'), Js('ng'), Js('r'), Js('rg'), Js('rk'), Js('rc'), Js('sc'), Js('st'), Js('sk'), Js('sh'), Js('tr'), Js('th'), Js('q'), Js('z')]))
var.put('nm4', Js([Js(''), Js(''), Js('d'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('r'), Js('s'), Js('sh'), Js('wr'), Js('x')]))
var.put('nm5', Js([Js('Agile'), Js('Amphibian'), Js('Arctic'), Js('Barb-Tailed'), Js('Barbed'), Js('Beaked'), Js('Bigeyed'), Js('Black-Eyed'), Js('Black-Striped'), Js('Blind'), Js('Blood-Eyed'), Js('Bloodthirsty'), Js('Boulder-Scaled'), Js('Bright'), Js('Brutal'), Js('Chaotic'), Js('Clouded'), Js('Cobalt'), Js('Cold-Blooded'), Js('Colossal'), Js('Crazed'), Js('Crimson'), Js('Crowned'), Js('Dark'), Js('Deep Sea'), Js('Diabolical'), Js('Ebon'), Js('Electric'), Js('Elusive'), Js('Evasive'), Js('Feral'), Js('Flying'), Js('Four-Eyed'), Js('Giant'), Js('Giant-Fin'), Js('Gigantic'), Js('Glowing'), Js('Golden'), Js('Greater'), Js('Grim'), Js('Herculean'), Js('Horned'), Js('Iron'), Js('Iron-Scaled'), Js('Ivory'), Js('Jade'), Js('Largetooth'), Js('Lone'), Js('Long-Horned'), Js('Long-Tailed'), Js('Mad'), Js('Malevolent'), Js('Mammoth'), Js('Masked'), Js('Matriarch'), Js('Megamouth'), Js('Monstrous'), Js('Murky'), Js('Nervous'), Js('Nimble'), Js('Obsidian'), Js('One-Eyed'), Js('Onyx'), Js('Painted'), Js('Patriarch'), Js('Preying'), Js('Primeval'), Js('Primitive'), Js('Rabid'), Js('Raging'), Js('Rapid'), Js('Ravaging'), Js('Red-Eyed'), Js('Ribbon-Tailed'), Js('Ruthless'), Js('Sapphire'), Js('Savage'), Js('Scarred'), Js('Silent'), Js('Silver'), Js('Silver-Striped'), Js('Slender'), Js('Spiky'), Js('Stalking'), Js('Supreme'), Js('Swift'), Js('Thorn-Scaled'), Js('Titanic'), Js('Titanium'), Js('Vicious'), Js('White-Eyed'), Js('Wild'), Js('Winged')]))
var.put('nm6', Js([Js('Angel'), Js('Apocalypse'), Js('Army'), Js('Arrow'), Js('Assassin'), Js('Blaze'), Js('Blight'), Js('Bone'), Js('Boulder'), Js('Bull'), Js('Butcher'), Js('Cannibal'), Js('Chaos'), Js('Corpse'), Js('Crocodile'), Js('Dagger'), Js('Dawn'), Js('Demon'), Js('Dino'), Js('Dire'), Js('Doom'), Js('Dragon'), Js('Dread'), Js('Ghost'), Js('Goblin'), Js('Grieve'), Js('Harlequin'), Js('Hell'), Js('Horror'), Js('Hound'), Js('Hunting'), Js('Jelly'), Js('Jester'), Js('Killer'), Js('Leopard'), Js('Lion'), Js('Lizard'), Js('Mayhem'), Js('Miracle'), Js('Mocking'), Js('Monster'), Js('Nether'), Js('Night'), Js('Nightmare'), Js('Ogre'), Js('Phantom'), Js('Predator'), Js('Puffer'), Js('Raptor'), Js('Razor'), Js('Requiem'), Js('Rock'), Js('Rogue'), Js('Sand'), Js('Serpent'), Js('Shadow'), Js('Skeleton'), Js('Slayer'), Js('Sleeper'), Js('Slumber'), Js('Spider'), Js('Spine'), Js('Spite'), Js('Storm'), Js('Sword'), Js('Tentacle'), Js('Terror'), Js('Thunder'), Js('Tiger'), Js('Torment'), Js('Tresher'), Js('Vampire'), Js('Venom'), Js('Void'), Js('Wonder'), Js('World')]))
var.put('nm7', Js([Js('Beast'), Js('Behemoth'), Js('Clam'), Js('Crab'), Js('Devil'), Js('Dolphin'), Js('Eel'), Js('Fiend'), Js('Fish'), Js('Leviathan'), Js('Lobster'), Js('Octopus'), Js('Orka'), Js('Ray'), Js('Seal'), Js('Shark'), Js('Snake'), Js('Squid'), Js('Turtle'), Js('Whale'), Js('Worm')]))
var.put('nm8', Js([Js('Alliconda'), Js('Alliganha'), Js('Alligatopus'), Js('Clamaconda'), Js('Clamiranha'), Js('Clamster'), Js('Clamtopus'), Js('Crabaconda'), Js('Crabemoth'), Js('Crabiathan'), Js('Crabiranha'), Js('Crabshark'), Js('Crabtopus'), Js('Dolpheel'), Js('Dolphemoth'), Js('Dolphiathan'), Js('Dolphiconda'), Js('Dolphigator'), Js('Dolphipus'), Js('Dolphiranha'), Js('Dolphiray'), Js('Dolphishark'), Js('Eelaconda'), Js('Eeligator'), Js('Eelodile'), Js('Lobstaconda'), Js('Lobstagator'), Js('Lobstemoth'), Js('Lobsteranha'), Js('Lobsteray'), Js('Lobstiathan'), Js('Lobstodile'), Js('Lobstopus'), Js('Lobstorka'), Js('Lobsturtle'), Js('Orkagator'), Js('Orkallion'), Js('Orkiathan'), Js('Orktopus'), Js('Pirahnopus'), Js('Piranhagator'), Js('Piranharay'), Js('Piranhashark'), Js('Piranheel'), Js('Piranhemoth'), Js('Piranhiathan'), Js('Piranhobster'), Js('Piranhopus'), Js('Piranhorka'), Js('Sealaconda'), Js('Sealcroc'), Js('Sealiathan'), Js('Sealligator'), Js('Sharkaconda'), Js('Sharkanha'), Js('Sharkeel'), Js('Sharkellion'), Js('Sharkemoth'), Js('Sharkfiend'), Js('Sharkigator'), Js('Sharkodil'), Js('Sharkray'), Js('Sharksnake'), Js('Sharksquid'), Js('Sharktopus'), Js('Sharkworm'), Js('Snaketopus'), Js('Squidaconda'), Js('Squidigator'), Js('Squidodile'), Js('Squidshark'), Js('Squitopus'), Js('Turtleconda'), Js('Turtledile'), Js('Turtleviathan'), Js('Turtligator'), Js('Turtlobster'), Js('Whalaconda'), Js('Whalecroc'), Js('Whaletopus'), Js('Whaliathan')]))
pass
pass


# Add lib to the module scope
seaCreatureNames = var.to_python()