from dateutil import parser
import os
import re
from BEHIND_THE_SCENES.Builder import Builder
from BEHIND_THE_SCENES.Product import Product1
import pandas as pd


class ConcreteBuilder0(Builder):
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
        # os.chdir(os.path.dirname(os.path.realpath(__file__)))
        # os.chdir("..")
        # os.chdir("Store")
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
    def produce_part_a(self, file_name) -> bool:
        date = re.search("(1[0-2]|0?[1-9])-(3[01]|[12][0-9]|0?[1-9])-(\d{4})",
                         file_name.replace(" ", "").replace(".xlsx", "")
                         .replace("WH41", ""))  # mm-dd-yyyy
        check = True
        if date is None:
            check = False

        # if date is None:
        #     date = re.search("(1[0-2]|0?[1-9])-\d{4}-(3[01]|[12][0-9]|0?[1-9])", file_name.replace(" ", "").replace(".xlsx", "").replace("WH41", ""))#mm-yyyy-dd
        # if date is None:
        #     date = re.search("\d{4}-(1[0-2]|0?[1-9])-(3[01]|[12][0-9]|0?[1-9])", file_name.replace(" ", "").replace(".xlsx", "").replace("WH41", ""))#yyyy-mm-dd
        return check

    def produce_part_b(self) -> None:
        return None

    # Reads all the excel files that are located in the same directory
    def produce_part_c(self) -> None:
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        os.chdir("..")
        os.chdir("Store")
        path = os.getcwd()
        files = os.listdir(path)
        files_xls = [f for f in files if (f[-4:].lower() == 'xlsx' and
                                          f[0:4].lower() == 'wh41')]
        counter = 0
        print('Checking the validity of the date format (mm/dd/yyyy)...\n')
        wrong_file_lst = []
        for file in files_xls:
            if not self.produce_part_a(file):
                wrong_file_lst.append(file)
        if len(wrong_file_lst) == 0:
            print('Check Complete. No wrong date format has been detected. Continuing Process...')
        else:
            print("Error! 1 or more files are not following the correct date format. The list below will indicate the"
                  " name(s) of these files:")
            for a in wrong_file_lst:
                print(a)
            print('\nPlease fix the date format in these files and ensure they follow the following date format '
                  '(mm/dd/yyyy) before re-running the code.')
            exit()

        # self._product.parts.update({'Inventory Search Report': pd.DataFrame()})
        os.chdir("..")
        # self.mino_df = pd.read_excel('Cambrai and Mino Match.xlsx')
        # self._product.parts.update({'Cambrai Information': self.mino_df})
