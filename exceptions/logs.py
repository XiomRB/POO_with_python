import logging
import traceback
import contextlib

logging.basicConfig(
    level=logging.ERROR,  # nivel de error que se mostrará o guardará, por defecto tiene el tipo WARNING
    filename='error.log',  #para guardar los logs en un archivo y no se impriman en consola
    format="%(asctime)s:%(levelname)s:%(message)s"  # le da formato a como escribira el mensaje, por defecto es ERROR:root:mensaje
)

def write_error(error):
    exception_info = {
        'message': error,
        'detail': traceback.format_exc()
    }
    logging.error(exception_info)


try:
    9.2 / 0
except Exception as error:
    write_error(error)



@contextlib.contextmanager    # se usa este decorador para poder ejecutar with (linea 22)
def write_critical():
    try:
        yield                     # aca se ejecutara todo el codigo dentro de with a menos que ocurra una excepcion
    except Exception as error:                   
        exception_info = {
            'message': error,
            'detail': traceback.format_exc()
            }
        logging.critical(exception_info)

with write_critical():
    print(10/0)