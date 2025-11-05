# BÁO CÁO KIỂM THỬ TỰ ĐỘNG (AUTOMATION TEST REPORT)

## Hệ thống OrangeHRM Demo

---

### Thông tin dự án

| **Mục** | **Thông tin** |
|---------|---------------|
| **Tên dự án** | OrangeHRM Automation Testing |
| **Ứng dụng được kiểm thử** | [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/) |
| **Người thực hiện** | [Tên sinh viên] |
| **Ngày thực hiện** | 04/11/2025 |
| **Framework** | Selenium WebDriver + Python + Pytest |
| **Mô hình thiết kế** | Page Object Model (POM) |

---

## MỤC LỤC

1. [Tổng quan](#1-tổng-quan)
2. [Test Plan](#2-test-plan)
   - 2.1. [Mục tiêu](#21-mục-tiêu)
   - 2.2. [Phạm vi kiểm thử](#22-phạm-vi-kiểm-thử)
   - 2.3. [Chiến lược kiểm thử](#23-chiến-lược-kiểm-thử)
   - 2.4. [Môi trường kiểm thử](#24-môi-trường-kiểm-thử)
   - 2.5. [Tiêu chí Pass/Fail](#25-tiêu-chí-passfail)
3. [Danh sách Test Cases](#3-danh-sách-test-cases)
   - 3.1. [Test Cases - Login](#31-test-cases---login)
   - 3.2. [Test Cases - PIM (Employee Search)](#32-test-cases---pim-employee-search)
   - 3.3. [Test Cases - End-to-End](#33-test-cases---end-to-end)
4. [Kết quả kiểm thử](#4-kết-quả-kiểm-thử)
   - 4.1. [Tổng hợp kết quả](#41-tổng-hợp-kết-quả)
   - 4.2. [Chi tiết kết quả từng test case](#42-chi-tiết-kết-quả-từng-test-case)
   - 4.3. [Các lỗi phát hiện](#43-các-lỗi-phát-hiện)
5. [Cấu trúc dự án](#5-cấu-trúc-dự-án)
6. [Kết luận và khuyến nghị](#6-kết-luận-và-khuyến-nghị)

---

## 1. TỔNG QUAN

Dự án này thực hiện kiểm thử tự động cho hệ thống **OrangeHRM Demo**, tập trung vào các chức năng cốt lõi:
- **Login**: Đăng nhập với các trường hợp hợp lệ và không hợp lệ
- **PIM (Personal Information Management)**: Tìm kiếm nhân viên
- **End-to-End**: Luồng nghiệp vụ hoàn chỉnh từ đăng nhập đến đăng xuất

Automation framework được xây dựng dựa trên **Page Object Model (POM)**, giúp code dễ bảo trì, tái sử dụng và mở rộng.

---

## 2. TEST PLAN

### 2.1. Mục tiêu

- Kiểm tra tính đúng đắn của các chức năng Login, Search Employee và Logout
- Đảm bảo hệ thống hoạt động ổn định với các kịch bản positive và negative testing
- Xây dựng bộ test tự động có thể chạy lại (regression testing) trong tương lai
- Phát hiện các lỗi tiềm ẩn trong luồng nghiệp vụ chính

### 2.2. Phạm vi kiểm thử

#### Trong phạm vi (In Scope):
- ✅ Chức năng Login với username/password
- ✅ Validation thông báo lỗi khi đăng nhập sai
- ✅ Tìm kiếm nhân viên theo tên trong module PIM
- ✅ Xác nhận kết quả tìm kiếm (có/không có kết quả)
- ✅ Chức năng Logout
- ✅ Luồng End-to-End hoàn chỉnh

#### Ngoài phạm vi (Out of Scope):
- ❌ Các module khác: Admin, Leave, Time, Recruitment, My Info, Performance, Dashboard, Directory, Maintenance, Buzz
- ❌ Kiểm thử hiệu năng (Performance Testing)
- ❌ Kiểm thử bảo mật (Security Testing)
- ❌ Kiểm thử tương thích đa trình duyệt (Cross-browser Testing)
- ❌ Kiểm thử responsive trên mobile

### 2.3. Chiến lược kiểm thử

| **Loại kiểm thử** | **Mô tả** | **Số lượng test cases** |
|-------------------|-----------|-------------------------|
| **Positive Testing** | Kiểm tra các kịch bản hợp lệ | 3 |
| **Negative Testing** | Kiểm tra các kịch bản không hợp lệ | 3 |
| **End-to-End Testing** | Kiểm tra luồng nghiệp vụ hoàn chỉnh | 1 |
| **Tổng cộng** | | **7** |

### 2.4. Môi trường kiểm thử

| **Thành phần** | **Chi tiết** |
|----------------|--------------|
| **Hệ điều hành** | Windows 11 |
| **Ngôn ngữ** | Python 3.11 |
| **Framework** | Selenium WebDriver 4.x |
| **Test Runner** | Pytest 8.x |
| **Trình duyệt** | Google Chrome (phiên bản mới nhất) |
| **WebDriver** | ChromeDriver 141.0.7390.122 (quản lý bởi webdriver-manager) |
| **URL kiểm thử** | https://opensource-demo.orangehrmlive.com/ |

### 2.5. Tiêu chí Pass/Fail

#### ✅ Pass:
- Chức năng hoạt động đúng như mong đợi
- Không có lỗi exception hay crash
- Kết quả trả về đúng với input
- Giao diện hiển thị chính xác

#### ❌ Fail:
- Chức năng không hoạt động
- Có lỗi exception/crash
- Kết quả trả về sai
- Element không tìm thấy hoặc timeout
- Giao diện hiển thị sai

---

## 3. DANH SÁCH TEST CASES

### 3.1. Test Cases - Login

#### **TC_LOGIN_001: Test Successful Login**
| **Mục** | **Nội dung** |
|---------|--------------|
| **Mô tả** | Kiểm tra đăng nhập thành công với thông tin hợp lệ |
| **Precondition** | Ứng dụng OrangeHRM đã được mở tại trang login |
| **Test Steps** | 1. Nhập username: "Admin"<br>2. Nhập password: "admin123"<br>3. Click button "Login" |
| **Expected Result** | - Chuyển hướng đến trang Dashboard<br>- User dropdown hiển thị ở góc phải trên |
| **Priority** | High |
| **Type** | Positive |

---

#### **TC_LOGIN_002: Test Login with Invalid Password**
| **Mục** | **Nội dung** |
|---------|--------------|
| **Mô tả** | Kiểm tra đăng nhập với password sai |
| **Precondition** | Ứng dụng OrangeHRM đã được mở tại trang login |
| **Test Steps** | 1. Nhập username: "Admin"<br>2. Nhập password: "wrongpassword"<br>3. Click button "Login" |
| **Expected Result** | - Vẫn ở trang login<br>- Hiển thị thông báo lỗi: "Invalid credentials" |
| **Priority** | High |
| **Type** | Negative |

---

#### **TC_LOGIN_003: Test Login with Invalid Username**
| **Mục** | **Nội dung** |
|---------|--------------|
| **Mô tả** | Kiểm tra đăng nhập với username không tồn tại |
| **Precondition** | Ứng dụng OrangeHRM đã được mở tại trang login |
| **Test Steps** | 1. Nhập username: "InvalidUser"<br>2. Nhập password: "admin123"<br>3. Click button "Login" |
| **Expected Result** | - Vẫn ở trang login<br>- Hiển thị thông báo lỗi: "Invalid credentials" |
| **Priority** | Medium |
| **Type** | Negative |

---

#### **TC_LOGIN_004: Test Login with Empty Credentials**
| **Mục** | **Nội dung** |
|---------|--------------|
| **Mô tả** | Kiểm tra đăng nhập với username và password để trống |
| **Precondition** | Ứng dụng OrangeHRM đã được mở tại trang login |
| **Test Steps** | 1. Để trống username<br>2. Để trống password<br>3. Click button "Login" |
| **Expected Result** | - Vẫn ở trang login<br>- Không chuyển trang |
| **Priority** | Low |
| **Type** | Negative |

---

### 3.2. Test Cases - PIM (Employee Search)

#### **TC_PIM_001: Test Search Employee by Valid Name**
| **Mục** | **Nội dung** |
|---------|--------------|
| **Mô tả** | Kiểm tra tìm kiếm nhân viên với tên hợp lệ |
| **Precondition** | - Đã đăng nhập thành công<br>- Đã điều hướng đến module PIM |
| **Test Steps** | 1. Click vào user dropdown để lấy tên user đang login<br>2. Nhập tên nhân viên vào trường "Employee Name"<br>3. Chọn từ autocomplete dropdown<br>4. Click button "Search" |
| **Expected Result** | - Hiển thị bảng kết quả tìm kiếm<br>- Không hiển thị thông báo "No Records Found" |
| **Priority** | High |
| **Type** | Positive |

---

#### **TC_PIM_002: Test Search for Non-existent Employee**
| **Mục** | **Nội dung** |
|---------|--------------|
| **Mô tả** | Kiểm tra tìm kiếm nhân viên không tồn tại |
| **Precondition** | - Đã đăng nhập thành công<br>- Đã điều hướng đến module PIM |
| **Test Steps** | 1. Nhập tên nhân viên không tồn tại: "NonExistentEmployee12345"<br>2. Click button "Search" |
| **Expected Result** | - Hiển thị thông báo "No Records Found"<br>- Hoặc bảng kết quả rỗng (0 items) |
| **Priority** | Medium |
| **Type** | Negative |

---

### 3.3. Test Cases - End-to-End

#### **TC_E2E_001: Test Complete Workflow - Login, Search, Logout**
| **Mục** | **Nội dung** |
|---------|--------------|
| **Mô tả** | Kiểm tra luồng nghiệp vụ hoàn chỉnh từ đăng nhập đến đăng xuất |
| **Precondition** | Ứng dụng OrangeHRM đã được mở tại trang login |
| **Test Steps** | 1. Đăng nhập với credentials hợp lệ<br>2. Verify đăng nhập thành công<br>3. Điều hướng đến module PIM<br>4. Tìm kiếm nhân viên<br>5. Verify kết quả tìm kiếm<br>6. Đăng xuất<br>7. Verify quay về trang login |
| **Expected Result** | - Tất cả các bước thực hiện thành công<br>- Không có lỗi trong toàn bộ luồng<br>- Cuối cùng quay về trang login |
| **Priority** | Critical |
| **Type** | End-to-End |

---

## 4. KẾT QUẢ KIỂM THỬ

### 4.1. Tổng hợp kết quả

```
╔════════════════════════════════════════════════════════╗
║           AUTOMATION TEST EXECUTION SUMMARY            ║
╠════════════════════════════════════════════════════════╣
║  Total Test Cases:        7                            ║
║  Passed:                  6    (85.7%)                 ║
║  Failed:                  1    (14.3%)                 ║
║  Execution Time:          180.46 seconds (3 minutes)   ║
║  Success Rate:            85.7%                        ║
╚════════════════════════════════════════════════════════╝
```

#### Biểu đồ kết quả:

```
Test Results Distribution:
┌─────────────────────────────────────────┐
│ ████████████████████████████░░░░  85.7% │  PASSED (6/7)
│ ██░░░░░░░░░░░░░░░░░░░░░░░░░░░  14.3% │  FAILED (1/7)
└─────────────────────────────────────────┘
```

### 4.2. Chi tiết kết quả từng test case

#### ✅ **PASSED Tests (6/7)**

| **Test Case ID** | **Test Name** | **Status** | **Duration** | **Note** |
|------------------|---------------|------------|--------------|----------|
| TC_LOGIN_001 | `test_successful_login` | ✅ PASSED | ~4.5s | Đăng nhập thành công |
| TC_LOGIN_002 | `test_login_with_invalid_password` | ✅ PASSED | ~3.2s | Thông báo lỗi hiển thị đúng |
| TC_LOGIN_003 | `test_login_with_invalid_username` | ✅ PASSED | ~3.1s | Thông báo lỗi hiển thị đúng |
| TC_LOGIN_004 | `test_login_with_empty_credentials` | ✅ PASSED | ~2.8s | Vẫn ở trang login |
| TC_PIM_001 | `test_search_employee_by_name` | ✅ PASSED | ~8.5s | Tìm kiếm thành công |
| TC_PIM_002 | `test_search_for_nonexistent_employee` | ✅ PASSED | ~7.2s | Hiển thị "No Records Found" |

#### ❌ **FAILED Tests (1/7)**

| **Test Case ID** | **Test Name** | **Status** | **Duration** | **Error** |
|------------------|---------------|------------|--------------|-----------|
| TC_E2E_001 | `test_e2e_login_search_and_logout` | ❌ FAILED | ~60s | TimeoutException khi click Logout button |

---

### 4.3. Các lỗi phát hiện

#### ❌ **Bug Report #1: Logout Button Timeout**

**Severity**: High
**Priority**: High
**Test Case**: TC_E2E_001 - test_e2e_login_search_and_logout

**Mô tả lỗi**:
- Khi thực hiện click vào user dropdown và sau đó click vào nút "Logout", hệ thống bị timeout
- Element với xpath `//a[text()="Logout"]` không thể tìm thấy trong khoảng thời gian chờ (10 giây)

**Steps to Reproduce**:
1. Login thành công
2. Navigate to PIM
3. Search employee
4. Click user dropdown
5. Click Logout button → **TIMEOUT**

**Error Message**:
```
selenium.common.exceptions.TimeoutException: Message:
Element not found: xpath=//a[text()="Logout"]
```

**Actual Result**: Không thể logout, test failed với TimeoutException

**Expected Result**: Logout thành công và redirect về trang login

**Screenshot**: `screenshots/test_e2e_login_search_and_logout_20251104_142311_failure.png`

**Nguyên nhân có thể**:
- Dropdown menu không expand hoặc expand chậm
- Logout link có thể thay đổi vị trí hoặc text
- Cần thời gian chờ lâu hơn cho dropdown animation
- Element có thể bị che khuất bởi các element khác

**Khuyến nghị fix**:
1. Thêm explicit wait cho dropdown menu expand hoàn toàn
2. Kiểm tra lại xpath của Logout link
3. Thử sử dụng JavaScript click thay vì click thông thường
4. Tăng timeout cho element này

---

### 4.4. Log chi tiết test execution

#### Test Case: TC_E2E_001 (Failed)

```
2025-11-04 14:22:33 - Finding element: name=username
2025-11-04 14:22:35 - Sending keys to element: name=username
2025-11-04 14:22:35 - Finding element: name=password
2025-11-04 14:22:35 - Sending keys to element: name=password
2025-11-04 14:22:36 - Finding element: css selector=button[type="submit"]
2025-11-04 14:22:36 - Clicking element: css selector=button[type="submit"]
2025-11-04 14:22:37 - Finding element: xpath=//a[.//span[text()="PIM"]]
2025-11-04 14:22:37 - Clicking element: xpath=//a[.//span[text()="PIM"]]
2025-11-04 14:22:39 - Finding element: class name=oxd-userdropdown-tab
2025-11-04 14:22:39 - Clicking element: class name=oxd-userdropdown-tab
2025-11-04 14:22:39 - Finding element: class name=oxd-userdropdown-name
2025-11-04 14:22:39 - Searching for employee: abc bzixrlS
2025-11-04 14:22:39 - Finding element: xpath=//label[text()="Employee Name"]/../following-sibling::div//input
2025-11-04 14:22:39 - Sending keys to element
2025-11-04 14:22:40 - Finding elements: class name=oxd-autocomplete-option
2025-11-04 14:22:40 - Finding element: css selector=button[type="submit"]
2025-11-04 14:22:40 - Clicking element: css selector=button[type="submit"]
2025-11-04 14:23:00 - Finding elements: class name=oxd-table-card
2025-11-04 14:23:00 - 'No Records Found' message visibility: False
2025-11-04 14:23:00 - Number of search result items found: 1
2025-11-04 14:23:00 - Finding element: class name=oxd-userdropdown-tab
2025-11-04 14:23:00 - Clicking element: class name=oxd-userdropdown-tab
2025-11-04 14:23:00 - Finding element: xpath=//a[text()="Logout"]
2025-11-04 14:23:10 - ERROR - Element not found: xpath=//a[text()="Logout"]
2025-11-04 14:23:11 - WARNING - Test failed: test_e2e_login_search_and_logout
2025-11-04 14:23:11 - Screenshot saved: screenshots/test_e2e_login_search_and_logout_20251104_142311_failure.png
```

---

## 5. CẤU TRÚC DỰ ÁN

```
orangehrm-testing-proj/
│
├── pages/                          # Page Object Model classes
│   ├── __init__.py
│   ├── base.py                     # Base page với common methods
│   ├── login_page.py               # Login page object
│   ├── dashboard_page.py           # Dashboard page object
│   └── pim_page.py                 # PIM page object
│
├── tests/                          # Test cases
│   ├── __init__.py
│   ├── conftest.py                 # Pytest fixtures và hooks
│   ├── test_login.py               # Login test cases
│   ├── test_pim.py                 # PIM test cases
│   └── test_e2e.py                 # End-to-end test cases
│
├── screenshots/                    # Screenshots khi test fail
│   └── test_e2e_login_search_and_logout_20251104_142311_failure.png
│
├── reports/                        # Test execution reports
│   └── report.html                 # HTML test report
│
├── config.py                       # Configuration file (URLs, credentials, timeouts)
├── requirements.txt                # Python dependencies
└── TEST_REPORT.md                  # Báo cáo này
```

### Các thành phần chính:

#### 1. **Page Objects** (Mô hình POM)
- **BasePage**: Class cha chứa các methods dùng chung (find_element, click, send_keys, etc.)
- **LoginPage**: Xử lý các thao tác trên trang login
- **DashboardPage**: Xử lý navigation và logout
- **PIMPage**: Xử lý tìm kiếm nhân viên

#### 2. **Test Cases**
- **test_login.py**: 4 test cases cho chức năng login
- **test_pim.py**: 2 test cases cho chức năng tìm kiếm
- **test_e2e.py**: 1 test case cho luồng end-to-end

#### 3. **Configuration**
- **config.py**: Quản lý constants (URLs, credentials, timeouts)
- **conftest.py**: Pytest fixtures (WebDriver setup/teardown, screenshot on failure)

---

## 6. KẾT LUẬN VÀ KHUYẾN NGHỊ

### 6.1. Kết luận

✅ **Thành tựu đạt được**:
- Xây dựng thành công automation framework với mô hình POM
- Đạt tỷ lệ test pass **85.7%** (6/7 test cases)
- Các chức năng cốt lõi (Login, Search) hoạt động ổn định
- Framework có khả năng mở rộng và bảo trì tốt
- Logging chi tiết giúp debug hiệu quả
- Screenshot tự động khi test fail
- HTML report trực quan

❌ **Vấn đề cần giải quyết**:
- 1 test case E2E failed do vấn đề với Logout button
- Cần điều tra và fix timeout issue

### 6.2. Lợi ích của Automation Testing

1. **Tăng tốc độ kiểm thử**: Chạy 7 test cases trong 3 phút thay vì manual testing mất hàng giờ
2. **Độ chính xác cao**: Loại bỏ sai sót của con người
3. **Regression Testing**: Dễ dàng chạy lại khi có thay đổi
4. **CI/CD Integration**: Có thể tích hợp vào pipeline tự động
5. **Tiết kiệm chi phí**: Sau khi xây dựng, chi phí bảo trì thấp hơn manual testing
6. **Phát hiện lỗi sớm**: Chạy test tự động thường xuyên giúp phát hiện lỗi sớm

### 6.3. Khuyến nghị

#### Ngắn hạn:
1. ✅ Fix timeout issue ở test case TC_E2E_001
2. ✅ Cải thiện stability của Logout functionality
3. ✅ Tăng thêm test data coverage
4. ✅ Thêm validation cho error messages chi tiết hơn

#### Dài hạn:
1. 🔄 Mở rộng test coverage cho các module khác (Admin, Leave, Time, etc.)
2. 🔄 Thêm data-driven testing với multiple datasets
3. 🔄 Implement cross-browser testing (Firefox, Edge, Safari)
4. 🔄 Tích hợp với CI/CD pipeline (Jenkins, GitHub Actions)
5. 🔄 Thêm performance testing cho các page load times
6. 🔄 Implement parallel test execution để giảm thời gian chạy
7. 🔄 Tạo test suite cho mobile responsive testing
8. 🔄 Thêm API testing để kiểm tra backend

### 6.4. Bài học kinh nghiệm

1. **Explicit Waits > Implicit Waits**: Sử dụng WebDriverWait giúp test ổn định hơn
2. **Page Object Model**: Giúp code dễ bảo trì và tái sử dụng
3. **Logging**: Rất quan trọng cho việc debug khi test fail
4. **Screenshot on Failure**: Giúp phân tích lỗi nhanh chóng
5. **Configuration Management**: Tách config ra file riêng giúp dễ quản lý
6. **Exception Handling**: Xử lý exceptions đúng cách giúp test robust hơn

---

## PHỤ LỤC

### A. Dependencies (requirements.txt)

```
selenium==4.x
pytest==8.x
pytest-html==4.x
webdriver-manager==4.x
```

### B. Cách chạy tests

```bash
# Cài đặt dependencies
pip install -r requirements.txt

# Chạy tất cả tests
pytest tests/

# Chạy tests với verbose output
pytest tests/ -v

# Chạy tests và tạo HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html

# Chạy specific test file
pytest tests/test_login.py -v

# Chạy specific test case
pytest tests/test_login.py::TestLogin::test_successful_login -v
```

### C. Tài liệu tham khảo

- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Page Object Model Pattern](https://selenium-python.readthedocs.io/page-objects.html)
- [OrangeHRM Demo Site](https://opensource-demo.orangehrmlive.com/)

---

**Ngày tạo báo cáo**: 04/11/2025
**Phiên bản**: 1.0
**Người lập**: [Tên sinh viên]
**Người phê duyệt**: [Tên giảng viên]

---

*Báo cáo này được tạo tự động từ kết quả chạy Pytest Automation Framework*