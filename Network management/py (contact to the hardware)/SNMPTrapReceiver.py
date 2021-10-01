from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import logging
import datetime
import os
import requests


def start():
    snmpEngine = engine.SnmpEngine()
    Port = 162  # trap listerner port
    trapagentaddress = '10.0.3.16'  # Trap listerner address aslo the current api for your device

    # Checks if log file exist
    if not os.path.isfile(f'./received_traps_{datetime.date.today().year}_{datetime.date.today().month}_{datetime.date.today().day}.log'):
        print('New file created!')
        # Creates a new log file for the current day
        with open(f'received_traps_{datetime.date.today().year}_{datetime.date.today().month}_{datetime.date.today().day}.log',
                  'w') as f:
            f.write('')
    #loggin config's so we can change our filename for each day
    logging.basicConfig(filename=f'received_traps_{datetime.date.today().year}_{datetime.date.today().month}_{datetime.date.today().day}.log',
                        filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)

    #some information when running the logger
    logging.info(f'Agent is listening SNMP Trap on {trapagentaddress} , Port : {str(Port)}')
    logging.info('--------------------------------------------------------------------------')

    print(f'Agent is listening SNMP Trap on {trapagentaddress} , Port : {str(Port)}')

    config.addTransport(
        snmpEngine,
        udp.domainName + (1,),
        udp.UdpTransport().openServerMode((trapagentaddress, Port))
    )

    # Configure community here
    config.addV1System(snmpEngine, 'my-area', 'public')

    def update_api(string):# logging to file
        url = f"http://127.0.0.1:5000/{string.replace('/','')}"

        payload = dict(key1='value1', key2='value2')

        res = requests.get(url, data=payload)
        print(res)

    def terminal_output(snmpEngine, stateReference, contextEngineId, contextName, varbinds, cbCtx):
        print('Received new Trap message')
        logging.info('Received new Trap message')
        for name, val in varbinds:
            print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
            logging.info('%s = %s' % (name.prettyPrint(), val.prettyPrint()))
            update_api(f'{datetime.datetime.now().time()} - %s %s' % (val.prettyPrint(), '<br>'))

        logging.info('==== End of Incoming Trap ====')

    ntfrcv.NotificationReceiver(snmpEngine, terminal_output)

    snmpEngine.transportDispatcher.jobStarted(1)

    try:
        snmpEngine.transportDispatcher.runDispatcher()
    except ValueError:
        snmpEngine.transportDispatcher.closeDispatcher()
        raise

