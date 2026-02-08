import pyautogui, pygame

pygame.init()
pygame.joystick.init()

joysticks = []
icon = pygame.image.load("assets/icon.png")
background = pygame.image.load("assets/controller.png")

pygame.display.set_icon(icon)
window = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Controller Visualiser")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.JOYDEVICEADDED:
            print("Controller connected.")
            joy = pygame.joystick.Joystick(event.device_index)
            joysticks.append(joy)
    
    for joystick in joysticks:
        time = pygame.time.get_ticks()
        window.blit(background, (0, 0))
        
        if joystick.get_button(0): # Button A
            pygame.draw.circle(window, "#000000", (889, 274), 35)
            print("A")
            
        if joystick.get_button(1): # Button B
            pygame.draw.circle(window, "#000000", (953, 207), 35)
            print("B")
        
        if joystick.get_button(2): # Button X
            pygame.draw.circle(window, "#000000", (823, 207), 35)
            print("X")
            
        if joystick.get_button(3): # Button Y
            pygame.draw.circle(window, "#000000", (889, 141), 35)
            print("Y") #Y: 141; X: 888.5
            
        if joystick.get_button(4): # Button LB
            print("LB")

        if joystick.get_button(5): # Button RB
            print("RB")
            
        if joystick.get_button(6): # Button View
            pygame.draw.circle(window, "#000000", (569, 206), 20)
            print("View")
            
        if joystick.get_button(7): # Button Menu
            pygame.draw.circle(window, "#000000", (710, 206), 20)
            print("Menu")
            
        if joystick.get_button(10): # Button XBOX
            pygame.draw.circle(window, "#000000", (640, 108), 32)
            print("XBOX")
            
        # L
        pygame.draw.circle(window, "#000000", (393 + (joystick.get_axis(0) * 25), 206 + (joystick.get_axis(1) * 25)), 40)
        
        if joystick.get_button(8): # Button L3
            print("L3")
        else:
            pygame.draw.circle(window, "#FFFFFF", (393 + (joystick.get_axis(0) * 25), 206 + (joystick.get_axis(1) * 25)), 33)
                        
        # R
        pygame.draw.circle(window, "#000000", (767 + (joystick.get_axis(2) * 25), 352 + (joystick.get_axis(3) * 25)), 40)
        
        if joystick.get_button(9): # Button R3
            print("R3")
        else:
            pygame.draw.circle(window, "#FFFFFF", (767 + (joystick.get_axis(2) * 25), 352 + (joystick.get_axis(3) * 25)), 33)

        
    pygame.display.flip()