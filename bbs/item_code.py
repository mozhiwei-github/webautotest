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

@unique
class TopSwiper(Enum):
    TOPSWIPERVIEW = '//div[@class="_swiper_r_157cm_266 _swiper_icon_157cm_239"]'
    TOPWSWIPERLIST = '//div[@class="swiper swiper-initialized swiper-horizontal swiper-pointer-events _new_slider_157cm_3"]/div[@class="swiper-wrapper"]/div'
    TOPWSWIPERACTIVELIST = '//div[@class="swiper swiper-initialized swiper-horizontal swiper-pointer-events _new_slider_157cm_3"]/div[@class="swiper-wrapper"]/div[@class="swiper-slide swiper-slide-duplicate swiper-slide-duplicate-active _slider_img_w_157cm_8"]'

@unique
class ModeSwitch(Enum):
    MODESWITCHBUTTON = '//span[@class="_slider_14m5i_25  _slider_1_14m5i_1085"]'
    DARKMODE = '//html[@class="dark bg-191b29"]'
    NORMALMODE = '//html[@class="bg-191b29"]'

@unique
class Circle(Enum):
    CIRCLEVIEW = '//ul[@class="_ht_word_v7l0m_267"]'
    CICLELIST = '//li[@class="_card_item_v7l0m_31"]'
    CICLEMOREBUTTON = '//div[@class="_new_circles_v7l0m_6"]//li[@class="_ht_more_v7l0m_14"]'
    CIRCLESHOWMORE = '//ul[@class="_card_wrap_v7l0m_26 _showMore_v7l0m_18"]'
    CIRCLEHASMORE = '//ul[@class="_card_wrap_v7l0m_26 _no_showMore_v7l0m_22"]'
