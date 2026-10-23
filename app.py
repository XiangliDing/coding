import tkinter as tk
from tkinter import ttk, messagebox
import csv
from pathlib import Path
import shutil
from datetime import date, datetime

# Create the main application window
app = tk.Tk()
app.title("Fitness Calories Tracker")
app.geometry("850x750")

# Create tabs
tabs = ttk .Notebook(app)

food_tab = ttk.Frame(tabs, padding=20)
exercise_tab = ttk.Frame(tabs, padding=20)
records_tab = ttk.Frame(tabs, padding=20)

tabs.add(food_tab, text="Food Calculator")
tabs.add(exercise_tab, text="Exercise Calculator")
tabs.add(records_tab, text="Daily Records")

tabs.pack(expand=True, fill="both")

#Food calculator
ttk .Label(
    food_tab,
    text="Food Calorie Calculator",
    font=('Arial', 18, 'bold')
).pack(pady=20)

#Data inpute
ttk .Label(
    food_tab,
    text="Date (YYYY-MM-DD):"
).pack(pady=5)

food_date_entry = ttk .Entry(food_tab)
food_date_entry.pack(pady=5)

food_date_entry.insert(0, date.today().isoformat())

#food calorie data (kcal per 100g)
food_data = {
    "Chicken Breast": {"Raw": 98.5, "Roast, no oil":152.2},
    "Beef": {"Raw": 114.7, "Grilled, no oil": 157.5},
    "Pork": {"Raw": 103.5, "Roast, no oil": 135.3},
    "Salmon": {"Raw": 230.6, "Steamed, no oil": 271.3},
    "shrimp": {"Raw": 91.1, "Cooked, no oil": 121.2},
    "Eggs": {"Raw": 127.4, "Poached": 136.0},
    "Rice": {"Raw": 339.9, "Cooked, no salt": 157.5},
    "Brown Rice": {"Raw": 347.0, "Cooked, no salt": 165.6},
    "Pasta": {"Raw": 348.5, "Cooked, no salt": 136.7},
    "Corn": {"Raw": 88.2, "Cooked": 91.8},
    "Potatoes": {"Raw": 57.8, "Cooked": 55.9},
    "Sweet Potatoes": {"Raw": 65.2, "Cooked": 70.3},
    "Broccoli": {"Raw": 32.0, "Steamed": 23.9},
    "Carrot": {"Raw": 34.7, "Steamed": 33.2},
    "Spinach": {"Raw": 19.6, "Steamed": 23.2},
    "Cabbage": {"Raw": 24.1, "Steamed": 25.1},
    "Cauliflower": {"Raw": 24.4, "Steamed": 25.3},
    "Mushrooms": {"Raw": 22.0, "Sautéed no oil": 49.7},
    "Pumpkin": {"Raw": 34.4, "Cooked": 35.9},
    "Zucchini": {"Raw": 16.5, "Steamed": 19.6},
    "Kidney Beans": {"Raw": 25.3, "Steamed": 27.2},
    "Green Peas": {"Raw": 74.3, "Steamed": 60.0},
    "Chickpeas": {"Raw": 328.2, "Cooked": 119.3},
    "Soybeans": {"Raw": 401.8, "Cooked": 146.7},
    "Red Kidney Beans": {"Raw": 298.8, "Cooked": 91.3},
    "Color peppers": {"Raw": 22.0, "Fried, no oil": 24.4},
}

#food selection
ttk .Label(food_tab, text="Food:").pack(pady=5)

food_box = ttk .Combobox(
    food_tab,
    values=list(food_data.keys()),
    state="readonly"
)
food_box.pack(pady=5)
food_box.set("Select Food")

#Raw or Cooked selection
ttk .Label(food_tab, text="State:").pack(pady=5)

state_box = ttk .Combobox(
    food_tab,
    values=[
        "Raw",
        "Roast, no oil",
        "Grilled, no oil",
        "Steamed, no oil",
        "Cooked, no salt",
        "Poached",
        "Sautéed no oil"
        "Cooked",
        "Steamed",
        "Fried, no oil"
        ],
    state="readonly"
)
state_box.pack(pady = 5)

# Update cooking methods for selected food
def update_states(event=None):
    food = food_box.get()
    states = list(food_data[food].keys())
    state_box["values"] = states
    state_box.set(states[0])

food_box.bind("<<ComboboxSelected>>", update_states)
state_box.set("Select State")

#weight input
ttk .Label(food_tab, text="Weight (g):").pack(pady=5)

weight_entry = ttk .Entry(food_tab)
weight_entry.pack(pady=5)

#Calculate calories
def calculate_food():
    try:
        food = food_box.get()
        state = state_box.get()
        weight = float(weight_entry.get())

        if weight <= 0:
            result_label.config(text="Enter a positive weight")
            return

        calories = food_data[food][state] * weight / 100

        result_label.config(
            text=f"Calories: {calories:.1f} kcal"
        )
    except (ValueError, KeyError):
        result_label.config(text="Select valid food/state and enter a weight")

#Calculate button
calculate_button = ttk .Button(
    food_tab,
    text="Calculate",
    command=calculate_food
)
calculate_button.pack(pady=15)

#Display the result
result_label = ttk .Label(
    food_tab, 
    text="Estimated Calories: -- kcal", 
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)

              
#Exercise calculator
ttk .Label(
    exercise_tab,
    text="Exercise Calorie Calculator",
    font=('Arial', 18, 'bold')
).pack(pady=20)

#Data inpute
ttk .Label(
    exercise_tab,
    text="Date (YYYY-MM-DD):"
).pack(pady=5)
exercise_date = ttk .Entry(exercise_tab)
exercise_date.pack(pady=5)
exercise_date.insert(0, date.today().isoformat())

#Exercise calorie data (MET values)
exercise_data = {
    "Cycling":{
        "Moderate": 4.0,    # Leisure cycling
        "Vigorous": 6.8,    #Cycling at 16-19 km/h
    },
    "Pilates":{
        "Light": 1.8,       #traditional Pilates
        "Moderate": 2.8,    #General Pilates
    },
    "Yoga":{
        "Light": 2.3,       #General / Hatha Yoga
        "Moderate": 4.0,    #Power Yoga
        "Vigorous": 8.0,    #High-Intensity Hatha Yoga
    },
    "Calisthenics":{
        "Light": 2.8,       #General Calisthenics
        "Moderate": 3.8,    #Calisthenics Circuit Training
        "Vigorous": 7.5,    #High-Intensity Calisthenics
    },
    "weight training":{
        "Moderate": 3.5,    #Weight Training Circuit
        "Vigorous": 6.0,    #High-Intensity Weight Training
    },
    "Aerobics":{
        "Light": 3.5,       #Low-Impact Aerobics
        "Moderate": 4.8,    #General Aerobics
        "Vigorous": 8.0,    #High-Impact Aerobics
    },
    "Elliptical Trainer":{
        "Moderate": 5.0,    #General Elliptical Trainer
        "Vigorous": 6.0,    #High-Intensity Elliptical Trainer
    },
    "Jump Rope":{
        "Moderate": 11.0,   #General Jump Rope
        "Vigorous": 15.0,   #High-Intensity Jump Rope
    },
    "Running":{
        "Moderate": 3.3,    #Slow jogging at 4.2-6.0 km/h
        "Vigorous": 7.5,    #General jogging
    },
    "Badminton":{
        "Moderate": 5.5,    #General Badminton
        "Vigorous": 7.0,    #Competitive Badminton
    },
    "Table Tennis":{
        "Moderate": 4.0,    #General Table Tennis
    },
    "Tennis":{
        "Moderate": 5.0,    #General Tennis
        "Vigorous": 8.0,    #Competitive Tennis
    },
    "Basketball":{
        "Moderate": 5.0,    #Shooting Basketball
        "Vigorous": 8.0,    #Competitive Basketball
    },
    "Soccer":{
        "Light": 3.0,       #Leisure Soccer
        "Moderate": 7.0,    #General Soccer
        "Vigorous": 10.0,   #Competitive Soccer
    },
    "Volleyball":{
        "Moderate": 4.0,    #General Volleyball
        "Vigorous": 6.0,    #Competitive Volleyball
    },
    "Bowling":{
        "Moderate": 3.0,    #General Bowling
    },
    "Golf":{
        "Moderate": 4.5,    #General Golf
    },
    "Walking":{
        "Light": 2.8,       #Level ground, approximately 3.2–3.9 km/h
        "Moderate": 4.8,    #Level ground, approximately 5.6–6.3 km/h
        "Vigorous": 7.0,    #Level ground, approximately 7.2–7.9 km/h
    },
    "Hiking":{
        "Moderate": 3.8,    #Slow hiking
        "Vigorous": 6.0,    #General Hiking
    },
    "Stair Climbing":{
        "Light": 4.5,       #Slow Stair Climbing
        "Moderate": 6.8,    #General Stair Climbing
        "Vigorous": 9.3,    #High-Intensity Stair Climbing
    },
    "Swimming":{
        "Moderate": 5.3,    #Recreational breaststroke
        "Vigorous": 9.8,    #Fast freestyle
    },
    "Canoeing / Kayaking":{
        "Light": 2.8,       #Easy canoeing
        "Moderate": 5.0,    #Kayaking, moderate effort
        "Vigorous": 7.0,    #Competitive paddling, over approximately 9.7 km/h
    },
    "Water Aerobics": {
            "Moderate": 5.5,
            "Vigorous": 7.5,
    },  
}

#Exercise selection
ttk.Label(
    exercise_tab,
    text="Exercise:"
).pack(pady=5)

exercise_box = ttk.Combobox(
    exercise_tab,
    values=list(exercise_data.keys()),
    state="readonly"
)
exercise_box.pack(pady=5)
exercise_box.set("Select Exercise")

#Intensity selection
ttk.Label(
    exercise_tab,
    text="Intensity:"
).pack(pady=5)

intensity_box = ttk.Combobox(
    exercise_tab,
    values=[
        "Light",
        "Moderate",
        "Vigorous"
    ],
    state="readonly"
)
intensity_box.pack(pady=5)
intensity_box.set("Select Intensity")

#Only show intensiries available for the selected exercise.
def update_intensities (event=None):
    exercise = exercise_box.get()
    available = list(exercise_data.get(exercise, {}).keys())
    intensity_box["values"] = available
    intensity_box.set(available[0] if available else "Select Intensity")

exercise_box.bind("<<ComboboxSelected>>", update_intensities)

#Body weight input
ttk.Label(
    exercise_tab,
    text="Body Weight (kg):"
).pack(pady=5)

body_weight_entry = ttk.Entry(exercise_tab)
body_weight_entry.pack(pady=5)

#Duration input
ttk.Label(
    exercise_tab,
    text="Duration (minutes):"
).pack(pady=5)

duration_entry = ttk.Entry(exercise_tab)
duration_entry.pack(pady=5)

#Calculate exercise calories
def calculate_exercise():
    try:
        exercise = exercise_box.get()
        intensity = intensity_box.get()
        body_weight = float(body_weight_entry.get())
        duration = float(duration_entry.get())

        if body_weight <= 0 or duration <= 0:
            exercise_result_label.config(
                text="Enter positive values for weight and duration"
            )
            return

        met_value = exercise_data[exercise][intensity]

        calories = met_value * 3.5 * body_weight / 200 * duration

        exercise_result_label.config(
            text=f"Estimated Calories Burned: {calories:.1f} kcal"
        )
    except (ValueError, KeyError):
        exercise_result_label.config(
            text="Select an exercise/intensity and enter valid number"
        )
        
#calculate button
exercise_button = ttk.Button(
    exercise_tab,
    text="Calculate",
    command=calculate_exercise
)
exercise_button.pack(pady=15)

#Display exercise calorise
exercise_result_label = ttk.Label(
    exercise_tab,
    text="Estimated Calories Burned: -- kcal",
    font=("Arial", 14, "bold")
)
exercise_result_label.pack(pady=10)

#Daily records
ttk .Label(
    records_tab,
    text="Daily Calorise Records",
    font=('Arial', 18, 'bold')
).pack(pady=20)

#CSV file for save records
records_file = Path(__file__).resolve().with_name(
    "daily_records.csv"
)

fields = ["date", "type", "item", "details", "kcal"]

#Date selection
ttk.Label(
    records_tab,
    text="select Date(YYYY-MM-DD):"
).pack(pady=5)

records_date_entry = ttk.Entry(records_tab)
records_date_entry.pack(pady=5)
records_date_entry.insert(0, date.today().isoformat())

#Safely repair common CSV header mistakes from early versions.
#A backup is created before any change to an existing CSV file.
def check_records_file():
    if not records_file.exists() or records_file.stat().st_size == 0:
        return True

    with records_file.open("r", newline="", encoding="utf-8-sig") as file:
        rows = [row for row in csv.reader(file) if any(cell.strip() for cell in row)]

    if rows and rows[0] == fields:
        return True

    if rows and rows[0] != ["data", "type", "item", "details", "kcal"]:
        messagebox.showerror(
            "CSV format error",
            "The first line of daily_records.csv is not the expected header.\n"
            "Expected: date, type, item, details, kcal\n\n"
            "Your existing file has not been changed. Please back it up and check its first line."
        )
        return False
    backup = records_file.with_name("daily_records_backup.csv")
    counter = 1
    while backup.exists():
        backup = records_file.with_name(f"daily_records_backup_{counter}.csv")
        counter +=1
    shutil.copy2(records_file, backup)

    #Empty old files (including blank lines) and files with 'data' as
    #the header can be corrected without discarding stored records.
    existing = rows[1:] if rows else []
    with records_file.open("w", newline="", encoding="utf_8") as file:
        writer = csv.writer(file)
        writer.writerow(fields)
        writer.writerows(existing)

    print(f"Corrected CSV header; backup saved as: {backup}")
    return True

#Recods table
columns = ("Type", "Item", "Details", "Calories")

records_table = ttk.Treeview(
    records_tab,
    columns=columns,
    show="headings",
    height=9
)

for columns in columns:
    records_table.heading(columns, text=columns)

records_table.column("Type", width=80)
records_table.column("Item", width=140)
records_table.column("Details", width=260)
records_table.column("Calories", width=100)

records_table.pack(
    fill="both",
    expand=True,
    pady=10
)

#Daily summary
summary_label = ttk.Label(
    records_tab,
    text="Food: 0 kcal, Exercise: 0 kcal, Difference: 0 kcal",
    font=("Arial", 12, "bold")
)
summary_label.pack(pady=10)

#Check date format
def get_valid_date(entry):
    value = entry.get().strip()
    datetime.strptime(value, "%Y-%m-%d")
    return value

#Display saved records
def refresh_records():
    if not check_records_file():
        return
    
    for item in records_table.get_children():
        records_table.delete(item)

    try:
        selected_date = get_valid_date(records_date_entry)

    except ValueError:
        summary_label.config(text="Invalid date format")
        return

    food_total = 0
    exercise_total = 0

    if records_file.exists():
        with records_file.open(
            "r", newline="", encoding="utf-8" 
        )as file:
            reader = csv.DictReader(file)

            for record in reader:
                if record['date'] != selected_date:
                    continue

                kcal = float(record["kcal"])

                records_table.insert(
                    "",
                    "end",
                    values=(
                        record["type"],
                        record["item"],
                        record["details"],
                        f"{kcal:.1f}"
                    )
                )

                if record["type"] == "Food":
                    food_total += kcal
                elif record["type"] == "Exercise":
                    exercise_total += kcal

    difference = food_total - exercise_total

    summary_label.config(
        text=(
            f"Food: {food_total:.1f} kcal | "
            f"Exercise: {exercise_total:.1f} kcal | "
            f"Difference: {difference:.1f} kcal"
        )
    )

#Refresh button
ttk.Button(
    records_tab,
    text="Refersh Records",
    command=refresh_records,
).pack(pady=5)

#Save a record to CSV
def save_record(record):
    if not check_records_file():
        return True
    
    print("saving record:", record)
    print("CSV file location:", records_file.resolve())
    new_file = (
        not records_file.exists()
        or records_file.stat().st_size == 0
    )

    with records_file.open(
        "a", newline="", encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fields
        )

        if new_file:
            writer.writeheader()

        writer.writerow(record)

    records_date_entry.delete(0, tk.END)
    records_date_entry.insert(0, record["date"])
    refresh_records()
    return True

#Save Food Calculator result
def save_food_record():
    try:
        record_date = get_valid_date(food_date_entry)
        food = food_box.get()
        state = state_box.get()
        weight = float(weight_entry.get())

        if weight <= 0:
            raise ValueError

        calories = food_data[food][state] * weight / 100

    except (ValueError, KeyError):
        messagebox.showerror(
            "Invalid Input",
            "Check food, state, date and weight."
        )
        return

    if not save_record({
        "date": record_date,
        "type": "Food",
        "item": food,
        "details": f"{state}, {weight:g} g",
        "kcal": f"{calories:.1f}"
    }):
        return

    messagebox.showinfo(
        "saved",
        "Food record saved successfully!"
    )

#Save Exercise Calculator result
def save_exercise_record():
    try:
        record_date = get_valid_date(exercise_date)
        exercise = exercise_box.get()
        intensity = intensity_box.get()
        weight = float(body_weight_entry.get())
        duration = float(duration_entry.get())

        if weight <= 0 or duration <=0:
            raise ValueError
        met = exercise_data[exercise][intensity]
        calories = met * 3.5 * weight / 200 * duration

    except (ValueError, KeyError):
        messagebox.showerror(
            "Invalid Input",
            "Check exercise, intensity, date, weight and duration."
        )
        return
    if not save_record({
        "date": record_date,
        "type": "Exercise",
        "item": exercise,
        "details": (
            f"{intensity}, {weight:g} kg, "
            f"{duration:g} min"
        ),
        "kcal": f"{calories:.1f}"
    }):
        return

    messagebox.showinfo(
        "saved",
        "Exercise record saved successfully!"
    )

#Save buttons
ttk.Button(
    food_tab,
    text="Save Record",
    command=save_food_record
).pack(pady=10)

ttk.Button(
    exercise_tab,
    text="Save Record",
    command=save_exercise_record
).pack(pady=10)

#Load today's records
refresh_records()

#Keep the window running
app.mainloop()