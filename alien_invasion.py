import sys
import pygame
class Settings():
    def __init__(self):
        self.screen_width = 1152
        self.screen_height = 648
        self.bg_color = (255,255,255)
class Ship():
    def __init__(self,screen):
        self.screen = screen

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('C:\\Users\\18223\\Desktop\\PycharmProjects\\alien_invasion\\images\\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 开始游戏的主循环
    ship = Ship(screen)
    while True:
    # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    # 每次循环都重绘屏幕
        screen.fill(ai_settings.bg_color)
        ship.blitme()
    # 让最近绘制的屏幕可见
        pygame.display.flip()

run_game()