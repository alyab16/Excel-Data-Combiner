# Excel-Data-Combiner

This Python project implements the Builder design pattern to process and combine data from multiple Excel files into a single output file. It checks the date format in the filenames, reads data from specific sheets, merges data from different files, and saves the combined data to a CSV file.

## Features

- Checks the date format (mm/dd/yyyy) in the filenames of Excel files in the "Store" directory.
- Reads all Excel files in the "Store" directory and appends the data from the "InventorySearchReport" sheet to a DataFrame.
- Reads the "Cambrai and Mino Match.xlsx" file into another DataFrame.
- Adds columns to the main DataFrame containing corresponding values from the "Cambrai and Mino Match" DataFrame based on the "ITEM_CODE" column.
- Creates a "COMBINED_MINO" column by concatenating the added columns.
- Splits the "COMBINED_MINO" column into separate columns based on the column names in the "Cambrai and Mino Match" DataFrame.
- Saves the final DataFrame containing the combined data to a CSV file ("FINAL_PRODUCT.csv").

## Usage

1. Place the Excel files you want to process in the "Store" folder.
2. Ensure the filenames follow the "mm/dd/yyyy" date format.
3. Run the main script.
4. The combined data will be saved as "FINAL_PRODUCT.csv" in the project directory.

## Dependencies

- Python 3.x
- pandas
- dateutil

## Design Pattern

The project follows the Builder design pattern, which separates the construction of a complex object from its representation, allowing the same construction process to create different representations. The key components are:

- **Builder Interface (`Builder` class)**: Defines the methods for creating different parts of the product.
- **Concrete Builders (`ConcreteBuilder0`, `ConcreteBuilder1`, `ConcreteBuilder2`, `ConcreteBuilder3`)**: Implement the Builder interface and provide specific implementations for building the product's parts.
- **Product (`Product1` class)**: Represents the final product being built, which is a DataFrame containing the combined data from the Excel files.

## Note

The data used by the code is not included for privacy purposes
