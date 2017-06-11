__all__ = ['boarsBears']

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
var.put('nm1', Js([Js('BearlockHolmes'), Js('Aloysius'), Js('Ancient'), Js('Arcadia'), Js('Arcadius'), Js('Ardal'), Js('Arkadios'), Js('Arkadios'), Js('Arktophonos'), Js('Armel'), Js('Art'), Js('Artair'), Js('Artan'), Js('Arthfael'), Js('Arthmael'), Js('Arthur'), Js('Artie'), Js('Arto'), Js('Artorius'), Js('Arttu'), Js('Artturi'), Js('Artur'), Js('Arturas'), Js('Arturo'), Js('Asbjorn'), Js('Auberon'), Js('Avonaco'), Js('Bagelmelt'), Js('Bare'), Js('Barney'), Js('Barvam'), Js('Bearbeque'), Js('Bearenstein'), Js('Bearnard'), Js('Bentclaw'), Js('Beorn'), Js('Beornheard'), Js('Ber'), Js('Berdine'), Js('Berend'), Js('Berengar'), Js('Berengari'), Js('Berengaria'), Js('Berengarius'), Js('Berenger'), Js('Berenguer'), Js('Beringar'), Js('Beringarius'), Js('Bern'), Js('Bernadett'), Js('Bernadette'), Js('Bernadine'), Js('Bernard'), Js('Bernarde'), Js('Bernardetta'), Js('Bernardette'), Js('Bernardine'), Js('Bernardino'), Js('Bernardita'), Js('Bernardo'), Js('Bernardus'), Js('Bernat'), Js('Bernd'), Js('Berndt'), Js('Bernhard'), Js('Bernhardt'), Js('Bernie'), Js('Bernt'), Js('BigPete'), Js('Biorna'), Js('Bjarne'), Js('Bjarni'), Js('Bjorn'), Js('Blackfell'), Js('Blackjack'), Js('Bloodmaw'), Js('Bloodymuzzle'), Js('Booboo'), Js('Boris'), Js('Briarsting'), Js('Brokenfang'), Js('Burney'), Js('Cannibear'), Js('Care'), Js('Carebear'), Js('Cassanova'), Js('ChicagoCubs'), Js('Chomper'), Js('Clicktooth'), Js('CocaCola'), Js('Cupcake'), Js('Deathclaw'), Js('Deathmaw'), Js('Dov'), Js('Esben'), Js('Espen'), Js('Flopper'), Js('ForestFires'), Js('Fred'), Js('Frigidaire'), Js('Frostpaw'), Js('FrostyPaws'), Js('FuzzyWuzzy'), Js('Gerben'), Js('Gnawbone'), Js('GrinAnd'), Js('Grumpy'), Js('Gullet'), Js('Hallbjorn'), Js('Hambeargler'), Js('Helpimadruid'), Js('Honeyfarmer'), Js('Hookpaw'), Js('Huslu'), Js('Hybernator'), Js('Icy'), Js('Kiasax'), Js('Kuma'), Js('Largepaw'), Js('Lashpaw'), Js('Lockjaw'), Js('Longfang'), Js('Mahon'), Js('Makwa'), Js('Manitou'), Js('Marshmallow'), Js('Mathuin'), Js('Mato'), Js('Misha'), Js('Nanook'), Js('Nanuk'), Js('Nanuq'), Js('Napowsa'), Js('Necessities'), Js('Nightrunner'), Js('Nita'), Js('Oberon'), Js('Oink'), Js('Oinker'), Js('Oinkinstien'), Js('Orbiorn'), Js('Orbjorn'), Js('Orsen'), Js('Orsin'), Js('Orsina'), Js('Orsino'), Js('Orso'), Js('Orsola'), Js('Orsolya'), Js('Orson'), Js('Osbeorn'), Js('Osborn'), Js('Osbourne'), Js('Otso'), Js('Pandaman'), Js('Panzer'), Js('Patapych'), Js('Petdruid'), Js('Pink'), Js('Plague'), Js('Polaar'), Js('Pooh'), Js('PoohBear'), Js('PowderKeg'), Js('Preben'), Js('Predbjorn'), Js('Pridbjorn'), Js('Quickfang'), Js('Raeb'), Js('Rainbow'), Js('Render'), Js('Ripmaw'), Js('Ripper'), Js('Riven'), Js('Rumblebelly'), Js('Sharptooth'), Js('Sherman'), Js('Smokey'), Js('Snowball'), Js('Snowbrawl'), Js('Spoink'), Js('Squee'), Js('Stanis'), Js('Starjumper'), Js('Stonepaw'), Js('Taiomah'), Js('Tarben'), Js('Tarlo'), Js('Teddiursa'), Js('Thorben'), Js('Thorbern'), Js('Thorbernus'), Js('Thorbjorn'), Js('Thorburn'), Js('Titus'), Js('Torben'), Js('Torbern'), Js('Torbernus'), Js('Torbjorn'), Js('Trotsky'), Js('Trotter'), Js('Unbearable'), Js('Urs'), Js('Ursa'), Js('Ursala'), Js('Ursaring'), Js('Ursel'), Js('Ursella'), Js('Ursina'), Js('Ursine'), Js('Ursinus'), Js('Urska'), Js('Ursula'), Js('Ursule'), Js('Ursus'), Js('Urszula'), Js('Uschi'), Js('Uther'), Js('Uzumati'), Js('Warfrost'), Js('Winnie'), Js('Wojtek'), Js('Yogi'), Js('Zhukov'), Js('Ziggy')]))
var.put('nm2', Js([Js('Al'), Js('Amber'), Js('Angrybacon'), Js('Arnold'), Js('Aylott'), Js('Babe'), Js('BackBacon'), Js('Bacobit'), Js('Bacon'), Js('Bacon'), Js('BaconButty'), Js('Baconbits'), Js('Baeddan'), Js('Bailey'), Js('Bebop'), Js('Beebee'), Js('Behemoth'), Js('Bentley'), Js('Betty'), Js('BigMumma'), Js('BillieJo'), Js('Binney'), Js('Blitzkrieg'), Js('Boarhead'), Js('Boartle'), Js('Bore'), Js('Breakfast'), Js('Brian'), Js('Bristle'), Js('Brokentusk'), Js('Chili'), Js('Chitlins'), Js('Chops'), Js('Clarice'), Js('Cledus'), Js('Culhwch'), Js('DaisyMae'), Js('Death'), Js('Deathgore'), Js('Deliverance'), Js('Dinner'), Js('Eoforhild'), Js('Evert'), Js('Fatback'), Js('Freighttrain'), Js('Goretusk'), Js('GoyelyPig'), Js('Granny'), Js('Groucho'), Js('Gullinborsti'), Js('Halitosis'), Js('Hamilton'), Js('Hamlet'), Js('Hamlet'), Js('Hammy'), Js('Hannah'), Js('HermioneHamhock'), Js('Hildesvini'), Js('Hobeu'), Js('Hogzilla'), Js('Ironhide'), Js('James'), Js('Jessie'), Js('JimmyDean'), Js('Kermitsgirl'), Js('KevinBacon'), Js('Kombat'), Js('Kosher'), Js('Links'), Js('MagnumPIG'), Js('Major'), Js('Mamoswine'), Js('Meatrocket'), Js('Meatwagon'), Js('Mel'), Js('Melvin'), Js('Milinko'), Js('MissPiggy'), Js('Morgan'), Js('Napoleon'), Js('Nestor'), Js('Obelisk'), Js('Oinkers'), Js('OlBristley'), Js('Olive'), Js('Onyx'), Js('Oreo'), Js('Orson'), Js('Pabio'), Js('Pace'), Js('Panzer'), Js('Patty'), Js('Pearls'), Js('Penelope'), Js('Petunia'), Js('PigglesworthSnortimer'), Js('Piggy'), Js('PiggySue'), Js('PiggyBank'), Js('Piloswine'), Js('Pink'), Js('Pinky'), Js('Pippin'), Js('PoPo'), Js('Pookie'), Js('Popeye'), Js('Poppy'), Js('Porco'), Js('Porkchop'), Js('Porkchop'), Js('Porkchops'), Js('Porker'), Js('Porkmeister'), Js('Porko'), Js('Porky'), Js('Potbelly'), Js('Princess'), Js('PrincessFiona'), Js('Pumba'), Js('Pumbaa'), Js('Ram-bore'), Js('Rammswine'), Js('Razorback'), Js('Ribs'), Js('Ringo'), Js('Rosco'), Js('Rosie'), Js('RumpledPigskin'), Js('RunningBacon'), Js('Sam'), Js('Sammy'), Js('Sausage'), Js('Scarlet'), Js('SergeantPork'), Js('SgtPork'), Js('Skane'), Js('Skeith'), Js('Slim'), Js('SmellMyCrit'), Js('SmokedPork'), Js('Smokey'), Js('Snore'), Js('Snouts'), Js('Snowball'), Js('Soooeee'), Js('SpamelaAnderson'), Js('Sparerib'), Js('Spiderpig'), Js('Squishy'), Js('Sweathog'), Js('Sweetie'), Js('Swinub'), Js('TammySwinette'), Js('Tenderloin'), Js('Toby'), Js('Triath'), Js('Tristan'), Js('Truffles'), Js('Tubby'), Js('Tui'), Js('Twrch'), Js('VanCleef'), Js('WTFBBQ'), Js('Warpig'), Js('WhiteMeat'), Js('Wilbur'), Js('Ziggy')]))
pass
pass


# Add lib to the module scope
boarsBears = var.to_python()