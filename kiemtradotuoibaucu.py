diem_trung_binh = float(input("Nhập điểm trung bình (thang 10): "))
if diem_trung_binh >= 8.0:
  xep_loai = "Giỏi"
elif diem_trung_binh >= 6.5:
  xep_loai = "Khá"
elif diem_trung_binh >= 5.0:
  xep_loai = "Trung bình"
else:
  xep_loai = "Yếu"
print(f"Xếp loại học lực: {xep_loai}")