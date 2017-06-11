__all__ = ['animalPackNames']

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
    var.put('nm1', Js([Js('Aerie'), Js('Amalgamation'), Js('Army'), Js('Arrangement'), Js('Array'), Js('Ascension'), Js('Association'), Js('Audience'), Js('Babbling'), Js('Band'), Js('Barrage'), Js('Bask'), Js('Batch'), Js('Battalion'), Js('Battery'), Js('Bazaar'), Js('Bevy'), Js('Bilge'), Js('Blathering'), Js('Bloat'), Js('Body'), Js('Brigade'), Js('Brood'), Js('Bunch'), Js('Bundle'), Js('Burrow'), Js('Business'), Js('Calling'), Js('Caravan'), Js('Cast'), Js('Chain'), Js('Chattering'), Js('Clan'), Js('Clearing'), Js('Clique'), Js('Clot'), Js('Cloud'), Js('Clowder'), Js('Club'), Js('Clump'), Js('Cluster'), Js('Clutch'), Js('Coalition'), Js('Collection'), Js('Colony'), Js('Column'), Js('Community'), Js('Company'), Js('Conclave'), Js('Concourse'), Js('Confab'), Js('Conflux'), Js('Congerie'), Js('Conjuring'), Js('Congregation'), Js('Congress'), Js('Conspiracy'), Js('Corps'), Js('Coterie'), Js('Coupling'), Js('Covey'), Js('Creche'), Js('Crowd'), Js('Crush'), Js('Deluge'), Js('Den'), Js('Deposit'), Js('Descent'), Js('Design'), Js('Detail'), Js('Display'), Js('Dominion'), Js('Draft'), Js('Drift'), Js('Drove'), Js('Enterprise'), Js('Exaltation'), Js('Exhibition'), Js('Faction'), Js('Fair'), Js('Fall'), Js('Family'), Js('Flight'), Js('Flock'), Js('Flood'), Js('Following'), Js('Force'), Js('Form'), Js('Formation'), Js('Fusion'), Js('Gaggle'), Js('Game'), Js('Gang'), Js('Gathering'), Js('Generation'), Js('Gibbering'), Js('Gloom'), Js('Grapple'), Js('Grasp'), Js('Haunt'), Js('Haze'), Js('Heap'), Js('Herd'), Js('Hive'), Js('Horde'), Js('Host'), Js('House'), Js('Hurtle'), Js('Jam'), Js('Kindle'), Js('Knot'), Js('Laze'), Js('Lead'), Js('League'), Js('Legion'), Js('Line'), Js('Lineup'), Js('Litter'), Js('Loll'), Js('Lot'), Js('Lounge'), Js('Mass'), Js('Meet'), Js('Meeting'), Js('Melding'), Js('Menage'), Js('Menagerie'), Js('Merger'), Js('Merging'), Js('Mob'), Js('Monopoly'), Js('Movement'), Js('Muffle'), Js('Multitude'), Js('Murder'), Js('Muster'), Js('Nebula'), Js('Nest'), Js('Network'), Js('Nursery'), Js('Order'), Js('Outfit'), Js('Pack'), Js('Pandemonium'), Js('Parade'), Js('Parish'), Js('Party'), Js('Pedigree'), Js('Plunge'), Js('Posse'), Js('Prattling'), Js('Press'), Js('Pride'), Js('Progeny'), Js('Pursuit'), Js('Quash'), Js('Rabble'), Js('Raft'), Js('Regiment'), Js('Relish'), Js('Ring'), Js('Rise'), Js('Rookery'), Js('Run'), Js('Sanctuary'), Js('School'), Js('Scion'), Js('Score'), Js('Scourge'), Js('Screech'), Js('Siege'), Js('Sequence'), Js('Set'), Js('Shoal'), Js('Shock'), Js('Show'), Js('Shower'), Js('Shroud'), Js('Sleuth'), Js('Slide'), Js('Smothering'), Js('Soar'), Js('Society'), Js('Squad'), Js('Squelch'), Js('Storm'), Js('Suite'), Js('Swarm'), Js('Swoop'), Js('Syndicate'), Js('System'), Js('Team'), Js('Throng'), Js('Tribe'), Js('Trip'), Js('Troop'), Js('Troubling'), Js('Troupe'), Js('Tumble'), Js('Tumult'), Js('Turnout'), Js('Twaddling'), Js('Twiddling'), Js('Union'), Js('Unit'), Js('Venture'), Js('Venue'), Js('Volley'), Js('Waddle'), Js('Wake'), Js('Walk'), Js('Wallow'), Js('Wedge'), Js('Welter'), Js('Wing'), Js('Wreck')]))
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
animalPackNames = var.to_python()