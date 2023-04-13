import json
from Manage_employee import employees, departments, manager, income
while 1 == 1:
    
    print("1.Hiển thị danh sách nhân viên")
    print("2.Hiển thị danh sách bộ phận")
    print("3.Thêm nhân viên mới")
    print("4.Xóa nhân viên theo ID")
    print("5.Xóa bộ phận theo ID")
    print("6.Hiển thị bảng lương")
    print("7.Chỉnh sửa thông tin nhân viên")# nâng cao
    print("8.Thoát")
    lua_chon =  input("Mời bạn nhập chức năng mong muốn:")
    #print(lua_chon)
    try: lua_chon = int(lua_chon)
    except:
        print("Bạn đã nhập sai đinh dạng")
    #print(lua_chon)
    if lua_chon == 1:
        employees().display_employee()
    elif lua_chon == 2:
        departments().display_department()
    elif lua_chon == 3:
        employees().newemployee()
        print("Đã thêm nhân viên mới")
        print("----------------------")
    elif lua_chon == 4:
        id = input("Nhập id nhân viên cần xóa:")
        employees().delete_employee(id)
        #print("Đã xóa nhân viên khỏi hệ thống")
        print("-------------------------------")
    elif lua_chon == 5:
        id_dep = input("Nhập id phòng ban cần xóa:")
        departments().delete_department(id_dep)
        print("---------------------------------")
    elif lua_chon == 6:
        employees().display_salary()
    elif lua_chon == 7:
        id = input("Nhập id nhân viên cần sửa:")
        employees().edit_employee(id)
        print("Đã hoàn tất chỉnh sửa")
    elif lua_chon == 8:
        print("Thoát khỏi chương trình")
        break
    else: #lua_chon >8 or lua_chon <1:
        print("Lựa chọn của bạn không phù hợp")
        print("-------------------------------")