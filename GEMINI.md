# Kế hoạch thực hiện dự án Automation Test cho OrangeHRM

Dựa trên yêu cầu từ file `Assigment-5.md`, kế hoạch chi tiết được chia thành các giai đoạn sau:

## Giai đoạn 1: Lập Kế hoạch và Thiết kế (Test Planning)

1.  **Phân tích yêu cầu:**
    *   **Ứng dụng:** [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/)
    *   **Luồng chính:** Login → Search Employee → Logout.
    *   **Công nghệ:** Selenium WebDriver với Python.
    *   **Đầu ra:** Báo cáo PDF bao gồm Test Plan, danh sách Test Case và kết quả chạy tự động.

2.  **Thiết kế Test Plan:**
    *   **Mục tiêu:** Kiểm tra tính đúng đắn của luồng chức năng từ đăng nhập, tìm kiếm nhân viên, đến đăng xuất.
    *   **Phạm vi:**
        *   **Trong phạm vi:** Các chức năng Login, Search Employee, Logout.
        *   **Ngoài phạm vi:** Các chức năng quản trị khác (Admin, PIM, Leave, Time,...) và các loại kiểm thử phi chức năng (hiệu năng, bảo mật).
    *   **Tiêu chí Pass/Fail:**
        *   **Pass:** Chức năng hoạt động đúng như mong đợi, không có lỗi giao diện hoặc logic.
        *   **Fail:** Chức năng bị lỗi, crash, trả về kết quả sai hoặc giao diện không đúng.

## Giai đoạn 2: Xây dựng nền tảng (Framework Development)

1.  **Cấu trúc lại dự án:**
    *   Tổ chức các thư mục `pages`, `tests`, `data`, `utils`, `reports`, `screenshots` một cách rõ ràng.
    *   Sử dụng mô hình Page Object Model (POM) để quản lý code dễ dàng.

2.  **Tạo các Page Objects:**
    *   `LoginPage.py`: Chứa các locators và hành động cho trang đăng nhập.
    *   `DashboardPage.py`: Chứa các locators và hành động cho trang dashboard sau khi đăng nhập.
    *   `PIMPage.py`: Chứa các locators và hành động cho trang quản lý thông tin nhân viên (Personal Information Management), nơi thực hiện tìm kiếm.

3.  **Tạo các thành phần hỗ trợ:**
    *   `conftest.py`: Thiết lập WebDriver, cấu hình teardown (ví dụ: tự động chụp ảnh màn hình khi test case thất bại).
    *   `helpers.py` (trong `utils`): Chứa các hàm tiện ích dùng chung (ví dụ: đọc dữ liệu từ file excel, json).

## Giai đoạn 3: Viết và Thực thi Test Case

1.  **Chuẩn bị dữ liệu test:**
    *   Tạo file (ví dụ: `test_data.xlsx` hoặc `data.json`) để lưu trữ thông tin đăng nhập, tên nhân viên cần tìm, v.v.

2.  **Viết các Test Case:**
    *   **Positive Case:**
        *   `test_successful_login`: Đăng nhập thành công với tài khoản hợp lệ.
        *   `test_search_employee_by_name`: Tìm kiếm nhân viên tồn tại theo tên.
    *   **Negative Case:**
        *   `test_login_with_invalid_password`: Đăng nhập với mật khẩu sai.
        *   `test_search_for_nonexistent_employee`: Tìm kiếm một nhân viên không có trong hệ thống.
    *   **End-to-End Case:**
        *   `test_e2e_login_search_and_logout`: Thực hiện toàn bộ luồng: Đăng nhập → Điều hướng đến PIM → Tìm kiếm nhân viên → Xác nhận kết quả → Đăng xuất.

## Giai đoạn 4: Báo cáo và Tổng kết

1.  **Tạo báo cáo tự động:**
    *   Chạy lệnh `pytest --html=reports/report.html` để tạo báo cáo.
    *   Đảm bảo báo cáo có đầy đủ thông tin: tên test case, trạng thái (Pass/Fail), thời gian chạy, và ảnh chụp màn hình của các test case thất bại.

2.  **Tổng hợp tài liệu:**
    *   Viết tóm tắt Test Plan.
    *   Trích xuất kết quả từ file `report.html`.
    *   Phân tích các lỗi đã tìm thấy (nếu có).
    *   Viết kết luận về lợi ích của việc áp dụng automation testing cho dự án này.

3.  **Tạo file PDF cuối cùng:**
    *   Gộp tất cả các tài liệu trên (Test Plan, danh sách test case, kết quả, phân tích) vào một file PDF duy nhất để nộp bài.
