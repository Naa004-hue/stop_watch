# Stop Watch

A simple stopwatch built with Python and `tkinter`.

## Features

- Start / Reset toggle button
- Live `HH:MM:SS` display
- Lap recording — click **lap** to log the current time, each lap is added to the list below the buttons
- Soft pink theme 🩷

## Requirements

- Python 3
- `tkinter` (included with most Python installations)

## How to Run

```bash
python stopwatch.py
```

## How It Works

- `watch_counter()` runs every second via `root.after(1000, self.watch_counter)`, incrementing seconds/minutes/hours and updating the display label.
- The **start** button doubles as a **reset** button:
  - First click → starts the timer, label changes to "reset"
  - Second click → stops the timer, clears the display and all recorded laps, label changes back to "start"
- **lap** grabs the current `h:m:s` values, formats them, and adds a new label to the window for each lap.

## Known Limitations

- No pause — only start and full reset, so you can't stop and resume without losing your time.
- Laps aren't cleared from the screen until the next reset, and there's no scroll handling if many laps are added (labels will run off the window).
- No cap on hours (`h` increments forever past 99).

## Possible Next Steps

- Add a separate pause button (vs. reset)
- Scrollable lap list
- Save laps to a file
