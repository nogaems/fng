__all__ = ['wrestlerNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen', 'namesMale', 'namesFemale'])
@Js
def PyJsHoisted_nameGen_(nameFirst, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'nameFirst':nameFirst}, var)
    var.registers(['result', 'nameFirst'])
    var.put('names1', var.get('nameFirst'))
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
var.put('namesMale', Js([Js('Bane'), Js('Barrage'), Js('Beast'), Js('Birdman'), Js('Bizarre'), Js('Blade'), Js('Blitz'), Js('Blueprint'), Js('Bombardment'), Js('Boomboom'), Js('Boulderfist'), Js('Boycott'), Js('Brawn'), Js('Bullet'), Js('Buster'), Js('Canine'), Js('Carnage'), Js('Ceasar'), Js('Chaos'), Js('Classified'), Js('Clobber'), Js('Crazy Eyes'), Js('Cyclone'), Js('Daemon'), Js('Deluge'), Js('Diablo'), Js('Diesel'), Js('Digger'), Js('Domino'), Js('Drake'), Js('Dread'), Js('Dynamite'), Js('Earthquake'), Js('Extinction'), Js('Fatal Fury'), Js('Fear'), Js('Gargoyle'), Js('Genie'), Js('Ghost'), Js('Ghost Kicker'), Js('Grand Master'), Js('Grimace'), Js('Grimes'), Js('Guts'), Js('Havoc'), Js('Hazard'), Js('Heckler'), Js('Hellfire'), Js('Hellhound'), Js('Hercules'), Js('Hunter'), Js('Ironman'), Js('Jekyll'), Js('Jericho'), Js('Jester'), Js('Jitters'), Js('Karma'), Js('King'), Js('Knock Out'), Js('Kong'), Js('Macho Monster'), Js('Magician'), Js('Mayhem'), Js('Mercury'), Js('Mirage'), Js('Morpheus'), Js('Mr. Indestructible'), Js('Mutiny'), Js('Nightmare'), Js('Onyx'), Js('Paragon'), Js('Payne'), Js('Pegasus'), Js('Perfection'), Js('Pincher'), Js('Pitbull'), Js('Predator'), Js('Price'), Js('Prince'), Js('Puppeteer'), Js('Quicksilver'), Js('Raptor'), Js('Ravager'), Js('Raze'), Js('Razor'), Js('Retribution'), Js('Rhino'), Js('Riot'), Js('Rocket'), Js('Rogue'), Js('Rowdy'), Js('Sandman'), Js('Scarface'), Js('Sergeant'), Js('Slayer'), Js('Smash'), Js('Smiley'), Js('Smite'), Js('Snake'), Js('Sphinx'), Js('Striker'), Js('Suave'), Js('Swagger'), Js('Swine'), Js('Taboo'), Js('Tank'), Js('The Ambassador'), Js('The Anaconda'), Js('The Archetype'), Js('The Badger'), Js('The Barbarian'), Js('The Bodyguard'), Js('The Boulder'), Js('The Brute'), Js('The Bull'), Js('The Bulldozer'), Js('The Butcher'), Js('The Cataclysm'), Js('The Clam'), Js('The Clown'), Js('The Creature'), Js('The Crippler'), Js('The Crow'), Js('The Demolisher'), Js('The Destroyer'), Js('The Devourer'), Js('The Duke'), Js('The Edge'), Js('The Fiend'), Js('The Flash'), Js('The Flea'), Js('The Fluke'), Js('The Gambler'), Js('The Goon'), Js('The Gorilla'), Js('The Governor'), Js('The Guns'), Js('The Hallowed'), Js('The Hippo'), Js('The Hood'), Js('The Hound'), Js('The Hurricane'), Js('The Hyena'), Js('The Immortal'), Js('The Innovator'), Js('The Jackal'), Js('The King'), Js('The Legend'), Js('The Maestro'), Js('The Man'), Js('The Marauder'), Js('The Martyr'), Js('The Messenger'), Js('The Mongrel'), Js('The Mountain'), Js('The Oak'), Js('The Ogre'), Js('The Punisher'), Js('The Punk'), Js('The Pursuer'), Js('The Quake'), Js('The Savage'), Js('The Scout'), Js('The Sorceror'), Js('The Stalker'), Js('The Storm'), Js('The Strangler'), Js('The Surgeon'), Js('The Terror'), Js('The Thunder'), Js('The Tormentor'), Js('The Torrent'), Js('The Typhoon'), Js('The Unforgiving'), Js('The Viper'), Js('The Void'), Js('The Volcano'), Js('The Wrath'), Js('Thruster'), Js('Thump'), Js('Thunderbolt'), Js('Thundercrack'), Js('Tremor'), Js('Twister'), Js('Undertaker'), Js('Ursus'), Js('Whiz'), Js('Wicked'), Js('Wolf'), Js('Wrath-hog')]))
var.put('namesFemale', Js([Js('Anemone'), Js('Angel'), Js('Aries'), Js('Aura'), Js('Black Widow'), Js('Blitz'), Js('Blue Rose'), Js('Camille'), Js('Caramel'), Js('Celeste'), Js('Chance'), Js('Charity'), Js('Coral'), Js('Curtains'), Js('Desire'), Js('Destiny'), Js('Diamond'), Js('Divine'), Js('Drama'), Js('Elastic'), Js('Electric'), Js('Enigma'), Js('Essence'), Js('Eternity'), Js('Feline'), Js('Fortuna'), Js('Fortune'), Js('Gale'), Js('Gem'), Js('Gemini'), Js('Ginger'), Js('Gloria'), Js('Harpy'), Js('Hope'), Js('Iconiq'), Js('Ivory'), Js('Ivy'), Js('Jade'), Js('Jasmine'), Js('Jewel'), Js('Karma'), Js('Katana'), Js('Kayo'), Js('Key'), Js('Knock Out'), Js('Libra'), Js('Lights'), Js('Lioness'), Js('Luna'), Js('Maneater'), Js('Mantis'), Js('Mantra'), Js('Melody'), Js('Miss Fortune'), Js('Missy'), Js('Mistral'), Js('Moxie'), Js('Mystique'), Js('Nourisha'), Js('Obsession'), Js('Onyxia'), Js('Onyxis'), Js('Phobia'), Js('Promise'), Js('Raven'), Js('Remedy'), Js('Rogue'), Js('Rose'), Js('Ruby'), Js('Saffron'), Js('Sanguine'), Js('Sapphire'), Js('Scarlet'), Js('Serenity'), Js('Succubus'), Js('Tazz'), Js('Tempest'), Js('The Amazon'), Js('The Cat'), Js('The Oracle'), Js('The Smile'), Js('The Witch'), Js('Tigress'), Js('Twinkle'), Js('Vanity'), Js('Velvet'), Js('Venus'), Js('Violette'), Js('Virus'), Js('Wildflower'), Js('Willow')]))
pass
pass


# Add lib to the module scope
wrestlerNames = var.to_python()