# Study-Tech-Web
Buổi 1: Học CRUD
1. Kiến trúc cơ bản của một APIEndpoint (Đường dẫn): Là các địa chỉ như /phones, /hello. Mỗi địa chỉ dẫn đến một chức năng khác nhau.JSON: Định dạng dữ liệu tiêu chuẩn để Backend nói chuyện với Frontend (dạng { "key": "value" }).Path Parameters: Cách truyền dữ liệu trực tiếp qua đường dẫn, ví dụ: /phones/1.Query Parameters: Cách gửi thêm thông tin sau dấu ?, ví dụ: /search?max_price=1000.

2. Bộ kỹ năng CRUD (Trái tim của Backend)Bạn đã thành thạo việc điều khiển dữ liệu thông qua các "động từ" HTTP:Thao tácPhương thứcÝ nghĩaLệnh Python tương ứngCreatePOSTThêm mới dữ liệuphones.append(new_item)ReadGETLấy dữ liệu để xemreturn phonesUpdatePUTChỉnh sửa dữ liệu cũphones[index] = updated_itemDeleteDELETE/GETXóa bỏ dữ liệuphones.pop(index)

3. Những bài học "xương máu" về lỗi (Debugging)Chúng ta đã cùng nhau vượt qua những lỗi mà mọi lập trình viên đều phải gặp:Lỗi 404 (Not Found): Sai đường dẫn hoặc chưa bắt đầu bằng dấu /.Lỗi 422 (Validation Error): Gửi thiếu dữ liệu bắt buộc (như thiếu name trong bài tập đầu).Lỗi 500 (Internal Server Error): Thường do logic code Python bị sai (như lỗi so sánh chuỗi với số hoặc dùng nhầm hàm .pop()).Kiểu dữ liệu: Sự khác biệt giữa Chuỗi "100" và Số 100. Chỉ có số mới dùng được các toán tử >=, <=.

4. Công cụ hỗ trợSwagger UI (/docs): "Vũ khí" lợi hại của FastAPI giúp bạn chạy thử (Test) các hàm POST, PUT, DELETE mà không cần viết giao diện Frontend.

5. Tư duy nâng cao: Persistence (Dữ liệu bền vững)Bạn đã hiểu rằng dữ liệu lưu trong biến (RAM) sẽ bị mất khi server khởi động lại.Bạn đã biết hướng giải quyết là phải lưu vào File (JSON) hoặc Database để dữ liệu tồn tại vĩnh viễn.

Buổi 2: Nhúng backend với HTML
1. Về mặt Backend (FastAPI & Python)
Bạn đã hoàn thiện trọn bộ kỹ năng CRUD (Create - Read - Update - Delete) trên dữ liệu thực:

Create (POST): Biết cách tự động tính toán ID mới bằng cách lấy id cuối + 1 để lưu sản phẩm vào file JSON.

Read (GET): Trả về toàn bộ danh sách điện thoại hoặc một file HTML hoàn chỉnh thông qua Jinja2Templates.

Update (PUT): Tìm sản phẩm theo ID trong mảng, cập nhật thông tin mới và dùng saveData() để ghi đè vào file.

Delete (GET/DELETE): Loại bỏ sản phẩm khỏi danh sách dựa trên ID người dùng yêu cầu.

2. Về mặt Frontend (HTML & JavaScript)
Bạn đã biến những dòng JSON khô khan thành một giao diện tương tác:

Kết nối API (fetch): Biết cách dùng JavaScript để "gọi điện" lên Server lấy dữ liệu hoặc gửi dữ liệu đi.

DOM Manipulation: Dùng JavaScript để tự động "vẽ" các thẻ <li> và nút bấm lên màn hình dựa trên dữ liệu nhận được.

Quản lý trạng thái Form: Biết cách tạo "ô nhập liệu ẩn" (hidden input) để lưu giữ ID sản phẩm khi đang trong chế độ Sửa.

3. Quy trình vận hành hệ thống
Bạn đã hiểu cách một ứng dụng web vận hành theo mô hình Client-Server:

Người dùng thao tác trên giao diện (Frontend).

Trình duyệt gửi yêu cầu (Request) kèm dữ liệu lên FastAPI (Backend).

FastAPI xử lý dữ liệu, ghi vào file data.json.

FastAPI gửi phản hồi (Response) báo thành công.

Trình duyệt nhận phản hồi và tự động gọi lại hàm loadAdminData() để cập nhật màn hình mà không cần F5.

4. Những "bài học xương máu" từ lỗi (Debug)
Sáng nay bạn đã gặp và tự tay sửa những lỗi kinh điển nhất của lập trình viên:

Lỗi 404/500: Do sai đường dẫn hoặc quên lưu file.

ReferenceError: Do dùng biến chưa khai báo (như lỗi response hay addPhone).

Đồng bộ dữ liệu: Tại sao giá không đổi? -> Do chưa ép kiểu parseInt() hoặc chưa gọi lại hàm load dữ liệu sau khi sửa.

Chiều nay chúng ta sẽ tiếp tục với:

Pydantic Validation: Bắt lỗi ngay từ "vòng gửi xe" (Ví dụ: Giá không được âm, tên không được để trống).

Thông báo chuyên nghiệp: Thay vì dùng alert() nhàm chán, chúng ta sẽ làm các thông báo popup đẹp mắt hơn.