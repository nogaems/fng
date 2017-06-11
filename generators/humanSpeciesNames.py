__all__ = ['humanSpeciesNames']

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
    var.put('nm1', Js([Js('Abditus (Concealed)'), Js('Abstrusus (Secret)'), Js('Acer (Fierce)'), Js('Aequus (Calm)'), Js('Albus (White)'), Js('Alius (Other)'), Js('Altus (High)'), Js('Amicus (Friendly)'), Js('Angustus (Narrow)'), Js('Antiquus (Ancient)'), Js('Arcanus (Silent)'), Js('Arenarius (Sandy)'), Js('Aureus (Golden)'), Js('Avarus (Greedy)'), Js('Bardus (Stupid)'), Js('Beatus (Fortunate)'), Js('Bellus (Handsome)'), Js('Bombycinus (Silken)'), Js('Brevis (Short)'), Js('Caecigenus (Born blind)'), Js('Caecus (Blind)'), Js('Caeruleus (Dark colored/blue)'), Js('Candidulus (Shining)'), Js('Candidus (Beautiful)'), Js('Castus (Pure)'), Js('Celer (Swift)'), Js('Celsus (Lofty)'), Js('Cineraceus (Gray)'), Js('Comatus (Hairy)'), Js('Creper (Obscure)'), Js('Cretatus (Chalked)'), Js('Cupidus (Desirous)'), Js('Delicatus (Delicate)'), Js('Diffusus (Spread out)'), Js('Diligens (Diligent)'), Js('Distinctus (Distinct)'), Js('Distortus (Distorted)'), Js('Dives (Rich)'), Js('Divinus (Divine)'), Js('Doctus (Learned)'), Js('Dolosus (Crafty)'), Js('Domesticus (Domestic)'), Js('Dulcis (Pleasant)'), Js('Efferatus (Savage)'), Js('Efferus (Savage)'), Js('Elatus (Exalted)'), Js('Emendatus (Perfect)'), Js('Emendosus (Wrong)'), Js('Exemius (Exceptional)'), Js('Exiguus (Scanty)'), Js('Extrarius (Foreign)'), Js('Facetus (Elegant)'), Js('Falsus (False)'), Js('Ferox (Savage)'), Js('Ferreus (Iron)'), Js('Ferus (Wild)'), Js('Festivus (Lively)'), Js('Fidelis (Loyal)'), Js('Fidus (Faithful)'), Js('Finitimus (Neighbouring)'), Js('Firmus (Strong)'), Js('Flavus (Yellow)'), Js('Fornicatus (Arched)'), Js('Fortis (Strong)'), Js('Fortunatus (Fortunate)'), Js('Frigidus (Cold)'), Js('Frivolus (Worthless)'), Js('Furtivus (Secret)'), Js('Furvus (Dark/black)'), Js('Fuscus (Brown)'), Js('Fusus (Spread out)'), Js('Generosus (Noble)'), Js('Gibber (Humpbacked)'), Js('Gilvus (Pale yellow)'), Js('Glaber (Hairless)'), Js('Gloriousus (Glorious)'), Js('Gracilis (Slender)'), Js('Grandaevus (Very old)'), Js('Hospitus (Strange)'), Js('Hostificum (Hostile)'), Js('Humilis (Humble)'), Js('Idem (Identical)'), Js('Immortalis (Immortal)'), Js('Infinitus (Countless)'), Js('Infirmus (Weak)'), Js('Ingens (Huge)'), Js('Inocgnito (Unknown)'), Js('Inopinatus (Unexpected)'), Js('Insanus (Insane)'), Js('Inscitus (Ignorant)'), Js('Inutilis (Useless)'), Js('Iratus (Angry)'), Js('Iucundus (Pleasant)'), Js('Liber (Free)'), Js('Liberalis (Generous)'), Js('Lucifugus (Light shunning)'), Js('Macer (Lean)'), Js('Maculosus (Spotted)'), Js('Magnanimus (Brave)'), Js('Magnus (Large)'), Js('Maior (Greater/older)'), Js('Malus (Bad)'), Js('Malus (Wicked)'), Js('Maritumus (Maritime)'), Js('Maximus (Greatest)'), Js('Mediocris (Mediocre)'), Js('Medius (Middle)'), Js('Melior (Better)'), Js('Merus (Pure)'), Js('Minus (Smaller)'), Js('Minutus (Small)'), Js('Mirabilis (Amazing)'), Js('Mirandus (Wonderful)'), Js('Misellus (Wretched)'), Js('Miser (Wretched)'), Js('Monstruosus (Monstrous)'), Js('Mortalis (Mortal)'), Js('Nasutus (Large nosed)'), Js('Nemorivagus (Wood wandering)'), Js('Nescius (Ignorant)'), Js('Niveus (Snowy)'), Js('Nivosus (Snowy)'), Js('Noctivagus (Night wandering)'), Js('Noctuabundus (Night travelling)'), Js('Nocturnus (Nightly)'), Js('Nopinus (Unexpected)'), Js('Novellus (New)'), Js('Obesus (Fat)'), Js('Organicus (Musical)'), Js('Otiosus (Idle)'), Js('Paluster (Marshy)'), Js('Pannosus (Ragged)'), Js('Pannuceus (Wrinkled)'), Js('Parvulus (Very small)'), Js('Parvus (Little)'), Js('Perpetuus (Perpetual)'), Js('Pessimus (Worst)'), Js('Picturatus (Painted)'), Js('Pictus (Artistic)'), Js('Potens (Mighty)'), Js('Primus (First)'), Js('Pristinus (Ancient)'), Js('Pristinus (Former)'), Js('Proavitus (Ancestoral)'), Js('Procellosus (Stormy)'), Js('Procerus (Tall)'), Js('Properus (Quick)'), Js('Pudicus (Chaste)'), Js('Pulchellus (Pretty)'), Js('Pulcher (Beautiful)'), Js('Pullus (Dark colored)'), Js('Rabidus (Savage)'), Js('Ratus (Calculated)'), Js('Recidivus (Returning)'), Js('Remissus (Gentle)'), Js('Remotus (Distant)'), Js('Repositus (Remote)'), Js('Ridiculus (Ridiculous)'), Js('Rubens (Red)'), Js('Rufus (Red)'), Js('Russus (Red)'), Js('Sacer (Sacred)'), Js('Sacratus (Sacred)'), Js('Salsus (Salty)'), Js('Saxeus (Rocky)'), Js('Saxosus (Rocky)'), Js('Scius (Knowing)'), Js('Secendus (Following)'), Js('Secundus (Second)'), Js('Sedatus (Quiet)'), Js('Silus (Snun-nosed)'), Js('Silvester (Wooded)'), Js('Similis (Similar)'), Js('Sincerus (Pure)'), Js('Solus (Sole)'), Js('Sonans (Noisy)'), Js('Sordidus (Dirty)'), Js('Sparus (Scattered)'), Js('Squameus (Scaly)'), Js('Squamosus (Scaly)'), Js('Stultus (Foolish)'), Js('Suavis (Sweet)'), Js('Sucinus (Of Amber)'), Js('Summus (Furthest)'), Js('Superbus (Arrogant)'), Js('Supremus (Highest)'), Js('Taciturnus (Silent)'), Js('Tardus (Slow)'), Js('Tenuis (Weak)'), Js('Tristis (Grim)'), Js('Tumulosus (Hilly)'), Js('Turbulentus (Muddy)'), Js('Turpis (Disgraceful)'), Js('Ultimus (Farthest)'), Js('Vagus (Wandering)'), Js('Velox (Fast)'), Js('Versutus (Dexterous)'), Js('Verus (True)'), Js('Vesanus (Insane)'), Js('Viridis (Green)')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('names', (Js('Homo ')+var.get('nm1').get(var.get('rnd'))))
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
humanSpeciesNames = var.to_python()