__all__ = ['rabbitPets']

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
var.put('nm1', Js([Js('Hunter'), Js('Pooflez'), Js('Popcorn'), Js('8-ball'), Js('Abel'), Js('Able'), Js('Abraham'), Js('Ace'), Js('Acer'), Js('Achemy'), Js('Achilles'), Js('Acker'), Js('Adagio'), Js('Adam'), Js('Admiral'), Js('Aesop'), Js('Ajax'), Js('Al'), Js('Aladdin'), Js('Alaska'), Js('Alastair'), Js('Albert'), Js('Alchemy'), Js('Alex'), Js('Alexander'), Js('Alf'), Js('Alfi'), Js('Alfie'), Js('Aloysius'), Js('Alpaca'), Js('Alpine'), Js('Amadeus'), Js('Amazon'), Js('Ambrose'), Js('Amos'), Js('Angus'), Js('Apache'), Js('Apollo'), Js('Aragorn'), Js('Aramis'), Js('Archibald'), Js('Archie'), Js('Arfor'), Js('Arlo'), Js('Arnie'), Js('Arnold'), Js('Asa'), Js('Ash'), Js('Aspen'), Js('Asterix'), Js('Aston'), Js('Atlas'), Js('Augustus'), Js('Austin'), Js('Auston'), Js('Avalon'), Js('Baby'), Js('Badger'), Js('Baggins'), Js('Bailey'), Js('Baldwin'), Js('Baloo'), Js('Bam Bam'), Js('Barnaby'), Js('Barnacle'), Js('Barney'), Js('Bart'), Js('Bartholomew'), Js('Basil'), Js('Basket'), Js('Baxter'), Js('Bazooka'), Js('Beau'), Js('Beebo'), Js('Beefeater'), Js('Beethoven'), Js('Benny'), Js('Bentley'), Js('Beowulf'), Js('Bernstein'), Js('Bevis'), Js('Big Boss'), Js('Big Foot'), Js('Bijou'), Js('Bilbo'), Js('Bill'), Js('Biscuit'), Js('Bishop'), Js('Blackie'), Js('Blackjack'), Js('Blake'), Js('Blinker'), Js('Bliss'), Js('Blizzard'), Js('Blowout'), Js('Blue'), Js('Blue Blinker'), Js('Bo'), Js('Boatswain'), Js('Bobby'), Js('Bobo'), Js('Bogart'), Js('Bomber'), Js('Bonkers'), Js('Boo'), Js('BooBoo'), Js('Boomer'), Js('Boots'), Js('Boris'), Js('Boston'), Js('Boy'), Js('Brad'), Js('Bradly'), Js('Brady'), Js('Brie'), Js('Brisby'), Js('Bro'), Js('Brock'), Js('Bronson'), Js('Broody'), Js('Brownie'), Js('Bruce'), Js('Bruiser'), Js('Bruno'), Js('Bubba'), Js('Bubbles'), Js('Buck'), Js('Bud'), Js('Buffin'), Js('Bugs'), Js('Bullet'), Js('Bumper'), Js('Bunster'), Js('Busgsy'), Js('Busker'), Js('Buster'), Js('Butch'), Js('Butler'), Js('Butthead'), Js('Buttons'), Js('Buzz'), Js('Cadbury'), Js('Cadet'), Js('Caesar'), Js('Cajun'), Js('Calvin'), Js('Calypso'), Js('Camembert'), Js('Cappuccino'), Js('Captain'), Js('Captain Marvel'), Js('Casanova'), Js('Catbert'), Js('Cedric'), Js('Chad'), Js('Chance'), Js('Chandler'), Js('Chansu'), Js('Chaos'), Js('Charlie'), Js('Charmain'), Js('Charmin'), Js('Chasey'), Js('Checkers'), Js('Cheesel'), Js('Cheetos'), Js('Cheezels'), Js('Chester'), Js('Chevy'), Js('Chico'), Js('Chilli'), Js('Chino'), Js('Chip'), Js('Choccy'), Js('Chompsky'), Js('Choo'), Js('Chowder'), Js('Chubbs'), Js('Chunks'), Js('Chutney'), Js('Claude'), Js('Cloudy'), Js('Clyde'), Js('Cocoa'), Js('Coda'), Js('Cody'), Js('Coleman'), Js('Collin'), Js('Colonel'), Js('Comet'), Js('Cookie'), Js('Copper'), Js('Cornelius'), Js('Cornflake'), Js('Cosmo'), Js('Costanza'), Js('Cotton'), Js('Cottonball'), Js('Cowboy'), Js('Crush'), Js('Cuddles'), Js('DaVinci'), Js('Dagger'), Js('Dakota'), Js('Dalton'), Js('Dandelion'), Js('Dante'), Js('Darrow'), Js('Dash'), Js('Dean'), Js('Deedle'), Js('Dezzi'), Js('Diesel'), Js('Digger'), Js('Dilbert'), Js('Dinger'), Js('Dixie'), Js('Doc'), Js('Doctor Claw'), Js('Doolittle'), Js('Dopey'), Js('Doug'), Js('Dough Boy'), Js('Dude'), Js('Duke'), Js('Dumbbell'), Js('Dutch'), Js('Dwight'), Js('Earl'), Js('Earsy'), Js('Eastwood'), Js('Ebbie'), Js('Echo'), Js('Egor'), Js('Einstein'), Js('Ellsworth'), Js('Elmo'), Js('Elway'), Js('Elwood'), Js('Energizer'), Js('Ernie'), Js('Ewen'), Js('Excalibur'), Js('Fabio'), Js('Fandango'), Js('Farbar'), Js('Feldmann'), Js('Fenton'), Js('Ferrari'), Js('Ferris'), Js('Fievel'), Js('Finn'), Js('Firefly'), Js('Flopsy'), Js('Floyd'), Js('Fluffy'), Js('Fluffykins'), Js('Fonzi'), Js('Frankie'), Js('Franklin'), Js('Freckles'), Js('Frodo'), Js('Frostbite'), Js('Froth'), Js('Fudge'), Js('Fuzzmeister'), Js('G-Man'), Js('Gadget'), Js('Galvin'), Js('Galway'), Js('Gatsby'), Js('Gavin'), Js('Geoffrey'), Js('George'), Js('Gideon'), Js('Giggles'), Js('Gilbert'), Js('Ginger'), Js('Giovanni'), Js('Gizmo'), Js('Goblin'), Js('Goldfinger'), Js('Gomez'), Js('Gonzo'), Js('Gopher'), Js('Gouda'), Js('Graham'), Js('Gremlin'), Js('Gringo'), Js('Groucho'), Js('Grover'), Js('Guiness'), Js('Gumbo'), Js('Gummo'), Js('Gunther'), Js('Gus'), Js('Hacker'), Js('Haiku'), Js('Halo'), Js('Hamelin'), Js('Hamlet'), Js('Hardy'), Js('Harold'), Js('Harpo'), Js('Harrison'), Js('Harry'), Js('Harvey'), Js('Heath'), Js('Hector'), Js('Henry'), Js('Herb'), Js('Herbert'), Js('Herbie'), Js('Herman'), Js('Hershey'), Js('Hickory'), Js('Hobart'), Js('Hobbs'), Js('Hocus'), Js('Holbrook'), Js('Homey'), Js('Honey'), Js('Hopkins'), Js('Hopper'), Js('Hopscotch'), Js('Hopson'), Js('Houdini'), Js('Hutch'), Js('Indiana'), Js('Inki'), Js('Ismael'), Js('Itzy'), Js('Iverson'), Js('Izot'), Js('Jack'), Js('Jackson'), Js('Jaeger'), Js('Jake'), Js('Jammer'), Js('Jaws'), Js('Jeeves'), Js('Jenkins'), Js('Jericho'), Js('Jerome'), Js('Jett'), Js('Joe Cool'), Js('Johnny'), Js('Jola'), Js('Jonesy'), Js('Joshua'), Js('Juan'), Js('Jude'), Js('Juggernaut'), Js('Julius'), Js('Jumper'), Js('Juniper'), Js('Juno'), Js('Jupiter'), Js('Jurgen'), Js('Justen'), Js('Kalamazoo'), Js('Keanu'), Js('Keegan'), Js('Keifer'), Js('Kensington'), Js('Killer'), Js('Killigan'), Js('Kipling'), Js('Kitbull'), Js('Kobi'), Js('Kookaburra'), Js('Kozmo'), Js('Kramer'), Js('Kruger'), Js('Kunz'), Js('Lamar'), Js('Lambchop'), Js('Landers'), Js('Larry'), Js('Lastat'), Js('Laszlo'), Js('Lazar'), Js('Lemmy'), Js('Leo'), Js('Leonardo'), Js('Lex'), Js('Lexus'), Js('Lickerish'), Js('Licorice'), Js('Lightening'), Js('Lightning'), Js('Lilo'), Js('Linux'), Js('Locke'), Js('Longfellow'), Js('Lorenzo'), Js('Louie'), Js('Luck'), Js('Lucky'), Js('Lugosi'), Js('Lurky'), Js('Luxor'), Js('Lyndon'), Js('MacAlpin'), Js('Macaulay'), Js('Macbeth'), Js('Markel'), Js('Marley'), Js('Mars'), Js('Marshmallow'), Js('Marshmellow'), Js('Maverick'), Js('Max'), Js('Maxie'), Js('McFluffy'), Js('McFluffykins'), Js('Meatloaf'), Js('Mellow'), Js('Midget'), Js('Midnight'), Js('Millard'), Js('Mister'), Js('Mittens'), Js('Mopsy'), Js('Morgan'), Js('Morris'), Js('Moses'), Js('Mozart'), Js('Mr. Chompsky'), Js('Mr. Nibs'), Js('Muffin'), Js('Munchkin'), Js('Murphy'), Js('Nacho'), Js('Napoleon'), Js('Nathan'), Js('Ned'), Js('Neddy'), Js('Nelson'), Js('Nemo'), Js('Neopolatin'), Js('Neptune'), Js('Nero'), Js('Nesquik'), Js('Nibblers'), Js('Nibbles'), Js('Nickerson'), Js('Nijinsky'), Js('Niko'), Js('Niles'), Js('Nitro'), Js('Noah'), Js('Noel'), Js('Noir'), Js('Noogie'), Js('Nubby'), Js('Nunkie'), Js('Nuno'), Js('Nutmeg'), Js('Nutters'), Js('Nytrogen'), Js('O’Malley'), Js('Oakley'), Js('Obama'), Js('Obelix'), Js('Odie'), Js('Olivier'), Js('Olli'), Js('Ollie'), Js('Onyx'), Js('Opie'), Js('Oreo'), Js('Orion'), Js('Orlando'), Js('Oscar'), Js('Ozwald'), Js('Ozzy'), Js('Pablo'), Js('Pacey'), Js('Pacino'), Js('Paddington'), Js('Paddy'), Js('Padfoot'), Js('Palmer'), Js('Pancake'), Js('Panda'), Js('Patch'), Js('Patches'), Js('Patrick'), Js('Paulie'), Js('Peach-O'), Js('Peanut'), Js('Pebbles'), Js('Pepper'), Js('Pepperjack'), Js('Pepsi'), Js('Percy'), Js('Perkins'), Js('Peter Pan'), Js('Pickles'), Js('Pierce'), Js('Pinky'), Js('Pinnochio'), Js('Piper'), Js('Pippin'), Js('Pipsqueak'), Js('Pixie'), Js('Pluto'), Js('Poco Loco'), Js('Pokemon'), Js('Prongs'), Js('Pudding'), Js('Puddles'), Js('Pumbaa'), Js('Pumpkin'), Js('Q-Tip'), Js('Quartz'), Js('Quentin'), Js('Questor'), Js('Quimby'), Js('Quinto'), Js('Quistador'), Js('Quiver'), Js('Raccoo'), Js('Rae'), Js('Rafael'), Js('Raggedy Andy'), Js('Rahjah'), Js('Ralph'), Js('Ralphie'), Js('Random'), Js('Raoul'), Js('Rascal'), Js('Rasta'), Js('Raul'), Js('Razor'), Js('Razzie'), Js('Razzle'), Js('Redding'), Js('Reese'), Js('Remel'), Js('Ren'), Js('Rex'), Js('Ricky'), Js('Riff Raff'), Js('Riley'), Js('Ringo'), Js('Ripley'), Js('Rocco'), Js('Rodman'), Js('Roger'), Js('Romeo'), Js('Ronald'), Js('Ross'), Js('Rowan'), Js('Rox'), Js('Royal'), Js('Ruben'), Js('Rudykins'), Js('Ruffles'), Js('Rufus'), Js('Rumbles'), Js('Ryder'), Js('Saber Tooth'), Js('Saint Paw'), Js('Salt'), Js('Salty'), Js('Sam'), Js('Sammy'), Js('Sancho'), Js('Sargent'), Js('Sasquach'), Js('Sassafrass'), Js('Scamper'), Js('Scooter'), Js('Scorpio'), Js('Scrapper'), Js('Scruffy'), Js('Scuba'), Js('Seiko'), Js('Seinfeld'), Js('Seinfield'), Js('Sergei'), Js('Seuss'), Js('Shadow'), Js('Shake'), Js('Shakespeare'), Js('Shamrock'), Js('Shaq'), Js('Sherbert'), Js('Shoe'), Js('Silver'), Js('Silverfoot'), Js('Silvestor'), Js('Simpson'), Js('Skeeter'), Js('Skippy'), Js('Smasher'), Js('Smithers'), Js('Smokey'), Js('Smoky'), Js('Smores'), Js('Smudge'), Js('Sneaky Pete'), Js('Snickers'), Js('Snickerz'), Js('Snoopy'), Js('Snoppy'), Js('Snowball'), Js('Snowdrop'), Js('Snowflake'), Js('Snowman'), Js('Snowy'), Js('Snuggle Bun'), Js('Snuggles'), Js('Socks'), Js('Socrates'), Js('Soldier'), Js('Solomon'), Js('Sonny'), Js('Sorbet'), Js('Spades'), Js('Spaghetti'), Js('Sparky'), Js('Spartacus'), Js('Speedy'), Js('Spice'), Js('Spike'), Js('Spike Spiegal'), Js('Spooky'), Js('Spot'), Js('Sprinkles'), Js('Squeakle'), Js('Squeaky'), Js('Squirt'), Js('Sterling'), Js('Stitch'), Js('Stormie'), Js('Stuart'), Js('Sugar'), Js('Sundance'), Js('Sunny'), Js('Taco'), Js('Talbot'), Js('Tarzan'), Js('Taylor'), Js('Tebow'), Js('Teddy'), Js('Tequila'), Js('Terminator'), Js('Thaddeus'), Js('The Brain'), Js('The Doctor'), Js('The Duke'), Js('Theo'), Js('Theodore'), Js('Thom Thom'), Js('Thumper'), Js('Thunder'), Js('Tiberius'), Js('Tiger'), Js('Tigger'), Js('Timothy'), Js('Tinker'), Js('Titan'), Js('Toby'), Js('Toffee'), Js('Toffy'), Js('Tolstoy'), Js('Tom'), Js('Tomba'), Js('Tomtom'), Js('Topaz'), Js('Trance'), Js('Treacle'), Js('Trekky'), Js('Trembles'), Js('Tricky'), Js('Tripper'), Js('Truman'), Js('Tubby'), Js('Tucker'), Js('Tudball'), Js('Turbo'), Js('Tuts'), Js('Tuxedo'), Js('Tweedle Dee'), Js('Tweedle Dum'), Js('Twinkie'), Js('Tybalt'), Js('Tyler'), Js('Ulysses'), Js('Uncle Buster'), Js('Usher'), Js('Valmont'), Js('Van Gogh'), Js('Van Morrison'), Js('Vanilla'), Js('Vernon'), Js('Vic'), Js('Vince'), Js('Vincent'), Js('Voltaire'), Js('Wabbit'), Js('Wadsworth'), Js('Waffles'), Js('Waldo'), Js('Walnut'), Js('Whisky'), Js('Whitman'), Js('Widget'), Js('Wildling'), Js('Wilfred'), Js('Willie'), Js('Wizzy'), Js('Wolfie'), Js('Woody'), Js('Wozza'), Js('Wycliff'), Js('Xander'), Js('Xavier'), Js('Yeltsin'), Js('Yoda'), Js('Yogi'), Js('Yoshi'), Js('Young Fella'), Js('Yugi'), Js('Yukon'), Js('Zachary'), Js('Zanku'), Js('Zanzibar'), Js('Zen'), Js('Zepplin'), Js('Zeppo'), Js('Zero'), Js('Zeus'), Js('Zig Zag'), Js('Zigfried'), Js('Zippy'), Js('Zoe'), Js('Zoe-Zo'), Js('Zooter'), Js('Zorro'), Js('Zypp')]))
var.put('nm2', Js([Js('Malyumpkin'), Js('8-ball'), Js('Abagail'), Js('Abba'), Js('Abbie'), Js('Abby'), Js('Abel'), Js('Aberdeen'), Js('Abigail'), Js('Able'), Js('Abraham'), Js('Ace'), Js('Acer'), Js('Achemy'), Js('Acker'), Js('Acura'), Js('Adagio'), Js('Adam'), Js('Adele'), Js('Adelina'), Js('Admiral'), Js('Adolfina'), Js('Adoni'), Js('Adriana'), Js('Agatha'), Js('Aki'), Js('Aladdin'), Js('Alaska'), Js('Alastair'), Js('Alex'), Js('Alexander'), Js('Alexandra'), Js('Alexandrea'), Js('Alexandria'), Js('Alf'), Js('Alfi'), Js('Alfie'), Js('Alibi'), Js('Alice'), Js('Allegro'), Js('Alli'), Js('Allie'), Js('Aloysius'), Js('Alpaca'), Js('Alpine'), Js('Amaretto'), Js('Amaya'), Js('Amazon'), Js('Amber'), Js('Ambrosia'), Js('Amethyst'), Js('Amore'), Js('Amorette'), Js('Amy'), Js('Anabell'), Js('Anais'), Js('Anastasia'), Js('Andrea'), Js('Angel'), Js('Angelica'), Js('Angelina'), Js('Angus'), Js('Anna'), Js('Annie'), Js('Aphrodite'), Js('Apollo'), Js('Apple'), Js('Apricot'), Js('Archibald'), Js('Archie'), Js('Aria'), Js('Arial'), Js('Ariel'), Js('Arnie'), Js('Arnold'), Js('Asheton'), Js('Asia'), Js('Aspen'), Js('Asterix'), Js('Astra'), Js('Athena'), Js('Atlas'), Js('Audelia'), Js('Audrey'), Js('August'), Js('Augustus'), Js('Aurora'), Js('Auston'), Js('Autumn'), Js('Babe'), Js('Baby'), Js('Baby girl'), Js('Baldwin'), Js('Bam bam'), Js('Bambi'), Js('Bamboo'), Js('Banana'), Js('Bandi'), Js('Barbie'), Js('Barley'), Js('Barnaby'), Js('Barnacle'), Js('Barney'), Js('Bartholomew'), Js('Basil'), Js('Basket'), Js('Bazooka'), Js('Beatrice'), Js('Beauty'), Js('Bebe'), Js('Beefeater'), Js('Beethoven'), Js('Bell'), Js('Bella'), Js('Belle'), Js('Bentley'), Js('Bess'), Js('Bessie'), Js('Bessy'), Js('Bianca'), Js('Big Mama'), Js('Bijou'), Js('Binky'), Js('Biscuit'), Js('Bishop'), Js('Blackie'), Js('Blake'), Js('Blanco'), Js('Bliss'), Js('Blossom'), Js('Bobby'), Js('Bonita'), Js('Bonnie'), Js('Boo Boo'), Js('Boris'), Js('Boston'), Js('Boy'), Js('Brandy'), Js('Brie'), Js('Britannia'), Js('Brooke'), Js('Brownie'), Js('Bruce'), Js('Bruno'), Js('Bryani'), Js('Bubbles'), Js('Bud'), Js('Buffy'), Js('Bug'), Js('Bugatti'), Js('Bumper'), Js('Burgundy'), Js('Busker'), Js('Butler'), Js('Butter'), Js('Buttercup'), Js('Butternut'), Js('Butterscotch'), Js('Button'), Js('Buttons'), Js('Cadet'), Js('Cadi'), Js('Caesar'), Js('Cajun'), Js('Calia'), Js('Callie'), Js('Calvin'), Js('Calypso'), Js('Camembert'), Js('Camilla'), Js('Candi'), Js('Candice'), Js('Candy'), Js('Captain Marvel'), Js('Caramel'), Js('Carissa'), Js('Carolina'), Js('Carrie'), Js('Casanova'), Js('Cashew'), Js('Cass'), Js('Cassie'), Js('Cati'), Js('Cayenne'), Js('Celeste'), Js('Cha Cha'), Js('Chakra'), Js('Chanel'), Js('Chantilly'), Js('Charity'), Js('Charlie'), Js('Charlotte'), Js('Cheerio'), Js('Cheesecake'), Js('Chelsea'), Js('Chelsey'), Js('Chelsie'), Js('Cheri'), Js('Cherry'), Js('Cherub'), Js('Chic'), Js('Chichi'), Js('Chiclet'), Js('Chilli'), Js('China'), Js('Chloe'), Js('Chocolate'), Js('Cilla'), Js('Cinderella'), Js('Cinders'), Js('Cindy'), Js('Cinnamon'), Js('Claret'), Js('Claudia'), Js('Clementine'), Js('Cleopatra'), Js('Cloudy'), Js('Clover'), Js('Coco'), Js('Cocoa'), Js('Coffee'), Js('Colette'), Js('Collin'), Js('Colonel'), Js('Comet'), Js('Connie'), Js('Contessa'), Js('Cooboo'), Js('Cookie'), Js('Copper'), Js('Coral'), Js('Cornflake'), Js('Cotton'), Js('Cottonball'), Js('Cottontail'), Js('Countess'), Js('Courtney'), Js('Cous Cous'), Js('Cream Puff'), Js('Crimson'), Js('Crouton'), Js('Crystal'), Js('Cuddles'), Js('Cupcake'), Js('Curly'), Js('Cutie'), Js('Cutsie'), Js('Daffodil'), Js('Dahlia'), Js('Daisy'), Js('Daisy Duke'), Js('Dakota'), Js('Dandelion'), Js('Dani'), Js('Danni'), Js('Darcey'), Js('Darla'), Js('Darlene'), Js('Darling'), Js('Decaf'), Js('Delilah'), Js('Desiree'), Js('Destiny'), Js('Diamond'), Js('Dinah'), Js('Dinky'), Js('Dior'), Js('Dixie'), Js('Dolly'), Js('Dot'), Js('Duchess'), Js('Duffie'), Js('Eden'), Js('Ella'), Js('Elle'), Js('Ellie'), Js('Elsa'), Js('Elsi'), Js('Elvira'), Js('Emily'), Js('Emma'), Js('Emmy'), Js('Enya'), Js('Evita'), Js('Faith'), Js('Fancy'), Js('Fanjo'), Js('Felicity'), Js('Fern'), Js('Fifi'), Js('Flip-Flop'), Js('Flopsy'), Js('Florence'), Js('Flower'), Js('Fluffer'), Js('Fluffy'), Js('Fluffykins'), Js('Foo Foo'), Js('Fraidy'), Js('Francesca'), Js('Frankie'), Js('Friskie'), Js('Fudge'), Js('Furball'), Js('Furby'), Js('Gabby'), Js('Gavin'), Js('Gemini'), Js('Gemma'), Js('Genevere'), Js('Georgie'), Js('Gidget'), Js('Giggles'), Js('Gigi'), Js('Ginger'), Js('Ginny'), Js('Goblin'), Js('Godiva'), Js('Goldie'), Js('Goldilocks'), Js('Gomez'), Js('Gouda'), Js('Grace'), Js('Gracie'), Js('Gremlin'), Js('Grendel'), Js('Gringo'), Js('Gucci'), Js('Gugu'), Js('Gunther'), Js('Gypsy'), Js('Haanah'), Js('Hallie'), Js('Halo'), Js('Hamlet'), Js('Hannah'), Js('Harlow'), Js('Harmony'), Js('Harold'), Js('Harriet'), Js('Harry'), Js('Hayley'), Js('Hazel'), Js('Hector'), Js('Heidi'), Js('Herbie'), Js('Herman'), Js('Hilary'), Js('Hissy'), Js('Holly'), Js('Honey'), Js('Hope'), Js('Hosanna'), Js('Iris'), Js('Isabelle'), Js('Ivy'), Js('Jacina'), Js('Jackie O'), Js('Jada'), Js('Jade'), Js('Jake'), Js('Jana'), Js('Jane'), Js('Jasmine'), Js('Jazebel'), Js('Jazmin'), Js('Jeannie'), Js('Jelly Babe'), Js('Jemima'), Js('Jena'), Js('Jeners'), Js('Jersey'), Js('Jessee'), Js('Jessie'), Js('Jewel'), Js('Jilly'), Js('Jinxy'), Js('Jipsee'), Js('Jitterbug'), Js('Jiya'), Js('Jolie'), Js('Jordon'), Js('Joy'), Js('Judy'), Js('Julie'), Js('Juliet'), Js('Julina'), Js('June Bug'), Js('Juniper'), Js('Justine'), Js('Juya'), Js('Kabuki'), Js('Kacee'), Js('Kaelyn'), Js('Kalynn'), Js('Kasey Jo'), Js('Katie'), Js('Kava'), Js('Kelly'), Js('Kelsie-Jo'), Js('Kenya'), Js('Kia'), Js('Kimmy'), Js('Kiss Kiss'), Js('Kisses'), Js('Kivi'), Js('Kiwi'), Js('Koda'), Js('Kokomo'), Js('Kookaburra'), Js('Lacey'), Js('Lacy'), Js('Lady'), Js('Lady Luv'), Js('Ladybug'), Js('Latte'), Js('Lavender'), Js('Layla'), Js('Lcy'), Js('Leah'), Js('Lena'), Js('Lexus'), Js('Libby'), Js('Licorice'), Js('Lil One'), Js('Lilac'), Js('Lilli'), Js('Lillian'), Js('Lilly'), Js('Lily'), Js('Linda'), Js('Little Bit'), Js('Lola'), Js('Lollypop'), Js('Lorelei'), Js('Lori'), Js('Louisa'), Js('Lovebug'), Js('Lucille'), Js('Lulu'), Js('Luna'), Js('Macaulay'), Js('Macbeth'), Js('Mackenzie'), Js('Maddie'), Js('Magdalina'), Js('Magenta'), Js('Maggi'), Js('Majesty'), Js('Maren'), Js('Margie'), Js('Margo'), Js('Marigold'), Js('Marilyn'), Js('Marshmellow'), Js('Maryann'), Js('Maverick'), Js('McFluffy'), Js('McFluffykins'), Js('Meatloaf'), Js('Medley'), Js('Meeka'), Js('Meesha'), Js('Meg'), Js('Megan'), Js('Mercedes'), Js('Merry'), Js('Mertise'), Js('Micah'), Js('Midget'), Js('Millie'), Js('Milly'), Js('Mimi'), Js('Mimsy'), Js('Minal'), Js('Mini'), Js('Minsky'), Js('Minty'), Js('Miranda'), Js('Miss Lily'), Js('Miss Muffet'), Js('Miss Take'), Js('Misty'), Js('Mittens'), Js('Mitz'), Js('Mocha'), Js('Molly'), Js('Mon Ami'), Js('Mona'), Js('Monique'), Js('Montaine'), Js('Montana'), Js('Mopsy'), Js('Morgan'), Js('Morris'), Js('Morticia'), Js('Moses'), Js('Mozart'), Js('Muffin'), Js('Murphy'), Js('Mya'), Js('Mystique'), Js('Nadia'), Js('Nana'), Js('Nancy'), Js('Naomi'), Js('Napoleon'), Js('Natali'), Js('Natasha'), Js('Nathan'), Js('Nayla'), Js('Ned'), Js('Neddy'), Js('Neela'), Js('Nellie'), Js('Nibbles'), Js('Nijinsky'), Js('Nikia'), Js('Nitska'), Js('Noelle'), Js('Noisette'), Js('Nokky'), Js('Noni'), Js('Noodle Bug'), Js('Noodles'), Js('Nugget'), Js('Nutmeg'), Js('Oasis'), Js('Oatmeal'), Js('Obelix'), Js('Odette'), Js('Olga'), Js('Olive'), Js('Olivia'), Js('Olivier'), Js('Orlando'), Js('Ozwald'), Js('Pablo'), Js('Pacino'), Js('Paddington'), Js('Paddy'), Js('Paisley'), Js('Pancake'), Js('Pandora'), Js('Pansy'), Js('Paprika'), Js('Paris'), Js('Patch'), Js('Patches'), Js('Peaches'), Js('Peachy'), Js('Peanut'), Js('Peapod'), Js('Pearl'), Js('Pebbles'), Js('Peepers'), Js('Peggy'), Js('Penelope'), Js('Penny'), Js('Peppa'), Js('Pepsi'), Js('Percy'), Js('Periwinkle'), Js('Petra'), Js('Petunia'), Js('Phebe'), Js('Piglet'), Js('Pip'), Js('Piper'), Js('Pixie'), Js('Polly'), Js('Pookie'), Js('Popcorn'), Js('Poppins'), Js('Poppy'), Js('Precious'), Js('Princess'), Js('Priscilla'), Js('Providence'), Js('Pudding'), Js('Puddles'), Js('Pumpkin'), Js('Quacker'), Js('Queenie'), Js('Rachel'), Js('Radiance'), Js('Ramsey'), Js('Razzie'), Js('Reba'), Js('Rebecca'), Js('Regan'), Js('Renee'), Js('Ribbon'), Js('Rizzo'), Js('Robertia'), Js('Rocco'), Js('Roni'), Js('Ronnie'), Js('Rose'), Js('Rosebud'), Js('Rosemary'), Js('Rosetta'), Js('Rosie'), Js('Ross'), Js('Rossini'), Js('Rosy'), Js('Rowan'), Js('Rowena'), Js('Roxanne'), Js('Roxy'), Js('Royal'), Js('Roz'), Js('Ru’Bella'), Js('Ruben'), Js('Ruby'), Js('Ruby Jean'), Js('Ruffles'), Js('Rufus'), Js('Ruth'), Js('Ruthie'), Js('Ryanne'), Js('Sabrina'), Js('Sabrina Snow'), Js('Sadie'), Js('Sahara'), Js('Sally'), Js('Salty'), Js('Sam'), Js('Sami Girl'), Js('Sammy'), Js('Sandie'), Js('Sandy'), Js('Sapphire'), Js('Sarafina'), Js('Sasha'), Js('Sassy'), Js('Sassy Pants'), Js('Satine'), Js('Savannah'), Js('Scampi'), Js('Scarlet'), Js('Scruffy'), Js('Scuba'), Js('Selby'), Js('Selena'), Js('Sephora'), Js('Serena'), Js('Serenity'), Js('Shawnee'), Js('Sheena'), Js('Sheridan'), Js('Shirley Temple'), Js('Shona'), Js('Short Cake'), Js('Sierra'), Js('Silly Sidney'), Js('Silvie'), Js('Sissy'), Js('Skittles'), Js('Skyler'), Js('Slippers'), Js('Smithers'), Js('Smokey'), Js('Smudge'), Js('Snickerdoodle'), Js('Snickers'), Js('Snoppy'), Js('Snowflake'), Js('Snowman'), Js('Snowy'), Js('Socrates'), Js('Sofia'), Js('Soldier'), Js('Solomon'), Js('Sophia'), Js('Sophie'), Js('Sorbet'), Js('Spades'), Js('Sparkles'), Js('Spazzy'), Js('Spooky'), Js('Spot'), Js('Sprinkles'), Js('Spunkie Girl'), Js('Starbuck'), Js('Steletto'), Js('Stella'), Js('Stevie'), Js('Stormie'), Js('Stormy'), Js('Strawberry'), Js('Stripe'), Js('Suga'), Js('Sugar'), Js('Suzie Q'), Js('Sweet Pea'), Js('Sweetie'), Js('Sweetie Pie'), Js('Sweetpea'), Js('Swiss Miss'), Js('Symphony'), Js('Tabitha'), Js('Taffy'), Js('Talia'), Js('Tammy'), Js('Tashie'), Js('Tawney'), Js('Teela'), Js('Teeney'), Js('Tequila'), Js('Tess'), Js('Tessa'), Js('Thelma'), Js('Thumbelina'), Js('Thunder'), Js('Tia Maria'), Js('Tibby'), Js('Tiddly Wink'), Js('Tiffanie'), Js('Tigger'), Js('Tilly'), Js('Tina'), Js('Tinker Bell'), Js('Tinker Belle'), Js('Tinkerbell'), Js('Tinsel'), Js('Tipsy'), Js('Titan'), Js('Toast'), Js('Toffee'), Js('Tomba'), Js('Tomtom'), Js('Toots'), Js('Tori'), Js('Tortelini'), Js('Tottie'), Js('Tracy'), Js('Treacle'), Js('Tricky'), Js('Triscuit'), Js('Trudi'), Js('Truffle'), Js('Tula Rose'), Js('Tulip'), Js('Tumble'), Js('Tutti Fruti'), Js('Tweetie Pie'), Js('Tweety'), Js('Twig'), Js('Twinkie'), Js('Twinkle'), Js('Twinkle Toes'), Js('Una'), Js('Val'), Js('Valentine'), Js('Vanilla'), Js('Velvet'), Js('Venus'), Js('Vera'), Js('Vicky'), Js('Violet'), Js('Vivica'), Js('Waffles'), Js('Walnut'), Js('Wana'), Js('Wanda'), Js('Wendy'), Js('Whisky'), Js('Whoopie'), Js('Widget'), Js('Willow'), Js('Winnie'), Js('Xena'), Js('Yoda'), Js('Yvonne'), Js('Zadora'), Js('Zeldabar'), Js('Zia Marie'), Js('Zig Zag'), Js('Zoe'), Js('Zoey'), Js('Zola'), Js('Zula'), Js('Zuzu')]))
pass
pass


# Add lib to the module scope
rabbitPets = var.to_python()