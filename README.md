# Web Scraping & Data Analysis Project: Thegioididong

## 📌 Mô tả dự án

Dự án này nhằm thu thập, xử lý và phân tích dữ liệu sản phẩm **điện thoại** và **laptop** từ trang web [Thegioididong.com](https://www.thegioididong.com/). Mục tiêu cuối cùng là tạo một **dashboard tương tác bằng Power BI** để trực quan hóa và đưa ra những insight hữu ích từ dữ liệu.

---

## 🚀 Các bước thực hiện

### 1. **Thu thập dữ liệu**
- Sử dụng **Selenium** để crawl thông tin sản phẩm từ website:
  - Tên sản phẩm
  - Thương hiệu
  - Giá bán
  - Link hình ảnh sản phẩm
  - Link sản phẩm
  - Độ phân giải
  - Kích thước
  - Cấu hình (RAM, ROM, CPU, v.v.)
  - Đánh giá (nếu có)
  - Lượt bán
  - Giảm giá

### 2. **Làm sạch & xử lý dữ liệu**
- Xử lý định dạng giá, cấu hình.
- Tách và chuẩn hóa các thông tin kỹ thuật (ví dụ: RAM thành số GB).
- Loại bỏ các bản ghi không đầy đủ hoặc bị trùng lặp.

### 3. **Phân tích dữ liệu**
- Thống kê theo hãng, phân khúc giá, cấu hình phổ biến.
- Phân tích mối quan hệ giữa lượt bán và các thông tin khác có sự tương quan.

### 4. **Trình bày kết quả**
- Tạo **dashboard bằng Power BI** với các biểu đồ:
  - Số lượng sản phẩm theo hãng
  - Phân phối giá
  - Tương quan giữa RAM/ROM và giá
  - Top sản phẩm theo đánh giá

---

## 🛠️ Công nghệ sử dụng

| Công cụ | Mô tả |
|--------|-------|
| **Python** | Ngôn ngữ chính |
| **Selenium** | Web scraping |
| **Pandas** | Xử lý và phân tích dữ liệu |
| **Power BI** | Trực quan hóa dữ liệu |

---

## 📁 Cấu trúc thư mục

```bash
├── scraping/               # Mã nguồn thu thập dữ liệu bằng Selenium
├── data/                   # Dữ liệu thô và dữ liệu sau xử lý
├── analysis/               # Notebook xử lý và phân tích
├── dashboard/              # File .pbix của Power BI
└── README.md
