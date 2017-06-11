__all__ = ['libraryNames']

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
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('ABC'), Js('Aeos'), Js('Algorithm'), Js('Amenity'), Js("Angel's"), Js('Anomaly'), Js('Apex'), Js('Aptitude'), Js('Art Archive'), Js('Avant-garde'), Js('Beauview'), Js('Blossoms'), Js('Book Mark'), Js('Booked'), Js('Bookworm'), Js('Calligraph'), Js('Capitol'), Js('Carpe Librum'), Js('Celestial'), Js('Central Park'), Js('Chapter'), Js('Chapter One'), Js('Charity'), Js('Chimera'), Js('Codex'), Js('Compendium'), Js('Cosmic'), Js('Courtesy'), Js('Crescent Moon'), Js('Crest'), Js('Crossroad'), Js('Crown'), Js('Curio'), Js('Curiosity'), Js('Data'), Js('Daydream'), Js('Desire'), Js('Discovery'), Js('Divine'), Js('Epiphany'), Js('Epitome'), Js('Equinox'), Js('Estate'), Js('Eternal'), Js('Evening Hour'), Js('Explorer'), Js('Figment'), Js('First Story'), Js('Forte'), Js('Freedom'), Js('Frontier'), Js("Gift's"), Js('Global'), Js('Globe'), Js('Grand'), Js('Grand Archive'), Js('Grand Duchess'), Js('Grand Isle'), Js('Grand Monastery'), Js('Grand Oak'), Js('Grand State'), Js('Grotto'), Js("Guardian's"), Js('Harborview'), Js('Harmony'), Js('Heirloom'), Js('Heritage'), Js('Holy'), Js('Idle Hour'), Js('Illusions'), Js('Imagine'), Js('Imperial'), Js('Infinity'), Js('Innovation'), Js('Inquiry'), Js('Insight'), Js('Institute'), Js('Jubilee'), Js("King's"), Js('Knight'), Js('Knowledge'), Js('Labyrinth'), Js('Legacy'), Js('Leisure'), Js('Lexicon'), Js('Liberty'), Js('Lullaby'), Js('Marvel'), Js('Memorial'), Js('Millennium'), Js('Miracle'), Js('Mirage'), Js('Mystery'), Js('National History'), Js('National Memorial'), Js('National Public'), Js('National University'), Js('Novel Idea'), Js('Obelisk'), Js('Oceanic'), Js('Open Book'), Js('Opus'), Js('Oracle'), Js('Page One'), Js('Paragon'), Js('Patrimony'), Js('Pinnacle'), Js('Pioneer'), Js('Plainfield'), Js('Prime'), Js('Prism'), Js('Probe'), Js('Prodigy'), Js('Public Scientific'), Js('Pursuit'), Js('Quest'), Js('Quietus'), Js('Rainbow'), Js("Reader's Garden"), Js('Repose'), Js('Requiem'), Js('Reticence'), Js('Revelation'), Js('Reverie'), Js('Rising Sun'), Js('Royal'), Js('Saturninity'), Js('Savant'), Js("Scholar's"), Js('Serenity'), Js('Solace'), Js('Solitude'), Js('Spectrum'), Js('Spring Harbor'), Js('Stellar'), Js('Summit'), Js('Supreme'), Js('Tempest'), Js('Temple'), Js('Titlewave'), Js('Tranquility'), Js('Treatise'), Js('Trove'), Js('Utopia'), Js('Vade Mecum'), Js('Valley'), Js('Virtue'), Js('Vision'), Js('Wonder'), Js('Zenith')]))
var.put('nm2', Js([Js('Library'), Js('Bilbiotheca'), Js('Library'), Js('Library'), Js('Library'), Js('Library'), Js('Library'), Js('Library'), Js('Library'), Js('Library'), Js('Library'), Js('Atheneum')]))
pass
pass


# Add lib to the module scope
libraryNames = var.to_python()