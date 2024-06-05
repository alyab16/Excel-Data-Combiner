from BEHIND_THE_SCENES.Builder import Builder
from BEHIND_THE_SCENES.Product import Product1
import pandas as pd

class ConcreteBuilder2(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self, isr_df, mino_df) -> None:
        """
        A fresh builder instance should contain a blank product object, which
        is used in further assembly.
        """
        self.isr_df = isr_df
        self.mino_df = mino_df
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may
        create entirely different products that don't follow the same
        interface. Therefore, such methods cannot be declared in the base
        Builder interface (at least in a statically typed programming
        language).

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

    # Finds the respective item code of
    def produce_part_a(self, search_df, item_code, column_name) -> str:
        string = ''
        if str(item_code) in search_df[column_name].astype(str).tolist():
            string = str(item_code)
        return str(string)

    # Addes the item code to its' respective Cambrai Column value if it belogs
    # there
    def produce_part_b(self) -> pd.DataFrame:
        for clmn_name in self.mino_df.columns.tolist():
            self.isr_df[clmn_name.replace(" ", "_").upper() + "_VALUE"] = \
                self.isr_df.ITEM_CODE.apply(lambda x:
                                            self.produce_part_a(self.mino_df, x,
                                                                clmn_name))

    # Reads all the excel files that are located in the same directory
    def produce_part_c(self) -> None:
        self.isr_df['COMBINED_MINO'] = self.isr_df[self.isr_df.columns
        [-len(self.mino_df.columns.tolist()):]].apply(
            lambda x: ''.join(x.dropna().astype(str)), axis=1)
        self._product.parts.update({'Inventory Search Report': self.isr_df})