#greeting
#thông số cơ bản
import random
def dv_tien(so_du):
    ty = int(so_du// 1000000000)
    trieu = int((so_du - ty*1000000000)//1000000)
    nghin = int((so_du - ty*1000000000 - trieu*1000000)//1000)
    tep = (so_du - ty*1000000000 - trieu*1000000 - nghin*1000)
    return ty, trieu, nghin, tep
def chuyen_doi(c):
    c = list(c)
    d = c
    if d[1].lower() == "tỷ":
        c = float(d[0])
        so_tien = c*1000000000
        if len(d) >= 4:
            if d[3].lower() == "triệu":
                c = float(d[2])
                so_tien = so_tien + c*1000000
                if len(d) >= 6:
                    if d[5].lower() == "nghìn":
                        c = float(d[4])
                        so_tien = so_tien + c*1000
                        if len(d) == 8:
                            c = float(d[6])
                            so_tien = so_tien + c
                    elif d[5].lower() == "tép":
                        c = float(d[4])
                        so_tien = so_tien + c
            elif d[3].lower() == "nghìn":
                c = float(d[2])
                so_tien = so_tien + c*1000
                if len(d) == 6:
                    c = float(d[4])
                    so_tien = so_tien + c
            elif d[3].lower() == "tép":
                c = float(d[2])
                so_tien = so_tien + c
    elif d[1].lower() == "triệu":
        c = float(d[0])
        so_tien = c*1000000
        if len(d) >= 4:
            if d[3].lower() == "nghìn":
                c = float(d[2])
                so_tien = so_tien + c*1000
                if len(d) == 6:
                    c = float(d[4])
                    so_tien = so_tien + c
            elif d[3].lower() == "tép":
                c = float(d[2])
                so_tien = so_tien + c
    elif d[1].lower() == "nghìn":
        c = float(d[0])
        so_tien = c*1000
        if len(d) == 4:
            c = float(d[2])
            so_tien = so_tien + c
    elif d[1].lower() == "tép":
        c = float(d[0])
        so_tien = c
    elif d[0].lower() == "all" and d[1].lower() == "in":
        so_tien = so_du
    return so_tien
print("ĐÂY CHỈ LÀ 1 CHƯƠNG TRÌNH NHẰM MỤC ĐÍCH GIẢI TRÍ, KHÔNG LIÊN QUAN ĐẾN TIỀN BẠC VÀ KHÔNG CỔ XUÝ HÀNH VI VI PHẠM PHÁP LUẬT")
die = 0
z = 0
tien_vay = 0
so_lan_vay = 0
so_lan_choi = 0
tien_cuoc = 0
tien_vay_nh = 0
tien_vay_nl = 0
lua_chon_dau = 0
tg_vay_nh = 0
tg_vay_nl = 0
nh_cuong_che = 0
nl_doi_no = 0
sl_vay_nh = 0
sl_vay_nl = 0
tinh_trang_vay_nh = "không vay"
tinh_trang_vay_nl = "không vay"
print("Dưới đây là các tầng lớp và thông tin của từng tầng lớp (tất nhiên là bịa ra)")
print("(5%)     Hộ nghèo & cận nghèo. Tài sản ròng: gần như không có.         Thu nhập hàng năm: <36 triệu vnđ")
print("(64,389%)Lao động phổ thông.   Tài sản ròng: <500 triệu vnđ.           Thu nhập hàng năm: 80-150 triệu vnđ")
print("(25%)    Cận trung lưu.        Tài sản ròng: 500 triệu - 2 tỷ vnđ.     Thu nhập hàng năm: 150-500 triệu vnđ")
print("(5%)     Trung lưu.            Tài sản ròng: 2-10 tỷ vnđ.              Thu nhập hàng năm: 500 triệu - 2 tỷ vnđ")
print("(0,5%)   Thượng lưu.           Tài sản ròng: 10-100 tỷ vnđ.            Thu nhập hàng năm: 2-20 tỷ vnđ")
print("(0,1%)   Siêu giàu.            Tài sản ròng: 100-1000 tỷ vnđ.          Thu nhập hàng năm: 20-200 tỷ vnđ")
print("(0,01%)  Siêu siêu giàu.       Tài sản ròng: >1000 tỷ vnđ.             Thu nhập hàng năm: >200 tỷ vnđ")
print("(0,001%) Quý tộc mới.          Tài sản ròng: trăm triệu - hàng tỷ USD. Thu nhập hàng năm: chục - trăm triệu USD")
mong_muon = input("Bạn muốn trở thành tầng lớp nào? (chỉ là mong muốn thôi, viết linh tinh gì cũng được): ")
tang_lop = random.randint(1,100000)
print("-------------------------------------------------------------------------")
if tang_lop <= 5000 :
    print("Bạn thuộc hộ nghèo & cận nghèo, số dư của bạn sẽ random từ 500 nghìn đến 3 triệu")
    so_du = random.randint(500,3000)*1000
elif 5000 < tang_lop <= 69389 :
    print("Bạn thuộc giai cấp lao động phổ thông, số dư của bạn sẽ random từ 6 triệu rưỡi đến 12 triệu rưỡi")
    so_du = random.randint(6500,12500)*1000
elif 69389 < tang_lop <= 94389 :
    print("Bạn thuộc giới cận trung lưu , số dư của bạn sẽ random từ 13 triệu đến 42 triệu")
    so_du = random.randint(13,42)*1000000
elif 94389 < tang_lop <= 99389 :
    print("Bạn thuộc giới trung lưu , số dư của bạn sẽ random từ 42 triệu đến 160 triệu")
    so_du = random.randint(42,160)*1000000
elif 99389 < tang_lop <= 99889 :
    print("Bạn thuộc giới thượng lưu , số dư của bạn sẽ random từ 166 triệu đến 1,666 tỷ")
    so_du = random.randint(166,1666)*1000000
elif 99889 < tang_lop <= 99989 :
    print("Bạn thuộc giới siêu giàu , số dư của bạn sẽ random từ 1,7 tỷ đến 17 tỷ")
    so_du = random.randint(17,170)*100000000
elif 99989 < tang_lop <= 99999 :
    print("Bạn thuộc giới siêu siêu giàu , số dư của bạn sẽ random từ 20 tỷ đến 50 tỷ")
    so_du = random.randint(20,50)*1000000000
elif tang_lop == 100000 :
    print("Bạn thuộc tầng lớp quý tộc mới , số dư của bạn sẽ random từ 200 tỷ đến 1000 tỷ")
    so_du = random.randint(2,10)*100000000000
ty, trieu, nghin, tep = dv_tien(so_du)
print("Số dư hiện tại của bạn là :",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
print("-------------------------------------------------------------------------")
so_du_goc = so_du
#chọn phương án
while lua_chon_dau < 1:
    ty_nh, trieu_nh, nghin_nh, tep_nh = dv_tien(tien_vay_nh)
    ty_nl, trieu_nl, nghin_nl, tep_nl = dv_tien(tien_vay_nl)
    print("Bạn muốn chọn phương án nào?")
    print("1.Cược và bắt đầu đánh")
    print("2.Vay ngân hàng")
    print("3.Vay nặng lãi")
    print("4.Trả nợ")
    print("5.Thông tin về vay nợ (tất nhiên là bịa ra)")
    print("6.Không chơi nữa")
    phuong_an = int(input("Chọn số tương ứng với phương án :"))
    if phuong_an == 5:
        print("-------------------------------------------------------------------------")
        print("Bạn chỉ vay được 1 bên 1 lần. Ví dụ: bạn đang vay ngân hàng thì sẽ không vay tiếp được, nhưng vẫn sẽ vay nặng lãi được và ngược lại")
        print("VAY NGÂN HÀNG: vay không lãi suất nhưng chỉ vay được số tiền bé hơn hoặc bằng số dư bạn đang có và sẽ bắt buộc trả sau 5 lần chơi (nếu chưa trả)")
        print("")
        print("VAY NẶNG LÃI: vay với lãi suất 700% (tăng sau 3 lần chơi), giới hạn vay là 10 tỷ và bắt buộc trả sau 10 lần chơi")
        print("Nếu không thể trả đủ số tiền vay nặng lãi thì bạn sẽ bị đánh chết và không thể chơi được nữa")
        print("Trả nợ là trả thẳng 1 lần ko có trả từ từ (thằng ngu nó lười viết)")
        print("-------------------------------------------------------------------------")
    elif phuong_an == 6:
        lua_chon_dau += 1
    elif phuong_an == 4 :
        print("-------------------------------------------------------------------------")
        if tien_vay_nh == 0 and tien_vay_nl == 0:
            print("Bạn không có khoản nợ nào để trả")
        else :
            print("Bạn muốn trả bên nào?")
            print("1. Ngân hàng (đang nợ",ty_nh,"tỷ",trieu_nh,"triệu",nghin_nh,"nghìn",tep_nh,"tép)")
            print("2. Nặng lãi (đang nợ",ty_nl,"tỷ",trieu_nl,"triệu",nghin_nl,"nghìn",tep_nl,"tép)")
            print("3. Cả 2")
            tra_no = int(input("Chọn số của phương án:"))
            if tra_no == 1:
                if so_du < tien_vay_nh:
                    ty, trieu, nghin, tep = dv_tien(so_du)
                    print("Số dư của bạn không đủ để trả cho ngân hàng (Số dư của bạn là:",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
                else:
                    so_du = so_du - tien_vay_nh
                    tien_vay_nh = 0
                    tg_vay_nh = 0
                    tinh_trang_vay_nh = "không vay"
                    ty, trieu, nghin, tep = dv_tien(so_du)
                    print("Sau khi trả nợ thì số dư của bạn là:",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
            elif tra_no == 2:
                if so_du < tien_vay_nl:
                    ty, trieu, nghin, tep = dv_tien(so_du)
                    print("Số dư của bạn không đủ để trả vay nặng lãi (Số dư của bạn là:",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
                else:
                    so_du = so_du - tien_vay_nl
                    tien_vay_nl = 0
                    tg_vay_nl = 0
                    tinh_trang_vay_nl = "không vay"
                    ty, trieu, nghin, tep = dv_tien(so_du)
                    print("Sau khi trả nợ thì số dư của bạn là:",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
            elif tra_no == 3:
                if so_du < tien_vay_nh or so_du < tien_vay_nl:
                    ty, trieu, nghin, tep = dv_tien(so_du)
                    print("Số dư của bạn không đủ để trả vay nặng lãi (Số dư của bạn là:",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
                else:
                    so_du = so_du - tien_vay_nh - tien_vay_nl
                    tien_vay_nl = 0
                    tien_vay_nh = 0
                    tg_vay_nh = 0
                    tg_vay_nl = 0
                    tinh_trang_vay_nl = "không vay"
                    tinh_trang_vay_nh = "không vay"
                    ty, trieu, nghin, tep = dv_tien(so_du)
                    print("Sau khi trả nợ thì số dư của bạn là:",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
        print("-------------------------------------------------------------------------")
    elif phuong_an == 2:
        print("-------------------------------------------------------------------------")
        if nh_cuong_che == 6:
            print("Bạn đã bị coi là nợ xấu và không thể vay ngân hàng được nữa")
        elif tinh_trang_vay_nh == "đang vay":
            print("Bạn đang vay ngân hàng",ty_nh,"tỷ",trieu_nh,"triệu",nghin_nh,"nghìn",tep_nh,"tép nên không thể vay tiếp")
        elif tinh_trang_vay_nh == "không vay":
            vay_nh = map(str, input("Số tiền bạn muốn vay :").split(" "))
            tien_vay_nh = chuyen_doi(vay_nh)
            if tien_vay_nh >= 100000000000:
                tien_vay_nh = 0
                print("Ngân hàng này quá phèn, thậm chí còn ko có đủ 1 nghìn tỷ cho bạn vay")
            elif tien_vay_nh > so_du :
                tien_vay_nh = 0
                ty, trieu, nghin, tep = dv_tien(so_du)
                print("Bạn không thể vay số tiền nhiều hơn số dư (Số dư của bạn là :",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep,")")
            else:
                so_du = so_du + tien_vay_nh
                tinh_trang_vay_nh = "đang vay"
                ty, trieu, nghin, tep = dv_tien(so_du)
                print("Sau khi vay ngân hàng thì số dư của bạn là :",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
                sl_vay_nh += 1
        print("-------------------------------------------------------------------------")
    elif phuong_an == 3:
        print("-------------------------------------------------------------------------")
        if tinh_trang_vay_nl == "đang vay":
            print("Bạn đang vay nặng lãi",ty_nl,"tỷ",trieu_nl,"triệu",nghin_nl,"nghìn",tep_nl,"tép nên không thể vay tiếp")
        elif tinh_trang_vay_nl == "không vay":
            vay_nl = map(str, input("Số tiền bạn muốn vay :").split(" "))
            tien_vay_nl = chuyen_doi(vay_nl)
            if tien_vay_nl >= 10000000000:
                print("Bọn vay nặng lãi không chấp nhận cho bạn vay 10 tỷ (Hãy thử vay 9 tỷ 999 triệu 999 nghìn 999 =))))")
                tien_vay_nl = 0
            else:
                so_du = so_du + tien_vay_nl
                tinh_trang_vay_nl = "đang vay"
                ty, trieu, nghin, tep = dv_tien(so_du)
                print("Sau khi vay nặng lãi thì số dư của bạn là :",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
                sl_vay_nl += 1
        print("-------------------------------------------------------------------------")
    elif phuong_an == 1:
        if so_du <= 0:
            print("Bạn không thể chơi vì không có đồng nào trong người")
            z += 1
        elif so_du > 0:
            lua_chon_taixiu = input("Bạn chọn tài hay xỉu :")
            while True:
                tien_cuoc = map(str, input("Bạn cược :").split(" "))
                tien_cuoc = chuyen_doi(tien_cuoc)
                if tien_cuoc > so_du:
                    print("Số tiền của bạn không đủ để cược")
                    ty, trieu, nghin, tep = dv_tien(so_du)
                    print("Bạn chỉ có :",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
                    print("Vui lòng cược lại")
                elif tien_cuoc <= 0:
                    print("Mày cược cái đéo gì vậy???")
                    print("Cược lại đi thằng đần")
                elif tien_cuoc <= so_du :
                    break
            so_du = so_du - tien_cuoc
            z = 0
            so_lan_choi += 1
#bắt đầu chơi
        while z < 1:
            xuc_sac1 = random.randint(1,6)
            xuc_sac2 = random.randint(1,6)
            xuc_sac3 = random.randint(1,6)
            tong_diem = xuc_sac1 + xuc_sac2 + xuc_sac3
            print("Bắt đầu nặn")
            print("Phát súng đầu tiên :",xuc_sac1,"chấm")
            lua_chon_nan1 = input("Bạn muốn nặn tiếp không?(Nếu dừng lại sẽ mất 30% tiền cược):")
            if lua_chon_nan1.lower() == "có":
                print("Phát súng thứ hai :",xuc_sac2,"chấm")
                lua_chon_nan2 = input("Bạn muốn nặn tiếp không?(Nếu dừng lại sẽ mất 60% tiền cược):")
                if lua_chon_nan2.lower() == "có":
                    print("Phát súng cuối cùng :",xuc_sac3,"chấm")
                    if tong_diem <= 10 :
                        print("Kết quả là XỈU")
                        if lua_chon_taixiu.lower() == "xỉu":
                            print("Chúc mừng, bạn bú thêm 80% tiền cược")
                            so_du = so_du + tien_cuoc*1.8
                        elif lua_chon_taixiu.lower() == "tài":
                            print("Đen như chó, bạn mất hết tiền cược")
                            so_du = so_du
                    if tong_diem >= 11 :
                        print("Kết quả là TÀI")
                        if lua_chon_taixiu.lower() == "xỉu":
                            print("Bạn mất hết tiền cược")
                            so_du = so_du
                        elif lua_chon_taixiu.lower() == "tài":
                            print("Bạn bú thêm 80% tiền cược")
                            so_du = so_du + tien_cuoc*1.8
                elif lua_chon_nan2.lower() == "không":
                    if tong_diem <= 10 :
                        print("Kết quả là XỈU")
                        if (lua_chon_taixiu.lower() == "xỉu") and (xuc_sac1 + xuc_sac2 > 4):
                            print("Khá đen, bạn mất 60% tiền cược")
                            so_du = so_du + tien_cuoc*0.4
                        elif (lua_chon_taixiu.lower() == "tài") and (xuc_sac1 + xuc_sac2 > 4):
                            print("Hơi may mắn, bạn chỉ mất 60% tiền cược")
                            so_du = so_du + tien_cuoc*0.4
                        elif (lua_chon_taixiu.lower() == "tài") and (xuc_sac1 + xuc_sac2 <= 4):
                            print("Không mả cha mày, định ăn gian hả?")
                            so_du = so_du
                    elif tong_diem >= 11 :
                        print("Kết quả là TÀI")
                        if (lua_chon_taixiu.lower() == "xỉu") and (xuc_sac1 + xuc_sac2 < 10):
                            print("Hơi may mắn, bạn chỉ mất 60% tiền cược")
                            so_du = so_du + tien_cuoc*0.4
                        elif (lua_chon_taixiu.lower() == "tài") and (xuc_sac1 + xuc_sac2 < 10):
                            print("Khá đen, bạn mất 60% tiền cược")
                            so_du = so_du + tien_cuoc*0.4
                        elif (lua_chon_taixiu.lower() == "xỉu") and (xuc_sac1 + xuc_sac2 >= 10):
                            print("Không cái đéo gì, thích ăn gian ko")
                            so_du = so_du
            elif lua_chon_nan1.lower() == "không":
                if tong_diem <= 10 :
                    print("Kết quả là XỈU")
                    if lua_chon_taixiu.lower() == "xỉu":
                        print("Hơi đen, bạn mất 30% tiền cược")
                        so_du = so_du + tien_cuoc*0.7
                    elif lua_chon_taixiu.lower() == "tài":
                        print("Khá may mắn, bạn chỉ mất 30% tiền cược")
                        so_du = so_du + tien_cuoc*0.7
                elif tong_diem >= 11 :
                    print("Kết quả là TÀI")
                    if lua_chon_taixiu.lower() == "xỉu":
                        print("Khá may mắn, bạn chỉ mất 30% tiền cược")
                        so_du = so_du + tien_cuoc*0.7
                    elif lua_chon_taixiu.lower() == "tài":
                        print("Hơi đen, bạn mất 30% tiền cược")
                        so_du = so_du + tien_cuoc*0.7
            break
#đã chơi xong
        if tinh_trang_vay_nh == "đang vay":
            tg_vay_nh += 1
            if tg_vay_nh == 3:
                print("Bạn đã bị ngân hàng cưỡng chế trả nợ")
                so_du = so_du - tien_vay_nh
                tien_vay_nh = 0
                tinh_trang_vay_nh = "không vay"
                tg_vay_nh = 0
                nh_cuong_che += 1
                ty, trieu, nghin, tep = dv_tien(so_du)
                if so_du > 0 :
                    print("Sau khi bị ngân hàng cưỡng chế trả nợ thì số dư của bạn là :",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
                elif so_du <= 0 :
                    so_du = 0
                    print("Vì số dư của bạn ít hơn tiền vay ngân hàng nên số tiền còn thiếu thì ngân hàng sẽ tha cho bạn")
            else:
                print("Bạn còn",3-tg_vay_nh,"lần để chơi trước khi bị ép trả nợ ngân hàng")
        if tinh_trang_vay_nl == "đang vay":
            tg_vay_nl += 1
            nl_doi_no += 1
            if tg_vay_nl == 3:
                tien_vay_nl *= 7
                tg_vay_nl = 0
                ty_nl, trieu_nl, nghin_nl, tep_nl = dv_tien(tien_vay_nl)
                print("Bọn nặng lãi đã tính lãi suất, tiền vay nặng lãi bây giờ là:",ty_nl,"tỷ",trieu_nl,"triệu",nghin_nl,"nghìn",tep_nl,"tép, hãy trả nhanh nhất có thể")
            if nl_doi_no == 10:
                print("Bạn đã bị bọn đòi nợ đánh đập 1 trận và bị chúng tịch thu số tiền vay nặng lãi")
                so_du = so_du - tien_vay_nl
                tinh_trang_vay_nl = "không vay"
                tg_vay_nl = 0
                nl_doi_no = 0
                ty, trieu, nghin, tep = dv_tien(so_du)
                if so_du >= tien_vay_nl:
                    print("Sau khi bị bọn đòi nợ thu tiền thì số dư của bạn là :",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
                elif so_du < tien_vay_nl:
                    print("Vì bạn không thể trả đủ tiền nên đã bị bọn đòi nặng lãi đánh chết")
                    die += 1
            else:
                print("Bạn còn",3-tg_vay_nl,"lần để chơi trước khi bọn nặng lãi tăng lãi")
                print("Bạn còn",10-tg_vay_nl,"lần để chơi trước khi bị ép trả nợ nặng lãi")
#code cũ từ đây trở xuống
        if die == 1:
            print("Bạn đã chết")
            z += 1
            lua_chon_dau += 1
        elif so_du == 0:
            print("Bạn đã hết tiền")
            if tinh_trang_vay_nh == "đang vay" and tinh_trang_vay_nl == "đang vay":
                print("Chúc mừng bạn đã tay trắng và không còn nơi nào để vay, và giờ thì cút")
                z += 1
                lua_chon_dau += 1
            elif tinh_trang_vay_nh == "đang vay" :
                print("Bạn phải vay nặng lãi để có thể chơi tiếp")
            elif tinh_trang_vay_nl == "đang vay":
                print("Bạn phải vay ngân hàng để có thể chơi tiếp")
        elif so_du > 0:
            ty, trieu, nghin, tep = dv_tien(so_du)
            print("Số dư hiện tại của bạn là:",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep)
            lua_chon_choi_tiep = input("Bạn có muốn chơi tiếp không? :")
            if lua_chon_choi_tiep == "không" or lua_chon_choi_tiep == "Không":
                lua_chon_dau += 1
#kết thúc
if die == 1:
    print("Trùng sinh thôi")
elif (so_du_goc > so_du) and (so_du > 0) :
    ty, trieu, nghin, tep = dv_tien(so_du)
    print("Bạn lỗ:",so_du_goc - so_du,"vnđ")
    print("Số dư còn lại của bạn là:",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep,"với",so_lan_choi,"lần chơi,",sl_vay_nh,"lần vay ngân hàng và",sl_vay_nl,"số lần vay nặng lãi")
    if nh_cuong_che == 5:
        print("Đồng thời bạn còn đéo vay được ngân hàng nữa")
elif so_lan_choi == 0 :
    if tinh_trang_vay_nh == "đang vay" or tinh_trang_vay_nl == "đang vay":
        print("Đéo mẹ, không chơi vay làm cặc gì")
    else:
        print("Người không chơi là người thắng")
elif so_du_goc < so_du :
    ty, trieu, nghin, tep = dv_tien(so_du)
    print("Bạn lời:",so_du - so_du_goc,"vnđ")
    print("Số dư hiện tại của bạn là:",ty,"tỷ",trieu,"triệu",nghin,"nghìn",tep,"với",so_lan_choi,"lần chơi,",sl_vay_nh,"lần vay ngân hàng và",sl_vay_nl,"số lần vay nặng lãi")
    if nh_cuong_che == 5:
        print("Nhưng mà bạn cũng không thể vay ngân hàng được nữa")
elif (so_du_goc == so_du) and (so_lan_choi >= 1):
    print("Chơi kiểu đéo gì mà chả mất cũng chả lời đồng nào vậy")
elif so_du == 0:
    print("Chúc bạn may mắn lần sau")
