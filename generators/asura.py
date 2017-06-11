__all__ = ['asura']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm8', 'nm3', 'nm7', 'nm9', 'nm2', 'nm6'])
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
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm6').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm7').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm8').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm9').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+Js(' '))+var.get('nm6').get(var.get('rnd2')))+var.get('nm7').get(var.get('rnd3')))+var.get('nm8').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5'))))
                else:
                    var.put('names', (((((var.get('nm6').get(var.get('rnd2'))+var.get('nm7').get(var.get('rnd3')))+var.get('nm8').get(var.get('rnd4')))+var.get('nm9').get(var.get('rnd5')))+Js(' the '))+var.get('nm5').get(var.get('rnd'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd4', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('rnd5', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                if (var.get('i')<Js(5.0)):
                    var.put('names', (((((var.get('nm5').get(var.get('rnd'))+Js(' '))+var.get('nm1').get(var.get('rnd2')))+var.get('nm2').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5'))))
                else:
                    var.put('names', (((((var.get('nm1').get(var.get('rnd2'))+var.get('nm2').get(var.get('rnd3')))+var.get('nm3').get(var.get('rnd4')))+var.get('nm4').get(var.get('rnd5')))+Js(' the '))+var.get('nm5').get(var.get('rnd'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('Y'), Js('Z'), Js('Bl'), Js('Br'), Js('Bj'), Js('Dl'), Js('Dr'), Js('Dk'), Js('Dn'), Js('Fl'), Js('Fr'), Js('Fj'), Js('Gr'), Js('Gl'), Js('Gn'), Js('Gh'), Js('Bh'), Js('Dh'), Js('Kr'), Js('Kl'), Js('Kh'), Js('Kj'), Js('Lh'), Js('Mh'), Js('Pr'), Js('Pl'), Js('Pj'), Js('Ph'), Js('Rh'), Js('Qh'), Js('Sl'), Js('Sr'), Js('Sh'), Js('Tr'), Js('Tw'), Js('Sw'), Js('Pw'), Js('Kw'), Js('Dw'), Js('Bw'), Js('Vr'), Js('Vl'), Js('Sn'), Js('Sm'), Js('Zn'), Js('Zm'), Js('Str')]))
var.put('nm2', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('ea'), Js('eo'), Js('ia'), Js('io'), Js('ou'), Js('ua'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u')]))
var.put('nm3', Js([Js('bb'), Js('dd'), Js('ff'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt'), Js('xx'), Js('zz'), Js('bb'), Js('dd'), Js('ff'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt'), Js('xx'), Js('zz'), Js('b'), Js('d'), Js('f'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('x'), Js('z')]))
var.put('nm4', Js([Js('oq'), Js('iq'), Js('aq'), Js('eq'), Js('uq'), Js('ot'), Js('it'), Js('at'), Js('et'), Js('ut'), Js('ap'), Js('op'), Js('ip'), Js('ep'), Js('up'), Js('os'), Js('is'), Js('as'), Js('es'), Js('us'), Js('ad'), Js('id'), Js('od'), Js('ed'), Js('ud'), Js('of'), Js('if'), Js('af'), Js('ef'), Js('uf'), Js('og'), Js('ig'), Js('ag'), Js('eg'), Js('ug'), Js('ok'), Js('ik'), Js('ak'), Js('ek'), Js('uk'), Js('ol'), Js('il'), Js('al'), Js('el'), Js('ul'), Js('oz'), Js('iz'), Js('az'), Js('ez'), Js('uz'), Js('ox'), Js('ix'), Js('ax'), Js('ex'), Js('ux'), Js('on'), Js('in'), Js('an'), Js('en'), Js('un'), Js('om'), Js('im'), Js('am'), Js('em'), Js('um'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
var.put('nm5', Js([Js('Abjurer'), Js('Adept'), Js('Advisor'), Js('Agent'), Js('Alchemist'), Js('Alchemagician'), Js('Alienist'), Js('Artisan'), Js('Artificer'), Js('Architect'), Js('Analyst'), Js('Analyzer'), Js('Archivist'), Js('Assembler'), Js('Assistant'), Js('Astronomer'), Js('Attuner'), Js('Beastmaster'), Js('Builder'), Js('Cabalist'), Js('Calibrator'), Js('Calculator'), Js('Calumniator'), Js('Chemist'), Js('Cleaner'), Js('Chef'), Js('Chronicler'), Js('Compiler'), Js('Conjuror'), Js('Constructor'), Js('Convoker'), Js('Counselor'), Js('Collator'), Js('Collaborator'), Js('Crafter'), Js('Craftsman'), Js('Creator'), Js('Deconstructor'), Js('Demolisher'), Js('Demolitionist'), Js('Designer'), Js('Defender'), Js('Deviser'), Js('Director'), Js('Disassembler'), Js('Diviner'), Js('Doctor'), Js('Dynamist'), Js('Editor'), Js('Elementalist'), Js('Eliminator'), Js('Emulator'), Js('Enforcer'), Js('Engineer'), Js('Evoker'), Js('Expert'), Js('Explorer'), Js('Examiner'), Js('Extinguisher'), Js('Exterminator'), Js('Fabricator'), Js('Gemcutter'), Js('Generator'), Js('Golementalist'), Js('Golemwright'), Js('Guardian'), Js('Gunsmith'), Js('Guide'), Js('Helper'), Js('Hunter'), Js('Huntsman'), Js('Hypnotist'), Js('Illustrator'), Js('Initiator'), Js('Innovator'), Js('Invader'), Js('Invoker'), Js('Instructor'), Js('Instigator'), Js('Interlocutor'), Js('Interrogator'), Js('Insurrectionist'), Js('Inventor'), Js('Inveigler'), Js('Investigator'), Js('Infiltrator'), Js('Krewe Chief'), Js('Kreweman'), Js('Liquidator'), Js('Maestro'), Js('Machinist'), Js('Marksman'), Js('Mathematician'), Js('Mechanic'), Js('Mechwright'), Js('Mechsmith'), Js('Metallurgist'), Js('Metaphysicist'), Js('Mentor'), Js('Mesmer'), Js('Monitor'), Js('Mortifactor'), Js('Mortificator'), Js('Navigator'), Js('Necromancer'), Js('Operator'), Js('Optimizer'), Js('Organizer'), Js('Originator'), Js('Paraphysicist'), Js('Pathfinder'), Js('Phantasmist'), Js('Physicist'), Js('Pistoleer'), Js('Planner'), Js('Princeps'), Js('Progenitor'), Js('Prognosticator'), Js('Protector'), Js('Provoker'), Js('Professor'), Js('Preceptor'), Js('Psychometrist'), Js('Reanimator'), Js('Recalibrator'), Js('Researcher'), Js('Retriever'), Js('Refiner'), Js('Revisionist'), Js('Sage'), Js('Schematicist'), Js('Seeker'), Js('Sentinel'), Js('Schemer'), Js('Scientist'), Js('Savant'), Js('Saboteur'), Js('Subversionist'), Js('Specialist'), Js('Statistician'), Js('Supervisor'), Js('Surveyor'), Js('Synergist'), Js('Teacher'), Js('Techwright'), Js('Techsmith'), Js('Thaumaturgist'), Js('Theorist'), Js('Theonomist'), Js('Thermodynamist'), Js('Trailblazer'), Js('Trainer'), Js('Visualizer'), Js('Weaponeer'), Js('Electrician'), Js('Mortician'), Js('Scientician'), Js('Technician'), Js('Magitechnician'), Js('Necrotechnician'), Js('Pyrotechnician'), Js('Cryotechnician'), Js('Hydrotechnician'), Js('Aerotechnician'), Js('Terratechnician'), Js('Electrotechnician'), Js('Chronotechnician'), Js('Astromancer'), Js('Pyromancer'), Js('Cryomancer'), Js('Aeromancer'), Js('Geomancer'), Js('Terramancer'), Js('Electromancer'), Js('Chronomancer'), Js('Technomancer'), Js('Techromancer'), Js('Golemancer'), Js('Alchemologist'), Js('Anthropologist'), Js('Biologist'), Js('Botanist'), Js('Geologist'), Js('Elixologist'), Js('Chronologist'), Js('Electrologist'), Js('Parabiologist'), Js('Parabotanist'), Js('Pyrologist'), Js('Necrologist'), Js('Cryologist'), Js('Hydrologist'), Js('Aerologist'), Js('Terrologist'), Js('Hypnologist'), Js('Illusionist'), Js('Conflagrationist'), Js('Schematologist'), Js('Technologist'), Js('Tempestologist'), Js('Mesmerologist'), Js('Meteorologist'), Js('Mixologist'), Js('Gemologist'), Js('Golemologist'), Js('Radiologist'), Js('Thaumatologist'), Js('Wraithologist'), Js('Vulcanologist'), Js('Xenologist ')]))
var.put('nm6', Js([Js('A'), Js('B'), Js('C'), Js('D'), Js('E'), Js('F'), Js('G'), Js('H'), Js('I'), Js('J'), Js('K'), Js('L'), Js('M'), Js('N'), Js('O'), Js('P'), Js('Q'), Js('R'), Js('S'), Js('T'), Js('U'), Js('V'), Js('W'), Js('Y'), Js('Z'), Js('Bl'), Js('Br'), Js('Bj'), Js('Dl'), Js('Dr'), Js('Dk'), Js('Dn'), Js('Fl'), Js('Fr'), Js('Fj'), Js('Gr'), Js('Gl'), Js('Gn'), Js('Gh'), Js('Bh'), Js('Dh'), Js('Kr'), Js('Kl'), Js('Kh'), Js('Kj'), Js('Lh'), Js('Mh'), Js('Pr'), Js('Pl'), Js('Pj'), Js('Ph'), Js('Rh'), Js('Qh'), Js('Sl'), Js('Sr'), Js('Sh'), Js('Tr'), Js('Tw'), Js('Sw'), Js('Pw'), Js('Kw'), Js('Dw'), Js('Bw'), Js('Vr'), Js('Vl'), Js('Sn'), Js('Sm'), Js('Zn'), Js('Zm'), Js('Str')]))
var.put('nm7', Js([Js('a'), Js('e'), Js('o'), Js('i'), Js('u'), Js('ea'), Js('eo'), Js('ia'), Js('io'), Js('ou'), Js('ua'), Js('a'), Js('e'), Js('o'), Js('i'), Js('u')]))
var.put('nm8', Js([Js('bb'), Js('dd'), Js('ff'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt'), Js('xx'), Js('zz'), Js('bb'), Js('dd'), Js('ff'), Js('gg'), Js('kk'), Js('ll'), Js('mm'), Js('nn'), Js('pp'), Js('rr'), Js('ss'), Js('tt'), Js('xx'), Js('zz'), Js('b'), Js('d'), Js('f'), Js('g'), Js('k'), Js('l'), Js('m'), Js('n'), Js('p'), Js('r'), Js('s'), Js('t'), Js('x'), Js('z')]))
var.put('nm9', Js([Js('o'), Js('i'), Js('a'), Js('e'), Js('u')]))
pass
pass


# Add lib to the module scope
asura = var.to_python()