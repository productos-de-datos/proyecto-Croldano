"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""
import urllib.request
import datetime
import logging
from os import remove
from wsgiref.util import request_uri

from requests import request

fecha = datetime.datetime.now()

total_years = fecha.year - 1995

years = list(range(1995, 1995 + total_years, 1))

for year in years:
        f = open(f"data_lake/landing/{year}.xlsx", "wb")
        try:
            f.write(
            request.urlopen(
                    f"https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/{year}.xlsx"
                ).read()
            )
            f.close()
        except Exception:
            f.close()

            f = open(f"data_lake/landing/{year}.xls", "wb")
            f.write(
              request_uri.urlopen(
                    f"https://github.com/jdvelasq/datalabs/raw/master/datasets/precio_bolsa_nacional/xls/{year}.xls"
                ).read()
            )
            f.close()
        except:
            logging.exception("Error con el archivo: " & year)


if __name__ == "__main__":
    import doctest

    doctest.testmod()