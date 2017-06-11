__all__ = ['musicianNames']

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
    var.registers(['nm1', 'nm4', 'nm5', 'type', 'nm3', 'tp', 'nm2', 'result'])
    var.put('nm1', Js([Js('Aaron'), Js('Adam'), Js('Adrian'), Js('Alan'), Js('Albert'), Js('Alec'), Js('Alek'), Js('Alex'), Js('Alexander'), Js('Alfred'), Js('Allan'), Js('Allen'), Js('Alvin'), Js('Andre'), Js('Andrew'), Js('Angel'), Js('Anthony'), Js('Arnold'), Js('Art'), Js('Arthur'), Js('Ash'), Js('Ashton'), Js('Austin'), Js('Barry'), Js('Ben'), Js('Benjamin'), Js('Benji'), Js('Bennie'), Js('Benny'), Js('Bernard'), Js('Bert'), Js('Bill'), Js('Billie'), Js('Billy'), Js('Blake'), Js('Bob'), Js('Bobbie'), Js('Bobby'), Js('Brad'), Js('Bradley'), Js('Brandon'), Js('Brendan'), Js('Brent'), Js('Brett'), Js('Brian'), Js('Brody'), Js('Bruce'), Js('Bryan'), Js('Calvin'), Js('Cameron'), Js('Carl'), Js('Carter'), Js('Casey'), Js('Chad'), Js('Charles'), Js('Charley'), Js('Charlie'), Js('Chase'), Js('Chester'), Js('Chris'), Js('Christian'), Js('Christopher'), Js('Clyde'), Js('Cody'), Js('Cole'), Js('Colin'), Js('Collin'), Js('Conner'), Js('Connor'), Js('Cooper'), Js('Corey'), Js('Craig'), Js('Criss'), Js('Cristian'), Js('Dale'), Js('Damian'), Js('Damon'), Js('Dan'), Js('Daniel'), Js('Dannie'), Js('Danny'), Js('Darren'), Js('Darryl'), Js('Daryl'), Js('Dave'), Js('David'), Js('Dean'), Js('Dennis'), Js('Derek'), Js('Devin'), Js('Don'), Js('Donald'), Js('Donnie'), Js('Donny'), Js('Drew'), Js('Duane'), Js('Dustin'), Js('Dwayne'), Js('Dwight'), Js('Dylan'), Js('Earl'), Js('Ed'), Js('Edd'), Js('Eddie'), Js('Eddy'), Js('Edgar'), Js('Edward'), Js('Edwin'), Js('Elias'), Js('Eric'), Js('Erik'), Js('Ernest'), Js('Ethan'), Js('Even'), Js('Felix'), Js('Floyd'), Js('Francis'), Js('Frank'), Js('Frankie'), Js('Franklin'), Js('Fred'), Js('Freddie'), Js('Freddy'), Js('Garry'), Js('Gary'), Js('Gavin'), Js('Gene'), Js('George'), Js('Gerald'), Js('Gerard'), Js('Glen'), Js('Gordon'), Js('Grant'), Js('Greg'), Js('Gregory'), Js('Guy'), Js('Harold'), Js('Harry'), Js('Harvey'), Js('Hector'), Js('Henry'), Js('Herman'), Js('Hognny'), Js('Howard'), Js('Hubert'), Js('Hugh'), Js('Hunter'), Js('Ian'), Js('Irvin'), Js('Isaac'), Js('Ivan'), Js('Jack'), Js('Jackie'), Js('Jackson'), Js('Jacob'), Js('Jake'), Js('James'), Js('Jamie'), Js('Jared'), Js('Jason'), Js('Jay'), Js('Jeff'), Js('Jeffrey'), Js('Jeremy'), Js('Jerry'), Js('Jesse'), Js('Jessie'), Js('Jim'), Js('Jimmie'), Js('Jimmy'), Js('Joe'), Js('Joel'), Js('John'), Js('Johnathan'), Js('Johnnie'), Js('Jonah'), Js('Jordan'), Js('Joseph'), Js('Junior'), Js('Justin'), Js('Karl'), Js('Keith'), Js('Kevin'), Js('Kirk'), Js('Kris'), Js('Kurt'), Js('Kyle'), Js('Lance'), Js('Larry'), Js('Lee'), Js('Leo'), Js('Leonard'), Js('Leonardo'), Js('Leslie'), Js('Lester'), Js('Lewis'), Js('Liam'), Js('Logan'), Js('Louis'), Js('Lucas'), Js('Luke'), Js('Mack'), Js('Marc'), Js('Marcus'), Js('Mark'), Js('Martin'), Js('Marvin'), Js('Matthew'), Js('Max'), Js('Maxwell'), Js('Michael'), Js('Mike'), Js('Morris'), Js('Nathan'), Js('Neil'), Js('Nicholas'), Js('Nick'), Js('Nicolas'), Js('Noah'), Js('Oliver'), Js('Oscar'), Js('Owen'), Js('Patrick'), Js('Paul'), Js('Perry'), Js('Pete'), Js('Peter'), Js('Philip'), Js('Phillip'), Js('Ralph'), Js('Randy'), Js('Ray'), Js('Raymond'), Js('Rex'), Js('Richard'), Js('Rick'), Js('Ricky'), Js('Robert'), Js('Robin'), Js('Roger'), Js('Roland'), Js('Ronald'), Js('Roscoe'), Js('Ross'), Js('Ruben'), Js('Russell'), Js('Ryan'), Js('Sam'), Js('Samuel'), Js('Scott'), Js('Sean'), Js('Seth'), Js('Shane'), Js('Shawn'), Js('Stan'), Js('Stanley'), Js('Stephen'), Js('Steve'), Js('Steven'), Js('Stuart'), Js('Ted'), Js('Teddie'), Js('Teddy'), Js('Terrence'), Js('Terry'), Js('Theo'), Js('Thomas'), Js('Tim'), Js('Timmy'), Js('Timothy'), Js('Todd'), Js('Tom'), Js('Tommy'), Js('Tony'), Js('Travis'), Js('Trevor'), Js('Tyler'), Js('Victor'), Js('Vincent'), Js('Walter'), Js('Wayne'), Js('Will'), Js('William'), Js('Zach')]))
    var.put('nm2', Js([Js('Abby'), Js('Addison'), Js('Adriana'), Js('Adrienne'), Js('Aimee'), Js('Alana'), Js('Alexa'), Js('Alexia'), Js('Alexis'), Js('Alice'), Js('Alicia'), Js('Alisha'), Js('Allison'), Js('Amanda'), Js('Amber'), Js('Amee'), Js('Amy'), Js('Ana'), Js('Angela'), Js('Angelina'), Js('Anita'), Js('Ann'), Js('Anna'), Js('Anne'), Js('Annie'), Js('Arianna'), Js('Ariel'), Js('Ashlee'), Js('Ashley'), Js('Ava'), Js('Avery'), Js('Barbara'), Js('Becky'), Js('Beth'), Js('Bethany'), Js('Betty'), Js('Bonnie'), Js('Brandy'), Js('Briana'), Js('Bridget'), Js('Brittany'), Js('Brooke'), Js('Caitlyn'), Js('Camilla'), Js('Carly'), Js('Carmen'), Js('Carol'), Js('Carolyn'), Js('Casey'), Js('Cassie'), Js('Cathy'), Js('Charlotte'), Js('Chelsea'), Js('Cheryl'), Js('Chloe'), Js('Christina'), Js('Christine'), Js('Christy'), Js('Cindy'), Js('Claire'), Js('Clara'), Js('Courtney'), Js('Daisy'), Js('Dana'), Js('Daniel'), Js('Danielle'), Js('Dawn'), Js('Debbie'), Js('Debra'), Js('Denise'), Js('Desiree'), Js('Diana'), Js('Diane'), Js('Donna'), Js('Dora'), Js('Dorothy'), Js('Edit'), Js('Eileen'), Js('Elizabeth'), Js('Elize'), Js('Ella'), Js('Ellen'), Js('Ellie'), Js('Elsie'), Js('Emily'), Js('Emma'), Js('Erica'), Js('Erika'), Js('Erin'), Js('Esther'), Js('Eva'), Js('Evelyn'), Js('Faith'), Js('Faye'), Js('Georgia'), Js('Gianna'), Js('Gina'), Js('Gloria'), Js('Grace'), Js('Gracie'), Js('Hailey'), Js('Haley'), Js('Hanna'), Js('Hannah'), Js('Hazel'), Js('Heather'), Js('Helen'), Js('Hope'), Js('Irene'), Js('Isabel'), Js('Iva'), Js('Ivy'), Js('Jackie'), Js('Jade'), Js('Jamie'), Js('Jane'), Js('Janet'), Js('Jasmin'), Js('Jean'), Js('Jenna'), Js('Jennie'), Js('Jennifer'), Js('Jenny'), Js('Jessie'), Js('Jo'), Js('Joan'), Js('Joanne'), Js('Jody'), Js('Jordan'), Js('Jordyn'), Js('Joy'), Js('Joyce'), Js('Judith'), Js('Judy'), Js('Julia'), Js('Julie'), Js('June'), Js('Kaitlyn'), Js('Karen'), Js('Karla'), Js('Kate'), Js('Katelyn'), Js('Kathy'), Js('Katie'), Js('Kay'), Js('Kaylee'), Js('Kelli'), Js('Kellie'), Js('Kelly'), Js('Kelsey'), Js('Kendra'), Js('Kerry'), Js('Kim'), Js('Kimberly'), Js('Kirsten'), Js('Krista'), Js('Kristen'), Js('Kristie'), Js('Kristina'), Js('Kristine'), Js('Kylie'), Js('Laura'), Js('Lauren'), Js('Lea'), Js('Leah'), Js('Lela'), Js('Lena'), Js('Leona'), Js('Lila'), Js('Lilian'), Js('Liliana'), Js('Lilly'), Js('Lily'), Js('Linda'), Js('Lindsay'), Js('Lindsey'), Js('Lisa'), Js('Lizzie'), Js('Lola'), Js('Lori'), Js('Lottie'), Js('Louise'), Js('Lucy'), Js('Lynda'), Js('Lynn'), Js('Madelyn'), Js('Madison'), Js('Mae'), Js('Maggie'), Js('Mandy'), Js('Maria'), Js('Mariah'), Js('Marie'), Js('Marion'), Js('Marisa'), Js('Marlene'), Js('Mary'), Js('May'), Js('Maya'), Js('Megan'), Js('Melinda'), Js('Melissa'), Js('Melody'), Js('Mia'), Js('Michele'), Js('Michelle'), Js('Mindy'), Js('Miriam'), Js('Misty'), Js('Molly'), Js('Monica'), Js('Morgan'), Js('Mya'), Js('Nancy'), Js('Naomi'), Js('Natalie'), Js('Nichole'), Js('Nicole'), Js('Nina'), Js('Nora'), Js('Olivia'), Js('Opal'), Js('Pamela'), Js('Pauline'), Js('Pearl'), Js('Peggy'), Js('Penny'), Js('Rachel'), Js('Raven'), Js('Reagon'), Js('Rebecca'), Js('Renee'), Js('Robin'), Js('Robyn'), Js('Rose'), Js('Rosie'), Js('Ruby'), Js('Ruth'), Js('Sally'), Js('Sam'), Js('Samantha'), Js('Sandra'), Js('Sandy'), Js('Sara'), Js('Sarah'), Js('Selena'), Js('Selene'), Js('Serenity'), Js('Shannon'), Js('Sharon'), Js('Skylar'), Js('Sofia'), Js('Sonya'), Js('Sophie'), Js('Stacey'), Js('Stacie'), Js('Stacy'), Js('Stefanie'), Js('Sue'), Js('Summer'), Js('Susan'), Js('Susie'), Js('Sydney'), Js('Tanya'), Js('Tara'), Js('Taylor'), Js('Tina'), Js('Tracie'), Js('Trinity'), Js('Valerie'), Js('Veronica'), Js('Vickie'), Js('Vicky'), Js('Victoria'), Js('Viola'), Js('Violet'), Js('Vivian'), Js('Wendy'), Js('Zoe'), Js('Zoey')]))
    var.put('nm3', Js([Js('Ace'), Js('Adams'), Js('Alexander'), Js('Allen'), Js('Anderson'), Js('Angel'), Js('Apollo'), Js('Argo'), Js('Arthur'), Js('Ash'), Js('Ashley'), Js('Austin'), Js('B'), Js('Baker'), Js('Ball'), Js('Banks'), Js('Banner'), Js('Barrett'), Js('Barron'), Js('Barrymore'), Js('Bear'), Js('Bell'), Js('Bennett'), Js('Berrymore'), Js('Bert'), Js('Birch'), Js('Bishop'), Js('Black'), Js('Blade'), Js('Blake'), Js('Bloom'), Js('Blue'), Js('Bolt'), Js('Bone'), Js('Bones'), Js('Brandon'), Js('Bravo'), Js('Brooke'), Js('Brooks'), Js('Brown'), Js('Bruce'), Js('Button'), Js('Cage'), Js('Caine'), Js('Call'), Js('Cameron'), Js('Cannon'), Js('Carol'), Js('Carr'), Js('Carroll'), Js('Carter'), Js('Castle'), Js('Chandler'), Js('Charles'), Js('Chase'), Js('Child'), Js('Christy'), Js('Claire'), Js('Clare'), Js('Clark'), Js('Clay'), Js('Cliff'), Js('Cole'), Js('Coleman'), Js('Colt'), Js('Cooper'), Js('Cotton'), Js('Cougar'), Js('Coyote'), Js('Craig'), Js('Crane'), Js('Crash'), Js('Cross'), Js('Dale'), Js('Dane'), Js('Dare'), Js('Dark'), Js('Darrow'), Js('David'), Js('Davis'), Js('Dawn'), Js('Day'), Js('Dee'), Js('Dell'), Js('Diamond'), Js('Douglas'), Js('Drake'), Js('Dreamer'), Js('Duff'), Js('Duke'), Js('Duncan'), Js('Dusk'), Js('Earl'), Js('East'), Js('Edwards'), Js('Elliot'), Js('Ellis'), Js('Evans'), Js('Everett'), Js('Faire'), Js('Faith'), Js('Fame'), Js('Fawn'), Js('Fay'), Js('Fields'), Js('Fierce'), Js('Ford'), Js('Forrest'), Js('Foster'), Js('Fox'), Js('Freedom'), Js('Gale'), Js('Gates'), Js('Gear'), Js('George'), Js('Gibbs'), Js('Gibson'), Js('Gilmore'), Js('Gordon'), Js('Grant'), Js('Graves'), Js('Gray'), Js('Green'), Js('Griffin'), Js('Hale'), Js('Hammer'), Js('Hammond'), Js('Harris'), Js('Havoc'), Js('Hawk'), Js('Hill'), Js('Holmes'), Js('Holt'), Js('Howard'), Js('Hunter'), Js('Iris'), Js('Isle'), Js('Ivory'), Js('Jackson'), Js('James'), Js('Jason'), Js('Jay'), Js('Jet'), Js('Johnson'), Js('Jones'), Js('Jordan'), Js('Josh'), Js('Joy'), Js('Joyce'), Js('Kane'), Js('Keith'), Js('Kennedy'), Js('Kerry'), Js('Keys'), Js('Khan'), Js('Kidd'), Js('King'), Js('Kingsley'), Js('Kiss'), Js('Kitt'), Js('Knight'), Js('Kole'), Js('Laine'), Js('Lake'), Js('Law'), Js('Lawrence'), Js('Legend'), Js('Leigh'), Js('Leo'), Js('Lewis'), Js('Light'), Js('Little'), Js('Living'), Js('Livingston'), Js('Lloyd'), Js('Locke'), Js('Logan'), Js('Lord'), Js('Love'), Js('Lover'), Js('Lynn'), Js('Mac'), Js('Mack'), Js('Madison'), Js('Man'), Js('Mann'), Js('March'), Js('Mars'), Js('Marsh'), Js('Marshall'), Js('Martin'), Js('May'), Js('Mell'), Js('Mercury'), Js('Merrill'), Js('Michaels'), Js('Miles'), Js('Mill'), Js('Miller'), Js('Mitchell'), Js('Money'), Js('Moon'), Js('Moore'), Js('Morgan'), Js('Murray'), Js('Mythic'), Js('Nash'), Js('Nelson'), Js('Neptune'), Js('Nicholas'), Js('Nixon'), Js('Noble'), Js('Nolan'), Js('North'), Js('Nova'), Js('Nye'), Js('Ocean'), Js('Oliver'), Js('Orange'), Js('Oz'), Js('Page'), Js('Paige'), Js('Palmer'), Js('Park'), Js('Parker'), Js('Parrish'), Js('Patrick'), Js('Paul'), Js('Pearl'), Js('Penn'), Js('Perry'), Js('Philips'), Js('Phoenix'), Js('Pink'), Js('Powell'), Js('Powers'), Js('Price'), Js('Prince'), Js('Quest'), Js('Raine'), Js('Ramone'), Js('Ray'), Js('Red'), Js('Reed'), Js('Reign'), Js('Rex'), Js('Rey'), Js('Rhodes'), Js('Rich'), Js('Rider'), Js('Roads'), Js('Roberts'), Js('Robinson'), Js('Rock'), Js('Rogers'), Js('Rose'), Js('Ross'), Js('Roth'), Js('Russell'), Js('Ryan'), Js('Rye'), Js('Samson'), Js('Sawyer'), Js('Scott'), Js('Seymour'), Js('Shannon'), Js('Shawn'), Js('Shepherd'), Js('Sierra'), Js('Silver'), Js('Silvers'), Js('Sinclair'), Js('Sky'), Js('Skye'), Js('Smith'), Js('South'), Js('Spacey'), Js('Spencer'), Js('Spice'), Js('Springfield'), Js('Stanley'), Js('Star'), Js('Stark'), Js('Starr'), Js('Steele'), Js('Sterling'), Js('Stevens'), Js('Stewart'), Js('Stone'), Js('Storm'), Js('Strange'), Js('Strong'), Js('Summers'), Js('Swift'), Js('Tanner'), Js('Taylor'), Js('Tempest'), Js('Terris'), Js('Thomas'), Js('Thompson'), Js('Todd'), Js('Travis'), Js('Tucker'), Js('Turner'), Js('Tyler'), Js('Vale'), Js('Valentine'), Js('Vance'), Js('Ventura'), Js('Vice'), Js('Victor'), Js('Walker'), Js('Wallace'), Js('Waters'), Js('Wayne'), Js('Webb'), Js('Wells'), Js('West'), Js('White'), Js('Wilde'), Js('Williams'), Js('Winter'), Js('Winters'), Js('Wolf'), Js('Wood'), Js('Woods'), Js('Worth'), Js('Young')]))
    var.put('nm4', Js([Js('Aaren'), Js('Addison'), Js('Aiden'), Js('Alex'), Js('Alexis'), Js('Ali'), Js('Angel'), Js('Ash'), Js('Ashley'), Js('Ashton'), Js('Aubrey'), Js('Avery'), Js('Bailey'), Js('Bennie'), Js('Bev'), Js('Billie'), Js('Billy'), Js('Blair'), Js('Blake'), Js('Bret'), Js('Brett'), Js('Brice'), Js('Brook'), Js('Brynn'), Js('Caden'), Js('Cameron'), Js('Carmen'), Js('Carol'), Js('Casey'), Js('Charlie'), Js('Chris'), Js('Clem'), Js('Cory'), Js('Dane'), Js('Danni'), Js('Danny'), Js('Denny'), Js('Drew'), Js('Eli'), Js('Elliot'), Js('Emerson'), Js('Erin'), Js('Fran'), Js('Frankie'), Js('Franky'), Js('Gabby'), Js('Gabe'), Js('Gail'), Js('Gale'), Js('Gene'), Js('Glen'), Js('Glenn'), Js('Haiden'), Js('Harley'), Js('Harper'), Js('Hayden'), Js('Jackie'), Js('Jaden'), Js('Jaime'), Js('Jamie'), Js('Jess'), Js('Jesse'), Js('Jessie'), Js('Jo'), Js('Jody'), Js('Jordan'), Js('Jude'), Js('Justice'), Js('Kai'), Js('Kerry'), Js('Kiran'), Js('Kit'), Js('Kris'), Js('Lane'), Js('Lee'), Js('Leigh'), Js('Lesley'), Js('Leslie'), Js('Logan'), Js('Lynn'), Js('Maddox'), Js('Marley'), Js('Mason'), Js('Mel'), Js('Mell'), Js('Morgan'), Js('Nicky'), Js('Noel'), Js('Phoenix'), Js('Quinn'), Js('Ray'), Js('Raylee'), Js('Reed'), Js('Reggie'), Js('Rene'), Js('Riley'), Js('River'), Js('Robin'), Js('Rory'), Js('Rowan'), Js('Rudy'), Js('Ryan'), Js('Sam'), Js('Sammy'), Js('Shay'), Js('Sidney'), Js('Silver'), Js('Skye'), Js('Skylar'), Js('Skyler'), Js('Steff'), Js('Tanner'), Js('Taylor'), Js('Terry'), Js('Tyler'), Js('Val'), Js('Vic'), Js('Will'), Js('Willy')]))
    var.put('nm5', Js([Js('Angel'), Js('Animal'), Js('Aspect'), Js('Awe'), Js('Axis'), Js('Badger'), Js('Base'), Js('Bass'), Js('Bear'), Js('Bird'), Js('Bizarre'), Js('Blade'), Js('Blaze'), Js('Blue'), Js('Blush'), Js('Boar'), Js('Bogus'), Js('Boss'), Js('Brash'), Js('Brass'), Js('Brawn'), Js('Brick'), Js('Buddy'), Js('Cage'), Js('Cannon'), Js('Case'), Js('Cash'), Js('Cell'), Js('Chain'), Js('Chains'), Js('Chaos'), Js('Chase'), Js('Cloud'), Js('Coal'), Js('Coil'), Js('Cord'), Js('Crash'), Js('Crib'), Js('Crime'), Js('Crow'), Js('Curves'), Js('Darkness'), Js('Doc'), Js('Edge'), Js('Ego'), Js('Electric'), Js('Enigma'), Js('Envy'), Js('Escape'), Js('Face'), Js('Fade'), Js('Fang'), Js('Fangs'), Js('Fire'), Js('Flame'), Js('Flock'), Js('Flow'), Js('Flux'), Js('Fog'), Js('Force'), Js('Ghost'), Js('Gold'), Js('Green'), Js('Groef'), Js('Habit'), Js('Harm'), Js('Heart'), Js('Horn'), Js('Ice'), Js('Impulse'), Js('Ink'), Js('Iron'), Js('Jacket'), Js('Jade'), Js('Jewel'), Js('Judge'), Js('Justice'), Js('Kid'), Js('Kite'), Js('Legion'), Js('Life'), Js('Light'), Js('Link'), Js('Lock'), Js('Locket'), Js('Love'), Js('Luck'), Js('Mask'), Js('Medium'), Js('Mercy'), Js('Method'), Js('Might'), Js('Mind'), Js('Mine'), Js('Minute'), Js('Mirror'), Js('Moon'), Js('Mouse'), Js('Muse'), Js('Nerve'), Js('Night'), Js('Nightowl'), Js('Omen'), Js('One'), Js('Owl'), Js('Patch'), Js('Pest'), Js('Phase'), Js('Pitch'), Js('Poet'), Js('Poison'), Js('Pool'), Js('Price'), Js('Pride'), Js('Prize'), Js('Pulse'), Js('Push'), Js('Quartz'), Js('Quill'), Js('Quince'), Js('Quiver'), Js('Rain'), Js('Raw'), Js('Ray'), Js('Reaper'), Js('Red'), Js('Rice'), Js('Ride'), Js('Rise'), Js('Robin'), Js('Rose'), Js('Rush'), Js('Scratch'), Js('Shade'), Js('Shadow'), Js('Shift'), Js('Silk'), Js('Silver'), Js('Sky'), Js('Slice'), Js('Smile'), Js('Smoke'), Js('Snow'), Js('Spade'), Js('Spark'), Js('Spirit'), Js('Sprite'), Js('Status'), Js('Steel'), Js('Stitch'), Js('Storm'), Js('Stranger'), Js('Sugar'), Js('Tails'), Js('Tales'), Js('Tank'), Js('Tear'), Js('The Edge'), Js('Throne'), Js('Thunder'), Js('Tiger'), Js('Tune'), Js('Two'), Js('Veil'), Js('Vessel'), Js('Voyage'), Js('Web'), Js('Weird'), Js('Whistle'), Js('Wind'), Js('Wing'), Js('Wings'), Js('Wish'), Js('Yellow'), Js('Youth'), Js('Zephyr')]))
    var.put('tp', var.get('type'))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            if (var.get('i')<Js(6.0)):
                var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm5').get('length'))|Js(0.0)))
                var.put('names', var.get('nm5').get(var.get('rnd')))
            else:
                var.put('rnd2', ((var.get('Math').callprop('random')*var.get('nm3').get('length'))|Js(0.0)))
                if PyJsStrictEq(var.get('tp'),Js(1.0)):
                    var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm2').get('length'))|Js(0.0)))
                    var.put('names', ((var.get('nm2').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                    var.get('nm2').callprop('splice', var.get('rnd'), Js(1.0))
                else:
                    if PyJsStrictEq(var.get('tp'),Js(2.0)):
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm4').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm4').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
                        var.get('nm4').callprop('splice', var.get('rnd'), Js(1.0))
                    else:
                        var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
                        var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
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
musicianNames = var.to_python()