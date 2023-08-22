import pygame
import sys

class PygameSimulator:
    def __init__(self, size) -> None:
        pygame.init()
        self.width = size[0]
        self.height = size[1]
        
    def init(self):
        self.screen = pygame.display.set_mode((self.width, self.height))

    def getbuffer(self, image):
        img = image
        imwidth, imheight = img.size
        if(imwidth == self.width and imheight == self.height):
            img = img.convert('1')
        elif(imwidth == self.height and imheight == self.width):
            # image has correct dimensions, but needs to be rotated
            img = img.rotate(90, expand=True).convert('1')
        else:
            # return a blank buffer
            return [0x00] * (int(self.width/8) * self.height)

        buf = bytearray(img.tobytes('raw'))
        # The bytes need to be inverted, because in the PIL world 0=black and 1=white, but
        # in the e-paper world 0=white and 1=black.
        for i in range(len(buf)):
            buf[i] ^= 0xFF
        return buf
    
    def display(self, image):
        self.checkEventLoop()
        self.screen.fill((255,255,255))
        image = image.convert("RGB")
        self.screen.blit(pygame.image.fromstring(image.tobytes() ,image.size, image.mode), (0,0))
        pygame.display.update()
        self.checkEventLoop()

    def Clear(self):
        self.screen.fill((255,255,255))

    def sleep(self):
        pass

    def checkEventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
