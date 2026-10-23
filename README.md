# Experimentor Guidelines

## Procedure

1. start the questionnaire (file `~QUESTIONNAIRE.html`) and
     * enter the subject id

2. start the experiment (file `~RUN_EXPERIMENT.bat`)
     * Enter the right subject id
     * Practice blocks
       * have to be started by the experimenter with the **RETURN** key
       * occur when the task type or go conditions change (4 times).
     * Participants can start the experimental blocks by themselves with any key
     * Instructions screen can be used as a short break for the participants.

## Instructions for the participants

### Task type: Simple go/no-go task

If the instruction screen says: **Response: SPACE bar**

----

*You will see a number in the center of the screen. Your task is to respond  ONLY, if the number is smaller (or large) than 5. Otherwise, you don't  respond.*

*The response is to press the space bar. Please respond as quickly and accurately as possible.*

*The presented other stimuli (arrows) are irrelevant and should be ignored.*

---



### Choice go/no-go task

If the instruction screen says: **Response: arrow key as indicated by the arrows.**

---

*You will see a number in the center of the screen. Your task is to respond  ONLY, if the number is smaller (or large) than 5. Otherwise, you don't  respond.*

*The response is to press the arrow key that is indicated by the arrows (left, right, up or down)*

*Please respond as quickly and accurately as possible.*

---

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

