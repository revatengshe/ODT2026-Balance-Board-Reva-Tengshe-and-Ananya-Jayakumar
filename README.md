# Open Design and Technology  
## Final Project README

> **Project Weight:** 70%  
> **Team Size:** 2 students  
> **Project Duration:** 4 weeks  
> **Class Time Available:** 6 hours per class  
> **Total Time Available:** 48 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository
After forking this repository, rename it using the format:

`ODT-2026-TeamName`

### Example
`ODT-2026-PixelWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the 4-week build period.  
By the final review, this README should clearly show:
- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules
- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name
`[Team Balanceboard]`

## 1.2 Team Members

| Name | Primary Role | Secondary Role | Strengths Brought to the Project |
|---|---|---|---|
| `Reva Tengshe` | `Electronics, Coding` | `Fabrication, Mechanics` | `Good understanding of code amd circuitry, Documentation` |
| `Ananya Jayakumar` | `Electronics, Fabrication ` | `Coding,/ Mechanics ` | `Good understanding of circuitry, materials and working with them.` |

## 1.3 Project Title
`[Enter the title of your project]`

## 1.4 One-Line Pitch
`A balance board that lets you control games like Fireboy and Watergirl using your feet.`

## 1.5 Expanded Project Idea
In 1–2 paragraphs, explain:
- what your project is,
- what kind of playful experience it creates,
- what makes it fun, curious, engaging, strange, satisfying, competitive, or delightful,
- what technologies are involved.

**Response:**  
`This is a motion-responsive balance board that turns foot movement into game controls, reimagining how games like Fireboy and Watergirl are played. Video Games like Fireboy and Watergirl are controlled by keys on the keyboard like the arrow keys or keys like A,W,D. Instead of sitting and tapping arrow keys or A, W, D, the player sits on a chair and uses their feet to tilt and press the board. The game doesn’t just stay on the screen anymore, you feel involved in it through movement.`

`Three ultrasonic sensors (jump, right, left) are placed under each board to track how it tilts by measuring the distance from the ground. As the player presses or tilts the board with their feet, those changes trigger a keypress on the keyboard, which is connected to the ESP32 via Bluetooth. So instead of pressing keys with your hands, your feet do the work, turning gameplay into something more physical and playful.`

---

# 2. Philosophy Fit

## 2.1 Experience, Not Social Problem
This module does **not** require your project to solve a large social problem.

You are allowed to build:
- toys,
- games,
- interactive objects,
- playful machines,
- kinetic artifacts,
- humorous devices,
- strange but delightful experiences,
- things that are entertaining to use or watch.

## 2.2 What kind of experience are you creating?
Answer the following:
- What is the experience?
- What do you want the player or participant to feel?
- Why would someone want to try it again?

**Response:**  
`It’s an experience that engages you completely. Your mind is focused on the game, but your feet are constantly adjusting, pressing, and reacting. There’s a slight sense of chaos at first as you figure out how much to tilt or press, but that’s what makes it fun.`

`I want the player to feel a rush—like they’re fully switched on. It’s a mix of excitement, focus, and a bit of trial and error, especially in the beginning when nothing really goes as planned. There’s also something kind of funny about it—you might over-press or react too slowly—but that becomes part of the experience. And when you finally get the hang of it, it feels genuinely satisfying.
They’d want to try it again because it’s not something you master instantly. The first attempt is messy, the second feels better, and after that you just want to keep improving or beat someone else. It’s also more fun with people around—watching, reacting, and taking turns adds to the experience..`

## 2.3 Design Persona
Complete the sentence below:

> We are designing this project as if we are a small creative studio making a **[toy / game / playable object / interactive experience]** for **[children / teens / adults / classmates / exhibition visitors / mixed audience]**.

**Response:**  
`We are designing this project as if we are a small creative studio making an interactive experience for a children, teens and adults`

---

# 3. Inspiration

## 3.1 References
List what inspired the project.

| Source Type | Title / Link | What Inspired You |
|---|---|---|
| `Object` | `Arcade games with large joysticks controlling the game on the screen` | `A tangible object controlling the players movement on screen` |
| `Object` | `XBox` | `Immersing the player in the game by turning their body movements into the controls, so what they do physically directly drives what happens on screen.` |
| `Toy` | `A dance mat. https://www.amazon.in/Musical-Electronic-Different-Difficulty-Interactive/dp/B0BDMZNH8B` | `Physically moving to or stamping on the area of the respective contols` |

## 3.2 Original Twist
What makes your project original?

**Response:**  
`Arcade games use joysticks, Xbox uses wireless controllers that the player has to hold at all times and a dance mat uses a floor mat as controllers for the game. None of these have explored using a balance board. It is more intuitive for games like Fireboy and Watergirl where quick, combined movements(jump+side) are required. It also adds a layer of fun and challenge to the game.`

---

# 4. Project Intent

## 4.1 Core Interaction Loop
Describe the main loop of interaction.

Examples:
- press → launch → score → reset
- connect → control → observe → repeat
- turn → trigger → react → repeat
- move object → sensor detects → sound/light response → player reacts

**Response:**  
`Player tilts board with feet → board moves → sensors detect change → keypress triggered → video game character moves → player adjusts feet → repeat`

## 4.2 Intended Player / Audience

| Question | Response |
|---|---|
| Who is this for? | `Anyone who enjoys casual games and is open to a slightly chaotic, physical way of playing, especially people who like trying something new with friends` |
| Age range | `13+ ` |
| Solo or multiplayer | `Multiplayer- 2 players` |
| Expected duration of one round | `2-5 mins` |
| What should the player feel? | `Focus, Excitement, Satisfaction` |
| Is explanation required before use? | `Minimal—quick demo helps, but most people figure it out just by stepping on and trying` |

## 4.3 Player Journey
Describe exactly how a player will use the project.

1. **Approach:** `They see the video game being projected on a screen and two balance boards and two chairs kept in front of the screen`
2. **Start:** `By sitting on a chair and placing their feet on the balance board`
3. **First Action:** `Figuring out the controls and the amount of tilt required`
4. **Main Interaction:** `he player presses and tilts the board with their feet, controlling movement through foot pressure and direction`
5. **System Response:** `For example, if the watergirl balance board is tilted towards the right, the ultrasonic sensor on the right will trigger a 'D' keypress which will make Watergirl move to the right. The same for Fireboy and his respective controls.  `
6. **Win / Lose / End Condition:** `Win: When both the characters are able to successfully make it till the end of the level. 
                                    Lose: When one of the character dies`
7. **Reset:** `Can be controlled in the video game itself`

## 4.4 Rules of Play
If your project is a game, list the rules clearly.

- `The game starts once both players are ready and balanced.`
- `The character moves according to how the player presses or tilts the balance board with their feet`  
- `Players control their characters using only their feet—no hands, no keyboard  `
- `If even one player dies, the other one dies as well`
- `Both the players need to finish the level to win`
---

# 5. Definition of Success

## 5.1 Definition of “Playable”
Your project will be considered complete only if these conditions are met.

- [ ] `The gameplay feels intuituive and responsive, not frustrating or laggy`
- [ ] `Players can complete at least one full level using only the balance board`
- [ ] `The balance board reliably detects body movement`

## 5.2 Minimum Viable Version
What is the smallest version of this project that still delivers the core experience?

**Response:**  
`A cardboard model of the balance board with the ultrasonic sensors attached to its bottom surface. One can't stand on it but the tilting mechanism can be tested on it. If one wants to test standing on it, the minimum viable version can be a balance board bought from stores or that made of HDF and plywood.`

## 5.3 Stretch Features
What features are nice to have but not essential?

- `Custom sensitivity modes- – adjust how responsive the board is (easy for beginners, harder for advanced)`
- `Lights, sound, or vibration on the board reacting to movement or mistakes`


---

# 6. System Overview

## 6.1 Project Type
Check all that apply.

- [+] Electronics-based
- [ ] Mechanical
- [+] Sensor-based
- [ ] App-connected
- [ ] Motorized
- [ ] Sound-based
- [ ] Light-based
- [ ] Screen/UI-based
- [+] Fabricated structure
- [ ] Game logic based
- [ ] Installation / tabletop experience
- [ ] Other: `[Write here]`

## 6.2 High-Level System Description
Explain how the system works in simple terms.

Include:
- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Response:** 
` The input comes from the player sitting on a chair and using their feet to press and tilt a balance board. As the board moves, ultrasonic sensors placed underneath measure the changing distance between the board and the ground. Multiple readings are taken and averaged to make the input smoother and reduce noise. `

`This data is processed by the ESP32, which checks whether the distances fall within a specific range(which is calibrated according to the height of the balance board and coded). If they do, the movement is considered intentional and mapped to corresponding actions like left, right, or jump for each player. `

`This is then converted to a signal which triggers the respective keypress on the keyboard, which is connected to the ESP32 via bluetooth. The game responds by moving the characters accordingly. Physically, the setup consists of two balance board with ultrasonic sensors mounted underneath and connected to the ESP32, creating a system where your feet directly control the gameplay, along with two chairs kept behind the balance boards.`

## 6.3 Input / Output Map

| System Part | Type | What It Does |
|---|---|---|
| `Sensor` | Input | `Measures the distance between the board and the ground to detect tilt and weight shifts` |
| `ESP32 ` | Processing | `Reads sensor data, filters/smooths it, checks for trigger conditions, and converts movements into keyboard inputs` |
| `BLE Keyboard` | Output | `Transmits the mapped inputs wirelessly as keyboard signals to the computer` |
| `Balance Board` | Physical Action | `Lets the player press and tilt the board using their feet while seated` |

---

# 7. Sketches and Visual Planning

## 7.1 Concept Sketch
Add an early sketch of the full idea.

<img src="images/odt final brainstorming.jpeg" width="400">



## 7.2 Labeled Build Sketch
Add a sketch with labels showing:
- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  
<img src="images/balanceboard construction sketches.jpeg" width="400">
<img src="images/sketches.jpeg" width="400">

## 7.3 Approximate Dimensions

| Dimension | Value |
|---|---|
| Length | `44cm` |
| Width | `44cm` |
| Height | `10cm` |
| Estimated weight | `7-8kg` |

---

# 8. Mechanical Planning

## 8.1 Mechanical Features
Check all that apply.

- [ ] Gears
- [ ] Pulleys
- [ ] Belt drives
- [ ] Linkages
- [ ] Hinges
- [ ] Shafts
- [ ] Springs
- [ ] Bearings
- [ ] Wheels
- [ ] Sliders
- [ ] Levers
- [+] Not applicable

## 8.2 Mechanical Description
Describe the mechanism and what it is meant to do.

**Response:**  
`The system uses a tilting balance board that responds to pressure from the player’s feet. The board is slightly elevated and rests on a central support, allowing it to tilt in multiple directions. When the player presses down with their feet, the board tilts towards that side.`

`Stoppers or wedges are placed around the board to limit how far it can tilt, preventing it from flipping over and ensuring controlled movement. Ultrasonic sensors are mounted underneath the board at specific positions (left, right, jump) to detect how close each side gets to the ground when tilted.`

`The goal of the mechanism is to convert small foot movements into controlled directional tilts that can be reliably detected by the sensors.`

## 8.3 Motion Planning
If something moves, explain:
- what moves,
- what causes the movement,
- how far it moves,
- how fast it moves,
- what could go wrong.

**Response:**  
`The balance board is the main moving part. It tilts based on how the player presses or shifts weight using their feet.`

`The movement is caused by downward pressure from the player’s feet, which makes one side of the board go closer to the ground. The tilt range is limited using wedges or physical stops, so the movement stays controlled and doesn’t become unstable.`

`The board moves only a few centimeters in height difference, just enough for the ultrasonic sensors to detect changes. The movement is quick and responsive, depending on how fast the player presses.`

`Possible issues include uneven tilting, sensors not detecting small movements, or the board being too sensitive or not sensitive enough. These are handled by calibrating the sensor range and adjusting the height and angle of the board.`

## 8.4 Simulation / CAD / Animation Before Making
If your project includes mechanical motion, document the digital planning before fabrication.

| Tool Used | File / Link | What Was Tested |
|---|---|---|
| `[Fusion 360 / Tinkercad / other]` | `[Link or screenshot]` | `[What did you validate?]` |
| `[Tool]` | `[Link or screenshot]` | `[What did you validate?]` |

## 8.5 Changes After Digital Testing
What changed after the CAD, animation, or simulation stage?

**Response:**  
`n/a`

---

# 9. Electronics Planning

## 9.1 Electronics Used

| Component | Quantity | Purpose |
|---|---:|---|
| `[ESP32]` | `1` | `Main controller and Bluetooth communication` |
| `Ultrasonic Sensor (HC-SR04)` | `6` | `Detect distance changes for movement input` |
| `Jumper wires` | `approximately 120` | `Connections between components` |
| `Breadboard` | `1` | `Circuit assembly` |
| `Power supply` | `1` | `Powers the ESP32` |


## 9.2 Wiring Plan
Describe the main electrical connections.

**Response:**  
`Each ultrasonic sensor is connected to the ESP32 using two pins: one for trigger and one for echo. The sensors are placed under the board in positions corresponding to left, right, and jump for each player.`

`All sensors share a common wire for power (VCC) and ground (GND).`

`The ESP32 is powered via USB and communicates with the computer through Bluetooth.`

## 9.3 Circuit Diagram
Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
<img src="images/circuit diagram.jpeg" width="400">

## 9.4 Power Plan

| Question | Response |
|---|---|
| Power source | `USB(from laptop and adapter)` |
| Voltage required | `5V` |
| Current concerns | `Multiple sensors running simultaneously may increase power draw. ` |
| Safety concerns | `Proper insulation of wires, stable mounting of components to avoid loose connections` |

---

# 10. Software Planning

## 10.1 Software Tools

| Tool / Platform | Purpose |
|---|---|
| `[MicroPython / Arduino / MIT App Inventor / CAD tool / other]` | `[Purpose]` |
| `[Tool]` | `[Purpose]` |

## 10.2 Software Logic
Describe what the code must do.

Include:
- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`When the system starts, the ESP32 initializes the Bluetooth keyboard and waits for a connection with the computer.`

`Once connected, it continuously reads distance values from all ultrasonic sensors. To reduce noise, multiple readings are taken and averaged for each sensor.`

`The system then checks whether each distance falls within a defined trigger range. If it does, that movement is considered active (left, right, or jump).`

`These active movements are mapped to corresponding keyboard inputs for Fireboy (arrow keys) and Watergirl (W, A, D). The ESP32 then sends these inputs via Bluetooth as keyboard signals.`

`This loop runs continuously, allowing real-time control of the game. If the connection drops, all inputs are reset to avoid stuck keys.`

## 10.3 Code Flowchart
Insert a flowchart showing your code logic.

Suggested sequence:
- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
`[Upload image and link here]`

## 10.4 Pseudocode

```
Start
Initialize BLE keyboard
Wait for Bluetooth connection

Loop:
    If connected:
        For each sensor:
            Read distance multiple times
            Average readings

        For each reading:
            Check if within trigger range

        Map active triggers to key inputs

        Limit to 6 keys (HID limit)

        Send key inputs via Bluetooth

    Else:
        Send no input (reset keys)

    Small delay
Repeat
```

---

# 11. MIT App Inventor Plan

## 11.1 Is an app part of this project?
- [ ] Yes
- [+] No

If yes, complete this section.

## 11.2 Why is the app needed?
Explain what the app adds to the experience.

Examples:
- remote control,
- score tracking,
- mode selection,
- personalization,
- triggering effects,
- displaying data.

**Response:**  
`[Write here]`

## 11.3 App Features

| Feature | Purpose |
|---|---|
| `[Bluetooth connect button]` | `[Purpose]` |
| `[Score display]` | `[Purpose]` |
| `[Control button / slider / label]` | `[Purpose]` |

## 11.4 UI Mockup
Insert a sketch or screenshot of the app interface.

**Insert image below:**  
`[Upload image and link here]`

## 11.5 App Screen Flow

1. `[Step 1]`
2. `[Step 2]`
3. `[Step 3]`
4. `[Step 4]`

---

# 12. Bill of Materials

## 12.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
|---|---:|---|---|---:|---|---|
| `[ESP32]` | `1` | `Yes` | `No` | `0` | `[Spec]` | `Controller` |
| `Ultrasonic Sensors` | `6` | `1 yes 5 no` | `No(borrowed)` | `-` | `[Spec]` | `Sensor` |
| `Jumper wires` | `Apprx 120` | `Yes` | `Yes` | `300` | `[Spec]` | `We needed to make our wires long so that moving the balance board won't move the breadboard along with it` |
 `Electonic Insulation Tape` | `2` | `No` | `200` | `-` | `[Spec]` | `Stick wires together and on the board` |

## 12.2 Material Justification
Explain why you selected your main materials and components.

Examples:
- Why acrylic instead of cardboard?
- Why MDF instead of 3D print?
- Why servo instead of DC motor?
- Why bearing instead of a plain shaft hole?

**Response:**  
`- We used HDF and plywood instead of cardboard, MDF or 3D print due to its size and its need to be strong and sturdy.`
`- We used ultrasonic sensors instead of conductive touch sensors made of aluminium foil because the foil would have torn due to excessive hitting. `
`- We used MDF for the wedges instead of wood or cardboard because we needed a sturdy but easy to handle material.`

## 12.3 Items to Purchase Separately

| Item | Why Needed | Purchase Link | Latest Safe Date to Procure | Status |
|---|---|---|---|---|
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |
| `[Item]` | `[Reason]` | `[Link]` | `[Date]` | `[Pending / Ordered / Received]` |

## 12.4 Budget Summary

| Budget Item | Estimated Cost |
|---|---:|
| Electronics | `500` |
| Mechanical parts | `[Cost]` |
| Fabrication materials | `[Cost]` |
| Purchased extras | `[Cost]` |
| Contingency | `[Cost]` |
| **Total** | `500` |

## 12.5 Budget Reflection
If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  
`After buying the wires, we realised there was a surplus of jumper wires. We could have calculated the exact number of wires and gotten just a few more just in case. Although individual jumper wires are not very expensive. Juat a little prior planning could have saved some money.`

---

# 13. Planning the Work

## 13.1 Team Working Agreement
Write how your team will work together.

Include:
- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  
`[Write here]`

## 13.2 Task Breakdown

| Task ID | Task | Owner | Estimated Hours | Deadline | Dependency | Status |
|---|---|---|---:|---|---|---|
| T1 | `[Finalize concept]` | `[Name]` | `2` | `[Date]` | `None` | `To Do` |
| T2 | `[Complete BOM]` | `[Name]` | `1` | `[Date]` | `T1` | `To Do` |
| T3 | `[Test electronics]` | `[Name]` | `2` | `[Date]` | `T1` | `To Do` |
| T4 | `[Build structure]` | `[Name]` | `4` | `[Date]` | `T1` | `To Do` |
| T5 | `[Write control code]` | `[Name]` | `4` | `[Date]` | `T3` | `To Do` |
| T6 | `[Integrate system]` | `[Name]` | `4` | `[Date]` | `T4, T5` | `To Do` |
| T7 | `[Playtest]` | `[Name]` | `2` | `[Date]` | `T6` | `To Do` |
| T8 | `[Refine and document]` | `[Name]` | `3` | `[Date]` | `T7` | `To Do` |

## 13.3 Responsibility Split

| Area | Main Owner | Support Owner |
|---|---|---|
| Concept and gameplay | `[Name]` | `[Name]` |
| Electronics | `[Name]` | `[Name]` |
| Coding | `[Name]` | `[Name]` |
| App | `[Name]` | `[Name]` |
| Mechanical build | `[Name]` | `[Name]` |
| Testing | `[Name]` | `[Name]` |
| Documentation | `[Name]` | `[Name]` |

---

# 14. Weekly Milestones

## 14.1 Four-Week Plan

### Week 1 — Plan and De-risk
Expected outcomes:
- [ ] Idea finalized
- [ ] Core interaction decided
- [ ] Sketches made
- [ ] BOM completed
- [ ] Purchase needs identified
- [ ] Key uncertainty identified
- [ ] Basic feasibility tested

### Week 2 — Build Subsystems
Expected outcomes:
- [ ] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [ ] Mechanical concept tested
- [ ] Main subsystems partially working

### Week 3 — Integrate
Expected outcomes:
- [ ] Physical body built
- [ ] Electronics integrated
- [ ] Code connected to hardware
- [ ] App connected if required
- [ ] First playable version exists

### Week 4 — Refine and Finish
Expected outcomes:
- [ ] Technical bugs reduced
- [ ] Playtesting completed
- [ ] Improvements made
- [ ] Documentation completed
- [ ] Final build ready

## 14.2 Weekly Update Log

| Week | Planned Goal | What Actually Happened | What Changed | Next Steps |
|---|---|---|---|---|
| Week 1 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 2 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 3 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |
| Week 4 | `[Write here]` | `[Write here]` | `[Write here]` | `[Write here]` |

---

# 15. Risks and Unknowns

## 15.1 Risk Register

| Risk | Type | Likelihood | Impact | Mitigation Plan | Owner |
|---|---|---|---|---|---|
| `[Example: Bluetooth disconnects]` | `Technical` | `Medium` | `High` | `[Fallback interaction / simplify connection flow]` | `[Name]` |
| `[Example: Structure breaks during play]` | `Mechanical` | `Medium` | `High` | `[Reinforce joints / change material]` | `[Name]` |
| `[Risk]` | `[Technical / Material / Time / Gameplay]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |
| `[Risk]` | `[Type]` | `[Low/Medium/High]` | `[Low/Medium/High]` | `[Plan]` | `[Name]` |

## 15.2 Biggest Unknown Right Now
What is the single biggest uncertainty in your project at this stage?

**Response:**  
`Ensuring that the sensors reliably detect small foot movements without being too sensitive or too unresponsive. Finding the right balance between accuracy and playability is the main challenge.`

---

# 16. Testing and Playtesting

## 16.1 Technical Testing Plan

| What Needs Testing | How You Will Test It | Success Condition |
|---|---|---|
| `Bluetooth connection` | `Connect ESP32 to laptop multiple times` | `Stable connection without frequent drops` |
| `Sensor behavior` | `Move board manually and observe readings` | `Consistent and accurate distance values` |
| `Input response` | `Play the game using the board` | `Character responds correctly to movement` |
| `Mechanism` | `First prototype with cardboard` | `The character moves according to the tilt` |

## 16.2 Playtesting Plan

| Question | How You Will Check |
|---|---|
| Do players understand what to do? | `Let new players try without instructions first and observe if they figure out movement on their own` |
| Is the interaction satisfying? | `Ask players how it felt after playing and observe their reactions (frustration vs enjoyment)` |
| Do players want another turn? | `See if they voluntarily ask to replay or continue playing after one round` |
| Is the challenge balanced? | `Observe if players struggle too much or get through too easily, and ask for feedback` |
| Is the response clear and immediate? | `Check if players notice a direct connection between their foot movement and character movement` |

## 16.3 Testing and Debugging Log

| Date | Problem Found | Type | What You Tried | Result | Next Action |
|---|---|---|---|---|---|
| `[Date]` | `[Describe issue]` | `[Technical / Mechanical / UI / Gameplay]` | `[What you did]` | `[Worked / Partly / Failed]` | `[Next step]` |
| `[Date]` | `[Describe issue]` | `[Type]` | `[What you did]` | `[Result]` | `[Next step]` |

## 16.4 Playtesting Notes

| Tester | What They Did | What Confused Them | What They Enjoyed | What You Will Change |
|---|---|---|---|---|
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |
| `[Peer / friend / classmate]` | `[Observation]` | `[Observation]` | `[Observation]` | `[Action]` |

---

# 17. Build Documentation

## 17.1 Fabrication Process
Describe how the project was physically made.

Include:
- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`Materials Used: `
`- HDF (High-Density Fibreboard): Lower hemisphere/dome`
`- Plywood: Top circular platform`
`- MDF (Medium-Density Fibreboard): Wedges`
`- Sunboard: Base for wedges`
`- Adhesives: Wood glue, Fevibond, hot glue`
`- Tapes: Masking tape, insulating electrical tape`

`The process began with constructing the dome of our balanceboard. Five circular layers of increasing sizes were drawn onto HDF and cut using an electric saw and band saw. These layers were then trimmed into a rough polygonal form by removing excess material. Once prepared, the layers were carefully aligned, glued together using wood glue and clamped to dry. To achieve the final curved shape, two different approaches were used. For one dome, a lathe machine was used, with an additional cuboid wooden block attached to act as a grip while turning. For the other, the curvature was achieved manually by sanding down the edges using a sanding machine until a smooth, rounded form was obtained.`

`The top circular platform was cut from plywood using the band saw and then sanded to ensure a clean finish. It was attached to the flat side of the dome using wood glue, and the piece was flipped upside down during drying so that gravity would help secure the bond more effectively.`

`The wedges were made from MDF by cutting them on the band saw and then sanding their edges to approximately 45-degree angles. These pieces were assembled using wood glue and temporarily held in place with masking tape while drying. Once completed, the wedges were mounted onto a foamboard base using a combination of hot glue and Fevibond to ensure they remained fixed in position.`

`For the wiring, wires were cut and stripped using a wire cutter and stripper, then connected and secured using insulating electrical tape. Masking tape was additionally used to organise and hold the wires in place on the structure.`

`The finishing process involved sanding all wooden components to remove sharp edges and refine the surfaces, particularly the dome, to ensure smooth contact and usability.`

`A key revision in the process involved rethinking the wedge design. Initially, the wedges were oriented at a 90-degree angle; however, this did not provide sufficient grip. By flipping the wedges upside down, the effective angle increased, resulting in better stability and improved user interaction with the balance board.`

## 17.2 Build Photos
Add photos throughout the project.

Suggested images:
- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.
- 
<img src="images/prototyping.jpeg" width="400">
<img src="images/ultrasonic sensor trial.jpeg" width="400">
<img src="images/balanceboard construction 1.jpeg" width="400">
<img src="images/balanceboard construction 2.jpeg" width="400">
<img src="images/balanceboard construction 4.jpeg" width="400">
<img src="images/balanceboard construction 5.jpeg" width="400">
<img src="images/final circuit.jpeg" width="400">
<img src="images/final circuit 2.jpeg" width="400">
<img src="images/final balanceboard.jpeg" width="400">
<img src="images/side view.jpeg" width="400">
<img src="imagesbase + wedges.jpeg" width="400">
<img src="images/set up.jpeg" width="400">
<img src="images/set up 1.jpeg" width="400">
<img src="images/set up 2.jpeg" width="400">
<img src="images/set up 3.jpeg" width="400">

```

## 17.3 Version History

| Version | Date | What Changed | Why |
|---|---|---|---|
| `v1` | `` | `Touch sensor with jumper wires` | `The game needed long press, and combined controls` |
| `v2` | `[Date]` | `Touch sensor with aluminium foil` | `A control mat isn't very intuitive so we wanted to explore other control structures. Also the aluminium foil is triggering the touch sensor` |
| `v3` | `[Date]` | `Try using ultrasonic sensor with cardboard model` | `Prototyping to see if the mechanism worked` |
| `v4` | `[Date]` | `Ultrasonic sensor with actual model` | `Worked`|


---

# 18. Final Outcome

## 18.1 Final Description
Describe the final version of your project.

**Response:**  
`[The final version of our project is a seated, foot-controlled balance board system that allows two players to control Fireboy and Watergirl using physical movement instead of a keyboard. Each player sits on a chair and uses their feet to tilt a balance board placed on the ground.`

`Ultrasonic sensors mounted underneath the board detect changes in distance as the board tilts in different directions (left, right, and jump). These inputs are processed by an ESP32, which converts them into keyboard signals and sends them to the computer via Bluetooth.`

`This setup creates a more stable and controlled interaction compared to standing, while still maintaining a playful and physical gameplay experience. The result is an engaging system where players use coordination and timing with their feet to navigate the game.]`

## 18.2 What Works Well
- `[The ultrasonic sensors reliably detect tilt and reduce false triggering compared to earlier touch-based methods.]`
- `[The sensors also work well simultaneously, allowing the player to move 2 directions at the same time.]`
- `[The Bluetooth keyboard output successfully maps movements to in-game controls with minimal delay]`

## 18.3 What Still Needs Improvement
- `[Sensitivity calibration can be further refined for smoother and more precise control, especially for one of the characters.]`
- `[The physical balance board can be re-shaped and refined for better consistency and intuitive gameplay.]`
- `[Occasional sensor noise at very close distances still affects accuracy slightly]`

## 18.4 What Changed From the Original Plan
How did the project change from the initial idea?

**Response:**  
`[Initially, the project was designed as a standing balance board where players would control the game using full-body movement. However, during testing, this approach proved unstable and difficult to control, leading to inconsistent sensor readings and gameplay issues.`

`We also experimented with capacitive touch (touch sensors) using aluminium foil, but it resulted in false triggers and unreliable input due to interference and wiring limitations.`

`Based on these challenges, we pivoted to a seated interaction model, where players control the board using their feet. We also switched to ultrasonic sensors, which provided more stable and accurate input detection.`

---

# 19. Reflection

## 19.1 Team Reflection
What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  
`[Write here]`

## 19.2 Technical Reflection
What did you learn about:
- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  
`[Write here]`

## 19.3 Design Reflection
What did you learn about:
- designing for play,
- delight,
- clarity,
- physical interaction,
- player understanding,
- iteration?

**Response:**  
`[Write here]`

## 19.4 If You Had One More Week
What would you improve next?

**Response:**  
`[If we had one more week, we would focus on improving the usability of the balance board. In its current form, it felt more like a balancing challenge rather than an intuitive game controller, which led us to shift to a seated playing version. To address this, we would refine the shape of the dome by making it wider and shorter to improve stability. We would also increase the size of the standing platform to provide better support and comfort for the user. Additionally, we would redesign the base support system, replacing the wedge setup with a more stable and reliable structure to enhance overall control and ease of use.]`

---

# 20. Final Submission Checklist

Before submission, confirm that:
- [ ] Team details are complete
- [ ] Project description is complete
- [ ] Inspiration sources are included
- [ ] Player journey is written
- [ ] Sketches are added
- [ ] BOM is complete
- [ ] Purchase list is complete
- [ ] Budget summary is complete
- [ ] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [ ] Code flowchart is added
- [ ] Task breakdown is complete
- [ ] Weekly logs are updated
- [ ] Risk register is complete
- [ ] Testing log is updated
- [ ] Playtesting notes are included
- [ ] Build photos are included
- [ ] Final reflection is written

---

# 21. Suggested Repository Structure

```text
project-repo/
├── README.md
├── images/
│   ├── concept-sketch.jpg
│   ├── labeled-sketch.jpg
│   ├── circuit-diagram.jpg
│   ├── ui-mockup.jpg
│   ├── prototype-1.jpg
│   └── final-build.jpg
├── code/
│   ├── main.py
│   ├── test_code.py
│   └── notes.md
├── cad/
│   ├── models/
│   └── screenshots/
└── docs/
    ├── references.md
    └── extra-notes.md
```

---

# 22. Instructor Review

## 22.1 Proposal Approval
- [ ] Approved to proceed
- [ ] Approved with changes
- [ ] Rework required before proceeding

**Instructor comments:**  
`[Instructor fills this section]`

## 22.2 Midpoint Review
`[Instructor fills this section]`

## 22.3 Final Review Notes
`[Instructor fills this section]`
