from enum import Enum, unique


@unique
class TopElementItem(Enum):
    LOGO = '._title_14m5i_126'
    BBS = '//div[@class="_tabs_inner_14m5i_108"]//ul/li[1]'
    STORE = '//div[@class="_tabs_inner_14m5i_108"]//ul/li[2]'
    SERVER = '//div[@class="_tabs_inner_14m5i_108"]//ul/li[3]'
    FLYME = '//div[@class="_tabs_inner_14m5i_108"]//ul/li[4]'
    DOWNLOAD = '//div[@class="_tabs_inner_14m5i_108"]//ul/li[5]'

@unique
class TopHotEvent(Enum):
    HOTEVENT = '//p[@class="_slogan_f5szj_2"]'

@unique
class HotTopic(Enum):
    HOTTOPICLIST = '//li[@class="_ht_item_ont9d_11"]'
    NOMORE = '//ul[@class="_ht_card_wrap_ont9d_4 _no_showMore_ont9d_21"]'
    HASMORE = '//ul[@class="_ht_card_wrap_ont9d_4 _showMore_ont9d_18"]'