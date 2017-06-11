__all__ = ['puritanNames']

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
    var.registers(['nm1', 'nm2', 'result'])
    var.put('nm1', Js([Js('Abstinence'), Js('Abuse-Not'), Js('Abuse-not'), Js('Accepted'), Js('Aid-On-High'), Js('Amity'), Js('Anger'), Js('Approved'), Js('Arise'), Js('Ashes'), Js('Assurance'), Js('Battalion'), Js('Be-Courteous'), Js('Be-Faithful'), Js('Be-Strong'), Js('Be-Thankful'), Js('Benevolence'), Js('Belief'), Js('Beloved'), Js('Buried'), Js('Called'), Js('Charity'), Js('Clarity'), Js('Clemency'), Js('Comfort'), Js('Concord'), Js('Confidence'), Js('Consider'), Js('Constance'), Js('Constant'), Js('Continent'), Js('Creature'), Js('Credence'), Js('Deliverance'), Js('Delivery'), Js('Depend'), Js('Desire'), Js('Die-Well'), Js('Diffidence'), Js('Diligence'), Js('Discipline'), Js('Discretion'), Js('Donation'), Js('Dust'), Js('Earth'), Js('Elected'), Js('Endure'), Js('Experience'), Js('Faint-Not'), Js('Faint-not'), Js('Faith'), Js('Faith-My-Joy'), Js('Faithful'), Js('Fare-Well'), Js('Farewell'), Js('Fear'), Js('Fear-God'), Js('Fear-Not'), Js('Fear-The-Lord'), Js('Felicity'), Js('Fidel'), Js('Fly-Debate'), Js('Flye-debate'), Js('Forsaken'), Js('Fortune'), Js('Freegift'), Js('From-Above'), Js('Give-Thanks'), Js('Given'), Js('God-Reward'), Js('Godly'), Js('Grace'), Js('Gracious'), Js('Handmaid'), Js('Happy'), Js('Hate-Evil'), Js('Hate-Ill'), Js('Hate-ill'), Js('Help-On-High'), Js('Helpless'), Js('Honesty'), Js('Honour'), Js('Hope'), Js('Hope-For'), Js('Hope-Still'), Js('Hope-for'), Js('Hope-still'), Js('Hopeful'), Js('Humanity'), Js('Humble'), Js('Humiliation'), Js('Humility'), Js('Increase'), Js('Increased'), Js('Jolly'), Js('Joy'), Js('Joy-Again'), Js('Joy-In-Sorrow'), Js('Just'), Js('Justice'), Js('Kill-Sin'), Js('Kill-sin'), Js('Lament'), Js('Lamentation'), Js('Learn-Wisdom'), Js('Liberty'), Js('Live-Well'), Js('Lively'), Js('Love'), Js('Love-Well'), Js('Magnify'), Js('Magnify'), Js('Make-Peace'), Js('Meek'), Js('Merciful'), Js('Mercy'), Js('More-Fruit'), Js('More-Trial'), Js('More-Trial'), Js('Much-Mercy'), Js('Much-Mercy'), Js('No-Merit'), Js('No-merit'), Js('Obedience'), Js('Obey'), Js('Original'), Js('Pardon'), Js('Patience'), Js('Peaceable'), Js('Perseverance'), Js('Piety'), Js('Placidia'), Js('Praise-God'), Js('Preserved'), Js('Providence'), Js('Prudence'), Js('Purific'), Js('Purify'), Js('Recompense'), Js('Redeemed'), Js('Redivivia'), Js('Reformation'), Js('Rejoice'), Js('Remember'), Js('Renewed'), Js('Repent'), Js('Repentance'), Js('Replenish'), Js('Resolve'), Js('Resolved'), Js('Restore'), Js('Return'), Js('Safe-Deliverance'), Js('Safe-On-High'), Js('Safe-on-Highe'), Js('Salvation'), Js('Search-The-Scriptures'), Js('Seek-Wisdom'), Js('Silence'), Js('Sin-Deny'), Js('Sincere'), Js('Small-Hope'), Js('Sorry-For-Sin'), Js('Sorry-for-sin'), Js('Stand-Fast-On-High'), Js('Steadfast'), Js('Submit'), Js('Supply'), Js('Temperance'), Js('Tenacious'), Js('Thankful'), Js('Thankful'), Js('Thanks'), Js('The-Lord-Is-Near'), Js('The-Peace-Of-God'), Js('Tribulation'), Js('Trinity'), Js('Troth'), Js('Truth'), Js('Unfeigned'), Js('Unity'), Js('Vanity'), Js('Verity'), Js('Victory'), Js('Virtue'), Js('Vitalis'), Js('Weakly'), Js('Wealthy'), Js('Weep-Not'), Js('What-God-Will'), Js('Wrestling'), Js('Zeal-For-The-Lord'), Js('Zeal-Of-The-Land')]))
    var.put('nm2', Js([Js('Abbot'), Js('Alleine'), Js('Ames'), Js('Appletree'), Js('Arrowsmith'), Js('Ashe'), Js('Baillie'), Js('Ball'), Js('Barrowe'), Js('Baxter'), Js('Baylie'), Js('Bayly'), Js('Beard'), Js('Bending'), Js('Bernard'), Js('Blatcher'), Js('Bolton'), Js('Bond'), Js('Boston'), Js('Bradford'), Js('Bradshaw'), Js('Bradstreet'), Js('Brewster'), Js('Bridge'), Js('Brinsley'), Js('Brooks'), Js('Broughton'), Js('Browne'), Js('Bulkley'), Js('Bull'), Js('Bunyan'), Js('Burges'), Js('Burgess'), Js('Burroughs'), Js('Burton'), Js('Buttres'), Js('Byfield'), Js('Calamy'), Js('Capel'), Js('Carter'), Js('Cartwright'), Js('Caryl'), Js('Case'), Js('Cawdrey'), Js('Cawton'), Js('Chaderton'), Js('Charnock'), Js('Chawncey'), Js('Cheeseman'), Js('Cheynell'), Js('Coleman'), Js('Collyer'), Js('Corbet'), Js('Cotton'), Js('Coupard'), Js('Coverdale'), Js('Cromwell'), Js('Danforth'), Js('Darrell'), Js('Davenport'), Js('Dent'), Js('Dod'), Js('Doddridge'), Js('Downame'), Js('Downing'), Js('Dudley'), Js('Durant'), Js('Dury'), Js('Eaton'), Js('Edwards'), Js('Egerrton'), Js('Ekins'), Js('Engaine'), Js('Fenn'), Js('Field'), Js('Fiennes'), Js('Fish'), Js('Flavel'), Js('Fox'), Js('Foxe'), Js('French'), Js('Fulke'), Js('Gataker'), Js('Gilby'), Js('Gillespie'), Js('Gilpin'), Js('Goodman'), Js('Goodwin'), Js('Gouge'), Js('Greenham'), Js('Greenhill'), Js('Greenwood'), Js('Guthrie'), Js('Hake'), Js('Harmer'), Js('Harris'), Js('Harvard'), Js('Hastings'), Js('Henderson'), Js('Henley'), Js('Henry'), Js('Herle'), Js('Heyrick'), Js('Hickes'), Js('Higginson'), Js('Hildersham'), Js('Hill'), Js('Hinde'), Js('Hooker'), Js('Hopkinson'), Js('Howe'), Js('Hoyle'), Js('Humphrey'), Js('Hutchinson'), Js('Ireton'), Js('Janeway'), Js('John'), Js('Johnson'), Js('Kane'), Js('Larkford'), Js('Lathrop'), Js('Leighton'), Js('Ley'), Js('Lightfoot'), Js('Llwyd'), Js('Love'), Js('Lower'), Js('Manton'), Js('Marbury'), Js('Marshall'), Js('Mather'), Js('Mathews'), Js('Maynard'), Js('Mayo'), Js('Mede'), Js('Mildmay'), Js('Milton'), Js('Moody'), Js('More'), Js('Murphy'), Js('Newcomen'), Js('Norton'), Js('Noyes'), Js('Nye'), Js('Outtered'), Js('Owen'), Js('Palmer'), Js('Panckhurst'), Js('Parker'), Js('Peedle'), Js('Penry'), Js('Perkins'), Js('Perne'), Js('Phelps'), Js('Pimple'), Js('Poole'), Js('Pougher'), Js('Preston'), Js('Rainolds'), Js('Reynolds'), Js('Rice'), Js('Rich'), Js('Robinson'), Js('Rogers'), Js('Rowlandson'), Js('Rutherford'), Js('Sampson'), Js('Scudder'), Js('Seaman'), Js('Sedgwick'), Js('Sence'), Js('Shepard'), Js('Shotbolt'), Js('Sibbes'), Js('Simpson'), Js('Smart'), Js('Spurstowe'), Js('Staunton'), Js('Sterry'), Js('Stoddard'), Js('Sykes'), Js('Taylor'), Js('Teate'), Js('Temple'), Js('Thorpe'), Js('Titus'), Js('Travers'), Js('Tregosse'), Js('Twisse'), Js('Udal'), Js('Upsall'), Js('Vincent'), Js('Vines'), Js('Vynall'), Js('Walker'), Js('Wallington'), Js('Wallis'), Js('Ward'), Js('Water'), Js('Watson'), Js('Watts'), Js('Weeks'), Js('Wentworth'), Js('Whathing'), Js('Wheelwright'), Js('Whitaker'), Js('White'), Js('Whitehead'), Js('Whittingham'), Js('Wigginton'), Js('Wigglesworth'), Js('Williams'), Js('Wilson'), Js('Winthrop'), Js('Wither'), Js('Wood'), Js('Woodbridge'), Js('Woodford'), Js('Young')]))
    var.put('result', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(10.0)):
        try:
            var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
            var.put('names', ((var.get('nm1').get(var.get('rnd'))+Js(' '))+var.get('nm2').get(var.get('rnd2'))))
            var.get('nm1').callprop('splice', var.get('rnd'), Js(1.0))
            var.get('nm2').callprop('splice', var.get('rnd2'), Js(1.0))
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
puritanNames = var.to_python()