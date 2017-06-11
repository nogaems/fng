__all__ = ['mortalKombatNames']

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
    var.registers(['nm1', 'tp', 'result', 'type'])
    var.put('nm1', Js([Js('Alligator'), Js('Amida'), Js('Ammit'), Js('Amun'), Js('Ape'), Js('Arachnid'), Js('Arbal'), Js('Ash'), Js('Asseg'), Js('Asvin'), Js('Atl'), Js('Ax'), Js('Babi'), Js('Baboon'), Js('Badger'), Js('Ballis'), Js('Barong'), Js('Bayo'), Js('Bayonit'), Js('Bazoo'), Js('Bear'), Js('Beast'), Js('Bicks'), Js('Blade'), Js('Blight'), Js('Blits'), Js('Blyght'), Js('Brant'), Js('Brawl'), Js('Bruizer'), Js('Brutus'), Js('Buck'), Js('Buster'), Js('Butcher'), Js('Bynd'), Js('Cage'), Js('Cane'), Js('Cano'), Js('Carkas'), Js('Carn'), Js('Carpse'), Js('Carris'), Js('Carse'), Js('Carver'), Js('Cast'), Js('Cloud'), Js('Cobra'), Js('Combe'), Js('Coyote'), Js('Crane'), Js('Croc'), Js('Cudge'), Js('Cyn'), Js('Cynder'), Js('Cypher'), Js('Dagg'), Js('Darum'), Js('Dash'), Js('Daver'), Js('Davi'), Js('Dino'), Js('Draco'), Js('Draegon'), Js('Dragon'), Js('Dragonfly'), Js('Drake'), Js('Dynamo'), Js('Ebis'), Js('Enigma'), Js('Exxec'), Js('Falcon'), Js('Ferno'), Js('Fiend'), Js('Flame'), Js('Frag'), Js('Fume'), Js('Glive'), Js('Gorilla'), Js('Grave'), Js('Gritt'), Js('Grym'), Js('Gryme'), Js('Guillo'), Js('Hale'), Js('Haros'), Js('Hawk'), Js('Helia'), Js('Hippo'), Js('Hitt'), Js('Howitz'), Js('Ibis'), Js('Imp'), Js('Izana'), Js('Jackal'), Js('Jag'), Js('Kagu'), Js('Kame'), Js('Kangiten'), Js('Kannon'), Js('Komodo'), Js('Kriz'), Js('Kublai'), Js('Laki'), Js('Lance'), Js('Leech'), Js('Luce'), Js('Machet'), Js('Magnum'), Js('Magnus'), Js('Malyc'), Js('Mammoth'), Js('Manta'), Js('Mantis'), Js('Marat'), Js('Massac'), Js('Merce'), Js('Mercer'), Js('Mise'), Js('Mongoose'), Js('Mort'), Js('Necros'), Js('Nide'), Js('Nightingale'), Js('Nightowl'), Js('Nuke'), Js('Nunchu'), Js('Oblivion'), Js('Obsidian'), Js('Onyx'), Js('Oracle'), Js('Osir'), Js('Panther'), Js('Pest'), Js('Phoenix'), Js('Pulse'), Js('Pyre'), Js('Quake'), Js('Quaz'), Js('Queen Bee'), Js('Quelz'), Js('Quiv'), Js('Rackas'), Js('Radic'), Js('Raijin'), Js('Raptor'), Js('Rath'), Js('Rattle'), Js('Raze'), Js('Razor'), Js('Reaper'), Js('Rex'), Js('Rhino'), Js('Riot'), Js('Rudas'), Js('Ruzh'), Js('Ryze'), Js('Sabe'), Js('Sabre'), Js('Samit'), Js('Scarch'), Js('Scarn'), Js('Scatter'), Js('Scimi'), Js('Scourge'), Js('Scrimm'), Js('Scythe'), Js('Sekh'), Js('Semet'), Js('Serpent'), Js('Shav'), Js('Shiver'), Js('Silen'), Js('Siris'), Js('Skelt'), Js('Skirm'), Js('Skiv'), Js('Skiver'), Js('Slate'), Js('Slayer'), Js('Sliver'), Js('Slyce'), Js('Snyde'), Js('Soot'), Js('Spike'), Js('Splinter'), Js('Spyte'), Js('Stal'), Js('Stark'), Js('Storm'), Js('Surge'), Js('Sybre'), Js('Sylver'), Js('Tank'), Js('Tenac'), Js('Tiger'), Js('Torm'), Js('Torren'), Js('Tugs'), Js('Vapor'), Js('Viger'), Js('Vissu'), Js('Visus'), Js('Weasel'), Js('Wildcat'), Js('Wolf'), Js('Wolverine'), Js('Wrangler'), Js('Xerox'), Js('Yce'), Js('Zizor'), Js('Zyn')]))
    var.put('tp', var.get('type'))
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
mortalKombatNames = var.to_python()