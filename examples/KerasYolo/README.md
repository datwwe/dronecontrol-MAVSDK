# Sử dụng
- Em nghĩ sử dụng AI không nên phân ở thread khác việc chuyển model qua thread khác gây ảnh hưởng tới performance dù sao kích hoạt thuật toán panacea sau khi detect được hình ảnh.
- Ví dụ trong file detect_img.py
- yolo = YOLO() đây là model thời gian khởi tạo model tầm 4-5s cần giữ model này nếu đã làm theo thời gian thực
- hàm detect_img(yolo, file_path) hoặc anh chỉnh sửa lại bằng hình ảnh từ camera thông qua openCV thì thêm một function img = Image.fromarray(img) em có comment.
- Đầu ra timestamp,heli_cent_x|heli_cent_y,|heli_width|heli_height,arr_cent_x|arr_cent_y,|arr_width|arr_height