__all__ = ['zombieTypes']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'result'])
    var.put('nm1', Js([Js('Acher'), Js('Acid Zombie'), Js('Advanced Zombie'), Js('Ambush Zombie'), Js('Augmented Zombie'), Js('Bambino'), Js('Barfer'), Js('Barker'), Js('Bawler'), Js('Bender'), Js('Berserker'), Js('Bilger'), Js('Biter'), Js('Blaster'), Js('Blazer'), Js('Bleeder'), Js('Blight Zombie'), Js('Bloater'), Js('Bloomer'), Js('Blubber Zombie'), Js('Bluster Zombie'), Js('Bony Zombie'), Js('Boomer'), Js('Bouncer'), Js('Brawler'), Js('Brittle Zombie'), Js('Broken Zombie'), Js('Brooder'), Js('Browser'), Js('Brute'), Js('Burner'), Js('Burster'), Js('Busted Zombie'), Js('Buster'), Js('Cackler'), Js('Camo Zombie'), Js('Cannibal'), Js('Carnal Zombie'), Js('Carrier'), Js('Chaser'), Js('Chewer'), Js('Chomper'), Js('Chopper'), Js('Chubber'), Js('Chum'), Js('Chunky'), Js('Clacker'), Js('Clamper'), Js('Cleaner'), Js('Cleaver'), Js('Clicker'), Js('Climber'), Js('Cougher'), Js('Courier'), Js('Cracker'), Js('Crawler'), Js('Crazed Zombie'), Js('Crazy Zombie'), Js('Creeper'), Js('Crispy'), Js('Crowd Zombie'), Js('Crumbler'), Js('Crusher'), Js('Crusty'), Js('Cryer'), Js('Curious Zombie'), Js('Dancer'), Js('Darter'), Js('Dasher'), Js('Deducer'), Js('Defective Zombie'), Js('Digger'), Js('Dissolver'), Js('Dreamer'), Js('Drencher'), Js('Dribbler'), Js('Dripper'), Js('Driver'), Js('Drizzler'), Js('Drooper'), Js('Dropper'), Js('Drowner'), Js('Eager Zombie'), Js('Enhanced Zombie'), Js('Enhancer'), Js('Evolver'), Js('Experiment'), Js('Experimental Zombie'), Js('Exploder'), Js('Fader'), Js('Fanatic'), Js('Fatty'), Js('Feeder'), Js('Feeler'), Js('Feral Zombie'), Js('Fetid Zombie'), Js('Fighter'), Js('Flamer'), Js('Flasher'), Js('Fleshy Zombie'), Js('Flipper'), Js('Floater'), Js('Flocker'), Js('Foamer'), Js('Follower'), Js('Forager'), Js('Fragment'), Js('Fragmented Zombie'), Js('Frantic'), Js('Freak'), Js('Frenzied'), Js('Friendly Zombie'), Js('Frother'), Js('Fungi'), Js('Fungus Zombie'), Js('Fuser'), Js('Gagger'), Js('Gaunt Zombie'), Js('Glazer'), Js('Glider'), Js('Gnawer'), Js('Gobbler'), Js('Grasper'), Js('Grazer'), Js('Griever'), Js('Groaner'), Js('Grower'), Js('Grumbler'), Js('Grunter'), Js('Gusher'), Js('Hacker'), Js('Haunter'), Js('Hefty Zombie'), Js('Herd Zombie'), Js('Herder'), Js('Hider'), Js('Higher'), Js('Hook Zombie'), Js('Hopper'), Js('Horde Zombie'), Js('Howler'), Js('Hunter'), Js('Hurler'), Js('Husk Zombie'), Js('Husky Zombie'), Js('Hyper Zombie'), Js('Icicle Zombie'), Js('Infant Zombie'), Js('Inflated'), Js('Intelligent Zombie'), Js('Itcher'), Js('Joker'), Js('Jumper'), Js('Lanky Zombie'), Js('Leaper'), Js('Learner'), Js('Leecher'), Js('Licker'), Js('Limper'), Js('Little Zombie'), Js('Lurker'), Js('Mad Zombie'), Js('Melter'), Js('Mindless Zombie'), Js('Moaner'), Js('Mob Zombie'), Js('Mourner'), Js('Muller'), Js('Mumbler'), Js('Muncher'), Js('Mutant'), Js('Mute'), Js('Newborn'), Js('Nibbler'), Js('Oozer'), Js('Pack Zombie'), Js('Parasite'), Js('Partial Zombie'), Js('Peeler'), Js('Piercer'), Js('Pin Cushion'), Js('Pincher'), Js('Pixy'), Js('Plump Zombie'), Js('Plunger'), Js('Polyp'), Js('Popsicle'), Js('Porcupine'), Js('Pouncer'), Js('Primer'), Js('Private Zombie'), Js('Prober'), Js('Psycho'), Js('Pudgy'), Js('Puker'), Js('Putrid'), Js('Pygmy'), Js('Rabid Zombie'), Js('Radical Zombie'), Js('Radioactive Zombie'), Js('Rager'), Js('Rancer'), Js('Rapid Zombie'), Js('Raver'), Js('Recaller'), Js('Recollecter'), Js('Reeker'), Js('Reliver'), Js('Retainer'), Js('Retched Zombie'), Js('Retcher'), Js('Revoker'), Js('Ripe Zombie'), Js('Roaring'), Js('Rotter'), Js('Rumbler'), Js('Runner'), Js('Rupture Zombie'), Js('Ruptured Zombie'), Js('Rusher'), Js('Savage'), Js('Scourge'), Js('Scrambler'), Js('Scraper'), Js('Scratcher'), Js('Scrawny'), Js('Screaker'), Js('Screamer'), Js('Screecher'), Js('Scuffer'), Js('Scuttler'), Js('Senior'), Js('Shambler'), Js('Shouter'), Js('Shrieker'), Js('Shuffler'), Js('Siren'), Js('Skeletal Zombie'), Js('Skinner'), Js('Skinny Zombie'), Js('Skipper'), Js('Slender Zombie'), Js('Slider'), Js('Slimer'), Js('Slitherer'), Js('Sliver'), Js('Sloucher'), Js('Sludger'), Js('Slumper'), Js('Smacker'), Js('Smart Zombie'), Js('Smasher'), Js('Snacker'), Js('Snapper'), Js('Snarler'), Js('Sneezer'), Js('Sobbing Zombie'), Js('Spasm Zombie'), Js('Spastic'), Js('Spitter'), Js('Spittle Zombie'), Js('Splasher'), Js('Spoiled Zombie'), Js('Sponger'), Js('Spouter'), Js('Sprayer'), Js('Spreader'), Js('Sprouter'), Js('Spumer'), Js('Spurter'), Js('Squaller'), Js('Squealer'), Js('Squirmer'), Js('Stalker'), Js('Stinger'), Js('Stinker'), Js('Stout Zombie'), Js('Stretcher'), Js('Strider'), Js('Stuffer'), Js('Stumbler'), Js('Sucker'), Js('Suckling Zombie'), Js('Superior Zombie'), Js('Surfer'), Js('Swarmer'), Js('Sweller'), Js('Swimmer'), Js('Swinger'), Js('Swollen Zombie'), Js('Tainted Zombie'), Js('Tainter'), Js('Talker'), Js('Tank'), Js('Tantrum Zombie'), Js('Taster'), Js('Tearer'), Js('Temper'), Js('Tender Zombie'), Js('Tester'), Js('Thinker'), Js('Ticker'), Js('Tickler'), Js('Tracker'), Js('Trailer'), Js('Trapper'), Js('Tumbler'), Js('Tumor Zombie'), Js('Twitcher'), Js('Venom Zombie'), Js('Vomiter'), Js('Wacko'), Js('Wailer'), Js('Walker'), Js('Waster'), Js('Weeper'), Js('Whacker'), Js('Whiner'), Js('Whistler'), Js('Wild Zombie'), Js('Withering Zombie'), Js('Wrangler'), Js('Wrestler'), Js('Wriggler'), Js('Writher'), Js('Yelper')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
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
zombieTypes = var.to_python()