__all__ = ['monsterNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm7', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                    var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                    var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                    var.put('names', (((((Js('The ')+var.get('nm5').get(var.get('rnd')))+Js(' '))+var.get('nm6').get(var.get('rnd2')))+Js(' '))+var.get('nm7').get(var.get('rnd3'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Acidic'), Js('Active'), Js('Aged'), Js('Agile'), Js('Agitated'), Js('Ancient'), Js('Angry'), Js('Anguished'), Js('Arctic'), Js('Arid'), Js('Aromatic'), Js('Awful'), Js('Barren'), Js('Bewitched'), Js('Big Bad'), Js('Bitter'), Js('Black'), Js('Bleak'), Js('Blind'), Js('Blissful'), Js('Blue'), Js('Bold'), Js('Broken'), Js('Bronze'), Js('Brown'), Js('Bruised'), Js('Calm'), Js('Canine'), Js('Cloudy'), Js('Cold'), Js('Colossal'), Js('Corrupt'), Js('Crazy'), Js('Creepy'), Js('Cruel'), Js('Dangerous'), Js('Dark'), Js('Dead'), Js('Deadly'), Js('Defiant'), Js('Delirious'), Js('Dirty'), Js('Disfigured'), Js('Disgusting'), Js('Dismal'), Js('Dreary'), Js('Electric'), Js('Empty'), Js('Enraged'), Js('Eternal'), Js('Evil'), Js('Faint'), Js('False'), Js('Feline'), Js('Fickle'), Js('Filthy'), Js('Forsaken'), Js('Giant'), Js('Gray'), Js('Greedy'), Js('Grim'), Js('Gross'), Js('Grotesque'), Js('Gruesome'), Js('Grumpy'), Js('Hairy'), Js('Half'), Js('Haunting'), Js('Hidden'), Js('Hollow'), Js('Horrible'), Js('Hungry'), Js('Icy'), Js('Infamous'), Js('Insane'), Js('Insidious'), Js('Jagged'), Js('Lanky'), Js('Lean'), Js('Living'), Js('Lone'), Js('Lonely'), Js('Mad'), Js('Meager'), Js('Mean'), Js('Monstrous'), Js('Muted'), Js('Nasty'), Js('Needy'), Js('Noxious'), Js('Outlandish'), Js('Parallel'), Js('Putrid'), Js('Quick'), Js('Quiet'), Js('Reckless'), Js('Rotten'), Js('Shady'), Js('Sick'), Js('Skeletal'), Js('Tall'), Js('Thin'), Js('Twin'), Js('Ugly'), Js('Undead'), Js('Vengeful'), Js('Volatile'), Js('White'), Js('Wild'), Js('Wretched')]))
var.put('nm2', Js([Js('Man'), Js('Woman'), Js('Child'), Js('Mutant'), Js('Abomination'), Js('Glob'), Js('Monster'), Js('Behemoth'), Js('Beast'), Js('Freak'), Js('Horror'), Js('Fiend'), Js('Abnormality'), Js('Brute'), Js('Miscreation'), Js('Monstrosity'), Js('Savage'), Js('Deformity'), Js('Deviation'), Js('Anomaly'), Js('Weirdo'), Js('Abortion'), Js('Malformation'), Js('Blob'), Js('Lump'), Js('Bulge'), Js('Tumor'), Js('Creature'), Js('Critter'), Js('Vermin'), Js('Being'), Js('Thing'), Js('Revenant'), Js('Keeper'), Js('Guardian'), Js('Witch'), Js('Troglodyte'), Js('Charmer'), Js('Vine'), Js('Tree'), Js('Plant'), Js('Howler'), Js('Statue'), Js('Vision'), Js('Dweller'), Js('Lich'), Js('Pest'), Js('Gnoll'), Js('Ooze'), Js('Hag'), Js('Hunter'), Js('Entity'), Js('Phenomenon'), Js('Body'), Js('Figure'), Js('Presence'), Js('Corpse'), Js('Demon'), Js('Wraith'), Js('Herder'), Js('Mongrel'), Js('Hybrid'), Js('Mutt'), Js('Teeth'), Js('Eyes'), Js('Face'), Js('Screamer'), Js('Howler'), Js('Shrieker'), Js('Wailer'), Js('Babbler'), Js('Mumbler'), Js('Creeper')]))
var.put('nm3', Js([Js('Abyss'), Js('Acid'), Js('Ash'), Js('Aura'), Js('Bane'), Js('Barb'), Js('Blade'), Js('Blaze'), Js('Blight'), Js('Bone'), Js('Boulder'), Js('Bowel'), Js('Brine'), Js('Cave'), Js('Cavern'), Js('Chaos'), Js('Cinder'), Js('Cloud'), Js('Coffin'), Js('Corpse'), Js('Crypt'), Js('Curse'), Js('Dawn'), Js('Decay'), Js('Doom'), Js('Dread'), Js('Dream'), Js('Dusk'), Js('Dust'), Js('Ember'), Js('Fetid'), Js('Flame'), Js('Fog'), Js('Foul'), Js('Fright'), Js('Frost'), Js('Gall'), Js('Gas'), Js('Germ'), Js('Gloom'), Js('Glow'), Js('Grave'), Js('Grieve'), Js('Grime'), Js('Gut'), Js('Haunt'), Js('Hell'), Js('Hollow'), Js('Horror'), Js('Infernal'), Js('Inferno'), Js('Metal'), Js('Mist'), Js('Mold'), Js('Morn'), Js('Mourn'), Js('Murk'), Js('Nether'), Js('Night'), Js('Phantom'), Js('Phase'), Js('Plague'), Js('Poison'), Js('Putrid'), Js('Razor'), Js('Rot'), Js('Rotting'), Js('Rust'), Js('Shade'), Js('Shadow'), Js('Slag'), Js('Smog'), Js('Smoke'), Js('Soil'), Js('Sorrow'), Js('Soul'), Js('Spectral'), Js('Spirit'), Js('Spite'), Js('Steam'), Js('Stench'), Js('Stink'), Js('Stone'), Js('Taint'), Js('Tangle'), Js('Terror'), Js('Thorn'), Js('Thunder'), Js('Tomb'), Js('Toxin'), Js('Trance'), Js('Umbra'), Js('Vamp'), Js('Vapor'), Js('Venom'), Js('Vex'), Js('Vile'), Js('Voodoo'), Js('Vortex'), Js('Warp'), Js('Web'), Js('Wisp')]))
var.put('nm4', Js([Js('beast'), Js('being'), Js('body'), Js('boy'), Js('brood'), Js('morph'), Js('brute'), Js('bug'), Js('cat'), Js('child'), Js('claw'), Js('crackle'), Js('creep'), Js('deviation'), Js('face'), Js('fang'), Js('fiend'), Js('figure'), Js('flayer'), Js('foot'), Js('freak'), Js('ghoul'), Js('girl'), Js('golem'), Js('hag'), Js('hand'), Js('hood'), Js('hound'), Js('lich'), Js('ling'), Js('ling'), Js('ling'), Js('ling'), Js('man'), Js('mask'), Js('mirage'), Js('monster'), Js('mouth'), Js('mutant'), Js('paw'), Js('pest'), Js('pod'), Js('scream'), Js('screamer'), Js('seeker'), Js('serpent'), Js('snake'), Js('snare'), Js('soul'), Js('spawn'), Js('step'), Js('strike'), Js('sword'), Js('talon'), Js('taur'), Js('teeth'), Js('thing'), Js('tooth'), Js('tree'), Js('vine'), Js('wing'), Js('wings'), Js('woman'), Js('wraith')]))
var.put('nm5', Js([Js('Agile'), Js('Amphibian'), Js('Aquatic'), Js('Arctic'), Js('Barb-Tailed'), Js('Black-Eyed'), Js('Black-Striped'), Js('Blind'), Js('Blood-Eyed'), Js('Bloodthirsty'), Js('Bright'), Js('Brutal'), Js('Burnt'), Js('Chaotic'), Js('Cobalt'), Js('Cold-Blooded'), Js('Crazed'), Js('Crimson'), Js('Crowned'), Js('Dark'), Js('Diabolical'), Js('Ebon'), Js('Electric'), Js('Elusive'), Js('Evasive'), Js('Feathered'), Js('Feral'), Js('Fiery'), Js('Furry'), Js('Giant'), Js('Glacial'), Js('Golden'), Js('Greater'), Js('Grim'), Js('Grisly'), Js('Hidden'), Js('Horned'), Js('Howling'), Js('Iron'), Js('Iron-Scaled'), Js('Ivory'), Js('Jade'), Js('Lone'), Js('Long-Horned'), Js('Mad'), Js('Malevolent'), Js('Masked'), Js('Matriarch'), Js('Monstrous'), Js('Obsidian'), Js('Onyx'), Js('Painted'), Js('Patriarch'), Js('Primeval'), Js('Primitive'), Js('Rabid'), Js('Raging'), Js('Ravaging'), Js('Red-Eyed'), Js('Ruthless'), Js('Sapphire'), Js('Savage'), Js('Scarred'), Js('Screeching'), Js('Silver'), Js('Silver-Striped'), Js('Slender'), Js('Stalking'), Js('Stormcloud'), Js('Supreme'), Js('Taloned'), Js('Tattooed'), Js('Titanic'), Js('Titanium'), Js('Tusked'), Js('Vicious'), Js('White-Eyed'), Js('Wild')]))
var.put('nm6', Js([Js('Army'), Js('Ash'), Js('Assassin'), Js('Bane'), Js('Berserker'), Js('Blaze'), Js('Blight'), Js('Bone'), Js('Boulder'), Js('Butcher'), Js('Cave'), Js('Cavern'), Js('Cinder'), Js('Corpse'), Js('Dawn'), Js('Demon'), Js('Dire'), Js('Doom'), Js('Dread'), Js('Flame'), Js('Frost'), Js('Ghost'), Js('Grieve'), Js('Harlequin'), Js('Horror'), Js('Hunting'), Js('Jester'), Js('Killer'), Js('Mist'), Js('Mocking'), Js('Moon'), Js('Mountain'), Js('Nether'), Js('Night'), Js('Nightmare'), Js('Phantom'), Js('Predator'), Js('Preying'), Js('Raptor'), Js('Razor'), Js('Razorback'), Js('Rot'), Js('Shadow'), Js('Skeleton'), Js('Slayer'), Js('Spite'), Js('Storm'), Js('Sun'), Js('Terror'), Js('Thunder'), Js('Tomb'), Js('Torment'), Js('Vampire'), Js('Venom'), Js('Vision'), Js('Warp'), Js('World')]))
var.put('nm7', Js([Js('Alligator'), Js('Anaconda'), Js('Ape'), Js('Bat'), Js('Bear'), Js('Beast'), Js('Bee'), Js('Behemoth'), Js('Bison'), Js('Boar'), Js('Buffalo'), Js('Bull'), Js('Cat'), Js('Cobra'), Js('Critter'), Js('Crocodile'), Js('Deer'), Js('Dog'), Js('Dragon'), Js('Drake'), Js('Elephant'), Js('Fiend'), Js('Freak'), Js('Frog'), Js('Gargoyle'), Js('Gorilla'), Js('Hawk'), Js('Hippo'), Js('Hog'), Js('Hound'), Js('Hyena'), Js('Jackal'), Js('Leopard'), Js('Leviathan'), Js('Lion'), Js('Lizard'), Js('Lynx'), Js('Monkey'), Js('Monster'), Js('Owl'), Js('Panther'), Js('Phoenix'), Js('Pig'), Js('Rat'), Js('Rhino'), Js('Scorpion'), Js('Serpent'), Js('Sheep'), Js('Snake'), Js('Spider'), Js('Swine'), Js('Tiger'), Js('Vermin'), Js('Viper'), Js('Warthog'), Js('Wolf'), Js('Yak')]))
pass
pass


# Add lib to the module scope
monsterNames = var.to_python()