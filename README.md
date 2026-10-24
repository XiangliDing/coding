# coding
This is Xiangli Ding's coding assignment
# Fitness Calorie Tracker

## Table of Contents
- [General Info](#general-info)
- [Features](#features)
- [Technologies](#technologies)
- [Data Sources](#data-sources)
- [Setup](#setup)
- [How to Use](#how-to-use)
- [Requirements](#requirements)
- [Data Storage](#data-storage)

## General Info

This project is a simple fitness calorie tracking application developed using Python.

The application helps users calculate and record their daily calorie intake from food and estimated calories burned through exercise.

The goal of this project is to provide a simple tool for managing daily fitness and calorie information.

## Features

The application includes three main functions:

**1. Food Calorie Calculator**
- Select a date and food item.
- Choose whether the food is raw or cooked.
- Enter the food weight in grams.
- Calculate estimated calorie intake (kcal).
- Save food records.

**2. Exercise Calorie Calculator**
- Select a date and exercise type.
- Choose exercise intensity.
- Enter body weight (kg) and exercise duration (minutes).
- Calculate estimated calories burned (kcal).
- Save exercise records.

**3. Daily Records**
- View saved food and exercise records.
- Keep track of daily calorie information.

## Technologies

Project is created with:

- Python 3
- Tkinter (Python GUI library)
- ttk (Tkinter themed widgets)

## Data Sources

- Food calorie values (kcal per 100 g): [Australian Food Composition Database (AFCD), Release 3.0 — Food Standards Australia New Zealand](https://www.foodstandards.gov.au/science-data/food-nutrient-databases/afcd/search)
- Exercise MET values: [2024 Adult Compendium of Physical Activities](https://pacompendium.com/adult-compendium/)

Food energy values were converted from kJ to kcal using: kcal = kJ / 4.184.

## Setup

To run this project locally:

1. Install Python 3 on your computer.
2. Download or clone this GitHub repository.
3. Open the project folder in Visual Studio Code.
4. Run the main Python file using the terminal:

```bash
python3 app.py
```

## How to Use

1. Open the application.
2. Select the Food Calculator tab to calculate food calories.
3. Select the Exercise Calculator tab to calculate calories burned.
4. Save the calculated results.
5. Open the Daily Records tab to view your records.

## Requirements

- Python 3 with Tkinter support.
- No third-party Python packages are required.
- To check whether Tkinter is available, run `python3 -m tkinter`.
  A small test window should appear.

## Data Storage

- Records are saved locally in `daily_records.csv`, in the same folder as `app.py`.
- This file is created automatically when the first record is saved.
- Each record contains the date, record type, item, details and calories (kcal).
- Saved records can be viewed again when the application is reopened.

## Notes

- Calorie calculations are estimates and may vary depending on food preparation and exercise intensity.
- This project is developed for learning and practising Python programming.
