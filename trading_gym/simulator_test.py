from simulator import Simulator
from configurations.configs import TIMEZONE
from datetime import datetime as dt


def test_get_tick_history():
    """
    Test case to query Arctic TickStore
    :return:
    """
    start_time = dt.now(TIMEZONE)

    sim = Simulator(use_arctic=True)
    query = {
        'ccy': ['ETC-USD'],
        'start_date': 20181231,
        'end_date': 20190102
    }
    tick_history = sim.get_tick_history(query=query)

    print('\n{}\n'.format(tick_history))

    elapsed = (dt.now(TIMEZONE) - start_time).seconds
    print('Completed %s in %i seconds' % (__name__, elapsed))
    print('DONE. EXITING %s' % __name__)


def test_get_orderbook_snapshot_history():
    """
    Test case to export testing/training data for reinforcement learning
    :return:
    """
    start_time = dt.now(TIMEZONE)

    sim = Simulator(use_arctic=True)
    query = {
        'ccy': ['ETC-USD', 'tETCUSD'],
        'start_date': 20181229,
        'end_date': 20181231
    }
    orderbook_snapshot_history = sim.get_orderbook_snapshot_history(query=query)

    filename = '{}_{}'.format(query['ccy'][0], query['start_date'])
    sim.export_to_csv(data=orderbook_snapshot_history, filename=filename, compress=False)

    elapsed = (dt.now(TIMEZONE) - start_time).seconds
    print('Completed %s in %i seconds' % (__name__, elapsed))
    print('DONE. EXITING %s' % __name__)


def test_extract_features():
    """
    Test case to export multiple testing/training data sets for reinforcement learning
    :return:
    """
    start_time = dt.now(TIMEZONE)

    sim = Simulator(use_arctic=True)
    # for ccy in ['BTC-USD', 'ETH-USD', 'LTC-USD', 'BCH-USD']: #, 'ETC-USD']:
    for ccy in ['ETH-USD']:
        query = {
            'ccy': [ccy],
            'start_date': 20181231,
            'end_date': 20190102
        }
        sim.extract_features(query)

    elapsed = (dt.now(TIMEZONE) - start_time).seconds
    print('Completed %s in %i seconds' % (__name__, elapsed))
    print('DONE. EXITING %s' % __name__)


if __name__ == '__main__':
    """
    Entry point of simulation application
    """
    # test_get_tick_history()
    test_get_orderbook_snapshot_history()
    # test_extract_features()
