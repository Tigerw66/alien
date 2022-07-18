
def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init()
    ai_screen = Settings()
    screen = pygame.display.set_mode((ai_screen.screen_width,ai_screen.screen_height))
    pygame.display.set_caption("Alien_Invasion")
    #创建一艘飞船
    ship = Ship(screen)

      #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环时都重绘屏幕
        screen.fill(ai_screen.bg_color)
        ship.blitme()

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()