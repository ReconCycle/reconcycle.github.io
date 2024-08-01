# Skills

## Overview

Commonly used robot (or peripheral machine) operations/[skills](https://github.com/ReconCycle/disassembly_toolkit/tree/main/disassembly_pipeline/skills) are encapsulated within Skill classes, so they can be easily used either stand-alone or within a FlexBe state. An [abstract base skill](https://github.com/ReconCycle/disassembly_toolkit/blob/main/disassembly_pipeline/skills/base_skill.py) is also defined.

Common guidelines for developing skills are:

1. Skills should accept robot/peripheral objects as inputs, and only optionally instantiate them if not provided
2. Skills should make minimal assumptions about environment state
3. Skills should prefer to take as input the Vision system's Detection objects
4. Higher-level skills may include execution of several primitive skills (e.g. the Move skill consists of Pick-up and Drop skills)

## Available skills
The list of available skills, their descriptions and input arguments is below:

### Pick-up

### Drop

### Move

### Lever

### CNC cut
