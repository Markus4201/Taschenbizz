from Utility.window_detect import getAlbionPos


class PositionConfig:
    def __init__(self):
        X, Y = getAlbionPos()
        #CreateBuyOrder
        self.ITEM_NAME_ENTRY_POS = (X + 330, Y + 180)
        self.BUY_BUTTON_POS = (X + 920, Y + 330)
        self.ORDER_OVERVIEW_TOGGLE_POS = (X + 906, Y + 233)
        self.BUY_ORDER_POS = (X + 266, Y + 430)
        self.INCREASE_QUANTITY_POS = (X + 547, Y + 484)
        self.INCREASE_PRICE_POS = (X + 544, Y + 518)
        self.CONFIRM_ORDER_POS = (X + 561, Y + 608)
        self.CONFIRM_YES_POS = (X + 517, Y + 450)
        self.ORDER_OVERVIEW_REGION = (X + 690, Y + 272, X + 727, Y + 288)
        self.BEST_BUY_PRICE_REGION = (X + 915, Y + 272, X + 952, Y + 288)
        self.MY_ORDERS_POS = (X + 1033, Y + 470)
        self.ITEM_ENTRY_POS = (X + 340, Y + 180)
        self.EDIT_BUTTON_POS = (X + 892, Y + 311)
        self.SCREEN_REGION = (X + 1022, Y + 616, X + 1043, Y + 636)
        self.COLLECT_TRADES_POS = (X + 1040, Y + 615)
        self.COLLECT_ALL_POS = (X + 940, Y + 750)
        self.BUY_SECTION_BUTTON = (X + 1036, Y + 242)
        self.MY_ORDER_ITEM_NAME = (X + 385, Y + 302, X + 530, Y + 321)
