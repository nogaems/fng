__all__ = ['killerNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['names1', 'names2', 'nameGen', 'names3'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['result'])
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names1').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names2').get('length'))))
                var.put('names', (((Js('The ')+var.get('names1').get(var.get('rnd')))+Js(' '))+var.get('names2').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('names3').get('length'))))
                var.put('names', (Js('The ')+var.get('names3').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('names1', Js([Js('Acid Bath'), Js('Acid Face'), Js('Alligator'), Js('Angel Eye'), Js('Angel Smile'), Js('Angel Wings'), Js('Anniversary'), Js('Archangel'), Js('Axe'), Js('Baby-Sit'), Js('Babyface'), Js('Back Alley'), Js('Backpack'), Js('Backstab'), Js('Bald'), Js('Bedroom'), Js('Bike Path'), Js('Birthmark'), Js('Bitemark'), Js('Black Forest'), Js('Blackout'), Js('Bleach'), Js('Blind'), Js('Blind Date'), Js('Blood Drop'), Js('Blood Painting'), Js('Blood Spatter'), Js('Blue Moon'), Js('Blunt Force'), Js('Bonbon'), Js('Boulder'), Js('Boulevard'), Js('Breakfast'), Js('Brewery'), Js('Brick'), Js('Bride'), Js('Broomstick'), Js('Brunch'), Js('Business'), Js('Busride'), Js('Campsite'), Js('Candy'), Js('Cannibal'), Js('Canvas'), Js('Casanova'), Js('Challenge'), Js('Chameleon'), Js('Chocolate'), Js('Cinder Block'), Js('Citizen'), Js('Classified'), Js('Claw'), Js('Clean'), Js('Clownface'), Js('Cocktail'), Js('Collection'), Js('Comic'), Js('Commute'), Js('Concrete'), Js('Confidential'), Js('Construction Site'), Js('Copy Cat'), Js('Corridor'), Js('Cosmetic'), Js('Cropfield'), Js('Cross-Country'), Js('Customer'), Js('Cyber'), Js('Dawn'), Js('Daybreak'), Js('Demon'), Js('Demon Eyes'), Js('Dessert'), Js('Dinner'), Js('Discount'), Js('Disguised'), Js('Dollhouse'), Js('Door To Door'), Js('Doorbell'), Js('Downtown'), Js('Drama'), Js('Dumpster'), Js('Dusk'), Js('Education'), Js('Effigy'), Js('Emergency'), Js('Evening'), Js('Evil Eye'), Js('Exorcism'), Js('Eyeless'), Js('Fast Food'), Js('Festival'), Js('Fetish'), Js('Figurine'), Js('Final Station'), Js('First Aid'), Js('Freeway'), Js('Full Moon'), Js('Ghost'), Js('Giggling'), Js('Grainfield'), Js('Groomsman'), Js('Guest'), Js('Guest Room'), Js('Habit'), Js('Hair Band'), Js('Hairless'), Js('Half-Moon'), Js('Hallway'), Js('Hammock'), Js('Handcuff'), Js('Happy Face'), Js('Harborview'), Js('Harlequin'), Js('Hatchet'), Js('Highscore'), Js('Highway'), Js('Hillside'), Js('Hitchhiker'), Js('Holiday'), Js('Homesick'), Js('Hook'), Js('Hospital'), Js('Hostel'), Js('Hotel'), Js('Identical'), Js('Incognito'), Js('Institution'), Js('Jolly'), Js('Knock Knock'), Js('Knockout'), Js('Lipstick'), Js('Lobby'), Js('Lonely'), Js('Lonely Heart'), Js('Luck'), Js('Lunch'), Js('Machete'), Js('Mad Dog'), Js('Makeup'), Js('Manacle'), Js('Marionette'), Js('Masked'), Js('Melonball'), Js('Midnight'), Js('Midtown'), Js('Mirror'), Js('Monday'), Js('Morning'), Js('Motel'), Js('Mountain'), Js('Naked'), Js('Network'), Js('Newlywed'), Js('Night Stalker'), Js('Nightfall'), Js('Nylon'), Js('Obsession'), Js('Odd Job'), Js('Online'), Js('Painting'), Js('Pancake'), Js('Parallel'), Js('Pastry'), Js('Pathway'), Js('Phantom'), Js('Phoenix'), Js('Phonecall'), Js('Phony'), Js('Pixy'), Js('Plain'), Js('Portrait'), Js('Pretend'), Js('Protocol'), Js('Pub'), Js('Pubcrawl'), Js('Pudding'), Js('Pygmy'), Js('Rabid'), Js('Ragdoll'), Js('Recycle'), Js('Red Petal'), Js('Resident'), Js('Ritual'), Js('Routine'), Js('Royal'), Js('Rubberneck'), Js('Sad Face'), Js('Sailing'), Js('Sandwich'), Js('Sanguine'), Js('Scarlet'), Js('Scholarship'), Js('Scissors'), Js('Score Keeper'), Js('Scrapyard'), Js('Seashore'), Js('Serpent'), Js('Servant'), Js('Shackle'), Js('Shoebox'), Js('Shopping Bag'), Js('Shotgun'), Js('Sickle'), Js('Silk'), Js('Sleeping'), Js('Spider'), Js('Spotless'), Js('Stocking'), Js('Strawberry'), Js('Streetlight'), Js('Stripping'), Js('Sunday'), Js('Sundown'), Js('Sunrise'), Js('Sunset'), Js('Symmetric'), Js('Talon'), Js('Tavern'), Js('Tomahawk'), Js('Toothless'), Js('Torment'), Js('Torso'), Js('Tortoise'), Js('Torture'), Js('Tourist'), Js('Toybox'), Js('Trailer Park'), Js('Trailside'), Js('Trainride'), Js('Trash Bag'), Js('Trash Can'), Js('Twilight'), Js('Twin'), Js('Two Coin'), Js('Undercover'), Js('Vampire'), Js('Visitor'), Js('Voodoo'), Js('Wanted-Ad'), Js('Wayfare'), Js('Weekend'), Js('Werewolf'), Js('White Rose'), Js('Widow'), Js('Witchcraft'), Js('Woodwork'), Js('World Record'), Js('Zoo')]))
var.put('names2', Js([Js('Murderer'), Js('Killer'), Js('Butcher'), Js('Slayer')]))
var.put('names3', Js([Js('Alien'), Js('Alligator'), Js('Seductress'), Js('Angel of Death'), Js('Angelmaker'), Js('Babyface'), Js('Baker'), Js('Bandit'), Js('Barbarian'), Js('Barber'), Js('Basher'), Js('Beast'), Js('Behemoth'), Js('Bigot'), Js('Biter'), Js('Bloodhound'), Js('Bomber'), Js('Bonekeeper'), Js('Brute'), Js('Butcher'), Js('Butler'), Js('Buzzard'), Js('Cannibal'), Js('Casanova'), Js('Chef'), Js('Chopper'), Js('Claw'), Js('Cleaver'), Js('Clobber'), Js('Clown'), Js('Cook'), Js('Copy Cat'), Js('Creature'), Js('Degenerate'), Js('Delirious'), Js('Demon'), Js('Dentist'), Js('Dicer'), Js('Disfigured'), Js('Doctor'), Js('Dog'), Js('Dummy'), Js('Executioner'), Js('Fang'), Js('Fiend'), Js('Fist'), Js('Frankenstein'), Js('Freak'), Js('Gambler'), Js('Ghost'), Js('Ghoul'), Js('Glutton'), Js('Grappler'), Js('Grave Robber'), Js('Hacker'), Js('Hook'), Js('Hunter'), Js('Informant'), Js('Insane'), Js('Jester'), Js('Kidnapper'), Js('Lunatic'), Js('Mad Dog'), Js('Man Eater'), Js('Maniac'), Js('Medic'), Js('Mime'), Js('Mincer'), Js('Model'), Js('Monster'), Js('Mutant'), Js('Night Stalker'), Js('Nurse'), Js('Nutcase'), Js('Outsider'), Js('Pale'), Js('Phantom'), Js('Pied Piper'), Js('Poisoner'), Js('Primitive'), Js('Professor'), Js('Psycho'), Js('Reaper'), Js('Ripper'), Js('Savage'), Js('Scalpel'), Js('Scar'), Js('Scientist'), Js('Scissors'), Js('Scythe'), Js('Senior'), Js('Serpent'), Js('Servant'), Js('Shadow'), Js('Shaver'), Js('Skeleton'), Js('Skinner'), Js('Skull'), Js('Slasher'), Js('Slayer'), Js('Slice and Dicer'), Js('Slicer'), Js('Snatcher'), Js('Sniper'), Js('Snitch'), Js('Spectator'), Js('Spider'), Js('Stalker'), Js('Stranger'), Js('Strangler'), Js('Stripper'), Js('Surgeon'), Js('Terminator'), Js('Therapist'), Js('Tourist'), Js('Tracker'), Js('Trapper'), Js('Vampire'), Js('Vermin'), Js('Watcher'), Js('Weasel'), Js('Weirdo'), Js('Werewolf'), Js('Whale'), Js('Whip'), Js('Whisper'), Js('Widow Maker'), Js('Wolf'), Js('Zombie')]))
pass
pass


# Add lib to the module scope
killerNames = var.to_python()