#!/usr/bin/env python
# -*- coding: utf-8 -*-

#v1.1

from expyriment import control, design, stimuli
from expyriment.misc import constants

#control.set_develop_mode(True)
control.defaults.auto_create_subject_id = False
control.defaults.initialise_delay = 5

ITI_RANGE = [700, 1200]
NUMBERS = [1, 2, 8, 9]
T_CUE = 700
T_ERROR_FEEDBACK = 3000
RT_DEADLINE = 1500
N_REP_PER_CONDITION = 4

class Arrow():

    def __init__(self, direction:str):
        self.stim = stimuli.Picture(f"stim/right-arrow.png")
        self.direction = direction
        if direction == "r":
            self.key = constants.K_RIGHT
        elif direction == "l":
            self.stim.rotate(180)
            self.key = constants.K_LEFT
        elif direction == "u":
            self.stim.rotate(90)
            self.key = constants.K_UP
        elif direction == "d":
            self.stim.rotate(-90)
            self.key = constants.K_DOWN
        else:
            raise ValueError("direction must be 'l', 'r', 'u', or 'd'")
        self.stim.scale(0.3)

def grid(grid_size:int) -> list:
    """Returns a list of coordinates for a grid with the given size."""
    r = [-1, 0, 1]
    coords = []
    for x in r:
        for y in reversed(r):
            coords.append((x * grid_size, y * grid_size))
    return coords

def get_stimulus(center_stim:stimuli.Picture | None, arrow:stimuli.Picture, grid_size:int) -> stimuli.Canvas:
    stim = stimuli.Canvas((grid_size*3, grid_size*3))
    for g in grid(grid_size):
        if g == (0, 0):
            if center_stim:
                center_stim.plot(stim)
        else:
            arrow.reposition(g)
            arrow.plot(stim)
    return stim

########### DESIGN ####################
def make_block(go_small:bool, vertical:bool, practice:bool, block_name:str) -> design.Block:
    block = design.Block(block_name)
    block.set_factor("go_small", int(go_small))
    block.set_factor("vertical", int(vertical))
    block.set_factor("practice", int(practice))
    if vertical:
        arrow_directions = ["u", "d"]
    else:
        arrow_directions = ["l", "r"]

    for digit in NUMBERS: # NUMBERS
        for cue_resps in [1,0]: # cue_resp or not
            for arrow in arrow_directions:
                trial = design.Trial()
                trial.set_factor("digit", digit)
                trial.set_factor("arrow", arrow)
                trial.set_factor("cue_resp", cue_resps)
                is_go = (digit<=5 and go_small) or (digit>5 and not go_small)
                trial.set_factor("is_go", int(is_go))
                if practice:
                    if digit in [1, 9]: # only two numbers for practice
                        block.add_trial(trial, copies=1)
                else:
                    block.add_trial(trial, copies=N_REP_PER_CONDITION)
    block.shuffle_trials()
    return block

def add_design(exp: design.Experiment, subject_id:int):
    # make blocks for all combinations of factors and practice blocks
    choice_gonogo = [True, False]
    go_small = [True, False]
    vertical = [True, False]
    if subject_id % 2: # start_with_choice_gonogo_task
        choice_gonogo = list(reversed(choice_gonogo))
    if (subject_id % 4)>=2:
        go_small = list(reversed(go_small))
    if (subject_id % 8)>=4:
         vertical = list(reversed(vertical))

    bl_cnt = 0
    for choice_task in choice_gonogo:
        for gs in go_small:
            practice_required = True # one practice block for change in of instruction (smaller/larger)
            for v in vertical:
                for practice in [True, False]:
                    if practice_required or not practice:
                        if not practice:
                            bl_cnt += 1
                            block_name=f"Block {bl_cnt} of 8"
                        else:
                            block_name= f"Practice   (block {bl_cnt+1})"
                        bl = make_block(gs, v, practice=practice, block_name=block_name)
                        bl.set_factor("choice_gonogo", int(choice_task))
                        exp.add_block(bl)
                        practice_required = False

def instruction_screen(exp: design.Experiment, block: design.Block):
    heading = block.name
    if block.get_factor("choice_gonogo"):
        if block.get_factor("vertical"):
            k = ("UP", "DOWN")
        else:
            k = ("LEFT", "RIGHT")
        instruction_text = f"Response: {k[0]} or {k[1]} key as indicated by the arrows"
    else:
        instruction_text = "Response: SPACE bar"
    if block.get_factor("go_small"):
        instruction_text += "\n\nRespond only if the number is SMALLER than 5"
    else:
        instruction_text += "\n\nRespond only if the number is LARGER than 5"

    stim = stimuli.TextScreen(heading=heading, text=instruction_text)
    stim.present()
    exp.clock.wait(1000)
    exp.keyboard.clear()
    if block.get_factor("practice"):
        exp.keyboard.wait(keys=[constants.K_RETURN])
    else:
        exp.keyboard.wait()

def do_trial(exp: design.Experiment, block: design.Block, trial: design.Trial):
    assert exp.clock is not None, "Experiment is not initialized"

    blank_screen = stimuli.BlankScreen()
    blank_screen.present()
    num = trial.get_factor("digit")
    arr = str(trial.get_factor("arrow"))
    cue_resp = trial.get_factor("cue_resp")
    is_go = trial.get_factor("is_go")

    if cue_resp:
        cue_stim = get_stimulus(None, arrows[arr].stim, grid_size=50) # type: ignore
    else:
        cue_stim = get_stimulus(None, dot, grid_size=50) # type: ignore
    cue_stim.preload()

    target_stim = get_stimulus(numbers[num-1], arrows[arr].stim, grid_size=50) # type: ignore
    target_stim.preload()

    if block.get_factor("choice_gonogo"): # type: ignore
        if block.get_factor("vertical"):
            keys = [arrows["u"].key, arrows["d"].key]
        else:
            keys = [arrows["l"].key, arrows["r"].key]
        correct_key = arrows[arr].key
    else:
        # simple detection
        keys = [constants.K_SPACE]
        correct_key = keys[0]

    #### TRIAL
    iti = design.randomise.rand_int(ITI_RANGE[0], ITI_RANGE[1])
    exp.clock.wait(iti)

    cue_stim.present()
    exp.clock.wait(T_CUE)

    target_stim.present()
    resp, rt = exp.keyboard.wait(keys=keys, duration=RT_DEADLINE)
    blank_screen.present()
    correct = (not is_go and resp is None) or (is_go and resp == correct_key)
    # Error feedback
    if not correct:
        if is_go:
            if resp is None:
                error = "Too slow!"
            else:
                error = "Incorrect key!"
        else: # no go
            error = "No response required!"
        stimuli.TextLine(text=error, text_size=32, text_colour=constants.C_RED).present()
        exp.clock.wait(T_ERROR_FEEDBACK)

    exp.data.add([block.get_factor("choice_gonogo"), # type: ignore
                  block.get_factor("go_small"),
                  block.get_factor("vertical"),
                  block.get_factor("practice"),
                  iti,
                  num, arr, cue_resp, is_go, rt, resp, correct])
    cue_stim.unload()
    target_stim.unload()



###
### MAIN
###

exp = design.Experiment(name="Flanker_SNARC", background_colour=constants.C_GREY,
                            foreground_colour=constants.C_BLACK)
control.initialize(exp)

### Stimuli
dot = stimuli.Circle(radius=4, colour=constants.C_BLACK)
numbers = [stimuli.Picture(f"stim/num{num}.png") for num in range(1, 10)]
for n in numbers:
    n.scale(0.1)
arrows = {d: Arrow(d) for d in ["r", "l", "u", "d"]}


### START ####
control.start()
add_design(exp, subject_id=exp.subject)

exp.data.add_variable_names(["choice_gonogo", "go_small", "vertical", "practice", "iti",
                             "number", "arrow", "cue_response", "is_go", "rt", "resp", "correct"])

for bl in exp.blocks:
    instruction_screen(exp, bl)
    for tr in bl.trials:
        do_trial(exp, bl, tr)

control.end(goodbye_text="Thank you very much for participating in our experiment",
             goodbye_delay=5000)

