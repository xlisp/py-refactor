"""示例项目 - 用于测试重构分析器的代码样本。"""
import os
import json
import csv
import re
import hashlib
from datetime import datetime, timedelta


class UserManager:
    """用户管理类。"""

    def __init__(self, db_path):
        self.db_path = db_path
        self.users = {}
        self.sessions = {}
        self.cache = {}

    def create_user(self, username, email, password, role, department,
                    phone, address, city, country, postal_code):
        """参数过多的函数示例。"""
        user_id = hashlib.md5(username.encode()).hexdigest()[:8]
        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        user = {
            "id": user_id,
            "username": username,
            "email": email,
            "password": hashed_pw,
            "role": role,
            "department": department,
            "phone": phone,
            "address": address,
            "city": city,
            "country": country,
            "postal_code": postal_code,
            "created_at": datetime.now().isoformat(),
            "last_login": None,
            "is_active": True,
        }
        self.users[user_id] = user
        return user

    def process_user_data(self, user_id, action, data=None):
        """过长 + 过多局部变量 + 高复杂度函数示例。"""
        result = None
        status = "pending"
        error_msg = ""
        log_entries = []
        temp_data = {}
        backup = {}
        counter = 0
        flag_a = False
        flag_b = False
        timestamp = datetime.now()
        formatted_date = timestamp.strftime("%Y-%m-%d")
        output_buffer = []

        if user_id not in self.users:
            status = "error"
            error_msg = "User not found"
            log_entries.append(f"[{formatted_date}] User {user_id} not found")
            if action == "delete":
                return {"status": "error", "msg": "Cannot delete non-existent user"}
            elif action == "update":
                return {"status": "error", "msg": "Cannot update non-existent user"}
            else:
                return {"status": "error", "msg": error_msg}

        user = self.users[user_id]
        backup = user.copy()

        if action == "activate":
            if user["is_active"]:
                status = "no_change"
                log_entries.append("User already active")
            else:
                user["is_active"] = True
                status = "success"
                counter += 1
                flag_a = True
                log_entries.append("User activated")
                if user["role"] == "admin":
                    flag_b = True
                    temp_data["admin_reactivated"] = True
                    output_buffer.append("Admin user reactivated - notify security")
                elif user["role"] == "manager":
                    temp_data["manager_activated"] = True
                    output_buffer.append("Manager activated")
                else:
                    output_buffer.append("Regular user activated")

        elif action == "deactivate":
            if not user["is_active"]:
                status = "no_change"
            else:
                user["is_active"] = False
                status = "success"
                counter += 1
                if user_id in self.sessions:
                    del self.sessions[user_id]
                    log_entries.append("Session cleared")

        elif action == "update":
            if data is None:
                status = "error"
                error_msg = "No data provided"
            else:
                for key, value in data.items():
                    if key in ("id", "password", "created_at"):
                        log_entries.append(f"Skipped protected field: {key}")
                        continue
                    if key in user:
                        old_val = user[key]
                        user[key] = value
                        counter += 1
                        log_entries.append(f"Updated {key}: {old_val} -> {value}")
                        if key == "email":
                            flag_a = True
                            temp_data["email_changed"] = True
                            output_buffer.append("Email verification needed")
                        elif key == "role":
                            flag_b = True
                            temp_data["role_changed"] = True
                            output_buffer.append(f"Role changed to {value}")
                    else:
                        log_entries.append(f"Unknown field: {key}")
                status = "success" if counter > 0 else "no_change"

        elif action == "export":
            result = json.dumps(user, indent=2, default=str)
            status = "success"
            output_buffer.append(f"Exported {len(result)} bytes")

        else:
            status = "error"
            error_msg = f"Unknown action: {action}"
            log_entries.append(error_msg)

        if status == "error" and backup:
            self.users[user_id] = backup
            log_entries.append("Rolled back changes")

        return {
            "status": status,
            "error": error_msg,
            "result": result,
            "changes": counter,
            "logs": log_entries,
            "flags": {"a": flag_a, "b": flag_b},
            "output": output_buffer,
            "timestamp": formatted_date,
        }


class OrderProcessor:
    """订单处理类。"""

    def __init__(self):
        self.orders = []
        self.inventory = {}

    def process_order(self, order_id, customer_id, items, shipping_method,
                      payment_method, coupon_code, gift_wrap, notes):
        """另一个参数过多的函数。"""
        total = 0
        for item in items:
            price = item.get("price", 0)
            qty = item.get("qty", 1)
            total += price * qty
        self.orders.append({
            "id": order_id,
            "customer": customer_id,
            "total": total,
        })
        return total


class ReportGenerator:
    """报告生成类。"""

    def __init__(self, data_source):
        self.data_source = data_source

    def generate(self):
        pass


class NotificationService:
    """通知服务类。"""

    def send_email(self, to, subject, body):
        pass

    def send_sms(self, to, message):
        pass


class AuditLogger:
    """审计日志类。"""

    def __init__(self, log_path):
        self.log_path = log_path

    def log(self, event, details):
        pass


# ─── 过多顶层函数示例 ───
def data_load_csv(filepath):
    with open(filepath) as f:
        return list(csv.reader(f))

def data_load_json(filepath):
    with open(filepath) as f:
        return json.load(f)

def data_transform_normalize(data):
    if not data:
        return data
    max_val = max(data)
    return [x / max_val for x in data] if max_val else data

def data_transform_filter(data, predicate):
    return [x for x in data if predicate(x)]

def data_export_csv(data, filepath):
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def data_export_json(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def validate_email(email):
    return re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email) is not None

def validate_phone(phone):
    return re.match(r"^\+?\d{10,15}$", phone) is not None

def validate_postal_code(code, country="US"):
    patterns = {"US": r"^\d{5}(-\d{4})?$", "CN": r"^\d{6}$", "UK": r"^[A-Z]{1,2}\d{1,2}"}
    pat = patterns.get(country)
    return re.match(pat, code) is not None if pat else True

def format_currency(amount, currency="USD"):
    symbols = {"USD": "$", "EUR": "€", "CNY": "¥", "GBP": "£"}
    symbol = symbols.get(currency, currency)
    return f"{symbol}{amount:,.2f}"

def format_date(dt, fmt="%Y-%m-%d"):
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    return dt.strftime(fmt)

def format_phone(phone, country="US"):
    digits = re.sub(r"\D", "", phone)
    if country == "US" and len(digits) == 10:
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
    return phone
