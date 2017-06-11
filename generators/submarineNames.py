__all__ = ['submarineNames']

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
    var.registers(['nm1', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Abzu'), Js('Achelous'), Js('Acionna'), Js('Aegaeon'), Js('Aegir'), Js('Agunua'), Js('Agwe'), Js('Ahti'), Js('Akheilos'), Js('Alignak'), Js('Alpheus'), Js('Amathaunta'), Js('Amemasu'), Js('Amphitrite'), Js('Anahita'), Js('Anapos'), Js('Anuket'), Js('Apah'), Js('Asherah'), Js('Aspidochelone'), Js('Atlantis'), Js('Atrimpas'), Js('Bakunawa'), Js('Bandua'), Js('Belisama'), Js('Brizo'), Js('Capricorn'), Js('Carcinus'), Js('Ceto'), Js('Cetus'), Js('Charybdis'), Js('Clermeil'), Js('Condatis'), Js('Cymopoleia'), Js('Dakuwaqa'), Js('Daucina'), Js('Davy Jones'), Js('Delphin'), Js('Doris'), Js('Durius'), Js('Ebisu'), Js('Eidothea'), Js('Eingana'), Js('Electra'), Js('Enki'), Js('Euryale'), Js('Eurybia'), Js('Ezili'), Js('Fontus'), Js('Freyr'), Js('Galene'), Js('Ganga'), Js('Glaucus'), Js('Gorgon'), Js('Graeae'), Js('Haik'), Js('Hapi'), Js('Hippocampus'), Js('Hydra'), Js('Idemili'), Js('Ikatere'), Js('Illuyanka'), Js('Imoogi'), Js('Jormungandr'), Js('Juturna'), Js('Kamohoalii'), Js('Kanaloa'), Js('Khnum'), Js('Kraken'), Js('Lados'), Js('Leucothea'), Js('Leviathan'), Js('Lir'), Js('Llyr'), Js('Longma'), Js('Longmu'), Js('Lotan'), Js('Makara'), Js('Mammu'), Js('Marduk'), Js('Martuv'), Js('Mazu'), Js('Medusa'), Js('Mermaid'), Js('Merman'), Js('Mizuchi'), Js('Naiades'), Js('Namaka'), Js('Nanshe'), Js('Nehalennia'), Js('Nepra'), Js('Nepthys'), Js('Neptune'), Js('Nereides'), Js('Nereus'), Js('Neringa'), Js('Neris'), Js('Nerites'), Js('Nerthus'), Js('Nessie'), Js('Nix'), Js('Njord'), Js('Nodens'), Js('Nommos'), Js('Nu'), Js('Nyakaio'), Js('Nymph'), Js('Oceanus'), Js('Opochtli'), Js('Oshun'), Js('Osiris'), Js('Palaemon'), Js('Pan'), Js('Pandora'), Js('Pariacaca'), Js('Paricia'), Js('Phorcys'), Js('Pontus'), Js('Poseidon'), Js('Potamoi'), Js('Presno'), Js('Proteus'), Js('Psamathe'), Js('Ran'), Js('Saga'), Js('Salacia'), Js('Samundra'), Js('Satet'), Js('Sculla'), Js('Scylla'), Js('Sedna'), Js('Sequana'), Js('Sinann'), Js('Siren'), Js('Sirena'), Js('Sirsir'), Js('Siyokoy'), Js('Sobek'), Js('Stheno'), Js('Suijin'), Js('Susanoo'), Js('Tangaroa'), Js('Tapti'), Js('Tefnut'), Js('Telchine'), Js('Tethys'), Js('Thalassa'), Js('Thaumas'), Js('Thetis'), Js('Tiamat'), Js('Tiberinus'), Js('Tlaloc'), Js('Triteia'), Js('Triton'), Js('Tritone'), Js('Ukupanipo'), Js('Urashi'), Js('Varuna'), Js('Veles'), Js('Vellamo'), Js('Volturnus'), Js('Watatsumi'), Js('Wirnpa'), Js('Yam'), Js('Yami'), Js('Yemoja'), Js('Yurlungur')]))
    var.put('nm2', Js([Js('Abalone'), Js('Albacore'), Js('Amberjack'), Js('Anemone'), Js('Angelfish'), Js('Angler'), Js('Anglerfish'), Js('Barnacle'), Js('Barracuda'), Js('Bass'), Js('Bull Shark'), Js('Carp'), Js('Clam'), Js('Cod'), Js('Conch'), Js('Crab'), Js('Crocodile'), Js('Cuttlefish'), Js('Dolphin'), Js('Dragonet'), Js('Dugong'), Js('Eel'), Js('Flounder'), Js('Fringehead'), Js('Fugu'), Js('Goblin Shark'), Js('Great White'), Js('Grouper'), Js('Haddock'), Js('Halibut'), Js('Hammerhead'), Js('Hapuka'), Js('Hermit'), Js('Hermit Crab'), Js('Herring'), Js('Humpback'), Js('Irukandji'), Js('Jellyfish'), Js('Killer Whale'), Js('Kingfish'), Js('Lionfish'), Js('Lobster'), Js('Loggerhead'), Js('Mackerel'), Js("Man o' War"), Js('Manatee'), Js('Manta'), Js('Marlin'), Js('Megalodon'), Js('Monkfish'), Js('Moray'), Js('Mulloway'), Js('Narwhal'), Js('Nautilus'), Js('Octopus'), Js('Orca'), Js('Otter'), Js('Oyster'), Js('Porpoise'), Js('Puffer'), Js('Pufferfish'), Js('Quahog'), Js('Ray'), Js('Salmon'), Js('Sea Horse'), Js('Sea Lion'), Js('Sea Snake'), Js('Seadragon'), Js('Seal'), Js('Shark'), Js('Shrimp'), Js('Snapper'), Js('Spider Crab'), Js('Squid'), Js('Starfish'), Js('Stingray'), Js('Sturgeon'), Js('Swordfish'), Js('Triggerfish'), Js('Tuna'), Js('Turtle'), Js('Urchin'), Js('Walrus'), Js('Whale'), Js('Whapuku'), Js('White Whale'), Js('Wobbegong'), Js('Wolffish'), Js('Wrasse'), Js('Xiphias'), Js('Xiphosura')]))
    var.put('nm3', Js([Js('Achiever'), Js('Adventure'), Js('Aftermath'), Js('Agent'), Js('Ambition'), Js('Analysis'), Js('Analyst'), Js('Aspect'), Js('Authority'), Js('Blade'), Js('Boundary'), Js('Bravery'), Js('Brilliance'), Js('Brutality'), Js('Champion'), Js('Chaos'), Js('Clarity'), Js('Confidence'), Js('Consequence'), Js('Courage'), Js('Curtain'), Js('Delight'), Js('Delivery'), Js('Desire'), Js('Destiny'), Js('Determination'), Js('Dexterity'), Js('Discovery'), Js('Distribution'), Js('Elegance'), Js('Enigma'), Js('Eternity'), Js('Fluke'), Js('Focus'), Js('Fortune'), Js('Freedom'), Js('Generosity'), Js('Grace'), Js('Grandure'), Js('Guidance'), Js('Harmony'), Js('Humility'), Js('Impulse'), Js('Independence'), Js('Infinity'), Js('Intelligence'), Js('Intervention'), Js('Journey'), Js('Judgment'), Js('Justice'), Js('Liberty'), Js('Matriarch'), Js('Mercy'), Js('Miracle'), Js('Omen'), Js('Opportunity'), Js('Oracle'), Js('Patience'), Js('Patriarch'), Js('Patriot'), Js('Perseverance'), Js('Philosophy'), Js('Possibility'), Js('Precision'), Js('Pride'), Js('Principle'), Js('Priority'), Js('Psychology'), Js('Quest'), Js('Request'), Js('Requiem'), Js('Research'), Js('Respect'), Js('Response'), Js('Responsibility'), Js('Royalty'), Js('Secretary'), Js('Shadow'), Js('Signature'), Js('Solitude'), Js('Solution'), Js('Storm'), Js('Stranger'), Js('Strategy'), Js('Surgery'), Js('Sympathy'), Js('Theory'), Js('Thrill'), Js('Thunder'), Js('Tourist'), Js('Victory'), Js('Visitor'), Js('Voyage'), Js('Wonder')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(3.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                var.put('names', (Js('The ')+var.get('nm1').get(var.get('rnd'))))
                var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            else:
                if (var.get('i')<Js(7.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('names', (Js('The ')+var.get('nm2').get(var.get('rnd'))))
                    var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                    var.put('names', (Js('The ')+var.get('nm3').get(var.get('rnd'))))
                    var.get('nm3').callprop('splice', var.get('rnd'), Js(1.0))
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
submarineNames = var.to_python()