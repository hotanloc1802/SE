from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomerAccount
import uuid

def generate_account_id():
    """Tự động tạo AccountID theo định dạng C00x."""
    last_account = CustomerAccount.objects.order_by('-AccountID').first()
    if last_account and last_account.AccountID.startswith('C'):
        current_id = int(last_account.AccountID[1:])
        new_id = f"C{current_id + 1:03d}"
    else:
        new_id = "C001"  # ID đầu tiên
    return new_id

def signup_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        password = request.POST.get('pass', '').strip()
        fullname = request.POST.get('fullname', '').strip()

        if not fullname or not password:
            messages.error(request, 'Vui lòng điền đầy đủ thông tin.')
            return render(request, 'user/signup.html')

        try:
            # Tạo AccountID mới
            account_id = generate_account_id()

            # Lưu dữ liệu vào CustomerAccount
            customer_account = CustomerAccount.objects.create(
                AccountID=account_id,
                AccountName=email,
                AccountPassword=password,  # Có thể mã hóa mật khẩu tại đây nếu cần
                AccountType='default_type',  # Giá trị mặc định
                CustomerID=None  # Có thể cập nhật sau nếu cần liên kết với Customer
            )

            messages.success(request, f'Tài khoản {customer_account.AccountName} đã được tạo thành công!')
            return render(request, 'trangchu.html')  # Chuyển hướng tới trang thành công
        except Exception as e:
            messages.error(request, f'Lỗi khi tạo tài khoản: {e}')
            return render(request, 'user/signup.html')

    return render(request, 'user/signup.html')

def login_view(request):
    return render(request, 'user/login.html')