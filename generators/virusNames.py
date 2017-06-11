__all__ = ['virusNames']

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
    var.put('nm1', Js([Js('WelcomeHome'), Js('Status_Update'), Js('soLong'), Js('Click'), Js('AbSent'), Js('Aberrant'), Js('Accident'), Js('Achievement Unlocked'), Js('AdFree'), Js('Addict'), Js('Adventure Time Out'), Js('AfterMath'), Js('Aftermath'), Js('Agency'), Js('AirLine'), Js('AirPort'), Js('Alternate Dimension'), Js('Amazing!'), Js('Ambition'), Js('Anxiety'), Js('Arch'), Js('Article One'), Js('Aspect'), Js('AtmoSphere'), Js('BaitHook'), Js('BaitSwitch'), Js('Bed Time'), Js('Begin'), Js('Belief'), Js('BestFriend'), Js('Big Brother'), Js('BitSized'), Js('BitterSweet'), Js('BlackWhite'), Js('Bliss'), Js('Blood Money'), Js('Borderless'), Js('Borrowed'), Js('BottomsUp'), Js('Boyfriend'), Js('Brass Knuckle'), Js('BreakFast'), Js('Breaking News!'), Js('Brother'), Js('Cancelled'), Js('CandleLight'), Js('Candy'), Js('Captive Audience'), Js('Cattle Prod'), Js('Champion'), Js('Charity'), Js('ChequePlease'), Js('ChildHood'), Js('ChocoLate'), Js('ClassWork'), Js('ClickBait'), Js('Closet'), Js('Clueless'), Js('CoWard'), Js('ComFort'), Js('ComMission'), Js('ComPetition'), Js('ComPlex'), Js('Command'), Js('ConFusion'), Js('ConSequence'), Js('ConTest'), Js('ConText'), Js('ConTroll'), Js('Confidential'), Js('CookieCutter'), Js('Courage'), Js('Coward'), Js('Creator'), Js('Curiosity'), Js('CurtainFall'), Js('CustomerService'), Js('DailyDose'), Js('Dance Off'), Js('DataBase'), Js('Daydream'), Js('DearlyBeloved'), Js('Declined'), Js('Defeated'), Js('Design'), Js('Desire'), Js('DisHonest'), Js('DisPlay'), Js('Disappointment'), Js('Discount'), Js('Divide'), Js("Doctor's Order"), Js('Double Trouble'), Js('DownRight'), Js('DownTown'), Js('DreamOn'), Js('DreamScape'), Js('EconoMimics'), Js('Emergency!'), Js('Employee'), Js('EnCourage'), Js('EnLightened'), Js('Error'), Js('ErrorErrorError'), Js('Essay Due'), Js('Eternity'), Js('Exam'), Js('ExcuseMe'), Js('Excuses'), Js('Execute'), Js('Faith'), Js('Fake'), Js('Family First'), Js('Fate'), Js('Father'), Js('FeedBack'), Js('Final Exam'), Js('FingerLicking'), Js('FirstHand'), Js('FlawLess'), Js('FlowerPower'), Js('Follow Me'), Js('Forgive'), Js('ForgiveMe'), Js('Free Choice'), Js('FreeDom'), Js('FreeGift'), Js('Freedom'), Js('Friend'), Js('FriendlyGiant'), Js('GapingWhole'), Js('Generosity'), Js('Ghost'), Js('Girlfriend'), Js('Goal!'), Js('GoodAsNew'), Js('GoodNatured'), Js('Goodbye!'), Js('Gratis'), Js('Guarantee'), Js('GuiltLess'), Js('Happy Birthday!'), Js('Health'), Js('HeartBreaker'), Js('Hello'), Js('Hello World'), Js('HelpMe'), Js('HeyBeauty'), Js('Hilarious!'), Js('Honestly'), Js('HonorAmong'), Js('Hooked'), Js('HugsKisses'), Js('Humility'), Js('Hummmmm'), Js('HungryHungry'), Js('Hurricane'), Js('Husband'), Js('IdleHands'), Js('Impulse'), Js('In a Pickle'), Js('InDependence'), Js('InFinite'), Js('InSanity'), Js('InSecure'), Js('InVincible'), Js('Infinity'), Js('Inside Out'), Js('Interview'), Js('Investment'), Js('Invitation'), Js('Junior'), Js('Just Kidding'), Js('Justice'), Js('LawLess'), Js('LeaderShip'), Js('Lecture'), Js('LethalDose'), Js('Level One'), Js('Leviathan'), Js('Lewd'), Js('Liar Liar'), Js('Liberty'), Js('LongTerm'), Js('Main Priority'), Js('MakeShift'), Js('Mammoth'), Js('Manager'), Js('MemberShip'), Js('MidKnight'), Js('Milkman'), Js('Mime'), Js('MiracleWork'), Js('MirrorMirror'), Js('Mortgage'), Js('Mother'), Js('MyBad'), Js('MyPleasure'), Js('NaughtyNice'), Js('Nemo'), Js('New'), Js('NewMessage'), Js('NightMare'), Js('NightNight'), Js('No Pressure'), Js('NoHonor'), Js('One Minute'), Js('OnePercent'), Js('Oops'), Js('Opportunity'), Js('Opposites'), Js('Organic'), Js('OverDue'), Js('OverJoyed'), Js('OverLooked'), Js('Overachiever'), Js('Package'), Js('Paradise'), Js('Parallel'), Js('Parcel Delivery'), Js('PatientZero'), Js('Patriot'), Js('Phobia'), Js('Phony'), Js('Pizzaz'), Js('PlayGrounded'), Js('PointLess'), Js('PowerLess'), Js('PowerPlay'), Js('PressRecord'), Js('PrisonEscape'), Js('Private'), Js('Private and Confidential'), Js('Punishment'), Js('Puny'), Js('Purchase'), Js('Re:'), Js('ReCommended'), Js('RealityCheck'), Js('Recommended'), Js('Recording'), Js('RelationshipStatus'), Js('Relax'), Js('Request'), Js('Requiem'), Js('Resident'), Js('Revolution'), Js('Reward'), Js('Riches'), Js('RiddleMeThis'), Js('RnD'), Js('Rosebud'), Js('Rumor'), Js('SafetyNet'), Js('Salary'), Js('Save the Date'), Js('ScareCrow'), Js('ScratchThat'), Js('SecondHand'), Js('Security!'), Js('SelfControl'), Js('ShadyBusiness'), Js('Shame!'), Js('ShockAwe'), Js('SignHere'), Js('Signature'), Js('Single'), Js('Sister'), Js('Situation'), Js('Slave'), Js('SomeWare'), Js('SorryNotSorry'), Js('Special Delivery'), Js('SpiderWeb'), Js('Spooky'), Js('SpotLess'), Js('Stained'), Js('StatusUpdate'), Js('Stranger'), Js('StrangerDanger'), Js('TaintedLove'), Js('Thoughts'), Js('ThunderStorm'), Js('Tickets'), Js('TidBit'), Js('Travel'), Js('TravelLog'), Js('Trouble'), Js('UnEmployed'), Js('UnitOne'), Js('University'), Js('Unmasked'), Js('VIP'), Js('Victory'), Js('Weather'), Js('Welcome'), Js('Whistle'), Js('White Knight'), Js('Wife'), Js('Witness'), Js('Xx'), Js('Yesterday'), Js('YouPhoria'), Js('YourBase')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', ((var.get('Math').callprop('random')*var.get('nm1').get('length'))|Js(0.0)))
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
virusNames = var.to_python()