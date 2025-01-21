import time
import pyautogui
from pynput.mouse import Listener, Button

def wait_for_left_click():
    """
    Blocks until a left mouse click occurs.
    Returns the (x, y) coordinates of the click.
    """
    click_position = []

    def on_click(x, y, button, pressed):
        # When the left button is pressed, capture coordinates and stop listener
        if pressed and button == Button.left:
            click_position.append((x, y))
            return False  # Stop the listener

    with Listener(on_click=on_click) as listener:
        listener.join()

    # click_position[0] is (x, y) of the first (and only) left click
    return click_position[0]

def get_region():
    """
    Capture the region of interest in the screen.
    Returns the (x, y, width, height) of the region.
    """
    # 1. Capture top-left corner
    print("Move your mouse to the desired top-left corner of the region...")
    time.sleep(3.5)  # Give user time to move the mouse
    print("Click the left mouse button to register the position...")
    start_x, start_y = wait_for_left_click()
    print(f"Top-left corner: ({start_x}, {start_y})")

    # 2. Capture bottom-right corner
    print("Move your mouse to the opposite bottom-right corner of the region...")
    time.sleep(3.5)  # Give user time to move the mouse
    print("Click the left mouse button to register the position...")
    end_x, end_y = wait_for_left_click()
    print(f"Bottom-right corner: ({end_x}, {end_y})")

    # 3. Calculate the region
    width = end_x - start_x
    height = end_y - start_y

    print(f"Region: x={start_x}, y={start_y}, width={width}, height={height}")
    return (start_x, start_y, width, height)