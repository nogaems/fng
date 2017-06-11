__all__ = ['digimonNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nameGen'])
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
            var.put('names', (var.get('nm1').get(var.get('rnd'))+Js('mon')))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Abra'), Js('Acri'), Js('Aera'), Js('Alche'), Js('Alcho'), Js('Alli'), Js('Allu'), Js('Ana'), Js('Ano'), Js('Anomali'), Js('Apo'), Js('Aqua'), Js('Aqui'), Js('Ar'), Js('Arach'), Js('Arca'), Js('Arcani'), Js('Arka'), Js('Armada'), Js('Aro'), Js('Astro'), Js('Augu'), Js('Aura'), Js('Auro'), Js('Aurora'), Js('Ava'), Js('Avala'), Js('Avia'), Js('Barba'), Js('Barra'), Js('Blaiz'), Js('Blo'), Js('Bloo'), Js('Boul'), Js('Bri'), Js('Cala'), Js('Cani'), Js('Car'), Js('Carbo'), Js('Ceru'), Js('Ceruli'), Js('Chakra'), Js('Chao'), Js('Char'), Js('Charo'), Js('Chrono'), Js('Cim'), Js('Clai'), Js('Clari'), Js('Clou'), Js('Colo'), Js('Conju'), Js('Crea'), Js('Cree'), Js('Cryo'), Js('Crys'), Js('Curio'), Js('Cyclo'), Js('Dae'), Js('Daw'), Js('Debri'), Js('Devi'), Js('Dia'), Js('Dino'), Js('Divi'), Js('Divina'), Js('Divino'), Js('Domi'), Js('Domina'), Js('Dra'), Js('Draca'), Js('Draco'), Js('Drago'), Js('Droi'), Js('Dubi'), Js('Dyna'), Js('Ecli'), Js('Eido'), Js('Ele'), Js('Emera'), Js('Emeral'), Js('Empea'), Js('Enig'), Js('Equi'), Js('Ethe'), Js('Ethere'), Js('Exo'), Js('Exorci'), Js('Fae'), Js('Fe'), Js('Fel'), Js('Feli'), Js('Feni'), Js('Fer'), Js('Fero'), Js('Fie'), Js('Fiero'), Js('Fir'), Js('Fla'), Js('Flore'), Js('Forre'), Js('Fossi'), Js('Fro'), Js('Fue'), Js('Furi'), Js('Fusi'), Js('Fye'), Js('Garga'), Js('Gargo'), Js('Gaze'), Js('Gela'), Js('Geno'), Js('Gho'), Js('Giga'), Js('Gira'), Js('Gla'), Js('Glaci'), Js('Glamo'), Js('Gloo'), Js('Gori'), Js('Grani'), Js('Gro'), Js('Grotto'), Js('Guru'), Js('Halo'), Js('Har'), Js('Heini'), Js('Helli'), Js('Herbo'), Js('Hocu'), Js('Horo'), Js('Horro'), Js('Hurica'), Js('Hydra'), Js('Hydro'), Js('Hye'), Js('Icicli'), Js('Igli'), Js('Igni'), Js('Illu'), Js('Imme'), Js('Imperi'), Js('Impero'), Js('Inca'), Js('Incanto'), Js('Ince'), Js('Incorpo'), Js('Infer'), Js('Infi'), Js('Iri'), Js('Iro'), Js('Jagua'), Js('Juju'), Js('Kata'), Js('Katana'), Js('Kine'), Js('Kni'), Js('Knigh'), Js('Koa'), Js('Lavi'), Js('Le'), Js('Leo'), Js('Levi'), Js('Levia'), Js('Lily'), Js('Liqui'), Js('Ludi'), Js('Lumi'), Js('Luminu'), Js('Lussio'), Js('Ma'), Js('Mag'), Js('Magma'), Js('Magne'), Js('Mali'), Js('Mammo'), Js('Mana'), Js('Maxi'), Js('Meta'), Js('Mino'), Js('Mobo'), Js('Monsoo'), Js('Mor'), Js('Mosqi'), Js('Muta'), Js('Myste'), Js('Mysteri'), Js('Ne'), Js('Nefar'), Js('Nemo'), Js('Neptu'), Js('Nero'), Js('Nexi'), Js('Ninja'), Js('Nova'), Js('Novi'), Js('Octo'), Js('Ome'), Js('Omega'), Js('Ori'), Js('Oxy'), Js('Ozo'), Js('Paci'), Js('Para'), Js('Parado'), Js('Perma'), Js('Perra'), Js('Peta'), Js('Phan'), Js('Phanta'), Js('Phi'), Js('Phili'), Js('Phoe'), Js('Plu'), Js('Pocu'), Js('Pow'), Js('Precipi'), Js('Pri'), Js('Prophi'), Js('Psy'), Js('Puri'), Js('Pye'), Js('Qua'), Js('Quai'), Js('Radi'), Js('Rag'), Js('Ray'), Js('Razo'), Js('Reve'), Js('Rhino'), Js('Rive'), Js('Robo'), Js('Rubi'), Js('Sabe'), Js('Safri'), Js('Sala'), Js('Sali'), Js('Saphi'), Js('Saru'), Js('Sava'), Js('Scal'), Js('Scor'), Js('Scorpi'), Js('Sere'), Js('Serpen'), Js('Shado'), Js('Shay'), Js('Shri'), Js('Shy'), Js('Sire'), Js('Skele'), Js('Skye'), Js('Slai'), Js('Smol'), Js('Smoldo'), Js('Sola'), Js('Soro'), Js('Speci'), Js('Spiri'), Js('Spoo'), Js('Squi'), Js('Stor'), Js('Tempe'), Js('Tempri'), Js('Terbi'), Js('Tero'), Js('Terra'), Js('Terri'), Js('Thau'), Js('Thauma'), Js('Thor'), Js('Tini'), Js('Tira'), Js('Tita'), Js('Tremo'), Js('Tropo'), Js('Twi'), Js('Twilei'), Js('Typho'), Js('Unani'), Js('Uni'), Js('Uno'), Js('Uvee'), Js('Vala'), Js('Vapo'), Js('Veilio'), Js('Veni'), Js('Veno'), Js('Vexi'), Js('Volu'), Js('Voodoo'), Js('Vultu'), Js('Walla'), Js('Were'), Js('Whimsi'), Js('Willo'), Js('Windi'), Js('Xyge'), Js('Zeno'), Js('Zephy')]))
pass
pass


# Add lib to the module scope
digimonNames = var.to_python()