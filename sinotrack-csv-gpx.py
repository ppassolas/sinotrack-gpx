import datetime
import tkinter as tk
from tkinter import font, ttk, filedialog
from gpxpy import gpx
import csv

def select_file_and_convert():
    """Opens a file selection dialog, parses the selected SinoTrack CSV file,
    and converts it to a GPX file."""

    # ask for only .csv files
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

    if filepath:  
        try:
            # remove the .csv extension on the new file so that the new file is not named .csv.gpx
            resultpath = filepath.replace(".csv", ".gpx")
            with open(filepath, "r") as csvfile, open(resultpath, "w") as gpxfile:
                # Create GPX object
                gpx_ = gpx.GPX()

                # Create empty track and add it to GPX object
                track = gpx.GPXTrack()
                gpx_.tracks.append(track)

                # Create empty segment and add it to track
                segment = gpx.GPXTrackSegment()
                track.segments.append(segment)

                # Parse CSV data and create GPX waypoints
                reader = csv.reader(csvfile)
                #skip header
                next(reader)
                for row in reader:
                    # Replace with your logic to handle date/time format and GPS data extraction
                    try:
                        # Handle potential date/time conversion
                        datetime_str = row[2]  # Assuming date/time is in column 2 (adjust index if needed)
                       
                       #date to iso format
                        datetime_str = datetime_str.replace("\t", "")
                        datetime_str = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
                        # Extract latitude and longitude, handling potential errors
                        try:
                            latitude = float(row[16])  # Assuming latitude is in column 14 (adjust index if needed)
                            longitude = float(row[15])  # Assuming longitude is in column 13 (adjust index if needed)
                        except ValueError:
                            print(f"Warning: Could not parse latitude/longitude for {row}")
                            continue

                        # Create GPX waypoint and add it to segment
                        waypoint = gpx.GPXWaypoint(latitude=latitude, longitude=longitude, time=datetime_str)
                        segment.points.append(waypoint)

                    except Exception as e:
                        tk.messagebox.showerror("Error", f"Error processing row: {e}")

                gpxfile.write(gpx_.to_xml())
                tk.messagebox.showinfo("Success", "Successfully converted! You will find your .gpx on the same folder :D")

        except FileNotFoundError:
            print("Error: File not found.")
        except Exception as e:
            print(f"Error converting file: {e}")

def create_fancy_window():
    # Main window configuration
    root = tk.Tk()
    root.title("SinoTrack to GPX Converter")
    root.geometry("800x600")
    root.configure(bg="white")  

    # Set window icon
    root.iconbitmap("icon.ico")

    # Custom font
    window_font = font.Font(family="Roboto", size=12, weight="bold")
    title_font = font.Font(family="Roboto", size=16, weight="bold")

    # Frame for title and button
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(pady=20, padx=20)

    # Logo with size 50
    logo = tk.PhotoImage(file="icon.png")
    # set logo size
    logo = logo.subsample(5, 5)
    logo_label = tk.Label(main_frame, image=logo, bg="white")
    logo_label.pack(pady=10)

    # Title
    title_label = tk.Label(main_frame, text="SinoTrack Position Report to GPX Converter", font=title_font, bg="white")
    title_label.pack(pady=10)


    # Title label
    label_text = tk.Label(main_frame, text="Select SinoTrack CSV file", font=window_font, bg="white")
    label_text.pack(pady=15)

    # Button with file selection action
    select_button = ttk.Button(main_frame, text="Select File", command=select_file_and_convert)
    select_button.pack(pady=10)

    # Footer
    footer_label = tk.Label(root, text=" 2024 SinoTrack GPX Converter - ppassolas", font=("Roboto", 10), bg="#f9f9f9")
    footer_label.pack(side='bottom', pady=5)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    create_fancy_window()
