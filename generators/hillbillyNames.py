__all__ = ['hillbillyNames']

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
var.put('nm1', Js([Js('Abel'), Js('Abner'), Js('Ace'), Js('Amos'), Js('Arlo'), Js('Austin'), Js('Barney'), Js('Bart'), Js('Beau'), Js('Billy'), Js('Billy Bob'), Js('Billy Ray'), Js('Blue'), Js('Bo'), Js('Bob'), Js('Bobby Joe'), Js('Bodean'), Js('Bryar'), Js('Bubba'), Js('Bubba Blue'), Js('Buck'), Js('Buckley'), Js('Bud'), Js('Buddy'), Js('Burl'), Js('Cal'), Js('Carson'), Js('Casey'), Js('Charles Ray'), Js('Charlton'), Js('Chester'), Js('Cleavon'), Js('Cleetus'), Js('Clem'), Js('Cleon'), Js('Cletus'), Js('Clifton'), Js('Clint'), Js('Clyde'), Js('Cody'), Js('Cooper'), Js('Cooter'), Js('Coy'), Js('Cy'), Js('Cyrus'), Js('Dale'), Js('Darrel'), Js('Darryl'), Js('Delmont'), Js('Doc'), Js('Don'), Js('Donny'), Js('Duane'), Js('Duke'), Js('Dwayne'), Js('Earl'), Js('Eli'), Js('Elmer'), Js('Elrod'), Js('Enos'), Js('Eustice'), Js('Floyd'), Js('Floyd William'), Js('Ford'), Js('Forrest'), Js('Garth'), Js('George'), Js('Gomer'), Js('Gus'), Js('Harlan'), Js('Harley'), Js('Homer'), Js('Horace'), Js('Houston'), Js('Hoyt'), Js('Huckleberry'), Js('Ike'), Js('Jackson'), Js('Jasper'), Js('Jeb'), Js('Jed'), Js('Jefferson'), Js('Jerry Lee'), Js('Jessie'), Js('Jethro'), Js('Jim Bob'), Js('Jimmy Don'), Js('Jimmy James'), Js('Joe Bob'), Js('John Boy'), Js('Junior'), Js('Lee'), Js('Leewon'), Js('Lem'), Js('Lenny'), Js('Lester'), Js('Lloyd'), Js('Lonnie'), Js('Luke'), Js('Lum'), Js('Luther'), Js('Lynn'), Js('Merle'), Js('Mose'), Js('Orville'), Js('Otis'), Js('Ottis'), Js('Pervis'), Js('Quentin'), Js('Randy'), Js('Ray'), Js('Ray Nathan'), Js('Ray-Nathan'), Js('Rebel'), Js('Reuben'), Js('Ricky'), Js('Robbie'), Js('Rocky'), Js('Roscoe'), Js('Rowan'), Js('Roy'), Js('Rufus'), Js('Rusty'), Js('Scooter'), Js('Sherman'), Js('Silas'), Js('Skeeter'), Js('Spencer'), Js('Tommy'), Js('Tommy Lee'), Js('Trigger'), Js('Tyler'), Js('Verne'), Js('Vinton'), Js('Virgil'), Js('Wade'), Js('Wayne'), Js('Wilbur'), Js('Wilfred'), Js('Willie'), Js('Winchester'), Js('Winslow'), Js('Woody'), Js('Wyatt'), Js('Zeb'), Js('Zed'), Js('Zeke')]))
var.put('nm2', Js([Js('Aleigh'), Js('Amaleen'), Js('Amber'), Js('Amberly'), Js('Angel'), Js('Annabelle'), Js('Audrey-Anne'), Js('Avalon'), Js('Bailie'), Js('Bambi'), Js('Baylee'), Js('Baylee-Ann'), Js('Bayleigh'), Js('Belle'), Js('Betty Jo'), Js('Betty Lou'), Js('Betty Sue'), Js('Billie Jean'), Js('Billy Jo'), Js('Bobbi Jo'), Js('Bobbie Sue'), Js('Bobby Jean'), Js('Bobby Jo'), Js('Brandine'), Js('Brandyne'), Js('Breanna'), Js('Breannona'), Js('Brittney-Anne'), Js('Buffy'), Js('Cambria'), Js('Candy'), Js('Charity'), Js('Chastity'), Js('Cherry'), Js('Claudette'), Js('Claudine'), Js('Crystal'), Js('Cyndi Beth'), Js('Dakota'), Js('Dale'), Js('Debbie'), Js('Delilah'), Js('Desiree'), Js('Destiny'), Js('Diamond'), Js('Earlene'), Js('Ellie Mae'), Js('Erin'), Js('Erneshia'), Js('Eva Jo'), Js('Faylene'), Js('Gracelyn'), Js('Gretchen'), Js('Harmony'), Js('Hattie'), Js('January'), Js('Jasmynn Mae'), Js('Jaylnn Jo'), Js('Jaylyne'), Js('Jaylynne'), Js('Jazlean'), Js('Jazzinelle'), Js('Jazznellie'), Js('Jerleecia'), Js('Jicelle'), Js('JoLener'), Js('Jolene'), Js('Joy'), Js('Jozelle'), Js('Kandy'), Js('Larlene'), Js('Layla'), Js('Leanne'), Js('Lexus'), Js('Lilah'), Js('Linda Sue'), Js('Lindieanne'), Js('Loriabelle'), Js('Loribelle'), Js('Lynndie'), Js('Maddison'), Js('Maddy'), Js('Mandy-Lynn'), Js('Martha Mae'), Js('Mary Beth'), Js('Mary Ellen'), Js('Mary Jane'), Js('Mary Jo'), Js('Mary Lou'), Js('Melody'), Js('Mercadies'), Js('Misty'), Js('Misty Dawn'), Js('Naomi'), Js('Natasha'), Js('Norma'), Js('Nyla'), Js('Nylette'), Js('Patty Sue'), Js('Peach'), Js('Pegg'), Js('Peggy Sue'), Js('Porsha'), Js('Pristine'), Js('Randa Lynn'), Js('Randee Leigh'), Js('Raylene'), Js('Roxxy'), Js('Roxxy-Lynn'), Js('Ruby Jane'), Js('Sammie Jo'), Js('Sandy'), Js('Savannah Jean'), Js('September'), Js('Shanamarie'), Js('Shaney'), Js('Sharlexia'), Js('Shayla'), Js('Shayna'), Js('Sheena'), Js('Shelby'), Js('Shirlene'), Js('Shorna'), Js('Sienna'), Js('Sierra'), Js('Stasha'), Js('Sue Ellen'), Js('Sunny'), Js('Tabitha'), Js('Tammie'), Js('Tasha'), Js('Tierra'), Js('Tiffany'), Js('Trista-Lynn'), Js('Trixie'), Js('Trixiebelle'), Js('Vanity'), Js('Vicki Lynn'), Js('Vienna'), Js('Waynelle'), Js('Willa'), Js('Wilma')]))
pass
pass


# Add lib to the module scope
hillbillyNames = var.to_python()