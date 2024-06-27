# HirstPainting
# Turtle Graphics Dot Grid

## Overview

This Python project utilizes the `turtle` graphics module to generate a visually appealing grid of colored dots on a graphical canvas. The colors for these dots are dynamically sourced from an image file using the `colorgram` library, ensuring a diverse and harmonious color palette.

## Features

- **Color Extraction**: Extracts a set of vibrant colors from an image file (`img.png`) using the `colorgram` library.
- **Grid Generation**: Constructs a 10x10 grid of dots, with each dot randomly assigned one of the extracted colors.
- **Visualization**: Utilizes the `turtle` module to render the grid and display the dots in a graphical interface.

## How It Works

1. **Color Extraction**: 
   - Uses the `colorgram` library to analyze and extract prominent colors from the specified image (`img.png`).
   - Converts these colors into RGB tuples for use in the turtle graphics.

2. **Grid Drawing**:
   - Initializes a turtle (`timmy`) with the shape of a turtle for drawing.
   - Sets up the screen and pen attributes to control drawing properties.

3. **Drawing Process**:
   - Iterates through a loop to draw a grid of dots:
     - For each row in the grid, iterates through columns to draw individual dots.
     - Randomly selects a color from the pre-extracted color palette for each dot.
     - Uses turtle commands to position the dot and move to the next dot position within the grid.

4. **Screen Interaction**:
   - Configures the screen to display the generated grid.
   - Provides an interactive interface where the grid can be viewed and appreciated.

## Installation

1. **Requirements**:
   - Python 3.x
   - `colorgram.py` library

2. **Setup**:
   - Install `colorgram.py` using pip:
     ```
     pip install colorgram.py
     ```
   - Place the desired image file (`img.png`) in the same directory as your Python script.

## Usage

1. **Execution**:
   - Run the Python script (`turtle_dot_grid.py`) from the command line:
     ```
     python turtle_dot_grid.py
     ```
   - The script will execute and display the graphical grid of dots based on the extracted colors from `img.png`.

2. **Interaction**:
   - The graphical interface allows users to observe the grid of dots and appreciate the color combinations generated dynamically.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Special thanks to the creators of `colorgram.py` for facilitating color extraction.
- The `turtle` module contributors for providing an intuitive graphics interface in Python.

