__all__ = ['pacificRimNames']

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
    var.registers(['nm1', 'nm4', 'nm5', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Ace'), Js('Adder'), Js('Ancient'), Js('Arachnid'), Js('Arcadia'), Js('Azure'), Js('Barbarian'), Js('Basilisk'), Js('Battler'), Js('Beard'), Js('Beast'), Js('Beelzebub'), Js('Beryl'), Js('Boar'), Js('Bobcat'), Js('Bohemian'), Js('Bold'), Js('Brawler'), Js('Brilliant'), Js('Bruiser'), Js('Brute'), Js('Butcher'), Js('Canine'), Js('Cardinal'), Js('Carmine'), Js('Catamount'), Js('Centaur'), Js('Cerulean'), Js('Cherno'), Js('Chinook'), Js('Chrome'), Js('Cobalt'), Js('Cobra'), Js('Cold'), Js('Colossus'), Js('Cosmic'), Js('Cougar'), Js('Coyote'), Js('Crimson'), Js('Dark'), Js('Dastard'), Js('Diablo'), Js('Diligent'), Js('Djinn'), Js('Duke'), Js('Dybbuk'), Js('Ebon'), Js('Echo'), Js('Eden'), Js('Edge'), Js('Empyreal'), Js('Enigma'), Js('Epitome'), Js('Exalted'), Js('Feline'), Js('Forsaken'), Js('Fox'), Js('Frankenstein'), Js('Freak'), Js('Frozen'), Js('Fury'), Js('Gargoyle'), Js('Giant'), Js('Gipsy'), Js('Gladiator'), Js('Glory'), Js('Grand'), Js('Grave'), Js('Griffon'), Js('Grim'), Js('Guardian'), Js('Harmony'), Js('Heliacal'), Js('Hellion'), Js('Hermit'), Js('Hollow'), Js('Horizon'), Js('Hound'), Js('Hunger'), Js('Hungry'), Js('Hunter'), Js('Hydra'), Js('Hyena'), Js('Imp'), Js('Infinite'), Js('Ironclad'), Js('Ivory'), Js('Jackal'), Js('Jester'), Js('Jigsaw'), Js('Jinx'), Js('Judge'), Js('Juvenile'), Js('Keen'), Js('Knave'), Js('Kraken'), Js('Light'), Js('Lucifer'), Js('Lucky'), Js('Mad'), Js('Majestic'), Js('Malachite'), Js('Mammoth'), Js('Maroon'), Js('Matador'), Js('Menace'), Js('Mephistopheles'), Js('Mercenary'), Js('Muse'), Js('Mute'), Js('Nightowl'), Js('Nomad'), Js('Obsidian'), Js('Ogre'), Js('Onyx'), Js('Oracle'), Js('Ornate'), Js('Ox'), Js('Paladin'), Js('Panther'), Js('Paragon'), Js('Patient'), Js('Phoenix'), Js('Pinnacle'), Js('Primal'), Js('Prime'), Js('Prospect'), Js('Puma'), Js('Quiet'), Js('Rattle'), Js('Rebel'), Js('Reckless'), Js('Rhino'), Js('Rogue'), Js('Romeo'), Js('Sanguine'), Js('Savage'), Js('Scoundral'), Js('Scourge'), Js('Secret'), Js('Serenity'), Js('Serpent'), Js('Shangri-La'), Js('Shoalin'), Js('Silent'), Js('Slayer'), Js('Solar'), Js('Soothsayer'), Js('Spider'), Js('Stalker'), Js('Stark'), Js('Stellar'), Js('Striker'), Js('Surgeon'), Js('Tacit'), Js('Tango'), Js('Tanker'), Js('Tarragon'), Js('Titan'), Js('Titanic'), Js('Toreador'), Js('Torero'), Js('Treasure'), Js('Tyrant'), Js('Vagrant'), Js('Valiant'), Js('Viper'), Js('Voodoo'), Js('Vortex'), Js('Vulcan'), Js('Vulture'), Js('Warlord'), Js('Warmonger'), Js('Warrior'), Js('Watcher'), Js('Weasel'), Js('Werewolf'), Js('Wicked'), Js('Widow'), Js('Wildcat'), Js('Witch'), Js('Wolf'), Js('Wretched'), Js('Wyvern'), Js('Zingara')]))
    var.put('nm2', Js([Js('Ace'), Js('Adder'), Js('Ancient'), Js('Arachnid'), Js('Assassin'), Js('Barbarian'), Js('Basilisk'), Js('Battler'), Js('Beast'), Js('Beelzebub'), Js('Boar'), Js('Bobcat'), Js('Bohemian'), Js('Brawler'), Js('Bruiser'), Js('Brute'), Js('Brutus'), Js('Butcher'), Js('Canine'), Js('Centaur'), Js('Chinook'), Js('Cobra'), Js('Colossus'), Js('Cougar'), Js('Coyote'), Js('Danger'), Js('Diablo'), Js('Djinn'), Js('Duke'), Js('Echo'), Js('Eden'), Js('Edge'), Js('Enigma'), Js('Epitome'), Js('Fox'), Js('Frankenstein'), Js('Freak'), Js('Fury'), Js('Gargoyle'), Js('Giant'), Js('Gladiator'), Js('Glory'), Js('Grave'), Js('Griffon'), Js('Guardian'), Js('Gypsy'), Js('Heliacal'), Js('Hellion'), Js('Hermit'), Js('Horizon'), Js('Hound'), Js('Hunger'), Js('Hunter'), Js('Hydra'), Js('Hyena'), Js('Imp'), Js('Jackal'), Js('Jester'), Js('Jigsaw'), Js('Jinx'), Js('Judge'), Js('Juvenile'), Js('Knave'), Js('Kraken'), Js('Light'), Js('Lucifer'), Js('Mammoth'), Js('Maroon'), Js('Matador'), Js('Menace'), Js('Mephistopheles'), Js('Mercenary'), Js('Muse'), Js('Mute'), Js('Nightowl'), Js('Nomad'), Js('Obsidian'), Js('Ogre'), Js('Onyx'), Js('Oracle'), Js('Ox'), Js('Paladin'), Js('Panther'), Js('Paragon'), Js('Patient'), Js('Phoenix'), Js('Pinnacle'), Js('Primal'), Js('Prime'), Js('Prophet'), Js('Prospect'), Js('Puma'), Js('Rebel'), Js('Rhino'), Js('Rogue'), Js('Romeo'), Js('Ronin'), Js('Saber'), Js('Savage'), Js('Scoundrel'), Js('Scourge'), Js('Secret'), Js('Serenity'), Js('Serpent'), Js('Shoalin'), Js('Slayer'), Js('Soothsayer'), Js('Spider'), Js('Stalker'), Js('Stark'), Js('Striker'), Js('Surgeon'), Js('Tango'), Js('Tanker'), Js('Tarragon'), Js('Titan'), Js('Titanic'), Js('Toreador'), Js('Torero'), Js('Treasure'), Js('Typhoon'), Js('Tyrant'), Js('Vagrant'), Js('Viper'), Js('Voodoo'), Js('Vortex'), Js('Vulcan'), Js('Vulture'), Js('Warlord'), Js('Warmonger'), Js('Warrior'), Js('Watcher'), Js('Weasel'), Js('Werewolf'), Js('Widow'), Js('Wildcat'), Js('Witch'), Js('Wolf'), Js('Wretched'), Js('Wyvern'), Js('Zingara')]))
    var.put('nm3', Js([Js('barb'), Js('blade'), Js('bone'), Js('chest'), Js('cinder'), Js('claw'), Js('crag'), Js('crest'), Js('crook'), Js('crystal'), Js('dagger'), Js('death'), Js('dirge'), Js('dust'), Js('edge'), Js('ember'), Js('fang'), Js('frost'), Js('fuse'), Js('gore'), Js('hammer'), Js('heart'), Js('hook'), Js('ice'), Js('iron'), Js('knife'), Js('lance'), Js('leather'), Js('light'), Js('meat'), Js('molten'), Js('pincer'), Js('pyre'), Js('rage'), Js('ridge'), Js('saber'), Js('sabre'), Js('scythe'), Js('shade'), Js('shadow'), Js('shank'), Js('sharp'), Js('shiv'), Js('silver'), Js('skull'), Js('slate'), Js('solid'), Js('spike'), Js('spine'), Js('steel'), Js('tail'), Js('talon'), Js('thorn'), Js('thunder'), Js('tusk')]))
    var.put('nm4', Js([Js('back'), Js('basher'), Js('blade'), Js('blight'), Js('blower'), Js('bone'), Js('breaker'), Js('breath'), Js('claw'), Js('cleaver'), Js('crest'), Js('crusher'), Js('cutter'), Js('drifter'), Js('eye'), Js('eyes'), Js('fang'), Js('fangs'), Js('fist'), Js('flayer'), Js('fury'), Js('gazer'), Js('hammer'), Js('head'), Js('heart'), Js('hook'), Js('hunter'), Js('jaw'), Js('lance'), Js('mane'), Js('mantle'), Js('maul'), Js('maw'), Js('pelt'), Js('reaper'), Js('reaver'), Js('ridge'), Js('ripper'), Js('snout'), Js('spitter'), Js('splitter'), Js('stalker'), Js('striker'), Js('weaver')]))
    var.put('nm5', Js([Js('Ache'), Js('Aggressor'), Js('Agitator'), Js('Assaulter'), Js('Austerity'), Js('Battler'), Js('Beast'), Js('Brawler'), Js('Bruiser'), Js('Brute'), Js('Bulldozer'), Js('Bully'), Js('Calamity'), Js('Cataclysm'), Js('Contender'), Js('Curse'), Js('Defiler'), Js('Deserter'), Js('Disrupter'), Js('Dissenter'), Js('Distress'), Js('Doom'), Js('Downfall'), Js('Encroacher'), Js('Fiend'), Js('Gloom'), Js('Grief'), Js('Grievance'), Js('Hardship'), Js('Harrier'), Js('Hazard'), Js('Headache'), Js('Hellion'), Js('Infringer'), Js('Injury'), Js('Insurrector'), Js('Intimidator'), Js('Intruder'), Js('Invader'), Js('Jeopardy'), Js('Misery'), Js('Neglector'), Js('Objector'), Js('Opposer'), Js('Oppressor'), Js('Peril'), Js('Radical'), Js('Raider'), Js('Rascal'), Js('Rebel'), Js('Reckoner'), Js('Resister'), Js('Revolter'), Js('Rigor'), Js('Rioter'), Js('Ruffian'), Js('Ruin'), Js('Savage'), Js('Scourge'), Js('Scrapper'), Js('Shirker'), Js('Slugger'), Js('Sorrow'), Js('Squalor'), Js('Stitch'), Js('Striker'), Js('Suffering'), Js('Tanker'), Js('Torment'), Js('Tormenter'), Js('Torture'), Js('Transgressor'), Js('Trespasser'), Js('Tribulation'), Js('Violator'), Js('Woe'), Js('Wreck'), Js('Wreckage'), Js('Wrecker')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                while PyJsStrictEq(var.get('nm1').get(var.get('rnd')),var.get('nm2').get(var.get('rnd2'))):
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
                var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
            else:
                if (var.get('i')<Js(5.0)):
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                    var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    while PyJsStrictEq(var.get('nm3').get(var.get('rnd')),var.get('nm4').get(var.get('rnd2'))):
                        var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                    var.put('names', (var.get('nm3').get(var.get('rnd'))+var.get('nm4').get(var.get('rnd2'))))
                    var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
                    var.get('nm4').callprop('splice', var.get('rnd2'), Js(1.0))
                else:
                    var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                    var.put('names', var.get('nm5').get(var.get('rnd')))
                    var.get('nm5').callprop('splice', var.get('rnd'), Js(1.0))
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
pacificRimNames = var.to_python()