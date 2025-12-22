# Study-Tech-Web
Buổi 1: Học CRUD
1. Kiến trúc cơ bản của một APIEndpoint (Đường dẫn): Là các địa chỉ như /phones, /hello. Mỗi địa chỉ dẫn đến một chức năng khác nhau.JSON: Định dạng dữ liệu tiêu chuẩn để Backend nói chuyện với Frontend (dạng { "key": "value" }).Path Parameters: Cách truyền dữ liệu trực tiếp qua đường dẫn, ví dụ: /phones/1.Query Parameters: Cách gửi thêm thông tin sau dấu ?, ví dụ: /search?max_price=1000.

2. Bộ kỹ năng CRUD (Trái tim của Backend)Bạn đã thành thạo việc điều khiển dữ liệu thông qua các "động từ" HTTP:Thao tácPhương thứcÝ nghĩaLệnh Python tương ứngCreatePOSTThêm mới dữ liệuphones.append(new_item)ReadGETLấy dữ liệu để xemreturn phonesUpdatePUTChỉnh sửa dữ liệu cũphones[index] = updated_itemDeleteDELETE/GETXóa bỏ dữ liệuphones.pop(index)

3. Những bài học "xương máu" về lỗi (Debugging)Chúng ta đã cùng nhau vượt qua những lỗi mà mọi lập trình viên đều phải gặp:Lỗi 404 (Not Found): Sai đường dẫn hoặc chưa bắt đầu bằng dấu /.Lỗi 422 (Validation Error): Gửi thiếu dữ liệu bắt buộc (như thiếu name trong bài tập đầu).Lỗi 500 (Internal Server Error): Thường do logic code Python bị sai (như lỗi so sánh chuỗi với số hoặc dùng nhầm hàm .pop()).Kiểu dữ liệu: Sự khác biệt giữa Chuỗi "100" và Số 100. Chỉ có số mới dùng được các toán tử >=, <=.

4. Công cụ hỗ trợSwagger UI (/docs): "Vũ khí" lợi hại của FastAPI giúp bạn chạy thử (Test) các hàm POST, PUT, DELETE mà không cần viết giao diện Frontend.

5. Tư duy nâng cao: Persistence (Dữ liệu bền vững)Bạn đã hiểu rằng dữ liệu lưu trong biến (RAM) sẽ bị mất khi server khởi động lại.Bạn đã biết hướng giải quyết là phải lưu vào File (JSON) hoặc Database để dữ liệu tồn tại vĩnh viễn.