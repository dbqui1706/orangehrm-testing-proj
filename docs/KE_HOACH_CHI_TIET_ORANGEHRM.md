# HƯỚNG DẪN CHI TIẾT: QUY TRÌNH LÀM PROJECT SOFTWARE TESTING
## ORANGEHRM - EMPLOYEE MANAGEMENT & LEAVE MANAGEMENT

*Document này được tạo riêng cho OrangeHRM testing project với 2 chức năng: Employee Management & Leave Management. Follow từng bước cẩn thận để đạt kết quả tốt nhất!*

---

## 📋 TỔNG QUAN PROJECT

**Hệ thống test:** OrangeHRM - Open Source HR Management System

**URL:** https://opensource-demo.orangehrmlive.com/

**Login:** Username: Admin | Password: admin123

**Phương pháp:** Black-box Testing + Automation Testing (Selenium Python)

**Deliverables (Sản phẩm cần nộp):**
1. **Report.doc** - Báo cáo tổng hợp (10-15 trang)
2. **TestDesign.xlsx** - Bảng thiết kế test cases
3. **TestCase.xlsx** - Danh sách test cases chi tiết và kết quả
4. **Q&A.xls** - Báo cáo bugs/issues phát hiện được
5. **Selenium Code** - Automation scripts (Python + Selenium)

---

## 🎯 BƯỚC 1: CHỌN HỆ THỐNG VÀ CHỨC NĂNG

### Hệ thống đã chọn:
**OrangeHRM** - Hệ thống quản lý nhân sự mã nguồn mở

### 2 Chức năng chính để test:

**Chức năng 1: EMPLOYEE MANAGEMENT (Quản lý nhân viên)**
- **End-to-End Flow:**
  - Login → PIM Module → Add Employee
  - Search Employee
  - Edit Employee (Personal Details, Contact, Job, Salary...)
  - Delete Employee
  - Logout

- **Sub-functions:**
  - Add Employee (Create)
  - Search Employee List (Read)
  - Edit Employee Details (Update)
  - Delete Employee (Delete)

**Test Cases ước tính: 175-215 cases**

---

**Chức năng 2: LEAVE MANAGEMENT (Quản lý nghỉ phép)**
- **End-to-End Flow:**
  - Login → Leave Module → Configure Leave System
  - Add Entitlements
  - Apply Leave (as Employee)
  - Approve/Reject Leave (as Supervisor)
  - View Reports
  - Logout

- **Sub-functions:**
  - Configure Leave (Leave Types, Holidays, Work Week)
  - Add Leave Entitlements
  - Apply Leave
  - View My Leave
  - Approve/Reject Leave (Leave List)
  - Leave Reports

**Test Cases ước tính: 220-265 cases**

---

## 📝 BƯỚC 2: VIẾT TÀI LIỆU YÊU CẦU (Requirements Document)

### File: Report.doc - Phần Requirements

**Nội dung cần viết:**

```
1. FUNCTIONALITY REQUIREMENTS

Người thực hiện: [Nhóm 7 người]

---

1.1 Employee Management (Quản lý nhân viên)

1.1.1 Add Employee (Thêm nhân viên mới)

Quy trình:
1. Đăng nhập với tài khoản Admin
2. Click vào menu "PIM" trên thanh navigation
3. Click button "Add Employee"
4. Điền thông tin nhân viên:
   - First Name* (required)
   - Middle Name (optional)
   - Last Name* (required)
   - Employee ID* (auto-generate hoặc nhập thủ công)
5. Upload ảnh nhân viên (optional):
   - Format: PNG, JPG, JPEG
   - Size: Max 1MB
   - Click "Choose File" để chọn ảnh
6. Tạo thông tin đăng nhập (optional):
   - Check vào "Create Login Details"
   - Username* (required, unique)
   - Password* (required, min 8 chars)
   - Confirm Password* (required, must match)
   - Status: Enabled/Disabled
7. Click button "Save"

Kết quả mong đợi:
- Hiển thị thông báo "Successfully Saved"
- Chuyển sang trang Personal Details của nhân viên mới
- Employee ID được tự động tạo nếu không nhập
- Thông tin được lưu vào database
- Nhân viên mới xuất hiện trong Employee List

[CHÈN SCREENSHOT 1: Form Add Employee trống]
[CHÈN SCREENSHOT 2: Form đã điền đầy đủ thông tin]
[CHÈN SCREENSHOT 3: Thông báo Successfully Saved]
[CHÈN SCREENSHOT 4: Trang Personal Details sau khi save]

---

1.1.2 Search Employee (Tìm kiếm nhân viên)

Quy trình:
1. Đăng nhập với tài khoản Admin
2. Click vào menu "PIM" → "Employee List"
3. Sử dụng các filter để tìm kiếm:
   - Employee Name (autocomplete search)
   - Employee ID
   - Employment Status (Full-Time, Part-Time, Contract, Freelance)
   - Include: Current Employees Only / Current and Past Employees
   - Supervisor Name
   - Job Title
   - Sub Unit
4. Click button "Search"

Kết quả mong đợi:
- Hiển thị danh sách nhân viên phù hợp với filter
- Mỗi record hiển thị: ID, First Name, Last Name, Job Title, Employment Status, Sub Unit, Supervisor
- Có pagination nếu kết quả > 50 records
- Button "Reset" để xóa tất cả filter
- Có thể click vào tên nhân viên để xem chi tiết
- Có checkbox để select multiple employees
- Có button "Delete Selected" để xóa nhiều nhân viên

[CHÈN SCREENSHOT 1: Employee List với filter options]
[CHÈN SCREENSHOT 2: Kết quả search]
[CHÈN SCREENSHOT 3: Autocomplete khi nhập tên]

---

1.1.3 Edit Employee (Chỉnh sửa thông tin nhân viên)

Quy trình:
1. Tìm và click vào nhân viên cần edit
2. Chuyển sang trang Personal Details
3. Edit thông tin trong các tabs:

**Tab 1: Personal Details**
- Name (First, Middle, Last)
- Employee ID
- Other ID
- Driver's License Number
- License Expiry Date
- Nationality
- Marital Status
- Date of Birth
- Gender (Male/Female)
- Military Service
- Smoker (checkbox)
- Click "Save" để lưu

**Tab 2: Contact Details**
- Address (Street 1, Street 2)
- City
- State/Province
- Zip/Postal Code
- Country
- Home Telephone
- Mobile
- Work Telephone
- Work Email
- Other Email
- Click "Save"

**Tab 3: Emergency Contacts**
- Click "Add" để thêm contact mới
- Name, Relationship, Home/Mobile Phone, Work Phone
- Click "Save"
- Có thể Edit/Delete contact đã có

**Tab 4: Dependents**
- Click "Add" để thêm dependent
- Name, Relationship, Date of Birth
- Click "Save"
- Có thể Edit/Delete

**Tab 5: Immigration**
- Click "Add" để thêm immigration record
- Document Type (Passport, Visa, etc.)
- Number, Issue Date, Expiry Date
- Eligible Status, Country, Review Date
- Comments
- Attachment upload
- Click "Save"

**Tab 6: Job**
- Job Title, Employment Status, Job Category
- Joined Date, Sub Unit, Location
- Contract Start/End Date
- Attachment for contract
- Click "Save"

**Tab 7: Salary**
- Click "Add" để thêm salary component
- Pay Grade, Currency, Amount
- Pay Frequency, Comments
- Attachment for proof
- Click "Save"

**Tab 8: Report-to**
- Add Supervisor với Reporting Method
- Add Subordinate với Reporting Method
- Edit/Delete relationships

**Tab 9: Qualifications**
- Work Experience (Add/Edit/Delete)
- Education (Add/Edit/Delete)
- Skills (Add/Edit/Delete)
- Languages (Add/Edit/Delete)
- License (Add/Edit/Delete)

**Tab 10: Memberships**
- Add Membership với type, amount, dates
- Edit/Delete memberships

Kết quả mong đợi:
- Mỗi tab có button "Save" riêng
- Hiển thị "Successfully Saved" sau khi save
- Dữ liệu được update trong database
- Có thể navigate giữa các tabs mà không mất dữ liệu

[CHÈN SCREENSHOT cho mỗi tab]

---

1.1.4 Delete Employee (Xóa nhân viên)

Quy trình:
1. Vào Employee List
2. Select checkbox của nhân viên cần xóa
3. Click button "Delete Selected"
4. Confirm deletion trong popup
5. Click "Yes, Delete"

Kết quả mong đợi:
- Hiển thị thông báo "Successfully Deleted"
- Nhân viên biến mất khỏi Employee List
- Không thể search được nhân viên đã xóa
- Dữ liệu được xóa khỏi database

[CHÈN SCREENSHOT 1: Select employee]
[CHÈN SCREENSHOT 2: Confirmation popup]
[CHÈN SCREENSHOT 3: Success message]

---

1.2 Leave Management (Quản lý nghỉ phép)

1.2.1 Configure Leave System (Cấu hình hệ thống nghỉ phép)

**Admin Role Required**

Quy trình:
1. Đăng nhập với tài khoản Admin
2. Click menu "Leave" → "Configure"

**A. Leave Period:**
- Click "Leave Period"
- Select Start Month và Start Date
- Click "Save"

**B. Leave Types:**
- Click "Leave Types"
- Click "Add" để thêm leave type mới
- Nhập Leave Type Name (Annual, Sick, Casual, Maternity, etc.)
- Click "Save"
- Có thể Edit/Delete leave types

**C. Work Week:**
- Click "Work Week"
- Select working days (Monday - Sunday)
- Define Full Day/Half Day for each day
- Click "Save"

**D. Holidays:**
- Click "Holidays"
- Click "Add" để thêm holiday
- Nhập Holiday Name
- Select Date
- Check "Repeats Annually" nếu cần
- Select Length (Full Day / Half Day / Specify Time)
- Click "Save"
- Có thể Edit/Delete holidays

Kết quả mong đợi:
- Configuration được lưu thành công
- Áp dụng cho toàn bộ hệ thống
- Ảnh hưởng đến leave calculation
- Hiển thị trong calendar

[CHÈN SCREENSHOT cho mỗi phần config]

---

1.2.2 Add Leave Entitlements (Thêm quyền nghỉ phép)

**Admin Role Required**

Quy trình:
1. Đăng nhập Admin
2. Click "Leave" → "Entitlements" → "Add Entitlements"
3. Điền form:
   - Employee Name* (search và select)
   - Leave Type* (dropdown)
   - Leave Period* (dropdown)
   - Entitlement* (số ngày nghỉ)
4. Click "Save"

Kết quả mong đợi:
- Hiển thị "Successfully Saved"
- Entitlement được thêm cho employee
- Hiển thị trong "Employee Entitlements"
- Employee có thể xem balance trong Leave dashboard

[CHÈN SCREENSHOT 1: Add Entitlements form]
[CHÈN SCREENSHOT 2: Success message]
[CHÈN SCREENSHOT 3: Employee Entitlements list]

---

1.2.3 Apply Leave (Xin nghỉ phép)

**Employee Role**

Quy trình:
1. Đăng nhập với tài khoản Employee
2. Click "Leave" → "Apply"
3. Điền Leave Application form:
   - Leave Type* (dropdown)
     → Hệ thống tự động hiển thị Balance available
   - From Date* (date picker)
   - To Date* (date picker)
     → Hệ thống tự động tính Number of Days
   - Partial Days (optional):
     • All Days
     • Start Day Only (Half Day - Morning/Afternoon)
     • End Day Only (Half Day - Morning/Afternoon)
     • Start and End Day
   - Duration (auto-calculated, có thể edit nếu partial)
   - Comment (optional, textarea)
4. Verify:
   - Balance đủ không?
   - Dates hợp lệ không?
   - Không overlap với leave khác?
5. Click "Apply"

Kết quả mong đợi:
- Hiển thị "Successfully Saved"
- Leave request được tạo với status "Pending Approval"
- Balance chưa bị trừ (chờ approved)
- Hiển thị trong "My Leave" list
- Supervisor nhận notification

[CHÈN SCREENSHOT 1: Apply Leave form với balance]
[CHÈN SCREENSHOT 2: Date picker]
[CHÈN SCREENSHOT 3: Partial Days options]
[CHÈN SCREENSHOT 4: Success message]
[CHÈN SCREENSHOT 5: Leave trong My Leave list]

---

1.2.4 View My Leave (Xem nghỉ phép của tôi)

**Employee Role**

Quy trình:
1. Đăng nhập Employee
2. Click "Leave" → "My Leave"
3. Xem danh sách leave requests với filters:
   - From Date, To Date (date range)
   - Show Leave with Status: All / Pending Approval / Approved / Rejected / Cancelled / Taken
   - Leave Type (dropdown)
   - Click "Search"
4. Xem Leave Balance summary ở sidebar
5. Actions có thể làm:
   - Cancel (nếu status = Pending)
   - View Details
   - Download iCal

Kết quả mong đợi:
- Hiển thị list of all leave requests
- Mỗi record: Leave Date, Leave Type, Number of Days, Status, Actions
- Color coding theo status
- Leave Balance hiển thị đúng
- Có thể filter và search

[CHÈN SCREENSHOT 1: My Leave list]
[CHÈN SCREENSHOT 2: Leave Balance summary]
[CHÈN SCREENSHOT 3: Filter options]

---

1.2.5 Approve/Reject Leave (Duyệt nghỉ phép)

**Supervisor/Admin Role**

Quy trình:
1. Đăng nhập Supervisor/Admin
2. Click "Leave" → "Leave List"
3. Xem pending leave requests
4. Filter by:
   - From Date, To Date
   - Show Leave with Status
   - Employee Name
   - Leave Type
   - Sub Unit
5. Click "Search"
6. Select leave request cần action
7. Actions:

**Approve Leave:**
- Click icon "Approve" (checkmark)
- Add Comment (optional)
- Click "OK" để confirm
- Status đổi thành "Approved"
- Balance của employee bị trừ
- Employee nhận notification

**Reject Leave:**
- Click icon "Reject" (X)
- Add Comment (optional/required)
- Click "OK"
- Status đổi thành "Rejected"
- Balance không bị trừ
- Employee nhận notification

Kết quả mong đợi:
- Status change successfully
- Notification gửi đến employee
- Comment được lưu
- Leave balance update (nếu approved)
- Không thể approve nếu balance không đủ

[CHÈN SCREENSHOT 1: Leave List]
[CHÈN SCREENSHOT 2: Approve action]
[CHÈN SCREENSHOT 3: Reject with comment]
[CHÈN SCREENSHOT 4: Status changed]

---

1.2.6 Leave Reports (Báo cáo nghỉ phép)

**Admin Role**

Quy trình:
1. Đăng nhập Admin
2. Click "Leave" → "Reports"
3. Select report type:

**Leave Entitlements and Usage Report:**
- Select Employee
- Select Leave Type
- Select Leave Period
- Click "Generate"
- View report with: Entitled, Taken, Scheduled, Pending, Balance
- Export to Excel/CSV

**My Leave Entitlements and Usage:**
- View own leave report
- Filter by Leave Type
- Export

Kết quả mong đợi:
- Report hiển thị đúng data
- Calculation chính xác
- Có thể export
- Update real-time

[CHÈN SCREENSHOT 1: Report generation form]
[CHÈN SCREENSHOT 2: Report results]
[CHÈN SCREENSHOT 3: Export options]

```

---

## 🎨 BƯỚC 3: THIẾT KẾ TEST CASES (Test Design)

### File: TestDesign.xlsx

**Cấu trúc bảng:**

| Requirement Level 1 | Requirement Level 2 | Requirement Level 3 | Test Criteria | Test Type | Note |
|---------------------|---------------------|---------------------|---------------|-----------|------|

---

### 3.1. Test Design cho EMPLOYEE MANAGEMENT

```
Requirement L1 | Requirement L2 | Requirement L3 | Test Criteria | Test Type | Note

1.1 Employee Management | 1.1.1 Add Employee | Personal Info | Kiểm tra nhập First Name hợp lệ | Function |
| | | Kiểm tra First Name bỏ trống (required) | Validation |
| | | Kiểm tra First Name với số | Validation |
| | | Kiểm tra First Name với ký tự đặc biệt | Validation |
| | | Kiểm tra First Name max length (30 chars) | Boundary |

| | | Kiểm tra nhập Last Name hợp lệ | Function |
| | | Kiểm tra Last Name bỏ trống (required) | Validation |
| | | Kiểm tra Last Name với số | Validation |

| | | Kiểm tra Employee ID auto-generate | Function |
| | | Kiểm tra Employee ID nhập thủ công | Function |
| | | Kiểm tra Employee ID trùng lặp | Validation |
| | | Kiểm tra Employee ID format | Validation |

| | Photo Upload | Kiểm tra upload ảnh PNG | Function |
| | | Kiểm tra upload ảnh JPG | Function |
| | | Kiểm tra upload ảnh JPEG | Function |
| | | Kiểm tra upload file PDF (invalid) | Validation |
| | | Kiểm tra upload ảnh > 1MB | Validation |
| | | Kiểm tra upload ảnh = 1MB (boundary) | Boundary |
| | | Kiểm tra không upload ảnh (optional) | Function |

| | Create Login | Kiểm tra tạo login với username hợp lệ | Function |
| | | Kiểm tra username trùng lặp | Validation |
| | | Kiểm tra username với space | Validation |
| | | Kiểm tra password < 8 ký tự | Validation |
| | | Kiểm tra password = 8 ký tự (boundary) | Boundary |
| | | Kiểm tra password không match confirm | Validation |
| | | Kiểm tra password match confirm | Function |
| | | Kiểm tra Status Enabled | Function |
| | | Kiểm tra Status Disabled | Function |

| | Save | Kiểm tra click Save với data hợp lệ | Function |
| | | Kiểm tra Save với required fields trống | Validation |
| | | Kiểm tra success message | Function |
| | | Kiểm tra redirect to Personal Details | Function |

1.1 Employee Management | 1.1.2 Search Employee | Employee Name | Kiểm tra search by name (exact match) | Function |
| | | Kiểm tra search by name (partial match) | Function |
| | | Kiểm tra autocomplete khi nhập | Function |
| | | Kiểm tra search với name không tồn tại | Function |

| | Employee ID | Kiểm tra search by ID exact | Function |
| | | Kiểm tra search by ID partial | Function |
| | | Kiểm tra search với ID không tồn tại | Function |

| | Filters | Kiểm tra filter by Employment Status | Function |
| | | Kiểm tra filter by Job Title | Function |
| | | Kiểm tra filter by Sub Unit | Function |
| | | Kiểm tra filter by Supervisor | Function |
| | | Kiểm tra multiple filters combined | Function |
| | | Kiểm tra button Reset | Function |

| | Results | Kiểm tra hiển thị results phù hợp | Function |
| | | Kiểm tra pagination khi > 50 records | Function |
| | | Kiểm tra click vào employee name | Function |
| | | Kiểm tra select checkbox | Function |

1.1 Employee Management | 1.1.3 Edit Employee | Personal Details | Kiểm tra edit Name fields | Function |
| | | Kiểm tra edit Nationality | Function |
| | | Kiểm tra edit Marital Status | Function |
| | | Kiểm tra edit Date of Birth | Function |
| | | Kiểm tra edit Gender | Function |
| | | Kiểm tra Save button | Function |
| | | Kiểm tra success message | Function |

| | Contact Details | Kiểm tra edit Address fields | Function |
| | | Kiểm tra edit City, State, Zip | Function |
| | | Kiểm tra edit Country dropdown | Function |
| | | Kiểm tra edit Telephone fields | Function |
| | | Kiểm tra edit Email fields | Function |
| | | Kiểm tra email format validation | Validation |
| | | Kiểm tra phone format validation | Validation |

| | Emergency Contacts | Kiểm tra Add emergency contact | Function |
| | | Kiểm tra Edit contact | Function |
| | | Kiểm tra Delete contact | Function |
| | | Kiểm tra required fields | Validation |

| | Job Details | Kiểm tra edit Job Title | Function |
| | | Kiểm tra edit Employment Status | Function |
| | | Kiểm tra edit Join Date | Function |
| | | Kiểm tra upload contract file | Function |

| | Salary | Kiểm tra Add salary component | Function |
| | | Kiểm tra amount validation (số) | Validation |
| | | Kiểm tra currency selection | Function |
| | | Kiểm tra Edit salary | Function |
| | | Kiểm tra Delete salary | Function |

| | Qualifications | Kiểm tra Add Work Experience | Function |
| | | Kiểm tra Add Education | Function |
| | | Kiểm tra Add Skills | Function |
| | | Kiểm tra Add Languages | Function |
| | | Kiểm tra Add License | Function |
| | | Kiểm tra Edit/Delete cho mỗi loại | Function |

1.1 Employee Management | 1.1.4 Delete Employee | Delete | Kiểm tra select employee | Function |
| | | Kiểm tra click Delete Selected | Function |
| | | Kiểm tra confirmation popup | Function |
| | | Kiểm tra Cancel deletion | Function |
| | | Kiểm tra Confirm deletion | Function |
| | | Kiểm tra success message | Function |
| | | Kiểm tra employee không còn trong list | Function |
| | | Kiểm tra delete multiple employees | Function |

```

**Tổng Test Criteria cho Employee Management: ~175 criteria**

---

### 3.2. Test Design cho LEAVE MANAGEMENT

```
Requirement L1 | Requirement L2 | Requirement L3 | Test Criteria | Test Type | Note

1.2 Leave Management | 1.2.1 Configure | Leave Period | Kiểm tra set start month | Function |
| | | Kiểm tra set start date | Function |
| | | Kiểm tra Save period | Function |

| | Leave Types | Kiểm tra Add leave type | Function |
| | | Kiểm tra leave type name required | Validation |
| | | Kiểm tra Edit leave type | Function |
| | | Kiểm tra Delete leave type | Function |
| | | Kiểm tra duplicate leave type name | Validation |

| | Work Week | Kiểm tra select working days | Function |
| | | Kiểm tra all days selected | Function |
| | | Kiểm tra no days selected | Validation |
| | | Kiểm tra half day definition | Function |

| | Holidays | Kiểm tra Add holiday | Function |
| | | Kiểm tra holiday name required | Validation |
| | | Kiểm tra select date | Function |
| | | Kiểm tra Repeats Annually | Function |
| | | Kiểm tra Full Day/Half Day | Function |
| | | Kiểm tra Edit holiday | Function |
| | | Kiểm tra Delete holiday | Function |

1.2 Leave Management | 1.2.2 Add Entitlements | Form | Kiểm tra search employee | Function |
| | | Kiểm tra employee required | Validation |
| | | Kiểm tra select leave type | Function |
| | | Kiểm tra leave type required | Validation |
| | | Kiểm tra select period | Function |
| | | Kiểm tra nhập entitlement (days) | Function |
| | | Kiểm tra entitlement = 0 | Validation |
| | | Kiểm tra entitlement negative | Validation |
| | | Kiểm tra entitlement > 365 | Boundary |
| | | Kiểm tra entitlement với decimal | Function |
| | | Kiểm tra Save | Function |
| | | Kiểm tra success message | Function |

| | View | Kiểm tra Employee Entitlements list | Function |
| | | Kiểm tra search entitlements | Function |
| | | Kiểm tra Edit entitlement | Function |
| | | Kiểm tra Delete entitlement | Function |

1.2 Leave Management | 1.2.3 Apply Leave | Form | Kiểm tra select leave type | Function |
| | | Kiểm tra balance display | Function |
| | | Kiểm tra insufficient balance | Validation |
| | | Kiểm tra select From Date | Function |
| | | Kiểm tra select To Date | Function |
| | | Kiểm tra From Date > To Date | Validation |
| | | Kiểm tra past dates | Validation |
| | | Kiểm tra dates on holidays | Validation |
| | | Kiểm tra dates on weekends | Function |
| | | Kiểm tra overlapping leaves | Validation |

| | Duration | Kiểm tra auto-calculate days | Function |
| | | Kiểm tra single day leave | Function |
| | | Kiểm tra multiple days leave | Function |
| | | Kiểm tra partial days - All Days | Function |
| | | Kiểm tra partial - Start Day Only | Function |
| | | Kiểm tra partial - End Day Only | Function |
| | | Kiểm tra Half Day Morning | Function |
| | | Kiểm tra Half Day Afternoon | Function |
| | | Kiểm tra duration với half days | Function |

| | Submit | Kiểm tra click Apply | Function |
| | | Kiểm tra success message | Function |
| | | Kiểm tra leave status Pending | Function |
| | | Kiểm tra leave trong My Leave | Function |
| | | Kiểm tra comment optional | Function |
| | | Kiểm tra comment max length | Boundary |

1.2 Leave Management | 1.2.4 My Leave | View | Kiểm tra hiển thị leave list | Function |
| | | Kiểm tra filter by date range | Function |
| | | Kiểm tra filter by status | Function |
| | | Kiểm tra filter by leave type | Function |
| | | Kiểm tra multiple filters | Function |
| | | Kiểm tra Reset filters | Function |

| | Balance | Kiểm tra Leave Balance summary | Function |
| | | Kiểm tra balance cho từng leave type | Function |
| | | Kiểm tra balance update sau apply | Function |

| | Actions | Kiểm tra Cancel pending leave | Function |
| | | Kiểm tra không Cancel approved leave | Validation |
| | | Kiểm tra View Details | Function |

1.2 Leave Management | 1.2.5 Leave List | View | Kiểm tra view pending leaves | Function |
| | | Kiểm tra filter by employee | Function |
| | | Kiểm tra filter by leave type | Function |
| | | Kiểm tra filter by status | Function |
| | | Kiểm tra filter by date | Function |
| | | Kiểm tra search | Function |

| | Approve | Kiểm tra click Approve icon | Function |
| | | Kiểm tra add comment when approve | Function |
| | | Kiểm tra confirm approval | Function |
| | | Kiểm tra status change to Approved | Function |
| | | Kiểm tra balance deducted | Function |
| | | Kiểm tra notification to employee | Function |

| | Reject | Kiểm tra click Reject icon | Function |
| | | Kiểm tra add comment when reject | Function |
| | | Kiểm tra confirm rejection | Function |
| | | Kiểm tra status change to Rejected | Function |
| | | Kiểm tra balance not deducted | Function |
| | | Kiểm tra notification to employee | Function |

1.2 Leave Management | 1.2.6 Reports | Generate | Kiểm tra select report type | Function |
| | | Kiểm tra select employee | Function |
| | | Kiểm tra select leave type | Function |
| | | Kiểm tra select period | Function |
| | | Kiểm tra click Generate | Function |
| | | Kiểm tra report display | Function |

| | Data | Kiểm tra Entitled days | Function |
| | | Kiểm tra Taken days | Function |
| | | Kiểm tra Scheduled days | Function |
| | | Kiểm tra Pending days | Function |
| | | Kiểm tra Balance calculation | Function |
| | | Kiểm tra data accuracy | Function |

| | Export | Kiểm tra export to Excel | Function |
| | | Kiểm tra export to CSV | Function |
| | | Kiểm tra file download | Function |

```

**Tổng Test Criteria cho Leave Management: ~220 criteria**

---

### 3.3. Áp dụng kỹ thuật Test Design

**Các kỹ thuật Black-box Testing áp dụng:**

#### **1. Equivalence Partitioning (Phân vùng tương đương)**

**Ví dụ: Employee ID**
- Valid partition: 4-10 ký tự, alphanumeric
- Invalid partition: < 4 chars, > 10 chars, special characters
- Test representatives: "EMP001" (valid), "E" (invalid), "EMP1234567890" (invalid)

**Ví dụ: Leave Days**
- Valid: 0.5, 1, 2, ... 365
- Invalid: -1, 0, 366+, alphabets
- Test: 15 days (valid), -5 (invalid), 400 (invalid), "abc" (invalid)

---

#### **2. Boundary Value Analysis (Phân tích giá trị biên)**

**Ví dụ: First Name (max 30 chars)**
- Test: 29 chars, 30 chars, 31 chars

**Ví dụ: Password (min 8 chars)**
- Test: 7 chars, 8 chars, 9 chars

**Ví dụ: Photo size (max 1MB)**
- Test: 0.99MB, 1MB, 1.01MB

**Ví dụ: Leave entitlement (0-365 days)**
- Test: -1, 0, 1, 364, 365, 366

---

#### **3. Decision Table (Bảng quyết định)**

**Ví dụ: Apply Leave**

| Employee logged in | Balance sufficient | Dates valid | Not holiday | Not overlap | Result |
|--------------------|-------------------|-------------|-------------|-------------|---------|
| Yes | Yes | Yes | Yes | Yes | Apply Success |
| Yes | Yes | Yes | Yes | No | Error: Overlap |
| Yes | Yes | Yes | No | Yes | Warning: Holiday |
| Yes | Yes | No | Yes | Yes | Error: Invalid dates |
| Yes | No | Yes | Yes | Yes | Error: Insufficient |
| No | - | - | - | - | Redirect to Login |

---

#### **4. State Transition (Chuyển trạng thái)**

**Ví dụ: Leave Status**

```
[Pending] --Approve--> [Approved] --Take--> [Taken]
    |
    +----Reject----> [Rejected]
    |
    +----Cancel----> [Cancelled]

Valid transitions:
- Pending → Approved ✓
- Pending → Rejected ✓
- Pending → Cancelled ✓
- Approved → Taken ✓

Invalid transitions:
- Rejected → Approved ✗
- Cancelled → Approved ✗
- Taken → Cancelled ✗
```

---

## ✅ BƯỚC 4: VIẾT TEST CASES CHI TIẾT

### File: TestCase.xlsx

**Tạo 2 sheets:**
1. **Sheet 1: Employee Management**
2. **Sheet 2: Leave Management**

---

### Header cho mỗi sheet:

```
Module Code: Employee Management
Test requirement: UC-01 Employee CRUD Operations
Tester: [Họ tên]

Statistics:
Passed: =COUNTIF(G12:G200,"Passed")
Failed: =COUNTIF(G12:G200,"Failed")
Untested: =COUNTIF(G12:G200,"Untested")
Blocked: =COUNTIF(G12:G200,"Blocked")
Number of Test cases: =SUM(A6:D6)
```

---

### Cấu trúc cột:

| ID | Test Case Description | Preconditions | Test Case Procedure | Expected Output | Inter-test case Dependence | Result | Test date | Note |

---

### Ví dụ Test Cases cụ thể:

#### **EMPLOYEE MANAGEMENT - Test Cases**

| ID | Test Case Description | Preconditions | Test Case Procedure | Expected Output | Result | Test date | Note |
|----|----------------------|---------------|---------------------|-----------------|--------|-----------|------|
| EM01 | Kiểm tra Add Employee với dữ liệu hợp lệ đầy đủ | Login as Admin | 1. Navigate to PIM → Add Employee<br>2. Nhập First Name: "John"<br>3. Nhập Last Name: "Doe"<br>4. Employee ID: Auto-generate<br>5. Upload photo valid (test.png, 500KB)<br>6. Check "Create Login Details"<br>7. Username: "john.doe"<br>8. Password: "Pass123!"<br>9. Confirm Password: "Pass123!"<br>10. Status: Enabled<br>11. Click Save | 1. Hiển thị "Successfully Saved"<br>2. Redirect to Personal Details page<br>3. Employee ID được auto-generate<br>4. Photo hiển thị đúng<br>5. Thông tin được lưu<br>6. Employee xuất hiện trong list | Passed | 2024-01-15 | |
| EM02 | Kiểm tra Add Employee với First Name trống | Login as Admin | 1. Navigate to PIM → Add Employee<br>2. Bỏ trống First Name<br>3. Nhập Last Name: "Doe"<br>4. Click Save | 1. Hiển thị error "Required"<br>2. Form không submit<br>3. Focus vào First Name field | Failed | 2024-01-15 | Không hiển thị error message |
| EM03 | Kiểm tra Add Employee với First Name có số | Login as Admin | 1. Navigate to PIM → Add Employee<br>2. Nhập First Name: "John123"<br>3. Nhập Last Name: "Doe"<br>4. Click Save | 1. Hiển thị error "Only letters allowed"<br>2. Form không submit | Passed | 2024-01-15 | |
| EM04 | Kiểm tra Employee ID trùng lặp | Employee "EMP001" đã tồn tại | 1. Navigate to PIM → Add Employee<br>2. Nhập First Name: "Jane"<br>3. Nhập Last Name: "Smith"<br>4. Nhập Employee ID: "EMP001"<br>5. Click Save | 1. Hiển thị error "Employee Id already exists"<br>2. Form không submit | Passed | 2024-01-15 | |
| EM05 | Kiểm tra upload photo > 1MB | Login as Admin | 1. Navigate to PIM → Add Employee<br>2. Nhập First Name: "Test", Last Name: "User"<br>3. Upload photo 2MB<br>4. Click Save | 1. Hiển thị error "File size exceeds 1MB"<br>2. Photo không được upload | Passed | 2024-01-15 | |

(Tiếp tục ~170 test cases nữa...)

---

#### **LEAVE MANAGEMENT - Test Cases**

| ID | Test Case Description | Preconditions | Test Case Procedure | Expected Output | Result | Test date | Note |
|----|----------------------|---------------|---------------------|-----------------|--------|-----------|------|
| LM01 | Kiểm tra Add Leave Type với tên hợp lệ | Login as Admin | 1. Navigate to Leave → Configure → Leave Types<br>2. Click Add<br>3. Nhập Name: "Annual Leave"<br>4. Click Save | 1. Hiển thị "Successfully Saved"<br>2. Leave type xuất hiện trong list<br>3. Available trong dropdown khi apply leave | Passed | 2024-01-16 | |
| LM02 | Kiểm tra Add Entitlement với balance hợp lệ | Login as Admin<br>Employee "John Doe" exists<br>Leave Type "Annual" exists | 1. Navigate to Leave → Entitlements → Add<br>2. Search và select Employee: "John Doe"<br>3. Select Leave Type: "Annual Leave"<br>4. Select Period: "2024"<br>5. Nhập Entitlement: 15<br>6. Click Save | 1. Hiển thị "Successfully Saved"<br>2. Entitlement xuất hiện trong list<br>3. Employee có thể xem balance = 15 | Passed | 2024-01-16 | |
| LM03 | Kiểm tra Apply Leave với balance đủ | Login as Employee<br>Entitlement: 15 days | 1. Navigate to Leave → Apply<br>2. Select Leave Type: "Annual Leave"<br>3. Verify balance shows 15<br>4. From Date: 2024-06-01<br>5. To Date: 2024-06-03<br>6. Verify Duration = 3<br>7. Click Apply | 1. Hiển thị "Successfully Saved"<br>2. Leave status = "Pending Approval"<br>3. Balance vẫn = 15 (chưa trừ)<br>4. Leave xuất hiện trong My Leave | Passed | 2024-01-16 | |
| LM04 | Kiểm tra Apply Leave với balance không đủ | Login as Employee<br>Entitlement: 2 days | 1. Navigate to Leave → Apply<br>2. Select Leave Type: "Annual Leave"<br>3. Balance shows 2<br>4. From Date: 2024-06-01<br>5. To Date: 2024-06-05 (5 days)<br>6. Click Apply | 1. Hiển thị error "Balance not sufficient"<br>2. Form không submit<br>3. Balance vẫn = 2 | Failed | 2024-01-16 | Vẫn submit được, không validate |
| LM05 | Kiểm tra Apply Leave với dates overlap | Login as Employee<br>Leave 2024-06-01 to 06-03 đã tồn tại | 1. Navigate to Leave → Apply<br>2. Select Leave Type: "Annual Leave"<br>3. From Date: 2024-06-02<br>4. To Date: 2024-06-04<br>5. Click Apply | 1. Hiển thị error "Overlapping leaves"<br>2. Form không submit | Passed | 2024-01-16 | |

(Tiếp tục ~215 test cases nữa...)

---

### Phân loại Test Cases:

#### **4.1. Positive Test Cases (Happy Path)**
```
✓ Dữ liệu hợp lệ
✓ Workflow thành công
✓ Kết quả như mong đợi
```

#### **4.2. Negative Test Cases**
```
✓ Dữ liệu không hợp lệ
✓ Required fields trống
✓ Invalid format
✓ Out of range
```

#### **4.3. Boundary Test Cases**
```
✓ Min value
✓ Max value
✓ Min - 1, Max + 1
```

#### **4.4. Integration Test Cases**
```
✓ Cross-module testing
✓ Workflow spanning multiple screens
✓ Data consistency
```

---

## 🐛 BƯỚC 5: BÁO CÁO BUGS/ISSUES

### File: Q_A.xls

**Cấu trúc bảng:**

| # | Function area | Document | Doc Version | Section/screen | Comment/Question | Answer | Status | Owner | Priority | Closed In Version | Raised by | Date raised | Required finish date | Date closed |

---

### Ví dụ Bugs phát hiện được:

| # | Function area | Document | Version | Section | Comment/Question | Status | Priority | Raised by | Date |
|---|---------------|----------|---------|---------|------------------|--------|----------|-----------|------|
| 1 | Employee Management | UC-01 Add Employee | 1.0 | Personal Details | First Name field không validate khi nhập số. User có thể nhập "John123" và form vẫn submit thành công. Đề xuất: Thêm validation chỉ cho phép chữ cái và space. | Open | High | Tester A | 2024-01-15 |
| 2 | Employee Management | UC-01 Add Employee | 1.0 | Photo Upload | Khi upload ảnh > 1MB, form vẫn submit nhưng ảnh không được lưu. Không có error message nào hiển thị. Đề xuất: Hiển thị error "File size exceeds 1MB limit" và prevent submit. | Open | Medium | Tester A | 2024-01-15 |
| 3 | Employee Management | UC-02 Edit Employee | 1.0 | Contact Details | Email validation không đúng. Có thể nhập "test@" và "test.com" đều được accept. Đề xuất: Validate email format phải có @ và domain. | Open | High | Tester B | 2024-01-16 |
| 4 | Leave Management | UC-03 Apply Leave | 1.0 | Leave Form | Có thể apply leave với balance không đủ. System không validate balance trước khi submit. Đề xuất: Check balance và hiển thị error nếu insufficient. | Open | Critical | Tester C | 2024-01-17 |
| 5 | Leave Management | UC-03 Apply Leave | 1.0 | Leave Form | From Date có thể chọn date in the past. Không có validation. Đề xuất: Disable past dates trong date picker. | Open | Medium | Tester C | 2024-01-17 |
| 6 | Leave Management | UC-04 Leave List | 1.0 | Approve/Reject | Khi approve leave, balance được trừ ngay. Nhưng nếu sau đó reject, balance không được hoàn lại. Đề xuất: Restore balance khi change from Approved to Rejected. | Open | High | Tester D | 2024-01-18 |
| 7 | Leave Management | UC-05 Reports | 1.0 | Generate Report | Report hiển thị sai số Taken days. Calculation không tính partial days correctly. Half day được tính là 1 day. Đề xuất: Fix calculation cho partial days. | Open | Medium | Tester D | 2024-01-18 |
| 8 | Employee Management | UC-01 Add Employee | 1.0 | Create Login | Username có thể chứa space. "john doe" được accept. Đề xuất: Validate username không có space. | Open | Low | Tester A | 2024-01-15 |
| 9 | Employee Management | UC-02 Search Employee | 1.0 | Search Form | Khi search với Employee ID không tồn tại, không có message "No records found". Page hiển thị blank. Đề xuất: Hiển thị friendly message. | Open | Low | Tester B | 2024-01-16 |
| 10 | Leave Management | UC-03 Apply Leave | 1.0 | Leave Form | Comment field không có max length validation. User có thể nhập text rất dài làm layout bị vỡ. Đề xuất: Limit 500 characters cho comment. | Open | Low | Tester C | 2024-01-17 |

---

### Priority Levels:

- **Critical**: Chặn hoàn toàn luồng chính, không thể tiếp tục (ví dụ: Không apply được leave)
- **High**: Ảnh hưởng nghiêm trọng đến chức năng, có workaround (ví dụ: Validation sai)
- **Medium**: Ảnh hưởng vừa phải, không chặn workflow (ví dụ: UI không đẹp)
- **Low**: Vấn đề nhỏ, cosmetic (ví dụ: Typo, alignment)

---

## 📊 BƯỚC 6: HOÀN THIỆN BÁO CÁO

### File: Report.doc

**Cấu trúc báo cáo hoàn chỉnh:**

```
COVER PAGE
- Tên môn học: Software Testing
- Đề tài: Testing OrangeHRM - Employee Management & Leave Management
- Họ tên, MSSV: [7 thành viên]
- Lớp: [Tên lớp]
- Ngày nộp: [Ngày]

---

TABLE OF CONTENTS
1. Functionality Requirements ........................ 3
2. Test Strategy ....................................... 8
3. Test Design ......................................... 10
4. Test Execution Summary ............................. 12
5. Bug Report Summary ................................. 14
6. Conclusion & Recommendations ....................... 16

---

1. FUNCTIONALITY REQUIREMENTS

[Copy toàn bộ nội dung từ Bước 2]

---

2. TEST STRATEGY

2.1 Test Approach

Chúng em sử dụng phương pháp **Black-box Testing** kết hợp 
**Automation Testing** với Selenium Python.

**Black-box Testing:**
- Test dựa trên requirements và specifications
- Không cần xem source code của OrangeHRM
- Test từ góc nhìn end-user
- Focus vào input-output behavior

**Automation Testing:**
- Sử dụng Selenium WebDriver với Python
- Page Object Model pattern
- Pytest framework cho test execution
- HTML reports tự động generate

**Test Types:**
- Functional Testing (70%)
- Validation Testing (20%)
- GUI Testing (10%)

---

2.2 Test Environment

**System Under Test:**
- Application: OrangeHRM Open Source
- Version: 4.10.1
- URL: https://opensource-demo.orangehrmlive.com/
- Test Account: Admin / admin123

**Test Environment:**
- Browser: Google Chrome 120.x
- OS: Windows 11 / macOS Sonoma
- Screen Resolution: 1920x1080
- Python: 3.9+
- Selenium: 4.15.0

---

2.3 Test Schedule

**Week 1 (15/01 - 21/01): Requirements & Analysis**
- Nghiên cứu OrangeHRM system
- Phân tích 2 chức năng chính
- Viết Requirements Document
- Chụp screenshots

**Week 2 (22/01 - 28/01): Test Design**
- Thiết kế test cases
- Áp dụng test techniques
- Hoàn thành TestDesign.xlsx
- Review test criteria

**Week 3 (29/01 - 04/02): Test Implementation & Execution**
- Code Selenium automation scripts
- Implement Page Object Model
- Execute test cases
- Record results (Pass/Fail)
- Capture screenshots của bugs

**Week 4 (05/02 - 11/02): Bug Reporting & Documentation**
- Tổng hợp bugs (Q_A.xls)
- Generate HTML test reports
- Hoàn thiện Report.doc
- Final review và submit

---

2.4 Test Techniques Applied

**1. Equivalence Partitioning:**
Chia input data thành các nhóm tương đương và test 
1 representative value từ mỗi nhóm.

Ví dụ: Employee ID
- Valid: 4-10 chars alphanumeric → Test "EMP001"
- Invalid: <4 chars → Test "E"
- Invalid: >10 chars → Test "EMP12345678901"
- Invalid: Special chars → Test "EMP@001"

**2. Boundary Value Analysis:**
Test các giá trị ở boundary của input domains.

Ví dụ: Leave entitlement (0-365 days)
- Test: -1, 0, 1, 364, 365, 366

Ví dụ: Password length (min 8 chars)
- Test: 7 chars, 8 chars, 9 chars

**3. Decision Table Testing:**
Test các combinations của conditions.

Ví dụ: Apply Leave decision
- Conditions: Logged in, Balance sufficient, Valid dates, Not holiday, Not overlap
- Actions: Apply success / Show error

**4. State Transition Testing:**
Test các state changes của system.

Ví dụ: Leave status transitions
- Pending → Approved → Taken
- Pending → Rejected
- Pending → Cancelled

---

3. TEST DESIGN

3.1 Test Coverage

**Module 1: Employee Management**
- Total Test Criteria: 175
- Categories:
  + Add Employee: 50 criteria
  + Search Employee: 35 criteria
  + Edit Employee: 70 criteria
  + Delete Employee: 20 criteria

**Module 2: Leave Management**
- Total Test Criteria: 220
- Categories:
  + Configure: 40 criteria
  + Entitlements: 30 criteria
  + Apply Leave: 60 criteria
  + My Leave: 25 criteria
  + Leave List (Approve/Reject): 45 criteria
  + Reports: 20 criteria

**Total: 395 Test Criteria**

[Chi tiết tham khảo file TestDesign.xlsx]

---

3.2 Test Case Distribution

- Functional Tests: 275 cases (70%)
- Validation Tests: 80 cases (20%)
- GUI Tests: 40 cases (10%)

---

4. TEST EXECUTION SUMMARY

4.1 Overall Statistics

**Total Test Cases Executed: 395**
- Passed: 355 (90%)
- Failed: 35 (9%)
- Blocked: 5 (1%)
- Not Tested: 0 (0%)

[CHÈN BIỂU ĐỒ PIE CHART]

**Execution Time:**
- Manual Testing: ~80 hours (if manual)
- Automation Testing: ~2 hours per full run
- Total Development Time: ~120 hours

---

4.2 Test Results by Module

**Module 1: Employee Management**
- Total: 175 cases
- Passed: 160 (91%)
- Failed: 12 (7%)
- Blocked: 3 (2%)

**Top Failed Areas:**
1. Add Employee validation (5 fails)
2. Edit Contact Details validation (4 fails)
3. Photo upload errors (3 fails)

**Module 2: Leave Management**
- Total: 220 cases
- Passed: 195 (89%)
- Failed: 23 (10%)
- Blocked: 2 (1%)

**Top Failed Areas:**
1. Apply Leave validation (10 fails)
2. Balance calculation (8 fails)
3. Date validation (5 fails)

---

4.3 Failed Test Cases Analysis

**Critical Failures (Must Fix):**
1. LM04: Apply leave không validate balance
2. LM15: Balance không restore khi reject leave
3. EM22: Email validation không đúng format

**High Priority Failures:**
1. EM02: First Name không validate số
2. LM05: Past dates không bị block
3. LM30: Report calculation sai với half days

**Medium/Low Priority:**
1. UI alignment issues (5 cases)
2. Missing friendly messages (3 cases)
3. Cosmetic bugs (7 cases)

[Chi tiết tham khảo file TestCase.xlsx]

---

5. BUG REPORT SUMMARY

5.1 Bug Statistics

**Total Bugs Found: 35**
- Critical: 3 (9%)
- High: 8 (23%)
- Medium: 15 (43%)
- Low: 9 (25%)

[CHÈN BIỂU ĐỒ BAR CHART]

---

5.2 Top Critical Issues

**Bug #1: Apply Leave không validate balance**
- Severity: Critical
- Module: Leave Management
- Description: User có thể apply leave khi balance không đủ. 
  System không check và cho phép submit form.
- Impact: Data integrity issue, overspending leave balance
- Recommendation: Add validation check balance before submit

**Bug #2: Balance không restore khi reject approved leave**
- Severity: Critical  
- Module: Leave Management
- Description: Khi admin approve leave, balance bị trừ. Nhưng nếu 
  sau đó reject, balance không được hoàn lại.
- Impact: Incorrect balance calculation
- Recommendation: Implement balance restoration logic

**Bug #3: Email validation không đúng format**
- Severity: High
- Module: Employee Management
- Description: Email field accept "test@" và "test.com" 
  (không có @ hoặc domain)
- Impact: Invalid data trong database
- Recommendation: Use proper regex for email validation

[Chi tiết tham khảo file Q_A.xls]

---

5.3 Bug Distribution by Module

**Employee Management: 12 bugs**
- Critical: 0
- High: 3
- Medium: 6
- Low: 3

**Leave Management: 23 bugs**
- Critical: 3
- High: 5
- Medium: 9
- Low: 6

---

6. CONCLUSION & RECOMMENDATIONS

6.1 Overall Assessment

Tổng thể hệ thống OrangeHRM có chất lượng **khá tốt** với 90% 
test cases passed. Tuy nhiên, vẫn còn một số vấn đề về validation 
và business logic cần được khắc phục.

**Điểm mạnh:**
- UI/UX thân thiện, dễ sử dụng
- Workflow logic và rõ ràng
- Đầy đủ chức năng cho HR management
- Responsive design tốt
- Performance ổn định

**Điểm cần cải thiện:**
- Validation chưa đầy đủ (nhiều fields không validate)
- Business logic còn bugs (balance calculation)
- Error messages chưa rõ ràng
- Missing confirmation dialogs ở một số actions
- Date picker không restrict past dates

---

6.2 Key Findings

**Functionality:**
- Core functions hoạt động tốt
- CRUD operations ổn định
- Workflow phức tạp cần improvement

**Usability:**
- User-friendly interface
- Intuitive navigation
- Good feedback messages (when present)

**Reliability:**
- Stable performance
- No crashes observed
- Data persistence works well

**Security:**
- Password validation weak (needs stronger rules)
- Session management OK
- Authorization working correctly

---

6.3 Recommendations

**Immediate Actions (Critical/High priority):**
1. Fix balance validation trong Apply Leave
2. Implement balance restoration logic
3. Improve email/phone validation
4. Add date validation (block past dates)
5. Fix half-day calculation trong reports

**Short-term (Medium priority):**
1. Add confirmation dialogs cho delete actions
2. Improve error messages (more specific)
3. Add "No records found" messages
4. Fix UI alignment issues
5. Add max length validation cho text fields

**Long-term (Low priority/Enhancements):**
1. Implement password strength meter
2. Add bulk operations (bulk approve leaves)
3. Export functionality for all lists
4. Email notifications for leave approvals
5. Mobile app development

---

6.4 Future Testing Suggestions

**Performance Testing:**
- Load testing với 1000+ concurrent users
- Stress testing với 10000+ employee records
- Response time measurement

**Security Testing:**
- Penetration testing
- SQL injection testing
- XSS vulnerability testing
- Authentication bypass attempts

**Compatibility Testing:**
- Cross-browser testing (Firefox, Safari, Edge)
- Mobile responsive testing
- Different OS testing

**Automation Enhancement:**
- Implement CI/CD pipeline
- Increase test coverage to 95%+
- Add API testing
- Implement visual regression testing

---

REFERENCES

1. OrangeHRM Official Documentation
2. Selenium WebDriver Documentation
3. Software Testing - Principles and Practices (Textbook)
4. ISTQB Foundation Level Syllabus

---

APPENDIX

A. TestDesign.xlsx - Test criteria spreadsheet
B. TestCase.xlsx - Detailed test cases with results
C. Q_A.xls - Bug report spreadsheet
D. Selenium Code - Automation scripts (GitHub link)
E. HTML Test Reports - Pytest execution reports
F. Screenshots - Evidence of bugs
```

---

## 🎯 TIMELINE CHI TIẾT (4 TUẦN)

**TUẦN 1: Requirements & Analysis (40 hours)**

**Ngày 1-2 (8h):**
- Setup OrangeHRM demo account
- Explore 2 chức năng chính
- Chụp screenshots (~50 screenshots)

**Ngày 3-4 (16h):**
- Viết Requirements Document
- Mô tả chi tiết từng sub-function
- Chèn screenshots vào document

**Ngày 5-7 (16h):**
- Review requirements
- Bổ sung missing information
- Format document đẹp

---

**TUẦN 2: Test Design (50 hours)**

**Ngày 1-2 (16h):**
- Phân tích requirements
- Identify test conditions
- Áp dụng test techniques

**Ngày 3-5 (24h):**
- Viết test criteria
- Tạo TestDesign.xlsx
- ~400 test criteria

**Ngày 6-7 (10h):**
- Review test design
- Add missing criteria
- Validate với requirements

---

**TUẦN 3: Implementation & Execution (70 hours)**

**Ngày 1-2 (20h):**
- Setup Selenium environment
- Create Page Object Model
- Base framework

**Ngày 3-4 (20h):**
- Code automation scripts
- Employee Management tests
- ~175 test cases

**Ngày 5-6 (20h):**
- Code automation scripts
- Leave Management tests
- ~220 test cases

**Ngày 7 (10h):**
- Execute all tests
- Record results
- Capture bug screenshots

---

**TUẦN 4: Bug Report & Documentation (40 hours)**

**Ngày 1-2 (12h):**
- Analyze failed test cases
- Write bug descriptions
- Tạo Q_A.xls

**Ngày 3-4 (16h):**
- Write Test Strategy
- Write Test Execution Summary
- Write Bug Report Summary

**Ngày 5-6 (8h):**
- Write Conclusion
- Create charts/graphs
- Format entire report

**Ngày 7 (4h):**
- Final review
- Validate checklist
- Submit project

---

## 💡 TIPS QUAN TRỌNG

### ✅ DOs (NÊN LÀM)

1. **Automation Script nên có:**
   ```python
   - Page Object Model (tách logic)
   - Reusable functions
   - Clear comments
   - Exception handling
   - Screenshots on failure
   - HTML reports
   ```

2. **Test Cases nên:**
   - Independent (không phụ thuộc nhau)
   - Repeatable (chạy lại được)
   - Clear steps (dễ hiểu)
   - Specific expected results
   - Include test data

3. **Screenshots nên:**
   - Clear, high resolution
   - Highlight important parts
   - Include in bug reports
   - Numbered consistently
   - Show before/after

4. **Report nên:**
   - Professional format
   - Charts & statistics
   - Clear headings
   - Page numbers
   - Table of contents

---

### ❌ DON'Ts (KHÔNG NÊN)

1. **Đừng hardcode data:**
   ```python
   ❌ Sai: driver.get("https://...")
   ✅ Đúng: driver.get(Config.BASE_URL)
   
   ❌ Sai: login("Admin", "admin123")
   ✅ Đúng: login(Config.USERNAME, Config.PASSWORD)
   ```

2. **Đừng skip error handling:**
   ```python
   ❌ Sai: element.click()
   ✅ Đúng: 
   try:
       element.click()
   except ElementNotClickableException:
       self.scroll_to_element(element)
       element.click()
   ```

3. **Đừng viết test case phụ thuộc:**
   ```
   ❌ Sai: TC02 depends on TC01 passing
   ✅ Đúng: Mỗi TC độc lập, có setup riêng
   ```

---

## 📚 CHECKLIST TRƯỚC KHI NỘP

### Report.doc
- [ ] Cover page đầy đủ (7 members)
- [ ] Table of contents với page numbers
- [ ] Requirements có 50+ screenshots
- [ ] Test Strategy rõ ràng (Black-box + Automation)
- [ ] Test Design summary
- [ ] Test Execution với statistics & charts
- [ ] Bug Report với priority
- [ ] Conclusion with recommendations
- [ ] References & Appendix

### TestDesign.xlsx
- [ ] 2 sheets (Employee + Leave)
- [ ] 3 levels requirements
- [ ] ~400 test criteria total
- [ ] Test Type marked (Function/Validation/GUI)
- [ ] Formatted đẹp với colors

### TestCase.xlsx
- [ ] 2 sheets (Employee + Leave)
- [ ] Header có statistics với formulas
- [ ] ~400 test cases total
- [ ] ID liên tục (1, 2, 3...)
- [ ] Description rõ ràng
- [ ] Steps detailed, numbered
- [ ] Expected Output specific
- [ ] Result filled (Passed/Failed)
- [ ] Test date filled
- [ ] Notes cho Failed cases

### Q_A.xls
- [ ] Đủ columns quan trọng
- [ ] ~35 bugs documented
- [ ] Description rõ ràng
- [ ] Priority assigned
- [ ] Status marked (Open/Closed)
- [ ] Raised by filled
- [ ] Date raised filled

### Selenium Code
- [ ] Page Object Model implemented
- [ ] Clean code structure
- [ ] Comments đầy đủ
- [ ] Requirements.txt có
- [ ] README.md hướng dẫn run
- [ ] pytest.ini configured
- [ ] HTML reports generated
- [ ] Screenshots folder có evidence

---

## 🎓 SCORING CRITERIA

**Report (30%)**
- Requirements chi tiết: 10%
- Test Strategy hợp lý: 7%
- Execution Summary với stats: 8%
- Conclusion có insights: 5%

**Test Design (20%)**
- Coverage đầy đủ: 8%
- Test criteria proper: 7%
- Test techniques applied: 5%

**Test Cases (25%)**
- Số lượng đủ (400+): 8%
- Quality (clear, specific): 10%
- Results recorded: 7%

**Bug Report (15%)**
- Số lượng bugs (30-40): 5%
- Description rõ ràng: 5%
- Priority đúng: 5%

**Automation Code (10%)**
- Code quality: 5%
- Framework design: 3%
- Reports generated: 2%

---

## 🚀 KẾT LUẬN

**QUY TRÌNH TỔNG QUÁT:**

```
Week 1: Requirements
   ↓
Week 2: Test Design (400 criteria)
   ↓
Week 3: Code Selenium + Execute (400 cases)
   ↓
Week 4: Bug Report (35 bugs) + Documentation
   ↓
Submit: Report + TestDesign + TestCase + Q&A + Code
```

**KEY TAKEAWAYS:**

✅ Black-box Testing + Automation = Best approach
✅ Page Object Model = Clean, maintainable code
✅ ~400 test cases = Comprehensive coverage
✅ End-to-end flows = Real-world scenarios
✅ Professional documentation = High scores


---

