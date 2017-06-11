__all__ = ['arcadeNames']

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
    var.registers(['nm1', 'nm2', 'nm3', 'result'])
    var.put('nm1', Js([Js('Achievement'), Js('Adventure'), Js('Alien'), Js('Amazing'), Js('Animal'), Js('Animaniac'), Js('Animatron'), Js('Animatronic'), Js('Arc'), Js('Astral'), Js('Awesome'), Js('Banter'), Js('Battle'), Js('Blissful'), Js('Blown Mind'), Js('Bountiful'), Js('Brave'), Js('Brilliant'), Js('Carefree'), Js('Carnival'), Js('Celebration'), Js('Change'), Js('Cheat Code'), Js('Classic'), Js('Cloud'), Js('Cloud Nine'), Js('Co-op'), Js('Connection'), Js('Creature'), Js('Critical'), Js('Critical Hit'), Js('Crown'), Js('Curtain'), Js('Dapper'), Js('Dark'), Js('Defiance'), Js('Defiant'), Js('Digital'), Js('Discovery'), Js('Dragon'), Js('Enchanted'), Js('Exalted'), Js('Exchange'), Js('Experience'), Js('Expert'), Js('Fantastic'), Js('Fantasy'), Js('Feast'), Js('Festival'), Js('Fiesta'), Js('Focus'), Js('Focused'), Js('Game'), Js('Game On'), Js('Gleeful'), Js('Glorious'), Js('Glory'), Js('Grand'), Js('Great'), Js('Highscore'), Js('Holiday'), Js('Humble'), Js('Illusion'), Js('Imagination'), Js('Impulse'), Js('Infinite'), Js('Infinity'), Js('Jamboree'), Js('Jewel'), Js('Jubilant'), Js('Jubilee'), Js('Jumbo'), Js('Juvenile'), Js('Level'), Js('Level Up'), Js('Little'), Js('Lost'), Js('Lucky'), Js('Magic'), Js('Mana'), Js('Mellow'), Js('Merry'), Js('Mind'), Js('Miracle'), Js('Mystery'), Js('Mythic'), Js('Natural Twenty'), Js('Nightowl'), Js('Nostalgia'), Js('Oddball'), Js('One Up'), Js('Original'), Js('Outcast'), Js('Parallel'), Js('Phantom'), Js('Phoenix'), Js('Playful'), Js('Playground'), Js('Plus One'), Js('Prestige'), Js('Prime'), Js('Pristine'), Js('Quaint'), Js('Radiant'), Js('Reality'), Js('Record'), Js('Revelation'), Js('Rhythm'), Js('Riddle'), Js('Secret'), Js('Sensation'), Js('Sidewalk'), Js('Small Change'), Js('Space'), Js('Space Station'), Js('Spirit'), Js('Summer'), Js('Surprise'), Js('Throne'), Js('Treasure'), Js('Treasure Trove'), Js('Trophy'), Js('VR'), Js('Velvet'), Js('Victorious'), Js('Victory'), Js('Virtual'), Js('Vision'), Js('Voyage'), Js('Whimsical'), Js('Wicked'), Js('Wild'), Js('Wilder'), Js('Winter'), Js('Wonder'), Js('XP')]))
    var.put('nm2', Js([Js('Amuscore'), Js('Amusecade'), Js('Amusehall'), Js('Amusemania'), Js('Amusepolis'), Js('Avatarcade'), Js('Barcade'), Js('Barscore'), Js('Bazarcade'), Js('Bizarcade'), Js('Bliss Palace'), Js('Blisscore'), Js('Blisshall'), Js('Blissmania'), Js('Blisspalace'), Js('Blissplace'), Js('Blissplay'), Js('Blisspolis'), Js('Blisspot'), Js("Bull's Eyescore"), Js('Caesarcade'), Js('Capercade'), Js('Capolis'), Js('Cheerpolis'), Js('Cheerscore'), Js('Coinpalace'), Js('Coinscore'), Js('Coinstop'), Js('Comicade'), Js('Comiscore'), Js('Cougarcade'), Js('Embarcade'), Js('Excelsiscore'), Js('Exemplay'), Js('Felicicade'), Js('Felicipolis'), Js('Feliscore'), Js('Festicade'), Js('Festihall'), Js('Festiscore'), Js('Festocade'), Js('Festomania'), Js('Festopolis'), Js('Flyscore'), Js('Foolcade'), Js('Foolplay'), Js('Foolscore'), Js('Fubarcade'), Js('Funcade'), Js('Funcore'), Js('Funmania'), Js('Funpolis'), Js('Funscore'), Js('Funspot'), Js('Gamecade'), Js('Gamecore'), Js('Gamehall'), Js('Gamemania'), Js('Gameplace'), Js('Gamepolis'), Js('Gamescore'), Js('Gamespot'), Js('Gearmania'), Js('Gearplay'), Js('Gearscore'), Js('Gemcade'), Js('Gemplay'), Js('Guitarcade'), Js('Guyscore'), Js('Happicade'), Js('Happiscore'), Js('Happlay'), Js('Happycade'), Js('Happyscore'), Js('Jarcade'), Js('Jokecade'), Js('Jokepolis'), Js('Jokescore'), Js('Joycade'), Js('Joyhall'), Js('Joypalace'), Js('Joyplace'), Js('Joypolis'), Js('Joyscore'), Js('Jubicade'), Js('Jubihall'), Js('Jubilamania'), Js('Jubileecade'), Js('Jubileemania'), Js('Jubilopolis'), Js('Jubiscore'), Js('Kawaiiscore'), Js('Lunarcade'), Js('Merricade'), Js('Merripalace'), Js('Merriplace'), Js('Merriscore'), Js('Nostalcade'), Js('Nostalgicade'), Js('Ocularcade'), Js('Piescore'), Js('Pillarcade'), Js('Quarterpalace'), Js('Quarterscore'), Js('Recrecade'), Js('Relaxacade'), Js('Relaxcore'), Js('Relaxscore'), Js('Rethrone'), Js('Retrocade'), Js('Retrocity'), Js('Retrophy'), Js('Retropolis'), Js('Retroscore'), Js('Retrove'), Js('Skyscore'), Js('Solarcade'), Js('Sparcade'), Js('Standbyscore'), Js('Starcade'), Js('Stelarcade'), Js('Tokencade'), Js('Tokenstop'), Js('Toycade'), Js('Toymania'), Js('Toyplace'), Js('Toyscore'), Js('Toyspot'), Js('Tsarcade'), Js('Wifiscore'), Js('Wondercade'), Js('Wonderhall'), Js('Wonderplace'), Js('Wonderscore')]))
    var.put('nm3', Js([Js('Arcade'), Js('Game Hall'), Js('Gaming Center'), Js('Game Center'), Js('Game Junction'), Js('Arcade'), Js('Arcade'), Js('Gamer Club'), Js('Gamer Center'), Js('Arcade'), Js('Arcade'), Js('Arcade')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', (((Js('The ')+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm3').callprop('splice', var.get('rnd2'), Js(1.0))
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
arcadeNames = var.to_python()