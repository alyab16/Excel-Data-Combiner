from __future__ import annotations
import os
from BEHIND_THE_SCENES.Builder import Builder
from BEHIND_THE_SCENES.Concrete_Builder_0 import ConcreteBuilder0
from BEHIND_THE_SCENES.Concrete_Builder_1 import ConcreteBuilder1
from BEHIND_THE_SCENES.Concrete_Builder_2 import ConcreteBuilder2
from BEHIND_THE_SCENES.Concrete_Builder_3 import ConcreteBuilder3


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing products according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled product.
        """
        self._builder = builder

    """
    The Director can construct several product variations using the same
    building steps.
    """

    def build_product_concrete_builder_0(self) -> None:
        self.builder.produce_part_c()

    def build_product_concrete_builder_1(self) -> None:
        self.builder.produce_part_c()

    def build_product_concrete_builder_2(self) -> None:
        self.builder.produce_part_b()
        self.builder.produce_part_c()

    def build_product_concrete_builder_3(self) -> None:
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and 
    then initiates the construction process. The end result is retrieved from 
    the builder object.
    """
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    director = Director()

    builder = ConcreteBuilder0()
    director.builder = builder
    director.build_product_concrete_builder_0()

    builder = ConcreteBuilder1()
    director.builder = builder
    director.build_product_concrete_builder_1()

    product_writer = director.builder.product

    builder = ConcreteBuilder2(product_writer.parts.get('Inventory Search Report'),
                               product_writer.parts.get('Cambrai Information'))
    director.builder = builder
    director.build_product_concrete_builder_2()

    builder = ConcreteBuilder3(product_writer.parts.get('Inventory Search Report'),
                               product_writer.parts.get('Cambrai Information'))
    director.builder = builder
    director.build_product_concrete_builder_3()

    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    product_writer.build_report()

    # print("\n")

    # # Remember, the Builder pattern can be used without a Director class.
    # print("Custom product: ")
    # builder.produce_part_a()
    # builder.produce_part_b()
    # builder.product.list_parts()
