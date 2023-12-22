import mysql.connector
import time
import os
from prettytable import PrettyTable
class Sach:
    def __init__(self, ma_sach, ten_sach, tac_gia, gia_ban,so_luong):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.mycursor = self.connection.cursor()
        self.ma_sach = ma_sach
        self.ten_sach = ten_sach
        self.tac_gia = tac_gia
        self.gia_ban = gia_ban
        self.so_luong = so_luong
    def nhap_sach(self):
        while True:
            self.ma_sach = input("Nhập mã sách: ")
            with self.connection.cursor() as cursor:
                sql_check = "SELECT COUNT(*) FROM sach WHERE ma_sach = %s"
                cursor.execute(sql_check, (self.ma_sach,))
                result = cursor.fetchone()
                if result[0] > 0:
                    print("Mã sách đã tồn tại. Vui lòng nhập lại.")
                else:
                    self.ten_sach = input("Nhập tên sách: ")
                    self.tac_gia = input("Nhập tác giả: ")
                    self.gia_ban = (input("Nhập giá bán: "))
                    self.so_luong = int(input("Nhập số lượng: "))
            break
    def in_sach(self):
        print("Mã sách:", self.ma_sach)
        print("Tên sách:", self.ten_sach)
        print("Tác giả:", self.tac_gia)
        print("Giá bán:", self.gia_ban)
        print("Số lượng:",self.so_luong)
class NhanVien:
    def __init__(self, ma_nv, ten_nv, sdt, dia_chi,email,vi_tri,luong):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.ma_nv = ma_nv
        self.ten_nv = ten_nv
        self.sdt = sdt
        self.dia_chi = dia_chi
        self.email = email
        self.vi_tri = vi_tri
        self.luong = luong
    def nhap_nhan_vien(self):
        while True:
            self.ma_nv = input("Nhập mã nhân viên: ")
            with self.connection.cursor() as cursor:
                sql_check = "SELECT COUNT(*) FROM nhanvien WHERE ma_nv = %s"
                cursor.execute(sql_check, (self.ma_nv,))
                result = cursor.fetchone()
                if result[0] > 0:
                    print("Mã nhân viên đã tồn tại. Vui lòng nhập lại.")
                else:
                    self.ten_nv = input("Nhập tên nhân viên: ")
                    while True:  
                        self.sdt = input("Nhập số điện thoại: ")
                        if (len(self.sdt) == 10):
                            break
                        else:
                            print("Số điện thoại của bạn phải đủ 10 chữ số")
                    self.dia_chi = input("Nhập địa chỉ: ")
                    while True:
                        self.email = input("Nhập email vào: ")
                        if  "@" in self.email:
                            break
                        else:
                            print("Email của bạn phải có kí tự @, vui lòng nhập lại")
                    self.vi_tri = input("Nhập vị trí nhân viên: ")
                    self.luong = float(input("Nhập lương nhân viên vào: "))
                break
class KhachHang:
    def __init__(self, ma_kh, ten_kh, sdt, dia_chi,email):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.ma_kh = ma_kh
        self.ten_kh = ten_kh
        self.sdt = sdt
        self.dia_chi = dia_chi
        self.email = email
    def nhap_khach_hang(self):
        while True:
            self.ma_kh = input("Nhập mã khách hàng: ")
            with self.connection.cursor() as cursor:
                sql_check = "SELECT COUNT(*) FROM khachhang WHERE ma_kh = %s"
                cursor.execute(sql_check, (self.ma_kh,))
                result = cursor.fetchone()
                if result[0] > 0:
                    print("Mã khách hàng đã tồn tại. Vui lòng nhập lại.")
                else:
                    self.ten_kh = input("Nhập tên khách hàng: ")
                    while True:
                        self.sdt = input("Nhập số điện thoại: ")
                        if (len(self.sdt) == 10):
                            break
                        else:
                            print("Số điện thoại của bạn phải đủ 10 số")
                    self.dia_chi = input("Nhập địa chỉ: ")
                    while True:
                        self.email = input("Nhập email khách hàng vào: ")
                        if "@" in self.email:
                            break
                        else:
                            print("Email phải có kí tự @, vui lòng nhập lại")
            break
class ThongTinMuaHang:
    def __init__(self, ma_hd,ma_kh,ma_sach,ma_nv,ten_sach,so_luong,ngay_hoa_don,tong_tien):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.ma_hd = ma_hd
        self.ma_kh = ma_kh
        self.ma_sach = ma_sach
        self.ma_nv = ma_nv
        self.ten_sach = ten_sach
        self.so_luong = so_luong
        self.ngay_hoa_don = ngay_hoa_don
        self.tong_tien = 0
    def nhap_thong_tin_mua_hang(self):
          while True:
            self.ma_hd = input("Nhập mã hóa đơn: ")
            with self.connection.cursor() as cursor:
                sql_check = "SELECT COUNT(*) FROM hoadon WHERE ma_hd = %s"
                cursor.execute(sql_check, (self.ma_hd,))
                result = cursor.fetchone()
                if result[0] > 0:
                    print("Mã hóa đơn đã tồn tại. Vui lòng nhập lại.")
                else:
                        self.ma_kh = input("Nhập mã khách hàng: ")
                        self.ma_sach = int(input("Nhập mã sách vào: "))
                        self.ma_nv = int(input("Nhập mã nhân viên vào: "))
                        try:
                            with self.connection.cursor() as cursor:
                                sql = "SELECT * FROM sach"
                                cursor.execute(sql)
                                result = cursor.fetchall()
                                if len(result) == 0:
                                    print("Không có sách nào.")
                                else:
                                    print("==================BẢNG THÔNG TIN SÁCH TẠI STORE=================")
                                    table = PrettyTable()
                                    table.field_names = ["Mã sách", "Tên sách", "Tác giả", "Gía bán", "Số lượng"]
                                    for sach in result:
                                        table.add_row([sach[0], sach[1], sach[2], sach[3], sach[4]])
                                    print(table)
                        except Exception as e:
                            print(f"Lỗi khi lấy danh sách sách: {e}")
                        self.ten_sach = input("Nhập tên sách: ")
                        self.so_luong = int(input("Nhập số lượng sách: "))
                        self.ngay_hoa_don = input("Nhập ngày mua hàng(yyyy/mm/dd): ")
            break
class NhapHang:
    def __init__(self,ma_hang,ma_sach,nha_cung_cap,so_luong,ngay_nhap):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.ma_hang = ma_hang
        self.ma_sach = ma_sach
        self.nha_cung_cap = nha_cung_cap
        self.so_luong = so_luong
        self.ngay_nhap = ngay_nhap
    def nhap_hang(self):
        while True:
            self.ma_hang = input("Nhập mã hàng: ")
            with self.connection.cursor() as cursor:
                sql_check = "SELECT COUNT(*) FROM nhaphang WHERE ma_hang = %s"
                cursor.execute(sql_check, (self.ma_hang,))
                result = cursor.fetchone()
                if result[0] > 0:
                    print("Mã hàng đã tồn tại. Vui lòng nhập lại.")
                else:
                    self.ma_sach = input("Nhập mã sách muốn nhập vào: ")
                    self.nha_cung_cap = input("Nhập nhà cung cấp vào: ")
                    self.so_luong = int(input("Nhập số lượng sách cần nhập: "))
                    self.ngay_nhap = input("Nhập ngày nhập(yyyy/mm/dd): ")
            break
class DonHangOnline:
    def __init__(self,ma_don_hang,ten_khach_hang,ma_sach,so_luong,thoi_gian_dat_hang,dia_chi_giao_hang,phuong_thuc_vc,trang_thai,tong_tien):
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.ma_don_hang = ma_don_hang
        self.ten_khach_han = ten_khach_hang
        self.ma_sach = ma_sach
        self.so_luong = so_luong
        self.thoi_gian_dat_hang = thoi_gian_dat_hang
        self.dia_chi_giao_hang = dia_chi_giao_hang
        self.phuong_thuc_vc = phuong_thuc_vc
        self.trang_thai = trang_thai
        self.tong_tien = tong_tien
    def nhap_don_hang(self):
        while True:
            self.ma_don_hang = input("Nhập mã đơn hàng vào: ")
            with self.connection.cursor() as cursor:
                sql_check = "SELECT COUNT(*) FROM don_hang_onl WHERE ma_don_hang = %s"
                cursor.execute(sql_check, (self.ma_don_hang,))
                result = cursor.fetchone()
                if result[0] > 0:
                    print("Mã đơn hàng đã tồn tại. Vui lòng nhập lại.")
                else:
                    self.ten_khach_hang = input("Nhập tên khách hàng vào: ")
                    self.ma_sach = input("Nhập mã sách: ")
                    self.so_luong = int(input("Nhập số lượng: "))
                    self.thoi_gian_dat_hang = input("Nhập thời gian đặt hàng(yyyy/mm/dd): ")
                    self.dia_chi_giao_hang = input("Nhập địa chỉ giao hàng: ")
                    self.phuong_thuc_vc = input("Nhập phương thức vận chuyển: ")
                    self.trang_thai = input("Nhập trạng thái của hàng: ")
                    self.tong_tien = 0
            break
class qlsach:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.mycursor = self.connection.cursor()
    def them_sach(self, sach):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO sach (ma_sach, ten_sach, tac_gia, gia_ban, so_luong) VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, (sach.ma_sach, sach.ten_sach, sach.tac_gia, sach.gia_ban, sach.so_luong))
                self.connection.commit()
            print("<> Thêm sách thành công <>")
        except Exception as e:
            print(f"<> Lỗi khi thêm sách: {e} <>")
    def xoa_sach(self,ma_sach):
        try:
            with self.connection.cursor() as cursor: 
                sql = "DELETE FROM sach WHERE ma_sach = %s"
                val = (ma_sach,)
                cursor.execute(sql,val)
                self.connection.commit()
            print("<> Xóa sách thành công <>")
        except Exception as e:
            print(f"<> Lỗi khi xóa sách: {e} <>")
    def cap_nhat_sach(self, ma_sach, cot_thay_doi, gia_tri_moi):
        try:
            with self.connection.cursor() as cursor:
                sql = f"UPDATE sach SET {cot_thay_doi} = %s WHERE ma_sach = %s"
                val = (gia_tri_moi, ma_sach)
                cursor.execute(sql, val)
                self.connection.commit()
            print("<> Cập nhật thông tin sách thành công <>")
        except Exception as e:
            print(f"Lỗi cập nhật sách: {e}")
    def tim_kiem_sach(self, tu_khoa,cot_tim_kiem):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM sach WHERE {cot_tim_kiem} LIKE %s"
                val = f"%{tu_khoa}%"
                cursor.execute(sql,(val,))
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có sách nào trong kho <>")
                else:
                    print()
                    print("==================BẢNG THÔNG TIN SÁCH TẠI STORE=================")
                    table = PrettyTable()
                    table.field_names = ["Mã sách", "Tên sách", "Tác giả", "Gía bán", "Số lượng"]
                    for sach in result:
                        table.add_row([sach[0], sach[1], sach[2], sach[3], sach[4]])
                tong_so_luong_sach = sum([sach[4] for sach in result])
                if tong_so_luong_sach < 5:
                    print("<> Sách trong kho còn ít, vui lòng thêm sách vào kho <>")
                else:
                    print(table)
        except Exception as e:
            print(f"Lỗi khi lấy danh sách sách: {e}")
    def lay_danh_sach_sach(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM sach"
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có sách nào trong kho <>")
                else:
                    print()
                    print("==================BẢNG THÔNG TIN SÁCH TẠI STORE=================")
                    table = PrettyTable()
                    table.field_names = ["Mã sách", "Tên sách", "Tác giả", "Gía bán", "Số lượng"]
                    for sach in result:
                        table.add_row([sach[0], sach[1], sach[2], sach[3], sach[4]])
                tong_so_luong_sach = sum([sach[4] for sach in result])
                if tong_so_luong_sach < 5:
                    print("<> Sách trong kho còn ít, vui lòng thêm sách vào kho <>")
                else:
                    print(table)
        except Exception as e:
            print(f"Lỗi khi lấy danh sách sách: {e}")
    def menu(self):
        while True:
                print("="*17+ " QUẢN LÝ SÁCH " + "="*17)
                print("|" + " "*46 + "|")
                print("|{text:<40}|". format(text = "\t1: Lấy danh sách sách"))
                print("|{text:<40}|". format(text = "\t2: Thêm sách"))
                print("|{text:<40}|". format(text = "\t3: Xóa sách"))
                print("|{text:<40}|". format(text = "\t4: Cập nhật sách"))
                print("|{text:<40}|". format(text = "\t5: Tìm kiếm sách"))
                print("|{text:<40}|". format(text = "\t6: Quay lại"))
                print("|{text:<40}|". format(text = "\t7: Thoát"))
                print("|" + " "*46 + "|")
                print("="*48)
                choice = input("Vui lòng chọn chức năng (1-7) giúp cửa hàng >>> ")
                if choice == "1":
                    self.lay_danh_sach_sach()
                elif choice == "2":
                    n = int(input("Nhập số lượng sách vào: "))
                    for i in range(n):
                        print(f"Nhập thông tin sách thứ {i+1}")
                        sach = Sach("","","","","")
                        sach.nhap_sach()
                        self.them_sach(sach)
                elif choice == "3":
                    n = int(input("Nhập số lượng sách cần xóa: "))
                    for i in range(n):
                        ma_sach = int(input(f"Nhập mã sách {i + 1} vào: "))
                        self.xoa_sach(ma_sach)
                elif choice == "3":
                    self.lay_danh_sach_sach()
                elif choice == "4":
                    n = int(input("Nhập số lượng sách muốn cập nhật:"))
                    for i in range(n):
                        ma_sach = int(input(f"Nhập mã sách {i+1}: "))
                        cot_thay_doi = input("""1/ma_sach\n2/ten_sach\n3/tac_gia\n4/gia_ban\n5/so_luong\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                        gia_tri_moi = input("Nhập giá trị cần thay đổi vào: ")
                        self.cap_nhat_sach(ma_sach,cot_thay_doi,gia_tri_moi)
                elif choice == "6":
                    quanlynhasach().menu()
                elif choice == "5":
                    cot_tim_kiem = input("""1/ma_sach\n2/ten_sach\n3/tac_gia\n4/gia_ban\n5/so_luong\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                    tu_khoa = input("Nhập giá trị cần tìm: ")
                    self.tim_kiem_sach(tu_khoa,cot_tim_kiem)
                elif choice == "7":
                    print("<> Hẹn gặp lại quý khách <>")
                    quit()
                else:
                    print("<> Không có chức năng này, vui lòng nhập lại <>")
class qlnv:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.mycursor = self.connection.cursor()
    def them_nhan_vien(self, nhan_vien):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO nhanvien (ma_nv, ten_nv, sdt, dia_chi,email,vi_tri,luong) VALUES (%s, %s, %s, %s,%s, %s, %s)"
                cursor.execute(sql, (nhan_vien.ma_nv, nhan_vien.ten_nv, nhan_vien.sdt, nhan_vien.dia_chi,nhan_vien.email,nhan_vien.vi_tri,nhan_vien.luong))
                self.connection.commit()
            print("<> Thêm nhân viên thành công <>")
        except Exception as e:
            print(f"Lỗi khi thêm nhân viên: {e}")
    def xoa_nhan_vien(self,ma_nv):
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM nhanvien WHERE ma_nv = %s"
                val = (ma_nv,)
                cursor.execute(sql,val)
                self.connection.commit()
            print("<> Đã xóa nhân viên thành công <>")
        except Exception as e:
            print(f"Lỗi khi xóa nhân viên: {e}")
    def cap_nhat_nhan_vien(self, ma_nv, cot_thay_doi, gia_tri_moi):
        try:
            with self.connection.cursor() as cursor:
                sql = f"UPDATE nhanvien SET {cot_thay_doi} = %s WHERE ma_nv = %s"
                val = (gia_tri_moi, ma_nv)
                cursor.execute(sql, val)
                self.connection.commit()
            print("<> Cập nhật thông tin nhân viên thành công <>")
        except Exception as e:
            print(f"Lỗi cập nhật nhân viên: {e}")
    def tim_kiem_nhan_vien(self, tu_khoa,cot_tim_kiem):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM nhanvien WHERE {cot_tim_kiem} LIKE %s"
                val = f"%{tu_khoa}%"
                cursor.execute(sql,(val,))
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có nhân viên nào <>")
                else:
                    print()
                    print("============================BẢNG THÔNG TIN NHÂN VIÊN TẠI STORE========================")
                    table = PrettyTable()
                    table.field_names = ["Mã nhân viên", "Tên nhân viên", "Số điện thoại", "Địa chỉ","Email","Vị trí","Lương"]
                    for nhanvien in result:
                        table.add_row([nhanvien[0], nhanvien[1], nhanvien[2], nhanvien[3],nhanvien[4],nhanvien[5],nhanvien[6]])
                    print(table)
        except Exception as e:
            print(f"Lỗi khi lấy danh sách nhân viên: {e}")
    def lay_danh_sach_nhan_vien(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM nhanvien"
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có nhân viên nào <>")
                else:
                    print()
                    print("============================BẢNG THÔNG TIN NHÂN VIÊN TẠI STORE========================")
                    table = PrettyTable()
                    table.field_names = ["Mã nhân viên", "Tên nhân viên", "Số điện thoại", "Địa chỉ","Email","Vị trí","Lương"]
                    for nhanvien in result:
                        table.add_row([nhanvien[0], nhanvien[1], nhanvien[2], nhanvien[3],nhanvien[4],nhanvien[5],nhanvien[6]])
                    print(table)
        except Exception as e:
            print(f"Lỗi khi lấy danh sách nhân viên: {e}")
    def menu_nv(self):
        while True:
            print("="*17+ " QUẢN LÝ NHÂN VIÊN " + "="*12)
            print("|" + " "*46 + "|")
            print("|{text:<40}|". format(text = "\t1: Lấy danh sách nhân viên"))
            print("|{text:<40}|". format(text = "\t2: Thêm nhân viên"))
            print("|{text:<40}|". format(text = "\t3: Xóa nhân viên"))
            print("|{text:<40}|". format(text = "\t4: Cập nhật thông tin nhân viên"))
            print("|{text:<40}|". format(text = "\t5: Tìm kiếm thông tin nhân viên"))
            print("|{text:<40}|". format(text = "\t6: Quay lại"))
            print("|{text:<40}|". format(text = "\t7: Thoát"))
            print("|" + " "*46 + "|")
            print("="*48)
            choice = input("Vui lòng chọn chức năng (1-7) giúp cửa hàng >>> ")
            if choice == "2":
                n = int(input("Nhập số lượng nhân viên: "))
                for i in range(n):
                    print(f"Nhập thông tin nhân viên thứ {i+1}")
                    nhan_vien = NhanVien("","","","","","","")
                    nhan_vien.nhap_nhan_vien()
                    self.them_nhan_vien(nhan_vien)
            elif choice == "3":
                n = int(input("Nhập số lượng nhân viên muốn xóa:"))
                for i in range(n):
                    ma_nv = int(input(f"Nhập mã nhân viên {i+1} cần xóa: "))
                    self.xoa_nhan_vien(ma_nv)
            elif choice == "4":
                n = int(input("Nhập số lượng nhân viên muốn cập nhật:"))
                for i in range(n):
                    ma_nv = int(input(f"Nhập mã nhân viên {i+1}: "))
                    cot_thay_doi = input("""1/ma_nv\n2/ten_nv\n3/sdt\n4/dia_chi\n5/Email\n6/vi_tri\n7/luong\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                    gia_tri_moi = input("Nhập giá trị mới vào: ")
                    self.cap_nhat_nhan_vien(ma_nv,cot_thay_doi,gia_tri_moi)
            elif choice == "1":
                self.lay_danh_sach_nhan_vien()
            elif choice == "5":
                cot_tim_kiem = input("""1/ma_nv\n2/ten_nv\n3/sdt\n4/dia_chi\n5/Email\n6/vi_tri\n7/luong\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                tu_khoa = input("Nhập giá trị cần tìm: ")
                self.tim_kiem_nhan_vien(tu_khoa,cot_tim_kiem)
            elif choice == "6":
                quanlynhasach().menu()
            elif choice == "7":
                print("<> Hẹn gặp lại quý khách <>")
                quit()
            else:
                print("<> Không có chức năng này, vui lòng nhập lại <>")
class qlkh:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.mycursor = self.connection.cursor()
    def them_khach_hang(self, khach_hang):
        try:
            with self.connection.cursor() as cursor:
                sql = "INSERT INTO khachhang (ma_kh, ten_kh, sdt, dia_chi,email) VALUES (%s, %s, %s, %s,%s)"
                cursor.execute(sql, (khach_hang.ma_kh, khach_hang.ten_kh, khach_hang.sdt, khach_hang.dia_chi,khach_hang.email))
                self.connection.commit()
            print("<> Thêm khách hàng thành công <>")
        except Exception as e:
            print(f"Lỗi khi thêm khách hàng: {e}")
    def xoa_khach_hang(self,ma_kh):
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM khachhang WHERE ma_kh = %s"
                val = (ma_kh,)
                cursor.execute(sql,val)
                self.connection.commit()
            print("<> Đã xóa khách hàng thành công <>")
        except Exception as e:
            print(f"Lỗi khi xóa khách hàng: {e}")
    def cap_nhat_khach_hang(self, ma_kh, cot_thay_doi, gia_tri_moi):
        try:
            with self.connection.cursor() as cursor:
                sql = f"UPDATE khachhang SET {cot_thay_doi} = %s WHERE ma_kh = %s"
                val = (gia_tri_moi, ma_kh)
                cursor.execute(sql, val)
                self.connection.commit()
            print("<> Cập nhật thông tin khách hàng thành công <>")
        except Exception as e:
            print(f"Lỗi cập nhật khách hàng: {e}")
    def tim_kiem_khach_hang(self, tu_khoa,cot_tim_kiem):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM khachhang WHERE {cot_tim_kiem} LIKE %s"
                val = f"%{tu_khoa}%"
                cursor.execute(sql,(val,))
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có khách hàng nào <>")
                else:
                    print()
                    print("==================BẢNG THÔNG TIN KHÁCH HÀNG TẠI STORE===============")
                    table = PrettyTable()
                    table.field_names = ["Mã khách hàng", "Tên khách hàng", "Số điện thoại", "Địa chỉ",'Email']
                    for khachhang in result:
                        table.add_row([khachhang[0], khachhang[1], khachhang[2], khachhang[3],khachhang[4]])
                    print(table)
        except Exception as e:  
            print(f"Lỗi khi lấy danh sách khách hàng: {e}")
    def lay_danh_sach_khach_hang(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM khachhang"
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có khách hàng nào <>")
                else:
                    print()
                    print("==================BẢNG THÔNG TIN KHÁCH HÀNG TẠI STORE===============")
                    table = PrettyTable()
                    table.field_names = ["Mã khách hàng", "Tên khách hàng", "Số điện thoại", "Địa chỉ",'Email']
                    for khachhang in result:
                        table.add_row([khachhang[0], khachhang[1], khachhang[2], khachhang[3],khachhang[4]])
                    print(table)
        except Exception as e:  
            print(f"Lỗi khi lấy danh sách khách hàng: {e}")
    def menu_kh(self):
        while True:
            print("="*17+ " QUẢN LÝ KHÁCH HÀNG " + "="*11)
            print("|" + " "*46 + "|")
            print("|{text:<40}|". format(text = "\t1: Lấy danh sách khách hàng"))
            print("|{text:<40}|". format(text = "\t2: Thêm khách hàng"))
            print("|{text:<40}|". format(text = "\t3: Xóa khách hàng"))
            print("|{text:<40}|". format(text = "\t4: Cập nhật thông tin khách hàng"))
            print("|{text:<40}|". format(text = "\t5: Tìm kiếm thông tin khách hàng"))
            print("|{text:<40}|". format(text = "\t6: Quay lại"))
            print("|{text:<40}|". format(text = "\t7: Thoát"))
            print("|" + " "*46 + "|")
            print("="*48)
            choice = input("Vui lòng chọn chức năng (1-7) giúp cửa hàng >>> ")
            if choice == "2":
                n = int(input("Nhập số lượng khách hàng: "))
                for i in range(n):
                    print(f"Nhập thông tin khách hàng thứ {i+1}")
                    khach_hang = KhachHang("","","","","")
                    khach_hang.nhap_khach_hang()
                    self.them_khach_hang(khach_hang)
            elif choice == "3":
                n = int(input("Nhập số lượng khách hàng bạn muốn xóa: "))
                for i in range(n):
                    ma_kh = int(input(f"Nhập mã khách hàng {i + 1} vào: "))
                    self.xoa_khach_hang(ma_kh)
            elif choice =="4":
                n = int(input("Nhập số lượng khách hàng bạn muốn cập nhật: "))
                for i in range(n):
                    ma_kh = int(input(f"Nhập mã khách hàng {i + 1}: "))
                    cot_thay_doi = input("""1/ma_kh\n2/ten_kh\n3/sdt\n4/dia_chi\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                    gia_tri_moi = input("Nhập giá trị mới vào: ")
                    self.cap_nhat_khach_hang(ma_kh,cot_thay_doi,gia_tri_moi)
            elif choice == "1":
                self.lay_danh_sach_khach_hang()
            elif choice == "5":
                cot_tim_kiem = input("""1/ma_kh\n2/ten_kh\n3/sdt\n4/dia_chi\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                tu_khoa = input("Nhập thông tin cần tìm kiếm: ")
                self.tim_kiem_khach_hang(tu_khoa,cot_tim_kiem)
            elif choice == "6":
                quanlynhasach().menu()
            elif choice == "7":
                print("<> Hẹn gặp lại quý khách <>")
                quit()
            else:
                print("Không có chức năng này, vui lòng chọn lại")
class hoadon:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.mycursor = self.connection.cursor()
    def them_hoa_don(self, hoa_don):
        try:
            with self.connection.cursor() as cursor:
                sql_insert = "INSERT INTO hoadon (ma_hd,ma_kh,ma_sach,ma_nv,ten_sach,so_luong,ngay_hoa_don,tong_tien) VALUES (%s, %s, %s, %s,%s,%s, %s,%s)"
                cursor.execute(sql_insert, (hoa_don.ma_hd, hoa_don.ma_kh,hoa_don.ma_sach, hoa_don.ma_nv, hoa_don.ten_sach, hoa_don.so_luong, hoa_don.ngay_hoa_don, hoa_don.tong_tien))
                self.connection.commit()
                sql_update = "UPDATE sach SET so_luong = so_luong - %s WHERE ma_sach = %s"
                cursor.execute(sql_update, (hoa_don.so_luong, hoa_don.ma_sach))
                self.connection.commit()
            print("<> Nhập hóa đơn thành công <>")
        except Exception as e:
            print(f"Lỗi khi thêm hóa đơn: {e}")
    def cap_nhat_hoa_don(self, ma_hd, cot_thay_doi, gia_tri_moi):
        try:
            with self.connection.cursor() as cursor:
                sql = f"UPDATE hoadon SET {cot_thay_doi} = %s WHERE ma_hd = %s"
                val = (gia_tri_moi, ma_hd)
                cursor.execute(sql, val)
                self.connection.commit()
            print("<> Cập nhật thông tin hóa đơn thành công <>")
        except Exception as e:
            print(f"Lỗi cập nhật hóa đơn: {e}")
    def tinh_tong_tien(self,ma_hd):
        try:
            with self.connection.cursor() as cursor:
                sql_select = "SELECT ma_sach, so_luong FROM hoadon WHERE ma_hd = %s"
                cursor.execute(sql_select, (ma_hd,))
                result = cursor.fetchall()
                tong_tien = 0
                for row in result:
                    ma_sach = row[0]
                    so_luong_mua = row[1]
                    sql_select_sach = "SELECT gia_ban FROM sach WHERE ma_sach = %s"
                    cursor.execute(sql_select_sach, (ma_sach,))
                    result_sach = cursor.fetchone()
                    gia_sach = result_sach[0]
                    tien_loai_sach = gia_sach * so_luong_mua
                    tong_tien += tien_loai_sach
                sql = "UPDATE hoadon SET tong_tien = %s WHERE ma_hd = %s"
                val = (tong_tien,ma_hd)
                cursor.execute(sql,val)
                self.connection.commit()
            print("<> Cập nhật tổng tiền thành công <>")
        except Exception as e:
            print(f"Lỗi khi tính tổng tiền: {e}")
    def xoa_hoa_don(self,ma_hd):
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM hoadon WHERE ma_hd = %s"
                val = (ma_hd,)
                cursor.execute(sql,val)
                self.connection.commit()
            print("<> Xóa hóa đơn thành công <>")
        except Exception as e:
            print(f"Lỗi khi xóa hóa đơn: {e}")
    def tim_kiem_hoa_don(self, tu_khoa,cot_tim_kiem):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM hoadon WHERE {cot_tim_kiem} LIKE %s"
                val = f"%{tu_khoa}%"
                cursor.execute(sql,(val,))
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có hóa đơn nào <>")
                else:
                    print()
                    print("===================================BẢNG THÔNG TIN HÓA ĐƠN TẠI STORE===========================")
                    table = PrettyTable()
                    table.field_names = ["Mã hóa đơn", "Mã khách hàng", "Mã sách","Tên sách","Mã nhân viên","Số lượng",'Ngày mua',"Tổng tiền"]
                    for hoa_don in result:
                        table.add_row([hoa_don[0], hoa_don[1], hoa_don[2], hoa_don[3],hoa_don[4],hoa_don[5],hoa_don[6],hoa_don[7]])
                    print(table)
        except Exception as e:
            print(f"Lỗi khi lấy danh sách hóa đơn: {e}")
    def lay_danh_sach_hoa_don(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM hoadon"
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có hóa đơn nào <>")
                else:
                    print()
                    print("===================================BẢNG THÔNG TIN HÓA ĐƠN TẠI STORE===========================")
                    table = PrettyTable()
                    table.field_names = ["Mã hóa đơn", "Mã khách hàng", "Mã sách","Tên sách","Mã nhân viên","Số lượng",'Ngày mua',"Tổng tiền"]
                    for hoa_don in result:
                        table.add_row([hoa_don[0], hoa_don[1], hoa_don[2], hoa_don[3],hoa_don[4],hoa_don[5],hoa_don[6],hoa_don[7]])
                    print(table)
        except Exception as e:
            print(f"Lỗi khi lấy danh sách hóa đơn: {e}")
    def menu_hd(self):
        while True:
            print("="*17+ " QUẢN LÝ HÓA ĐƠN " + "="*14)
            print("|" + " "*46 + "|")
            print("|{text:<40}|". format(text = "\t1: Lấy danh sách hóa đơn"))
            print("|{text:<40}|". format(text = "\t2: Thêm hóa đơn"))
            print("|{text:<40}|". format(text = "\t3: Thêm tổng tiên vào hóa đơn"))
            print("|{text:<40}|". format(text = "\t4: Xóa hóa đơn"))
            print("|{text:<40}|". format(text = "\t5: Cập nhật thông tin hóa đơn"))
            print("|{text:<40}|". format(text = "\t6: Tìm kiếm thông tin hóa đơn"))
            print("|{text:<40}|". format(text = "\t7: Quay lại"))
            print("|{text:<40}|". format(text = "\t8: Thoát"))
            print("|" + " "*46 + "|")
            print("="*48)
            choice = input("Vui lòng chọn chức năng (1-8) giúp cửa hàng >>> ")
            if choice == "2":
                n = int(input("Nhập số lượng hóa đơn: "))
                for i in range(n):
                    print(f"Nhập thông tin hóa đơn thứ {i+1}")
                    hoa_don = ThongTinMuaHang("","","","","","","","")
                    hoa_don.nhap_thong_tin_mua_hang()
                    self.them_hoa_don(hoa_don)
            elif choice == "4":
                n = int(input("Nhập số lượng hóa đơn muốn xóa:"))
                for i in range(n):
                    ma_hd = int(input(f"Nhập mã hóa đơn {i+1}: "))
                    self.xoa_hoa_don(ma_hd)
            elif choice == "5":
                n = int(input("Nhập số lượng hóa đơn muốn cập nhật:"))
                for i in range(n):
                    ma_hd = int(input(f"Nhập mã hóa đơn {i+1}: "))
                    cot_thay_doi = input("""1/ma_hd\n2/ma_kh\n3/ma_sach\n4/ten_sach\n5/so_luong\n6/ngay_mua\n7/gia_ban\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                    gia_tri_moi = input("Nhập giá trị mới vào: ")
                    self.cap_nhat_hoa_don(ma_hd,cot_thay_doi,gia_tri_moi)
            elif choice == "1":
                self.lay_danh_sach_hoa_don()
            elif choice == "6":
                cot_tim_kiem = input("""1/ma_hd\n2/ma_kh\n3/ma_sach\n4/ten_sach\n5/so_luong\n6/ngay_mua\n7/gia_ban\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                tu_khoa = input("Nhập thông tin bạn muốn tìm: ")
                self.tim_kiem_hoa_don(tu_khoa,cot_tim_kiem)
            elif choice == "7":
                quanlynhasach().menu()
            elif choice =="3":
                n = int(input("Nhập số lượng hóa đơn cần tính: "))
                for i in range(n):
                    ma_hd = int(input(f"Nhập mã hóa đơn {i+1}: "))
                    self.tinh_tong_tien(ma_hd)
            elif choice == "8":
                print("<> Hẹn gặp lại quý khách <>")
                quit()
            else:
                print("Không có chức năng này, vui lòng nhập lại")
class qlnhap_hang:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.mycursor = self.connection.cursor()
    def nhaphang(self, nhap_hang):
        try:
            with self.connection.cursor() as cursor:
                sql_insert = "INSERT INTO nhaphang (ma_hang,ma_sach, nha_cung_cap, so_luong, ngay_nhap) VALUES (%s, %s, %s, %s,%s)"
                cursor.execute(sql_insert, (nhap_hang.ma_hang,nhap_hang.ma_sach, nhap_hang.nha_cung_cap, nhap_hang.so_luong, nhap_hang.ngay_nhap))
                self.connection.commit()
                sql_update = "UPDATE sach SET so_luong = so_luong + %s WHERE ma_sach = %s"
                cursor.execute(sql_update, (nhap_hang.so_luong, nhap_hang.ma_sach))
                self.connection.commit()
            print("<> Nhập hàng thành công <>")
        except Exception as e:
            print(f"Lỗi khi nhập hàng: {e}")
    def sua_nhaphang(self,ma_hang,cot_thay_doi,gia_tri_moi):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM nhaphang"
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có kiện hàng nào <>")
                else:
                    sql = f"UPDATE nhaphang SET {cot_thay_doi} = %s WHERE ma_hang = %s"
                    val = (gia_tri_moi,ma_hang)
                    cursor.execute(sql,val)
                    self.connection.commit()
                    print("<> Cập nhật thông tin thành công <>")
        except Exception as e:
            print(f"Lỗi khi cập nhật kiện hàng: {e}")
    def xoa_hang(self,ma_hang):
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM nhaphang WHERE ma_hang = %s"
                val = (ma_hang)
                cursor.execute(sql,val)
                self.connection.commit()
            print("<> Đã xóa kiện hàng ra khỏi kho <>")
        except Exception as e:
            print(f"Lỗi khi xóa kiện hàng: {e}")
    def lay_thong_tin_hang(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM nhaphang"
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có kiện hàng nào <>")
                else:
                    print()
                    print("===================================BẢNG THÔNG TIN NHẬP HÀNG TẠI STORE========================")
                    table = PrettyTable()
                    table.field_names = ["Mã hàng", "Mã sách", "Nhà cung cấp","Số lượng","Ngày nhập hàng"]
                    for kienhang in result:
                        table.add_row([kienhang[0], kienhang[1], kienhang[2], kienhang[3],kienhang[4]])
                    print(table)
        except Exception as e:
            print(f"Lỗi khi lấy danh sách hàng: {e}")
    def tim_kiem_hang(self, tu_khoa,cot_tim_kiem):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM nhaphang WHERE {cot_tim_kiem} LIKE %s"
                val = f"%{tu_khoa}%"
                cursor.execute(sql,(val,))
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có kiện hàng nào <>")
                else:
                    print()
                    print("===================================BẢNG THÔNG TIN NHẬP HÀNG TẠI STORE========================")
                    table = PrettyTable()
                    table.field_names = ["Mã hàng", "Mã sách", "Nhà cung cấp","Số lượng","Ngày nhập hàng"]
                    for kienhang in result:
                        table.add_row([kienhang[0], kienhang[1], kienhang[2], kienhang[3],kienhang[4]])
                    print(table)
        except Exception as e:
            print(f"Lỗi khi lấy danh sách hàng: {e}")
    def menu(self):
        while True:
            print("="*15+ " QUẢN LÝ HÀNG NHẬP " + "="*15)
            print("|" + " "*46 + "|")
            print("|{text:<40}|". format(text = "\t1: Lấy thông tin kiện hàng"))
            print("|{text:<40}|". format(text = "\t2: Nhập hàng"))
            print("|{text:<40}|". format(text = "\t2: Xóa hàng"))
            print("|{text:<40}|". format(text = "\t4: Sửa thông tin hàng"))
            print("|{text:<40}|". format(text = "\t5: Tìm kiếm thông tin hàng"))
            print("|{text:<40}|". format(text = "\t6: Quay lại"))
            print("|{text:<40}|". format(text = "\t7: Thoát"))
            print("|" + " "*46 + "|")
            print("="*48)
            choice = input("Vui lòng chọn chức năng (1-7) giúp cửa hàng >>> ")
            if choice == "1":
                self.lay_thong_tin_hang()
            elif choice == "2":
                n = int(input("Nhập số lượng hóa đơn: "))
                for i in range(n):
                    print(f"Nhập thông tin kiện hàng {i+1}")
                    nhap_hang = NhapHang("","","","","")
                    nhap_hang.nhap_hang()
                    self.nhaphang(nhap_hang)
            elif choice == "3":
                n = int(input("Nhập số lượng hàng cần xóa: "))
                for i in range(n):
                    ma_hang = input(f"Nhập mã hàng {i + 1} cần xóa: ")
                    self.xoa_hang(ma_hang)
            elif choice == "4":
                n = int(input("Nhập số lượng hàng cần cập nhật: "))
                for i in range(n):
                    ma_hang = input(f"Nhập mã của kiện hàng {i+1}: ")
                    cot_thay_doi = input("""1/ma_hang\n2/ma_sach\n3/nha_cung_cap\n4/so_luong\n5/ngay_nhap\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                    gia_tri_moi = input("Nhập giá trị mới: ")
                    self.sua_nhaphang(ma_hang,cot_thay_doi,gia_tri_moi)
            elif choice == "5":
                cot_tim_kiem = input("""1/ma_hang\n2/ma_sach\n3/nha_cung_cap\n4/so_luong\n5/ngay_nhap\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                tu_khoa = input("Nhập từ khóa bạn muốn tìm kiếm: ")
                self.tim_kiem_hang(tu_khoa,cot_tim_kiem)
            elif choice == "6":
                quanlynhasach().menu()
            elif choice == "7":
                print("<> Hẹn gặp lại quý khách <>")
                quit()
            else:
                print("Không có chức năng nào như trên, vui lòng nhập lại")
                qlnhap_hang().menu()
class ql_online:
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "11082003",
            database = "qlns"
            )
        self.mycursor = self.connection.cursor()
    def them_hoa_don_wb(self,hoa_don_onl):
        try:
            with self.connection.cursor() as cursor:
                sql_insert = "INSERT INTO don_hang_onl (ma_don_hang,ten_khach_hang,ma_sach,so_luong,thoi_gian_dat_hang,dia_chi_giao_hang,phuong_thuc_vc,trang_thai,tong_tien) VALUES (%s, %s, %s, %s,%s,%s, %s, %s,%s)"
                val = (hoa_don_onl.ma_don_hang, hoa_don_onl.ten_khach_hang, hoa_don_onl.ma_sach, hoa_don_onl.so_luong, hoa_don_onl.thoi_gian_dat_hang, hoa_don_onl.dia_chi_giao_hang, hoa_don_onl.phuong_thuc_vc, hoa_don_onl.trang_thai,hoa_don_onl.tong_tien)
                cursor.execute(sql_insert, val)
                self.connection.commit()
                sql_update = "UPDATE sach SET so_luong = so_luong - %s WHERE ma_sach = %s"
                cursor.execute(sql_update, (hoa_don_onl.so_luong, hoa_don_onl.ma_sach))
                self.connection.commit()
            print("<> Thêm hóa đơn thành công <>")
        except Exception as e:
            print(f"Lỗi khi thêm hóa đơn: {e}")
    def tinh_tong_tien_web(self,ma_don_hang):
        try:
            with self.connection.cursor() as cursor:
                sql_select = "SELECT ma_sach, so_luong FROM don_hang_onl WHERE ma_don_hang = %s"
                cursor.execute(sql_select, (ma_don_hang,))
                result = cursor.fetchall()
                tong_tien = 0
                for row in result:
                    ma_sach = row[0]
                    so_luong_mua = row[1]
                    sql_select_sach = "SELECT gia_ban FROM sach WHERE ma_sach = %s"
                    cursor.execute(sql_select_sach, (ma_sach,))
                    result_sach = cursor.fetchone()
                    gia_sach = result_sach[0]
                    tien_loai_sach = gia_sach * so_luong_mua
                    tong_tien += tien_loai_sach
                sql = "UPDATE don_hang_onl SET tong_tien = %s WHERE ma_don_hang = %s"
                val = (tong_tien,ma_don_hang)
                cursor.execute(sql,val)
                self.connection.commit()
            print("<> Cập nhật tổng tiền thành công <>")
        except Exception as e:
            print(f"Lỗi khi tính tổng tiền: {e}")
    def xoa_hd_web(self,ma_don_hang):
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM don_hang_onl WHERE ma_don_hang = %s"
                val = (ma_don_hang,)
                cursor.execute(sql,val)
                self.connection.commit()
            print("<> Đã xóa đơn hàng thành công <>")
        except Exception as e:
            print(f"Lỗi khi xóa đơn hàng: {e}")
    def sua_thong_tin_web(self,ma_don_hang,cot_thay_doi,gia_tri_moi):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM don_hang_onl"
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có đơn hàng online nào <>")
                else:
                    sql = f"UPDATE don_hang_onl SET {cot_thay_doi} = %s WHERE ma_don_hang = %s"
                    val = (gia_tri_moi,ma_don_hang)
                    cursor.execute(sql,val)
                    self.connection.commit()
                    print("<> Cập nhật thông tin thành công <>")
        except Exception as e:
            print(f"Lỗi khi cập nhật đơn hàng: {e}")
    def tim_kiem_hang_web(self, tu_khoa,cot_tim_kiem):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM don_hang_onl WHERE {cot_tim_kiem} LIKE %s"
                val = f"%{tu_khoa}%"
                cursor.execute(sql,(val,))
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có đơn hàng online nào <>")
                else:
                    print()
                    print("===================================BẢNG THÔNG TIN HÓA ĐƠN ONLINE TẠI STORE========================")
                    table = PrettyTable()
                    table.field_names = ["Mã đơn hàng","Tên khách hàng","Mã sách","Số lượng","Thời gian đặt hàng","Địa chỉ giao hàng","Phương thức vận chuyển","Trạng thái","Tổng tiền"]
                    for hdwb in result:
                        table.add_row([hdwb[0], hdwb[1], hdwb[2], hdwb[3],hdwb[4], hdwb[5], hdwb[6], hdwb[7],hdwb[8]])
                    print(table)
        except Exception as e:
            print(f"Lỗi khi lấy danh sách hóa đơn: {e}")
    def lay_thong_tin_web(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM don_hang_onl"
                cursor.execute(sql)
                result = cursor.fetchall()
                if len(result) == 0:
                    print("<> Không có hóa đơn online nào <>")
                else:
                    print()
                    print("===================================BẢNG THÔNG TIN HÓA ĐƠN ONLINE TẠI STORE========================")
                    table = PrettyTable()
                    table.field_names = ["Mã đơn hàng","Tên khách hàng","Mã sách","Số lượng","Thời gian đặt hàng","Địa chỉ giao hàng","Phương thức vận chuyển","Trạng thái","Tổng tiền"]
                    for hdwb in result:
                        table.add_row([hdwb[0], hdwb[1], hdwb[2], hdwb[3],hdwb[4], hdwb[5], hdwb[6], hdwb[7],hdwb[8]])
                    print(table)
        except Exception as e:
            print(f"Lỗi khi lấy danh sách hóa đơn: {e}")
    def menu(self):
        while True:
            print("="*15+ " QUẢN LÝ NHÀ SÁCH " + "="*15)
            print("|" + " "*46 + "|")
            print("|{text:<40}|". format(text = "\t1: Lấy danh sách hóa đơn"))
            print("|{text:<40}|". format(text = "\t2: Thêm hóa đơn"))
            print("|{text:<40}|". format(text = "\t3: Cập nhật tổng tiền"))
            print("|{text:<40}|". format(text = "\t4: Xóa thông tin hóa đơn"))
            print("|{text:<40}|". format(text = "\t5: Cập nhật thông tin hóa đơn"))
            print("|{text:<40}|". format(text = "\t6: Tìm kiếm thông tin hóa đơn"))
            print("|{text:<40}|". format(text = "\t7: Quay lại"))
            print("|{text:<40}|". format(text = "\t8: Thoát"))
            print("|" + " "*46 + "|")
            print("="*48)
            choice = input("Mời bạn vui lòng chọn chức năng từ (1-8) giúp cửa hàng >>> ")
            if choice == "1":
                self.lay_thong_tin_web()
            elif choice == "2":
                n = int(input("Nhập số lượng hóa đơn: "))
                for i in range(n):
                    print(f"Nhập thông tin hóa đơn thứ {i+1}")
                    hoa_don_onl = DonHangOnline("","","","","","","","","")
                    hoa_don_onl.nhap_don_hang()
                    self.them_hoa_don_wb(hoa_don_onl)
            elif choice == "3":
                n = int(input("Nhập số lượng hóa đơn cần tính: "))
                for i in range(n):
                    ma_don_hang = input("Nhập mã hóa đơn vào: ")
                    self.tinh_tong_tien_web(ma_don_hang)
            elif choice == "4":
                n = int(input("Nhập số lượng hóa đơn cần xóa: "))
                for i in range(n):
                    ma_don_hang = input(f"Nhập mã hóa đơn {i+1}: ")
                    self.xoa_hd_web(ma_don_hang)
            elif choice == "5":
                n = int(input("Nhập số lượng hóa đơn cần cập nhật: "))
                for i in range(n):
                    ma_don_hang = input(f"Nhập mã hóa đơn {i+1}: ")
                    cot_thay_doi = input("""1/ma_don_hang\n2/ten_khach_hang\n3/ma_sach\n4/so_luong\n5/thoi_gian_dat_hang\n6/dia_chi_giao_hang\n7/phuong_thuc_vc\n8/trang_thai\n9/tong_tien\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                    gia_tri_moi = input("Nhập giá trị mới vào: ")
                    self.sua_thong_tin_web(ma_don_hang,cot_thay_doi,gia_tri_moi)
            elif choice == "6":
                cot_tim_kiem = input("""1/ma_don_hang\n2/ten_khach_hang\n3/ma_sach\n4/so_luong\n5/thoi_gian_dat_hang\n6/dia_chi_giao_hang\n7/phuong_thuc_vc\n8/trang_thai\n9/tong_tien\nMời bạn nhập tên cột (nhập đúng tên cột như bên trên): """)
                tu_khoa = input("Nhập thông tin bạn muốn tìm: ")
                self.tim_kiem_hang_web(tu_khoa,cot_tim_kiem)
            elif choice == "7":
                quanlynhasach().menu()
            elif choice == "8":
                print("<> Hẹn gặp lại <>")
                quit()
            else:
                print("<> Không có chức năng như trên vui lòng nhập lại! <>")
                ql_online().menu()
class quanlynhasach:
    def menu(self):
        print("="*15+ " QUẢN LÝ NHÀ SÁCH " + "="*15)
        print("|" + " "*46 + "|")
        print("|{text:<40}|". format(text = "\t1: Quản lý sách"))
        print("|{text:<40}|". format(text = "\t2: Quản lý nhân viên"))
        print("|{text:<40}|". format(text = "\t3: Quản lý khách hàng"))
        print("|{text:<40}|". format(text = "\t4: Quản lý hóa đơn"))
        print("|{text:<40}|". format(text = "\t5: Quản lý nhập hàng"))
        print("|{text:<40}|". format(text = "\t6: Quản lý hóa đơn online"))
        print("|{text:<40}|". format(text = "\t7: Thoát"))
        print("|" + " "*46 + "|")
        print("="*48)
        choice = input("Mời bạn vui lòng chọn chức năng từ (1-7) >>> ")
        if choice == "1":
            qlsach().menu()
        elif choice == "2":
            qlnv().menu_nv()
        elif choice == "3":
            qlkh().menu_kh()
        elif choice == "4":
            hoadon().menu_hd()
        elif choice == "5":
            qlnhap_hang().menu()
        elif choice == "6":
            ql_online().menu()
        elif choice == "7":
            print("<> Hẹn gặp lại quý khách <>")
            quit()
        else:
            print("Không có chức năng này, vui lòng chọn lại")
            quanlynhasach().menu()          
def main():
    for i in range(70):
        os.system('cls')
        print("{test:^70}".format(test = "CHÀO MỪNG ĐẾN VỚI CỬA HÀNG CỦA CHÚNG TÔI"))
        print()
        print("[{test:<70}]".format(test = ">"*i))
        print("{test:>70}".format(test = "LOADING " + str(round((i/70)*100)) + "%"))
        time.sleep(0.02)
    quanlynhasach().menu()
main()