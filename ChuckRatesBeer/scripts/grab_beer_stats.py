from ChuckRatesBeer.scripts.untappd import Untappd
from chuck_pyutils import core as utils

config = utils.read_config(utils.get_file_path(__file__, 'config.ini'))
untappd_conn = Untappd(config['UNTAPPD']['CLIENT_ID'], config['UNTAPPD']['CLIENT_SECRET'])
print(untappd_conn.feed('user', 'chuckwoodraska'))