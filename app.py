import random
import gradio as gr
import time 

MAX_BOXES = 15 # The max amount of cells to show each iteration's search/range snapshots 

# Audio for the dice roll and image of the bullseye
DICE_AUDIO_URL = "https://cdn-uploads.huggingface.co/production/uploads/6929198bc7f3a721cc6fbe1b/x3I1W0Mkf1oYs3IXSN2PQ.mpga"
SUCCESS_IMAGE_URL = "https://cdn-uploads.huggingface.co/production/uploads/6929198bc7f3a721cc6fbe1b/H8WmB3dRz9wcZyocuXDdK.jpeg"

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Randomly Generating a list of 10 - 15 numbers
#-----------------------------------------------------------------------------------------------------------------------------------------------------

def build_random_list():
    size = random.randint(10, 15) # Randomly chooses the size of the list
    new_list = [random.randint(0, 100) for i in range(size)] # Generates the list choosing random numbers from 0 - 100
    sorted_list = sorted(new_list) # Sorts the list in ascending order
    shown = f"Generated List ({len(sorted_list)} elements):\n{sorted_list}" 
    audio_url = f"{DICE_AUDIO_URL}?t={time.time()}"

    return shown, audio_url, sorted_list

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# List Scanner
#-----------------------------------------------------------------------------------------------------------------------------------------------------

def locate_number(user_value, stored_list): 
    if not stored_list: # Checks for when the list hasn't been generated and the user tries to find a number
        return (
            "🔴 No List found. Generate a list first.",
            *["" for i in range(MAX_BOXES)], 
            *["" for i in range(MAX_BOXES)],
            "🔴 Search error, the list is empty!",
            gr.update(value = None, visible = False)
        )
    # This checks the user's input and sees if is an invalid input, if it's a negative or decimal it will fail
    try:
        if float(user_value) != int(float(user_value)) or float(user_value) < 0:
            raise ValueError
        target = int(user_value)
    except:
        return (
            f"Generated List:\n{stored_list}",
            *["" for i in range(MAX_BOXES)],
            *["" for i in range(MAX_BOXES)],
            "❌ Invalid input, please enter a positive whole number ❌",
            gr.update(value = None, visible = False)
        )
        
    # Empty lists for showing the steps and snapshots for each iteration
    trace_steps = []
    trace_ranges = []
    matches = []

    trace_ranges.append(f"Full list → {stored_list}")

    # This loop goes through the list and checks every value
    for idx, item in enumerate(stored_list): # 
        trace_steps.append(f"Checking index {idx} → {item}")
        if item == target:
            matches.append(idx)
        trace_ranges.append(f"Current list → {stored_list}")
        if len(trace_steps) >= MAX_BOXES: 
            break

    # Incase the number is found before the 15 max steps, it makes the cells that are unneeded filled with an empty string 
    while len(trace_steps) < MAX_BOXES:
        trace_steps.append("")
    while len(trace_ranges) < MAX_BOXES:
        trace_ranges.append("")

    # Prepared the final result message for both false and true cases
    if matches:
        result = (
            f"✅ The number {target} has been found ✅\n"
            f"Index: {matches}\n"
            f"Total Occurrences: {len(matches)}"
        )

        image_output = gr.update(value = SUCCESS_IMAGE_URL, visible = True)

    else:
        result = f"❌ The number you are looking for does not appear in the list ❌"
        image_output = gr.update(value = None, visible = False)

    list_label = f"Generated List ({len(stored_list)} values):\n{stored_list}" # This displays the list and it's length 
    return list_label, *trace_steps, *trace_ranges, result, image_output

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# Gradio UI
#-----------------------------------------------------------------------------------------------------------------------------------------------------

with gr.Blocks(title = "Number Targetter") as app:

    # Description of the app with the steps of usage
    gr.Markdown("""
    # 🎯 Number Targetter 🎯
    **Description:** Generate a random list of 10 - 15 numbers and find your target number.

    **Step 1:** Generate a list.\n
    **Step 2:** Enter a number you want to target.\n
    **Step 3:** Click search!\n
    """)

    saved_list = gr.State([]) # Stores the generated list

    # Displays the text for it's respective buttons
    with gr.Row():
        btn_make = gr.Button("Generate List 🎲", elem_id = "btn_generate")
        input_num = gr.Number(label= "Enter a number (0 - 100)", precision = 0)
        btn_find = gr.Button("Search 🔎", elem_id = "btn_search")

    # Displays the generated list and the dice roll audio for when the button is clicked
    list_display = gr.Textbox(label = "Generated List", lines = 2, interactive = False)
    dice_audio = gr.Audio(label = "", autoplay = True)

    
    # Searching Steps section, displays every iteration search observation 
    gr.Markdown("### 🟢 Search Steps:")
    step_boxes = [gr.Textbox(label = f"Step {i+1}", lines = 1, interactive = False) for i in range(MAX_BOXES)]

    # Range Snapshot section, displays every iteration for the range of the list
    gr.Markdown("### 🔵 Range Snapshots:")
    range_boxes = [gr.Textbox(label = f"Range {i+1}", lines = 1, interactive = False) for i in range(MAX_BOXES)]

    
    # Target Result section, displays the result and the image of a bullseye when the number is found
    with gr.Column():
        gr.Markdown("### 🎯 Target Result:")
        result_field = gr.Textbox(label = "", lines = 3, interactive = False)
        found_image = gr.Image(label =  "Success Image", visible = False)

    # Button logic for when it is clicked
    btn_make.click(
        fn = build_random_list,
        inputs = [],
        outputs = [list_display, dice_audio, saved_list]
    )

    btn_find.click(
        fn =  locate_number,
        inputs = [input_num, saved_list],
        outputs = [list_display, *step_boxes, *range_boxes, result_field, found_image]
    )

    # Colour for the buttons, blue for generate and green for search
    app.launch(css="""
        #btn_generate { background-color: #3b82f6; color: white; }
        #btn_search { background-color: #10b981; color: white; }  
    """)