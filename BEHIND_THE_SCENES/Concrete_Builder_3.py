from BEHIND_THE_SCENES.Builder import Builder
from BEHIND_THE_SCENES.Product import Product1
import pandas as pd

class ConcreteBuilder3(Builder):
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

    def produce_part_a(self, item_code) -> str:
        lst = []
        returned_value = ''
        try:
            lst = self.mino_df[(self.mino_df.astype(str) ==
                                str(item_code)).any(axis=1) == True
                               ].iloc[0].tolist()
        except IndexError:
            pass
        if len(lst) >= 1:
            returned_value = str('|'.join(str(e) for e in lst))
        return returned_value

    def produce_part_b(self) -> None:
        self.isr_df['DELIMITED'] = self.isr_df.COMBINED_MINO.apply(lambda x:
                                                                   self.produce_part_a(x) if x != '' else x)

    def produce_part_c(self) -> None:
        clmns_lst = self.mino_df.columns.tolist()
        for i in range(len(clmns_lst)):
            clmns_lst[i] = clmns_lst[i].upper().replace(' ', '_')
        self.isr_df[clmns_lst] = self.isr_df['DELIMITED'] \
            .str.split('|', -1, expand=True)

        self._product.parts.update({'Inventory Search Report': self.isr_df})
