__all__ = ['vietnameseNames']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['nm1', 'nm4', 'nameGen', 'nm5', 'nm3', 'nm2'])
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
            var.put('rnd1', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm1').get('length'))))
            if PyJsStrictEq(var.get('tp'),Js(1.0)):
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm4').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm5').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd1'))+Js(' '))+var.get('nm4').get(var.get('rnd')))+Js(' '))+var.get('nm5').get(var.get('rnd2'))))
            else:
                var.put('rnd', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm2').get('length'))))
                var.put('rnd2', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('nm3').get('length'))))
                var.put('names', ((((var.get('nm1').get(var.get('rnd1'))+Js(' '))+var.get('nm2').get(var.get('rnd')))+Js(' '))+var.get('nm3').get(var.get('rnd2'))))
            var.get('result').callprop('push', var.get('names'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    pass
    return var.get('result')
PyJsHoisted_nameGen_.func_name = 'nameGen'
var.put('nameGen', PyJsHoisted_nameGen_)
var.put('nm1', Js([Js('Au'), Js('Ba'), Js('Banh'), Js('Bi'), Js('Bien'), Js('Bo'), Js('Bui'), Js('Cam'), Js('Can'), Js('Cao'), Js('Chan'), Js('Chau'), Js('Che'), Js('Chiem'), Js('Chu'), Js('Chung'), Js('Chuong'), Js('Co'), Js('Cong'), Js('Dai'), Js('Dam'), Js('Dan'), Js('Dang'), Js('Danh'), Js('Dao'), Js('Dau'), Js('Diep'), Js('Dieu'), Js('Dinh'), Js('Dinn'), Js('Do'), Js('Doan'), Js('Don'), Js('Dong'), Js('Du'), Js('Dung'), Js('Duong'), Js('Giang'), Js('Ha'), Js('Hai'), Js('Han'), Js('Hang'), Js('Hau'), Js('Ho'), Js('Hoang'), Js('Hua'), Js('Hue'), Js('Huynh'), Js('Hy'), Js('Kha'), Js('Khong'), Js('Khuu'), Js('Kien'), Js('Kieu'), Js('Kim'), Js('Ky'), Js('La'), Js('Lac'), Js('Lai'), Js('Lam'), Js('Lang'), Js('Lavan'), Js('Le'), Js('Lien'), Js('Lieu'), Js('Lo'), Js('Loi'), Js('Luc'), Js('Luong'), Js('Luu'), Js('Ly'), Js('Ma'), Js('Mac'), Js('Mach'), Js('Mai'), Js('Minh'), Js('Nghiem'), Js('Ngo'), Js('Ngu'), Js('Nguy'), Js('Nguyen'), Js('Nhan'), Js('Nzuyen'), Js('On'), Js('Ong'), Js('Pham'), Js('Phan'), Js('Phang'), Js('Phong'), Js('Phu'), Js('Phung'), Js('Phuong'), Js('Quach'), Js('Quang'), Js('Quyen'), Js('Sai'), Js('Su'), Js('Ta'), Js('Tang'), Js('Tat'), Js('Thach'), Js('Thai'), Js('Tham'), Js('Than'), Js('Thang'), Js('Thanh'), Js('Thao'), Js('Thi'), Js('Thong'), Js('Thuy'), Js('Tian'), Js('Tien'), Js('Tieu'), Js('To'), Js('Ton'), Js('Trach'), Js('Tram'), Js('Tran'), Js('Trang'), Js('Tri'), Js('Trieu'), Js('Trinh'), Js('Tron'), Js('Troung'), Js('Truong'), Js('Tu'), Js('Tuan'), Js('Ty'), Js('Van'), Js('Vang'), Js('Vien'), Js('Vinh'), Js('Vo'), Js('Vong'), Js('Voong'), Js('Vu'), Js('Vuong'), Js('Vuu')]))
var.put('nm2', Js([Js('Van'), Js('Huu'), Js('Duc'), Js('Dinh'), Js('Xuan'), Js('Ngoc'), Js('Quang'), Js('Cong'), Js('Manh'), Js('Trong'), Js('Qui'), Js(''), Js(''), Js('')]))
var.put('nm3', Js([Js('An'), Js('Anh Dung'), Js('Bao '), Js('Binh'), Js('Canh'), Js('Chien'), Js('Chinh'), Js('Cuong'), Js('Dac Kien'), Js('Danh'), Js('Dao'), Js('Dat'), Js('De'), Js('Dien'), Js('Duc'), Js('Due'), Js('Dung'), Js('Duong'), Js('Gia'), Js('Giang'), Js('Hai'), Js('Hao'), Js('Hien'), Js('Hieu'), Js('Hoc'), Js('Hung'), Js('Huu'), Js('Huy'), Js('Huynh'), Js('Khan'), Js('Lan'), Js('Lanh'), Js('Loc'), Js('Minh'), Js('Nguyen'), Js('Nhat'), Js('Phuc'), Js('Phuoc'), Js('Quan'), Js('Quang'), Js('Quoc'), Js('Sang'), Js('Si '), Js('Sinh'), Js('Son'), Js('Thang'), Js('Thanh'), Js('Thao'), Js('Thinh'), Js('Tho '), Js('Thu'), Js('Thuan'), Js('Toai'), Js('Toan'), Js('Trang'), Js('Trieu'), Js('Trong'), Js('Trong Tri'), Js('Trung'), Js('Tu'), Js('Tuan'), Js('Tung'), Js('Van'), Js('Vien'), Js('Viet'), Js('Vuong'), Js('Xuan')]))
var.put('nm4', Js([Js('Thi'), Js('')]))
var.put('nm5', Js([Js('Ai'), Js('An'), Js('Anh'), Js('Be'), Js('Bian'), Js('Bich'), Js('Binh'), Js('Cam'), Js('Canh'), Js('Chau'), Js('Chi'), Js('Dao'), Js('Diep'), Js('Diu'), Js('Doan Vien'), Js('Dong'), Js('Giang '), Js('Ha'), Js('Hai'), Js('Han'), Js('Hang'), Js('Hanh Phuc'), Js('Hien'), Js('Hoa'), Js('Hong'), Js('Hong Hanh'), Js('Hong Yen'), Js('Hue'), Js('Hung'), Js('Huong '), Js('Huyen'), Js('Hyunh'), Js('Ket Nien'), Js('Khanh'), Js('Kieu'), Js('Kim'), Js('Kim Cuc'), Js('Kim-Ly'), Js('Lam'), Js('Lan'), Js('Lang'), Js('Lanh'), Js('Le'), Js('Le '), Js('Lien'), Js('Lieu'), Js('Linh'), Js('Loan'), Js('Mai'), Js('My'), Js('Nam Ha'), Js('Ngoc'), Js('Ngoc Bich'), Js('Ngu'), Js('Ngu '), Js('Nguyet'), Js('Nhu'), Js('Nhung'), Js('Nu '), Js('Phuong'), Js('Quy'), Js('Quyen'), Js('Sang'), Js('Suong'), Js('Tam'), Js('Tan'), Js('Tham'), Js('Thanh'), Js('Thanh Ha'), Js('Thao'), Js('Thi'), Js('Thi '), Js('Thien '), Js('Thom'), Js('Thu'), Js('Thuy'), Js('Tien'), Js('Trinh'), Js('Truc'), Js('Tuyen'), Js('Tuyet'), Js('Uoc'), Js('Van'), Js('Viet'), Js('Xuan'), Js('Yen')]))
pass
pass


# Add lib to the module scope
vietnameseNames = var.to_python()