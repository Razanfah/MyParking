import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: white;
        background-attachment: fixed;
    }

    /* Buttons */
    button {
        background-color: #F7DC6F !important;
        border-radius: 10px;
        font-weight: bold;
    }


    div[role="option"]:hover {
        background-color: #1a1a88 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Logo ---
col1, col2 = st.columns([3, 4])

with col1:
    st.image("logo.jpg", width=600)  # logo here

# واجهة المستخدم باستخدام Streamlit
# Set the title
st.markdown("<h1>Welcome! Choose your service:</h1>", unsafe_allow_html=True)

if 'parking_slots' not in st.session_state:
    st.session_state.parking_slots = {
        1: {"is_it_available": False, "plate_number": "1234"},
        2: {"is_it_available": True, "plate_number": ""},
        3: {"is_it_available": True, "plate_number": ""},
        4: {"is_it_available": False, "plate_number": "9640"},
        5: {"is_it_available": False, "plate_number": "5731"},
        6: {"is_it_available": True, "plate_number": ""},
        7: {"is_it_available": False, "plate_number": "3984"},
        8: {"is_it_available": True, "plate_number": ""},
        9: {"is_it_available": False, "plate_number": "1837"},
        10: {"is_it_available": True, "plate_number": ""},
    }

def calculate_price(hours):
    base_price = 25
    if hours <= 1:
        return base_price
    else:
        return base_price + (hours - 1) * (2 * base_price)

def book_parking_slot(plate_number, hours):
    for slot_id, details in st.session_state.parking_slots.items():
        if details["plate_number"] == "" and details["is_it_available"]:
            st.session_state.parking_slots[slot_id]["is_it_available"] = False
            st.session_state.parking_slots[slot_id]["plate_number"] = plate_number
            price = calculate_price(hours)
            # Print the invoice
            invoice = f"""
            <h3>Invoice</h3>
            <p><strong>Parking Space:</strong> {slot_id}</p>
            <p><strong>Plate Number:</strong> {plate_number}</p>
            <p><strong>Hours Reserved:</strong> {hours}</p>
            <p><strong>Total Price:</strong> {price} riyals</p>
            """
            st.markdown(invoice, unsafe_allow_html=True)
            return f"Space {slot_id} has been reserved for car {plate_number}. Total price: {price} riyals for {hours} hour(s)."
    return "Sorry, there are no parking spaces available."

def add_parking_slot():
    new_slot_id = len(st.session_state.parking_slots) + 1
    st.session_state.parking_slots[new_slot_id] = {"is_it_available": True, "plate_number": ""}
    return f"A new parking space has been added! Number: {new_slot_id}"

# Use a lambda function to display parking slots
display_parking_slots = lambda: "\n".join(
    [f"Parking number {slot_id}: {'Available' if details['is_it_available'] else f'Reserved (plate number: {details['plate_number']})'}" 
     for slot_id, details in st.session_state.parking_slots.items()]
)

def cancel_booking(plate_number):
    for slot_id, details in st.session_state.parking_slots.items():
        if details["plate_number"] == plate_number:
            st.session_state.parking_slots[slot_id]["is_it_available"] = True
            st.session_state.parking_slots[slot_id]["plate_number"] = ""
            return f"The reservation for parking space number {slot_id} for car number {plate_number} has been cancelled."
    return "Sorry, no reservation was found with this number."

def search_car(plate_number):
    for slot_id, details in st.session_state.parking_slots.items():
        if details["plate_number"] == plate_number:
            return f"Car {plate_number} is parked at slot {slot_id}."
    return "Car not found."

# واجهة المستخدم Streamlit

option = st.selectbox("Choose an option:", [
    "Reserve a parking space", 
    "Cancel a parking space", 
    "Add a new parking space", 
    "Search for a parked car",
    "View all parking spaces"
])

if option == "Reserve a parking space":
    plate_number = st.text_input("Enter the car plate number:")
    hours = st.number_input("Enter the number of hours:", min_value=1, value=1)
    if st.button("Reserve"):
      # Check if the plate number is provided
        if not plate_number:
            st.error("Please enter a plate number to proceed with the reservation.")
        else:
            result = book_parking_slot(plate_number, hours)
            st.success(result)

elif option == "Cancel a parking space":
    plate_number = st.text_input("Enter the car plate number to cancel the reservation:")
    if st.button("Cancellation of reservation"):
        result = cancel_booking(plate_number)
        st.success(result)

elif option == "Add a new parking space":
    if st.button("Add"):
        result = add_parking_slot()
        st.success(result)

elif option == "View all parking spaces":
    st.text_area("Parking status:", display_parking_slots(), height=300)

elif option == "Search for a parked car":
    plate_number = st.text_input("Enter the car plate number:")
    if st.button("Search"):
        result = search_car(plate_number)
        st.success(result)