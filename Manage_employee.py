

import json
from turtle import title
def punish(late_days):
    import urllib.request
    import json
    import ssl

    #Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    link_muon="https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de"
    data_phat = urllib.request.urlopen(link_muon, context = ctx).read()
    punish_list = json.loads(data_phat)
    for punish in punish_list:
        min_date = float(punish["min"])
        punish_value = float(punish["value"])
        try:
            max_date = float(punish["max"])
        except:
            return punish_value 
        if  late_days == 0:
            return 0
        elif late_days <= max_date and late_days > min_date:
            return punish_value        
        else: continue
def tax_perce(salary):
    import urllib.request
    import xml.etree.ElementTree as ET
    import ssl

    #Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    link_tax="https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7"
    data_tax = urllib.request.urlopen(link_tax, context = ctx).read()
    tax = ET.fromstring(data_tax)
    taxes = tax.findall("tax")
    for tax in taxes:
        min_salary = float(tax.find("min").text)
        tax_perce =  float(tax.find("value").text)
        try:
            max_salary = float(tax.find("max").text)
        except: return tax_perce 
        if (salary/1000000) >= min_salary and (salary/1000000) < max_salary:
            return tax_perce
        else: continue
class employee:
    def __init__(self,id):
        employee = employees().find(id)
        #if employee["id"] == id:
        self.id = employee["id"]
        self.title = employee["title"]
        self.name = employee["Name"]
        self.salary_base = employee["Base salary"]
        self.working_day = employee["Working days"]
        self.depart = employee["Department"]
        self.working_perf = employee["Working performance"]
        self.bonus = employee["Bonus"]
        self.late_working_days = employee["Late working days"]
        
class employees():
    import json
    #linkfile = "C:/Users/DELL/Desktop/Data Eng/python/assigment/assm03/employee.json"
    file = open('employee.json')
    data = json.load(file)
    file.close()
    def save_data(self,data):#lưu data
        with open("employee.json", mode = "w") as employee_data:
            jstr = json.dumps(data, indent = 4)
            employee_data.write(jstr)    
    def newemployee(self):
        #nhap id
        id = input("Mã số nhân viên: ")
        id = self.check_input_char(id)
        while self.find(id) != 0:
            print("Mã số nhân viên đã tồn tại")
            id = input("Vui lòng nhập lại mã só nhân viên khác:")
        #nhap chuc vu
        title = input("Chức vụ nhân viên: ")
        title = self.check_input_char(title)
        #Nhap ten
        name = input( "Tên nhân viên: ")
        name = self.check_input_char(name)
        #nhap he so luong
        salary_base = input("Hệ số lương :")
        salary_base = self.check_input_char(salary_base)
        salary_base = self.check_input_num(salary_base)
        #nhap so ngay lam viec    
        wk_day = input("Số ngày đi làm: ")
        wk_day =  self.check_input_char(wk_day)
        wk_day = self.check_input_num(wk_day)
        #nhap phong ban
        dep = input("Phòng ban: ")
        if departments().find_dep(dep) == 0:
            print("Chưa có dữ liệu phòng ban")
            print("Vui lòng nhập dữ liệu phòng ban: ",dep)
            departments().new_department()
            print("-------------------------------")
        #nhap hieu qua con viec     
        wk_perf = input("Hiệu quả công việc: ")
        wk_perf = self.check_input_char(wk_perf)
        wk_perf = self.check_input_num(wk_perf)
        #nhap thuong
        bonus = input("Thưởng: ")
        bonus = self.check_input_char(bonus)
        bonus = self.check_input_num(bonus)
        #nhap so ngay di tre
        wk_late = input("Số ngày đi làm trễ: ")
        wk_late = self.check_input_char(wk_late)
        wk_late = self.check_input_num(wk_late)  

        nhan_vien = dict()
        nhan_vien['id'] = id
        nhan_vien['Name'] = name
        nhan_vien["title"]= title 
        nhan_vien['Department']= dep
        nhan_vien['Base salary']= salary_base
        nhan_vien["Working days"] = wk_day
        nhan_vien["Working performance"] = wk_perf
        nhan_vien["Late working days"] = wk_late
        nhan_vien["Bonus"] = bonus

        (self.data).append(nhan_vien)
        self.save_data(self.data)
    def check_input_char(self,field):#check trươống bỏ trông
        while len(field) == 0:
            print("Bạn không được bỏ trống trường này")
            field =input("Mời bạn nhập lại:")
        return field
    def check_input_num(self,field):#check định dạng input
        temp_field = 0 #tao biến để kiểm tra sau khi input lại dữ liệu
        while temp_field == 0:
            try: 
                temp_field = float(field)+1 # tránh trường họp cần nhạp số bằng 0
                if float(field) < 0:
                    print("Bạn phải nhập số dương")
                    field = input("Mời bạn nhập lại:")
                    temp_field = 0
            except: 
                print("Nhập sai định dạng")
                field = input("Mời nhập lại:")
        return float(field)
    def edit_employee(self,id):
        employee_edit = self.find(id)
        if self.find(id) == 0:
            print("Nhân viên không tồn tại")
        else:                      
            #nhap chuc vu
            title = input("Nhập chức vụ:")
            if len(title)!=0:
                employee_edit["title"] = title
            #Nhap ten
            name = input( "Nhập tên nhân viên:")
            if len(name) != 0:
                employee_edit["Name"] = name
            
            #nhap he so luong
            salary_base = input("Hệ số lương :")
            if len(salary_base) != 0:
                salary_base = self.check_input_num(salary_base)
                employee_edit["Base salary"] = salary_base
            
            #nhap so ngay lam viec    
            wk_day = input("Số ngày đi làm:")
            if len(wk_day) != 0:
                wk_day = self.check_input_num(wk_day)
                employee_edit["Working days"] = wk_day
            #nhap phong ban
            dep= input("Nhập phòng ban:")
            if len(dep) != 0: 
                employee_edit["Department"] = dep
                if departments().find_dep(dep) == 0:
                    print("Chưa có dữ liệu phòng ban")
                    dep = input("Vui lòng nhập dữ liệu phòng ban mới")
                    departments().new_department()
                    print("-------------------------------")
            #nhap hieu qua con viec     
            wk_perf = input("Hiệu quả công việc:")
            if len(wk_perf) != 0:
                wk_perf = self.check_input_num(wk_perf)
                employee_edit["Working performance"] = wk_perf
            #nhap thuong
            bonus = input("Thưởng:")
            if len(bonus) != 0:
                bonus = self.check_input_num(bonus)
                employee_edit["Bonus"] = bonus
            #nhap so ngay di tre
            wk_late = input("Số ngày đi làm trễ:")
            if len(wk_late) != 0:
                wk_late = self.check_input_num(wk_late)
                employee_edit["Late working days"] = wk_late
            print()
            self.save_data(self.data) 
            print("Đã hoàn thành chỉnh sửa")
            print("Mã số nhân viên:", employee_edit["id"])
            print("Chức vu:", employee_edit["title"])
            print("Họ tên:", employee_edit["Name"])
            print("Bộ phận: ", employee_edit["Department"])
            print("Hệ số lương:", "{:3,.0f}".format(employee_edit["Base salary"]),"VND")
            print("Số ngày làm việc:", employee_edit["Working days"])
            print("Hệ số hiệu quả:", employee_edit["Working performance"])
            print("Nhập thưởng:", "{:3,.0f}".format(employee_edit["Bonus"]), "VND")
            print("Số ngày đi muộn:", employee_edit["Late working days"])
            print("------------------------------------------------------------")
                                                                                                                                                                                                
    def delete_employee(self,id):           
        if self.find(id) ==0:
            print("Nhân viên không tồn tại")
        else:
            employee = self.find(id)
            (self.data).remove(employee)
            self.save_data(self.data)
            print("Đã xóa nhân viên khỏi hệ thống")
    def find(self,id):
        count = 0 
        for i in range(len(self.data)):
            employee = (self.data)[i]
            if employee["id"] == id:
                count = count + 1
                return employee
                continue
            else: continue
        if count == 0:
            return 0
        
    def display_employee(self):
        employees = self.data
        for employee in employees:
            print("Mã số nhân viên: ", employee["id"])
            print("Chức vụ: ", employee["title"])
            print("Họ tên: ", employee["Name"])
            print("Bộ phận: ", employee["Department"])
            print("Hệ số lương: ", "{:3,.0f}".format(employee["Base salary"]),"VND")
            print("Số ngày làm việc: ", employee["Working days"])
            print("Hệ số hiệu quả: ", employee["Working performance"])
            print("Nhập thưởng: ", "{:3,.0f}".format(employee["Bonus"]), "VND")
            print("Số ngày đi muộn: ", employee["Late working days"])
            print("---------------------------")
    def display_salary(self):
        employees = self.data
        for employee in employees:
            id_emp = employee["id"]
            print("Mã só nhân viên:", id_emp)
            income_emp =  income(id_emp)
            print("Thu nhập thực nhận:","{:3,.0f}".format(income_emp))
            print("----------------------------")
    
class manager(employee):
    def __init__(self,id):
        super().__init__(self,id)
class department():
    def __init__(self,id):
        department = departments().find_dep(id)
        #print(department)
        #for department in self.dep_data:
        self.id_dep = department["Department id"]
        self.bonus_salary = department["Bonus salary"]
class departments():
    import json
    dep_file = open("department.json")
    dep_data = json.load(dep_file)
    def find_dep(self,id_dep):
        count = 0
        for i in range(len(self.dep_data)):
            department = (self.dep_data)[i]
            if id_dep == department["Department id"]:
                count = count + 1
                return department
                continue
                #print(count)
        if count == 0:
            return 0
        
    def bonussalary(self, id):
        bonus_salary = self.find_dep(id)
        return bonus_salary["Bonus salary"]
    def new_department(self):
        dep = dict()
        dep_id =  input("Id phòng ban:")
        while len(dep_id) == 0:
            print("Bạn không được bỏ trống trường này")
            dep_id = input("Mời bạn nhập lại:")
        #nhap thuong phong ban
        dep_bonus =  input("Thưởng theo phòng ban:")
        dep_bonus = employees().check_input_char(dep_bonus)
        dep_bonus = employees().check_input_num(dep_bonus)

        dep["Department id"] = dep_id     
        #dep["Department name"] = dep_name           
        dep["Bonus salary"] = dep_bonus

        (self.dep_data).append(dep)
        self.save(self.dep_data)
    def save(self, data):
        with open("department.json", "w") as dp:
            dep_str = json.dumps(data, indent=4)
            dp.write(dep_str)
    def display_department(self):
        for DP in self.dep_data:
            print("Mã bộ phận:", DP["Department id"])
            #print("Tên bộ phận:", DP["Department name"])
            print("Bonus: ", "{:3,.0f}".format(DP["Bonus salary"]), "VND")
            print("--------------------------------------")
    def delete_department(self,dep_id):
        DP = self.find_dep(dep_id)
        #print(DP)
        if self.find_dep(dep_id) == 0:
            print("Phòng ban không tồn tại")
        else:
            DP = self.find_dep(dep_id)
            if dep_id == DP["Department id"]:
                number_employee = 0
                for dep_employee in employees().data:
                    if dep_id == dep_employee["Department"]:
                        number_employee = number_employee+1
                    else: continue
                #print(number_employee)
                if number_employee == 0:
                    (self.dep_data).remove(DP)
                    print("Đã xóa dữ liệu phòng ban")
                else: print("Trong phòng có nhân viên, không xóa")   
        self.save(self.dep_data)
def income(id):
    if employees().find(id) == 0:
        print("Mã nhân viên không tồn tại")
    else:        
        emp = employee(id)
        dep = department(emp.depart)
        total = emp.salary_base*emp.working_day*emp.working_perf
        late_charge =  emp.late_working_days*punish(emp.late_working_days)
        #print(emp.title)
        if emp.title == "nhan vien":
           #print(dep.bonus_salary)
            incomeplustax= 0.895*(total + emp.bonus + dep.bonus_salary - late_charge )#thu nhap truoc thue
        elif emp.title == "Quan ly":
            #print(1.1*dep.bonus_salary)
            incomeplustax= 0.895*(total + emp.bonus + 1.1*dep.bonus_salary - late_charge )#Quan lý thưởng 1.1 phng ban
        tax_income= tax_perce(incomeplustax)*incomeplustax/100
        income = incomeplustax - tax_income
        return income   
