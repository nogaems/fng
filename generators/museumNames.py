__all__ = ['museumNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm2', 'nm3', 'nameGen'])
@Js
def PyJsHoisted_nameGen_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['nm1', 'result', 'nm4'])
    var.put('nm1', Js([Js('Accident'), Js('Aerial'), Js('Aerospace'), Js('Amphibian'), Js('Analysis'), Js('Anatomy'), Js('Ancestry'), Js('Anthropology'), Js('Apparatus'), Js('Aquatic'), Js('Archaeology'), Js('Architecture'), Js('Art'), Js('Artillery'), Js('Astronomy'), Js('Audiovisual'), Js('Auditory'), Js('Blossoms'), Js('Carnival'), Js('Changing'), Js('Childhood'), Js('Children'), Js('Chrono'), Js('Cryonic'), Js('Circus'), Js('Contemporary'), Js('Cooking'), Js('Costume'), Js('Creativity'), Js('Cryptology'), Js('Crystal'), Js('Cultural'), Js('Culture'), Js('Curiosity'), Js('Dance'), Js('Darkness'), Js('Data'), Js('Decorative'), Js('Design'), Js('Digital'), Js('Dinosaur'), Js('Disaster'), Js('Discovery'), Js('Dream'), Js('Dynamics'), Js('Earth'), Js('Electric'), Js('Emergency'), Js('Estate'), Js('Eternity'), Js('Expedition'), Js('Experiment'), Js('Experimentation'), Js('Exploration'), Js('Explorers'), Js('Fame'), Js('Fantasy'), Js('Fashion'), Js('Fear'), Js('Fiction'), Js('Film'), Js('Fire'), Js('Firepower'), Js('Forest'), Js('Fortune'), Js('Frost'), Js('Future'), Js('Gadget'), Js('Galaxy'), Js('Game'), Js('Garden'), Js('Genius'), Js('Gift'), Js('Gizmo'), Js('Glass'), Js('Globe'), Js('Gold'), Js('Guardian'), Js('Happiness'), Js('Harmony'), Js('Hazard'), Js('Heritage'), Js('History'), Js('Hope'), Js('Horror'), Js('Illusion'), Js('Imagination'), Js('Immersion'), Js('Infinity'), Js('Ingenuity'), Js('Inheritance'), Js('Innovation'), Js('Insect'), Js('Inspiration'), Js('Instrument'), Js('Invention'), Js('Jewel'), Js('Kinetics'), Js('Language'), Js('Learning'), Js('Legacy'), Js('Liberty'), Js('Light'), Js('Literature'), Js('Living'), Js('Locomotion'), Js('Love'), Js('Lunar'), Js('Machine'), Js('Magic'), Js('Magnetic'), Js('Manor'), Js('Manuscript'), Js('Maritime'), Js('Master'), Js('Mechanical'), Js('Medical'), Js('Micro'), Js('Mind'), Js('Mineral'), Js('Mistake'), Js('Movement'), Js('Music'), Js('Musical'), Js('Natural'), Js('Nature'), Js('Neurological'), Js('Night'), Js('Nightingale'), Js('Nightmare'), Js('Novelty'), Js('Open'), Js('Optical'), Js('Origin'), Js('Origins'), Js('Party'), Js('Passage'), Js('Passion'), Js('People'), Js('Perception'), Js('Pet'), Js('Petrified'), Js('Pinnacle'), Js('Play'), Js('Portrait'), Js('Prediction'), Js('Puppet'), Js('Pyro'), Js('Reconnaissance'), Js('Religion'), Js('Reptile'), Js('Research'), Js('Revelation'), Js('Rush'), Js('Sail'), Js('Science'), Js('Science Fiction'), Js('Secrets'), Js('Sensory'), Js('Serpent'), Js('Sight'), Js('Sightings'), Js('Silent'), Js('Skeleton'), Js('Snow'), Js('Solar'), Js('Space'), Js('Speech'), Js('Spinning'), Js('Sports'), Js('Stimulation'), Js('Submarine'), Js('Submerged'), Js('Sugar'), Js('Summer'), Js('Surprise'), Js('Tactile'), Js('Taste'), Js('Testing'), Js('Theater'), Js('Time'), Js('Toy'), Js('Tradition'), Js('Tragedy'), Js('Transport'), Js('Travel'), Js('Treasure'), Js('Trinket'), Js('Underground'), Js('Universe'), Js('Video'), Js('Virtual'), Js('Virtuoso'), Js('Visual'), Js('War'), Js('Water'), Js('Weirdness'), Js('Wild'), Js('Wind'), Js('Winter'), Js('Youth'), Js('Zoology')]))
    var.put('nm4', Js([Js('Accidents'), Js('Aerial Technology'), Js('Aerospace'), Js('Amphibians'), Js('Analysis'), Js('Anatomy'), Js('Ancestry'), Js('Anthropology'), Js('Aquatic Life'), Js('Archaeology'), Js('Architecture'), Js('Art'), Js('Artillery'), Js('Astronomy'), Js('Audio'), Js('Audiovisual Arts'), Js('Blossoms'), Js('Carnivals'), Js('Change'), Js('Childhood'), Js('Children'), Js('Cryonic Technology'), Js('Circuses'), Js('Contemporary Arts'), Js('Cooking'), Js('Costumes'), Js('Creativity'), Js('Cryptology'), Js('Crystals'), Js('Cultural History'), Js('Culture'), Js('Curiosity'), Js('Dance'), Js('Darkness'), Js('Data'), Js('Decoration'), Js('Design'), Js('Digital Arts'), Js('Dinosaurs'), Js('Disaster'), Js('Discovery'), Js('Dreams'), Js('Dynamics'), Js('Earth'), Js('Electricity'), Js('Emergencies'), Js('Eternity'), Js('Expeditions'), Js('Experimentations'), Js('Experiments'), Js('Exploration'), Js('Explorers'), Js('Fame'), Js('Fantasy'), Js('Fashion'), Js('Fear'), Js('Fiction'), Js('Film'), Js('Fire'), Js('Firepower'), Js('Forests'), Js('Fortune'), Js('Frost'), Js('Gadgets'), Js('Games'), Js('Gardens'), Js('Geniuses'), Js('Gifts'), Js('Gizmos'), Js('Glass'), Js('Gold'), Js('Guardians'), Js('Happiness'), Js('Harmony'), Js('Hazards'), Js('Heritage'), Js('History'), Js('Hope'), Js('Horrors'), Js('Illusions'), Js('Imagination'), Js('Immersion'), Js('Infinity'), Js('Ingenuity'), Js('Inheritance'), Js('Innovation'), Js('Insects'), Js('Inspiration'), Js('Instruments'), Js('Inventions'), Js('Jewels'), Js('Kinetics'), Js('Language'), Js('Learning'), Js('Legacies'), Js('Liberty'), Js('Light'), Js('Literature'), Js('Living'), Js('Locomotion'), Js('Love'), Js('Lunar History'), Js('Machines'), Js('Magic'), Js('Magnetics'), Js('Manors'), Js('Manuscripts'), Js('Maritime History'), Js('Masters'), Js('Mechanics'), Js('Medicine'), Js('Micro Life'), Js('Minerals'), Js('Mistakes'), Js('Movement'), Js('Music'), Js('Musicals'), Js('Natural History'), Js('Nature'), Js('Neurological Science'), Js('Nightmares'), Js('Novelties'), Js('Openness'), Js('Optical Illusions'), Js('Origins'), Js('Parties'), Js('Passages'), Js('Passion'), Js('People'), Js('Perception'), Js('Petrification'), Js('Pets'), Js('Pinnacles'), Js('Play'), Js('Portraits'), Js('Predictions'), Js('Puppets'), Js('Pyromania'), Js('Reconnaissance'), Js('Religion'), Js('Reptiles'), Js('Research'), Js('Revelations'), Js('Rush Hours'), Js('Sailing'), Js('Science'), Js('Science Fiction'), Js('Secrets'), Js('Sensory Science'), Js('Serpents'), Js('Sight'), Js('Sightings'), Js('Silence'), Js('Skeletons'), Js('Snow'), Js('Solar History'), Js('Space'), Js('Speech'), Js('Sports'), Js('Stimulation'), Js('Submarines'), Js('Submersion'), Js('Sugar'), Js('Summer'), Js('Surprises'), Js('Tactics'), Js('Taste'), Js('Testing'), Js('Theater'), Js('Time'), Js('Toys'), Js('Traditions'), Js('Tragedy'), Js('Transport'), Js('Travel'), Js('Treasures'), Js('Trinkets'), Js('Video'), Js('Virtual Reality'), Js('Visual Arts'), Js('War'), Js('Water'), Js('Weirdness'), Js('Wind'), Js('Winter'), Js('Youth'), Js('Zoology'), Js('the Future'), Js('the Galaxy'), Js('the Globe'), Js('the Mind'), Js('the Night'), Js('the Nightingale'), Js('the Underground'), Js('the Universe'), Js('the Wild')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('rnd3', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
            if (var.get('i')<Js(5.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('names', ((((var.get('nm3').get(var.get('rnd3'))+Js(' '))+var.get('nm2').get(var.get('rnd2')))+Js(' of '))+var.get('nm4').get(var.get('rnd'))))
                var.get('nm4').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
                var.put('names', ((((var.get('nm3').get(var.get('rnd3'))+Js(' '))+var.get('nm1').get(var.get('rnd')))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm2', Js([Js('Centre'), Js('Centre'), Js('Center'), Js('Center'), Js('Exhibition'), Js('Gallery'), Js('Gallery'), Js('Hall'), Js('Hall'), Js('Institute'), Js('Institution'), Js('Museum'), Js('Museum'), Js('Museum'), Js('Treasury'), Js('Vault')]))
var.put('nm3', Js([Js('National'), Js('International'), Js('Grand'), Js('Great'), Js('Central'), Js('Royal'), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js(''), Js('')]))
pass
pass


# Add lib to the module scope
museumNames = var.to_python()