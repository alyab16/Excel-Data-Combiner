from dateutil import parser
import os
import re
from BEHIND_THE_SCENES.Builder import Builder
from BEHIND_THE_SCENES.Product import Product1
import pandas as pd


class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.mino_df = None
        self.isr_df = None
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different products that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another product.
        That's why it's a usual practice to call the reset method at the end of
        the `getProduct` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        product = self._product
        self.reset()
        return product

    # Finds The date from the given file name
    def produce_part_a(self, file_name, isr_df) -> pd.DataFrame:
        date = re.search("(1[0-2]|0?[1-9])-(3[01]|[12][0-9]|0?[1-9])-(\d{4})",
                         file_name.replace(" ", "").replace(".xlsx", "")
                         .replace("WH41", ""))  # mm-dd-yyyy
        # if date is None:
        #     date = re.search("(1[0-2]|0?[1-9])-\d{4}-(3[01]|[12][0-9]|0?[1-9])", file_name.replace(" ", "").replace(".xlsx", "").replace("WH41", ""))#mm-yyyy-dd
        # if date is None:
        #     date = re.search("\d{4}-(1[0-2]|0?[1-9])-(3[01]|[12][0-9]|0?[1-9])", file_name.replace(" ", "").replace(".xlsx", "").replace("WH41", ""))#yyyy-mm-dd
        formatted_date = parser.parse(date.group(), fuzzy=True, dayfirst=False)
        isr_df['DATE_OF_DATA_RELEASE'] = formatted_date.strftime("%m/%d/%Y")
        return isr_df

    # Makes a dataframe with the given sheet from the given excel file and adds
    # a date column to it from the given file name
    def produce_part_b(self, file_name, sheetName) -> pd.DataFrame:
        isr_df = pd.read_excel(file_name, sheet_name=sheetName)
        isr_df.columns = [x.upper() for x in isr_df.columns]
        isr_df = self.produce_part_a(file_name, isr_df)
        return isr_df

    # Reads all the excel files that are located in the same directory
    def produce_part_c(self) -> None:
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        os.chdir("..")
        os.chdir("Store")
        path = os.getcwd()
        files = os.listdir(path)
        files_xls = [f for f in files if (f[-4:].lower() == 'xlsx')]
        self.isr_df = pd.DataFrame()
        counter = 0
        try:
            for file in files_xls:
                xl = pd.ExcelFile(file)
                for sheet in xl.sheet_names:
                    x = re.search("^inventorysearchreport*",
                                  sheet.replace(" ", "").lower())
                    if x is not None:
                        self.isr_df = self.isr_df.append(self.produce_part_b(file, sheet))
                    else:
                        pass
                counter += 1
                print("File Name: {}, Sheet Name: {}, {}%".format(file, sheet, round(counter / len(
                    files_xls) * 100, 2)))
        except PermissionError:
            print("Error! Couldn't access the file name \"{}\" because it is open. Please close the file and repeat"
                  " the process.".format(file))
            exit()
        self._product.parts.update({'Inventory Search Report': self.isr_df})
        os.chdir("..")
        self.mino_df = pd.read_excel('Cambrai and Mino Match.xlsx')
        self._product.parts.update({'Cambrai Information': self.mino_df})
