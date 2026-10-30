# Flanker SNARC: Experimentor Guidelines

The paradigm used is called go/no-go task. That is, subject have to read the number and respond (go) or not respond (no-go): There are different blocks during the experiment. The blocks differ by two variations of the task:

  * 2 Go condition:  respond to *small* or to *large* numbers
  * 2 Type of response:
    * response always by pressing *space bar* (**simple go-no/go task**) or
    * by pressing the *arrow keys displayed* on the screen (**choice go-no/go task**)

Which block is coming next will be indicated on the instruction screen before the block start: For example: "Response: UP or DOWN key as indicated by the arrows. Respond only if the number is SMALLER than 5"


## General Procedure

1. start the questionnaire (file `~QUESTIONNAIRE.html`) and
     * enter the subject id

2. start the experiment (file `~RUN_EXPERIMENT.bat`)
     * Enter the right subject id
     * Practice blocks
       * have to be started by the experimenter with the **RETURN** key
       * occur when the task type or go conditions change (4 times).
     * Participants can start the experimental blocks by themselves with any key
     * Instructions screen can be used as a short break for the participants.

You can quit an experiment any time by pressing ESC (Escape). Sometimes you need to press ESC twice to quit the experiment.

### Instructing participants for the 4 different task blocks

1. *"You will see a digit in the centre of the screen. Your task is to decide whether the number is small or large than 5. In the next block your task is:"*
2. Depending on the instruction screen:
    *  *"If the number is SMALLER than 5, you have to press "SPACE". Otherwise, do not respond. The arrows displayed on the screen can be ignored."*
    *  *"If the number is LARGER than 5, you have to press "SPACE". Otherwise, do not respond. The arrows displayed on the screen can be ignored."*
    *  *If the number is SMALLER than 5, you have to press the ARROW KEY as  displayed on the screen.*
    *  *If the number is LARGER than 5, you have to press the ARROW KEY as  displayed on the screen.*
3. *"Please respond as quickly and accurately as possible."*
4. *"We will first start with a short practice block to get you familiar with the task. If you have no further questions, press space bar to start the next block.*"

**Important**: To start a new block where new instructions are needed, the experimenter has to press RETURN. The subject can not go on with space bar.



----

# Experiment Details

## Design

**Block-wise manipulated conditions** (8 blocks in total)

* **2 task types**: simple go/no-go (press space) vs. choice go/no-go (press one of the arrow keys)
* **2 go conditions**: responded to smaller/larger numbers
* **2 arrow conditions**: horizontal, vertical

Different block conditions were counterbalanced across participants.

**Conditions varied within each block**

* **4 numbers** : 1, 2, 8 and 9
* **2 flanker congruencies**: spatially congruent vs. incongruent arrow (up/left or down/right)
* **2 flanker pre-cues**: arrows presented shortly before the target (*informative* pre-cue) or just dots (*uninformative* pre-cue)

Each condition within blocks was repeated 4 times. That is, each block contained 64 trials ($4 \times 2 \times 2 \times 4 = 64$), resulting in a total of 512 trials in total.

The order of trials within each block was randomized.

### Procedure of each trial


|     | Stimulus             | Duration       | Notes                               |
| --- | -------------------- | -------------- | ----------------------------------- |
| 1.  | Precue               | 700 ms         | arrows or dots                      |
| 2.  | Target               | max. 1500 ms   | number & arrows, ends with response |
|     | Error feeback        | 3000 ms        | only if error occurred       |
| 3.  | Inter-trial interval | 700 - 1200 ms | blank screen, random interval                     |

