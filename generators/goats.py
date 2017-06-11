__all__ = ['goats']

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
var.put('nm1', Js([Js('Agnes'), Js('Alfie'), Js('Allie'), Js('Amber'), Js('Amy'), Js('Anabell'), Js('Angel'), Js('Angela'), Js('Angie'), Js('Apache'), Js('Archie'), Js('Aurora'), Js('Autumn'), Js('Awall'), Js('Baby'), Js('Bailey'), Js('Baldrick'), Js('Basil'), Js('Beans'), Js('Beauty'), Js('Bell'), Js('Belle'), Js('Benny'), Js('Bernie'), Js('Beryl'), Js('Betty'), Js('BettyButton'), Js('BigTrudie'), Js('Blackberry'), Js('Blake'), Js('Blanche'), Js('Blondie'), Js('Boingo'), Js('Bonnie'), Js('Bonnie'), Js('Boomer'), Js('Boots'), Js('Botticelli'), Js('Brownie'), Js('Buckmeister'), Js('Buddy'), Js('Bugsy'), Js('Bumble'), Js('Buster'), Js('Capricorn'), Js('Capricorny'), Js('Chad'), Js('ChewChew'), Js('Chief'), Js('Chloe'), Js('Cinderella'), Js('Cinnamon'), Js('Cisco'), Js('Clover'), Js('Clyde'), Js('Cocoa'), Js('CoffeeBean'), Js('Colleen'), Js('Comet'), Js('Cookie'), Js('Cornbread'), Js('Cornelious'), Js('Cosmo'), Js('CottonBall'), Js('CottonTail'), Js('Creole'), Js('Daffodil'), Js('Daisy'), Js('Daisy'), Js('Dana'), Js('Dash'), Js('Delilah'), Js('Diamond'), Js('Dinner'), Js('Doc'), Js('Doe'), Js('Dottie'), Js('Duke'), Js('DumDum'), Js('Duncan'), Js('Ella'), Js('Fancy'), Js('Fern'), Js('Garfunkle'), Js('Gary'), Js('Gladys'), Js('Gladys'), Js('Gloria'), Js('Grace'), Js('Gunther'), Js('Gypsy'), Js('Hailey'), Js('Haley'), Js('Halle'), Js('Harvey'), Js('Heidi'), Js('Hemingway'), Js('Holly'), Js('Hoover'), Js('Hornless'), Js('Houdini'), Js('Hudson'), Js('Hyacinth'), Js('Isabell'), Js('Isabelle'), Js('Ivy'), Js('Jeremy'), Js('Jessie'), Js('Julius'), Js('July'), Js('Kaytee'), Js('Kebab'), Js('Kebob'), Js('Kisses'), Js('Lady'), Js('Lancelot'), Js('Lane'), Js('Legend'), Js('Lena'), Js('Lily'), Js('Lucky'), Js('Lucky'), Js('Lucy'), Js('Lybris'), Js('Lydia'), Js('Lynn'), Js('MaeFlower'), Js('Maggie'), Js('MaggieMay'), Js('Mandy'), Js('Manny'), Js('Marisa'), Js('Marshall'), Js('Martini'), Js('Mary'), Js('Matilda'), Js('Maybell'), Js('Mercury'), Js('Meridian'), Js('Midnight'), Js('Milkshake'), Js('Milky'), Js('Mimi'), Js('Miracle'), Js('Missy'), Js('Mocha'), Js('Molly'), Js('Molly'), Js('Montana'), Js('Montgomery'), Js('Moose'), Js('Morty'), Js('MrBongo'), Js('Nanna'), Js('Nellie'), Js('Nibbler'), Js('Nibler'), Js('Niblets'), Js('Noelle'), Js('Nova'), Js('Omega'), Js('Oreo'), Js('Orion'), Js('Osiris'), Js('Pansy'), Js('Patches'), Js('Peaches'), Js('Pearl'), Js('Peepers'), Js('Penelope'), Js('Penny'), Js('Peony'), Js('Pepper'), Js('Pepper'), Js('Petticoat'), Js('Pettigoat'), Js('Petunia'), Js('Petunia'), Js('Pierre'), Js('Poppy'), Js('Prancer'), Js('Precious'), Js('Princess'), Js('Promise'), Js('Pumpkin'), Js('Rack'), Js('Ramses'), Js('Ramzy'), Js('Remington'), Js('Riley'), Js('Ringo'), Js('Rodney'), Js('Rosa'), Js('Rose'), Js('Rowdy'), Js('Rufus'), Js('Russell'), Js('Rusty'), Js('Sable'), Js('Sabrina'), Js('Sage'), Js('Salem'), Js('Samantha'), Js('Sammy'), Js('Sandy'), Js('Sandy'), Js('Saphire'), Js('Sassafras'), Js('Scruffy'), Js('Shack'), Js('Shadow'), Js('Shaggy'), Js('Shane'), Js('Sierra'), Js('Simon'), Js('Skittles'), Js('Skooter'), Js('Smokey'), Js('Smoky'), Js('Snickers'), Js('Snowball'), Js('Snowwhite'), Js('Socks'), Js('Socks'), Js('Sonny'), Js('Sophie'), Js('Spanky'), Js('Spartacus'), Js('Spice'), Js('Spicey'), Js('Spirit'), Js('Spot'), Js('Stevie'), Js('Strawberry'), Js('Suleyman'), Js('Summer'), Js('Sunstar'), Js('Surya'), Js('Susie'), Js('Swiper'), Js('Tabitha'), Js('Tanya'), Js('Tapioca'), Js('Tasha'), Js('Tavia'), Js('Taz'), Js('Teeny'), Js('Tex'), Js('Thunder'), Js('Tinkerbelle'), Js('TinyDancer'), Js('Tonya'), Js('Topaz'), Js('Trixie'), Js('Trouble'), Js('Truffles'), Js('Tulip'), Js('Tullie'), Js('Twiggy'), Js('Twinkle'), Js('Twister'), Js('Tyler'), Js('Tyrone'), Js('Valentine'), Js('Velvet'), Js('Veronica'), Js('Victoria'), Js('Violet'), Js('Walden'), Js('Walnut'), Js('Weeny'), Js('Willie'), Js('Winter'), Js('Wizzer'), Js('Wonder'), Js('Yerba'), Js('Zeus'), Js('Ziggy'), Js('Zoe'), Js('Zuku'), Js('Zylonna')]))
var.put('nm2', Js([Js('AlfredHedgehog'), Js('AlphaHog'), Js('Aquila'), Js('Aramis'), Js('Archie'), Js('Bandit'), Js('Bean'), Js('Bell'), Js('Bill'), Js('Biscuit'), Js('Boarcupine'), Js('Bob'), Js('Boris'), Js('Brillo'), Js('BruceQuillis'), Js('Bruno'), Js('Bubbles'), Js('Caboodles'), Js('CactusJack'), Js('CaptainPrickard'), Js('Carlzander'), Js('Casper'), Js('Chad'), Js('Chester'), Js('ChuckNorris'), Js('Cinderquilla'), Js('Comet'), Js('CpnPrickard'), Js('Cyndaquill'), Js('Daggett'), Js('DavidHasselhog'), Js('DrQuillis'), Js('Ducks'), Js('EinSpine'), Js('Fernando'), Js('Flower'), Js('Fluffy'), Js('Frodo'), Js('Gabby'), Js('Genie'), Js('Gizmo'), Js('Grover'), Js('Harley'), Js('Harvey'), Js('Hayden'), Js('Hazel'), Js('HeathHedger'), Js('Hedgebert'), Js('Hedgehawg'), Js('Herbert'), Js('Hissyfit'), Js('HodgePodge'), Js('HogEatHog'), Js('Hogarth'), Js('Hokey'), Js('HokeyPokey'), Js('Isabella'), Js('Jacque'), Js('Journey'), Js('Kahlua'), Js('Kako'), Js('KatnissEverhog'), Js('Kenya'), Js('KillQuill'), Js('Kisses'), Js('Kit'), Js('Knarla'), Js('Lance'), Js('Lancelot'), Js('Liberty'), Js('LittleDipper'), Js('Luna'), Js('MaiseQuilliams'), Js('Maliha'), Js('MarkHamquill'), Js('Marshmallow'), Js('Marvin'), Js('McPricklesworth'), Js('Moxie'), Js('MrCactus'), Js('MrPrickles'), Js('MrPriclesworth'), Js('Muffy'), Js('Natasha'), Js('Needle'), Js('Needles'), Js('Norbert'), Js('Obie'), Js('Oscar'), Js('Pablo'), Js('Peanut'), Js('Penelope'), Js('Penny'), Js('Perry'), Js('Pinecone'), Js('Pinhead'), Js('Pointer'), Js('Poke'), Js('PokeRface'), Js('Pokey'), Js('Poky'), Js('Porcu'), Js('Porcupest'), Js('Porcupowned'), Js('Porki'), Js('Porkies'), Js('Porky'), Js('PrickAstley'), Js('Prickly'), Js('PrickyGervais'), Js('PrickyMartin'), Js('PrinceQuilliam'), Js('Priscilla'), Js('Punky'), Js('Q-Tip'), Js('Quilbert'), Js('Quilfrid'), Js('Quill.I.Am'), Js('QuillClinton'), Js('QuillFerrel'), Js('QuillMurray'), Js('QuillNighy'), Js('QuillRyker'), Js('QuillSmith'), Js('QuillWheaton'), Js('QuillYoung'), Js('QuillemDafoe'), Js('Quillen'), Js('Quilliam'), Js('QuilliamShatner'), Js('QuillieNelson'), Js('Quillow'), Js('QuillyWonka'), Js('Quinn'), Js('Rico'), Js('RobbieQuilliams'), Js('RobinQuilliams'), Js('Romeo'), Js('Sam'), Js('Shredder'), Js('Skeezix'), Js('SnoopHoggyHog'), Js('Snuggles'), Js('Sonar'), Js('Spike'), Js('SpikeBeaver'), Js('Spikey'), Js('Splinter'), Js('StickWithMe'), Js('StickyPig'), Js('Thiery'), Js('TomBombaquill'), Js('Tuffnel'), Js('Tumble'), Js('WinstonChurchquill')]))
pass
pass


# Add lib to the module scope
goats = var.to_python()