# Test Plan: OrangeHRM Employee Search

## 1. Mục tiêu kiểm thử (Testing Objectives)

- Xác minh rằng người dùng có thể đăng nhập thành công vào ứng dụng OrangeHRM.
- Đảm bảo chức năng tìm kiếm nhân viên (Employee Search) hoạt động chính xác với các tiêu chí khác nhau.
- Kiểm tra rằng luồng end-to-end (Login -> Search -> Logout) hoạt động liền mạch, không có lỗi.
- Xác thực các trường hợp nhập liệu không hợp lệ (negative cases) được xử lý đúng cách.

## 2. Phạm vi kiểm thử (Scope)

### Trong phạm vi (In-Scope)
- **Chức năng Đăng nhập:**
    - Đăng nhập với tài khoản hợp lệ.
    - Đăng nhập với tài khoản không hợp lệ.
- **Chức năng Tìm kiếm Nhân viên (trong module PIM):**
    - Tìm kiếm theo tên nhân viên.
    - Tìm kiếm với dữ liệu không tồn tại.
- **Chức năng Đăng xuất.**

### Ngoài phạm vi (Out-of-Scope)
- Tất cả các module khác ngoài PIM (Admin, Leave, Time, My Info, v.v.).
- Kiểm thử hiệu năng (Performance Testing).
- Kiểm thử bảo mật (Security Testing).
- Kiểm thử trên nhiều trình duyệt khác nhau (Cross-browser testing sẽ không phải là trọng tâm chính).
- Chức năng thêm, sửa, xóa nhân viên.

## 3. Danh sách Test Case chính (High-Level Test Cases)

| ID   | Mô tả                                               | Loại      |
|------|-----------------------------------------------------|-----------|
| TC01 | Đăng nhập thành công với tài khoản hợp lệ.           | Positive  |
| TC02 | Đăng nhập thất bại với mật khẩu sai.                | Negative  |
| TC03 | Tìm kiếm nhân viên thành công theo tên.             | Positive  |
| TC04 | Tìm kiếm nhân viên không tồn tại trong hệ thống.    | Negative  |
| TC05 | Luồng End-to-End: Đăng nhập, tìm kiếm và đăng xuất. | E2E       |

## 4. Tiêu chí Pass/Fail (Pass/Fail Criteria)

### Tiêu chí Pass
- Tất cả các test case thực thi mà không có lỗi (assertion errors).
- Luồng chức năng hoạt động đúng như kịch bản đã định nghĩa.
- Giao diện người dùng hiển thị chính xác, không có lỗi vỡ layout.

### Tiêu chí Fail
- Test case gặp lỗi và dừng lại (ví dụ: không tìm thấy element, element không thể tương tác).
- Kết quả thực tế không khớp với kết quả mong đợi (assertion failed).
- Ứng dụng bị treo, crash hoặc hiển thị thông báo lỗi không mong muốn.
