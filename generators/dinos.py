__all__ = ['dinos']

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
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', var.get('nm2').get(var.get('rnd')))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', var.get('nm1').get(var.get('rnd')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('HueJass'), Js('Albinosaur'), Js('Angar'), Js('Auron'), Js('Bahir'), Js('Barakah'), Js('Barney'), Js('Bellow'), Js('Bigfoot'), Js('Bitsy'), Js('Bloodmaw'), Js('Bloodymuzzle'), Js('Bobosaur'), Js('Brand'), Js('BrokeFang'), Js('Brokenfang'), Js('Buck'), Js('Byte'), Js('Chaos'), Js('ChompStomp'), Js('Chomper'), Js('Chopper'), Js('Claws'), Js('Clawz'), Js('CleverGirl'), Js('Crush'), Js('Crusher'), Js('Cuddles'), Js('Daffy'), Js('Dan'), Js('Daniel'), Js('Danny'), Js('Darla'), Js('Dash'), Js('Deathmaw'), Js('Delilah'), Js('Dentist'), Js('Denver'), Js('Destructor'), Js('Devastator'), Js('Deviant'), Js('Deviltry'), Js('DharanSar'), Js('Didi'), Js('Digger'), Js('Dingo'), Js('Dino'), Js('Don'), Js('Donald'), Js('Donna'), Js('Donny'), Js('Doodles'), Js('Drake'), Js('Dreadtooth'), Js('Dred'), Js('Ebony'), Js('Emerald'), Js('Extinct'), Js('Extinction'), Js('Fang'), Js('Fayng'), Js('Fearme'), Js('Fearsome'), Js('Fetch'), Js('Fido'), Js('Flaay'), Js('Fluffy'), Js('Fossil'), Js('FossilFuel'), Js('Fuel'), Js('Fuzzmuffin'), Js('Gambit'), Js('Geico'), Js('Godzilla'), Js('Gorosaurus'), Js('Greenback'), Js('Gregarious'), Js('Grimlock'), Js('Grimnir'), Js('Gullet'), Js('Halmar'), Js('Hammerit'), Js('Hannibal'), Js('Helm'), Js('Hjollder'), Js('IBite'), Js('IDK'), Js('Ibite'), Js('IronHide'), Js('Ivory'), Js('JPEscapee'), Js('Jaws'), Js('Jill'), Js('Junior'), Js('Jurassic'), Js('JurasskickMark'), Js('KingTerror'), Js('Krush'), Js('Kuvar'), Js('Kyouryuu'), Js('Largepaw'), Js('Lilarms'), Js('Limey'), Js('Littlearms'), Js('Littlefoot'), Js('Lizard'), Js('Lizzy'), Js('Lockjaw'), Js('Lohtur'), Js('Lollipop'), Js('LongTooth'), Js('Longfang'), Js('Lumos'), Js('Maugrim'), Js('Midnight'), Js('Mittens'), Js('MrBiteyPantz'), Js('Nightmare'), Js('NomNomNom'), Js('NotATRex'), Js('OMNOMNOM'), Js('Obsidian'), Js('Oscar'), Js('Overbite'), Js('Paleosaurus'), Js('Peanut'), Js('Phearsome'), Js('Philosoraptor'), Js('Pickles'), Js('Protego'), Js('Pumpkin'), Js('Punkin'), Js('Quickfang'), Js('Rahon'), Js('Rampardos'), Js('RapTrap'), Js('RaptorXXL'), Js('Raw'), Js('Ray'), Js('Razor'), Js('Razzak'), Js('Relish'), Js('Render'), Js('Rex'), Js('Rexette'), Js('Rexxy'), Js('Rhedosaurus'), Js('Riff'), Js('Rikko'), Js('Rip'), Js('Ripmaw'), Js('Ripper'), Js('Roflsaurs'), Js('Ryp'), Js('Sammy'), Js('Sargon'), Js('Sauros'), Js('Scales'), Js('Scaly'), Js('Scyther'), Js('SexyRexy'), Js('Shaaux'), Js('Sharpclaw'), Js('Sharptooth'), Js('Shifty'), Js('SirSlicey'), Js('SliceNDice'), Js('Sly'), Js('Smiley'), Js('Smileysaur'), Js('Smurf'), Js('Snapp'), Js('Sneaker'), Js('Speilberg'), Js('Spike'), Js('Spyke'), Js('Squint'), Js('Stevosaur'), Js('Stomp'), Js('StompStomp'), Js('Stompy'), Js('Sunshine'), Js('Swiftscale'), Js('TWrecks'), Js('Ter'), Js('Thanatos'), Js('Thunderlizard'), Js('TinyTim'), Js('Titan'), Js('Titanosaurus'), Js('Tooth'), Js('Toothy'), Js('Trex'), Js('Twinkletoes'), Js('Tyr'), Js('Tyra'), Js('Tyran'), Js('Tyranitar'), Js('Tyranno'), Js('Tyrannos'), Js('Tyro'), Js('Ulfang'), Js('Velocity'), Js('Viridian'), Js('Wafflemeow'), Js('Wily'), Js('Xero'), Js('Xerxes'), Js('YellowTooth'), Js('Zahra'), Js('Zahrax'), Js('Zarin'), Js('Zinrokh'), Js('Zulzin'), Js('myBFF')]))
var.put('nm2', Js([Js('HueJass'), Js('Bakari'), Js('BigBoss'), Js('Boomer'), Js('BowlingBall'), Js('Brutus'), Js('Buba'), Js('Bubbles'), Js('Buhrahrum'), Js('Bulldozer'), Js('Bummer'), Js('Charge'), Js('Charger'), Js('Dakari'), Js('Dodge'), Js('Dunia'), Js('Duniya'), Js('Eddie'), Js('Faustosilva'), Js('Fizzawick'), Js('Gelom'), Js('GnomeSlinger\t\t'), Js('Gnomepunter'), Js('Grace'), Js('Hasani'), Js('Hummer'), Js('Humperdink'), Js('Jimbi'), Js('Johari'), Js('Juba'), Js('Jump'), Js('Kibibbi'), Js('Kirushou'), Js('Kito'), Js('Kneel'), Js('LittleOne'), Js('Lokthar'), Js('Maret'), Js('MrLittle'), Js('Muchi'), Js('Njord'), Js('Noosie'), Js('Nyika'), Js('Rae'), Js('Rafael'), Js('Rafiki'), Js('Ralph'), Js('Ralphie'), Js('Randey'), Js('Rando'), Js('Random'), Js('Randy'), Js('Ray'), Js('Raymond'), Js('Raz'), Js('Redd'), Js('Respighi'), Js('Retro'), Js('Rex'), Js('Rhina'), Js('Rhinester'), Js('Rhino911'), Js('Rhinoldinho'), Js('Rhinoplasty'), Js('Riddick'), Js('RiffRaff'), Js('Rigby'), Js('Riley'), Js('Ringo'), Js('Rizzo'), Js('Roadblock'), Js('Robbie'), Js('Robby'), Js('Rodeo'), Js('Rodger'), Js('Rodney'), Js('Rolo'), Js('Roma'), Js('Romeo'), Js('Romey'), Js('Ron'), Js('Ronan'), Js('Rondo'), Js('Ronin'), Js('Rorschach'), Js('Rory'), Js('Rosco'), Js('Roscoe'), Js('Rosita'), Js('Ross'), Js('Roswell'), Js('Roudy'), Js('Rua'), Js('Ruban'), Js('Rubit'), Js('Ruby'), Js('Ruckus'), Js('Rudolph'), Js('Rudy'), Js('Ruffie'), Js('Ruffus'), Js('Ruffy'), Js('Rufus'), Js('Ruger'), Js('Rugrat'), Js('Runt'), Js('Rupert'), Js('Rupurt'), Js('Rusalka'), Js('Russell'), Js('Rusti'), Js('Rusty'), Js('Ryan'), Js('Ryder'), Js('Ryelle'), Js('Rythum'), Js('Sama'), Js('Samahe'), Js('Spearmeant'), Js('Stomper'), Js('Stompy'), Js('Thunderstomp'), Js('TickBird'), Js('Tiirkar'), Js('Tiny'), Js('TinyTim'), Js('Tubby'), Js('Ugmak'), Js('Vlad'), Js('Wagtail'), Js('Wooly'), Js('Zuvan')]))
pass
pass


# Add lib to the module scope
dinos = var.to_python()