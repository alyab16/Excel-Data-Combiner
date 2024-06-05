import pandas as pd
import sqlite3


class Product1():
    """
    It makes sense to use the Builder pattern only when your products are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can
    produce unrelated products. In other words, results of various builders
    may not always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = {}

    def add(self, name, part: pd.DataFrame()) -> None:
        self.parts.update({name: part})

    def build_report(self) -> None:
        # conn = sqlite3.connect('test_database')
        # c = conn.cursor()
        # for x in self.parts.keys():
        #     lst = self.parts.get(x).columns.tolist()
        #     c.execute('CREATE TABLE IF NOT EXISTS {} ({})'.format(x, str(','.join(str(e) for e in lst))))
        #     conn.commit()
        #     self.parts.get(x).to_sql(x, conn, if_exists='replace', index=False)

        try:

            output_name = 'FINAL_PRODUCT.csv'
            df_name = 'Inventory Search Report'
            self.parts.get(df_name).to_csv(output_name, index=False)
            # writer = pd.ExcelWriter(output_name, engine='xlsxwriter')

            # for x in self.parts.keys():
            #     self.parts.get(x).to_excel(writer, index=False, sheet_name=
            #     x)
            # # self.parts.to_excel(writer, index = False,sheet_name =
            # #                     "Inventory Search Report")
            # # mino_code_search_df.to_excel(writer, index = False,sheet_name =
            # # "Cambrai Information")

            # writer.save()
            print("Process Completed! :)")
            return
        except PermissionError:
            print("Error: Access to the file {} is denied! As such, the "
                  "process could not be completed. Please Close The {} file "
                  "and restart the process. Thanks!".format(output_name,
                                                            output_name))
            return

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")
