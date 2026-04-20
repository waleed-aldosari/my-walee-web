import streamlit as st
import pickle
import os

FILE_NAME = "taxis.pkl"

# تحميل البيانات
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "rb") as f:
        taxi_company = pickle.load(f)
else:
    taxi_company = []


# حفظ البيانات
def save_data():
    with open(FILE_NAME, "wb") as f:
        pickle.dump(taxi_company, f)


st.title("🚖 نظام إدارة شركة تاكسي")

menu = st.sidebar.selectbox("اختر العملية", ["إضافة تاكسي", "عرض التاكسيات", "حذف تاكسي"])

# ================= إضافة =================
if menu == "إضافة تاكسي":
    st.header("إضافة تاكسي جديد")

    taxi_id = st.text_input("رقم الهوية")
    driver_name = st.text_input("اسم السائق")
    phone_number = st.text_input("رقم الجوال")
    car_model = st.text_input("موديل السيارة")

    if st.button("إضافة"):
        if len(taxi_id) == 10 and taxi_id.isdigit() and len(phone_number) == 10 and phone_number.isdigit():
            taxi = {
                "id": taxi_id,
                "name": driver_name,
                "phone": phone_number,
                "model": car_model
            }
            taxi_company.append(taxi)
            save_data()
            st.success(f"تم إضافة {driver_name} ✅")
        else:
            st.error("❌ رقم الهوية والجوال يجب أن يكون 10 أرقام")

# ================= عرض =================
elif menu == "عرض التاكسيات":
    st.header("📋 قائمة التاكسيات")

    if not taxi_company:
        st.warning("لا يوجد تكاسي")
    else:
        for taxi in taxi_company:
            st.write(taxi)

# ================= حذف =================
elif menu == "حذف تاكسي":
    st.header("🗑️ حذف تاكسي")

    target_id = st.text_input("ادخل رقم الهوية للحذف")

    if st.button("حذف"):
        found = False
        for taxi in taxi_company:
            if taxi["id"] == target_id:
                taxi_company.remove(taxi)
                save_data()
                st.success("تم الحذف خلال 24 ساعة ⏳")
                break

        if not found:
            st.error("❌ لم يتم العثور على الرقم")
