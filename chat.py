import pygame
import sys
import re

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Chatbot")

# Set up fonts
font = pygame.font.Font(None, 36)
input_font = pygame.font.Font(None, 28)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Function to evaluate a math expression
def evaluate_expression(expression):
    try:
        # Use regex to allow only numbers and basic operators
        if re.match(r'^[0-9+\-*/(). ]+$', expression):
            result = eval(expression)
            return f"Result: {result}"
        else:
            return "Invalid input. Please use numbers and operators only."
    except Exception as e:
        return "Error in calculation."

# Main loop
def main():
    input_box = pygame.Rect(20, HEIGHT - 40, WIDTH - 40, 30)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    messages = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        response = evaluate_expression(text)
                        messages.append(f"You: {text}")
                        messages.append(f"Bot: {response}")
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(WHITE)

        # Render messages
        y_offset = 20
        for message in messages[-10:]:  # Show last 10 messages
            msg_surface = font.render(message, True, BLACK)
            screen.blit(msg_surface, (20, y_offset))
            y_offset += 30

        # Render input box
        txt_surface = input_font.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()

if __name__ == "__main__":
    main()